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

# Verification

The complete finite check is `verify.py`, a standalone Python 3.10+ standard-library program. Executing it on the package files gives the exact output:

```
VERIFY_OK counts= [(1, 1, 1, 0), (2, 40, 8, 0), (3, 400, 33, 5), (4, 2306, 103, 48)] feature_comparisons= 53 witness_union_histograms= ((0, 1, 2, 7, 0), (0, 0, 6, 2, 2))
```

For every \(m\le4\), every multiset of \(m\) nonempty four-bit plant neighborhoods covering all four primary vertices is visited. The per-guild degree multisets determine a conservative equivalence key: comparing within those broad keys detects any counterexample with exactly fixed labeled margins. The sign-changing criterion \(a(a+b)<0\) follows from the exact double-root factorization, not a numerical grid. The witness is also checked by direct enumeration of all \(16\) independent-loss outcomes at \(19\) exact rational probabilities. Separately, exhaustive iteration over labeled matrices found \(1,79,2161,41503\) nonisolated matrices for plant counts \(1,2,3,4\), respectively, and no sign reversal.

The unrestricted three-pollinator assertion is analytic. The small-network certificate is complete **only** for four pollinators and at most four plants. The checker does not establish any ecological causal identification, nor does it independently audit novelty. Originality comparisons and model limitations are in the scientific review.
