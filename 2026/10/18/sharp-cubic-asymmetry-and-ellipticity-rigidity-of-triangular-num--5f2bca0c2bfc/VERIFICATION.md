---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For complex 1<p<infinity triangular T=(a b;0 d), the norming functional makes W_p the union of circles centered at d+(a-d)t with radius B t^alpha(1-t)^beta, alpha=(p-1)/p and beta=1/p. Intermediate-value argument shows every filled disk occurs; strict concavity f''=-alpha beta f/[t²(1-t)²] makes the union convex. Its support G(c)=max_t(ct+Bf(t)) is analytic with G''>0 and radius of curvature h+h''=Bf(t(c))+L²sin²(theta)/(-Bf''(t(c)))>0. Implicit differentiation gives G'''(0)=2alpha beta(beta-alpha)/(B²F²), nonzero iff p≠2. Reflection symmetry confines any center to real axis; central symmetry would force G(c)-G(-c) linear, contradicting the nonzero cubic. p=2 gives the classical ellipse, L=0 a disk and B=0 a segment. For small L/B the odd support term cubic, and Chebyshev best uniform x³ vs z x is (3/4)x with error 1/4, yielding Hausdorff symmetry defect |alpha beta(beta-alpha)| L³/(6F² B²)+O_p(L⁵/B⁴). Symbolically checked p=4: G'''=-1/sqrt3 and defect coefficient 1/(12sqrt3). This is an analytic proof for all fixed 1<p<infinity; a numerical example alone would not establish it.

## originality

PASS

Mandal–Bhanja–Bag–Paul Corollary 2.6.1 already proves triangular numerical-range convexity, and their Theorem 2.7 supplies a boundary envelope. Müller–Tomilov Proposition 2.8 separately proves star-shapedness and a circle parametrization, not the cubic central-symmetry obstruction, everywhere-positive curvature, or sharp small-gap Hausdorff coefficient. Both full texts were materially inspected (arXiv PDF and author-posted full text). The submitted novelty is these geometric refinements, not the known union-of-circles description or mere convexity.

## value

PASS

It classifies exactly when the classical elliptic-range phenomenon survives in a non-Hilbert complex coordinate plane and gives the first nontrivial sharp quantitative distortion as diagonal entries separate. Positive curvature and the cubic defect provide reusable boundary asymptotics beyond a routine linear-algebra identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
