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

## Reproducible checks

Execute `python3 verify_graph.py` from a directory containing the provided standalone source. The checker constructs all nonzero pairs of relevant upper off-diagonal matrices and directly evaluates the finite-field commutation equation. It computes the reduced quotient graph, whose vertices lift to identical complete twin classes in the actual group commuting graph, and checks component sizes and diameters. It covers thirteen test tuples and the finite fields of orders two, three, four and five. Expected final line: `ALL_GRAPH_CHECKS_PASSED 13`. The field of order four is implemented using the irreducible polynomial `t*t+t+1` over the binary field.

## Mathematical boundaries

Finite enumeration tests only the listed small cases, not the quantified statement for every finite field or block size. General validity comes from the complete symbolic proof in `RESULT.md`. The exact diameter for the interior range where the smaller outer width lies strictly between one and the middle width is not claimed. Independent mathematical audit has not been performed.
