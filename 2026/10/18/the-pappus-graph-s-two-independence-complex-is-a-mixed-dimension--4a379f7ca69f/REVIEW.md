# Independent mathematical audit

## correctness

PASS

The LCF [5,7,-7,7,-7,-5]^3 specifies an 18-vertex cubic simple graph with 27 edges. For any vertex set S, induced components have at most two vertices iff each induced vertex has degree <=1, equivalently no triple supporting a length-two path is contained. Independently exhaustively enumerating all 2^18 masks gives 54 forbidden 3-vertex path triples, 20652 augmented faces, f-vector (18,153,762,2394,4806,6027,4428,1728,308,27), and reduced Euler characteristic -8. The exact 18-vertex toggle order in RESULT.md yields 10321 disjoint matched pairs (including the empty face pair), and precisely nine critical 5-faces [0x6621,0xcc03,0x12264,0x18846,0x20b18,0x22360,0x2c409,0x2c902,0x3404c] and one critical 6-face 0x3212a. Independently oriented all 120240 Hasse covers and topologically sorted all 20652 nodes, proving the acyclic matching. The signed integral Morse projection of the seven 5-dimensional facets of the 6-dimensional critical cell has only two nonzero contributions, deletion vertex 5 giving -e5 and deletion vertex 13 giving +e5 (one-indexed), so the full Z^9 differential is zero. Discrete Morse gives one basepoint, nine 5-cells and one 6-cell; its 5-skeleton is wedge^9 S5 and is 4-connected. Hurewicz gives pi5 ≅ H5, hence zero signed attaching degrees imply a nullhomotopic 6-cell attaching map and the asserted wedge^9 S5 ∨ S6. An independent full augmented F2 chain reduction verifies ranks (1,17,136,626,1768,3038,2980,1447,281,27) and beta5=9,beta6=1, which is only an auxiliary check. All seven actual frozen Git blob SHA1s exactly reconstruct the assigned Git subtree SHA; administrative originals were separately checked against their blob SHA1s before redaction.

## originality

PASS

Best-of-knowledge PASS for the exact integral homotopy type of the vertex-subset 2-independence complex of the 18-vertex Pappus graph. Primary papers by Deshpande–Singh (2021), Deshpande–Shukla–Singh (2020), Abdelmalek et al. (2023), and Deshpande–Roy–Sawant (2026) define and analyze higher independence, chordal families, algebraic duals, and general connectivity, but their inspected theorem hypotheses and enumerated graph families do not yield this Pappus-specific nine S5 plus one S6 homotopy result. Related published Pappus ordinary independence, matching, and graph Čech results compute different complexes; Petersen Ind2 uses a different graph. Exact-object/alias searches found no published identical classification; these searches are evidence, not a novelty guarantee. An unindexed full computation or an unexpected general theorem remains possible.

## value

PASS

Pappus is a canonical 18-vertex cubic symmetric distance-regular Levi graph, so the component-bound-two higher-independence complex is a natural invariant, not an arbitrary constructed slice. Its complete integral homotopy type exhibits both degree-five and degree-six sphere summands, unlike the equidimensional/contractible families in early classifications and unlike the ordinary Pappus independence and matching complexes. The exact integral attaching vector is mathematically essential: the same mod-two Betti numbers would not generally determine homotopy type. This creates a useful reproducible mixed-dimensional benchmark for higher independence of nonchordal cubic graphs, even though it is one finite graph rather than a general-family theorem. The result is not asserted to classify automorphism actions, other component bounds or all cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
