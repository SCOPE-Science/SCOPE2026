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

The Löwner condition for K=cond(DAD), with Z=λ_min(DAD)D^{-2}, is Z≤A≤KZ. Averaging Z over permutations of the last n−1 coordinates preserves feasibility and yields an exchangeable diagonal optimum without presuming symmetry. The reduced 2x2 block B(x) has one other eigenvalue 1 with multiplicity n−2. det(B−I)=t(n−1)b²(x²−1) determines the min eigenvalue order; the 2x2 eigenratio is minimized by Px+Q/x on 0<x<=1, and λ_max grows on x>=1. Hence the closed minimizer and phase threshold. Independently checked 600 nonsymmetric scaling trials over five parameter configurations and exact n=5 Jacobi eigenvalues; numerical checks support but do not prove global optimality, which follows analytically.

## originality

PASS

General exact global diagonal scaling formulations and convex algorithms exist, but inspected primary texts do not state this rank-one all-dimensions mass localization transition or harmful Jacobi example. Shapiro 1985 explicitly advertises some closed-form special cases; its full paper was inaccessible through authorized institutional access, so an equivalent older case remains a genuine priority risk rather than a fabricated negative comparison.

## value

PASS

Exact diagonal congruence scaling of a canonical spiked covariance/precision model is a natural preconditioner benchmark. The theorem identifies the sharp mass-imbalance boundary for any possible scaling and a concrete case where a standard heuristic is strictly harmful, so the closed-form fact is a motivated operator-optimization result rather than just a numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
