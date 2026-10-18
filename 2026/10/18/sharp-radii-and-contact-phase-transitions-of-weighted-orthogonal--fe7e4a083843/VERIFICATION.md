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

# Verification and reproducibility

The exact theorem is proved in `RESULT.md` by reduction to a strictly concave support-function maximization over a simplex, complete active-set KKT conditions, and equality analysis. The centered inradius is established by strict concavity at the simplex vertices. Contact points follow from equality in Cauchy–Schwarz, rather than simulation.

Run `python3 check_geometry.py` using Python 3 and only the standard library. The deterministic checker examines 390 weight profiles in dimensions three through eight, 136,500 direct random unit directions, independently enumerated finite-dimensional stationary candidates on all coordinate faces, and the three-dimensional transition and boundary examples. It is numerical corroboration, not an exhaustive search over real weights or dimensions and not a replacement for the proof.

No independent mathematical audit or external formal proof certification has been performed.
