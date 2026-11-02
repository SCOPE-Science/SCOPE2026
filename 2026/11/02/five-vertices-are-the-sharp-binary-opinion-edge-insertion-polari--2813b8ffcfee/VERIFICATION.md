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

# Verification of finite binary polarization classification

Run `python3 verify_binary.py` using only the Python 3 standard library. The replay enumerates every connected labeled graph with two through five vertices, every missing edge, and every binary opinion vector, using exact rational inverses. It validates the inverse matrices by exact multiplication and checks that the strict-increase census is \(0,0,0,480\) for orders \(2,3,4,5\). It also checks the canonical orbit classes \((58,0,9)\) and \((185,1,11)\), each of size \(240\), and independently recomputes their exact rational differences \(8/405\) and \(18123/1250600\).

The successful replay prints `EXHAUSTIVE_RATIONAL_CENSUS_OK` followed by the four graph/test/increase totals and the two orbit counts. The finite enumeration is exhaustive for its explicitly bounded domain, not a proof about unbounded graph size or arbitrary edge weights. The analytical mean-centering and rank-one arguments are given in RESULT.md; they are not substitutes for the full finite graph census.
