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

## Exact checks
Running `python3 verify.py` checks all labeled simple graphs through order five, all connected graph isomorphism representatives via exhaustive permutations, all binary assignments with at least two agents per type, and all two-agent swaps. It uses integer cross multiplication for utility inequalities and checks all counted outcomes against independent benchmark connected-graph counts. The six-edge witness utilities are checked with `fractions.Fraction`.

The complete enumeration establishes only the finite, precisely stated theorem; no infinite order or randomized simulation is used. The exact certificate was executed successfully after construction. Independent scientific audit was not performed.
