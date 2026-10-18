# Sharp growth of 3-abelian singleton words over every alphabet

## Finding

For a fixed alphabet \(\Sigma=\{0,1,\ldots,q-1\}\) with \(q\geq2\), words are **3-abelian equivalent** if every contiguous factor of length at most three has the same number of occurrences in both words. A word is a **3-abelian singleton** when no different word is equivalent to it. Let \(S_{3,q}(n)\) be the number of singleton words of length \(n\). Put
\[
R=\frac{q(q+1)}2,\qquad H=\binom q2,\qquad n_0=2q^2-q+2.
\]
Then, as \(n\to\infty\) with \(q\) fixed,
\[
\boxed{S_{3,q}(n)=\Theta_q\!\left(n^{R-1}\right)}.
\]
More precisely, there is an explicitly defined family \(\mathcal W_q\) of pairwise distinct 3-abelian singleton words whose length enumerator is exactly
\[
\boxed{\sum_{w\in\mathcal W_q}z^{|w|}=\frac{z^{n_0}}{(1-z)^q(1-z^2)^H}}.
\]
Consequently, the number of members of this family of length \(n\) is
\[
\frac{n^{R-1}}{2^H(R-1)!}+O_q(n^{R-2}).
\]
The exponent matches the upper bound in the 2016 work of Karhumäki, Puzynina, Rao and Whiteland. This establishes the fixed-factor-length-three case of their proposed sharp-growth principle for every fixed alphabet size.

## Assumptions and scope

All alphabets are **labeled** and fixed while the word length tends to infinity; the symbols need no group structure. Factors are contiguous and overlapping occurrences count separately. A singleton is counted once, not up to renaming or rotation. The enumeration displayed is of an explicit **subfamily** of singletons, not all singleton words. The theorem does not assert that the displayed generating function is the generating function of all singleton words.

The directed order-two de Bruijn graph has vertices \(ab\in\Sigma^2\) and a labeled edge \(ab\longrightarrow bc\) for each triple \(abc\in\Sigma^3\). Its vertices partition into the \(q\) singleton cycles \(aa\) and the \(H\) two-cycles \(ab\leftrightarrow ba\) for \(a\ne b\). We call these the length-two necklace cycles.

## Proof

**1. An ordered complete cycle decomposition.** List the necklace cycles in the following precise order: first \((0,0)\), followed by the two-cycles \(\{(0,j),(j,0)\}\) for \(j=1,\ldots,q-1\). Then, for each pivot \(p=q-1,q-2,\ldots,1\), list its singleton \((p,p)\) followed by the two-cycles \(\{(j,p),(p,j)\}\) for \(j=1,\ldots,p-1\). Every two-cycle occurs exactly once: pairs containing zero occur first, and every remaining unordered pair is listed at its larger positive endpoint. Every singleton occurs once. Thus the list contains exactly \(R\) cycles and covers all \(q^2\) vertices.

Consecutive cycles share a symbol; indeed, within each pivot star all pairs contain its pivot, while the last pair in the star contains the pivot of the next singleton. If adjacent cycles share symbol \(s\), there is a directed de Bruijn connector from a vertex ending in \(s\) in the first cycle to a vertex beginning in \(s\) in the next. This connector is an edge labeled by a triple. Its endpoints lie in different necklace cycles. Choose that connector once and for all; since consecutive distinct classes share exactly one symbol, its endpoints are uniquely specified here. Denote by \(u_i\) the entry state of cycle \(i\) (initially \(00\)) and by \(v_i\) its exit state (finally the singleton \(11\)). Let \(\ell_i\in\{1,2\}\) be the cycle length and \(\delta_i\in\{0,1\}\) the forward cycle distance from \(u_i\) to \(v_i\). At intermediate pairs of a fixed star this distance is one; it is zero at singleton cycles and at each final pair immediately preceding the next singleton. Thus
\[
\sum_{i=1}^R\delta_i=\sum_{p=2}^{q-1}(p-2)+(q-2)=\binom{q-1}{2}.
\]
For \(q=2\) the sum is empty and is zero.

**2. A family of unique trails.** For each vector \((t_1,\ldots,t_R)\) of arbitrary positive integers, begin at state \(00\). In cycle \(i\), follow its fixed directed cycle for \(\delta_i+\ell_i t_i\) edges, reaching \(v_i\), then take its single connector into the next cycle, and repeat; stop after the final cycle. Reading the initial two symbols and then the last symbol of each traversed edge gives a unique word. All its length-three factor multiplicities are exactly those of the directed multigraph consisting of \(t_i\) copies of every edge on cycle \(i\), the \(\delta_i\) additional cycle edges on the entry-to-exit arc, and the \(R-1\) one-way connectors.

Fix these multiplicities and the initial two-symbol prefix. Any equivalent word has the same triple multiplicities and the same first two symbols: this is the usual length-three factor-count characterization, which also follows immediately by subtracting shorter factor counts along de Bruijn paths. It must therefore give an Euler trail of the same labeled-edge multigraph starting at \(00\). A connector leaves one necklace cycle and enters the next; there are no backward connectors. Any trail traversing all edges must exhaust every edge within a cycle before using its unique exit connector, since that cycle is never revisited afterward. Within a necklace cycle each vertex has exactly one internal successor, so the order of its internal traversals is forced, including the required final vertex. The resulting symbol sequence is therefore unique. Every constructed word is a 3-abelian singleton. Distinct vectors have distinct triple multiplicities on their individual cycles, so their constructed words are pairwise different.

