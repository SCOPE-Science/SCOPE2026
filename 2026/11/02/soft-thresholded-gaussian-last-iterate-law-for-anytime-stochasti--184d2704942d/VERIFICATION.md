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

For horizon n objective epsilon_n|x| with epsilon_n=theta b sqrt(H_n)/S_n, sign(0)=0, eta_t=gamma/sqrt(t), and iid bounded Rademacher noise (b-epsilon_n)xi_t, early normalized noise up to m_n=floor(n/(log n)^4) has CLT variance H_m/H_n->1 while early drift epsilon_n S_m/(b sqrt(H_n))=theta S_m/S_n->0. Late drift has total normalized mass ->theta, late noise supremum variance O((H_n-H_m)/H_n)->0 by Doob. A deterministic bounded-disturbance tracking estimate then gives normalized last iterate convergence to -soft_theta(Z), not a Gaussian itself. Normalized objective ->gamma b² theta/2 (|Z|-theta)_+, with mean gamma b² theta[phi(theta)-theta barPhi(theta)] from uniform L2 moments. Root uniqueness follows theta barPhi(theta)/phi(theta) increasing 0->1 and crossing 1/2. Independent 100,000 random finite bounded-disturbance trajectories satisfied the claimed 3delta+h tracking bound; numerical unique theta*=0.612003180962481, coefficient 0.10122824509401235. The finite checks corroborate but do not prove the triangular-array CLT/limit.

## originality

PASS

Beretta–Cesari–Colomboni arxiv:2610.30143v1 Theorem 2 uses the same scalar absolute-value bounded-iid-noise construction to prove an expected logarithmic last-iterate lower bound, choosing epsilon via mean absolute Rademacher sum. Their complete Section 2 (read) does not derive a weak limit, nonlinear Gaussian soft threshold, atom or exact optimized leading coefficient. Their rate is prior work and explicitly credited. The new claim uses a theta-dependent horizon-tuned scaling and computes a distributional refinement beyond a rate.

## value

PASS

The Gaussian-to-soft-threshold transition yields a point mass at the minimizer, explicit exceedance curve, exact expected error and unique optimal within-family tuning. It refines an established lower bound in a mathematically natural way and quantifies stochastic subgradient dynamics, not just another big-O rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
