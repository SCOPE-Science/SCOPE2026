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

The theorem is established by the cyclic-gap argument in `RESULT.md`; the two Python programs are independently structured finite checks, not a substitute for the general proof.

Run `python3 check_direct.py` to enumerate sets from the closed-neighborhood definition for cycle orders 4 through 22 and check all one-vertex replacements. Expected terminal marker: `CYCLE_ISOLATION_DIRECT_GRAPH_PASS`.

Run `python3 check_gaps.py` to enumerate cyclic weak compositions for cycle orders 5 through 54 and check the exchange degrees and connectedness for orders up to 38. Expected terminal marker: `CYCLE_ISOLATION_GAP_MODEL_PASS`.

These scripts require only the Python standard library. The finite checks establish the asserted enumerations in their tested ranges. The proof, rather than finite extrapolation, establishes every order \(n\ge5\). The connected components of the graph for orders divisible by four are isolated points; the smaller order-four exception is recorded separately. No other verification channel has been performed.
