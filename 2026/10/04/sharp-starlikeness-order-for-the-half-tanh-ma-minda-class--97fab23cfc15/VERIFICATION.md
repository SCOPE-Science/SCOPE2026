---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The identity \(\operatorname{Re}\tanh(x+iy)=\sinh(2x)/(\cosh(2x)+\cos(2y))\) reduces the positive maximum over the unit disk to the first-quadrant boundary arc because, for fixed \(x\ge0\), the denominator decreases with \(|y|\). Differentiation gives \(F'(t)=2G(t)/D(t)^2\) with positive \(D\). The actual verifier's sign certificate was independently checked: the derivative formula simplifies exactly, crude analytic bounds give the stated global Lipschitz constants for the certificate, and high-precision root solving reproduced \(t_*=1.007214594072238336\ldots\) and \(\alpha=0.574270065606231212\ldots\). Odd symmetry gives the minimum; subordination transfers the half-plane bound; the canonical integral extremal satisfies the defining differential equation and approaches equality.

## originality

PASS

The 2026 defining paper studies coefficients, Fekete--Szegő/Zalcman/Hankel functionals, logarithmic/inverse coefficients, and majorization rather than this supporting half-plane. Earlier full-tanh papers study convolution/determinants/Bernardi inclusions and radius/disk-containment questions. In particular, the 2021 paper gives disks centered in the image and sufficient radius estimates; those do not determine the actual left supporting line, whose extremizer occurs at a nonreal boundary point. Fresh Resultary and exact formula searches found no earlier statement of this order.

## value

PASS

The classical starlikeness order is a canonical global geometric invariant of a newly defined Ma--Minda class. The result gives the exact sharp supporting half-plane, not a coefficient estimate or coarse disk containment, and comes with a canonical extremal realizing sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
