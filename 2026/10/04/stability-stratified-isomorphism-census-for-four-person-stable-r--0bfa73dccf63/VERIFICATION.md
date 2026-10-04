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
The embedded `verify_roommates4_orbits.py` exhausts all \(6^4=1296\) strict four-agent roommate profiles. It computes stability using two independent implementations and computes relabeling classes by two independent group-action routes: canonical representatives and stability-stratified Burnside averaging.

Replay command:

`python3 verify_roommates4_orbits.py`

Expected leading output:

`VERIFY_OK`

The replay verifies the labeled split \(48,1098,150\), the unlabeled split \(2,51,7\), the complete orbit-size distribution, the Burnside fixed-count table by conjugacy class, and the exact two unsolvable canonical representatives. Because every profile is enumerated, this is an exhaustive finite certificate rather than a sample or timeout-based inference.
