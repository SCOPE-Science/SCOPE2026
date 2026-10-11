# Scientific review: Chvátal independence-complex vertex-deletion dichotomy

## Correctness — PASS

The explicit 24-edge, 12-vertex Chvátal graph yields exactly 126 nonempty independent faces, with \(f\)-vector \((12,42,52,20)\). The exhaustive graph-of-incidences topological sort checks the complete discrete-Morse gradient in the five representative complexes: critical dimensions are \((0,2)\) for the full complex, \((0)\) for orbit-A deletion, \((0,2)\) for orbit-B deletion, \((0,1)\) for orbit-A link and \((0)\) for orbit-B link. Explicit free-face collapse orders prove simplicial collapsibility in both one-critical-vertex cases. The given edge-preserving permutations generate all four/eight vertices in the two classes, and different deletion cardinalities rule out mixing. The cone-on-link gluing argument proves the canonical inclusion homotopy equivalence for each of the eight orbit-B deletions. A second separately written program computes complete mod-two boundary ranks on all 25 relevant complexes. Both checkers ran successfully from the package. This is a finite exhaustive proof, not a probabilistic computation or a homology-only inference.

## Originality — PASS with documented residual risk

The methodological anchor is Barmak's original 2010 star-cluster paper (arXiv:1007.0418v1, primary MSC 57M15). Its general suspension conclusion for triangle-free graphs does not identify this sphere nor the two orbitwise deletion/link types. Kitaev–Pyatkin (arXiv:2003.06204) study semi-transitive orientability of this exact graph; their investigated theorem is not an independence-complex homotopy statement. Goyal–Shukla–Singh (arXiv:1905.06926) address different specified graph families. The graph-specific indexed record concerning a Ramanujan signing reports a different spectral assertion. Exact searches for the independence complex of the Chvátal graph, its vertex links, deletion orbit types, and complement-clique formulation returned no stronger covering result; a negative search alone is not novelty proof. Full indexing of unpublished literature cannot be guaranteed.

## Value — PASS

The twelve-vertex Chvátal graph is a canonical small four-chromatic triangle-free regular graph. Its exact independence-complex homotopy type is sharpened to a **complete classification of all twelve vertex deletions and links**, respecting its full two-orbit automorphism structure. The meaningful contrast is that every graph vertex is chromatically critical, yet only the four-vertex orbit is homotopically deletion-critical. The eight other inclusion maps are homotopy equivalences; both collapsible classes have actual simplicial-collapse certificates. This determines a natural invariant and a natural finite boundary phenomenon, not just a recomputation of Euler characteristic or a renamed general lemma.

## Limitations

The proof concerns this finite labeled graph, not a parametric graph class. The published exact-coverage search may miss an unindexed equivalent proof. No independent audit has yet occurred.

Same-model review: passed. Independent audit: not yet performed.
