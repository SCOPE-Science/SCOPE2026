---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem was checked against the full statements needed from the cited random-SWAP Schur-sampling construction: maximal first-column antisymmetry, the history-uniform growth lower bound, stochastic domination for history-dependent waiting times, the geometric-sum concentration inequality, and the pairwise-SWAP approximation cost for an antisymmetric measurement.

For a high sector \(h=\lambda'_1\ge r+1\), the proof uses only
\[
p_k\ge \frac{h-k}{(n-k)(k+1)}\ge \frac{r+1-k}{n(k+1)}
\]
for \(1\le k\le r\). The exact reciprocal sum is
\[
\sum_{k=1}^{r}\frac{n(k+1)}{r+1-k}=n((r+2)H_r-r).
\]
For a low sector \(h\le r\), reaching size \(r+1\) is impossible, so no bottom-of-column certification is needed for the binary decision.

The accompanying `artifacts/verify.py` checks the reciprocal-sum identity exactly for a range of \(r\), checks the auxiliary monotonic inequalities, and exhaustively verifies the deterministic partition-level mean bound for all integer partitions up to size \(12\). It returns `VERIFY_OK`. These finite checks are corroborative only; the general theorem follows from the analytic inequalities above.

The verification does not establish optimal logarithmic factors, does not implement a full post-measurement Schur instrument, and does not alter the copy complexity of the statistical rank-testing problem.
