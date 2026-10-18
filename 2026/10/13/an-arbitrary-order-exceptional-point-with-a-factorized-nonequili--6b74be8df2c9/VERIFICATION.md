---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The displayed 2x2 seed a=(1/2)[[1,1],[-1,-1]] obeys a²=0 and a≠0. Its sum over the m=N−1 symmetric tensor factors yields exactly the displayed tridiagonal L, L^N=0 and L^{N−1}e_m≠0; so B=−kI+δL has one size-N Jordan block at −k. The diagonal K_rr=k−δ(m/2−r) is positive iff k>δm/2 and B+B^T=−2K; uniqueness of the stable covariance I follows from the Lyapunov equation. Current J=δSxφ is nonzero, divergence-free; Gaussian trace gives the displayed positive sum of squared bond currents. The propagated terminal mean is the m-fold tensor power of (δt/2,1−δt/2), yielding exactly KL=½e^(−2kt)[(δt/2)²+(1−δt/2)²]^m; derivative −µ^T Kµ<0 proves strict monotonic decay. The inspected exact symbolic checker tests N=2,...,8 only as corroboration.

## originality

PASS

The SU(2)/symmetric-tensor higher-order EP mechanism, Lyapunov Gaussian stationarity, and Jordan polynomial relaxation were previously known individually. Here the novel joint statement is their all-N simultaneous realization in an explicit positive heterogeneous OU bath with irreversible currents plus full closed KL and entropy-production laws. Comparing same-model parameters, Pal–Gupta exhibit the all-order EP and the Gaussian pseudo-equilibrium in different regimes, not simultaneously in this tuned family.

## value

PASS

A concrete all-N stable stochastic dynamics exhibiting a maximal-order EP together with independent equilibrium coordinates but nonzero stationary circulation is a structural compatibility result. It makes a motivated nonnormality/irreversibility distinction precise and computes nontrivial entropy-production and all-time relaxation observables, exceeding an arbitrary normal-form substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
