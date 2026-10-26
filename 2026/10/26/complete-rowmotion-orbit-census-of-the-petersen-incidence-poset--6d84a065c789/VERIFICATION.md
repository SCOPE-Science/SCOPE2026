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

# Reproduction and limits

Run `python3 verify_petersen_rowmotion.py` with Python 3.10 or later. No third-party module, external dataset, random seed, service or network connection is required.

The verifier enumerates the complete set of ideals by selecting each vertex subset \(U\) and then every submask of the edges induced by \(U\). It directly constructs minimal complement elements and their generated ideal, separately applies rank-ordered toggles to all states, checks equality of transitions, then performs complete cycle traversals. An independently encoded Kneser-graph model supplies a second full cycle census. Both exact histograms equal the declared 39-entry distribution; all weighted counts and the period are verified with integer arithmetic.

Expected terminal output ends with `VERIFY_OK`. This is an exact finite computation for one poset. It does not establish an infinite-family theorem or novelty against unpublished/unindexed material. Independent audit has not been performed.
