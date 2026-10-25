# Ordinary three-cut homology distinguishes the Shrikhande graph from its rook mate

## Finding

Let \(S\) be the Shrikhande graph on \(V=(\mathbb Z/4\mathbb Z)^2\): two vertices are adjacent exactly when their difference belongs to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
Let \(\Delta=\Delta_3(S)\) be its **ordinary** three-cut complex: the facets are the complements in \(V\) of the three-element subsets that induce disconnected graphs. Then the combinatorial Alexander dual, taken on all sixteen vertices, has integral homotopy type
\[
\Delta^\vee\simeq\bigvee^{11}S^2.
\]
Consequently the complete reduced **integral homology** of the original cut complex is
\[
\widetilde H_i(\Delta;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{11},&i=11,\\
0,&i\neq11.
\end{cases}
\]
The ordinary cut complex is pure of dimension twelve but has nonzero reduced homology one degree below its top dimension, so it is not shellable. The \(4\times4\) rook graph, which has the same strongly regular parameters \((16,6,2,2)\), instead has previously determined rank \(27\) in degree eleven. Hence ordinary three-cut integral homology separates these cospectral strongly regular graphs.

## Assumptions and scope

All complexes are ordinary abstract simplicial complexes, with the full specified ground vertex set. An ordinary three-cut facet is a graph-vertex complement of a disconnected induced triple, rather than a facet of the **total** cut complex. The notation \(\Delta^\vee\) denotes the combinatorial Alexander dual on the sixteen vertices; the homotopy assertion is for that dual, not for the original cut complex. Graph adjacency uses differences modulo four in both coordinates, and graph connectedness for three vertices means the induced subgraph contains at least two edges. The statement concerns the single Shrikhande graph, not all strongly regular graphs with these parameters.

## Proof

**1. Structure and faces of the dual.** Write \(K=\Delta^\vee\). By the definition of combinatorial Alexander duality, a vertex set belongs to \(K\) precisely when none of its three-element subsets induces a disconnected graph in \(S\). Hence every pair is a face of \(K\), and its triangular faces are precisely the connected graph triples. Directly from the six Cayley steps, \(S\) has sixteen vertices of degree six, every vertex neighborhood induces a six-cycle, and every pair of distinct vertices has exactly two common neighbors (the strongly regular parameters are \((16,6,2,2)\)). There are forty-eight graph edges. Each lies in exactly two graph triangles, so there are \(48\cdot2/3=32\) graph triangles. The count of connected induced triples is
\[
16\binom62-2\cdot32=176,
\]
since the first summand counts incident edge pairs (one per induced path, three per graph triangle). Therefore \(K\) has \(16\) vertices, \(120\) edges, and \(176\) triangles.

**2. All tetrahedra and the dimension bound.** For any set of at least three vertices to lie in \(K\), every vertex may have **at most one nonneighbor within the set**: two nonneighbors of one vertex would make a disconnected triple. Equivalently, missing edges in its induced graph form a matching. A four-element face therefore induces a clique, a diamond (one missing edge), or a four-cycle (two disjoint missing edges). The neighborhood six-cycle excludes graph cliques of order four. Every graph edge \(uv\) has two common neighbors that are nonadjacent, since its common-neighbor subgraph lies in the induced six-cycle at either endpoint; these give precisely one diamond with central edge \(uv\), hence forty-eight diamonds. For the seventy-two nonedges \(ab\), the two common neighbors are either adjacent (giving a unique diamond with missing edge \(ab\)) or nonadjacent (giving an induced four-cycle). Exactly forty-eight nonedges occur as the missing pairs of the forty-eight diamonds, so twenty-four nonedge pairs are diagonals of induced four-cycles; each four-cycle has two diagonals, giving twelve four-cycles. Thus \(f_3(K)=48+12=60\).

A five-element face would have missing edges forming a matching on five vertices, leaving a vertex adjacent to the other four. Those four vertices would then form a four-element face of \(K\) inside a six-cycle neighborhood, but a six-cycle contains no induced graph clique, diamond or four-cycle on four vertices. This is impossible. Therefore there are no faces of dimension greater than three, and the exact face vector is
\[
(f_0,f_1,f_2,f_3)=(16,120,176,60).
\]

**3. A two-dimensional collapse.** Every triangle of \(K\) that induces exactly two graph edges is a path \(a-b-c\), with nonadjacent endpoints \(a,c\). The two common neighbors of \(a,c\) are precisely \(b\) and one other vertex \(d\), so the only four-element face of \(K\) containing this triangle is \(\{a,b,c,d\}\). It is therefore a free triangular face of that unique tetrahedron. Every diamond has two such path triangles; every four-cycle has four. Select any one free path triangle in each of the sixty tetrahedra and collapse the tetrahedron across it. The selected triangles belong to no other tetrahedron, so the sixty elementary collapses are compatible, leaving a two-dimensional simplicial complex \(K'\simeq K\).

**4. Triviality of the fundamental group.** Let \(Y\subset K\) be the clique complex of \(S\). It is the standard sixteen-vertex triangulation of a torus obtained by identifying the \(4\times4\) grid with diagonals of slope \(1\) periodically; the graph triangles are the thirty-two elementary triangular faces. Thus \(\pi_1(Y)\cong\mathbb Z^2\), with generators represented by horizontal and vertical coordinate loops of length four. Because any nonadjacent pair in \(S\) has a common neighbor, every edge of the complete one-skeleton of \(K\) not already in \(Y\) is homotopic, relative endpoints in \(K\), to a two-edge path in \(Y\), using a triangular face of \(K\). The induced map \(\pi_1(Y)\to\pi_1(K)\) is therefore surjective. Each horizontal or vertical coordinate four-cycle spans a tetrahedron of \(K\): every triple of the four vertices induces a path in \(S\). Both torus generators consequently bound disks in \(K\), proving \(\pi_1(K)=0\).

**5. Dual homotopy and integral homology.** Euler characteristic gives
\[
\chi(K)=16-120+176-60=12.
\]
Because \(K\) is connected, simply connected, and collapses to dimension two, its reduced integral homology vanishes except possibly in degree two. Its second integral homology is free, as a subgroup of the free simplicial chain group of \(K'\), and has rank \(\chi(K)-1=11\). Hurewicz identifies \(\pi_2(K)\cong H_2(K;\mathbb Z)\). Maps representing a basis induce a homology isomorphism \(\bigvee^{11}S^2\to K\); the homological Whitehead theorem for simply connected CW complexes makes it a homotopy equivalence. Thus \(K\simeq\bigvee^{11}S^2\), integrally, without relying on experimental field ranks.

**6. Combinatorial Alexander duality.** For a simplicial complex on \(N=16\) vertices, the integral combinatorial Alexander duality isomorphism is
\[
\widetilde H_i(\Delta;\mathbb Z)\cong
\widetilde H^{N-i-3}(\Delta^\vee;\mathbb Z).
\]
The dual cohomology is \(\mathbb Z^{11}\) only in degree two, so the original three-cut homology is \(\mathbb Z^{11}\) only in degree \(i=16-3-2=11\), without torsion. Each facet of \(\Delta\) has thirteen vertices, hence its dimension is twelve. Pure shellable complexes have reduced homology concentrated in their top dimension, whereas \(\widetilde H_{11}(\Delta;\mathbb Z)\neq0\). Consequently \(\Delta\) is not shellable.

**7. Distinguishing the known rook case.** The \(4\times4\) rook graph \(R=K_4\mathbin\square K_4\) is the other strongly regular graph with parameters \((16,6,2,2)\). The published all-parameter ordinary three-cut homology theorem for rook graphs gives
\[
\operatorname{rank}\widetilde H_{11}(\Delta_3(R);\mathbb Z)
=\binom42^2-(4-1)^2=27.
\]
This earlier rank is not claimed as new; its contrast with the newly determined Shrikhande rank eleven proves the stated separation.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It independently generates the Cayley adjacency relation and enumerates every vertex subset of size at most five to test the exact dual defining criterion, the graph triangles, tetrahedron types, free faces and coordinate-loop filling. It recomputes all signed boundary ranks over three different prime fields. It reports

```
VERIFY_OK: 16 vertices, 48 graph edges, 32 graph triangles;
dual f-vector (16,120,176,60), 60 collapsible tetrahedra,
boundary ranks (15,105,60) mod 2,3,5, Betti vector (1,0,11,0).
```

To reproduce, execute `python3 verify.py` in the directory containing this document and the checker. Finite-field tests verify the finite enumerations but do not by themselves exclude arbitrary integral torsion; the proved integral collapse and fundamental-group argument in Steps 3–5 supplies that conclusion. The checker is not an independent scientific audit.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduce ordinary cut complexes in *Topology of Cut Complexes of Graphs* (arXiv:2304.13675); the sequel *Topology of Cut Complexes II* (arXiv:2407.08158) studies other graph families, including path grids. Their inspected theorems do not identify the Shrikhande ordinary three-cut homology. The previously published *Integral and equivariant homology of three-cut complexes of rook graphs* establishes the rook-graph formula used only as the comparator in Step 7. The same graph pair has appeared in studies of independence, neighborhood and intrinsic Čech complexes, which are different constructions and do not determine the ordinary three-cut homology claimed here. Our result isolates an integral homology difference in a natural cospectral strongly regular pair.

## Limitations

The full homotopy type is established for the **combinatorial Alexander dual**, not the ordinary three-cut complex itself. The theorem gives no arbitrary-parameter strongly-regular-graph classification. The checker verifies finitely many exact incidence and finite-field identities; the proof, not the checker, establishes the integral homotopy and homology. The comparison to published rook results does not establish a theorem about all cospectral pairs. A text and database search cannot exclude all unindexed or unpublished equivalent results, and external independent validation has not been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted April 26, 2023 (definition and foundational topological results).
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted July 11, 2024 (related graph families and grid methods).
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, publicly accessible mathematical result and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-integral-and-equivariant-homology-of-three-cut-complexes-of-rook--bd50464fc17f/RESULT.md (ordinary rook three-cut homology, including the rank twenty-seven at \(4\times4\)).
