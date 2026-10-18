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

The standalone `verify.py` uses Python's standard library (`fractions`, `math`) to expand normalized Chebyshev polynomials into affine Bernstein polynomials and back, exactly over the rationals. The command `python3 verify.py` checks all modes \(0\le m\le120\) at approximation degrees \(1,2,3,4\); the complete degree-four coefficient formulas for those modes; and the claimed negative leading Schoenberg coefficient at every degree \(5\le n\le25\). The exact finite check does not prove the infinite ranges; the analytic trigonometric bounds and finite-difference argument in `RESULT.md` do.

The distinct coefficient signs and zero patterns are asserted for the positive-semidefinite cone, not the strictly positive-definite cone. No independent scientific validation has been performed.
