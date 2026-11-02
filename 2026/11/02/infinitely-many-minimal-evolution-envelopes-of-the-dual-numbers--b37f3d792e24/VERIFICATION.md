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

The exact symbolic checks are reproducible from the attached standalone programs. `VERIFY_EXACT.py` computes the Vandermonde coefficients over rational fractions, verifies the dual-number multiplication table on a 625-pair sample grid for 21 integer parameters, and checks strictly distinct invariant values. `VERIFY_SYMBOLIC.py` inverts the generic Vandermonde matrix symbolically, checks its defining moment identities, derives the endomorphism eigenvalues, proves the rational invariant formula, and verifies the derivative identity. The outputs `VERIFY_EXACT.out` and `VERIFY_SYMBOLIC.out` record the actual runs and end `VERIFY_OK`.

The general all-integer statement rests on the algebraic proof in `RESULT.md`, not the finite test grid. These checks do not establish historical originality or constitute an independent mathematical audit. Reproduction requires Python 3; the symbolic checker additionally requires SymPy.
