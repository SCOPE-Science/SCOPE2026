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

Run `python3 petal_gamma_quotient_verify.py`. The script reconstructs the move-state component from the published definitions, asserts the independently published total of \(3186\) states and the \(18/3168\) layer split, then computes the new orbit and quotient data. A passing replay prints `VERIFY_OK`, \(145\) dihedral quotient vertices, orbit profile one size-\(18\) orbit plus \(144\) size-\(22\) orbits, \(144\) quotient edges, and degree profile one \(144\) with \(144\) ones.

The computation is exhaustive only within the explicit cap of eleven petals. It does not certify any assertion about routes through thirteen or more petals or the unrestricted move graph.
