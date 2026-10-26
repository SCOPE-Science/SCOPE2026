# Self-review

**Correctness — PASS.** The fort condition is equivalent to the local four-bit triple rule. A nonempty cyclic fort cannot have two adjacent empty columns. An exact 255-state potential certifies reduced costs are nonnegative; four tight recurrent components are bipartite; the constructions attain the parity lower bounds. The even enumeration follows from exact adjacency polynomials, and the odd enumeration from 255 verified residuals followed by Cayley--Hamilton. The attached `verify.py` actually reconstructs the matrices; small-size direct exhaustive checks are supplemental rather than purported infinite proofs.

**Originality — PASS with residual risk.** The new contribution is the all-order minimum-fort count in the narrow natural toroidal grid family, not the zero-forcing framework or the known \(Q_4\) value. Cameron et al. discuss the Cartesian-product framework, Becker et al. enumerate minimal forts in other families, and Brimkov et al. count the four-cube case. Their inspected results do not imply the width-four all-order parity law. Searches for equivalents involving stopping sets, minimum forts, and failed zero forcing found no decisive earlier theorem. Literature not indexed in the consulted sources may overlap.

**Value — PASS.** The exact extremal enumeration grows exponentially and separates even and odd circumferences; it quantifies genuinely different minimum fort configurations for an infinite natural graph family. These are structural enumerative data beyond the simple vertex-transitive fractional optimum. The same finite-state certificate can be checked without external computer algebra.

**Closest prior literature and limitations.** arXiv:2310.17904 (2023), arXiv:2404.05963 (2024) and arXiv:2507.10826 (2025). The four-cube specialization is known, and no priority claim is made for it. Widths other than four, independent certificate audit, and comprehensive detection of unindexed work are outside scope.

Self-review: passed. Independent audit: not yet performed.
