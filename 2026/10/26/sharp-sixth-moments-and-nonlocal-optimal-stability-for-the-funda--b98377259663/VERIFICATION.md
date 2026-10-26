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

Run `python3 checker.py` using Python 3 and only the standard library. It constructs the finite Laurent polynomials from the three torus eigenvalues and multiplies by the Weyl density to reproduce, with exact rational arithmetic, the moments \(145,40,13,6,22\). It checks the characteristic deficit and derivative polynomial identities, verifies the sign intervals for the two positive roots, and executes 600 seeded finite complex-coefficient consistency tests. The complete observed output is in `checks.txt`.

The proof in `RESULT.md` establishes the infinite statements: Weyl integration is an identity on all class functions used; the phase reduction is exact; Descartes' rule proves the critical-point count; and the derivative sign pattern proves global optimality. Randomized tests, rounded decimals, and the execution log are corroboration, not a substitute for those arguments. No external scientific audit or independent validation has been performed.
