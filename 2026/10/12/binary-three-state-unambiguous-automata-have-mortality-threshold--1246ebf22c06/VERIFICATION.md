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

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The compiled verifier precomputes ordinary integer products of all \(512\) zero-one \(3\times3\) matrices. It then enumerates all \(262{,}144\) ordered generator pairs and computes their complete reachable product monoids from the identity. Any product entry above one certifies ambiguity; otherwise the breadth-first distance to zero is the exact shortest killing length.

A separate Boolean-relation composition implementation must agree with every integer product that remains zero-one. The replay checks the exact unambiguous and mortal counts, the complete length histogram, the twelve threshold-\(6\) extremizers, and their single canonical state-and-letter symmetry class.

Finally, it directly checks all binary words of lengths below \(6\) for the canonical representative and verifies that \(\mathtt{abaaba}\) has zero product. Independent audit has not been performed.
