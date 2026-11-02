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

# Verification

The theorem is proved analytically in `RESULT.md` by a direct trace/determinant computation for one to four factors, Perron-root monotonicity at common determinant, and positive exact pairing differences. The four-season traces and determinant in the epidemic reversal are rational values, so no floating-point tolerance is used to certify invasion signs.

Run `python3 CHECK.py` in the same directory. The Python-standard-library checker tests 9,963 exact rational product/trace/determinant comparisons, all 24 permutations of 405 four-distinct-level combinations, three ordered traces of multiplicity eight, all one- to three-season permutations in the test grid, and the exact invasion reversal.

These computations are corroborating finite checks, not a proof of universal quantifiers. The article's complete general result rests on the algebra in `RESULT.md`. The checked claim concerns local disease-free epidemic invasion in a discrete SEIS model. It makes no claims about nonlinear transient epidemics, noise, or arbitrary positive-matrix families. Historical priority has unresolved full-text access risks. Independent scientific audit has not been performed.
