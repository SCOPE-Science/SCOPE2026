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

For the exact normalized payoff U_i=a_i(neighbor mean −d_i θ/3), the gains are Δ_leaf=c−θ/3 and Δ_h=k/2−2θ/3. The degree-weighted potential Ψ=a1a2+a2a3−θ(a1+4a2+a3)/3 increases along improving moves; for 3/4<θ<3/2 there are only absorbing zero-noise equilibria 000 and 111. Min-cost paths have resistances R000→111=θ−1/2, R111→000=1−2θ/3; their equality is θ=9/10. Transient-root trees are more costly. At critical θ, exhaustive independent exact-rational enumeration of six-state rooted trees gave coefficients 12 and 18 for 000 and 111 and strict larger exponents at other four roots, hence 2/5 and 3/5 limiting probabilities. The potential is uniquely maximized at 111 for θ<1, so (0.9,1) is a true contradiction to potential-maximizer selection under uniform common inverse noise. Proof requires the open θ interval; finite parameter tests are not universal proof.

## originality

PASS

The original 2023 Zhang–Vasconcelos model has the normalized payoff but proved regular-graph selection; their 2024 general irregular-graph analysis changes the payoff to unnormalized neighbor sums. Therefore their general theorem does not cover P3 in this exact 2023 model. Generic Markov chain tree methods are prior; the exact 9/10 critical mixture in the three-node normalized game was not found in searches.

## value

PASS

A fully solved smallest irregular graph with explicit stochastic equilibrium selection at odds with welfare and weighted-potential maximization is a motivated boundary example. Exact critical mixture and transition distinguish it from unmotivated small-instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
