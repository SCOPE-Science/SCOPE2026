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

The result holds for the stated exchange-symmetric deterministic ODE on strictly positive initial states. Bounded interaction terms and logistic comparison give positive global solutions. Subtracting resident per-capita growth rates gives y′=−(a/2)p y(1−y²), and differencing invader and mean resident payoffs gives z′=zp[(−k+ar/2)p−dz]. Thus in ds=p dt the squared contrast obeys r_s=−ar(1−r) and the resident odds obey w_s+(−k+ar/2)w=d. Their integrating factor is H(s)=e^{cs}/√(r₀+(1−r₀)e^{as}); its integral is exactly T(r₀) by u=e^(−as). The numerator w₀+d∫H is strictly decreasing, and its limit distinguishes all three cases, with w₀=R/I. If the limit is positive or zero, s goes to infinity in physical time; on equality the tail ratio ∫_s^∞H/H tends to 1/k and yields w→−d/k. On these branches the eventual mean interaction tends respectively to a/2 and c(−d)/(k−d), so scalar logistic comparison gives the claimed positive total limits. When the numerator vanishes first at finite s*, w_s(s*)=d<0 and p has a simple zero there. Physical time diverges logarithmically; equivalently d(log p)/dt→d<0, giving integrability of the mean interaction Φ=O(p). Solving (1/N)′=μ−Φ/N and applying the Cesàro limit to its integrating factor yields μtN→1 and z→1. Differentiation gives T′>0. Substitution u=(1−r)v gives the beta constant by dominated convergence with dominating integrand v^(q−1)/√(1+v/2) for r≥1/2 and 0<q<1/2. The balanced threshold uses T(0)=1/k, and the resident-equilibrium rare-invader exponent is −k.

## originality

PASS

Credit the explicit all-initial-state boundary, contrast scaling and physical-time treatment jointly, not the interaction model, the existence of total extinction in it, or the representation by replicator and projective Lotka–Volterra equations. The strongest inspected same-model primary passages describe a rare-invasion barrier and simulated outcomes, not the contrast-dependent basin formula. The strongest inspected catalogue matches analyze different dynamics. Classical phase-plane coverage of the projective special case could not be fully checked and is a residual risk, not a priority assertion.

## value

PASS

Within this published deterministic model class the finding quantifies the gap between linear invasion fitness and the actual basin. It provides a benchmark that is uniform over all positive initial triples in the symmetric slice, not a comparison of selected trajectories: the same resident sum can have arbitrarily different critical fractions as the imbalance changes, and asymptotic composition dominance is distinguished from establishment at positive abundance. The motivation and use are mathematical and model-specific.

The dated certificate retains the supplied scientific assessment, sources and limitations.
