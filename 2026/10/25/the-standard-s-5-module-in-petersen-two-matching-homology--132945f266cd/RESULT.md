# The standard \(S_5\)-module in Petersen two-matching homology

## Finding
Let \(P=KG(5,2)\) be the Petersen graph, with graph vertices the two-element subsets of \(\{1,2,3,4,5\}\) and graph edges joining disjoint pairs. Let \(M_2(P)\) be the simplicial complex whose vertices are the fifteen graph edges and whose faces are graph-edge subsets inducing degree at most two at every graph vertex. The natural action of \(S_5\) on the five labels acts simplicially on \(M_2(P)\).

The only nonzero reduced rational homology group is in degree seven. As a rational representation,
\[
\widetilde H_7(M_2(P);\mathbb Q)\cong\mathbb Q^5/\langle(1,1,1,1,1)\rangle.
\]
Equivalently, for every \(\sigma\in S_5\),
\[
\operatorname{tr}\!\left(\sigma\mid\widetilde H_7(M_2(P);\mathbb Q)\right)
=\#\{i\in\{1,2,3,4,5\}:\sigma(i)=i\}-1.
\]
This four-dimensional representation is irreducible over \(\mathbb Q\) and has no nonzero \(S_5\)-invariant vectors.

## Assumptions and scope
All objects are finite and all homology in the principal statement has coefficients in \(\mathbb Q\). The Petersen graph is the Kneser disjointness graph on two-element subsets of a five-element set. A simplex is a set of GRAPH EDGES (not a set of Petersen vertices); the bound two applies to degrees in the selected-edge subgraph. A graph automorphism acts on the fifteen vertices of the simplicial complex through its permutation of graph edges. The result concerns this particular graph and the full natural \(S_5\) action; no integral-equivariant homotopy type or integral module classification is claimed.

## Proof
**Homology concentration.** Lexicographically index the ten two-subsets of \(\{0,1,2,3,4\}\), and index the fifteen unordered pairs of disjoint two-subsets. Represent a selected-edge set by a fifteen-bit mask. A mask is a face precisely when no graph vertex is incident with more than two selected edges. There are exactly \(10870\) faces including the empty face; in dimensions zero through nine the complete face vector is
\[
(15,105,445,1245,2358,2985,2400,1095,215,6).
\]
On nonempty faces, toggle the first indexed complex vertex whenever it is absent and both that face and the face with the vertex added remain unmatched; remove these pairs and repeat successively with all fifteen complex vertices. This is a discrete-Morse matching, verified directly as follows. It has \(5432\) pairs. The orientation of all \(63780\) nonempty-face Hasse covers, downward except on matching edges, admits a complete topological ordering of all \(10869\) nonempty faces. Hence it is acyclic. The unmatched faces comprise exactly one zero-dimensional and four seven-dimensional simplices, and no others. Discrete Morse theory therefore gives a CW complex with one zero-cell and four seven-cells; the attaching maps have only a point as their target, so the complex has the ordinary homotopy type of four seven-spheres. In particular its reduced rational homology has precisely the asserted degree and rank. This same nonequivariant sphere-wedge classification is already published and is not the new assertion here.

**Equivariant traces.** Fix \(\sigma\in S_5\). It permutes the fifteen graph edges; write these edge orbits as disjoint cycles \(C_1,\ldots,C_s\). An invariant simplex is exactly a union \(\bigcup_{j\in I}C_j\) whose selected graph edges all have degree at most two. The signed trace of \(\sigma\) on an oriented simplex supported on such a union is the sign of the induced permutation on its complex vertices. A cycle of length \(\ell\) contributes \((-1)^{\ell}\cdot(-1)^{\ell-1}=-1\) to the alternating chain trace, so the sum over all invariant simplices INCLUDING the empty face is
\[
T(\sigma)=\sum_{\substack{I\subseteq\{1,\ldots,s\}\\\bigcup_{j\in I}C_j\in M_2(P)}}(-1)^{|I|}.
\]
The reduced Lefschetz identity says this alternating chain trace equals \(-\widetilde L(\sigma)\). Since all reduced homology is in odd degree seven, \(T(\sigma)\) is exactly the degree-seven homology trace. The checker independently computes the same trace by summing \((-1)^{|F|}\operatorname{sgn}(\sigma|_F)\) over all setwise fixed oriented faces \(F\), including the empty face.

