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

# Reproducible verification

The supplied standalone `verify.py` requires only Python 3 and the standard library. Execute it in the same directory as this document using `python3 verify.py`.

The verification run passed 3,000 fixed-gap split comparisons, 3,000 evaluations of strict second-derivative negativity, and 3,000 global-gap comparisons against 52 test schedules apiece. It also compared 120 exact flow compositions with independent Simpson integrations of both wet infiltration intervals, performed 800 independent centered-difference derivative comparisons, verified the exact \(T=\log32\) benchmark, and tested the cutoff, monotone rest duration, large-horizon saturation, and critical onset.

The calculation relies on a fixed reproducible pseudorandom seed. Its randomized comparisons sample finite real inputs; they do not establish the global-in-parameters claim. The proof of that claim uses the exact switched-flow composition, arithmetic–geometric mean inequality, strict concavity, and implicit differentiation documented in `RESULT.md`. No external or independent audit has been performed.
