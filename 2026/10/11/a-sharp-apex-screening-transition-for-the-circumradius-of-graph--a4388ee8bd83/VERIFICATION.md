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

# Verification record

The general theorem is proved by exact variance and barycenter identities in RESULT.md. The independent-set vertex test is exhaustive *for each listed finite test graph*, not exhaustive for all vertex-transitive graphs.

Run `python3 verify.py` with Python 3's standard library. It enumerates all independent sets of 41 graph cases in four explicit graph families and checks exact rational ball containment, strict contact classification, uniform maximum-set barycenter, weighted squared-distance identity and sign cases. The run completed with `EXACT_CHECKS_OK graph_classes= 41 indicator_vertices= 1733 max_contacts= 241`. An independent audit has not been performed.
