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

# Reproduction and scope

Run `python verify.py` in an environment with Python 3, NumPy and SciPy installed. The script checks exact Gaussian projection algebra on random SPD matrices, the Student-regularized-beta identity, equality of the sharp two-eigenvalue angle witness, the sign and Pareto-tail formulas, and numerical approach of independently replicated sample means toward the analytically specified Cauchy quantiles. With its fixed pseudorandom seed, it prints `PASS: 1562 algebraic, probabilistic, sharpness, Cauchy-law, and numerical checks`.

The infinite moment claims and Cauchy weak limit depend on the written probability and characteristic-function proof, not on finite simulations. Exact equality in distribution is proved for every fixed real SPD input and every finite integer sketch size. Historical priority has not been independently established; independent mathematical audit has not been performed.
