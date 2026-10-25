# The full octahedral homology character of the truncated-cube scale-three Rips complex

## Finding
Let \(T\) be the graph of the truncated cube, with its shortest-path metric, and let \(K=\operatorname{VR}_{\leq3}(T)\) be the inclusive Vietoris–Rips complex. Its geometric symmetry group \(G\cong S_4\times C_2\) acts on \(K\). Write \(\varepsilon\) for the nontrivial character of the central-inversion factor and \(S^\lambda\) for the rational Specht representation of \(S_4\) indexed by the partition \(\lambda\). Then the complete reduced rational homology representation is
\[
\widetilde H_j(K;\mathbb Q)\cong
\begin{cases}
\mathbf1\boxtimes\varepsilon,&j=2,\\
(S^{(4)}\oplus S^{(2,2)})\boxtimes\mathbf1\;\oplus\;S^{(2,1,1)}\boxtimes\varepsilon,&j=3,\\
0,&j\notin\{2,3\}.
\end{cases}
\]
In particular, central inversion fixes precisely three dimensions of third homology and negates the other three; the full symmetry-fixed reduced rational homology is one-dimensional in degree three and vanishes in degree two. The previously established nonequivariant homotopy type \(S^2\vee\bigvee^6S^3\) is not asserted as a new result.

## Assumptions and scope
An explicit graph model is \(V(T)=\{(a,s):a\in\{0,1,2\},\ s\in\{\pm1\}^3\}\). Vertices \((a,s)\) and \((b,t)\) are adjacent precisely if either \(a\ne b\) and \(s=t\), or \(a=b\) and \(t\) differs from \(s\) only at coordinate \(a\). Its Euclidean realization has one coordinate of absolute value \(1\) and the other two of absolute value \(1+\sqrt2\). Signed coordinate permutations give the complete group of geometric symmetries of order \(48\); determinant-positive elements act as the rotation group \(S_4\), and central inversion supplies the other factor. All distances in the theorem are graph distances, not Euclidean distances.

## Proof
**1. Exact chain ranks.** The simplex counts by dimension \(0\) through \(5\) are
\[
(24,156,376,372,144,20).
\]
On the increasing-vertex oriented simplicial chains, direct rational Gaussian elimination gives boundary ranks
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_5)=(23,133,242,124,20).
\]
The chain identities \(\partial_{j-1}\partial_j=0\) follow from the alternating face formula. Consequently \(H_0(K;\mathbb Q)=\mathbb Q\), \(H_1=0\), \(\widetilde H_2=\mathbb Q\), \(\widetilde H_3=\mathbb Q^6\), and all higher groups vanish. These ranks independently reconstruct the rational part of the known sphere-wedge result.

**2. The degree-two character.** Regard the graph as the one-skeleton of the Euclidean truncated cube, which has eight triangular faces and six octagonal faces. Each octagonal face admits a triangulation by diagonals joining graph vertices at distance at most three. Give every triangle its outward orientation. Summing the eight triangular faces and the six triangulated octagons yields a simplicial \(2\)-cycle \(z\) with \(44\) nonzero oriented triangles and \(\partial_2 z=0\). Exact reduction of \(z\) modulo the image of \(\partial_3\) over \(\mathbb F_{101}\) is nonzero. Moreover, all boundary ranks modulo \(101\) equal the rational ranks above, so degree-two homology has dimension one over both fields. For each of the \(48\) signed coordinate symmetries \(g\), the signed chain \(g z-\det(g)z\) reduces to zero modulo \(\operatorname{im}\partial_3\) over \(\mathbb F_{101}\). The one-dimensional rational character of this finite group has values \(\pm1\). Reduction modulo \(101\) therefore identifies it as \(g\mapsto\det(g)\), which is exactly \(\mathbf1\boxtimes\varepsilon\).

