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

# Finite verification record

Two independently developed C++17 programs were compiled and executed for every order from 3 through 24. Their outputs agree in the exact shortest admissible length at all 22 orders. The first program performs full product-state unit-cost breadth-first search, including forbidden-run tracking; the second performs a weighted subset shortest-path search after the independently proved normal form. The latter does not use the former program or its distances. Both programs output explicit witnesses; those may differ but were separately replayed to a singleton under the defined transitions. The product-state search processes 25,165,756 nodes at order 24, and the weighted search processes 8,388,585. The CSV holds the latter witnesses and both programs' visited-state counts. `artifacts/verify_witnesses.py` directly replays each CSV word and the all-order constructive witnesses through order 100. Reconstruct the finite shortest-path argument by inspecting the actual program source before relying on computed values. Experiments beyond the proven order range are not supplied as proof of the extrapolated length formula.
