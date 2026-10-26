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

Run `python3 verify.py` with the standard Python 3 library. The script computes the exact valuation map, detects its eventual least period, and compares it to the recursive reduction for \(p=2,3,5,7,11\) and every initial exponent \(p\le m<1500\). It also checks explicit complete-period witnesses, exact rational partial density sums, and finite counting estimates. The instance \(p=2\) serves only as a regression check, not as a newly claimed theorem.

A length-\(R\) partial density sum is exactly rational and differs from the infinite sum by at most \(p^{-R}\). Numerical checks do not establish the infinite theorem; its separate proof is in `RESULT.md`. No external audit has been performed.
