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

Run `python3 verify.py` with Python 3 using only standard-library modules. The diagnostic outputs should include:

`VERIFY_OK exact_rational_competitors=14263 junction_identities=34 boundary_samples=5712 monotone_ratio_steps=3400`

The exact-rational comparisons concern the squares of ellipsoid volume objectives, and the exact grid-monotonicity comparison removes the common factor \((\kappa_d/\kappa_{d-1})^2\). The sampled geometric boundary tests use seeded pseudorandom points. All such experiments are finite; the proof's symmetry reduction, exact support equivalence, derivative sign, and weighted-mean monotonicity cover all dimensions \(d\ge2\) and all real \(0\le t\le1\). The contact threshold and both endpoint cases are handled analytically in `RESULT.md`. No external independent audit has been performed.
