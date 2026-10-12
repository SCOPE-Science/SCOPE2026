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

The exact domain is the uniform coupon collector with \(m\ge2\) types and the first-completion stopping time \(T_m\). The accepted transform concerns multiplicities \(r\ge2\).

The critical proof certificate is the exact coefficient identity
\[
\mathbb E\!\left[K_{m,r}\mathbf 1\{T_m=t\}\right]
=
\frac{m!}{m^t}\binom{t-1}{r}S(t-1-r,m-2),
\]
which follows from a marked successful-sequence count. Summation with the ordinary Stirling-number generating function gives the transform.

`checker.py` exhaustively enumerates small coupon sequences and verifies this coefficient identity directly. It then checks the doubleton mean, covariance, harmonic increment, and negativity claims by exact rational arithmetic through a large finite range.

The exhaustive checks are supplementary. The universal transform and covariance formula are supplied by the symbolic proof. The result does not claim the singleton joint law, nonuniform coupon probabilities, or a full multivariate stopped-spectrum transform.
