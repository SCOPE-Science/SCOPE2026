# The 24-cell neighborhood complex is \(S^1\vee\bigvee^{48}S^3\)

## Finding
Let \(G\) be the graph of the regular 24-cell with its ordinary one-skeleton adjacency. Its Lovász open-neighborhood complex has integral homotopy type
\[
\mathcal N(G)\simeq S^1\vee\bigvee^{48}S^3.
\]
Consequently the only nonzero reduced integral homology groups are \(\widetilde H_1(\mathcal N(G);\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_3(\mathcal N(G);\mathbb Z)\cong\mathbb Z^{48}\). The result is nonequivariant and does not assert the automorphism representation on these groups.

## Assumptions and scope
Use four-dimensional standard coordinate vectors \(e_1,e_2,e_3,e_4\). The vertex set consists of all 24 vectors \(\pm e_i\pm e_j\) with \(1\le i<j\le4\), independently chosen signs, in the deterministic indexing of `verify_24cell.py`: pairs \((i,j)\) in lexicographic order, and signs in the order \((-,-),(-,+),(+,-),(+,+)\). Join two distinct roots if and only if their Euclidean inner product is \(1\). Every vertex has norm \(\sqrt2\), so this is exactly the edge relation at Euclidean distance \(\sqrt2\) on the 24-cell. There are 96 graph edges and every vertex has eight open neighbors.

The nonempty faces of \(\mathcal N(G)\) are precisely the nonempty subsets \(\sigma\subseteq V\) for which there exists \(v\in V\) with \(\sigma\subseteq N_G(v)\), where \(N_G(v)\) is the set of vertices adjacent to \(v\), not including \(v\). The homotopy statement concerns geometric realization of this abstract complex, not graph independence, graph-metric Vietoris–Rips, or the polytope boundary complex.

## Proof
**Complete finite face description.** Enumerate each of the 24 sets \(N_G(v)\), each of cardinality eight. Take all its nonempty subsets and deduplicate them as bit masks. This produces the complete complex because any face, by definition, is contained in one such neighborhood. Its face vector by dimensions \(0\) through \(7\) is
\[
(24,264,960,1608,1344,672,192,24),
\]
for exactly 5088 nonempty faces and Euler characteristic \(-48\).

**A finite, explicit acyclic matching.** Label vertices from zero to 23 in the indexing above, and use the pivot sequence

`5,18,22,15,7,14,23,21,6,19,13,16,8,0,9,11,3,17,2,1,20,12,4,10`.

Start with every nonempty face unpaired. For each pivot \(p\), visit the full list of faces in increasing order of `(cardinality, integer bit mask)`; whenever \(p\notin\sigma\) and both \(\sigma\) and \(\sigma\cup\{p\}\) remain unpaired faces, match these two faces and remove them from further matching consideration. The complete process gives exactly 2519 face pairs. There remain exactly one unmatched zero-face, one unmatched one-face, and 48 unmatched three-faces, with no other unmatched faces.

The acyclicity check considers **every** codimension-one incidence of nonempty faces, orienting it downward except for each matched pair, which is oriented upward. It constructs the resulting 5088-vertex directed Hasse graph with 22,128 directed incidences and verifies by exhaustive topological sorting that all 5088 vertices are removed. Thus this is an acyclic matching in the precise sense of discrete Morse theory, not an unsupported greedy-collapse assumption. The integer-arithmetic verifier `verify_24cell.py` is a standalone reconstruction and complete finite certificate for these assertions, including the directed-acyclicity test.

**Identification of attaching maps.** Discrete Morse theory therefore gives a CW homotopy model with exactly one cell in dimensions zero and one and 48 cells in dimension three. Its one-skeleton is a circle. There are no two-cells. Each three-cell attaches along a map from \(S^2\) to the circle, necessarily null-homotopic because \(\pi_2(S^1)=0\). Successively replacing null-homotopic attaching maps by constant ones gives the asserted wedge of one circle and 48 three-spheres, integrally. This argument does not assume that mod-two Betti numbers determine an integral homotopy type.

## Verification
Run `python3 verify_24cell.py` with Python 3.9 or later and no third-party modules. It independently reconstructs all 24 roots and 96 graph edges, enumerates all faces, computes the exact matching, verifies the unmatched dimensions and checks that the fully oriented Hasse graph is acyclic. Recorded results are in `verification_output.txt`.

An independent program, `homology_f2.py`, builds the simplicial boundary matrices without using the Morse pairs and performs exact bit-vector elimination over \(\mathbf F_2\). Its ranks in degrees \(1\) through \(7\) are \(23,240,720,840,504,168,24\); its Betti numbers are one in dimensions zero and one and 48 in dimension three, zero otherwise. This serves as a separate consistency check only; the integral conclusion follows from the acyclic matching and the attaching-map argument. Recorded results are in `mod2_output.txt`.

## Relationship to prior work
Lovász introduced the neighborhood complex in the proof of Kneser's conjecture. Csorba–Lange–Schurr–Waßmer (arXiv:math/0310339) compare neighborhood, Lovász and box complexes by deformation retractions. Kahle (arXiv:math/0512077) studies neighborhood complexes of random graphs. Shukla (arXiv:1802.04526) classifies neighborhood complexes of graphs of maximum degree at most three and four-regular circulant graphs; the 24-cell graph is eight-regular, so those classification hypotheses do not apply. The related independence complex of the 24-cell graph and neighborhood complexes of other named graphs are different combinatorial constructions or different input graphs. The specific rank-48 mixed-dimensional homotopy statement is not supplied by the identified general results.

## Limitations
The finite verification is exhaustive for **this** 24-vertex graph, not for a family of 24-cell deformations, alternative root-graph adjacencies or its box complex with an explicit equivariant action. No integral automorphism-module calculation is claimed. A matching of finite cells and its full acyclicity together prove the stated infinite homotopy conclusion via discrete Morse theory; the mod-two computation alone would not. Publication-priority verification is not exhaustive: an uncatalogued equivalent computation or an incidental result in inaccessible full text may exist. No independent mathematical audit has been performed.

## References
- L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, J. Combin. Theory Ser. A **25** (1978), 319–324, DOI 10.1016/0097-3165(78)90022-5.
- P. Csorba, C. Lange, I. Schurr, A. Waßmer, *Box complexes, neighborhood complexes, and the chromatic number*, arXiv:math/0310339 (initial public submission 2003-10-21).
- M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077 (initial public submission 2005-12-04).
- S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (initial public submission 2018-02-13).
- Wolfram MathWorld, *24-Cell*, standard 24-cell vertex coordinates and 96-edge combinatorics, https://mathworld.wolfram.com/24-Cell.html.
