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

# Reproducibility and verification

Run `python verify.py` using Python 3.9 or later; it requires no nonstandard packages. The source uses exact rational Laurent-polynomial expansion, independent chord and barycentric convex-hull tests, numerical Simpson integrations as supplementary consistency checks, and a rational tail bound for the positive series for \(\log3\). It checks the expected exact values at sample counts \(2,3,4,5,6\), the rounded values for counts \(10,11\), and the sharp \(95\%\) threshold.

Observed successful output:

```
PASS: 5 exact formula identities, 16 independent Simpson integrations,
      16 finite-sample monotonicity/range checks, exact 95% cutoff,
      and 4500 exact-rational geometric comparisons.
p_10= 0.9411269334147931 p_11= 0.9603356140490007
```

The exact finite-sample comparisons and rational certificate can be rerun. The independent geometric comparisons are a finite test and do not establish the theorem for all real node choices; the proof of the hull criterion and continuous-density integration is in `RESULT.md`. The asymptotic \(3(2/3)^m\) is analytically justified by endpoint Laplace estimates, not by finite numerical extrapolation. No independent mathematical audit has been performed.
