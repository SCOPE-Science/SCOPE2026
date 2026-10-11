# Scientific review of the Herschel graph independence-complex classification

## Correctness — PASS

For the exact eighteen-edge graph in RESULT.md, 123 nonempty independent faces were reconstructed exhaustively. A complete discrete-Morse acyclic matching on these faces has 60 pairs and three unmatched faces, one zero-cell and two two-cells. Across the full complex and each of its eleven deletions and links, the verifier proves pair validity and performs complete acyclic topological sorts on all 3,644 nonempty Hasse incidences. The twenty-two local Morse reductions leave precisely the critical-cell patterns required by the stated homotopy types. For each of the two collapsible deletions the code constructs all 48 elementary simplicial collapse pairs, verifying every unique free coface. The reduced CW complexes have cells only in dimensions zero and one, or zero and two, so attaching maps are constant. This proves the integral homotopy types. A distinct independent-subset recursion and full mod-two boundary-rank computation corroborates all 23 reduced Betti profiles; it is a check, not a substitute for the Morse proof.

## Originality — PASS with a residual bibliographic risk

The complete graph-specific statement was compared to the triangle-free suspension and star-cluster results of Barmak (arXiv:1007.0418v1, Sections 3 and 4) and to Engström's deletion/gluing results (arXiv:math/0508148v1, independence-complex sections). Their statements supply general tools and suspensions, not this exact sphere multiplicity or the complete eleven-vertex deletion/link profile. The independence-complex, complement-clique and edge-ideal Stanley–Reisner formulations describe the same object; the graph matching complex is distinct. Herschel-graph reference entries give combinatorial and spectral graph data, not a homotopy classification. Targeted exact-object literature searches did not find a covering theorem, though such an account could exist in unindexed work. The claims are not presented as first-ever definitive worldwide discoveries.

## Value — PASS

The Herschel graph is a canonical eleven-vertex, eighteen-edge non-Hamiltonian polyhedral graph. The total integral homotopy type and all its single-vertex deletions and links form a complete, natural finite topological invariant for this small canonical graph. The profile distinguishes the two exceptional degree-three vertices, whose deletions collapse the complex, from the other degree-three vertices, whose deletions retain a sphere. This is stronger than an Euler-characteristic or field-Betti table and is not a mechanical substitution into a graph-family formula. The result offers a reproducible local-topology benchmark; no unsupported general Hamiltonicity theorem is claimed.

## Closest literature and limits

Barmak's Theorems 3.4–3.5 imply a suspension for the triangle-free Herschel graph. They do not compute the specific homotopy type. Engström supplies general local graph-complex reductions without this complete classification. MathWorld's graph entry and the published `H11_edges` example support the graph identification. Possible unindexed identical computations are residual risks. Integral proof is confined to the explicit finite graph, with no automatic extension to larger polyhedra.

Same-model review: passed. Independent audit: not yet performed.
