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
The analytic proof uses the exact occupancy identity for complete multipartite graphs. The only computational artifact is `verify.py`, which is a finite corroboration and not an infinite certificate.

Replay command:

`python verify.py`

Expected successful output:

`ALL CHECKS PASSED; multipartite_profiles_N<=11=183; bipartite_profiles_a,b<=20=210`

The verifier independently enumerates all occupancy vectors to obtain \(\gamma_2\), independently enumerates all vertex-deletion count vectors to obtain stability, and compares those values with the closed formulas. It explicitly checks the boundary profiles \(K_{1,2}\), \(K_{2,2}\), \(K_{2,3}\), and \(K_{5,5}\).

Limit: the exhaustive enumeration stops at the stated finite ranges. The theorem for arbitrary order rests on the proof in `RESULT.md`.
