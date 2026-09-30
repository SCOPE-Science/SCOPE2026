# Independent audit — Exact asymptotics for eventual weighted-representation balance

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/exact-asymptotic-weighted-representation-partitions--fb5b8dfd89f0`
**Audited tree:** `404bd91c8d285a8af2be691a7a129e0c8c3ffcd8`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The asymptotic constant and diffusive profile are correct. Starting from the exact Li--Xu--Yan boundary-sign reduction, the free block sizes satisfy M_s/T -> (k-1)/k^2 and the boundary vector has covariance B=k^{-2}(I+(k+2)J). The parity-aware Rademacher local limit and multivariate CLT reduce the limit to a Gaussian integral; its determinant and all-ones quadratic form simplify to exactly the submitted factor 2^k(2k/pi)^{k/2}/sqrt(k+3) times exp(-2k^2 gamma^2/(k+3)). Independent exact finite counts reproduce the record's convergence checks.

### Independent checks

- Re-derived C={0,...,Q}, M_s=(k-1)T/k^2+O_k(1), and the limiting covariance B=k^{-2}(I+(k+2)J).
- Recomputed det(I+B/m0)=(k/(k-1))^k(k+3) and the all-ones eigenvalue (k+3)/k of m0 I+B, yielding the stated constant and Gaussian exponent.
- Checked that the source parity identity makes every local-limit argument land on the admissible Rademacher lattice, so no residue-class oscillation survives.
- Independently implemented the exact finite dynamic count; for k=2,3,4 the scaled counts at T=50,100,200 move toward the stated C_k, matching the submitted verification data.
- Inspected the motivating arXiv theorem and finite-sign lemmas; they give comparability/unique tail continuation but not the submitted exact asymptotic.

## Originality

PASS to the best of current searchable knowledge. Li--Xu--Yan arXiv:2609.20385 proves only N_{k,c}(T) asymp_{k,c} 2^T/T^{k/2} for fixed c; its theorem/corollaries do not state an asymptotic equality, explicit leading constant, or c_T/sqrt(T) Gaussian profile. Searches of the cited weighted-representation chain and current indexed literature found no prior matching constant or diffusive extension.

### Literature checked

- https://arxiv.org/abs/2609.20385 — Li–Xu–Yan, A problem of Yang and Chen on weighted representation functions; the source proves order of magnitude for fixed offset, not an explicit leading constant.
- https://doi.org/10.4064/cm6512-12-2015 — Qu (2016), earlier weighted-representation work; no matching large-threshold exact asymptotic located.
- https://doi.org/10.1007/s11139-025-01113-7 — Yan–Shan (2025), structural/exact small-threshold results in the same literature chain rather than this large-T leading constant.

## Scientific value

The record upgrades a very recent order-of-magnitude theorem to a closed exact first-order asymptotic, explains fixed-offset universality, gives an asymptotic comparison across weights, and identifies the natural square-root-scale profile of moving offsets. That is a meaningful quantitative advance over comparability bounds.

## Limitations

- k is fixed; no uniform result for k growing with T is established.
- The moving-offset theorem is limited to c_T/sqrt(T) converging to a finite real number.
- The source and submitted theorem are extremely recent, so contemporaneous unindexed work remains a residual originality risk.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
