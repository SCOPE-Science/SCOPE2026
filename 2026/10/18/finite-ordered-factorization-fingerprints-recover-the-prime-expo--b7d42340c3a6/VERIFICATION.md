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

# Reproduction and limitations

Run `python3 CHECKER.py` using the standard Python 3 library. Its output is `PASS: 33487 exact exponent tuples recovered; three sharpness witnesses.` It reconstructs interpolated monic polynomials using rational fractions, divides out negative integer roots, and checks direct ordered-factorization identities. Finite tests do not establish universal injectivity; the proof in `RESULT.md` establishes it by the degree bound on a difference of monic polynomials. The script checks sharpness witnesses for supports two, three and four, while the support-one witness is immediate from the formula for two-factor counts.

This package has received self-review only. No independent audit, external certification or automated proof-assistant validation has been performed.
