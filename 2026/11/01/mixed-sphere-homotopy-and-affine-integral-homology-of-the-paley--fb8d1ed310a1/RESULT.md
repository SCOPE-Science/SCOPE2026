# Mixed sphere homotopy and affine integral homology of the Paley-thirteen dissociation complex

## Finding

Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\) with adjacency \(i\sim j\) precisely when \(i-j\in\{1,3,4,9,10,12\}\). Write \(X=\operatorname{Ind}_2(P_{13})\) for the simplicial complex of all subsets whose induced connected components contain at most two vertices. Equivalently, each induced vertex degree is at most one, and \(X\) is the first forest-filtration complex \(\mathcal F_1(P_{13})\).

**Theorem.** The complex \(X\) is pure of dimension three, with exactly 78 tetrahedral facets, but
\[
 X\simeq S^2\vee S^3\vee S^3.
\]
In particular, it is not shellable. Its full graph automorphism group is \(G\cong C_{13}\rtimes C_6\), consisting of all maps \(x\mapsto ux+b\) for \(u\in\{1,3,4,9,10,12\}\) and \(b\in\mathbb F_{13}\). On the complete reduced **integral** homology, translations act trivially; writing \(a:x\mapsto4x\),
\[
 \widetilde H_2(X;\mathbb Z)\cong\mathbb Z_{\mathrm{sign}},\quad a\cdot z=-z,
 \qquad \widetilde H_3(X;\mathbb Z)\cong\mathbb Z[\omega],\quad a\cdot w=\omega w,
\]
where \(\omega^2+\omega+1=0\). These are isomorphisms of integral \(G\)-modules; in the rank-two case the choice between \(\omega\) and \(\omega^2\) produces isomorphic integral modules. All other reduced integral homology groups vanish. Consequently, \(\widetilde H_j(X/G;\mathbb Q)=0\) for every integer \(j\).

## Assumptions and scope

The vertex set is the thirteen explicitly labeled elements \(0,\ldots,12\). A face is a nonempty bitmask \(S\) satisfying \(|N(v)\cap S|\le1\) for every \(v\in S\); the empty face is included abstractly. Every face of cardinality four is a tetrahedron. The finite chain calculations use increasing vertex order for simplex orientations. These conventions uniquely specify the object and its group action.

The historical archive source is Conant and Thistlethwaite's hypergraph-complex work, first publicly posted on **2008-08-05**. The explicit graph \(P_{13}\) and the equivalence with higher independence/forest-filtration notation are distinguished from that background, not attributed to that article as an already computed example.

## Proof

**1. Exact combinatorial model.** A subset fails to be a face exactly when it contains some triple \(\{u,v,w\}\) with \(u,w\in N(v)\) distinct. There are exactly 143 different such forbidden triples. Independent enumeration through this forbidden-triple formulation and through induced vertex degrees agrees on all \(2^{13}=8192\) subsets. The nonempty face vector, by dimensions zero through three, is
\[
 (13,78,143,78).
\]
There are no faces of higher dimension, and all maximal faces have dimension three: exactly 78 tetrahedra.

**2. Integral Morse reduction.** Iterate the elementary vertex matching for \(v=0,1,\ldots,12\). At stage \(v\), pair every remaining face \(S\) not containing \(v\) with \(S\cup\{v\}\), whenever both faces remain. This is the standard sequential element matching; its acyclicity also follows by the complete explicit directed Hasse-graph check in `VERIFY.py`. The matching has 149 pairs and exactly one critical vertex, six critical triangles, and seven critical tetrahedra. Its directed Hasse graph has 312 vertices and 897 incidences; topological sorting visits all 312 vertices.

Cancel each matched unit pair over \(\mathbb Z\), using oriented simplicial incidence numbers. In ascending bitmask order on the surviving six triangles and seven tetrahedra, the integral degree-three Morse boundary is exactly
\[
 \partial_3=\begin{pmatrix}
0&0&-1&1&0&0&1\\
0&-1&0&1&0&0&0\\
1&-1&0&0&0&0&0\\
0&1&-1&0&0&0&1\\
0&0&0&1&-1&0&0\\
0&0&0&0&1&-1&1
\end{pmatrix}.
\]
The first, second, fourth rows sum to zero with coefficients \((-1,1,1)\), so the rank is at most five. The submatrix consisting of rows numbered \(0,1,2,4,5\) and columns \(0,1,2,3,4\) (zero-based) has determinant \(-1\), so the rank is exactly five and its nonzero Smith factors are all one. In the resulting simply connected CW model, the six two-cells form a wedge of six two-spheres. Each three-cell attaches by a map in \(\pi_2(\bigvee^6 S^2)\cong\mathbb Z^6\), completely specified by this integer matrix. Integral elementary basis changes yield five degree-one attaching maps and two zero maps. Their homotopy cofiber is \(S^2\vee S^3\vee S^3\). This is an integral homotopy equivalence, not just a field-homology statement.

