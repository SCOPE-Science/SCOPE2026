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

The proof is analytical. Execute the included `check_toroid.py` with Python 3, NumPy and SciPy to independently test the azimuth-feasibility classifier, invariant-plane weighted probabilities, and the derivative inversion for ellipses. A successful run prints `TOROID_TOPOLOGY_INVERSE_OK` with comparison counts and errors. The code checks finite samples only and does not certify an infinite theorem. The inverse conclusion additionally needs a known full family of toroids with fixed meridian and variable revolution radius.
