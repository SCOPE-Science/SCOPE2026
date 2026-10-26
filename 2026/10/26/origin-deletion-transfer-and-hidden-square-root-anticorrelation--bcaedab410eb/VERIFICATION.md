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

# Reproducibility and limits

Run `python verification.py` with Python 3 and the standard library. It enumerates all 50,068 maps on 2–6 points, compares their cyclic/origin counts with an independently calculated conditional mass function, checks the full mixed factorial-moment transfer, and verifies the exact covariance identity. It then checks conditional mean formulas with rational arithmetic through size 25 and reports the numerically converging asymptotic constant through size 10,000.

The exact tests pass 6,653 assertions over finite cases and enumerate 50,068 maps. The normalized covariance tends numerically to -0.230534252, consistent with the proven analytic value \(-\sqrt{\pi/2}/(2e)\). None of these finite computations proves the asymptotic claim, which relies on the dominated Riemann-sum argument and the explicit tail estimate in RESULT.md. No independent audit has been performed.
