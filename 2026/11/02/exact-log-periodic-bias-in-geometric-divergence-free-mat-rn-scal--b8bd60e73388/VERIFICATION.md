---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. In d=2,3 for every real q>1 and r>0, differentiating the given radial Matérn profile yields S_d(t)=2(d-1)[d-(d+dt-t^2)e^-t], derivative 2(d-1)t(d+2-t)e^-t. Boundedness at infinity and O(t^2) near zero justify the two-sided increment sum and both truncation tails; index shift proves T(qr)=q^{2/3}T(r). Integrating the Mellin transform by parts in 0<Re(s)<2 gives 2(d-1)(d+s)Gamma(2-s)/s; Poisson periodization with s=2/3+2pi ik/log(q) gives all c_k. Gamma zero-freeness and Re(d+s)>0 show no harmonics vanish; vertical-line Stirling and first-harmonic dominance show sharp relative minimax error with exact prefactor 4 sqrt(2pi)/[(3d+2)Gamma(4/3)] times (2pi/log q)^{5/6} exp[-pi^2/log q]. Distinguishes convergent increment series from divergent zero-lag covariance amplitude.

## originality

PASS

PASS (best-of-knowledge, with specified residual risks). A Poisson/Mellin periodization of a radial structure function, a discrete-scale-invariant power-law correction and a lattice of complex Mellin poles all express the same normalized periodic profile. Sornette covers the framework, but the evaluated Matérn transform and all-q nonzero coefficients are specific computations not shown there. General log-periodic scale-mixture/Mellin theorems may permit mechanical evaluation once the exact radial trace is supplied. The source kernel paper treats finite physical mixtures, not the infinite ideal increment series; the proof separates these. Broader specialized analytical evaluation remains a priority risk. Existence of log-periodicity alone does not imply sharp exponent 5/6 and prefactor, nonvanishing for every q, nor both finite-grid tails. The published physical kernel by itself yields the setup, not the final arithmetic bias without this analysis.

## value

PASS

PASS. For a motivated physically used multiscale incompressible-flow Gaussian prior, the exact unavoidable log-periodic discretization bias, best constant fit and quantified finite-grid correction are meaningful kernel-accuracy facts. They tell a numerical researcher when a measured r^{2/3} slope is merely a dense-grid approximation and give a sharp coefficient and exponential error scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
