---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=3 with nonnegative independent edge conductances, fixed positive P,Q,B, the graph is connected at finite optimum and restricted Laplacian trace inverse is strictly convex in the edge weights since distinct edges give distinct off-diagonal entries. Uniqueness plus prism automorphisms forces common ring x_n>0 and rung y_n>0. Symmetric/antisymmetric Fourier modes give T=n(2P+Qt)/B*(a_n+sum_{k=0}^{n-1}1/(mu_k+2t)) and the stated unique scalar stationary equation. Exact cycle resolvent F_n(t)=n/(2sqrt(t(t+2)))*(1+rho(t)^n)/(1-rho(t)^n); testing t=s n^(-2/3), compactness upper/lower bounds on optimal s, uniform convergence yield minimizer s*=(18P^2/Q^2)^(1/3), t_n~s*n^(-2/3), T=(P/(6B))n^3+(Q*s/(4B))n^(7/3)+o(n^(7/3)). The n^5/3 rung scaling and equal-price 2/3 comparison follow. Independent full Laplacian traces n=3..7 and asymptotic n=200,400,800 checks corroborate, not replace proof.

## originality

PASS

PASS qualified: Ghosh–Boyd–Saberi established convex conductance design in general and solved trees/wheels/barbells, but not the prism two-class boundary-layer solution; Cinkir and Zhang–Yang fixed-edge resistance formulas do not optimize free conductances. The specialized 2017 prism full text was inaccessible, so priority remains qualified.

## value

PASS

A natural freely priced three-edge-class network optimization yields exact finite-n weights and a nontrivial fractional n^-2/3 rung-allocation boundary layer with next-order n^7/3 trace correction; this can inform resistance-design asymptotics and is not merely computing a known unweighted index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
