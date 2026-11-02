---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verification.py` using only the Python 3 standard library. The program performs exact Fraction-based inversion of the directed-cycle resolvent and verifies the stated diagonal closed form, row stochasticity, positivity of the off-diagonals, maximum-rate comparison, and exact sign of the positivity polynomial on 6,020 rational instances. It also numerically brackets 48 homogeneous roots at 90-digit precision and checks the trend of their exponentially scaled differences.

Observed output:

`PASS rational_cycle_step_cases 6020 negative_cases 4361 high_precision_uniform_roots 48 last_scaled_gap 1.000000000000045297099404710`

The decisive mathematical checks are the geometric-circuit resolvent formula, the inequality \(\prod_{j\ne i}z_j(1+\sum_{j\ne i}(1-z_j))<1\), and the fact that \(\min_i R_{ii}(t)\) occurs exactly where the departure rate is maximal. These prove the all-parameter result; enumerated numerical tests alone cannot establish it. No external independent validation has been performed.
