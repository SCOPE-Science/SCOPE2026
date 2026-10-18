---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For H=I−Δ on any finite connected compact Kirchhoff metric graph, the vertex covariance heat trace F(s)=Σ_j (φ_j|V)^T Q(φ_j|V)e^{−sμ_j} is the Laplace transform of a positive measure because Q is PSD. Zero-length paths in the metric-graph heat kernel yield F(s)=S e^(−s)/sqrt(πs)+exponentially small error, S=Σ_v Q_vv/deg(v)>0 (a nonzero PSD Q has positive diagonal). Karamata gives cumulative weighted spectral mass N_Q(Λ)∼2S sqrtΛ/π. Itô isometry then yields critical expected H^(1/4) energy S/(2π) logΛ, supercritical energy S/[π(4α−1)] Λ^(2α−1/2), and subcritical finite energy for all α<1/4. Gaussian zero-one law plus Fernique excludes a.s. membership when mean-square norm diverges. Integrating F(2s) yields small-time S/2 erf(sqrt(2t))+O(exp(−c/t)). Offdiagonal Q only affects positive-length walks to leading small-time order. Independent interval example with Q=[[2,1],[1,3]] gave log-slope 0.7957175 vs target 5/(2π)=0.7957747, corroboration not proof.

## originality

PASS

General subcritical α<1/4 stochastic Kirchhoff regularity and the deterministic graph heat-kernel local Weyl coefficients are prior work. A prior Resultary paper gives a sharp critical coefficient only on an equilateral star with scalar noise at its center; the present claim covers every compact finite Kirchhoff metric graph and every fixed nonzero correlated PSD vertex covariance, including exact a.s. endpoint exclusion, universal degree-weighted critical and supercritical coefficients, and small-time stochastic energy. Complete matching prior work inspected does not imply those general covariance-weighted statements. Best-of-knowledge residual risk remains for older boundary-noise trace asymptotics under other normalizations.

## value

PASS

The same physically natural noise problem was previously known to lie in subcritical fractional spaces and to fail at a critical index in a highly symmetric star. The reviewed theorem solves the sharp endpoint and exact universal ultraviolet coefficient for arbitrary compact metric graphs and arbitrary correlated rank-deficient vertex covariances, identifying the local degree-weighted invariant S and proving off-diagonal correlations cannot cancel the leading singularity. The general power law and small-time energy give reusable spectral/regularity benchmarks beyond a special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
