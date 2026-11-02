---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Let B=K+L0 be positive definite, b an incidence column, z0=B^{-1}Ks, h=B^{-1}b, q=b^Tz0, r=b^Th>0, a=z0^TL0h, c=h^TKh>0. Sherman–Morrison gives z(t)=z0-q[t/(1+rt)]h. Since h^TL0h=r-c, expanding z(t)^T(L0+tbb^T)z(t) proves D(t)=D(0)+(q²-2qa)λ-q²cλ² exactly. λ is strictly increasing for t≥0, giving an endpoint minimizer in each coordinate, with an interior stationary point necessarily a strict maximum if q≠0, or flat when q=0. A compact-box global minimum exists; sequentially moving individual coordinates to endpoints without increasing D produces an all-corner minimum. No connectivity assumption is needed because K is positive definite. Exact-rational independent checker verified 120 rank-one formula/endpoint cases and the nonuniform mixed optimum at (1/4,3), D=16/169, for the reported three-node path.

## originality

PASS

The rank-one update itself and FJ energy model are well-known; the claim is the global corner result for the pure equilibrium-recomputed disagreement functional under independently bounded tie weights. The complete accessible Chitra–Musco paper explicitly alternates equilibrium recomputation with an administrator step minimizing disagreement at FIXED previous-round opinions, with degree and Frobenius restrictions; it is not a global minimization of w↦D(z(w),w). Yi–Patterson Theorem 5.9 supplies convexity of a weighted polarization-plus-disagreement objective, not concavity of the pure disagreement response; Musco et al. likewise optimize their combined index. Rácz–Rigobon optimize polarization. No inspected statement or implication proves the all-box-corners theorem. Earlier unexamined general spectral-energy optimization results remain a priority risk.

## value

PASS

This is a structural, globally quantified reduction from a continuous multi-edge design problem to endpoint configurations, with a counterintuitive one-peak (never one-trough) response and an attained mixed corner even when lower bounds are strictly positive. It delineates a useful mathematical boundary between pure equilibrium edge disagreement and the convex combined objectives of earlier social-network optimization. Exponential corner search remains necessary; no polynomial-time algorithm is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
