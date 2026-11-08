---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fixed m0>=3, rates beta,lambda>0 and a walker jumping to any other vertex uniformly, the exact lumped process (A=N-1,D=X-1) has birth rate beta and discovery intensity lambda(A-D)/A. With alpha=lambda/(lambda+beta), R=D-alpha A has drift -lambda R/A. Its compensated birth/discovery martingales have limiting quadratic brackets beta t and a t, a=beta*lambda/(beta+lambda), and zero cross-variation. A second-moment estimate bounds R_t^2 by O(t); the cutoff epsilon argument justifies convergence to the stochastic entrance integral of s^k dW with k=lambda/beta, even at small positive k. Itô isometry gives covariance [[beta,beta*k^2/(1+k)^2],[same,beta*k*(k^2+1)/(1+k)^3]]. Checked exact algebra and frozen verify.py finite-step rational lumping/generator code. Independent simulation at t=300, beta=lambda=1, 4500 trials yielded approximate per-time variance/covariance (1.001,0.251,0.250), versus theoretical (1,0.25,0.25); simulation does not prove convergence.

## originality

PASS

Best-of-knowledge PASS for the Poisson-birth joint N_t-X_t Gaussian covariance. Demirci–Işlak–Yıldız establishes a CLT for visits with one vertex added at each integer time and Poisson walker steps, not independent Poisson arrivals, hence no fluctuating birth count to couple. Videla studies out-of-equilibrium growing-graph walks and remains a relevant unread full-text risk despite accessible abstract and an authorized retrieval blocked by disconnected VPN.

## value

PASS

The joint fluctuation law isolates extra randomness in the growth process and its negative/positive noise decomposition; exact birth/discovery covariance in the canonical complete-graph model is needed to distinguish random-growth from deterministic-growth benchmarks, beyond a routine marginal CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
