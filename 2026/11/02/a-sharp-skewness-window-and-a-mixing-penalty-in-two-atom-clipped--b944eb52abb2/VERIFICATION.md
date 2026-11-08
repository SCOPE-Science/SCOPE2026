---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS — For independent ξ=+qS (probability p) or −pS (probability q), η=1 and cap S/N, the exact shifted recursion in z=x+qS is z↦max(z−S/N,0) or min(z+S/N,S). From any deterministic real start it reaches the invariant [0,S] in finitely many steps; any N consecutive plus samples subsequently hit zero almost surely, yielding finite lattice absorption. Detailed balance gives π_j∝(q/p)^j and the boundary-inclusive tridiagonal characteristic polynomial (λ−1)(√pq)^N U_N(λ/(2√pq)). Weighted Riemann sums for p=1/2+θ/N prove tilted-uniform law and N²-gap limit π²/2+2θ². For p=q=1/2, checked the explicitly claimed cubic Poisson solution at BOTH reflecting boundaries for N=1,…,8 with exact rational arithmetic; it yields τ_int=(2N²+4N−1)/5 and sample-average variance S²(N+2)(2N²+4N−1)/(60N). Finite numerical checks are supporting only; the arguments prove all N and θ in stated restricted model.

## originality

PASS

PASS, qualified — Abstract reflected birth–death chains already have geometric π and Chebyshev eigenvalues; classical Poisson equations give autocorrelation once P is known. Koloskova–Hendrikx–Stich's gradient-clipping paper studies stochastic bias and convergence bounds but not this exact commensurate two-atom fixed-step invariant spectrum or critical skewness scaling in inspected material. A related published SCOPE signSGD Ehrenfest result has a different transition kernel and invariant law. Novelty is the nonlinear optimizer-to-reflecting-walk reduction and critical window/mixing tradeoff as a combined exact benchmark, not elementary random-walk formulas independently.

## value

PASS

PASS — A natural explicitly solvable clipping benchmark reveals that stronger clipping reduces single-step stationary variance while greatly increasing the variance cost of time averages, with an exact skewness width 1/N. The metric is motivated by bias/mixing in stochastic optimization rather than arbitrary finite algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
