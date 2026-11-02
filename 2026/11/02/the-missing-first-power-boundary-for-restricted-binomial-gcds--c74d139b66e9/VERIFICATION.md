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

# Reproduction and limits

Run `python verify.py` in a Python 3 environment using only the standard library. The script checks the initial valuation profile at all primes through 199 (46 primes, 280419 selected coefficients), with independent exact-binomial checks for primes through 13. The executed program returned `VERIFY_OK`.

The infinite theorem is established by two-column Kummer carrying in `RESULT.md`; finite tests are corroboration, not a substitute for proof. The universal valuation ceiling two is an established result quoted from Fairfax-Ball, not a computation. Priority comparisons rely on accessible source texts and remain subject to independent literature review.
