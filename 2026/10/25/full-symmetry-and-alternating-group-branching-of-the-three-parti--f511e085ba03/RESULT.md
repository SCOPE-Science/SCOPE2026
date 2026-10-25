# Full symmetry and alternating-group branching of the three-particle genus-three theta surface

## Finding
Write \(G=K_{2,4}\) for the graph with two branch vertices \(a,b\) and four length-two paths \(a-i-b\), \(i\in\{0,1,2,3\}\). Let \(X=\operatorname{UConf}_3(G)\) be the unordered configurations of three distinct points. The natural graph automorphisms give \(S_4\times\langle\rho\rangle\), where \(\rho\) exchanges \(a,b\). The full rational first-homology representation is
\[
H_1(X;\mathbb Q)\cong \bigl(S^{(3,1)}\oplus S^{(2,1,1)}\bigr)\boxtimes\varepsilon_\rho.
\]
Here the Specht summands both have dimension three, and \(\varepsilon_\rho(\rho)=-1\). On permutation cycle types \((1^4),(2,1,1),(2,2),(3,1),(4)\), the first-homology character is respectively \((6,0,-2,0,0)\) without hub exchange and its negative with hub exchange. The action on the integral fundamental class is \(\operatorname{sgn}_{S_4}\boxtimes\mathbf1_\rho\).

The orientation-preserving group \(A_4\) acts with quotient orbifold of signature
\[
\boxed{(0;2,2,3,3)}.
\]
More precisely, the fixed points of the three nontrivial double transpositions form two orbits of six points, and the fixed points of order-three elements form two orbits of four points. The underlying quotient is a sphere.

## Assumptions and scope
All configuration spaces are **unordered** and have exactly three particles. The graph is considered as a topological one-dimensional CW complex. The four degree-two vertices represent four parallel paths between the two essential vertices. The group acts by graph homeomorphisms, not by permuting particle labels. All representation decompositions are over \(\mathbb Q\), while the orientation calculation is integral. We make no assertion about an integral \(\mathbb Z[S_4\times C_2]\)-module decomposition.

## Proof
**Finite cubical model.** The Abrams unordered cubical deformation retract applies since every route between distinct essential vertices has at least two edges and every embedded circuit has at least four edges, the subdivision thresholds for three particles. Label the essential vertices \(4,5\) and the internal vertices \(0,1,2,3\). Orient each of the eight graph edges from an essential vertex to an internal vertex. An occupied cell is an unordered collection of three open vertices/edges with pairwise disjoint closed supports.

The zero-cells are all unordered triples of vertices (\(20\) cells). The one-cells are an edge and two external vertices (\(8\binom42=48\) cells). The two-cells are two disjoint edges and one external vertex (\(24\) cells). There are no higher cells. With the induced product orientation on an ordered pair of occupied edges, the boundary is the standard cubical rule \(\partial(e\times f)=\partial e\times f-e\times\partial f\). Consequently, in the ordered cellular bases the exact integral matrices \(d_1,d_2\) have sizes \(20\times48\) and \(48\times24\).

The included finite checker constructs every cell and incidence from these definitions and verifies \(d_1d_2=0\). It finds a single cyclic link at each of the \(20\) vertices and precisely two incident squares at each edge, so the complex is a closed connected surface. It constructs a global orientation cycle \(z\), having coefficient \(\pm1\) on every square and satisfying \(d_2z=0\). Its finite-field ranks are \(\operatorname{rank}d_1=19\) and \(\operatorname{rank}d_2=23\); in particular connectivity follows already from the first rank. The Euler characteristic is \(20-48+24=-4\), so \(X\) is an orientable genus-three surface. Hence \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z^6\), and \(H_2\cong\mathbb Z\). The genus and these ordinary groups are acknowledged as known from earlier literature; their reconstruction makes the new action calculation self-contained.

