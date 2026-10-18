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

Analytical checks: moment conditions from telescoping the zero-extended second difference; injectivity and the exact range dimension; two-by-two Gram inversion for the least-squares affine correction; exact rational factorization of the adjacent-site difference; equality characterization by the projection form of Cauchy–Schwarz; and leading-order asymptotics of the parity formulas.

Standalone reproduction: run `python verify.py` (Python 3, standard library only) beside this file. The executed checker reported `PASS: 938 exact rational/finite-limit diagnostic assertions; n=1,...,17`. It constructs an independent finite second-difference Gram matrix and solves rational linear systems for its Green diagonals. It compares all sites for each finite tested size, checks moment constraints and each proposed extremal reconstruction, confirms central sites and the difference identity, and checks three finite asymptotic approximations.

Scope and limits: finite diagnostics do not establish the all-length theorem; that follows from the explicit proof in RESULT.md. The originality finding remains subject to possible earlier fourth-order Green-function formulations. Independent audit is not performed, and no external certification is claimed.
