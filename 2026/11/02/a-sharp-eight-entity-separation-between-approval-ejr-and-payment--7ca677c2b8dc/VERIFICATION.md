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

# Verification scope

The standalone `verify.py` uses exact integer comparisons for all coalitions, rather than floating point. It enumerates every size-four elected multiset and one unelected approval mask for three voters (1,470 signatures), and every size-three elected multiset and one omitted mask for four voters (10,200 signatures). It forms orbits under all voter permutations and tests Pareto efficiency by the proved proper-subset condition. It additionally tests 19,448 other canonical small signatures as a consistency check. Run `python3 verify.py` and check its printed final marker and per-orbit counts. The general impossibility below eight entities depends on the analytical argument in `RESULT.md`, not on any finite sampling. No external independent audit has been performed.
