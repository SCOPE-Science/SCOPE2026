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

# Verification details

Run `python3 verify.py` using Python 3.8 or later; no external packages are required. The code builds the graph \(K_{n,n}-M-a_0\) from the edge rule, computes all residual degrees from adjacency, then checks each of its \(2^{2n-1}\) subsets directly against the degree-based strong-domination definition. It separately expands the four-case symbolic polynomial using integer binomial coefficients and compares all coefficients.

Observed complete checks (all passed):

```text
REMOVAL_ALL_SUBSETS_OK n=3 subsets=32 first=2 count=1 total=13
REMOVAL_ALL_SUBSETS_OK n=4 subsets=128 first=3 count=7 total=53
REMOVAL_ALL_SUBSETS_OK n=5 subsets=512 first=3 count=10 total=225
REMOVAL_ALL_SUBSETS_OK n=6 subsets=2048 first=3 count=15 total=945
REMOVAL_ALL_SUBSETS_OK n=7 subsets=8192 first=3 count=21 total=3905
REMOVAL_ALL_SUBSETS_OK n=8 subsets=32768 first=3 count=28 total=15937
REMOVAL_ALL_SUBSETS_OK n=9 subsets=131072 first=3 count=36 total=64513
VERIFY_OK
```

There are \(174752\) directly examined subsets in total. This is exhaustive for the tested finite orders, not for all orders. The unconditional result for arbitrary \(n\ge3\) is established by the case-by-case degree proof in `RESULT.md`, which also treats the smallest cases. The checker does not independently certify the proof, the prior-work priority, or a larger graph class.
