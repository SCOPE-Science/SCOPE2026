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

The analytical proof is contained in `RESULT.md`. The standalone `verify.py` uses only Python standard-library rational arithmetic, so it avoids floating-point sensitivity in the exact identities.

Run:

```text
python verify.py
```

Expected output:

```text
VERIFY_OK: exact rational pair variances; 18 quadratic finite-m identities; 9 cubic asymptotic checks; sharp factors 8 and 16
```

Checked identities include the three exact quadratic local variances \(1/2880\), \(1/360\) and \(1/180\); the corresponding exact total variances for mesh sizes \(1,2,3,5,8,17\); and the asymptotic curvature integral \(\int_0^1(2+6x)^2\,dx=28\) for the cubic example. The script does not enumerate the infinitely many copulas or all \(C^2\) functions: the explicit Fréchet–Hoeffding argument and the uniform interpolation remainder provide that proof.

No independent scientific audit has been performed.
