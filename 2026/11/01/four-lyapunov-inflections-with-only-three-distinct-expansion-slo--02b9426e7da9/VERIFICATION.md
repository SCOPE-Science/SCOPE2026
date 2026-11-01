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
# Reproducible checks
Execute `python verification.py` using `mpmath` with interval arithmetic. Five strict rational-argument sign enclosures with 75-digit outward bounds give the sequence negative, positive, negative, positive, negative; hence at least four distinct zeros with sign changes by continuity. The checker does not infer infinite results from a finite sample: analytic thermodynamic identities transfer the certified signs to spectrum curvature, and the published theorem supplies minimality. The exact count of all inflections for the witness is not established.
