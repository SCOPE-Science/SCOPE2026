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

The proof in RESULT.md establishes the statement for all stated integers. The standalone standard-library verifier rebuilds each graph from its undirected edge set and computes full zero-forcing closures from all size-(2k-1) subsets. For k=1..4, n=2k+3..2k+10 and d=1..k it checks exact candidate families and counts (80 cases, 341272 subsets). It directly checks a size-2k forcing witness when d<k. The verified run printed ALL_EDGE_LENGTH_CASES_OK 80, EXHAUSTIVE_MINIMUM_CANDIDATES_OK 341272, OPTIMAL_SEED_COUNT_OK 4k-2 when d=k, zero when d<k, VERIFY_OK. This is finite verification, not an independent infinite proof.

Run `python3 verify.py` using only Python 3's standard library.
