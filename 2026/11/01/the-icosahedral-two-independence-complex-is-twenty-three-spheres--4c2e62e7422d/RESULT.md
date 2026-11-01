# The icosahedral two-independence complex is twenty three-spheres with a five-dimensional antipodal-odd summand

## Finding
Let \(I\) be the graph of the regular icosahedron, with twelve vertices. Its two-independence complex \(K=\operatorname{Ind}_2(I)\) has the exact **integral homotopy type**
\[
K\simeq\bigvee^{20}S^3.
\]
Its full rational automorphism representation, for \(\operatorname{Aut}(I)\cong A_5\times C_2\), is
\[
\widetilde H_3(K;\mathbb Q)\cong
(\mathbf 1\oplus V_4\oplus2V_5)\boxtimes\mathbf 1
\;\oplus\; V_5\boxtimes\varepsilon,
\]
where \(V_4\) and \(V_5\) are the rational irreducible representations of \(A_5\) of dimensions four and five; \(\varepsilon\) is the nontrivial rational character of the central antipodal \(C_2\). In particular the antipodal involution has \(+1\) and \(-1\) eigenspace dimensions fifteen and five on rational third homology. The integral third homology is free of rank twenty, and all other reduced integral homology groups vanish.

## Assumptions and scope
For a finite graph \(G\), the two-independence complex consists of vertex subsets \(S\) for which each connected component of the induced graph \(G[S]\) contains at most two vertices. Equivalently, every vertex of \(G[S]\) has induced degree at most one. A graph model for \(I\), on vertex labels \(0,\ldots,11\), is encoded by the following thirty unordered edges:

```
(0,1) (0,5) (0,7) (0,8) (0,11)
(1,2) (1,5) (1,6) (1,8)
(2,3) (2,6) (2,8) (2,9)
(3,4) (3,6) (3,9) (3,10)
(4,5) (4,6) (4,10) (4,11)
(5,6) (5,11)
(7,8) (7,9) (7,10) (7,11)
(8,9) (9,10) (10,11)
```

The exact enumeration and matching proof below concern this fixed finite graph, not arbitrary five-regular graphs. The homotopy theorem is integral; the displayed equivariant **decomposition** is only asserted over \(\mathbb Q\), not as a decomposition of integral lattices.

## Proof
**1. Exhaustive face set.** Represent a subset by the twelve-bit integer \(s=\sum_{v\in S}2^v\). Let \(N(v)\) be the neighbor mask of vertex \(v\). A mask is a face if and only if
\[
\bigl|S\cap N(v)\bigr|\le1\quad\text{for every }v\in S.
\]
The standalone program `verify.py` constructs exactly all \(4096\) masks and tests this predicate with integer bit counts. It finds precisely \(324\) faces including the empty face; its nonempty face counts in dimensions zero through three are \((12,66,140,105)\). All \(105\) tetrahedra are maximal, and there are no higher-dimensional faces.

**2. Reproducible discrete-Morse matching.** Process the graph-vertex pivots in exactly this order:
```
4, 8, 2, 9, 11, 5, 3, 6, 0, 1, 7, 10
```
At each pivot \(v\), in the currently unmatched face set pair each still-unmatched face \(S\) not containing \(v\) with \(S\cup\{v\}\), if both are still unmatched. The code specifies an unambiguous processing order (increasing face size, then mask). This pairs \(304\) augmented faces in \(152\) pairs and leaves precisely \(20\) critical faces, all tetrahedra. To verify **acyclicity**, direct every Hasse edge from coface to face, except reverse paired edges. The program constructs all \(984\) such incidences and performs topological sorting. It visits all \(324\) faces, so this finite graph has no directed cycle. The counts, pairing and topological-sort assertion are exact integer calculations that can be fully replayed from the supplied source.

The augmented empty face is paired to a vertex. Remove that one pair from the matching; the empty face is omitted in the ordinary face poset, leaving exactly one critical vertex and the twenty critical three-simplices. Removing the empty pair cannot create a directed cycle: the corresponding vertex becomes unmatched and the empty face is absent, whereas all incidences among nonempty faces retain their original orientation. Forman's acyclic-matching theorem supplies a CW homotopy model with one zero-cell, twenty three-cells and no cells in dimensions one or two. All three-cell attaching maps land in a point, so the model is the stated wedge of twenty three-spheres. Thus the homotopy equivalence and torsion-freeness are integral and exact.

