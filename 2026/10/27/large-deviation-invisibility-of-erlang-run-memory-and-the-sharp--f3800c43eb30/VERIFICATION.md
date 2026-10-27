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

# Verification details
The accompanying `verify_pressure.py` independently builds the Markov phase generator and compares its leading eigenvalue with a stabilized scalar positive-root implementation. It runs 140 checks, across 16 phase-pairs, six randomized physical settings for each pair, the equal-phase quadratic formula, and five sets of extreme-tilt asymptotics at two tilt magnitudes. Reproduce with `python verify_pressure.py` after installing NumPy and SciPy. The spectral/root errors remained below 1.3e-11 in the recorded check. This is numerical corroboration, not an infinite-domain proof. The analytical argument in RESULT.md supplies general validity. The comparison with older Erlang telegraph finite-time theory is not an independent priority certification.
