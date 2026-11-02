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

# Verification record

The analytical proof in `RESULT.md` establishes the universal theorem; `verify.py` provides supplemental exact-rational consistency tests (17,464 passed at preparation). It checks the integral and both split products, the exact bias decomposition, the two tridiagonal forms, the echo summation by parts, all-uniform grids, two-step sharp ratio, and three-step failures.

Reproduce with `python3 verify.py` from the directory containing the complete files. Only Python standard-library modules are used. The randomized rational test cases have a fixed seed. The assertions are finite consistency tests, not a proof of positivity for infinitely many meshes. The leading-minor necessity/sufficiency and all-dimensional quantifiers are proved directly in `RESULT.md`. Independent mathematical validation has not been carried out.
