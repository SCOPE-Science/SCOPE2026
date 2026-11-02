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

For a deterministic finite total transition function, all-state AF P_j holds exactly iff every directed cycle hits each marked set. A cycle of length ℓ succeeds with probability ∏_j(1-(1-p_j)^ℓ); mapping components are cycles of rooted labelled trees with T=ze^T, so the weighted set-of-cycles EGF is exp(∑w_ℓT^ℓ/ℓ). Inclusion–exclusion gives the stated product and normalization n!/n^n. Joint falling factorial moments E∏(C_{ℓ,n})_{m_ℓ}=(n)_M/(n^M∏ℓ^{m_ℓ}) give independent Poisson(1/ℓ) limits for any fixed lengths; the missing-cycle tail ≤∑_{ℓ>L}ℓ^{-1}∑_j(1-p_j)^ℓ is uniformly small. Thus the infinite product limit is justified. For r=1 positive coefficients give p_1 identically. For r=2 the exact partial fraction F=1+λ((1-T)^-1-(1-cT)^-1), c=(1-p)(1-q), λ=pq/(1-c), reduces P_n=λ(1-Ec^{K_n}) with P(K_n=k)=(k/n)(n)_k/n^k. Survival P(K_n≥k)=(n)_k/n^k increases strictly for k≥2 in n; c∈(0,1) gives strict increase from pq to λ. Checked boundary n=1, and nondegenerate p_j∈(0,1).

## originality

PASS

Best-of-knowledge support for the complete combined statement: the independent-edge CTL literature studies a different probability space; classical random-mapping species and Poisson cycle laws already cover the core enumeration machinery and could give parts by specialization, but none of the actually inspected primary statements establishes the joint CTL all-n r-label law together with strict two-label finite-size interpolation. This is qualified novelty, not a claim to invent cycle EGFs, small-cycle Poisson convergence or the one-label identity.

## value

PASS

Several natural CTL eventuality obligations on uniformly random deterministic transition systems exhibit a nontrivial correlation and a precise size law: each one-label global requirement has probability p_j, yet two together increase strictly from pq to pq/(p+q-pq), and all r have an explicit non-0–1 limiting law. These are exact finite-state model-checking benchmark quantities for a canonical sparse transition class, and a motivated contrast with high-degree independent-edge 0–1 laws. The underlying mapping species is standard, so value is assigned to the complete joint-probability/interpolation classification, not to rebranding the exponential formula or a few finite checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
