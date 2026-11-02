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

Run `python3 verify.py` from this directory using the Python standard library. The program independently represents tournaments by their edge-orientation masks and counts directed simple cycles from cyclic words. It compares exhaustive exact moments against the claimed rational formulas, tests the triangle outdegree identity, checks the mixed residual moment, and calculates Walsh coefficients up to degree two. The observed output reports 101745 passing assertions across all tournament sizes from 3 through 6.

For unbounded sizes and fixed-length asymptotics, the proof in `RESULT.md`, not finite enumeration, supplies the argument. The remaining novelty uncertainty is the possible derivability from general random-tournament subgraph-count work. No independent audit has been performed.
