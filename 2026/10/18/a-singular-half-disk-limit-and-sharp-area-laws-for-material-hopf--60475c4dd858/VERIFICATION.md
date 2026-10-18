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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.10 or later. The checker uses only Python standard-library modules and must report `PASS: 78 independent finite consistency assertions; standard-library Python`.

The checks compare a divergence-theorem boundary quadrature against an independently evaluated algebraic area expression for four geometric regimes at four times each; measure boundary speeds by a separate parametric derivative; compare late-time lengths with the proved limiting values; test the first asymptotic area terms; evaluate five nontrivial points of the critical parameter boundary layer in both planar coordinates; and sample radial derivative/Jacobian formulas.

**Scope of verification:** Float quadrature and sample tests cannot certify all parameter choices or any infinite-time claim. The analytic differentiation, divergence theorem, winding/tangent geometry, boundary-layer limit, and Taylor expansions in `RESULT.md` constitute the proof. No independent external audit has been performed.
