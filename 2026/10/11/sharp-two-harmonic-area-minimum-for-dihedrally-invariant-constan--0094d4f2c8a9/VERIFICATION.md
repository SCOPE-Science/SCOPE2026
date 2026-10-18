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

Odd dihedral symmetry and constant width force h=w/2+a cos(n theta)+b cos(3n theta). The support-function convexity condition h+h''>=0 becomes ||alpha cos t+beta cos3t||_infty<=1, and the support area formula gives A=pi w^2/4 -pi w^2(alpha^2+r_n beta^2)/[8(n^2-1)]. Quadrants beta>=0 or alpha=0 give objective <=1; for beta/alpha=-s<0 the cubic Chebyshev norm has m(s)=1-s for s<=1/9 and m(s)^2=(1+3s)^3/(27s) thereafter. Direct symbolic differentiation confirms F'(s)=27(1-6s+3r_n s^2)/(1+3s)^4. The sole global maximizing ratio s_n=1/[3(1+sqrt(1-r_n/3))], where F_n>4/3, fixes exactly two opposite coefficients. They give convex bodies with exactly 2n zero-curvature normal directions; n=3 numerical check yields F_3=1.337068308... . The proof holds for all odd n>=3 and w>0; finite checks are not used for the continuum.

## originality

PASS

No retrieved theorem yields the two-mode fixed-dihedral area optimum. The stronger unrestricted Reuleaux minimum has a different (non-polynomial) equality class and is not attained under the spectral cutoff.

## value

PASS

The exact two admissible Fourier harmonics are the first meaningful spectral refinement beyond a one-harmonic dihedral constant-width class. A sharp area minimum with two explicit extremizers, finite-band gain factor, and curvature-contact geometry solves a natural variational cutoff rather than an arbitrary parameter slice; its strict >4/3 gain is quantitatively meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
