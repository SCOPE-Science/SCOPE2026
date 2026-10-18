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

# Reproducibility and proof boundaries

The mathematical proof is in `RESULT.md`. Its key implications are: a four-bit profile is complete for pointed first-order rank one; if the outside-both bit vanishes on any cell, the support is contained in a two-star and yields at most five types; otherwise eight types is the universal upper bound; four required two-element cells plus four one-element cells yield the sharp size twelve; and three core incidences, each admitting four leaf-weight assignments, give precisely twelve minimal isomorphism types.

From the extracted directory, run:

```
python3 verify_templates.py
g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
```

The first program checks all twelve explicit weighted-cell templates, their profile completeness and pairwise nonisomorphism using canonical incidence-equality matrices. It also checks the listed twelve-element witness. The second enumerates every restricted-growth \(F\)-partition for one \(E\)-partition of each integer block-size pattern on each of one through twelve elements. At twelve, this means \(324{,}446{,}969\) candidates (not isomorphism types); \(2{,}448\) candidates attain the eight-profile signature. It also computes the exact number of observed signatures at every size through twelve. The captured outputs are in `verification_output.txt`.

The all-cardinality theorem and twelve-isomorphism-type classification follow from the written combinatorial argument; a finite enumeration on its own would not prove either assertion. This package does not include an external or independent audit.
