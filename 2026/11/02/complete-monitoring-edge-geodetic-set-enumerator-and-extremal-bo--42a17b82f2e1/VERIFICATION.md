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
# Reproducible finite verification

Run `python3 verify.py 13` in the directory containing the embedded source. This program computes cycle distances by breadth-first search, removes each edge in turn, and determines monitoring from strictly increased pair distances. It does not use the proof's gap predicate to classify a set. It exhaustively enumerates every subset for each order from three through thirteen, compares **every** polynomial coefficient with the derived formula, verifies the types and counts of all inclusion-minimal monitoring sets, confirms precisely the proposed maximal nonmonitoring blocks, and checks their maximum cardinality. The successful independent execution produced `VERIFY_OK`.

This is finite, exhaustive evidence for the tested cases only. The all-order assertion is supported by the written structural and counting proof. No symbolic proof assistant or independent audit was used.
