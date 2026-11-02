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

# Reproducible checks and boundaries

The package contains `certificate.json`, `verify.py`, and `verify_normal_forms.cpp`. No external Python packages are needed.

Run from the package directory:

```sh
python3 verify.py
c++ -std=c++17 -O2 verify_normal_forms.cpp -o verify_normal_forms
./verify_normal_forms
```

Replayed output from Python:

```text
THREE_QUERY_STATIC_SHATTER_PASS 8
STRUCTURAL_BRANCH_TYPES_PASS ambient=4..8
FOUR_QUERY_STATIC_SHATTER_PASS 16
DEPTH_FIVE_ONLINE_TREE_PASS 31 32
UNIVERSAL_FIVE_QUERY_OBSTRUCTION_PASS 7260 normal_forms max_nonzero_patterns 26
EXACT_SMALL_ONLINE_PASS 1 0 2
EXACT_SMALL_ONLINE_PASS 2 0 2
EXACT_SMALL_ONLINE_PASS 3 1 4
EXACT_SMALL_ONLINE_PASS 4 3 16
EXACT_SMALL_ONLINE_PASS 5 4 64
EXACT_SMALL_ONLINE_PASS 6 5 64
RADIUS_TWO_ALL_CHECKS_PASS
```

Independently implemented C++17 output:

```text
INDEPENDENT_INCIDENCE_ENUM_PASS 7260 max_nonzero_patterns 26
```

The Python checker verifies three- and four-query static witnesses and finite checks of the universal branch-type classification through eight coordinates. It also verifies the four-query static witness, the entire 31-internal-node depth-five decision tree with 32 distinct terminal centers, exact online depths in dimensions one through six using an exhaustive recurrence, and all five-query coordinate-incidence normal forms. The independent C++17 checker uses incremental incidence-column enumeration and a separate Hamming-distance formula. Both enumerate the same complete 7,260 normal forms and establish a strict obstruction to all 31 required nonzero traces.

The universal online upper bound is an independently stated mathematical case argument in `RESULT.md`; the finite recurrence does not itself prove the all-dimensional bound. The exhaustive coordinate-incidence argument is a valid all-dimensional VC certificate because every proposed five-query shattered set has an all-positive center and hence the five support weights are at most two. An audit of any alternative implementation should check this reduction and the star-family branch cases.

Self-review: passed. Independent audit: not yet performed.
