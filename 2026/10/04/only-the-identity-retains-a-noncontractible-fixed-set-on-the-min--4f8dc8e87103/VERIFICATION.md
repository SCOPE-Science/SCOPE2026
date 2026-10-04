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
`artifacts/verify.py` reconstructs the nine-point order from the cover list, enumerates all order-preserving self-maps, checks all completed maps against the transitive order, recomputes fixed-set multiplicities, and replays every certified beat-point deletion from `artifacts/fixed_sets.json`.

Expected output:

`VERIFY_OK maps=12575 distinct_fixed_sets=210 sizes=3493,4877,2909,1013,234,41,5,2,1 nonidentity_contractible=12574 dual=invariant`

The verifier does not derive the literature premise that the full nine-point space \(R\) is noncontractible; it checks that \(R\) has no beat point and uses the cited primary source for noncontractibility. The order-dual conclusion is mathematical: reversing all inequalities leaves the monotone self-maps unchanged as set maps and exchanges up-beat and down-beat certificates.
