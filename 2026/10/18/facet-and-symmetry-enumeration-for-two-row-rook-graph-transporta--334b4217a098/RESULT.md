# Facet and symmetry enumeration for two-row rook graph transportation balls

## Finding

For every integer \(n\ge3\), let \(G_n=K_n\square K_2\cong L(K_{2,n})\), with the unit-edge shortest-path metric. The unit ball \(B_n\) of the real Lipschitz-free space \(\mathcal F(V(G_n))\) has dimension \(2n-1\) and exactly
\[
F_n=4^n+2\cdot3^n-9\cdot2^n+8
\]
facets. Under all graph automorphisms and global central inversion, these facets fall into exactly
\[
O_{2k}=\frac{k(2k^2+15k-5)}{6},\qquad
O_{2k+1}=\frac{k(k^2+9k+5)}{3},\qquad k\ge1,
\]
orbits. In particular, for \(n=3,4,5,6,7\), the facet counts are \(54,282,1230,4986,19614\); for \(n=3,4,5,6,7\), the corresponding orbit counts are \(5,11,18,29,41\). Their orbit-count generating function is
\[
\sum_{n\ge2}O_nz^n=\frac{z^2(2+z-z^2-z^3)}{(1-z)^2(1-z^2)^2},
\]
where its coefficient at \(n=2\) is merely the natural extension of the counting expression. As \(n\) grows, \(F_n\sim4^n\), while \(O_n\sim n^3/24\).

There is a complete combinatorial facet classification: after shifting an integral supporting potential so that its first clique layer takes both values zero and one, the second layer takes precisely two consecutive values with minimum \(-1,0,\) or \(1\). The middle case consists of two different nonconstant binary words, while either outer case is a three-symbol word in which both endpoint symbols occur. The orbit classification is by explicit occupation-number vectors modulo two commuting involutions.

## Assumptions and scope

Write the graph vertices as \(a_i=(i,0)\) and \(b_i=(i,1)\), \(1\le i\le n\). All pairs of distinct \(a_i\)'s are adjacent, all pairs of distinct \(b_i\)'s are adjacent, and exactly \(a_ib_i\) connects the layers. The metric is
\[
d((i,\sigma),(j,\tau))=\mathbf1_{i\ne j}+\mathbf1_{\sigma\ne\tau}.
\]
All edge lengths are one, the scalar field is real, and the free space is the zero-sum vector space \(\{x\in\mathbb R^{2n}:\sum_vx_v=0\}\), with the transportation norm induced by this metric. Its unit ball is the symmetric edge polytope
\[
B_n=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G_n)\}.
\]
The group used for orbits is \(\operatorname{Aut}(G_n)\times\{\pm1\}\cong (S_n\times C_2)\times C_2\), where the first factor simultaneously permutes columns, the next interchanges layers, and the last negates every supporting potential. This is **not** a claim about all abstract face-lattice automorphisms or all linear isometries of the ball.

## Proof

**1. Facets and connected tight graphs.** A supporting functional is represented by a real potential \(f:V(G_n)\to\mathbb R\) modulo constants with \(|f(u)-f(v)|\le1\) on every graph edge. In the dual Lipschitz polytope, the tight equations are \(f(u)-f(v)=\pm1\). Their incidence-matrix rank is \(2n-c\), where \(c\) is the number of connected components of the spanning tight-edge graph (isolated vertices included). A vertex of the \((2n-1)\)-dimensional dual, equivalently a facet of \(B_n\), occurs if and only if \(c=1\). A tight spanning tree then propagates integer values after fixing the potential at one vertex to zero. Conversely, any integer potential with all edge differences at most one and with connected spanning tight-edge graph defines a facet. This also proves that finite enumeration by integer height assignments is exhaustive.

**2. Both clique layers are nonconstant.** If the \(a\)-layer is constant, none of its clique edges is tight. Every vertex \(a_i\) has just the matching edge \(a_ib_i\) available for a tight connection, so connectedness forces every matching edge to be tight. The corresponding \(b_i\) then belongs to the two-value set \(\{c-1,c+1\}\), where \(c\) is the constant height of the \(a\)-layer. Since the \(b\)-layer is a clique, its height range is at most one, forcing it constant too; the remaining tight graph consists of \(n\) disjoint matching edges and is not connected. This contradiction proves both layers nonconstant. Every such integer-valued clique layer therefore uses **exactly** two consecutive values. Translate so that the \(a\)-layer has height set \(\{0,1\}\), and write the \(b\)-layer height set as \(\{d,d+1\}\). A matching edge and the integer one-Lipschitz inequalities imply \(d\in\{-1,0,1\}\). Within each layer the tight edges form a connected complete bipartite graph, so the entire tight-edge graph is connected exactly when there is at least one tight matching edge.

**3. Exact facet count.** If \(d=0\), the two layer words \(A,B\in\{0,1\}^n\) must both be nonconstant. A matching edge is tight precisely where the two words disagree. Thus \(A\ne B\), and the count is
\[
F_n^{(0)}=(2^n-2)(2^n-3).
\]
For \(d=1\), matching inequalities allow exactly three ordered column symbols \((A_i,B_i)=(0,1),(1,1),(1,2)\). Both layers are nonconstant precisely when the first and last symbols occur. Inclusion–exclusion gives
\[
F_n^{(+)}=3^n-2^{n+1}+1.
\]
The case \(d=-1\) is the sign-reversed equivalent and has the same count. Every listed potential is facet-defining by step 2, and normalization by the minimum of the first layer makes the cases disjoint. Therefore
\[
F_n=F_n^{(0)}+2F_n^{(+)}=4^n+2\cdot3^n-9\cdot2^n+8.
\]

