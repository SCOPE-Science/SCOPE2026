# Independence complex of the Möbius–Kantor graph is \(\bigvee^{4}S^{3}\vee S^{4}\)
## Finding
Let \(M=G(8,3)\) be the Möbius–Kantor graph. Its independence complex satisfies \[\operatorname{Ind}(M)\simeq \bigvee^{4}S^{3}\vee S^{4}.\]

## Assumptions and scope
The Möbius–Kantor graph is presented as the generalized Petersen graph \(G(8,3)\) with vertices \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), cycle edges \(u_i u_{i+1}\), spokes \(u_i v_i\), and inner edges \(v_i v_{i+3}\). The independence complex \(\operatorname{Ind}(M)\) contains one simplex for each independent vertex set of \(M\). The claim concerns this finite simplicial complex only; no family-level extension is asserted.

## Proof
Exact enumeration gives nonempty face vector
\[
(16,96,272,376,240,72,16,2)
\]
in dimensions \(0\) through \(7\). Apply the deterministic vertex-addition matching in the vertex order
\[
(v_5,u_5,u_1,u_7,v_7,u_0,v_4,v_6,u_4,u_2,v_2,v_3,u_3,v_0,v_1,u_6).
\]
At each stage, among faces not already matched, pair an independent face \(\sigma\) not containing the current vertex \(x\) with \(\sigma\cup\{x\}\) whenever the latter is also currently unmatched. Direct inspection of the complete oriented Hasse diagram verifies that the resulting matching is acyclic. It leaves exactly one critical \(0\)-simplex, four critical \(3\)-simplices, and one critical \(4\)-simplex, with no other critical cells. Hence discrete Morse theory gives a CW complex with one \(0\)-cell, four \(3\)-cells, and one \(4\)-cell.

It remains to identify the attaching map of the critical \(4\)-cell. The four critical \(3\)-faces are
\[
\{u_0,u_4,v_2,v_3\},\quad
\{u_2,u_6,v_0,v_4\},\quad
\{u_3,u_5,v_1,v_7\},\quad
\{u_2,u_5,v_3,v_7\},
\]
and the critical \(4\)-face is
\[
\{u_3,u_6,v_0,v_1,v_2\}.
\]
In the alternating Hasse orientation determined by the matching, the numbers of directed gradient paths from the critical \(4\)-cell to these four critical \(3\)-cells are respectively \(2,0,2,2\). Therefore every integral Morse-boundary coefficient has absolute value at most \(2\).

Independently, exact simplicial boundary elimination over both \(\mathbb F_2\) and \(\mathbb F_3\) gives reduced Betti numbers
\[
\widetilde\beta_3=4,\qquad \widetilde\beta_4=1,
\]
with all other reduced Betti numbers zero. Since the Morse chain group in degree \(4\) has rank one, the Morse differential from degree \(4\) to degree \(3\) vanishes modulo both \(2\) and \(3\). Thus each integral coefficient is divisible by \(6\); the path-count bound forces every coefficient to be zero.

The \(3\)-skeleton is therefore \(\bigvee^4 S^3\). This space is \(2\)-connected, so the Hurewicz map \(\pi_3\to H_3\) is an isomorphism. The attaching map of the \(4\)-cell has zero degree in every \(S^3\)-summand, hence is null-homotopic. Attaching the \(4\)-cell therefore wedges on one copy of \(S^4\), proving the claim.

## Verification
Running `python3 verify.py` reconstructs the graph and all independent faces, verifies the full acyclic matching, checks the critical-cell counts, counts the relevant gradient paths, computes exact boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\), and checks the girth comparison used below. A successful run ends with `MK_INDEPENDENCE_VERIFY_OK`.

## Relationship to prior work
Nilakantan and Shukla study independence complexes of a cyclic-neighborhood family of regular bipartite graphs \(G_m^d\) (arXiv:1709.04789v1). If their family contained a \(16\)-vertex cubic graph isomorphic to the Möbius–Kantor graph, vertex count and degree would force the candidate \(G_8^3\). But \(G_8^3\) contains the \(4\)-cycle \(a_0-b_1-a_7-b_0-a_0\), whereas the Möbius–Kantor graph has girth \(6\); hence that theorem does not cover this graph.

Goyal, Shukla, and Singh study several other graph families and graph operations whose independence complexes admit explicit homotopy descriptions (arXiv:1905.06926v1). Searches of that paper and of the checked semantic literature under the names “Möbius–Kantor,” “generalized Petersen \(G(8,3)\),” “Knödel \(W(3,16)\),” and the Levi-graph formulation did not identify this exact homotopy type. This is evidence against direct coverage, not a proof that no unindexed source exists.

## Limitations
The result is for one classical graph and does not supply a general formula for generalized Petersen graphs, symmetric cubic graphs, or all regular bipartite graphs. The originality assessment is limited to the explicitly inspected sources and semantic searches listed in the review record. The proof relies on a finite exhaustive verification of the matching and modular boundary ranks, together with standard discrete Morse theory and the Hurewicz theorem.

## References
1. N. Nilakantan and S. Shukla, “Homotopy type of the independence complexes of a family of regular bipartite graphs,” arXiv:1709.04789v1, 2017.
2. S. Goyal, S. Shukla, and A. Singh, “Homotopy Type of Independence Complexes of Certain Families of Graphs,” arXiv:1905.06926v1, 2019; later Contributions to Discrete Mathematics 16(3), 2021.
3. R. Forman, “Morse theory for cell complexes,” Advances in Mathematics 134 (1998), 90–145.
