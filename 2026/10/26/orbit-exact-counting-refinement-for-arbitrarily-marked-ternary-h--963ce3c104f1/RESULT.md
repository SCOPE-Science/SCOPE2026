# Orbit-exact counting refinement for arbitrarily marked ternary Hamming graphs

## Finding

**Theorem.** Let \(d\ge1\), let \(H(d,3)\) be the simple graph on \(\{0,1,2\}^d\) with adjacency at Hamming distance one, and let \(s_1,\ldots,s_r\) be any ordered list of \(1\le r\le3^d\) **distinct** vertices. Initially colour each \(s_i\) individually and give every unmarked vertex the same colour. Use synchronous ordinary one-dimensional counting colour refinement, retaining old colours at every round.

For a coordinate \(j\), write \(\pi_j\) for the partition of \([r]\) whose blocks are the nonempty sets \(\{i:(s_i)_j=a\}\) as \(a\) runs over the three symbols. For each partition \(\pi\) of \([r]\) into at most three blocks, put \(n_\pi=|\{j:\pi_j=\pi\}|\). Given a vertex \(x\), and a coordinate \(j\) of type \(\pi\), its *status* is the unique block \(B\in\pi\) for which \(x_j=(s_i)_j\) for all \(i\in B\), or the empty status \(\varnothing\) if \(x_j\) equals no marked symbol at that coordinate. Only when \(|\pi|<3\) can the empty status occur. Let \(c_{\pi,B}(x)\) count coordinates of type \(\pi\) and status \(B\).

Two vertices have the same stable refinement colour **if and only if** all their counts \(c_{\pi,B}\) agree. Equivalently, the stable colour partition is precisely the orbit partition of the pointwise stabilizer of \(s_1,\ldots,s_r\) in \(\operatorname{Aut}(H(d,3))\). This partition is attained after at most \(d+1\) refinement rounds.

The exact number of stable classes is
\[
\boxed{(n_{\{[r]\}}+1)\prod_{\substack{\pi\vdash[r]\\2\le|\pi|\le3}}\binom{n_\pi+2}{2}.}
\]
Here \(\{[r]\}\) denotes the unique one-block partition, and all absent coordinate types have multiplicity zero. A class specified by counts \(c_{\pi,B}\) has cardinality
\[
\boxed{\prod_{\pi}\frac{n_\pi!}{\prod_{B\in\pi\cup\{\varnothing\}_{\!\pi}}c_{\pi,B}!}\;2^{c_{\{[r]\},\varnothing}},}
\]
where the empty status is included only when \(|\pi|<3\). The formulas include \(r=1\), \(r=2\), and the case when every vertex is marked.

## Assumptions and scope

Only the **uncoloured undirected ternary Hamming adjacency graph** with its specified singleton initial vertex colours is considered. The theorem is a *within-one-graph* orbit-classification statement, not identification against every nonisomorphic graph. It places no assumption on the positions, number, or Hamming distances of the marked vertices beyond distinctness. All coordinates are labelled before taking automorphism orbits.

The status \(B\) is always a subset of the labelled marker-index set \([r]\), so distinct equality-pattern partitions cannot be confused. A coordinate type \(\pi\) with no occurrences contributes a factor one. For \(\pi=\{[r]\}\), the two symbol values absent from all markers give a single status \(\varnothing\), because they can be interchanged independently in each coordinate.

## Proof

**Automorphism orbit normal form.** Every graph automorphism of \(H(d,3)=K_3\square\cdots\square K_3\) is a coordinate permutation followed by independent permutations of the three alphabet symbols in each coordinate. This is the standard Hamming-graph automorphism description [1]. Fixing all labelled markers pointwise permits coordinate permutations exactly between coordinates with the same marker equality partition \(\pi\), and independent permutations of symbols not represented by the markers in each coordinate. In particular, the status histogram \(c_{\pi,B}(x)\) is constant on the pointwise-stabilizer orbit of \(x\). Conversely, if \(x,y\) have the same histograms, coordinate permutations first match their statuses within each \(\pi\), and independent symbol permutations then send the symbols of \(x\) to those of \(y\), while leaving all markers fixed. Thus the histograms classify the orbits exactly. Since automorphisms preserve initial colours and refinement, stable colours cannot separate points within one such orbit.

**Visible distance vectors.** Write \(D_i(x)=d_H(x,s_i)\), and \(D(x)=(D_1(x),\ldots,D_r(x))\). Induction on refinement rounds shows that after round \(t\), a vertex colour determines \(\min\{D_i(x),t+1\}\) for each marker \(i\): the colour of the singleton \(s_i\) is initially isolated, and the distance to that singleton is recovered layer by layer from neighbour counts without merging old colours. Consequently, at round \(d\), every colour determines the complete vector \(D(x)\), because all graph distances are at most \(d\).

**Displacement reconstruction in one further round.** For a neighbour \(y\) of \(x\), define \(\delta(y,x)=D(y)-D(x)\in\{-1,0,1\}^r\). Refinement at round \(d+1\) determines the exact multiset \(\{\!\{\delta(y,x):y\sim x\}\!\}\), since round-\(d\) colours determine all neighbour distance vectors and the old colour of \(x\) determines \(D(x)\).