**3. The degree-three character.** For a simplex \(\sigma\), an automorphism contributes to the simplicial Lefschetz trace only when it preserves the underlying vertex set; the signed contribution is the sign of the induced vertex permutation. Computing this directly from all \(1092\) nonempty simplices gives \(L(g)\). Since only degrees \(0,2,3\) have rational homology,
\[
\chi_3(g)=1+\det(g)-L(g).
\]
The next table lists \(\chi_3\) on all ten conjugacy classes of \(S_4\times C_2\). Here \(h\) denotes the permutation of the four cube body diagonals induced by the determinant-positive factor; the second column is the class size inside \(S_4\). The columns \(+\) and \(-\) mean the absence or presence of central inversion.

| Cycle type of \(h\) | Class size | \(\chi_3(h,+)\) | \(\chi_3(h,-)\) |
|:--|--:|--:|--:|
| \((1,1,1,1)\) | 1 | 6 | 0 |
| \((2,1,1)\) | 6 | 0 | 2 |
| \((2,2)\) | 3 | 2 | 4 |
| \((3,1)\) | 8 | 0 | 0 |
| \((4)\) | 6 | 2 | 0 |

Taking the ordinary character inner products with the five irreducible rational characters of \(S_4\), separately in the two central-parity sectors, gives exactly one copy each of \(S^{(4)}\boxtimes\mathbf1\), \(S^{(2,2)}\boxtimes\mathbf1\), and \(S^{(2,1,1)}\boxtimes\varepsilon\), with every other multiplicity zero. Their dimensions are respectively \(1,2,3\), summing to \(6\).

## Verification
The accompanying `checker.py` constructs the graph and all its Rips simplices from first principles, checks isomorphism with the standard truncated-cube graph and computes the complete rational and modulo-\(101\) chain ranks. It explicitly constructs the \(44\)-triangle oriented boundary cycle, tests its nonzero mod-\(101\) homology class, verifies its determinant transformation on all \(48\) group elements, computes all signed fixed-simplex Lefschetz traces, checks class constancy, and projects the resulting character onto rational irreducibles. Run `python checker.py` with Python, NetworkX, NumPy, and SymPy installed. Its final output is `RESULT PASS` followed by the checked counts and ranks. These finite exhaustive checks concern the specified finite complex, so no unverified extrapolation in size is used.

## Relationship to prior work
Saleh, Titz Mite, and Witzel (2023) classify the Rips homotopy types of the Platonic solids and explicitly propose Archimedean solids as an extension. Adamaszek (2011) supplies the general equivalence between graph-metric Rips complexes and clique complexes of graph powers, but does not determine this symmetry representation. A published exact calculation, *A mixed-dimensional Rips wedge for the truncated cube* (2026), establishes the identical complex's nonequivariant homotopy type and chain-level collapse; its complete scientific statement and proof were inspected, and do not supply the geometric symmetry character. The present result determines the entire \(S_4\times C_2\) action on both nonzero rational homology groups, rather than recomputing the already-known sphere counts. Separate calculations on the truncated octahedron or the cube's cut complexes concern nonisomorphic spaces and do not imply these ten character values.

## Limitations
The claim concerns rational representations at the single inclusive graph-distance threshold three. It does not determine integral representation lattices, equivariant homotopy types, or representations at other scales or for Euclidean metrics. The cited prior homotopy classification is acknowledged as established; only its symmetry refinement is the claimed contribution. An equivalent unindexed equivariant computation may exist; the literature search is not a proof of absolute priority. Independent external mathematical review has not been performed.

## References
1. Nada Saleh, Thomas Titz Mite, Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), *Innovations in Incidence Geometry* 21 (2024), 17–34. https://arxiv.org/html/2302.14388v1
2. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), *Israel Journal of Mathematics* 196 (2013), 295–319. https://arxiv.org/html/1104.0433v3
3. *A mixed-dimensional Rips wedge for the truncated cube*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-mixed-dimensional-rips-wedge-for-the-truncated-cube--4fae71a21a80
