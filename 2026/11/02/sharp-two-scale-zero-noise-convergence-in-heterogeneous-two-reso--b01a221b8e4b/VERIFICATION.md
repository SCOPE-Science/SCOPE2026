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

# Reproducibility and limitations

Execute `python check_rates.py` in a Python environment with SciPy installed. The program numerically solves the scalar logit equilibrium, checks the defining two congestion aggregates, compares three independently derived asymptotic ratios at several noise levels, verifies cutoff monotonicity over a grid from very small to large noise, evaluates the exact non-potential antisymmetric cross variation, and checks the general coefficient at three noise levels for a separate smooth nonuniform-density instance. Expected summaries include `VERIFY_OK sigma_cases=9 asymptotic_orders=3 nonpotential_gap=3/64` and `VERIFY_GENERAL_OK density_and_heterogeneous_weights`.

The numerical tests cover finitely many parameter values and do not certify general uniqueness, monotonicity, or asymptotics. The proof in `RESULT.md` establishes those conclusions under its stated assumptions, including the exact moment integrals and the interval-pairing argument. Exact symbolic coefficient claims do not depend on SciPy output. Independent audit remains unperformed.
