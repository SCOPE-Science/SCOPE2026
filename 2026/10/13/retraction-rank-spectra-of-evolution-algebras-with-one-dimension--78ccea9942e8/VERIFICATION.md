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

# Reproducible verification

Execute `python3 checker.py` in an environment with Python 3 and no third-party dependencies. Successful execution prints `VERIFY_OK`. The checker directly enumerates composition-idempotent algebra-homomorphism matrices for seven odd-prime-field test inputs, rather than assuming the derived parametrization. A second implementation enumerates row-reduced subspaces in seven inputs and checks total isotropy and exclusion of the distinguished vector. Outputs include the rank multiplicities.

The full generality of the result is deductive: nondegeneracy and composition-idempotence imply the projection classification; a geometric counting bijection and a hyperbolic-frame count imply the finite-field polynomial. The tests do not establish the result for untested field orders or dimensions. No external or independent audit has been conducted.
