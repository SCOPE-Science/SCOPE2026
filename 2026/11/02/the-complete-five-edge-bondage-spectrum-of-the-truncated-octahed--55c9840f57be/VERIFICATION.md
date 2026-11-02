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

Two independent exact programs were run successfully from their source definitions. `verify_fast.cpp` enumerates all vertex subsets of sizes 0–8 and all edge-deletion subsets of sizes 0–5. `verify_independent.py` uses a different domination-cover construction, bitset aggregation for all 376992 five-edge cases, checks an explicit LCF graph isomorphism, and independently classifies the eight orbits under 48 generated automorphisms.

The respective check results were 1767 minimum eight-vertex dominating sets, zero bondage sets for every deletion size below five, 276 bondage sets at deletion size five, and orbit sizes 12,24,24,24,48,48,48,48. No random sample, numerical approximation, timeout inference or claim of external certification is involved.

Reproduction from a clean source directory:

```sh
g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast
./verify_fast
python3 verify_independent.py
```

Boundary: full primary manuscript access was unavailable; it is not treated as inspected or certified. Mathematical priority remains qualified, and independent audit has not been performed.
