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

Run `python CHECK.py` with Python 3 and SymPy installed. It verifies the differential cancellation, the unique equilibrium, the radial-moment algebra, and the final residence-bound algebra exactly. The separate written proof supplies the invariant-measure conditional law and the uniform residence bound; the script does not claim to enumerate infinite trajectories or invariant measures. No independent audit has been performed.
