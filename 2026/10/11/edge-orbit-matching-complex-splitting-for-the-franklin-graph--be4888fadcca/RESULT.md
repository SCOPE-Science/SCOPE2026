# Edge-orbit matching-complex splitting for the Franklin graph

## Finding
Let \(F\) be the twelve-vertex Franklin graph with the explicit LCF labeling defined below. Write \(\mathcal M(G)\) for the ordinary matching complex of a finite simple graph \(G\), whose vertices are graph edges and whose simplices are nonempty sets of pairwise vertex-disjoint graph edges, together with the empty face.

The eighteen edges of \(F\) form exactly two automorphism orbits, \(A\) of size six and \(B\) of size twelve. For each edge \(e=\{u,v\}\) in the indicated orbit, the following integral homotopy equivalences hold:

| Orbit | \(\mathcal M(F-e)\) | \(\mathcal M(F-\{u,v\})\) |
| --- | --- | --- |
| \(e\in A\) | \(\bigvee^{8}S^3\) | \(\bigvee^{4}S^2\) |
| \(e\in B\) | \(\bigvee^{10}S^3\) | \(\bigvee^{2}S^2\) |

Here \(F-e\) deletes one graph edge, while \(F-\{u,v\}\) deletes two graph vertices and all incident edges. In both orbits, the standard deletion-link cofibration splits as an unbased homotopy equivalence
\[
\mathcal M(F)\simeq\mathcal M(F-e)\vee\Sigma\mathcal M(F-\{u,v\}),
\]
and hence \(\mathcal M(F)\simeq\bigvee^{12}S^3\). This is a simultaneous classification of the ordinary matching complex and its entire single-edge deletion/link profile, not a statement about the perfect-matching complex.

## Assumptions and scope
Label graph vertices by \(0,1,\ldots,11\), with residues modulo twelve. Include the twelve cycle edges \(\{i,i+1\}\). For even \(i\), also include \(\{i,i+5\}\); for odd \(i\), include \(\{i,i-5\}\). Identify repeated unoriented edges, leaving eighteen edges and degree three at every vertex. This is the Franklin graph in LCF notation `[5,-5]^6`, also called the six-crossed prism. The orbit \(A\) consists precisely of \(\{0,1\},\{2,3\},\{4,5\},\{6,7\},\{8,9\},\{10,11\}\); the other twelve edges constitute \(B\).

All equivalences concern ordinary, non-equivariant homotopy types of finite simplicial complexes with integral attaching degrees. No parameter-family extension beyond this graph is claimed.

## Proof
**Automorphism reduction.** The accompanying verifier enumerates all adjacency-preserving permutations by an injective backtracking search. It finds exactly 48 graph automorphisms and explicitly forms the orbits of \(\{0,1\}\) and \(\{0,5\}\): they are disjoint, have sizes six and twelve, and exhaust all eighteen graph edges. Thus it suffices to verify those two representatives and the full graph.

**Finite discrete Morse reductions.** Represent every graph matching by the bitmask of its ordered graph edges. Recursively enumerate every admissible matching, including the empty face. Iteratively pair an unpaired face lacking edge label \(i\) with its still-unpaired coface obtained by adjoining \(i\), processing labels in ascending order; remove the pair containing the empty face and retain its singleton vertex as critical. For each resulting matching, orient matched face incidences upward and all other nonempty codimension-one face incidences downward. A complete topological sort verifies that this directed Hasse diagram has no cycles. This constructs valid finite acyclic discrete-Morse matchings, not merely candidate matchings.

| Complex | Nonempty simplices | Matched pairs | Oriented incidences | Critical cells by dimension |
| --- | ---: | ---: | ---: | --- |
| \(\mathcal M(F)\) | 1091 | 539 | 3942 | one 0-cell and twelve 3-cells |
| \(\mathcal M(F-\{0,1\}_{\mathrm{edge}})\) | 875 | 433 | 3105 | one 0-cell and eight 3-cells |
| \(\mathcal M(F-\{0,1\}_{\mathrm{vertices}})\) | 215 | 105 | 609 | one 0-cell and four 2-cells |
| \(\mathcal M(F-\{0,5\}_{\mathrm{edge}})\) | 869 | 428 | 3075 | one 0-cell, one 2-cell and eleven 3-cells |
| \(\mathcal M(F-\{0,5\}_{\mathrm{vertices}})\) | 221 | 109 | 633 | one 0-cell and two 2-cells |

