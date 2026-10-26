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

# Internal mathematical verification and limits

Execute `python checker.py` with NumPy, SciPy and SymPy. In the provided package, this program passed 1,385 deterministic assertions: stationary two-mode moment balances; characteristic and parameter-polynomial factorizations; agreement of explicit real/complex/double-root covariances with direct two-by-two matrix exponentials; and positive-parameter cases spanning all proposed regimes. The exact zero count for infinitely many lags, uniqueness on the real branch, and limiting first-zero asymptotic come from the symbolic generator proof in `RESULT.md`, not from enumeration. No external or independent audit has been performed.
