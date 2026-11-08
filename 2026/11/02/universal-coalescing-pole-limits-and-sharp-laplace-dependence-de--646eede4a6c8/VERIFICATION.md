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

The single-pole integral is 2 Gamma(1-1/beta) s^(1/beta). Joint triangular-array Laplace functional splits into two marginals minus convolution overlap; convergence follows from g continuity, local coordinate scaling and integrable beta>1 tails (infinity separation gives zero overlap). Layer-cake intersections of moving centered intervals give strict decrease, differentiating convolution and integration by parts gives J0-Jdelta = beta*s*t*Gamma(2+1/beta)/(s+t)^(2+1/beta)*delta^2+o(delta^2), and splitting two neighborhoods gives C_beta*(t*s^(1/beta)+s*t^(1/beta))*delta^(-beta)+o. Scaling J_delta(cs,ct)=c^(1/beta)J_(delta*c^(-1/beta))(s,t) rules out joint positive stable homogeneity for delta in (0,infinity). Independent fresh quadrature beta=2,s=0.8,t=1.3 found small-delta coefficient ratio 0.99997165 at 0.01 and large-delta coefficient ratio 0.99974208 at delta=100; this corroborates but does not prove all-beta assertions.

## originality

PASS

Best-of-knowledge distinction based on actual statement/implication comparisons: generic techniques or marginals are credited, and the explicit theorem-specific conclusions were not found as covered by the primary material inspected; no claim of exhaustively proven historical novelty. The rescaled two-coalescing-pole inverse-distance statistics of independent observations on a circle converge to the specified two-site Poisson shot-noise law, with continuous strictly decreasing joint-Laplace overlap J_delta, sharp quadratic near-coincidence defect, power-law large-separation overlap, and non-joint-stability for every finite delta>0.

## value

PASS

The 1/(n*g(0)) coalescence window is a motivated critical spatial scale at which two singular observables change from identical to independent stable marginals. Exact monotonicity, both leading constants and the non-stable intermediate family provide a quantitative two-point dependence classification beyond generic Poisson-integral machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
