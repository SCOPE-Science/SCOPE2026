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

Conditional on coupon-label history to full appearance, each type’s final refresh mark is independent stationary Bernoulli(p_i), independent of the label history and future marks. Thus C_m and W_m are independent. Poissonization with independent rate-one clocks gives all-present return kernel H_m(e^-t), and renewal at stationary hit yields a0/[s∫u^(s−1)H_m(u)du]. Max diffuse p→0 and bounded sum imply H_m→exp(c(u−1))∏(1−q_j+q_j u) uniformly; dominated convergence proves Laplace convergence. The continuous-time immigration–death plus finite flags process identifies a proper limit and the atom at zero. Gumbel coupon collector plus exact independence yields stated sum. Independent exact rational subset-state hitting equations reproduce finite PGF examples.

## originality

PASS

Attrill–Garoni Theorem 4.10 already supplies common-loss p_m with mp_m→c and its Gumbel+immigration–death law; that r=0 homogeneous special case is not novel. The new statement allows arbitrary asymptotically diffuse loss profiles plus finitely many macroscopic exceptional types, identifies their survival as distinct two-state components and gives exact heterogeneous PGF. Published nonuniform global-reset coupon models have different sampling and reset mechanics.

## value

PASS

The theorem identifies exactly which types of heterogeneity disappear under a critical scaling and which remain visible. A one-exception example produces a different atom from a homogeneous dust model, and exact finite transform supports calculation of real waiting distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
