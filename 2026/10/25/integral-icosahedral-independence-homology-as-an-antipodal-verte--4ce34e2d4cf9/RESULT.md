# Integral icosahedral independence homology as an antipodal vertex lattice

## Finding
Let \(I\) be the twelve-vertex graph of a regular icosahedron, \(K=\operatorname{Ind}(I)\) its ordinary independence complex, and \(G=\operatorname{Aut}(I)\cong A_5\times C_2\). Write \(\alpha\) for the central antipodal involution on vertices, and let \(\mathbb Z^V\) be the integral permutation lattice on the vertices. There is a **canonical integral \(G\)-module isomorphism**
\[
H_1(K;\mathbb Z)\cong\{c\in\mathbb Z^V:\alpha c=-c\},
\]
where the right side is the rank-six integral *anti-invariant* vertex lattice. Furthermore, \(H_2(K;\mathbb Z)\cong\mathbb Z\) with the character trivial on \(A_5\) and negative on \(\alpha\), and no other reduced integral homology occurs. The non-equivariant homotopy type is
\[
K\simeq S^2\vee\bigvee^{6}S^1.
\]
If \(W_6\) denotes the six-dimensional irreducible **rational** representation of \(A_5\) whose complexification is the sum of its Galois-conjugate three-dimensional irreducibles, and \(\varepsilon\) is the sign character of the central \(C_2\), then
\[
H_1(K;\mathbb Q)\cong W_6\boxtimes\varepsilon,
\qquad H_2(K;\mathbb Q)\cong\mathbf1\boxtimes\varepsilon.
\]
For rotational conjugacy classes of orders \(1,2,3,5\) (the two order-five classes agree), the degree-one character is \((6,-2,0,1,1)\); multiplying any rotation by \(\alpha\) negates that character. In particular, all positive-degree rational homology fixed by the entire group is zero, while the rotationally fixed degree-two homology has dimension one.

## Assumptions and scope
Use the vertex set \(V=\{T,B,u_i,v_i:i\in\mathbb Z/5\mathbb Z\}\), with the thirty edges
\[
Tu_i,\quad Bv_i,\quad u_iu_{i+1},\quad
v_iv_{i+1},\quad u_iv_i,\quad u_iv_{i-1}.
\]
for each cyclic index \(i\), and **no other edges**. In this model the antipodal pairs are \(\{T,B\}\) and \(\{u_i,v_{i+2}\}\). (All indices are modulo five.) An independence simplex is a set containing no edge of \(I\). All graph automorphisms act simplicially on \(K\), and homology is ordinary unreduced homology unless a tilde is displayed.

The claim is about the *independence* complex, equivalently the clique complex of the complement graph. It is not a Lovász open-neighborhood complex, a distance-neighborhood complex, a matching complex, or a Vietoris--Rips complex.

## Proof
**1. Exact distance decomposition.** From the six displayed edge families the graph has distance partition \((1,5,5,1)\) around every vertex. In particular every \(x\) has a unique antipode \(\alpha(x)\) at distance three, and for every vertex \(y\), \(d_I(\alpha(x),y)=3-d_I(x,y)\). Directly from the adjacency lists, the distance-two graph \(J\) has precisely the following thirty edges as \(i\) runs through \(\mathbb Z/5\mathbb Z\):
\[
Tv_i,\quad Bu_i,\quad u_iu_{i+2},\quad v_iv_{i+2},\quad
u_iv_{i+1},\quad u_iv_{i+3}.
\]
It is itself an icosahedral graph: the map \(T\mapsto T\), \(B\mapsto B\), \(u_i\mapsto v_{2i}\), \(v_i\mapsto u_{2i+4}\) sends each original graph edge bijectively to a distance-two edge. Hence the clique complex \(S=\operatorname{Cl}(J)\) is exactly the triangulated boundary \(S^2\) of an icosahedron, with face vector \((12,30,20)\), and has no tetrahedron.

**2. The independence complex is a sphere with six attached diameters.** The pairs of distinct vertices nonadjacent in \(I\) are precisely the thirty distance-two pairs in \(J\) and the six antipodal pairs. An antipodal pair cannot be contained in an independent triple: for any third vertex \(y\), the distance identity above forces either \(d_I(x,y)=1\) or \(d_I(\alpha(x),y)=1\). Thus every independent triangle belongs to \(S\). Since \(J\) has no clique of size four and no antipodal edge lies in a triangle, no independent set has size four. Therefore, *as a simplicial complex*, \(K\) is the union of the two-sphere \(S\) and the six additional edges \(\{x,\alpha(x)\}\), whose endpoints belong to \(S\), but whose interiors are disjoint from it and from each other. The exact face vector of \(K\) is \((12,36,20)\). Attaching each such one-cell to an already path-connected simply connected sphere adds one free circle, proving the claimed homotopy type. This also proves integral homology is torsion-free, not merely its rational ranks.

