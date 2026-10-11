# Scientific review: Petersen matching complex

## Correctness — PASS
The graph definition and simplex enumeration are explicit. `verify_petersen.py` enumerates all 331 nonempty matchings, verifies 160 face-coface pairs and all 975 directed face incidences, topologically sorts the resulting directed graph, and computes the exact integral five-by-five Morse boundary as zero. The one-vertex, five-two-cell, five-three-cell Morse CW model then splits because the attaching maps from two-spheres are completely detected by their integral degree vectors. `verify_petersen_independent.py` constructs the isomorphic Kneser graph independently and checks the full face vector and five distinct prime-field homology computations.

## Originality — PASS, subject to residual search risk
A literature comparison checked actual statements rather than shared graph names. Barmak's claw-free connectivity theorem does not determine the homotopy type; the outerplanar matching-complex theorem does not cover the nonplanar Petersen graph; manifold matching-complex classifications answer a different question. Mondal–Mukherjee–Saha's identification \(\mathcal M(K_5)=P\) is not a result about \(\mathcal M(P)\). Searches for the ordinary matching complex, its line-graph independence-complex representation, its exact Betti multiplicities, and published related constructions found no implication proving this decomposition. An unindexed or unpublished equivalent calculation remains possible.

## Value — PASS
The Petersen graph is a central small, edge-transitive cubic graph and a canonical nonplanar example. Its ordinary matching complex is not covered by outerplanar wedge classifications. The explicit mixed-dimensional **integral homotopy classification**, unlike a face count, Euler characteristic, or finite-field Betti profile, verifies the vanishing of the attaching maps and supplies a reproducible benchmark for matching-complex topology beyond outerplanar graphs. No claim of a family theorem is made.

## Limits and closest literature
The four principal compared sources are Barmak (arXiv:1007.0418v1), Bayer–Jelić Milutinović–Vega (arXiv:2411.04601v2), Bayer–Goeckner–Jelić Milutinović (arXiv:1906.03328v3) and Mondal–Mukherjee–Saha (arXiv:2305.02973v5). The computer-assisted proof has not received external independent audit, and literature indexing may be incomplete.

Same-model review: passed. Independent audit: not yet performed.
