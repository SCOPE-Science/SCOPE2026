# A local noncrossing criterion for genus-zero tree-transposition words

## Finding

**Theorem (all finite trees).** Let \(T=(V,E)\) be a finite simple tree with \(n=|V|\ge2\) and \(m=n-1\). Associate with each edge \(e=\{u,v\}\) the transposition \(\tau_e=(u\ v)\) of the vertex set. Let \(w=(e_1,\ldots,e_{2m})\) be an ordered word of length \(2m\) in the edges of \(T\) which uses **every edge at least once**. Then

\[
\tau_{e_1}\tau_{e_2}\cdots\tau_{e_{2m}}=\mathrm{id}
\]

if and only if (a) every edge occurs exactly twice and (b) no pair of distinct edges sharing a vertex has alternating occurrences in \(w\). Condition (b) means precisely that the four occurrences of each such pair do not appear as \(e,f,e,f\) or \(f,e,f,e\) (possibly with other letters interspersed). Equivalently, at each vertex, the subword of incident edges is a noncrossing double-occurrence word.

This proves the tree criterion stated as Conjecture 1(iii) in the cited 2026 transposition-Cayley paper, for every tree order. It also yields a recognition procedure using positions of the two occurrences of each edge and testing crossing only for incident pairs.

## Assumptions and scope

Trees are undirected, simple and finite. Permutation multiplication may be read in either consistent composition convention: a product is the identity in one convention exactly when the reversed product is the identity in the other, and chord crossing is invariant under word reversal. The full-support condition is essential. The length is fixed at \(2(n-1)\), the minimal length of a transitive identity factorization into transpositions.

The theorem is a structural criterion, not a new closed counting formula for arbitrary trees. It makes the conjectured local constraint both necessary and sufficient. For a star it recovers the *previously known* Catalan count \(m!\operatorname{Cat}_m=(2m)!/(m+1)!\); the star enumerator itself is not claimed as new.

## Proof

**Lemma 1 (a bridge cannot appear once).** Suppose a word in edges of a tree has identity product. For any edge \(e=\{a,b\}\), removal of \(e\) separates the tree into vertex sets \(A,B\). Every transposition other than \(\tau_e\) belongs to the subgroup \(H=S_A\times S_B\). Were \(e\) to occur exactly once, the product would have the form \(U\tau_eV\) with \(U,V\in H\). This lies outside \(H\), since \(\tau_e\notin H\), so it cannot equal the identity. For a full-support identity word of length \(2m\) every one of the \(m\) edges consequently occurs at least twice, hence exactly twice.

**Lemma 2 (fixed-point test for factors of locally noncrossing words).** Let \(R\) be any tree. Let \(W\) be a word in its edges, each appearing exactly twice, with no alternating occurrences of adjacent edges. For any contiguous subword \(V\) of \(W\), the permutation represented by \(V\) fixes a vertex \(b\) if and only if every edge incident to \(b\) occurs an even number of times in \(V\).

*Proof of Lemma 2.* In \(V\), choose an edge \(f\) with both occurrences present and with the smallest distance between its occurrences. An edge \(g\) incident to \(f\) cannot occur exactly once between those occurrences, because that would alternate \(f,g\) in \(W\). If it occurred twice there, its two positions would form a strictly shorter complete pair in \(V\), contradicting minimality. Therefore every edge between the two occurrences of \(f\) is disjoint from \(f\), and its transposition commutes with \(\tau_f\). Thus those two copies of \(\tau_f\) can be brought together and canceled. Delete them. The remaining word is still a factor of a double-occurrence word obtained from \(W\) by removing a complete pair; the local noncrossing property is preserved. Repeating terminates with a word containing each surviving edge exactly once. Its surviving edges are precisely those with odd multiplicity in the original \(V\).

The surviving edges form a forest. For any ordering of pairwise distinct transpositions corresponding to forest edges, the cycles of their permutation product are exactly the vertex sets of the connected components of that forest, singleton vertices included: each successive edge joins distinct components of previously used edges and therefore merges two permutation cycles. Hence \(b\) is fixed exactly when no surviving edge is incident to \(b\), as required. \(\square\)

**Inductive proof of the theorem.** The tree with one edge is immediate. Assume the theorem for every smaller tree and fix a leaf \(a\) with neighbour \(b\) and incident edge \(e=\{a,b\}\). Under condition (a) write the word uniquely as

\[
w=U\,e\,V\,e\,W,
\]

