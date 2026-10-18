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

Run `python verify.py` using the Python standard library. The observed output was `PASS: 5528 finite independent matrix and affine checks`.

For each integer 3 through 30 and seven relaxation parameters (including both endpoints), the verifier independently composes all Euclidean projectors and reflectors in the stated order and compares the resulting 2-by-2 matrix to the closed-form theorem. It also checks four powers, singular-norm comparisons, and explicitly translated line-map differences. These computations do not exhaust real relaxation parameters or arbitrary line counts, and they do not constitute a numerical certificate for infinitely many cases. The analytical rotation-conjugacy argument, finite-product telescope and explicit triangular power prove those cases.

No independent audit has yet been performed. Earlier potentially equivalent specialized treatments remain a bibliographic risk.
