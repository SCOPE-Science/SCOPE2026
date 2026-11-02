---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: For a fixed input sign path and predictable rule, Z_k=(eps_k-m_k)h_k(xi_1,...,xi_{k-1}) are independent centered bounded masked variables with sum Var(Z_k)/k² finite, so Kolmogorov’s strong law gives their averages tending to zero. Fubini yields, for almost every fixed mask, almost-sure input-path vanishing of scaled cross-brackets. Adding the deterministic bias contribution bounded by a_n gives uniform-in-time bracket convergence to t I_2 for the pair (X,Y) conditioned on the mask. Each increment has length sqrt 2, so the vector martingale functional CLT applies in D([0,1],R²). Conversely choosing the fixed predictable h_k=sgn m_k forces a nonvanishing terminal cross-covariance on a subsequence whenever a_n fails, and uniform fourth moments of each marginal simple random walk make terminal products uniformly integrable. Hoeffding’s exponential maximal inequality yields P(max_{j<=n}|Q_j|>n(a_n+delta))<=2e^(-n delta²/2). The quantifier is for all fixed h, a.e. mask separately, not a common mask set for uncountably many h: a realized mask can be matched by the deterministic h_k=eps_k selected after that mask. Independently enumerated all fair masks and input walks to n=6 for a nontrivial predictable rule, confirming zero centered cross-bracket and E Q_n²=n. The infinite functional convergence is analytic, not deduced from enumeration.

## originality

PASS

PASS, qualified: Hamza–Tournier 2026 establish annealed functional convergence in their time-by-subset-size one-factor construction and explicitly do not settle its general quenched counterpart; their quenched theorem assumes different subset-indexed coefficient independence. Collevecchio–Hamza–Shi–Williams 2022 give the general martingale-bracket invariance principle but not the universal all-predictable-rules iff criterion from absolute Cesàro mask bias. This universal sharp temporal-bias characterization and fair-empty-coefficient application are the scientific contribution. Because it is built from standard martingale tools, an implicit prior equivalent characterization is a live historical-priority risk.

## value

PASS

PASS: Determining exactly which independent temporal perturbations force quenched decoupling against every fixed predictable transformation is a natural sharp invariance-principle question. A precise iff via absolute Cesàro bias, an adversarial necessity rule, exponential finite-horizon deviation estimate, and the fair-empty-bit subcase of an explicitly open question make the result useful beyond a routine statement that a martingale CLT exists. Its delicate null-set quantifier boundary prevents an otherwise plausible false strengthening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
