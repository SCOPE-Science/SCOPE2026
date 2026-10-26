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

# Direct verification and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The program constructs labelled 3-neighbour adjacency rows from the definitions without using the polynomial proof. It computes every matrix-power rank up to one step past the predicted sharp transient for each integer \(3\le n\le128\) on both graphs; it also updates each individual binary state and computes the exact recurrent-image and earliest-entry-time distribution on both graphs for \(3\le n\le9\).

Recorded output: `VERIFY_OK ranks= 909  complete_small_graphs= 14  small_state_evaluations= 699008`. Additional displayed examples verify the graph sizes \(n=3,6,9,12,18,24,48\). Finite enumeration is not an all-parameter proof; the complete proof is the polynomial-factor and local Smith-form argument in `RESULT.md`.

No independent mathematical audit was performed.
