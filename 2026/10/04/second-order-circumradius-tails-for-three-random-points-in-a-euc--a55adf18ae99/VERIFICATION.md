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

The analytic proof is self-contained once the exact circumradius/ball-segment identity and half-distance moment formula from arXiv:2608.29975v1 are taken as premises.

`artifacts/verify.py` performs the following reproducibility checks:

1. It evaluates the rational formula for \(a_d\) and verifies \(a_2=1/7\) and \(a_3=144/455\).
2. It verifies \(C_3a_3=432/25025\) using \(C_3=3/55\).
3. It verifies the three-dimensional extreme-value coefficient
\[
\frac{a_3}{C_3}+\frac12=\frac{1147}{182}.
\]
4. It numerically evaluates the exact ball-segment cross-section integral for \(d=2,3,4\) and checks that, after subtracting the second-order approximation, the relative residual scales as \(R^{-4}\).

The numerical integral is a finite consistency check, not a proof of the asymptotic statement. The proof of the universal fixed-\(d\) expansion is the uniform Taylor expansion and exact beta-integral computation given in `RESULT.md`.

Scientific limits: no uniformity in \(d\), no statement for more than three defining random points, and no statement for non-ball sampling domains.
