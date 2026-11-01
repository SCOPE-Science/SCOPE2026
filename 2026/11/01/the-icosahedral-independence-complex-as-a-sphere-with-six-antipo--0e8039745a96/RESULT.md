# The icosahedral independence complex as a sphere with six antipodal chords

## Finding
Let \(I\) be the ordinary twelve-vertex icosahedral graph and \(K=\operatorname{Ind}(I)\) its simplicial complex of independent vertex sets. Define \(B\subset K\) using every vertex, each edge joining vertices at graph distance two in \(I\), and every triangle whose three edges have distance two. Then \(B\) is a combinatorial two-sphere. The remaining simplices of \(K\) are exactly the six antipodal edges, with no higher-dimensional simplex containing any of them. This decomposition is invariant under the complete automorphism group \(G=\operatorname{Aut}(I)\cong A_5\times C_2\).

Consequently
\[
K\simeq S^2\vee\bigvee^{6}S^1,\qquad \pi_1(K)\cong F_6,
\]
with \(H_1(K;\mathbb Z)\cong\mathbb Z^6\), \(H_2(K;\mathbb Z)\cong\mathbb Z\), and all other reduced integral homology zero. In the canonical six-chord basis, \(G\) acts on \(H_1\) by signed permutations of the oriented antipodal pairs. This signed-permutation action lifts to the corresponding outer action on \(\pi_1(K)\). The central antipodal involution acts by \(-1\) on both positive-degree integral homology groups, while the rotation subgroup acts trivially on \(H_2\).

If \(W_6\) denotes the rationally irreducible six-dimensional representation of \(A_5\) whose complexification is the sum of the two distinct three-dimensional complex irreducibles \(V_3\oplus V_3'\), and \(\varepsilon\) is the nontrivial character of the central \(C_2\), the full rational representations are
\[
H_1(K;\mathbb Q)\cong W_6\boxtimes\varepsilon,
\qquad
H_2(K;\mathbb Q)\cong\mathbf 1\boxtimes\varepsilon.
\]
Hence \(K/A_5\) has the rational homology of \(S^2\) and \(K/G\) is rationally acyclic.

## Assumptions and scope
Everything refers to the *ordinary* independence complex, not the Lovász neighborhood, matching, or distance-neighborhood complex. The graph has vertices \(N,S,u_i,v_i\), where \(i\in\mathbb Z/5\mathbb Z\). Its edges are \(Nu_i\), \(Sv_i\), \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\), and \(u_iv_{i-1}\). An independent set has no pair joined by these edges. Graph distances are unweighted shortest-path distances in \(I\). The antipodal involution sends every vertex to its unique vertex at distance three. All homology groups are *ordinary* singular/simplicial groups unless reduced notation appears. Coefficients and group actions are specified explicitly; no statement about torsion in other complexes or arbitrary icosahedral graph modifications is made.

## Proof
**1. Graph-distance partition and the spherical subcomplex.** Every vertex has five neighbors at distance one, five vertices at distance two, and one vertex at distance three. The six distance-three pairs are \(\{N,S\}\) and \(\{u_i,v_{i+2}\}\), for \(i\in\mathbb Z/5\mathbb Z\). The distance-two graph \(I_2\) has thirty edges, and an explicit graph isomorphism \(\phi:I_2\to I\) is
\[
\phi(N)=N,\quad \phi(S)=S,\quad
\phi(u_i)=v_{2i+1},\quad \phi(v_i)=u_{2i}.
\]
All subscripts are modulo five. Verification consists of checking the six displayed edge families of \(I\) against the distance-two adjacency lists; the accompanying independent checker tests all \(66\) unordered vertex pairs. As the graph of the icosahedron is a maximal planar triangulation with twenty triangular faces and no four-cliques, the clique complex of \(I_2\) is a simplicial two-sphere. Its face numbers are \((12,30,20)\).

**2. The independence complex contains exactly six extra edges.** Each pair of nonadjacent vertices of \(I\) has distance two or three, so the one-skeleton of \(K\) is the union of \(I_2\) with the six antipodal edges. The open neighborhoods of the two endpoints of an antipodal pair partition the other ten vertices, so no independent triple can contain an antipodal pair. Every independent triple must therefore be a triangle of \(I_2\); there are twenty. No independent set of cardinality four exists. Thus \(K=B\cup\bigcup_{e\in E_3}e\), and every added edge meets \(B\) precisely at its endpoints. A sphere with six additional one-cells between points of that connected sphere is homotopy equivalent to \(S^2\vee\bigvee^6 S^1\). The decomposition proves the *integral* homology and free fundamental group, without using finite-field Betti numbers to infer torsion-freeness.

