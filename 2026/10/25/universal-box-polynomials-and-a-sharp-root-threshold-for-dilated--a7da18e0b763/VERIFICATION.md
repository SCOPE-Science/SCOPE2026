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

Run `python3 verify.py` using Python 3.10 or later; only standard library modules `fractions` and `math` are used. The checker independently derives Ehrhart numerators from exact lattice-point counts and enumerates strict barycentric open-box representatives in 124 dilated examples. It checks the closed-form ordinary and local numerators and the strict two-gamma-coefficient inequalities, and separately verifies the dilation-two factorizations for normalized volumes from two to one hundred.

Actual execution: `EXACT_OK parameter_cases=124 empty_tetra_shapes=31 box_points=19368 hstar_interpolation=True`.

The finite parameter range does not itself prove the theorem in all volumes and dilations. The all-parameter proof is given in RESULT.md. Historical novelty remains conditional on the inspected literature; no independent scientific audit has been performed.
