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

The scientific statements are proved analytically in `RESULT.md`. The included Python 3 standard-library script `certify_sensitivity.py` checks all required signs using only exact `fractions.Fraction` arithmetic; decimal floats appear solely in **displaying** its enclosures.

Run four commands in the directory containing the script:

```
python certify_sensitivity.py 7
python certify_sensitivity.py 8
python certify_sensitivity.py 9
python certify_sensitivity.py 10
```

Every invocation terminates with `EXACT-RATIONAL SIGN CERTIFICATE PASS`, and reproduces the appropriate `certified_intervals_*.json` report. Verification directly establishes the exact signs of the local mean slope, local absolute variance slope, and squared coefficient-of-variation slope for precisely the four stated integer team sizes. It does not compute any global optimal rate, and cannot support claims about other team sizes.

The interval algorithm bounds the monotone complementary-error-function quotient on a rational mesh, uses alternating Taylor bounds for the exponential kernel, bounds the normalization constant using a Machin arctangent identity, and encloses the improper integral tail algebraically. Errors from rounding reported decimal numbers never enter the proof.

Independent validation has not been performed.
