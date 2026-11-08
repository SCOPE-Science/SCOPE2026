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

The frozen-composition two-state transition chain has conditional stationary h_beta(c)=c^beta/(1-c+c^beta). Differentiating gives N_beta(p) with N_beta'<0 on (0,1) for beta>=2, N(0)>0>N(1), hence one inflection p_beta. A local fourth-order binomial/Taylor bound with exp-small tails gives g(Eh(K/g)-h(p)) -> p(1-p)h''/2 for fixed interior p; boundary substitution t=beta(1-p)=log beta-loglog beta+a gives normalized N -> 1-exp(-a), bracketing root. Independent stationary balance and beta=2,3,5,10,100,1000 numeric root checks corroborate. It does NOT address evolving strategies, uniform in p, or finite-g exact crossing locations.

## originality

PASS

Wei et al. supply the exact two-state environment transition mechanism in adaptive hypergraph public-goods dynamics. Candidate freezes composition, averages stationary h over Bin(g,p), proves strict curvature crossover and beta boundary layer; general Voronovskaya theorem implies expansion but not the model-specific uniqueness and scaling. Resultary semantic queries of published records performed with two tailored queries; no exact dominating result located, and this is not proof of priority. The listed primary sources were compared on mathematical implications; inaccessible relevant text retained as risk.

## value

PASS

For a fixed binomially sampled hyperedge in a published two-state transition model, sign of environmental sampling bias and its unique sensitivity-dependent transition are natural analytic comparative-statistics quantities. The asymptotic logarithmic threshold is nontrivial; does not imply conclusions for fully adaptive evolutionary dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
