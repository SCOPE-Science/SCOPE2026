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

# Reproducible numerical checks and proof scope

Run `python3 verify_parity.py` with a standard Python 3 installation. The program requires only Python standard-library modules. It constructs pure-loss Kraus output photon-number probabilities from normalized random complex Fock vectors, compares them against the analytic parity-generating polynomial, and checks the sharp extrema for all \(2\le K\le11\). It also checks the equality cutoffs, repeated adjacent even–odd values, strict monotonic trend, and a radial two-Fock-state transition example.

An execution against the supplied program gave:

`VERIFY_OK pure_loss_kraus_cases=5600 exact_sharp_cutoffs=10 odd_cutoff_plateau=passed radial_transition=passed`

The numerical assertions have finite scope and do not prove a universal inequality. The general proof uses the exact binomial identity, coefficientwise bounds and one-variable convex minimization in `RESULT.md`. The program does not test the entire mixed-state cone or exhaust all cutoff values. No independent validation has been performed.
