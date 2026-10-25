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

The complete component-budget filtration is finite: all 1023 nonempty subsets of the ten-vertex Petersen graph are enumerated. Reproduction requires `verify.py` and `collapse_pairs.json`; run `python3 verify.py` with the standard Python library. The output is recorded in `verification_output.txt`.

The checker constructs adjacency from disjoint two-subset labels. Two independent connected-component traversals agree on all masks. Exact reduction of the full filtered mod-two boundary matrix yields the stated barcode, with 511 boundary-pivot pairs and a single unpaired ordinary degree-zero generator. Independent boundary-rank computations cover ten levels, and independent cycle-inclusion computations check 279 induced-map ranks. A 60-pair ordered certificate is replayed against the actual face sets: every lower face has exactly one remaining strict coface and all removed faces lie outside the preserved threshold-two subcomplex.

`VERIFY_OK` is printed only after all assertions succeed. This finite exhaustive certificate establishes the stated finite-graph claims; it does not establish integral persistence, untested graphs, or literature priority. Independent audit has not been performed.
