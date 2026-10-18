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

Running `python verify.py` with Python 3.10 or newer and SymPy reconstructs the three 16-state transfer matrices from their five-site spin inequalities. It checks all characteristic polynomial identities exactly over the integers, identifies the nontrivial strongly connected components, checks the displayed Collatz–Wielandt rational eigenvalue bounds, verifies aperiodicity and compares transfer traces to direct recomputation of the complete Hamiltonian under each possible spin flip.

All checks passed in the packaged source: 24,480 labelled configurations, at each length from 5 through 12, across all three regimes. This finite verification is not the proof of the infinite-length entropy limits; those are consequences of the exact transfer coding and primitive strongly connected component arguments.

The verification requires no external data and no numerical eigensolver. It does require SymPy. Neither independent scientific validation nor any external audit has been performed.
