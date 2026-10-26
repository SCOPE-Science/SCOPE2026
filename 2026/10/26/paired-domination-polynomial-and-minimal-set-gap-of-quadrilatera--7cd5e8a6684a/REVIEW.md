# Review: Paired-domination polynomial and minimal-set gap of quadrilateral books

**Correctness: PASS.** The proof splits by zero, one, or two selected hub vertices, a complete partition. In the two-hub case, selected singleton pages force partners and parity enforces either zero singletons or an opposite-oriented pair. With one hub, every same-side page vertex is selected and the perfect matching forces exactly one omitted opposite page vertex. With no hub, all pages are complete. The inclusion-minimal classification is proved by ruling out **all strict paired-dominating subsets**, not merely one-vertex deletions. Independent exhaustive subset enumeration for \(r=2,\ldots,8\) agrees with the formula, individual families, and every minimal set.

**Originality: PASS, with specified residual priority risks.** Alizadeh–Gözüpek (arXiv:2104.02446 / DMTCS 2021) derives general upper bounds and describes an equality case with ordinary upper domination, not the book-family polynomial or minimal-set spectrum. Jiang et al. (AIMS Mathematics, 2022) discuss APX-completeness; Andreev et al. (IWOCA 2024) discuss generic algorithms and a parameterized counting problem. Searches under alternative graph names and statement-level comparison did not identify a covering formula. Unindexed work and technical sections not fully read in two less-directly-relevant sources remain risks; independent priority certification is not claimed.

**Value: PASS.** The complete generating polynomial counts every paired-dominating subset. Its sharper minimal-family theorem demonstrates an unbounded absence of intermediate even sizes in planar bipartite two-vertex-connected graphs, while all even sizes occur for the unrestricted feasible family. This addresses a structural question about inclusion-minimal solutions, not a routine numerical substitution.

**Limits.** The result is specific to quadrilateral books, no general theorem for other Cartesian products or page lengths is asserted. Finite checks corroborate but cannot replace the proof. Bibliographic coverage is nonexhaustive.

Self-review: passed. Independent audit: not yet performed.
