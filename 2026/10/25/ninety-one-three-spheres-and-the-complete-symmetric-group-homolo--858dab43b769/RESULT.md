# Ninety-one three-spheres and the complete symmetric-group homology character of a triangular neighborhood complex

## Finding
Let \(T_6=L(K_6)\) be the triangular graph: its fifteen vertices are the unordered pairs in \(\{0,1,2,3,4,5\}\), and distinct pairs are adjacent precisely when they intersect. Let \(X=\mathcal N(T_6)\) denote the ordinary Lovász open-neighborhood complex, whose faces are all subsets of the open neighborhood of at least one vertex of \(T_6\).

**Theorem.** The integral homotopy type and the entire natural rational \(S_6\)-homology module are
\[
X\simeq\bigvee^{91}S^3,\qquad
\widetilde H_3(X;\mathbb Q)\cong
S^{(4,2)}\oplus S^{(3,3)}\oplus2S^{(3,2,1)}\oplus S^{(3,1,1,1)}
\oplus2S^{(2,2,2)}\oplus S^{(2,2,1,1)}\oplus3S^{(2,1,1,1,1)}
\oplus S^{(1,1,1,1,1,1)}.
\]
Here \(S^\lambda\) denotes the rational Specht module for partition \(\lambda\) of six. All other reduced integral homology groups vanish; \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{91}\). No nonzero rational homology class is invariant under every permutation of the six labels, so the orbit space \(|X|/S_6\) is rationally acyclic in reduced homology.

## Assumptions and scope
The neighborhood is **open**, so a pair is not in its own neighborhood. This is the neighborhood complex of \(L(K_6)\), **not** of its Kneser complement \(\mathrm{KG}(6,2)\), nor its clique complex. All fifteen vertex labels are ordered lexicographically as \((01),(02),(03),(04),(05),(12),(13),(14),(15),(23),(24),(25),(34),(35),(45)\); an integer bit mask encodes each simplex. Integral homotopy and additive homology are claimed, but the representation decomposition is over \(\mathbb Q\) only. The result is for exactly six underlying labels, not an assertion for all triangular graphs.

## Proof
**Complete face set.** For each unordered pair \(a\), let \(N(a)\) consist of the eight other pairs sharing one label with \(a\). Encode a face by an integer mask \(f\) with one bit per ordered vertex. Then precisely
\[
\mathcal F=\{f:\exists a\text{ with }f\subseteq N(a)\}.
\]
Taking all submasks of the fifteen explicitly computed neighborhood masks produces exactly \(2881\) faces, including the empty face, with degree \((-1,0,1,2,3,4,5,6,7)\) face vector
\[
(1,15,105,420,945,840,420,120,15).
\]
The independent standard-library certificate `verify_t6_neighborhood.py` reconstructs every mask and checks the face vector without external data.

**Acyclic matching and homotopy.** Perform sequential element toggles in the lexicographic vertex-index order
```
2, 11, 3, 4, 1, 0, 9, 12, 6, 10, 14, 5, 7, 13, 8
```
At each index \(i\), inspect every currently unmatched face \(f\) not containing bit \(i\), in ascending mask order. If the face \(f\cup\{i\}\) is also unmatched, pair these two faces and remove them from further matching. This deterministic construction gives exactly \(1395\) pairs including the single pair involving the empty face, leaving exactly \(91\) unmatched faces, all of cardinality four.

Orient every Hasse cover relation from a face to its codimension-one subface, except reverse each matched cover. On the **entire** augmented Hasse graph the certificate constructs all \(12945\) cover incidences and deletes **all 2881 vertices** by indegree-zero topological sorting; hence there are no directed cycles. Removing the matched empty-face pair yields an ordinary acyclic discrete Morse matching with \(1394\) matched pairs, one critical vertex, and \(91\) critical three-cells. Forman's discrete Morse theorem therefore gives a CW complex with one zero-cell, no one- or two-cells, and \(91\) three-cells. Every attaching map to the sole zero-cell is constant. Consequently \(X\simeq\bigvee^{91}S^3\), establishing the integral claim rather than inferring it from characteristic-two ranks.

**Full permutation character.** Every permutation \(\pi\in S_6\) permutes the fifteen pair labels, preserving the fifteen neighborhood facets; this is checked for all \(720\) permutations. For each simplex \(f\) fixed setwise by \(\pi\), let \(\operatorname{sgn}(\pi|_f)\) be the sign of the induced permutation on its ordered vertices. The reduced Lefschetz number is the exact finite sum
\[
\widetilde L(\pi)=-1+\sum_{\substack{f\in\mathcal F,\ f\ne\varnothing\\\pi f=f}}
(-1)^{|f|-1}\operatorname{sgn}(\pi|_f).
\]
Since reduced homology is supported only in degree three, \(\chi_{\widetilde H_3}(\pi)=-\widetilde L(\pi)\). Exhaustively evaluating all \(720\) elements gives the following complete class character (the second entry is the conjugacy-class size):

