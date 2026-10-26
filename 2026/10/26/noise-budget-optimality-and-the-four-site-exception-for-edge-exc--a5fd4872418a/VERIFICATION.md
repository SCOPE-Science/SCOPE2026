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

# Reproducibility
The analytic derivation of the invariant diagonal and off-diagonal sectors, the sum-rule upper bound, the equality equations and the four-site spectral calculation are written in `RESULT.md`. Reproduce the finite checks with `python3 artifacts/verify.py` (NumPy required). Expected final line: `CHECKS_PASSED 157`.

The checker builds every superoperator from the elementary matrix formula on the full \(N^2\)-dimensional space and independently computes its eigenvalues. It checks all \(N=3,4\) unweighted graphs, randomly weighted examples through \(N=6\), budget upper bounds and five exceptional four-site allocations. The numerical tests cannot certify an arbitrary-\(N\) theorem or literature-wide novelty; the written proof supplies the former. No independent audit has been performed.