The seven permutation conjugacy classes give the following exact data:

| Cycle type | Number of elements | Trace |
| --- | ---: | ---: |
| \((1,1,1,1,1)\) | 1 | 4 |
| \((2,1,1,1)\) | 10 | 2 |
| \((2,2,1)\) | 15 | 0 |
| \((3,1,1)\) | 20 | 1 |
| \((3,2)\) | 20 | -1 |
| \((4,1)\) | 30 | 0 |
| \((5)\) | 24 | -1 |

The calculation covers every one of the \(120\) permutations, not just representatives; both independent formulas agree on the seven representatives. For each cycle type its trace is the number of fixed labels minus one.

**Identify the representation.** The five-dimensional permutation module \(\mathbb Q^5\) has character equal to the number of fixed labels. Its one-dimensional constant line is trivial, so the quotient \(W=\mathbb Q^5/\langle(1,1,1,1,1)\rangle\) has the character just obtained. By semisimplicity and rational character theory for finite groups, equality of the characters gives \(\widetilde H_7(M_2(P);\mathbb Q)\cong W\). The class-size-weighted self-inner product of this character is
\[
\frac{1\cdot4^2+10\cdot2^2+20\cdot1^2+20\cdot(-1)^2+24\cdot(-1)^2}{120}=1,
\]
so it is irreducible. Its invariant space vanishes: averaging the five-coordinate permutation module has one invariant line, precisely the line removed by the quotient.

## Verification
Run `python3 verify_petersen_m2_s5.py` with Python 3 and no third-party packages. The standalone checker reconstructs Petersen adjacency from disjoint two-subsets, enumerates all \(2^{15}\) edge subsets, checks the face vector, regenerates the full greedy Morse matching, verifies every reversed cover and exhaustively checks acyclicity by topological sorting. It then checks the orbit-cycle alternating sum for all \(120\) permutations and independently checks oriented-simplex Lefschetz traces for one representative of each of the seven cycle types. It also verifies the character self-inner product and vanishing invariant dimension. A successful run ends with `PETERSEN_M2_S5_STANDARD_CHARACTER_VERIFIED`.

## Relationship to prior work
Vega introduced the two-matching complex and studied wheel and caterpillar families; Singh obtained homotopy formulas for selected complete and complete-bipartite higher-matching complexes. Neither inspected family result covers the Petersen representation. A previously published computation establishes \(M_2(P)\simeq\bigvee^4 S^7\); that nonequivariant equivalence provides the homology dimension, **not** the permutation action on the four classes. A separate computation of the Petersen ordinary three-cut complex finds an exterior-square standard module in degree six; its simplicial objects, homology degree and representation are different. The present result supplies the previously unspecified exact \(S_5\)-character of two-matching homology.

## Limitations
This determines the rational representation for one graph, not an integral lattice, a canonical cycle basis, a family-level formula, or an equivariant homotopy equivalence. The displayed character was calculated by finite exhaustive enumeration with a complete mathematical trace formula; no inference from limited small-parameter experiments is used. Database and literature searches cannot exclude every unindexed equivalent computation.

## References
1. Julianne Vega, *2-matching complexes*, arXiv:1909.10406 (first public 2019-09-23), https://arxiv.org/abs/1909.10406.
2. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first public 2020-06-24), https://arxiv.org/abs/2006.13632.
3. *The Petersen 2-matching complex is a wedge of four 7-spheres*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-petersen-2-matching-complex-is-a-wedge-of-four-7-spheres--c0442780c8c1.
4. *An irreducible S5-module in the Petersen three-cut complex*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-irreducible-s-5-module-in-the-petersen-three-cut-complex--0eae16654cf3.