| Cycle type | Size | Trace on \(\widetilde H_3\) |
|:--|--:|--:|
| \((1,1,1,1,1,1)\) | 1 | 91 |
| \((2,1,1,1,1)\) | 15 | −13 |
| \((2,2,1,1)\) | 45 | 7 |
| \((2,2,2)\) | 15 | 7 |
| \((3,1,1,1)\) | 40 | 1 |
| \((3,2,1)\) | 120 | −1 |
| \((3,3)\) | 40 | 1 |
| \((4,1,1)\) | 90 | −3 |
| \((4,2)\) | 90 | −3 |
| \((5,1)\) | 144 | 1 |
| \((6)\) | 120 | 1 |

For each partition \(\lambda\vdash6\), independently compute the rational Specht character with the Murnaghan–Nakayama rule (remove connected rim hooks with no two-by-two squares and record their height signs). The exact inner product \(\frac1{720}\sum_{\text{classes }C}|C|\chi(C)\chi^\lambda(C)\) gives, in partition order \((6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1),(2,1,1,1,1),(1,1,1,1,1,1)\), multiplicities
\[
(0,0,1,0,1,2,1,2,1,3,1).
\]
Their dimension-weighted total is \(91\), yielding the displayed decomposition. The multiplicity of the trivial representation is zero. The rational cellular transfer theorem for finite group actions (e.g. after equivariant barycentric subdivision) identifies \(\widetilde H_*(|X|/S_6;\mathbb Q)\) with invariants, proving rational acyclicity of the quotient.

## Verification
Run `python3 verify_t6_neighborhood.py` with Python 3 and the standard library. It regenerates **every** simplicial face from the graph definition, checks all \(2881\) vertices and \(12945\) incidences of the augmented Hasse diagram, verifies the complete matching and its acyclicity, computes the full signed reduced Lefschetz traces for all \(720\) permutations, and independently decomposes those characters by Murnaghan–Nakayama recursion. Its final marker is `FULL_S6_NEIGHBORHOOD_CHARACTER_VERIFIED`. The finite enumeration is exhaustive for this fixed graph; it is not an extrapolation to larger \(n\).

## Relationship to prior work
Shukla's 2018 work establishes neighborhood-complex homotopy classifications for graphs of maximum degree at most three and selected 4-regular circulants; the present 8-regular triangular graph lies outside those hypotheses. Matsushita and Wakatsuki (2023) develop general neighborhood/dominance-complex duality, but their studied examples and general dualities do not determine the homotopy attaching data or this \(S_6\) action for \(L(K_6)\). Kozlov's equivalence with \(\operatorname{Hom}(K_2,G)\) provides an alternate description of the same object, not a computed representation for it.

The published result *Mixed-dimensional mod-two neighborhood homology first appears at* \(T_7\) explicitly tabulates \(\dim_{\mathbf F_2}\widetilde H_3(\mathcal N(T_6);\mathbf F_2)=91\). That **known dimension is not claimed as new**. Its own scope explicitly excludes integral homotopy types and the full permutation representation; neither is implied by the mod-two dimension. The previous triangular-graph four-cut result at five labels determines a different complex, \(\mathcal N(T_5)\); its \(S_5\) character cannot determine the six-label character. Likewise, the neighborhood complex of the complementary Kneser graph \(\mathrm{KG}(6,2)\) has a distinct face definition and homology degree. Comparisons are about mathematical implication, not only matching titles.

## Limitations
The theorem concerns a single canonical fifteen-vertex complex, not a general \(n\)-formula or integral \(\mathbb Z[S_6]\)-module splitting. A rationally acyclic quotient need not be contractible or integrally acyclic. The matching is not required to be equivariant; the group character is recovered independently by the signed Hopf trace formula. Searches cannot exclude an equivalent classification in unindexed or differently titled literature, including formulations in terms of graph Hom-complexes.

## References
1. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1 (first publicly posted 2018-02-13); Electronic Journal of Combinatorics 26 (2019).
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first publicly posted 2023-12-05).
3. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (2005).
4. *Mixed-dimensional mod-two neighborhood homology first appears at* \(T_7\), published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec .
5. *Eleven three-spheres and the symmetric-group character of a four-cut complex*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-eleven-three-spheres-and-the-symmetric-group-character-of-a-four--9dc76d8fa65e .
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
