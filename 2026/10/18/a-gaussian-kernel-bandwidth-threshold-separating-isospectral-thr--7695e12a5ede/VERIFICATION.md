---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Both kernels are Π plus half an orthogonal rank-one projection onto a unit zero-sum mode (adjacent difference u or endpoint difference w); positivity, uniform stationarity, spectrum, gap and half the maximum row ℓ¹ distance follow. The Gaussian Gram kernel is strictly positive definite (its Fourier density is everywhere positive and the trigonometric polynomial of a nonzero coefficient vector is not identically zero). Every zero-mass direction is realized by a sufficiently small probability perturbation of π, so the computed gain is sharp over probability laws. Independently, the zero-mass reflection basis w,(1,−2,1)/√6 yields diagonal metric entries λ₁=1−t⁴, λ₂=(1−t)²(t²+2t+3)/3. The endpoint projection is metric-orthogonal. The adjacent mode has squared basis coordinates 1/4 and 3/4; by Cauchy–Schwarz in the metric, its gain squared is ((λ₁+3λ₂)/4)((1/λ₁+3/λ₂)/4)/4, which simplifies to the claimed 1/[4(1−R)]. For A=t+t²+t³, R=A²/(3+2A), strictly increasing from 0 to 1. R=3/4 gives the polynomial and unique transition with the stated direction. From λ₁∼4h and λ₂∼2h² the sharp adjacent gain squared is asymptotic to 3/(32h). On two states the zero-mass subspace is one-dimensional, so kernel choice cannot change the ratio at fixed eigenvalue. h=0 is excluded and no indefinite trajectory growth is implied.

## originality

PASS

Bounded pass for the explicit isospectral three-state Gaussian-kernel comparison with its sharp bandwidth threshold and broad-kernel coefficient. Failure of contraction despite a spectral gap and the conjugated-operator-norm principle are known, not credited as original here.

## value

PASS

A minimal-state sharp witness clarifies a practical distinction between TV and MMD one-step behavior: keep the eigenvalues, reversibility, positivity and TV behavior fixed while switching the active site difference relative to the kernel geometry. The exact threshold decides whether any probability law is amplified, and the singular constant quantifies the maximal effect rather than merely showing noncontractivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
