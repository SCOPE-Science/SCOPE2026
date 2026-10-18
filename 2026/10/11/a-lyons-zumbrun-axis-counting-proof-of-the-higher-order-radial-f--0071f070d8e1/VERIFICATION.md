---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. Rebuilt the all-order tensor calculation from the Lyons–Zumbrun homogeneous derivative identity. Orthogonal covariance permits evaluation at re_1. Every odd transverse derivative vanishes; even exponents (a,2m_2,...,2m_d), sum m_j=q, contribute product (2m_j-1)!! times (D^qg)^(a). Ordered indices contribute n!/alpha!, and the central-binomial generating function [z^q](1-z)^(-(d-1)/2) gives exactly binom(n,2q)(2q-1)!! product_{k<q}(d-1+2k). Verified the coefficient identity independently with exact Fraction arithmetic for dimensions 2,3,5,8 and orders n=1..8; finite checks are merely corroborative. Smooth radiality extends the formula through r=0.

## originality

PASS

PASS best of knowledge with material-access limitation. The Mihula–Vybíral paper already proves the same Frobenius FORMULA; originality here is the different Lyons–Zumbrun-based proof of their expressly posed first method question, not the result formula itself. The 1994 componentwise identity and Ostermann’s radial Sobolev work do not, as located, sum exact squared tensor weights using axis parity and a Pochhammer convolution. Full focal PDF could not be independently obtained: the open abstract/index and source proof were read, and the uncertainty is retained.

## value

PASS

PASS. An explicitly stated open proof-method question is a mathematically motivated gap. The direct multi-index axis classification plus a closed generating-function evaluation explains coefficients and bypasses the focal paper’s induction; it is useful as an alternate structural derivation, without claiming a new Frobenius formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
