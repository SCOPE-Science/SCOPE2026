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

# Verification of the Euclidean-distance Bergman-ball zero classification

The analytic check starts with the unnormalized surface-area constant, exact beta moments and complete monomial basis in \(\mathbb B^d\). The hypergeometric coefficient ratio has been reconstructed independently, including Euler's exponent \(-d-t-1\) and the two upper parameters \(-m\) and \(-q-1/2\). Pfaff's formula gives Jacobi exponents \(d-1/2\) and \(\pm1/2\), both strictly greater than \(-1\); the resulting negative scalar roots are exhaustive and simple. The sign-variation count is exact because the shifted polynomial is real-rooted and the zero at \(s=-1\), if present, is discarded before Descartes is applied.

`check_ball_kernel.py` is self-contained and uses Python standard-library exact fractions. Running `python3 check_ball_kernel.py` returned:

`PASS: 5776 exact independent moment/closed-form coefficient identities; sample zero counts and numerator normalizations verified.`

The checker ranges over \(1\le d\le16\), \(0\le t\le18\), and \(0\le k\le18\), and separately checks the three displayed examples. These tests are finite checks of implementation and normalization, **not** a certificate for all unbounded integer pairs, and they are not independent validation. The universal assertion is supported by the complete symbolic proof. Related literature may contain equivalent results beyond the inspected sources. Independent audit has not been performed.
