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

# Verification notes

The analytic proof expands the Gaussian quadratic-form generating function through degree four, divides by the eighth radial moment, and applies the exact matrix identity \(\|A^2\|_F^2+\operatorname{tr}[(AA^*)^2]=2\operatorname{tr}(B^2+C^2)^2\). The difference from the claimed sharp squared-moment coefficient is the sum of three Frobenius-square terms given in RESULT.md. Nonzero equality requires \(A^2=0\) and \(B^2+C^2=(t/n)I_n\), which yield two anticommuting real symmetric involutions. An elementary eigenspace argument forces even dimension and an explicit orthogonal canonical form realizes equality.

Run `python3 verify.py` using Python 3 without external dependencies. The standalone implementation expands complex polynomial coefficients as pairs of arbitrary-precision integers, integrates each monomial using exact even spherical moments, and compares with the matrix-trace formula. It also computes both forms of the deficit with rational fractions. A recorded run returned:

```
PASS: 84 complete exact polynomial-moment/deficit comparisons
PASS: Clifford equality matrices in dimensions 2, 4, 6, 8
```

These finite tests are corroborative and do not certify the quantified theorem. No external independent scientific audit has been performed. The sharp odd-dimensional coefficient, other degrees, and nonuniform measures are not resolved.
