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

The included `verify.py` was executed in Python 3 using exact rational arithmetic and returned:

`PASS: 2589 exact rational polygon checks (including sharpness).`

The tests covered 2,500 independent random centrally symmetric rational polygons containing the normalized diamond and 89 rational parameters in the sharpness family. Each test reconstructed the polygon's area, extreme height, central chord, inscribed parallelogram, deficit, and maximum over its vertices of the parallelogram gauge. The sharpness parameters additionally satisfy the asserted equalities exactly.

The proof in RESULT.md is analytic and applies to all origin-symmetric full-dimensional planar convex bodies and real parameters. The randomized polygons and finite sharpness examples do not constitute an exhaustive verification of continuous convex bodies, nor an independent validation. The primitive-lattice and one-dimensional covering-radius identities were checked symbolically in the proof; the standalone script focuses on the independent geometric step.