Let \(\mathbf 1_B\in\{0,1\}^r\) denote the indicator vector of a marker-index block \(B\). Changing one coordinate from current symbol \(a\) to distinct symbol \(b\) changes the distance vector by \(\mathbf 1_B-\mathbf 1_C\), where \(B\) is the set of markers equal to \(a\) at this coordinate and \(C\) the corresponding set equal to \(b\). The sets \(B,C\) may be empty but never both are empty when \(\pi\) has three blocks. Because the alphabet has exactly three symbols, the possible moves can be listed exhaustively:

* If \(\pi=\{[r]\}\), a coordinate in the marked-symbol status emits two displacements \(+\mathbf1_{[r]}\); a coordinate in empty status emits one \(-\mathbf1_{[r]}\) and one zero displacement.
* If \(\pi=\{B,C\}\), a coordinate in status \(B\) emits \(+\mathbf1_B-\mathbf1_C\) and \(+\mathbf1_B\); one in status \(C\) gives the reversed formulas; one in empty status emits \(-\mathbf1_B\) and \(-\mathbf1_C\).
* If \(\pi=\{B,C,E\}\), a coordinate in status \(B\) emits \(+\mathbf1_B-\mathbf1_C\) and \(+\mathbf1_B-\mathbf1_E\), and similarly for either other status.

These patterns **recover every histogram count without ambiguity**. The multiplicity of \(+\mathbf1_{[r]}\) is twice \(c_{\{[r]\},[r]}\), and that of \(-\mathbf1_{[r]}\) is \(c_{\{[r]\},\varnothing}\). For every nonempty proper subset \(B\subsetneq[r]\), the multiplicity of \(+\mathbf1_B\) is \(c_{\{B,[r]\setminus B\},B}\), while that of \(-\mathbf1_B\) is \(c_{\{B,[r]\setminus B\},\varnothing}\). Finally, if \(B,C\) are disjoint nonempty sets whose union is a proper subset of \([r]\), the multiplicity of \(+\mathbf1_B-\mathbf1_C\) is exactly \(c_{\{B,C,[r]\setminus(B\cup C)\},B}\). Every two- and three-block count therefore appears explicitly in the multiset, as do both one-block counts. This proves that the round-\(d+1\) colours distinguish all pointwise-stabilizer orbits, establishing the equality and the stabilization bound.

**Enumeration.** Each coordinate type \(\pi\) has two possible statuses when \(|\pi|=1\), and three possible statuses when \(|\pi|=2\) or \(3\). By stars and bars, distributing \(n_\pi\) coordinates among those statuses yields \(n_\pi+1\) or \(\binom{n_\pi+2}{2}\) orbits, respectively. Distinct coordinate types are independent; multiplying gives the class formula. For a fixed histogram the number of coordinate allocations is multinomial, and only in one-block coordinates does an empty status leave two freely chosen unmatched symbols. This yields the class-size formula.

## Verification

The standalone script `verify_ternary.py`, using integer-exact enumeration, checks 985 distinguished-marker configurations on \(H(d,3)\) for \(1\le d\le4\) and \(1\le r\le4\). It independently computes the graph refinement partition, the marker-pattern orbit partition, and the exact neighbour displacement-count polynomial at every tested vertex. All checks pass, including exhaustive configurations for \(d\le2\) and deterministic bounded samples for dimensions three and four. The script also checks the bound of \(d+1\) refinement rounds and reports each tested category in `verification_output.txt`. As an illustrative four-mark configuration, marking \((0,0,0),(1,0,0),(0,1,0),(0,0,1)\) makes all \(27\) vertices of \(H(3,3)\) singleton classes after two rounds.

Run `python3 verify_ternary.py` with Python 3 standard library only. This finite test is a check of the formulas; the universal conclusion rests on the proof above, not on extrapolation.

## Relationship to prior work

The wreath-product description of Hamming graph automorphisms [1] and the counting-refinement formalism and general orbit-related hierarchy [2] are background. Existing two-marker Hamming results determine stabilizer orbits for exactly two individualized vertices, and binary-cube results allow arbitrary marker sets when the alphabet has two symbols; neither implication covers arbitrarily many labelled markers on a ternary Hamming graph. The present theorem provides the complete *all-marker* ternary result, a direct inverse from one-step distance-displacement counts, an explicit orbit-count product, and class-size formulas. General individualization complexity results [3] do not state these specialized formulas. The distinctions concern theorem implications rather than title similarity.

## Limitations

The theorem is specific to alphabet size three. The one-step displacement inversion uses that at most three distinct marker-symbol blocks exist in a coordinate, and no claim is made about arbitrary individualizations for larger alphabets. Only within-graph refinement-orbit equality is proved, not universal isomorphism identification or any graph-complexity separation. The literature comparison is best-effort; an unknown specialized theorem could already imply this classification. Independent scientific verification and publication-priority certification have not occurred.

## References

[1] G. A. Jones, *Classification and Galois conjugacy of Hamming maps*, arXiv:1006.0516 (first submitted 2010-06-02), Section 1 (Hamming-graph automorphism wreath product). https://arxiv.org/abs/1006.0516
[2] V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v3 (2015), Sections 2 and 8 and Appendix A.2 (general refinement and examples, including Johnson graphs). https://arxiv.org/html/1502.01255v3
[3] V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, MFCS 2016, LIPIcs 58, Article 13, DOI:10.4230/LIPIcs.MFCS.2016.13 (definitions and general complexity of individualization). https://doi.org/10.4230/LIPIcs.MFCS.2016.13