**4. Symmetry orbits when \(d=0\).** Index the four symbols \((A_i,B_i)=(0,0),(0,1),(1,0),(1,1)\) by their multiplicities \(a,b,c,d_0\), with sum \(n\). Simultaneous column permutations identify configurations with equal multiplicities. Negation modulo common translation and layer swapping generate the independent swaps \(a\leftrightarrow d_0\) and \(b\leftrightarrow c\). The exact admissible patterns are either (i) \(b,c\ge1\) with \(a,d_0\ge0\) arbitrary, or (ii) precisely one of \(b,c\) is positive, with \(a,d_0\ge1\). Hence the number of such orbits is
\[
D_0(n)=\sum_{t=2}^{n}\left\lfloor\frac t2\right\rfloor
\left(\left\lfloor\frac{n-t}{2}\right\rfloor+1\right)
+\sum_{s=2}^{n-1}\left\lfloor\frac s2\right\rfloor.
\]
The first sum chooses the unordered positive multiplicities \(b,c\), totaling \(t\), and the unordered nonnegative multiplicities \(a,d_0\); the second handles the unique positive mismatch symbol and unordered positive \(a,d_0\).

**5. Symmetry orbits when \(d=\pm1\).** Layer interchange or sign reversal exchanges the two classes of potentials. For \(d=1\), the multiplicities of \((0,1),(1,1),(1,2)\) are \(x,y,z\) with \(x,z\ge1\), \(y\ge0\), and \(x+y+z=n\). The composition of layer interchange and negation acts by \(x\leftrightarrow z\). Therefore the number of orbits across both classes is
\[
D_1(n)=\sum_{t=2}^{n}\left\lfloor\frac t2\right\rfloor
=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
There is no mixing between \(d=0\) and \(d=\pm1\), since their relative level offset is preserved up to sign by the group action. Thus \(O_n=D_0(n)+D_1(n)\). Evaluating the elementary sums separately for even and odd \(n\) yields the stated cubic quasi-polynomial; summing its two parity series yields the rational generating function. The asymptotics follow from the leading powers in the facet formula and the parity formulas for \(O_n\). This gives explicit representatives for every orbit by choosing any ordered columns realizing each allowed occupation vector.

## Verification

Run `python3 verify.py` with Python 3's standard library. The program does not assume the proposed classification: it enumerates all rooted integer potentials \(A_1=0\), checks all graph-edge Lipschitz constraints and uses a disjoint-set connectivity test for the tight-edge graph. It independently verifies the facet count for \(n=2,3,4,5,6\); the first value is a small-case cross-check beyond the stated range. It also generates actual group actions and checks the complete disjoint orbit decomposition for \(n=3,4,5\), comparing all counts against the analytic formulas. Expected output ends with `ALL EXACT CHECKS PASSED`. These finite checks corroborate but do not replace the proof for all integers \(n\ge3\).

## Relationship to prior work

Higashitani, Jochemko and Michałek (arXiv:1807.07678, Theorem 3.1) give the general tight-edge facet criterion and formulas for complete and complete multipartite graphs. That general criterion is used, not presented as new. D'Alì, Delucchi and Michałek (arXiv:1910.05193, Section 4) study cycles, joins and other graph operations, rather than evaluating the two-layer complete-graph Cartesian product. Çelik, Jamneshan, Montúfar, Sturmfels and Venturello (arXiv:2003.06725, Section 4) explicitly identify Cartesian products of complete graphs as Hamming-metric Lipschitz polytopes and discuss small graph products, but do not supply the all-\(n\) two-row rook facet and symmetry formulas here. Chen, Davis and Korchevskaia (arXiv:2107.12315) investigate general facet subgraphs; their classification principles do not themselves yield the evaluated formulas above. The preceding literature thus establishes the framework and motivation; the contribution claimed here is the explicit full-family enumeration and orbit classification.

## Limitations

The result is restricted to the real, unweighted, two-layer graph family with \(n\ge3\); it asserts neither a complete face vector nor facet orbits for more than two Cartesian factors. The symmetry count is for graph symmetries and central inversion, not necessarily every linear or combinatorial symmetry. The computer checks are finite tests, not a proof of the unrestricted theorem. A bibliographically unindexed equivalent formula or dataset remains a risk; no independent scientific audit has been performed.

## References

1. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278 (first public 26 October 2018), https://arxiv.org/abs/1810.11278.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (2018), https://arxiv.org/abs/1807.07678.
3. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), https://arxiv.org/abs/1910.05193.
4. T. Ö. Çelik, A. Jamneshan, G. Montúfar, B. Sturmfels and L. Venturello, *Wasserstein Distance to Independence Models*, arXiv:2003.06725 (2020), https://arxiv.org/abs/2003.06725.
5. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (2021), https://arxiv.org/abs/2107.12315.
6. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (2022), https://arxiv.org/abs/2201.13303.