**3. Enumeration.** The word has two initial symbols, \(R-1\) connector edges, and \(\sum_i(\delta_i+\ell_i t_i)\) cycle edges. Exactly \(q\) cycles have length one and \(H\) have length two; moreover, \(\sum_i\ell_i=q^2\). Hence its minimum length (all \(t_i=1\)) is
\[
2+(R-1)+\binom{q-1}2+q^2=2q^2-q+2=n_0.
\]
Each additional traversal of a singleton cycle adds one letter; each additional traversal of a two-cycle adds two. The map from the parameter vectors to singleton words is injective, yielding exactly
\[
\sum_{w\in\mathcal W_q}z^{|w|}=\frac{z^{n_0}}{(1-z)^q(1-z^2)^H}.
\]
Near \(z=1\), the right side has leading singularity \(2^{-H}(1-z)^{-R}\). The only other pole on the unit circle is \(z=-1\), of order \(H<R\). Partial fractions therefore give the stated coefficient asymptotic. In particular, the family contains at least a positive multiple of \(n^{R-1}\) words for all sufficiently large lengths \(n\).

**4. Matching upper bound.** Theorem 6.1 of Karhumäki, Puzynina, Rao and Whiteland [1] gives \(S_{k,q}(n)=O_{k,q}(n^{N_q(k-1)-1})\), where \(N_q(2)=\tfrac12(q^2+q)=R\) counts length-two necklaces. Substituting \(k=3\) and combining with the lower bound proves the claimed \(\Theta_q\) formula. No unproved general-\(k\) conjecture is used in this inference.

## Verification

The accompanying standalone `verify.py` enumerates the necklace-cycle chain for \(2\le q\le7\), checks full cycle coverage, consecutive connectors, the exact baseline lengths, and the forward-cycle offsets. For \(2\le q\le4\) it separately counts Euler trails in the resulting triple-count multigraph, checking uniqueness for each base construction and three parameter perturbations. For binary words through length fifteen it exhaustively builds all words, groups them by initial two-symbol prefix and triple-factor multiset, and confirms that every constructed word in that finite range has singleton class size one. The verifier prints `ALL_CHECKS_PASS`. These are finite checks supporting, but not replacing, the general graph proof.

For example, the family enumerators begin with \(z^8/((1-z)^2(1-z^2))\) for \(q=2\) and \(z^{17}/((1-z)^3(1-z^2)^3)\) for \(q=3\); their initial coefficient vectors, from the respective baseline lengths, are \((1,2,4,6,9,12)\) and \((1,3,9,19,39,69)\).

## Relationship to prior work

Karhumäki, Puzynina, Rao and Whiteland [1] proved the universal singleton upper bound, established a cycle-structure method, and formulated its sharpness as Conjecture 7.8. Their methods supply the upper bound used here but do not give the explicit all-alphabet length-three Hamiltonian necklace-cycle chain or its enumerator. The present result fills exactly that all-alphabet, fixed \(k=3\) case; it does not purport to resolve arbitrary \(k\).

A published CIRM presentation [2] describes the same general singleton-growth conjecture, with a verified public date before the 2016 arXiv version. Later papers on rationality and regularity of equivalence classes [3,4] concern related counting languages and fixed cardinality; the available material does not establish the particular all-alphabet exponent via the explicit construction here. Earlier binary-necklace Gray-code work [5] does not imply this stated all-alphabet length-two path and count without an additional argument.

## Limitations

The generating function enumerates only this constructed subfamily; no formula is claimed for the total number of 3-abelian singleton words. The positive leading constant is a lower-bound coefficient, not necessarily the asymptotic leading constant for \(S_{3,q}(n)\). The sharp-growth result treats fixed alphabet size and factor length exactly three. It does not establish Conjecture 7.8 for larger factor lengths. The 2017 rationality article and the 2018 fixed-cardinality article could not be completely inspected through the available accessible copies; a prior implicit proof cannot be absolutely excluded. Mathematical priority requires independent literature assessment.

## References

1. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319v1 (first posted 2016-05-11), especially Lemma 2.4, Theorem 6.1, Remark 6.6 and Conjecture 7.8. https://arxiv.org/abs/1605.03319
2. M. A. Whiteland, *k-abelian singletons and Gray codes for Necklaces*, CIRM recorded lecture, published 2016-03-31, DOI:10.24350/CIRM.V.18946003. https://www.carmin.tv/fr/collections/exposes-de-recherche/video/k-abelian-singletons-and-gray-codes-for-necklaces
3. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *k-Abelian Equivalence and Rationality*, Fundamenta Informaticae **154** (2017), 65–94, DOI:10.3233/FI-2017-1553.
4. J. Karhumäki, M. A. Whiteland, *Regularity of k-Abelian Equivalence Classes of Fixed Cardinality*, Lecture Notes in Computer Science **11011** (2018), 49–62, DOI:10.1007/978-3-319-98355-4_4.
5. C. Degni, A. A. Drisko, *Gray-ordered Binary Necklaces*, Electronic Journal of Combinatorics **14** (2007), #R7, DOI:10.37236/926.
