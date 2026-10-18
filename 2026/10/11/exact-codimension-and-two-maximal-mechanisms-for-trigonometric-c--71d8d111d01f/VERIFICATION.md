---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For nonconstant trigonometric factor of degree d, a nonzero P(h)h′ has leading Laurent frequency (degP+1)d, ruling out cancellation and bounding outer degree. Normalize two affine freedoms of h: parameter dimension 2d−1, outer pair 2floor(n/d), so Dd=2d+2floor(n/d)−1. For 2≤d≤n−1, d+floor(n/d)≤n gives Dd≤2n−1. Degree d=n gives rank-one proportional L_n of dim2n+1; d=1 gives common odd-axis R_n of dim2n+1 via Chebyshev sin(ks)=sin(s)U_(k−1)(cos s). Distinct closed semialgebraic branches for n≥2; intersect in proportional odd polynomials, generic n sine coefficients + phase + scalar = n+2. No intermediate d can attain max dimension. At n=2 only d=1,2, hence C2=Ln ∪ Rn, and Fourier coefficient test handles zero first harmonics. Reviewed frozen CHECKER.py confirms sample phases/tangent directions and n≤200 inequality, but not infinite dimension proof.

## originality

PASS

Full 2013 Giné–Grau–Santallusia Appendix already supplies degree-two symmetric/separable/proportional composition-center classification, so n=2 two-branch result is NOT a new consequence; the surviving final contribution is all-n 2n+1 semialgebraic dimension/codimension, top-dimensional exhaustion and intersection dimension, which inspected 2013 and 2026 sources do not imply. Resultary failed; priority risk retained.

## value

PASS

An all-harmonic-cutoff semialgebraic dimension law and identification of precisely two maximal geometric mechanisms for a natural trigonometric composition locus addresses a structural center-family classification, quantitatively separating generic mechanisms from intermediate factor-degree strata. Meaningful independently of n2 prior special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
