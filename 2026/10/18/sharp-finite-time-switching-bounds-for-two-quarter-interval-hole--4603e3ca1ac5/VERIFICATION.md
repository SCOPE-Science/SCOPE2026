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

The standalone executable `checker.py` runs without dependencies beyond the Python standard library. Execute `python3 checker.py` in the same directory.

Observed results:

```
PASS: 511 independent direct-bit versus matrix comparisons, n<=8
PASS: all schedule extrema and uniqueness for n<=15
PASS: closed formulas up to n=100, and 2-step adjacency identity
```

The direct-bit test counts length-\(n+1\) binary words by checking each forbidden adjacency at each time, independent of the matrix recurrence. The matrix test checks all \(2^n\) switching words through \(n=15\), including equality classifications. The third test checks formulas at larger finite horizons and the exact product \(M_1M_0\).

**Logical scope.** These finite tests do not prove the claims for arbitrarily large horizons and do not establish novelty. The proof in `RESULT.md` is a separate induction for all horizons and a directed-graph argument for the infinite survivor set. No independent audit or external validation has been performed.
