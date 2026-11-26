---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For unit conductances, the constants, hub contrast, zero-total petal averages, and within-petal zero-sum spaces give eigenvalues 0,n,1,k+1. The dimension sum is n; repeated petal sizes simply give additional orthogonal summands at the same eigenvalue. The [2/2] multiplier r(z)=1−12z/d(z) is in (0,1] for z>=0 because its numerator is (z−3)^2+3 and its denominator is positive. It follows that all diagonals are positive and the constant mode gives norm exactly 1. The hub entry is 12h/d(nh), and the cross-petal entry is 12h²((n+1)h+6)/(d(h)d(nh)). For a within-petal pair the projector correction is (r(h)−r((k+1)h))/k; clearing denominators after factoring 12h gives h((n+1)h+6)d((k+1)h)+(12−(k+1)h²)d(nh), exactly the stated P_(n,k). Writing n=k+2+j, j>=0, makes its leading coefficient −(k+1)(1+j(k+3)+j²), with all other coefficients positive. Thus P/h⁴ strictly decreases on h>0 from +infinity to a negative limit; this gives one crossing, the closed threshold, and no reentry. Singleton petals have no such off-diagonal entries; h=0 gives the identity, not strict off-diagonal positivity. I independently checked both signs of all four example root brackets with exact scaled quartic arithmetic (replay: branches/review-exact-small-checks.js). The supplied verifier was inspected, not executed; the inequalities for all sizes and real h follow analytically.

## originality

PASS

Matched and credit the exact equal-petal classification, the generic projectors and spectral entry identities, and prior unconditional star positivity as coverage. The supported distinct claim is the sharp sign problem for the nonconvex Gauss multiplier with unequal petals, including the competition of different within-petal thresholds. The closest equal-size and convex-filter statements do not themselves establish this extension; catalogue dates are not used to adjudicate priority.

## value

PASS

This is a sharp, all-step entry-sign classification for an implicit high-order diffusion integrator on a natural heterogeneous graph family. The exact thresholds distinguish stochastic positivity from spectral contraction and show why, even among cliques glued at one hub, neither the largest nor the smallest petal need control the admissible step. These are useful distinctions absent from an equal-petal or uniform sufficient bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
