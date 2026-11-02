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

# Reproducible finite verification

All checks use Python 3.10 or later and its standard library only. Execute from the directory containing both included files:

```sh
python3 verify_petersen_direct.py
python3 verify_triangle_orbits.py
```

The first verifier defines the Petersen graph directly by disjoint two-subsets of a five-element set. It tests the open-neighborhood total-domination condition on all \(1024\) masks, creates every cap-specific add/delete adjacency, checks the sharp connectivity transition, and performs exact breadth-first search from every one of the \(332\) cap-seven states. The second independently enumerates triangle-free five-vertex graphs by forbidden triangle masks, constructs all \(120\) ground-label permutations, verifies ten complete orbit classes, and obtains all-pairs distance counts from ten orbit representatives.

Actual run output includes:

```text
MINIMAL_TDS 4:10 5:12 6:5
CAP_4 states=10 components=10 largest=1
CAP_5 states=82 components=22 largest=7
CAP_6 states=222 components=6 largest=217
CAP_7 states=332 components=1 largest=332
DIRECT_DISTANCE_PASS states=332 edges=980 radius=8 diameter=10
ECC 8:100 9:220 10:12
UNORDERED_DISTANCE_HISTOGRAM 980 3210 7070 11585 13170 10970 5810 1875 270 6
HAMMING_DEFECT 0:54211 2:735
COMPLEMENTARY_C5_DIAMETRAL_PAIRS 6
DIRECT_PETERSEN_TDS_CERTIFICATE_PASS
ORBIT_COUNT 10 S5_SIZE=120
ORBIT_CERTIFICATE_PASS states=332 edges=980 radius=8 diameter=10
DIAMETRAL_PAIRS_ARE_SIX_COMPLEMENTARY_C5_PAIRS
TRIANGLE_ORBIT_CERTIFICATE_PASS
```

A full ten-row orbit certificate, including degree, eccentricity and every distance shell, is printed by the second program. The first program does not assume the triangle-free reduction; the second does not call the Petersen total-domination predicate. This independent formulation guards against a shared modelling error, but does not constitute independent scholarly review. Exact finite enumeration proves the stated finite conclusions only because the search domain and successor relation are exhaustive. It neither proves uniqueness in the historical literature nor establishes a theorem for larger graphs.
