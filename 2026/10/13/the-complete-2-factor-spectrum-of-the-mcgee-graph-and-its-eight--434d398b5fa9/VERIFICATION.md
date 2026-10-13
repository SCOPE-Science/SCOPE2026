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

# Verification of McGee graph factor census

Run `python3 verify.py` with `matchings.csv` and `orbits.csv` in the same directory. It validates the graph, BFS girth seven and diameter four, exhaustive perfect-matching recurrence, independent memoized count, all 60 complementary cycle partitions, complete group of 32 distance-preserving automorphisms, and the orbit table.

Run `g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent` and `./verify_independent` to replay the separate C++ matching enumeration and cycle decomposition. It uses a distinct minimum-available-neighbors branching criterion and does not read the certificates. Both source files were actually compiled/executed as applicable.

Actual assertions printed:
```
VERIFY_OK McGee LCF=[-12,7,-7]^8 vertices=24 edges=36 girth=7 diameter=4
VERIFY_OK independent_matching_dp=60 recursive_matchings=60
VERIFY_OK two_factor_types=8+8+8:12,12+12:6,24:42
VERIFY_OK automorphisms=32 perfect_matching_orbits=8 orbit_distribution=2x1+4x2+8x2+16x2
VERIFY_OK orbits.csv=exact matchings.csv=exact
VERIFY_INDEPENDENT_OK perfect_matchings=60 two_factor_types=24:42,12+12:6,8+8+8:12
```
The verification is an exhaustive finite calculation on the declared 24-vertex graph. This is not a general graph theorem and has not undergone independent external mathematical review.
