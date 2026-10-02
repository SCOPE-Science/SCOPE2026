# Independent audit — 2026-10-01

## Final claim

The claim in `RESULT.md` is accepted without changing `RESULT.md` or `SLOGAN.txt`.

## Correctness — PASS

The motivating paper's complete ten-page primary text was read and its Lemmas 2.1--2.6 and proof of Theorem 1.2 were checked against the record's starting reduction. The complement of the free residue blocks is exactly the initial interval through \(Q\); the normalized boundary vector has covariance \(k^{-2}(I+(k+2)J)\), while each independent residue block has asymptotic size \((k-1)T/k^2\). The parity-aware Rademacher local limit theorem plus exponential tails yields the Gaussian integral; its determinant and one-vector eigenvalue give exactly the stated constant and diffusive factor. The exact-count code's small direct checks and displayed convergence constants were also independently checked algebraically.

Sources checked: https://arxiv.org/abs/2609.20385; artifacts/verify_exact_counts.py; artifacts/verify_output.txt.

Residual risks: The asymptotic proof is for fixed \(k\) and finite diffusive limit \(c_T/\sqrt T\); no growing-\(k\) uniformity is claimed.

## Originality — PASS

The complete Li--Xu--Yan v1 text proves only two-sided order-of-magnitude bounds for fixed offset and uses coarse central-binomial estimates. It does not state a leading constant, an asymptotic ratio, or a diffusive offset profile. The record's multivariate local-limit evaluation therefore is not mechanically implied by the published theorem alone, although it deliberately starts from the source's finite sign reduction. Exact published-archive searches returned no covering record.

Equivalent formulations, broader coverage, database/table coverage, and claim-versus-prior implication were checked separately. Primary-source inspections are recorded in the companion JSON audit.

Residual risks: The motivating preprint is very recent, so concurrent refinements may be incompletely indexed.

## Scientific value — PASS

The theorem upgrades a newly proved order-of-magnitude count to an exact first-order asymptotic, determines a closed-form constant, sharpens comparison between weights to an asymptotic ratio, and reveals the natural Gaussian profile for diffusive offsets. These are useful exact invariants of the counting problem rather than a finite recomputation.

Residual risks: The motivating preprint is very recent, so concurrent refinements may be incompletely indexed.

## Disposition

Passed. Publication status may be updated to independently reviewed; no scientific claim text changes are required.