**3. Automorphisms and signed Lefschetz character.** `verify.py` explicitly lists a compatible cyclic order of the five neighbors at each vertex. These orders induce the usual oriented triangular embedding of the icosahedron: each edge bounds two triangles with opposite induced edge orientations, giving its spherical rotation system. A depth-first search enumerates all adjacency-preserving permutations, obtaining exactly \(120\), and distinguishes the \(60\) orientation-preserving automorphisms from the \(60\) reversing ones. The preserving subgroup is the rotational icosahedral group \(A_5\); its unique commuting order-two inversion \(z\) yields \(\operatorname{Aut}(I)\cong A_5\times\langle z\rangle\).

For each automorphism \(g\), a face fixed setwise contributes the sign of its induced vertex permutation, weighted by \((-1)^{\dim S}\), to the ordinary Lefschetz number:
\[
L(g)=\sum_{\varnothing\ne S\in K:\;gS=S}(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
Only \(H_0\cong\mathbb Z\) and \(H_3\cong\mathbb Z^{20}\) survive, hence \(\operatorname{tr}(g|\widetilde H_3)=1-L(g)\). The exhaustive signed-face counts give, for proper rotations of orders \(1,2,3,5\), traces \(20,4,-1,0\); for their products with \(z\), traces \(10,2,1,0\). The program checks every one of the \(120\) permutations, not just representatives.

The \(z\)-even and \(z\)-odd rational characters on the four rotation-order classes are, respectively,
\[
\chi_+=(15,3,0,0),\qquad\chi_-=(5,1,-1,0).
\]
Comparing these values to the standard rational \(A_5\)-characters \(\chi_{\mathbf1}=(1,1,1,1)\), \(\chi_{V_4}=(4,0,1,-1)\), and \(\chi_{V_5}=(5,1,-1,0)\) proves \(\chi_+=\chi_{\mathbf1}+\chi_{V_4}+2\chi_{V_5}\) and \(\chi_-=\chi_{V_5}\). Character semisimplicity over characteristic zero gives exactly the stated rational direct sum.

## Verification
Execute `python3 verify.py` from the directory containing the embedded files; the program depends only on the Python standard library. Its required success marker is `ICOSAHEDRAL_TWO_INDEPENDENCE_EXACT_MORSE_AND_SYMMETRY_OK`. The accompanying `verification_output.txt` gives the expected stdout. Independent reduced mod-two boundary calculations yield ranks \(11,55,85\) in degrees one, two, three, respectively, and third Betti number twenty. This second calculation checks numerical homology but is **not** substituted for the integral homotopy proof provided by the full acyclic matching. The exact graph, matching, Hasse digraph and graph automorphisms are all reconstructed from embedded source, without external graph libraries.

## Relationship to prior work
Deshpande and Singh introduced systematic homotopy classification of higher independence complexes and a sequential elementary-Morse matching method. Their full article treats complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees; it does not give this particular icosahedral calculation. Abdelmalek and collaborators investigate vertex-decomposability and higher independence for chordal graphs and selected related families; the icosahedral graph is nonchordal and not in those theorems' stated cases. Related calculated icosahedral open-neighborhood, distance-neighborhood and three-cut complexes are distinct simplicial complexes and do not determine \(\operatorname{Ind}_2(I)\). The present result determines both its complete integral homotopy type and its rational full-automorphism action.

## Limitations
This is an exact finite classification for the icosahedral graph alone, not an all-graphs theorem. The representation decomposition is over \(\mathbb Q\); no splitting of the integral automorphism lattice is asserted. A complete novelty guarantee against uncatalogued work is not claimed. The full text of recent work on the Alexander dual of higher independence complexes was not available for close theorem-by-theorem comparison in this report; its abstract concerns primarily structural graph classes rather than this specific automorphism representation, but an indirect implication cannot be categorically excluded.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, first submitted 2020-01-15, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, first submitted 2021-06-21, arXiv:2106.10863, https://arxiv.org/abs/2106.10863.
3. P. Deshpande, A. Roy and R. Sawant, *The complex of r-co-connected subgraphs, chordality and Fröberg's theorem*, first submitted 2025-10-29, arXiv:2510.25710, https://arxiv.org/abs/2510.25710 (abstract inspected only; comparison remains limited).
