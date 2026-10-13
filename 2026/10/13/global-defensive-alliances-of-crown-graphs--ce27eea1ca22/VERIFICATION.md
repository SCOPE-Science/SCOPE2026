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
# Verification

The proof is symbolic and valid for every stated \(n\). The checker is a finite corroboration that independently implements the crown graph rather than the closed formulas.

`verify.py` enumerates every vertex subset for \(3\le n\le9\), directly evaluates the defensive-alliance inequality and domination condition, tests induced connectivity, compares those outcomes with the four-state classification, reconstructs the claimed polynomial coefficients from multinomial state counts, and checks the minimum formulas and multiplicities.

Replay from the finalized package produced:

`VERIFY_OK n_range=3..9 subset_checks=349504 defensive_sets=101028 global_sets=100972 connected_checks=100835 coefficient_checks=91 minimum_checks=7 max_order=18`

The exhaustive range is finite and is not evidence for the universal quantifier. The universal statement rests on the local-degree and domination arguments in `RESULT.md`.
