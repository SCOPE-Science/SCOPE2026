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

Run `python3 verify_gp.py` from the directory containing the two standalone verification files. No dependencies beyond the Python 3 standard library are needed.

The code reconstructs all 120 admissible four-column states and 291 transitions from the exact forbidden-pair table. It checks the supplied 120-entry integer potential against every transition, establishing the universal upper-bound certificate. It separately generates graph edges and their third-edge conflicts for eight sample graph orders to cross-check the table, and uses an exact branch recurrence to prove all four small-order maximum independent-set optima, 3, 4, 5 and 6.

Each of thirteen explicit base mask words is independently tested against graph edge conflicts, with the stated selected-edge count. The concatenation rule is mathematically justified by the shared length-four automaton state. Larger numeric checks on order 18 through 180 and 271, 360 and 721 are only corroborating examples; they do not constitute the infinite argument. The captured stdout is provided unchanged as `verification_output.txt`.

The claimed result is not an independent audit, a formal proof-assistant certification, or a proof about generalized Petersen graphs with other step sizes. Any external independent assessment remains unperformed.
