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

The proof in `RESULT.md` is analytic. It uses an exact renewal characteristic equation, dominated convergence on a rescaled newborn-age boundary layer, exponential bounds on the complementary ages, and two exact inequalities to force at least two threshold roots by continuity.

The bundled standard-library `verify.py` was executed from its own file path using `python3 verify.py`. It returned:

`VERIFY_OK exact bounds and independent finite-quadrature checks`

The executable independently checks exact rational inequalities and tests the displayed kernel numerically for the two feeding laws. The finite quadrature does not prove the infinite-domain limit or uniqueness of threshold crossings; uniqueness is not claimed. In particular, numerical verification is supplemental and not a substitute for the dominated-convergence and continuity arguments. A separate independent scientific audit has not been performed.
