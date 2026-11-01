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

Regenerative renewal reward gives the exact joint diffusion occupation density p_t(y) psi(t+delta) dt dy ddelta and return density v^-1 psi(t) p_t(y+j) dt dy dj, before division by mean cycle duration m=s/r+[2sqrt(D/r)Gamma(s+1/2)]/[v sqrt(pi)Gamma(s)]. For y=x+u, the exponential action rt+(x+u+j)^2/(4Dt) has a unique minimum at t_x=x/(2sqrt(Dr)) with t_x-saddle variance scale h_x^2=t_x/(2r). Taylor expansion at t=t_x+h_x z gives kx+z^2/2+k(u+j), k=sqrt(r/D), while psi(t+delta)/psi(t)->e^{-r delta}. Uniform Gaussian concentration and the Gamma/exponential tails control integration outside compact z,u,j,delta sets for fixed s>0; this yields joint Gaussian and independent exponential limits. The diff/return weights are 1/(kr) and 1/(vk^2), giving v/(v+sqrt(Dr)). Integrating the Gamma-mixed Brownian endpoint tail and dividing by m verifies coefficient k^(s-1)/(2^s Gamma(s)m)*(1/r+1/(v k)) x^(s-1)e^{-kx}. Independent numerical integration of separate occupation kernels at x=180 for three parameter sets including s<1 and s>2 agreed with phase fractions and Gaussian duration means/variances; finite thresholds do not prove the limit.

## originality

PASS

Radice 2022 arXiv:2201.01829 establishes this exact Brownian Gamma-reset and finite-speed-return model, both stationary phase position densities and far spatial tail. The marginal tail constant and phase weight are already entailed and explicitly excluded from claimed originality. The surviving result is a JOINT extreme-position conditional limit: normal hidden diffusion duration together with independent exponential position overshoot and phase-specific forward time/return progress. Masó-Puigdellosas et al. arXiv:2205.01613 establish conditioned backward/forward times for resetting with instantaneous returns, an important close precursor; the inspected sections do not give the finite-speed two-phase Gamma joint saddle law. Novelty thus remains conditional on this precise full-joint specialization.

## value

PASS

The rare stationary spatial observation identifies the latent duration and mode in a natural two-phase regenerative diffusion. The joint normal/exponential conditional structure and its parameter-independent phase weight clarify a mechanistic inverse-inference question, beyond known stationary position marginals. Return travel and remaining alarm distributions have direct physical meaning; no paper-sized extension is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
