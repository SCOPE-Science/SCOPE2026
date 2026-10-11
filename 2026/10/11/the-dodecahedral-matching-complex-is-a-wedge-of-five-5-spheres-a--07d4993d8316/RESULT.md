# The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres

## Finding
Let \(D\) be the dodecahedral graph \(\operatorname{GP}(10,2)\), and let \(\mathcal M(D)\) be its ordinary matching complex: its vertices are the thirty edges of \(D\), and its simplices are the sets of pairwise endpoint-disjoint edges. There is an integral homotopy equivalence
\[
\mathcal M(D)\simeq\bigvee^{5}S^{5}\vee\bigvee^{117}S^{6}.
\]
In particular, the nonzero reduced integral homology groups are precisely \(\widetilde H_5(\mathcal M(D);\mathbb Z)\cong\mathbb Z^5\) and \(\widetilde H_6(\mathcal M(D);\mathbb Z)\cong\mathbb Z^{117}\). This is a homotopy classification, not only a field-homology computation.

## Assumptions and scope
The graph has outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), for every \(i\in\mathbb Z/10\mathbb Z\). Indices on both sorts of vertices are reduced modulo ten. Graph edges are sorted as ordered pairs of numbers \(0,\ldots,19\), with \(u_i=i\), \(v_i=10+i\). A matching is identified with a thirty-bit mask relative to this sorted list. The complex is the full ordinary matching complex, not its perfect-matching subcomplex or the Morse complex of acyclic orientations.

## Proof
First enumerate the matching complex exactly. Starting with the empty mask, process the thirty edges in sorted order; when processing edge \(e\), adjoin \(e\) to precisely those previously generated matchings whose edges do not touch \(e\). Every matching appears exactly once, because its largest-index edge has a unique predecessor. The resulting counts for matchings of sizes zero through ten are
\[
(1,30,375,2540,10155,24474,34805,27300,10260,1400,36).
\]
Thus the nonempty face poset has 111375 faces, and the maximum simplex dimension is nine.

Next construct a discrete-Morse matching. On the augmented face poset, for edge indices \(i=0,\ldots,29\), match every still-unpaired face mask \(s\) not containing \(i\) with \(s\cup\{i\}\) when both faces are present and still unpaired. This deterministic sequential toggle construction initially leaves ten critical five-faces, 127 critical six-faces, and five critical seven-faces, where dimensions are simplex dimensions. Apply ten Forman cancellations: first five between dimensions seven and six, then five between dimensions six and five. Each cancellation reverses the unique alternating gradient path between a chosen pair of adjacent-dimensional critical faces. The unique-path choice is computed explicitly; for each candidate target the program counts all directed alternating paths, capped at two, before selecting a target with count exactly one. The selection order and ten exact face masks are printed by `verify_morse.py`.

After these cancellations, remove the augmented empty-face pairing and restore its singleton as the critical vertex. The resulting ordinary discrete-Morse matching consists of exactly 55626 disjoint pairs, one critical zero-simplex, five critical five-simplices, and 117 critical six-simplices. Each pair is a codimension-one incidence. A complete topological sort of the Hasse graph, with every matched incidence reversed, visits all 111375 nonempty faces across all 666330 codimension-one incidences. Hence the matching is acyclic and Forman's theorem gives a homotopy-equivalent CW complex with exactly these critical cells and no others.

The Morse five-skeleton is a wedge of five five-spheres. The signed cellular Morse boundary from the 117 six-cells to the five five-cells is computed exactly, using oriented simplicial boundaries and the usual elimination along upward-paired faces. If \(s\) is paired upward to \(t\), its reduced projection is \(-\varepsilon(s,t)\) times the sum of the projections of the other facets of \(t\), weighted by their incidence signs; a face paired downward projects to zero and a critical face to its corresponding generator. The resulting integer matrix is exactly the zero matrix of size \(5\times117\). Because \(\pi_5(\bigvee^5 S^5)\cong H_5(\bigvee^5 S^5;\mathbb Z)\cong\mathbb Z^5\) by Hurewicz, each six-cell's attaching map is null-homotopic. Therefore the CW complex, and hence \(\mathcal M(D)\), is a wedge of five five-spheres and 117 six-spheres.

## Verification
Run `python3 verify_morse.py` with a standard Python 3 interpreter. It reconstructs the graph and every simplex, checks the original matching counts, performs all ten unique-gradient-path cancellations, verifies every face incidence and global acyclicity, computes the signed Morse boundary, and prints `MORSE_OK`. It confirms 55626 matched pairs, the critical-cell vector \((1\text{ in dimension }0,5\text{ in dimension }5,117\text{ in dimension }6)\), and a zero \(5\times117\) matrix.

Separately, run `python3 verify_independent.py`. This verifier computes the matching-count polynomial by an independent vertex-deletion recurrence on the original twenty-vertex graph, constructs its line graph separately, and computes all augmented mod-two simplicial boundary ranks by bitset elimination. It prints `HOMOLOGY_F2_OK`, with reduced Betti ranks five in degree five, 117 in degree six, and zero otherwise. The independent mod-two check supports the face enumeration and homology counts; the integral homotopy assertion comes from the complete acyclic Morse matching and the signed zero boundary, not from mod-two ranks alone.

## Relationship to prior work
Engström's 2005 paper analyzes independence complexes of claw-free graphs, including the fundamental identification of matching complexes with independence complexes of line graphs. Its theorems provide general reductions and connectivity bounds, not this exact integral dodecahedral homotopy classification. A public indexed calculation for exactly the same dodecahedral matching complex reports the mod-two Betti ranks five and 117; the present result upgrades those ranks to an explicit integral homotopy decomposition, settling all higher attaching degrees needed in this two-level CW model. The published dodecahedral *vertex-independence* complex has a different vertex set and is not the present edge-matching complex.

Bayer, Jelić Milutinović and Vega classify matching complexes of outerplanar graphs; the dodecahedral graph is not outerplanar, so their theorem has no implication here. Gupta, Sarkar, Sawant and Shukla treat categorical products of path graphs, not \(\operatorname{GP}(10,2)\). These distinctions concern hypotheses and theorem statements, not just title similarity.

## Limitations
This finite result applies only to the ordinary matching complex of the specified graph. It does not classify matching complexes of all generalized Petersen graphs, nor does it determine any equivariant homotopy structure. A prior calculation of mod-two homology for this exact graph was located through a published index; its full repository text could not be inspected through the available public retrieval route. The exact extent of that inaccessible text, and possible equivalent unindexed calculations, remain bibliographic uncertainties. No independent scientific audit has been performed.

## References
- A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (first public version 2005-12-17), https://arxiv.org/html/math/0512420v1.
- M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, https://arxiv.org/html/2411.04601v2.
- R. K. Gupta, S. Sarkar, S. S. Sawant, S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298, https://arxiv.org/html/2403.15298v2.
- Public indexed result, *Mod-2 homology of the dodecahedral matching complex*, identifier `2026/10/4/SCOPE-mod-2-homology-of-the-dodecahedral-matching-complex--0f7a788bfafc`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-dodecahedral-matching-complex--0f7a788bfafc.
- Dodecahedral Graph, Wolfram MathWorld, https://mathworld.wolfram.com/DodecahedralGraph.html.
