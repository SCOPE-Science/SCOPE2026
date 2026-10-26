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

# Verification of exact finite classification

Run `python3 verify.py` with Python 3.10+ (standard library only). It constructs graph edges algebraically, counts all base four-cocliques and rules out independent five-sets, enumerates all reciprocal maximum-coclique neighborhood systems, checks the induced token graph independence of each candidate, classifies the auxiliary graph, and partitions all solutions under the explicitly generated full base-graph automorphism actions.

Expected output ends `VERIFY_OK`. The six coclique/orbit count vectors and both auxiliary structural types are asserted. Every vertex and edge of each 120-state two-token graph is generated, not randomly sampled. The completeness proof uses the exhaustive search recursion and the exact local upper bound. No external validation or infinite-parameter assertion is represented.
