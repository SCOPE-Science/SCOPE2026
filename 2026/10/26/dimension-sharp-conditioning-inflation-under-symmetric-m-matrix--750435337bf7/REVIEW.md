# Self-review

**Correctness: PASS.** The scale is the unique minimizer of a strongly convex coercive barrier energy, the general bounds follow from the signed off-diagonal inequalities and the graph-Laplacian spectrum of the balanced matrix, and the weighted-star construction has explicitly solved hub/leaf equations and the complete three-level eigenspectrum. The asymptotic limits use a nonvanishing denominator \(1-c^2\). High-precision numerical replay is corroboration only, not the infinite proof.

**Originality: PASS, subject to independent examination.** The closest source [1] provides algorithms, numerical precision bounds and controls involving scaling spread but not the inspected quantitative claim that spectral conditioning of its exact balanced matrix must grow linearly with dimension for bounded-condition inputs. Source [2] solves the same scaling objective by another algorithm but states iteration-complexity results. Prior general balancing warnings are not equivalent to the particular signed congruence and dimensional matching theorem. No exact statement was located in the checked mathematical literature or research records. This cannot exclude equivalents in older matrix-equilibration literature.

**Mathematical value: PASS.** The star family is a natural, minimal hub-leaf structure with uniformly bounded input conditioning. It demonstrates an unavoidable gap between optimizing signed row sums and preserving spectral conditioning, pinpoints \(\Theta(d)\) as the worst possible dimension order, and quantifies the corresponding \(\Theta(\sqrt d)\) diagonal dynamic range. This is a structural limitation relevant when choosing scaling as a linear-solver preprocessing step; it is not presented as an algorithmic runtime guarantee.

**Closest literature:** [1] Liu–Sidford–Tu arXiv:2610.22302; [2] Vladu arXiv:2504.20619; [3] James–Langou–Lowery arXiv:1401.5766. The last addresses a different similarity-balancing objective. The findings do not supersede or contradict the source algorithms. The key residual originality risk is an unindexed traditional example of poor conditioning after symmetric signed diagonal scaling.

**Scope:** Exact signed row-sum congruence scaling, SPD symmetric \(M\)-matrices, and Euclidean condition numbers only; no universal sharp prefactor asserted.

Self-review: passed. Independent audit: not yet performed.