**3. Canonical integral and fundamental-group actions.** The full graph automorphism group preserves graph distance, hence \(B\) and its six antipodal chord edges. The long exact sequence of \((K,B)\), together with \(H_1(B;\mathbb Z)=0\) and \(H_0(B;\mathbb Z)\cong H_0(K;\mathbb Z)\), gives a canonical equivariant isomorphism \(H_1(K;\mathbb Z)\cong H_1(K,B;\mathbb Z)\), whose right side is the free group on the six oriented chord one-cells. Graph automorphisms permute these generators, reversing the sign exactly when the orientation of a chord is reversed. Similarly, choosing a basepoint in \(B\) and paths in \(B\) to chord endpoints produces six free generators for \(\pi_1(K)\). Paths between fixed endpoints in \(B\cong S^2\) are unique up to homotopy, so under change of basepoint the induced outer automorphism permutes and inverts those generators according to the same oriented-chord action. This describes the complete \(G\to\operatorname{Out}(F_6)\) action.

**4. The top class and character.** The sphere subcomplex has one integral fundamental class. The sixty geometric rotations preserve its orientation; central antipodal inversion reverses it, since the antipodal involution acts freely on \(B\cong S^2\) and has degree \(-1\) by the fixed-point-free Lefschetz formula. Thus \(H_2\) has the stated orientation character. The signed six-axis permutation character on the rotation subgroup \(A_5\), grouped by element order \(1,2,3,5\), takes values \(6,-2,0,1\); the respective numbers of elements are \(1,15,20,24\). (The order-five elements comprise two conjugacy classes of twelve, both with trace one.) The standard \(A_5\) character table identifies this as \(\chi_{V_3}+\chi_{V_3'}\). These are conjugate over \(\mathbb Q(\sqrt5)\), so their rational descent is the *six-dimensional rationally irreducible* module \(W_6\), not two independent rational three-dimensional modules. Central inversion swaps both ends of every chord, so it negates the entire signed chord module. Averaging the two character values over the finite symmetry groups gives positive-degree rational invariant dimensions \((0,1)\) for \(A_5\) and \((0,0)\) for \(G\). The rational transfer/invariants theorem for finite-group quotients (after equivariant subdivision) proves the quotient statements.

## Verification
Run `python3 verify_icosahedral.py` in the same directory. The checker uses Python's standard library only. It independently enumerates all independent faces, distance partitions, the explicitly supplied graph isomorphism, all twelve vertex links of the spherical subcomplex, and an integral orientation cycle. It then enumerates all \(120\) graph automorphisms via adjacency-preserving backtracking and checks the top orientation degree and signed chord trace for each. It also calculates simplicial boundary ranks modulo \(2,3,5,101\), consistently obtaining ranks \(11\) and \(19\). The exact homotopy and integral freeness conclusions do *not* rely on these modular tests; they follow from Steps 1–3. Recorded output is `verify_output.txt`.

## Relationship to prior work
Barmak's 2010 independence-complex paper provides the general definitions and topological context, not this graph's equivariant fundamental-group action. Established icosahedral-graph references explicitly record its self-isomorphism to the distance-two graph and its automorphism group; that graph fact is an acknowledged key input, not a discovery asserted here. The contribution is the exact equivariant decomposition of the **independence complex** into a spherical subcomplex and six antipodal chords and the resulting outer fundamental-group action and graded *integral* homology modules. Nearby equivariant calculations for the icosahedral *neighborhood* complex concern another functor and have different Betti numbers; they do not imply these homology modules. Equivalence through older, unindexed computations cannot be ruled out.

## Limitations
This is a single canonical finite graph, not a general theorem on all Platonic graphs. The rational six-dimensional module is irreducible over \(\mathbb Q\) but splits after scalar extension to \(\mathbb C\); identifying its two complex constituents individually over \(\mathbb Q\) would be incorrect. This work does not determine equivariant simple-homotopy refinements, integral homology of arbitrary quotients, or unspecified coefficient systems. Publication priority remains provisional pending wider independent literature checking; no independent validation has been performed.

## References
1. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, publicly submitted 2010-07-02, https://arxiv.org/html/1007.0418v1.
2. Eric W. Weisstein, *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html (distance-two graph and automorphism-group facts; webpage's revision date is not treated as the original publication date).
3. David A. Craven, *Character tables*, University of Bristol, https://people.maths.bris.ac.uk/~matyd/GroupNames/characters.html (\(A_5\) irreducible-character table).
4. DistanceRegular.org, *Icosahedron*, https://www.math.mun.ca/distanceregular/graphs/icosahedron.html (intersection array and symmetry group).
