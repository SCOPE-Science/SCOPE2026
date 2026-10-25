# Mixed-dimensional homotopy of the Möbius–Kantor induced-forest complex

## Finding
For the Möbius–Kantor graph \(M=\operatorname{GP}(8,3)\), the simplicial complex of vertex subsets that induce forests has the complete integral homotopy type
\[
\mathcal F(M)\simeq\bigvee^{25}S^9\vee\bigvee^4 S^{10}.
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_9(\mathcal F(M);\mathbb Z)\cong\mathbb Z^{25}\) and \(\widetilde H_{10}(\mathcal F(M);\mathbb Z)\cong\mathbb Z^4\). This is a mixed-dimensional wedge, not just a rational or mod-two homology calculation.

## Assumptions and scope
Write the graph vertices as \(u_i=i\) and \(v_i=8+i\) for \(i\in\{0,\ldots,7\}\), with subscripts modulo eight. Its undirected edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), for all eight indices. All edges are distinct, so the graph has sixteen vertices and twenty-four edges. The complex is
\[
\mathcal F(M)=\{A\subseteq V(M):M[A]\text{ has no cycle}\}.
\]
The empty set is the unique face of dimension minus one; a nonempty face \(A\) has dimension \(|A|-1\). Vertex masks use the displayed indexing and simplex orientations are the ascending order of vertex labels. The claim concerns this single graph and **vertex-induced** acyclicity, not the graphic-matroid complex of acyclic *edge* sets, the graph's ordinary independence complex, or a family of all generalized Petersen graphs.

## Proof
**Exact face enumeration.** For each of the \(2^{16}=65536\) vertex masks, a disjoint-set union algorithm inspects every induced edge, rejecting the mask exactly when an edge joins two already connected components. A second algorithm builds faces by adding their least selected vertex: an acyclic subgraph remains acyclic exactly when no two neighbors of the new vertex lie in one component of the old graph. These two mathematically equivalent but independently implemented tests agree on every mask. The face counts in dimensions minus one through ten are
\[
(1,16,120,560,1820,4368,7984,11200,11792,8672,3792,672).
\]
There are exactly 50,997 faces including the empty face, with reduced Euler characteristic \(-21\).

**Complete acyclic matching.** Begin with every face active. For each currently active set and each possible pivot vertex, form all available pairs \((\sigma,\sigma\cup\{v\})\) in which \(v\notin\sigma\), both faces are active, and their dimensions differ by one. Choose the smallest-labeled vertex with the *largest* number of available pairs, remove all these pairs from the active set, and iterate until no such pair remains. All pair removals, tie-breaking rules, and face predicates are executable in `mk_forest_verify.py`. The algorithm produces 25,483 pairs and 31 critical faces: one in dimension eight, 26 in dimension nine, and four in dimension ten. The augmented empty face is paired with a vertex, which yields one ordinary critical zero-cell in the unaugmented CW model.

Orient each codimension-one Hasse incidence from the upper to the lower face, except reverse every matched edge. Construct **all 375,056** such directed incidences. A topological sort visits all 50,997 faces and leaves no directed cycle. Hence the matching is acyclic in the sense of discrete Morse theory, giving a CW complex with one zero-cell and critical cells only in the three displayed positive dimensions.

**Exact integral Morse differential.** Give an increasing-label simplex \([w_0,\ldots,w_d]\) the boundary \(\partial=\sum_{j=0}^{d}(-1)^j[w_0,\ldots,\widehat{w_j},\ldots,w_d]\). For each matched pair with lower face \(\sigma\) and upper face \(\tau\), put \(p(\tau)=0\) and
\[
p(\sigma)=-[\tau:\sigma]^{-1}\sum_{\rho\prec\tau,\,\rho\ne\sigma}[\tau:\rho]p(\rho),
\]
where \([\tau:\rho]=\pm1\), and put \(p(\gamma)=\gamma\) for every critical face. The previous directed-acyclicity check guarantees that the recursion terminates. For a critical cell \(\gamma\), the Morse boundary is \(\sum_{\rho\prec\gamma}[\gamma:\rho]p(\rho)\), computed over the exact integers. With critical cells ordered by their vertex-mask integers, the differential from the 26 nine-cells to the unique eight-cell is the transpose of
\[
(1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0),
\]
and the differential from the four ten-cells to the 26 nine-cells is identically zero. In particular the nonzero differential has a unit coefficient and Smith invariant one, so there is no torsion.

**From chain groups to homotopy.** The dimension-eight generator and one nine-cell cancel as a CW pair because their attaching degree is one. The remaining nine-skeleton is a wedge of 25 nine-spheres; its first nontrivial homotopy group agrees with its ninth homology by Hurewicz. Since the ten-to-nine cellular boundary is zero, every remaining ten-cell has zero attaching class in \(\pi_9\) of that wedge and attaches null-homotopically. Thus the complete space is precisely the displayed wedge of 25 nine-spheres and four ten-spheres, integrally.

## Verification
Run `python3 mk_forest_verify.py`; it rebuilds both face tests, the deterministic matching, all 375,056 directed Hasse incidences, an acyclic topological order, the signed integral Morse matrices, and all asserted numerical identities. The included `mk_forest_verify_output.txt` ends with `VERIFY_OK`. A separate program, `mk_forest_mod2_check.py`, builds ordinary simplicial boundary matrices from scratch without using the matching, reporting mod-two ranks of 668 and 3,099 for the ten-to-nine and nine-to-eight boundaries, consistent with Betti ranks four and 25. It additionally checks every lower-dimensional boundary rank; its output is in `mk_forest_mod2_output.txt`. Every algorithm is finite and exhaustive at the specified sixteen-vertex order.

## Relationship to prior work
Taylan (arXiv:1501.06754v1, first submitted January 27, 2015) introduces general matching-tree methods and devoid complexes defined by forbidden induced subgraphs, but its specific classifications cover paths, cycles, forests avoiding three-vertex paths, and related constructions—not the induced-forest complex of this noncactus graph. Carnero Bravo (arXiv:2307.13271, first submitted July 25, 2023) explicitly studies the induced-forest filtration, including paths, cycles, cactus graphs and graph products. The Möbius–Kantor graph is not a cactus: it is connected, has cycle rank nine and girth six, whereas a cactus with twenty-four edges and girth six has at most four cycles. The inspected results therefore do not imply these two sphere multiplicities. Records concerning the same graph's independence, matching, Čech, and configuration-space complexes involve distinct face conditions and cannot be transferred merely from the graph name. An equivalent calculation in unindexed literature cannot be excluded.

## Limitations
This classifies exactly one sixteen-vertex graph. It does not prove a formula for generalized Petersen graphs, determine the automorphism representation on homology, or classify all forest-filtration stages. Numerical checks and an executable exact proof certificate support the complete finite statement; they do not constitute independent mathematical audit. Originality remains contingent on relevant unindexed or inaccessible literature.

## References
1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, January 27, 2015; DOI: 10.1007/s11083-015-9379-3.
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first submitted July 25, 2023 (later comparison; not the archival source).
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse foundation).
