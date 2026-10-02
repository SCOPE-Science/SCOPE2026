# Independent scientific review

Audit date: 2026-10-01 UTC

Disposition: **passed**.

Correctness: **PASS**. The positive-semidefinite construction checks exactly. The initial score makes the distinguished index q the unique first pivot, and its Schur-complement update removes the added rank-one term and leaves the prescribed block residual. At that same residual, the original-matrix correlation makes the bad index the unique second pivot, leaving Frobenius norm N; any good block pivot leaves norm 1. The displayed two-by-two spectrum gives the stated best rank-two SVD error. A fresh implementation reproduced the pivot sequence and residuals at N equal to 2, 7, 64, and 257, and the committed verifier source and saved output were inspected.

Originality: **PASS**. The motivating ACA preprint's primary abstract introduces the geometry-aware weighted-mass rule and reports empirical performance, but no source located states this deflation-history counterexample or an unbounded fixed-rank factor for that rule. Resultary searches returned the audited record itself and only different ACA/pivoted-Cholesky obstructions, such as complete-pivot Frobenius growth. Those results concern different pivot scores and do not imply the source-specific stale-correlation construction.

Value: **PASS**. This isolates a substantive algorithmic design defect in a new heuristic: the next pivot is not a function of the current residual, and an already removed component whose norm is asymptotically negligible can force an arbitrarily bad fixed-rank choice. The theorem quantifies both approximation loss and one-step-gain loss, so it is more than a toy counterexample.

The detailed source comparisons, residual risks, and reproducibility checks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Existing computational artifacts are corroborative evidence only and are not treated as a substitute for the proof.
