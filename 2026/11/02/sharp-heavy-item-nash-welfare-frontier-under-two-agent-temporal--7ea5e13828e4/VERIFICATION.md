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

The analytic certificate is the three-step inequality chain for the dominant-good region:

\[
P^*\le h(V-h),\quad xy\ge\frac{(V-h)(V+h)}4,\quad
\frac{xy}{P^*}\ge\frac{V+h}{4h}.
\]

For the witness sequence \((q,q,h)\), \(q=(V-h)/2>0\), first-two-prefix EF1 forces the two small goods to be split and final EF1 holds regardless of which agent receives the last good. The exact offline product is \(2qh\), while every feasible temporal final product is \(q(q+h)\).

The code file `verify.py` is self-contained and uses only Python's standard library. In a fresh extraction, `python3 verify.py` returned:

```
PASS instances=21840, final_EF1_allocations=1040454, heavy_branch_checks=470, prefix_EF1_allocations=254528, sharp_three_item_examples=199
```

The finite checks cover integer values \(1,2,3,4\), lengths \(2\) through \(7\), and 199 explicit heavy-family examples; they are not an exhaustive computation over arbitrary real values or arbitrary horizons. Those infinite assertions rely on the explicit proof in RESULT.md. No independent audit has been performed.
