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

# Mathematical verification

The complete proof uses only graph cut counting, Euclidean facet distances, and linear-algebra ranks. The supporting `verify.py` uses solely Python integer arithmetic, rational Gaussian elimination, and explicit connected-subset enumeration; run with `python verify.py`.

Actual run output:

```text
EXACT_OK orbit_cut_tests= 548905 explicit_connected_subset_tests= 55972 contact_normal_rank_cases= 26
```

The first check includes \(2\le p\le21\) and \(p\le q\le70\); all integer orbit inequalities and equality cases are checked without floating-point approximations. The second enumerates connected induced vertex subsets for \(2\le p\le5\), \(p\le q\le9\); the third recomputes the exact rank of the tangent-normal span for these \(26\) graph sizes. These finite computations are not an infinite-parameter proof, which is given by the elementary inequalities in `RESULT.md`.

There is no independent scientific audit or certification.
