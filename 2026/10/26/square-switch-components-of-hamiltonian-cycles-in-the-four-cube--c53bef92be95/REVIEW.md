# Scientific review

**Correctness — PASS.** Two exhaustive and independently structured generators (simple Hamiltonian walks and pairs of perfect matchings) produce the same \(1344\) undirected cycles. The local-switch equivalence is proved by even-degree symmetric differences and girth four. Two adjacency implementations agree, and full graph traversal and breadth-first search establish every reported component, degree, orbit and distance. The embedded verifier executed with `VERIFY_OK`.

**Originality — PASS, with residual risk.** Gilbert's nine symmetry types and the known \(1344\) cycle count are prior results, not claimed as new. Chebiryak–Kroening's full-text classification compares change-number classes, while Kleer–Patel–Stroh study switch-chain irreducibility under different, dense-graph hypotheses and constructions. The new result is the exact square-switch component profile and distances of the four-cube. Searches found no covering claim, but the entire Gilbert article could not be inspected and unindexed computations could exist.

**Value — PASS.** The full component decomposition measures a natural, exact obstruction to transforming cyclic Gray codes by a local two-edge switch. The simultaneous presence of \(240\) isolated states and a large component of diameter \(12\) is not implied by the previously known numbers of Hamiltonian cycles or symmetry types; it is useful for assessing local Hamiltonian-cycle sampling and reconfiguration.

**Scope and limits.** Only dimension four and two-edge switches are analyzed. No irreducibility or mixing statement for larger switch sizes, no infinite-family theorem, and no independent external audit are asserted.

**Closest literature:** Gilbert (1958); Chebiryak and Kroening (2008); Kleer, Patel and Stroh (2020); OEIS A066037.

Self-review: passed. Independent audit: not yet performed.
