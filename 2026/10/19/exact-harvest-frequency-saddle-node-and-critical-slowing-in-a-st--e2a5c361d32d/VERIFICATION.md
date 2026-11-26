---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For q≤a every first image is at most a, and the only fixed point there is zero, including the boundary q=a. For q>a every positive fixed point requires a<x<q; its flight time is H(x)=∫_x^{x/q} dz/f(z). H diverges at both endpoints. Writing f(x)=xg(x) with g(z)=r(1−z)(z−a), the sign of H′ is the sign of g(x)−g(x/q), equivalently x+x/q−1−a. The unique minimum is therefore x*=q(1+a)/(1+q), and partial fractions at the two endpoints give the displayed positive logarithmic cutoff. The sign of the map displacement on (a,q) is the sign of T−H(x); off that interval the displacement is negative except at zero. The increasing map preserves each side of any fixed point, so this sign pattern proves the full basins, including x_0=0 and x_0=1, and excludes nontrivial cycles. At the fold, q f(y*)/f(x*)=1 and ∂_T P_T(x*)=q f(y*)>0. Differentiating the first-variation formula once gives P″=(f′(y*)−f′(x*))/f(x*)<0, with the stated rational coefficient −2/P″. Taylor expansion and telescoping reciprocals of the positive forward-iterate deviations give the n(x_n−x*) limit. A fresh ODE integration at (a,q,r)=(0.37,0.78,1.3) gave the claimed tangency and critical scale (finite-difference estimate 0.476473858 versus formula 0.476473842).

## originality

PASS

The distinct claim supported by the inspected evidence is the exact cutoff, global basin classification, and explicit critical amplitude for the specified cubic flow with fixed periodic multiplicative removals. Strong-Allee bistability, fold mechanisms, flight-time methods and the generic parabolic 1/n rate are not claimed as original.

## value

PASS

For pulse removals under depensation it matters whether any positive stock can persist at a given retention and recovery interval. The closed interval cutoff and the all-stock basins answer that question without time-stepping or fitting, and the exact one-sided rate distinguishes slow critical persistence from ordinary attraction. The amplitude and global cutoff supply predictive information beyond the generic observation that saddle nodes occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
