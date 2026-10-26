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
# Reproducibility

Compile and execute both supplied standalone C++17 files:

```
g++ -O3 -std=c++17 verify_gp.cpp -o check_gp && ./check_gp
g++ -O3 -std=c++17 verify_kg.cpp -o check_kg && ./check_kg
```

Both check the full exhaustive configuration space, all distance shells, the seven diametral cycle patterns, and transport-gap counts. Both return `VERIFY_OK` only after exact equality checks; successful exit is the required diagnostic. The first also checks the factorial-radix round trip for every integer index. The second encodes inverse permutations and builds the Petersen graph independently as \(KG(5,2)\).

**Expected checks:** \(10!=3{,}628{,}800\) configurations, \(15\) generators, eccentricity \(13\), \(11616\) antipodes, shell counts \((1,15,135,955,5504,26096,99739,297535,655169,984833,923838,493350,130014,11616)\), and transport-gap counts \((431532,1509516,1382012,299060,6680)\) for gaps \(0,1,2,3,4\). The seven antipodal cycle counts are \((5832,24,960,960,2280,1320,240)\) in the displayed RESULT ordering.

**Proof scope:** Breadth-first search on an exhaustively indexed finite graph establishes exact metric data, not a general symbolic solution to token swapping. Source comparisons limit novelty risk but cannot eliminate unindexed or inaccessible computations. Independent external verification has not been performed.
