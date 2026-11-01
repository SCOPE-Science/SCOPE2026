# Four-cut integral homology separates the Shrikhande and four-by-four rook graphs

## Finding

For the two strongly regular graphs with parameters \((16,6,2,2)\), the ordinary four-cut complexes have different *integral* homology. Write \(R=K_4\square K_4\) for the rook graph and \(S\) for the Shrikhande graph. Then

\[
\widetilde H_i(\Delta_4(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{21}&i=10,\\
\mathbb Z^{96}&i=11,\\
0&\text{otherwise},
\end{cases}
\qquad
\widetilde H_i(\Delta_4(S);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{12}&i=9,\\
\mathbb Z^{2}&i=10,\\
\mathbb Z^{65}&i=11,\\
0&\text{otherwise}.
\end{cases}
\]

All integral groups above are torsion-free. Both cut complexes are pure of dimension \(11\), both are non-shellable, and both have reduced Euler characteristic \(-75\). Thus four-cut topology distinguishes these graphs despite their equal strongly regular parameters *and* Euler characteristic.

## Assumptions and scope

Graphs are finite, undirected and simple, with common vertex set \(V=\mathbb Z_4^2\) indexed by \((a,b)\mapsto 4a+b\). Vertices of \(R\) are adjacent when they agree in exactly one coordinate. Vertices of \(S\) are adjacent when their difference modulo four lies in

\[
\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]

For any graph \(G\) on \(V\), \(\Delta_4(G)\) denotes the simplicial complex whose facets are \(V\setminus U\), for \(U\subseteq V\) of size four whose induced graph \(G[U]\) is disconnected. This is the *ordinary*, not total, cut complex. The corresponding Alexander dual \(K_G=\Delta_4(G)^\vee\) consists exactly of subsets containing **no** disconnected induced four-set.

## Proof

**1. Finite Alexander-dual models.** Exhaustively test the \(\binom{16}{4}=1820\) four-subsets for connectedness via the graph's explicit adjacency. There are \(1200\) disconnected four-sets for \(R\), and \(1152\) for \(S\). The duals each have \(1652\) nonempty simplices, with respective full face vectors

\[
 f(K_R)=(16,120,560,620,288,48),\qquad
 f(K_S)=(16,120,560,668,288).
\]

Two independent constructions in `verify.py` agree: reject subsets containing any disconnected four-set, or demand that all their four-subsets induce connected graphs. An independent face enumeration of the original cut complexes yields reduced Euler characteristic \(-75\) for each.

**2. Acyclic matchings.** On each nonempty dual face set, apply the deterministic staged coordinate-toggle pairing given in `verify.py`, using vertex order \(0,1,\ldots,15\). For each stage, pair every currently active face lacking the vertex with its coface obtained by adding that vertex (provided both are active), and remove both. The verifier checks *all* Hasse incidences, reverses precisely the paired incidences, and topologically sorts the directed graph. This proves the pairings form genuine acyclic discrete-Morse matchings, not merely greedy reductions. For \(K_R\), there are \(767\) pairs and the critical cell counts are \((c_0,c_2,c_3)=(1,96,21)\); for \(K_S\), there are \(776\) pairs and \((c_0,c_2,c_3,c_4)=(1,69,12,18)\). All other critical counts vanish.

**3. Integral chain reduction.** Form every simplicial boundary with its alternating integer incidence signs. Eliminate the matching pairs as unit-coefficient pivots, updating all boundary columns exactly over \(\mathbb Z\), and verify the chain identity before and after cancellation. For \(K_R\), all remaining differentials vanish. For \(K_S\), the only nonzero critical differentials are the degree-three and degree-four matrices, of respective integer ranks \(4\) and \(6\). For both matrices all nonzero Smith factors are \(1\): iterative integer row and column operations find only unit pivots and leave zero residual blocks. The critical Betti groups therefore are

\[
\widetilde H_j(K_R;\mathbb Z)\cong\begin{cases}\mathbb Z^{96}&j=2,\\\mathbb Z^{21}&j=3,\\0&\text{otherwise},\end{cases}
\quad
\widetilde H_j(K_S;\mathbb Z)\cong\begin{cases}\mathbb Z^{65}&j=2,\\\mathbb Z^{2}&j=3,\\\mathbb Z^{12}&j=4,\\0&\text{otherwise}.\end{cases}
\]

The one critical vertex and no critical edges ensure connectedness and zero reduced degree-zero homology. The unit Smith factors ensure **integral** torsion-freeness. Independent full original boundary reductions over \(\mathbb F_2\) produce ranks \((15,105,359,240,48)\) and \((15,105,390,276)\), respectively, consistent with the integral computation.

**4. Combinatorial Alexander duality.** On sixteen vertices,

\[
\widetilde H_i(\Delta_4(G);\mathbb Z)\cong
\widetilde H^{13-i}(K_G;\mathbb Z).
\]

The universal coefficient theorem identifies the latter cohomology groups with the free homology groups computed above, since those have no torsion. Reversing the degrees gives the stated four-cut homology for both graphs. Each \(\Delta_4(G)\) is pure eleven-dimensional by its explicit facet definition; its positive homology below degree eleven proves it cannot be shellable, since a pure shellable complex is a wedge of spheres of top dimension (possibly with zero spheres).

## Verification

Run `python3 verify.py` using Python 3.10 or later, with no third-party packages. It reconstructs both graphs, verifies the common strongly regular parameters, exhausts all \(2^{16}-1=65535\) nonempty vertex subsets for each dual, checks two distinct dual definitions and the full cut-complex face counts, verifies all \(6128\) and \(6032\) Hasse incidences, performs exact signed integer Morse cancellations and unit Smith elimination, and separately computes all mod-two simplicial boundary ranks. The recorded stdout is `verification_output.txt`; its final line must be `ROOK_SHRIKHANDE_FOUR_CUT_INTEGRAL_HOMOLOGY_VERIFIED`. Only this finite pair of graphs is classified.

## Relationship to prior work

Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue introduce the standard cut-complex framework, its Alexander-dual formulation and results on cycles, complete multipartite graphs, trees, clique prisms and other examples [1]. Bayer–Denker–Jelić Milutinović–Sundaram–Xue study disjoint unions, squared paths and *rectangular path grids* [2]. A rectangular grid \(P_m\square P_n\) is not the rook graph \(K_4\square K_4\); the authors' grid theorems cannot be substituted for this graph. Published results about the **three-cut** topology of rook graphs and the independence complexes of the Shrikhande and rook graphs address different objects and do not imply the above **four-cut** integral homology computation. General Alexander duality and the definition of the cut complex are prior tools, not new claims.

## Limitations

The result gives **integral homology only**, not a homotopy or simple-homotopy classification and not a formula for all strongly regular graphs. The explicit certificate applies only to the two specified sixteen-vertex graphs and to cutoff four. The source search and published-record comparisons cannot rule out an unindexed equivalent calculation; this is a residual bibliographic risk. Computation is exact and exhaustive for the stated finite input, with the algorithm and expected values embedded for independent reproduction.

## References

[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 26 April 2023; see Sections 1, 6 and 7.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted 11 July 2024; see Section 5 on path-grid graphs.