where \(U,V,W\) contain no \(e\). Removing both copies of \(e\) gives the word \(w'=UVW\) on the smaller tree \(T-a\), with every remaining edge appearing twice.

*Necessity.* Suppose the original product is the identity. Every transposition in \(U,V,W\) fixes \(a\). Thus \(\tau_e\,P(V)\,\tau_e=P(U)^{-1}P(W)^{-1}\) fixes \(a\), where \(P\) is the permutation product. Applying the left side to \(a\) shows \(P(V)(b)=b\). As \(P(V)\) fixes both \(a\) and \(b\), it commutes with \(\tau_e\), so \(P(w')=P(w)=\mathrm{id}\). The induction hypothesis makes \(w'\) locally noncrossing. Lemma 2, applied to its contiguous factor \(V\), says that every edge incident to \(b\) occurs either zero or two times in \(V\). Hence none has a single occurrence between the copies of \(e\), so no edge adjacent to \(e\) alternates with \(e\). All other adjacent pairs are noncrossing by induction. Therefore \(w\) satisfies (b).

*Sufficiency.* Suppose (a) and (b) hold. The reduced word \(w'\) remains locally noncrossing, so by induction \(P(w')=\mathrm{id}\). By noncrossing of \(e\) with its neighbouring edges, each edge incident to \(b\) occurs zero or twice in \(V\). Lemma 2 gives \(P(V)(b)=b\). Since \(P(V)\) also fixes the leaf \(a\), it commutes with \(\tau_e\). Thus \(P(w)=P(U)\tau_eP(V)\tau_eP(W)=P(U)P(V)P(W)=P(w')=\mathrm{id}\). This completes the induction. \(\square\)

## Verification

The standard-library Python program `artifacts/verify.py` constructs independent predicates for the permutation product and the alternating-interval criterion, then exhaustively tests every double-occurrence word on 13 explicitly specified trees with up to five edges (all six unlabeled six-vertex tree shapes among them). It checks 688,147 words in total and compares the resulting identity counts with the values in the motivating paper, including \(42\) for the four-vertex path, \(30\) for the claw, and \(25{,}520\) for the six-vertex path. It additionally tests the fixed-point characterization for every contiguous factor of 347 selected locally noncrossing words, and tests 30,000 randomly shuffled words on longer path and star trees with six to eight edges. Execution produced `VERIFY_OK`, recorded in `artifacts/verification_output.txt`.

The finite program is a regression check only. Lemmas 1–2 and the leaf-induction argument establish the all-order statement; no extrapolation, numerical rank estimate or unavailable computation is used in the proof.

## Relationship to prior work

Boris Shapiro, *Transposition Cayley Spectra and Subgraph Counts*, arXiv:2610.14373v1 (first posted 9 October 2026), §4.1, Conjecture 1(iii), states exactly the local-noncrossing characterization as conjectural and reports checks through five tree edges. Its Theorem 1 already defines the support coefficients \(c_k(F)\); the general coefficient formalism is not new here. The proof above resolves the explicitly stated tree-word characterization and extends it to every finite tree, without asserting a universal closed formula for \(c_{2m}(T)\).

Cordelia Yuqiao Li and Ricky Ini Liu, *Minimal transitive factorizations supported on quasi-threshold graphs*, arXiv:2609.31982v1 (25 September 2026), count supported minimal transitive factorizations using weighted factorization trees on a different graph class. Theorems 1.1 and 4.9 address total enumeration on quasi-threshold support graphs, not the word-by-word local criterion for arbitrary tree supports. Earlier star-factorization formulas of Irving and Rattan already cover the star counting case. General bijections between minimal transitive factorizations and planar combinatorial maps are acknowledged as potential sources of equivalent reformulations.

## Limitations

The theorem requires both a tree support and the minimal full-support word length. It does not claim the stated criterion for graphs containing cycles, or for identity words of greater length. It does not provide an all-tree product formula for the coefficient count. An equivalent criterion might exist in older Hurwitz-map or Coxeter-word literature under different language; this remains a bibliographic priority risk. No independent audit has been performed.

## References

1. B. Shapiro, *Transposition Cayley Spectra and Subgraph Counts*, arXiv:2610.14373v1, 9 October 2026, https://arxiv.org/html/2610.14373v1 (especially Conjecture 1(iii) and §4.1).
2. C. Y. Li and R. I. Liu, *Minimal transitive factorizations supported on quasi-threshold graphs*, arXiv:2609.31982v1, 25 September 2026, https://arxiv.org/abs/2609.31982 (especially Theorem 4.9).
3. J. Irving and A. Rattan, *Minimal factorizations of permutations into star transpositions*, Discrete Mathematics 309 (2009), 1435–1442; https://arxiv.org/abs/math/0610640.
4. I. P. Goulden and D. M. Jackson, *Transitive factorisations into transpositions and holomorphic mappings on the sphere*, Proceedings of the American Mathematical Society 125 (1997), 51–60 (background on genus-zero transposition factorizations).