A pure shellable three-dimensional simplicial complex has reduced homology concentrated in dimension three. Because \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z\), \(X\) cannot be shellable.

**3. Integral symmetry modules.** The natural full automorphism group of \(P_{13}\) is \(G=C_{13}\rtimes C_6\) as specified above. It preserves the face rule. Every order-thirteen translation acts trivially on \(\widetilde H_2\cong\mathbb Z\). It also acts trivially on \(\widetilde H_3\cong\mathbb Z^2\): a nontrivial rational representation of a cyclic group of prime order thirteen has dimension at least twelve, because the cyclotomic polynomial has degree twelve.

It remains to determine the action of \(a:x\mapsto4x\), of order six. Exhaustively counting fixed oriented faces and their signs gives reduced simplicial Lefschetz numbers for \(a^j\), for \(j=0,\ldots,5\), of
\[
 (-1,\;0,\;2,\;-3,\;2,\;0).
\]
The involution \(a^3:x\mapsto-x\) has fixed-face contributions by dimensions zero through three of \((1,6,-3,-6)\); subtracting one for the reduced degree-zero term gives \(-3\). On the rank-one second homology its trace is either \(+1\) or \(-1\), whereas its trace on rank-two third homology must lie in \(\{-2,0,2\}\). The equation
\[
 -3=\operatorname{tr}(a^3\mid\widetilde H_2)-\operatorname{tr}(a^3\mid\widetilde H_3)
\]
forces these traces to be \(-1\) and \(2\), respectively. Hence \(a\) acts by \(-1\) on second homology and \(a^3\) acts trivially on third homology. The reduced Lefschetz number for \(a\) is zero, so its third-homology trace is \(-1\). Its characteristic polynomial on the rank-two lattice is therefore \(t^2+t+1\), making that lattice a rank-one torsion-free module over \(\mathbb Z[\omega]\). Since the Eisenstein ring is Euclidean, this module is free of rank one; \(a\) acts as multiplication by \(\omega\), up to integral conjugacy. The full integral module statement follows.

**4. Quotient.** Neither the sign line nor the rational Eisenstein plane has any \(G\)-invariant vector. Rational homology of a finite simplicial-group quotient equals the invariant part of rational homology, after barycentric subdivision if necessary to remove inversions. Therefore all reduced rational homology of \(X/G\) vanishes.

## Verification

`VERIFY.py` is self-contained Python 3 (standard library only). Run `python3 VERIFY.py` and compare with `VERIFY_OUTPUT.txt`. It enumerates all 8192 subsets by two independent membership tests, checks purity and all 897 oriented cover incidences, explicitly tests acyclicity, performs exact integral unit-pivot Morse cancellation, displays the full six-by-seven matrix, proves a unit minor, and independently computes complete simplicial boundary ranks modulo \(2,3,5,101\). It also computes the full 78-element affine group's signed Lefschetz traces. Its terminating marker is `ALL_CHECKS_PASS`. The integral homotopy interpretation and Eisenstein-module argument are mathematical deductions from the exact finite certificate; experiments on larger Paley graphs are neither needed nor claimed.

## Relationship to prior work

The 2008 hypergraph independence/theta-complex framework of Conant and Thistlethwaite motivates the independence-of-forbidden-triples interpretation, but its identifiable results concern other hypergraphs. The full text of Deshpande and Singh's higher-independence paper (first posted 2020-01-15) covers complete multipartite and whiskered graphs, paths, cycles and perfect rooted trees; none is the Paley-thirteen graph. Carnero Bravo's forest filtration (first posted 2023-07-25) is especially relevant since its first stage \(\mathcal F_1(G)\) equals \(\operatorname{Ind}_2(G)\) for every graph, but the examined main family sections cover paths, cycles, double stars, cactus graphs, joins, wheels and specified products, not the present affine representation. Published Paley graph descriptions establish the graph's toroidal character and the order-78 affine group, not the topological claim here. The ordinary independence, clique and neighborhood complexes are distinct constructions and cannot supply the stated homotopy or module without further argument.

## Limitations

This is an exact statement for the graph on thirteen vertices at higher-independence parameter two. It gives no analogous classification for other Paley orders or other forest-filtration stages. The orbit-space conclusion concerns rational homology only, not integral torsion or homotopy. Publication-priority searches did not find a covering result, but a mathematically equivalent unindexed or inaccessible paper remains possible. Independent mathematical evaluation has not been performed.

## References

1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739, first version dated 2008-08-05, https://arxiv.org/abs/0808.0739.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first version dated 2020-01-15, https://arxiv.org/abs/2001.05448.
3. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first version dated 2023-07-25, https://arxiv.org/abs/2307.13271.
4. A. E. Brouwer, *Paley graphs*, graph-data exposition, https://aeb.win.tue.nl/graphs/Paley.html (public page without relied-upon publication date).
