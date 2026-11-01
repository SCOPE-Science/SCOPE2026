# Integral homotopy type of the cube graph Morse complex

## Finding
Let \(Q_3\) be the graph on the eight binary triples \(\{0,1\}^3\), with an edge exactly when two triples differ in one coordinate. Its **ordinary Morse complex** \(\mathcal M(Q_3)\) parametrizes acyclic matchings between vertices and incident edges, viewed as an abstract simplicial complex. There is an integral homotopy equivalence
\[
\boxed{\mathcal M(Q_3)\simeq\bigvee^{4}S^5\vee\bigvee^{139}S^6.}
\]
In particular the only nonzero reduced integral homology groups are \(\widetilde H_5\cong\mathbb Z^4\) and \(\widetilde H_6\cong\mathbb Z^{139}\), with no torsion. This result concerns the ordinary *Morse complex*, not the ordinary matching complex of the graph.

## Assumptions and scope
Identify graph vertices with the integers \(0,\ldots,7\), represented by their three binary digits; the neighbors of \(u\) are \(u\oplus2^j\), for \(j\in\{0,1,2\}\). The twelve undirected edges produce 24 distinct incidence symbols \((u,\{u,v\})\), represented as arcs \(u\to v\). A subset of incidence symbols is a simplex precisely when (i) no graph vertex or undirected graph edge appears twice in the selected incidence pairs, and (ii) the selected arcs contain no directed cycle. Equivalently, it is an oriented forest with outdegree at most one at each vertex, each component being directed toward a root. The empty simplex is included in augmented enumeration. All equivalences and homology groups are integral unless an explicit coefficient field is shown.

## Proof
**Exhaustive face determination.** Every graph vertex has precisely four possibilities: be unmatched or be paired to one of its three incident edges. Enumerating all \(4^8\) assignments and rejecting pairs that reuse an undirected edge or create a directed cycle yields precisely 23,625 augmented simplicial faces. A separate construction enumerates every one of the \(2^{12}\) subsets of undirected edges, retains acyclic subsets, selects one root for each tree component, and orients each tree toward its selected root. Its resulting face set agrees **exactly**, as a set of 24-bit masks, with the first construction. The nonempty face vector in dimensions \(0,\ldots,6\) is
\[
(24,240,1296,4080,7488,7424,3072).
\]
In addition the full augmented simplicial boundary matrices over \(\mathbb F_2\) have ranks (from \(C_0\to C_{-1}\) to \(C_6\to C_5\))
\[
(1,23,217,1079,3001,4487,2933),
\]
independently recovering the previously known mod-two homology.

**Acyclic discrete-Morse certificate.** Put the 24 incidence symbols in ascending lexicographic \((u,v)\) order. Begin with the set of all nonempty faces. For each symbol in this order, simultaneously pair every remaining face not containing the symbol with its remaining one-symbol extension, and delete the paired faces from the remaining set. The accompanying `verify_cube_morse.py` constructs these pairs exactly and tests the entire directed Hasse graph, with every matched incidence directed upward and all other incidences directed downward. Kahn topological sorting visits all 23,624 vertices of this directed graph and all 124,176 directed Hasse incidences, proving the matching acyclic. The 11,697 matched face pairs leave precisely one critical zero-cell, 47 critical five-cells, and 182 critical six-cells; there are no other critical cells. Forman's discrete Morse theorem supplies a homotopy-equivalent CW complex with precisely this cell vector.

**Exact integral attaching degrees.** In the signed simplicial boundary, incidence signs are \((-1)^j\) for deletion of the \(j\)-th ordered symbol. For each matched pair \((a,b)\) with \(a\) five-dimensional and \(b\) six-dimensional, eliminate \(a\) from the six-dimensional boundary by the integral relation
\[
a=-[a:b]^{-1}\!\sum_{c\subset b,\,c\ne a}[c:b]c,\qquad[a:b]\in\{1,-1\}.
\]
Acyclicity makes this signed gradient-path substitution terminate, and lower-dimensional matching pairs are eliminated as in the cellular Morse reduction. Applied to all critical six-cells it produces an **exact** \(47\times182\) integer cellular boundary matrix, with 334 nonzero entries, each \(1\) or \(-1\). The checker then performs full integer row and column operations, taking only pivots \(\pm1\), and finds exactly 43 pivots; the remaining \(4\times139\) submatrix is **identically zero**. Thus the integral Smith invariant factors are 43 units and all other entries zero. In particular \(\widetilde H_5\cong\mathbb Z^4\) and \(\widetilde H_6\cong\mathbb Z^{139}\), with no torsion.