**Complete group character.** The permutations of the four internal vertices and exchange of the two essential vertices act on the cubical chains by signed permutation matrices. The checker enumerates all \(24\cdot2=48\) automorphisms. Because a cell image is explicit, the trace in each chain dimension is an exact integer sum over fixed oriented cells. The image of \(z\) is compared coefficientwise to \(z\) and \(-z\); this gives the fundamental-class trace \(\chi_2(g)=\operatorname{sgn}(\sigma)\), independent of \(\rho\). As \(X\) is connected, \(\chi_0=1\). The equivariant Euler identity gives
\[
\chi_1(g)=1+\chi_2(g)-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2).
\]
For the five \(S_4\) cycle types in the order specified above, this yields \(\chi_1(\sigma,1)=(6,0,-2,0,0)\) and \(\chi_1(\sigma,\rho)=(-6,0,2,0,0)\). The standard \(S_4\) character \(S^{(3,1)}\) is \((3,1,-1,0,-1)\); multiplying by permutation sign gives the character \((3,-1,-1,0,1)\) of \(S^{(2,1,1)}\). Their sum equals the computed character. Since the hub exchange acts by the negative of this full character, semisimplicity and character orthogonality over \(\mathbb Q\) prove the displayed module decomposition.

**Branching.** Every \(g\in A_4\) preserves orientation. A nontrivial finite-order orientation-preserving homeomorphism of a closed surface has isolated fixed points, each with local Lefschetz index \(+1\). For a double transposition, \(\chi_1=-2\), \(\chi_2=1\), so the Lefschetz number is \(1-(-2)+1=4\) and it fixes exactly four points. Each of the eight nonidentity three-cycles has \(\chi_1=0\), and fixes exactly two points. Stabilizers of an effective orientation-preserving finite surface action are cyclic. Thus the three involutions give \(3\cdot4=12\) points with stabilizer of order two (two orbits of six), while the eight order-three elements give \(8\cdot2/2=8\) points with stabilizer of order three (two orbits of four). The Riemann–Hurwitz relation for this \(12\)-sheeted quotient reads
\[
-4=12\left(2-2g_0-2(1-1/2)-2(1-1/3)\right),
\]
forcing \(g_0=0\). This proves the orbifold signature and exhausts the possible branching.

## Verification
Run `python3 triple_checker.py` from the directory containing this file and the checker. It enumerates all \(20\) zero-cells, \(48\) one-cells, \(24\) two-cells and computes signed integer incidence matrices, checks all vertex links, constructs a primitive orientation cycle, checks the boundary product, computes modular ranks, and checks all \(48\) group automorphisms. The final line is `PASS 20,48,24 cells; rank(d1)=19 rank(d2)=23; 48 symmetry actions; primitive orientation cycle; chain boundary`. Modular ranks alone are not a proof of integral torsion-freeness: that conclusion instead follows from the verified closed orientable surface structure. The orbifold computation is a mathematical consequence of the complete character and standard local properties of finite group actions on surfaces.

## Relationship to prior work
Maciążek and Sawicki, *Non-abelian Quantum Statistics on Graphs*, first submitted on 2018-06-07, §5.6, calculate the ordinary homology of configurations on \(K_{2,p}\) and identify the genus-three three-particle configuration on \(K_{2,4}\). Those statements are **not** novelty claims here. An and Knudsen, *On the second homology of planar graph braid groups* (2020 preprint; 2022 journal), establish a general theta-class theory. A separately published complete theta-class relation theorem identifies \(H_2(B_3(\Theta_m);\mathbb Z)\) with an exterior-cube augmentation lattice, which for four paths already explains the top sign character, but not the first-homology character or the quotient ramification. Modern work on stable homology representations of graph configuration spaces includes other complete-bipartite families, but the inspected coverage does not give this \(S_4\times C_2\) genus-three surface calculation. The result adds a complete action on the six independent first-homology cycles and the branched quotient type, neither implied by the ordinary Betti numbers or the known top-degree module.

## Limitations
The first-homology splitting is rational; no integral module splitting, fundamental-group outer action, or canonical algebraic-curve realization is asserted. The finite exact checker is not a formal theorem prover, but all relevant finite cell sets and operations are constructed exhaustively, not sampled. An independently performed mathematical audit is not available. An equivalent determination of this finite symmetry action outside the inspected literature remains possible.

## References
1. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, arXiv:1806.02846, first submitted 2018-06-07, §5.6; *Communications in Mathematical Physics* (2019), doi:10.1007/s00220-019-03583-5.
2. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020); *Journal of Topology* 15 (2022), 666–691.
3. *Complete theta-class relations for three-point generalized theta configurations*, published mathematical record (2026), identifier `2026/10/4/SCOPE-complete-theta-class-relations-for-three-point-generalized-theta--7d068c6381b8`.
4. D. Ramos and E. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813 (2026), particularly its treatment of balanced complete bipartite graphs.