The table's subscript \(\mathrm{edge}\) means deleting the displayed edge only; the subscript \(\mathrm{vertices}\) means deleting both endpoints. Each 0-and-top-dimensional-critical-cell Morse CW complex is a wedge of the stated spheres because all positive-dimensional cells attach to the sole 0-cell. The one exceptional row requires an integral attaching-degree check.

**Integral exceptional boundary.** For the class-\(B\) edge deletion, enumerate the eleven critical 3-simplices and the sole critical 2-simplex. Compute their signed Morse attaching degrees by eliminating each upward-matched facet using the simplicial alternating boundary, with the matched incidence of sign \(\pm1\). The complete critical \(\partial_3\) matrix is one row,
\[
(-1,-1,-1,-1,1,-1,0,-1,0,-1,1).
\]
In particular it has a unit entry and its Smith invariant is one. The 2-skeleton is \(S^2\), so these degrees determine the 3-cell attaching maps in \(\pi_2(S^2)\cong\mathbb Z\). An integral change of basis among the eleven 3-cells reduces the attachments to one degree-one 3-cell and ten null-attaching 3-cells. The degree-one pair cancels topologically, giving \(\mathcal M(F-\{0,5\}_{\mathrm{edge}})\simeq\bigvee^{10}S^3\). (The identity and basis change are homotopy equivalences at the cellular level, not just field-rank calculations.)

**Deletion-link splitting.** A simplex of \(\mathcal M(F)\) either excludes edge \(e\) or is obtained by coning \(e\) over a matching in \(F-\{u,v\}\). Thus \(\mathcal M(F)\) is the mapping cone of the inclusion \(\mathcal M(F-\{u,v\})\hookrightarrow\mathcal M(F-e)\), up to canonical homotopy. In both edge orbits this inclusion goes from a wedge of 2-spheres into a wedge of 3-spheres. Since \(\pi_2(\bigvee S^3)=0\), the inclusion is null-homotopic, so its mapping cone splits as a wedge of target and suspension of source. Each orbit gives twelve 3-spheres, proving the theorem for every edge.

## Verification
Run `python3 verify_franklin.py` and `python3 verify_franklin_chain.py` with standard Python 3, in the directory containing these two included files. The first exhaustively constructs the graph and five Morse matchings, checks every directed face incidence and graph automorphism, and computes the exceptional integral degree row. Its terminal success marker is `INTEGRAL_MORSE_VERIFIED`. The independently implemented second program enumerates simplicial chains directly, computes reduced homology ranks over characteristics two and three, checks the full complex's face vector \((18,117,336,417,186,17)\), and exhaustively checks the mod-two deletion/link profiles for all eighteen edges. Its success marker is `SECOND_CHAIN_VERIFIED`.

The integral attaching-degree certificate, rather than the field ranks, establishes the claimed homotopy types. The computer-assisted finite proof is fully specified by the source files and their exhaustive assertions; no numerical approximation or computation timeout is interpreted as mathematical evidence.

## Relationship to prior work
Engström's 2005 work on independence complexes of claw-free graphs provides the topological graph-complex framework and general reductions; it does not identify this Franklin-graph two-orbit homotopy profile. Matching complexes are independence complexes of line graphs, explaining the relevance. Bayer, Jelić Milutinović and Vega prove sphere-wedge statements for particular polygonal chains and outerplanar graphs. The Franklin graph is nonplanar and cubic, so those coverage hypotheses do not encompass this case. The classification here also concerns **ordinary** matchings, not only perfect matchings. General work on Möbius and circular ladder graphs does not immediately apply to this distinct crossed-prism graph; no assertion of exhaustive literature priority is made. The 2004 Knödel survey provides graph-family identification, but not the claimed homotopy-type calculation.

## Limitations
The result concerns one named finite graph; it asserts neither an infinite-family formula nor an equivariant decomposition. Verification uses exhaustive standard-library programs and a discrete-Morse argument, not a formal proof-assistant certificate. Unindexed or inaccessible literature could contain an equivalent earlier classification. In the exceptional edge-deletion case, integral attaching-degree verification is essential; finite-field ranks alone do not establish the asserted wedge decomposition.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first public submission 2005-12-17), primary classification 57M15; original preprint and full proof inspected.
2. R. Bayer, Z. Jelić Milutinović and L. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559 (2022); original text inspected.
3. R. Bayer, Z. Jelić Milutinović and L. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (2024); original text inspected.
4. G. Fertin and A. Raspaud, *A survey on Knödel graphs*, Discrete Applied Mathematics 137 (2004), 173–195, DOI:10.1016/S0166-218X(03)00260-9; graph definitions and abstract consulted.
5. *Franklin Graph*, Wolfram MathWorld, graph aliases and LCF presentation.