**From degree matrices to homotopy.** The Morse CW complex has only a basepoint, five-cells and six-cells. Its five-skeleton is \(\bigvee^{47}S^5\); the Hurewicz isomorphism identifies \(\pi_5\) of this skeleton with \(H_5\cong\mathbb Z^{47}\), so the **whole** attaching homotopy class of every six-cell is determined by its integral degree column. Integral elementary changes of bases among five-spheres and six-cell attachments, together with the 43 degree-one cellular cancellations certified above, leave 4 unattached five-spheres and 139 trivially attached six-cells. This proves the displayed homotopy equivalence; field homology ranks alone would not suffice.

## Verification
Run `python3 verify_cube_morse.py` using Python 3 with **only the standard library**. The script independently enumerates all simplicial faces twice, checks the face sets agree exactly, recomputes augmented mod-two simplicial boundary ranks, constructs the full matched directed Hasse graph and verifies its acyclicity, reconstructs the exact **signed integral** Morse boundary, and performs integer unimodular unit-pivot elimination to zero residual block. The actual successful execution is embedded in `verification_output.txt` and ends with `CUBE_MORSE_INTEGRAL_WEDGE_VERIFIED`.

Critical expected values are 23,625 augmented faces, 11,697 matching pairs, 23,624 directed Hasse vertices, 124,176 Hasse incidences, 47 critical five-cells, 182 critical six-cells, a \(47\times182\) integral boundary matrix, 43 unit pivots, and a zero \(4\times139\) residual block. The 43 integral pivots and zero residual are the additional tests beyond the published mod-two computation.

## Relationship to prior work
Donovan–Lin–Scoville analyze exact Morse-complex types for tree-like and several other families; their classifications do not include the cube graph. Scoville–Zaremsky prove general connectivity bounds for graph Morse complexes, including a hypercube connectivity example, not this exact integral homotopy type. Contreras–Tawfeek relate graph Laplacians to face enumeration, not to the attaching-degree matrix. Donovan–Scoville's star-cluster classifications concern paths, extended stars and related families, not \(Q_3\).

The **closest published same-object result** is the mod-two calculation for \(\mathcal M(Q_3)\) linked in References 5: it gives the identical face vector and mod-two Betti numbers but explicitly does not determine integral homology, torsion, or homotopy type. The present complete acyclic matching and integral Smith reduction settle those logically stronger questions. The directed-forest formulation gives an equivalent language; a 2020 thesis on directed forests of Cayley graphs (Reference 6) is therefore a plausible additional comparison. Its abstract and limited preview were accessible, but its full text was not, so it remains an unresolved potential overlap rather than being called noncovering.

## Limitations
The proof is exhaustive for the one graph \(Q_3\); it gives **no** general formula for higher-dimensional cubes \(Q_d\), other graph families, equivariant homology, or higher homotopy operations of related complexes. The named older same-object mod-two result is credited, not claimed new. The unrestricted full text of Courtney's Cayley-graph thesis was unavailable at review time; an implicit equivalent proof there or in unindexed sources is a residual bibliographic risk. This finding is not externally or independently certified.

## References
1. Connor Donovan, Maxwell Lin, Nicholas A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1 (2019-09-25).
2. Nicholas A. Scoville, Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1 (2020-04-22).
3. Iván Contreras, Ahmad Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388v1 (2021-05-12).
4. Connor Donovan, Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (2022-07-27).
5. *Mod-two homology of the cube-graph Morse complex is concentrated in degrees five and six*, published-finding corpus record 2026/10/4/SCOPE-mod-2-homology-of-the-cube-graph-morse-complex-is-concentrated-i--3861de13b7e0 (2026-10-04), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-cube-graph-morse-complex-is-concentrated-i--3861de13b7e0.
6. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, M.S. thesis, Boise State University, 2020, DOI:10.18122/td/1684/boisestate (abstract available; full text not inspected).
