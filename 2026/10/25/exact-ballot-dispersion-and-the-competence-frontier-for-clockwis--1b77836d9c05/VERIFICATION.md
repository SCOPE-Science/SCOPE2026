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
# Reproduction and verification

The standard-library-only `verify.py` runs from the same directory as this document, using `python3 verify.py`. It enumerates every action configuration on each ring for \(n=2,\ldots,9\), enumerates every correct/incorrect caster-signal assignment, forms the exact rational distribution of the total correct represented weight, and independently obtains it using ordered cyclic gap compositions. It also compares the exact rational sum of squared guru weights with the closed formula.

**Observed output:**

```
PASS: 24 complete rational joint-action-and-signal enumeration instances, n=2..9
n=2, q=1/2, E[sum weights squared]=5/2
n=3, q=1/2, E[sum weights squared]=45/8
n=5, q=1/2, E[sum weights squared]=415/32
n=8, q=1/2, E[sum weights squared]=749/32
```

Test parameter pairs are \((q,p)=(1/2,1/2)\), \((2/5,3/5)\), and \((3/4,5/7)\). The reciprocal two-node directed case is checked as a boundary even though the main result is stated for \(n\ge3\).

**Proved, not numerically certified:** The all-\(n\) finite formulas follow from marked cyclic compositions and pair events. The limiting Gaussian truth-tracking laws follow from a longest-run bound, finite-range concentration of truncated square weights, and a conditional triangular-array central limit theorem; exact finite enumeration cannot certify these infinite statements. No external or independent audit has been performed.
