---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The correct state reduction follows from the actual Algorithm 2: initial x=z=e1 on diagonal Hessian means only first coordinate can move; with theta=t/d the two 2x2 conditional updates K0 and K1 in RESULT.md follow directly. Their exact second-moment action S(K) on (E[a²],E[ab],E[b²]) gives M_d(t)=((d-1)S(K0)+S(K1))/d, w0=(1,1,1), and E f_kappa(x_j)=kappa(M^j w0)_1/2. I independently differentiated these rational matrices symbolically for d=2,3,5 and verified coefficient-by-coefficient N1 and N2 as printed, including the lower-left coefficient (d-1)/d². The Jordan chain 1->2->3->1 has leading product 2(d-1)t^4/d^4, forcing the three distinct Puiseux roots with shifts C_d*zeta*t^(4/3); the real root has strictly largest modulus for small positive t. The displayed positive left/right eigenvector leading components and h.v->3 exclude cancellation by w0/e1, so the fixed-kappa successive expected-objective ratio tends to that dominant root. Numerical eigensolutions for d=2,3,5, t=0.001 agreed with 1-2t/d+C_dt^(4/3). Fixed d and asymptotic k->infinity preceding kappa->0 are essential; finite checks alone would not prove either asymptotic.

## originality

PASS

The source method's theorem supplies a general (1-theta)^j expected-objective guarantee, not the exact observable spectral radius nor its nonanalytic positive kappa^(2/3) correction. A real second-moment covariance Jordan cycle is needed; the first-moment 2x2 recursion alone lacks it. The primary Algorithm 2 and strongly convex rate theorem and generic accelerated coordinate descent literature were compared at the level of update matrices and conclusion. No directly dominating exact-covariance formula was found in Resultary/topical literature, subject to possible differently indexed specialized random-matrix asymptotics.

## value

PASS

The exact stationary asymptotic rate of a prescribed published acceleration algorithm is a natural convergence invariant, distinct from its worst-case certified bound. Identifying a fractional-power correction and mechanism changes low-curvature prediction quantitatively, is not a routine substitution in the published complexity estimate, and may guide covariance-sensitive parameter analysis. The tight statement is deliberately only for fixed dimensions, a diagonal quadratic and one-coordinate initialization; no global acceleration or finite-precision guarantee is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
