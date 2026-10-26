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

# Computational verification and limits

Run `python VERIFY.py` with Python 3, NumPy and SciPy installed. The source code is self-contained and requires no external data.

The program independently solves the two-state backward boundary-value problem via matrix exponentials and a boundedness condition, without using the hyperbolic-cotangent closed formula in that calculation. It compares the outputs over 400 deterministic-random positive parameter sets and random interior starting positions and orientation biases. The largest measured absolute error was \(1.62\times10^{-13}\). It separately evaluates 300 strict derivative signs for the ratio of effective trap impedances and 110 sampled parameter sets for the phase criterion, and checks exact symmetry, asymptotic regimes, and the exhibited unique crossing.

Passing this finite suite establishes reproducibility of numerical identities in the sampled domain. The recurrence proof, all-parameter monotonicity of the hyperbolic ratio, and existence/uniqueness of the crossover require the analytic proof in `RESULT.md` and are not implied by tests. Independent scientific audit has not been performed.