**3. Canonical integral module.** Because the action preserves graph distances, both \(S\) and the set \(E_\alpha\) of six antipodal edges are invariant. In the pair \((K,S)\), the relative cellular complex has only one nonzero group, \(C_1(K,S;\mathbb Z)=\mathbb Z[E_\alpha]\), with oriented edges, and zero relative boundary. Since \(H_1(S;\mathbb Z)=0\) and \(H_0(S;\mathbb Z)\to H_0(K;\mathbb Z)\) is an isomorphism, the natural long exact sequence yields a \(G\)-equivariant isomorphism \(H_1(K;\mathbb Z)\to H_1(K,S;\mathbb Z)\). The identification \([x,\alpha(x)]\mapsto e_x-e_{\alpha(x)}\) is an isomorphism of this oriented-edge lattice with the anti-invariant vertex lattice. The same long exact sequence identifies \(H_2(K;\mathbb Z)=H_2(S;\mathbb Z)\).

**4. Orientation and character.** The rotational subgroup \(A_5\) acts trivially on the sphere orientation since it is a simple group and orientation is a one-dimensional sign character. The central antipode fixes no vertex, edge, or triangle of \(S\) setwise: antipodal edges are *absent from* \(S\), and an invariant odd-sized triangle would require a fixed vertex. The simplicial Lefschetz number on \(S\) of \(\alpha\) is therefore zero; since it equals \(1+\deg(\alpha)\), the degree is \(-1\). On oriented antipodal edges, \(\alpha\) acts as \(-1\). The trace on \(H_1\) for any \(g\in A_5\) is \(\bigl(f(g)-f(\alpha g)\bigr)/2\), where \(f(h)\) counts vertices fixed by \(h\). The counts are \((f(g),f(\alpha g))=(12,0),(0,4),(0,0),(2,0)\) for rotational orders \(1,2,3,5\), respectively, giving \((6,-2,0,1,1)\). The standard rational character table of \(A_5\) identifies this as \(\chi_3+\chi_{3'}\), the irreducible rational character \(W_6\). Every nonrotation is \(\alpha g\) and negates both positive-degree characters, completing the proof.

## Verification
The accompanying `verify_icosahedron.py` reconstructs the graph solely from the six declared edge families; enumerates all independent simplices; certifies that exactly 30 complementary edges occur in exactly two independent triangles and exactly six in none; checks every vertex link in the 20-triangle subcomplex is a five-cycle and its Euler characteristic is two; verifies the explicit distance-two graph isomorphism and identifies the antipodal pairs; constructs an integral fundamental 2-cycle with opposite signs around every edge; enumerates all 120 graph automorphisms; checks that each preserves the subcomplex, that the antipode is central and orientation-reversing, and that every character value is correct. Its final success marker is `VERIFY_OK_ICOSAHEDRAL_INDEPENDENCE_INTEGRAL_MODULE`. Run with Python 3 and `networkx` as specified in `requirements.txt`.

The verifier's finite enumerations check the combinatorial statements in this proof for this one graph; the long exact sequence and the character-theoretic decomposition are written above as mathematical arguments. No inference from a finite sample to an infinite family is made.

## Relationship to prior work
Engström's 2005 works introduce the independence complex and develop general homotopy-reduction and claw-free-graph connectivity tools. The icosahedral graph is claw-free, but the published general connectivity bounds do not provide its mixed-dimensional homotopy decomposition, its integral signed permutation module, or this complete group character. Standard graph tables give its vertex count, independence number and automorphism-group order but do not determine the homology representations.

Two relevant same-graph published computations concern different functors. *Complete integral homotopy classification of the icosahedral distance-neighborhood complexes* computes complexes generated by distance-shell unions \(\bigcup_v\Delta(N_D(v))\); none of those definitions is \(\operatorname{Ind}(I)\). *Rational icosahedral symmetry on the neighborhood complex* computes \(H_2(\mathcal N(I);\mathbb Q)\) for an open-neighborhood complex with 264 nonempty faces, whereas the current independent-set complex has 68 nonempty faces and nonzero first homology. In particular neither theorem implies the asserted **integral anti-invariant vertex lattice** even though their symmetry groups agree. The analogous dodecahedral-graph independence calculation concerns the different 20-vertex graph. These are implication comparisons rather than claims that absence of a search hit proves novelty.

## Limitations
This theorem concerns the one twelve-vertex icosahedral graph; it does not classify independence complexes of other Platonic graphs, describe equivariant homotopy types, or determine the full homotopy action beyond induced homology modules. The rational identification with conjugate three-dimensional irreducibles does not separately provide a preferred integral splitting into two rank-three lattices. Equivalent work not found by the cited focused searches could exist.

## References
1. Alexander Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, publicly submitted 8 August 2005, especially Section 3, https://arxiv.org/abs/math/0508148.
2. Alexander Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, publicly submitted 17 December 2005, especially Sections 2–3, https://arxiv.org/abs/math/0512420.
3. E. W. Weisstein, *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html (graph parameters and symmetry group, not an equivariant homology theorem).
4. *Complete integral homotopy classification of the icosahedral distance-neighborhood complexes*, publicly indexed result identifier `137f948604a4`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-integral-homotopy-classification-of-the-icosahedral-dis--137f948604a4 (different complex).
5. *Rational icosahedral symmetry on the neighborhood complex*, publicly indexed result identifier `5d7e0af98d39`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rational-icosahedral-symmetry-on-the-neighborhood-complex--5d7e0af98d39 (different complex).
