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

# Numerical reproducibility and analytic limits

The executable `verify.py` uses only `numpy` and `mpmath` as declared in `requirements.txt`. Run `python verify.py` from the directory containing these files. On the final reviewed program, the observed output was:

`VERIFY_OK 215 ODE/Volterra, CPTP Schur, Poisson log-time, sharp Hilbert-Schmidt exponent`

The program performs direct time stepping of the original normalized history integral and compares with the confluent-hypergeometric formula across rates, biases and positive, zero or negative Bohr frequencies; differentiates the closed form and checks the scalar ODE; reconstructs finite-time multilevel phase-multiplier matrices and tests positive semidefiniteness as a check of complete positivity; compares rescaled time multipliers with independent compound-Poisson characteristic functions; tests the explicit sharp qubit first-order diamond coefficient numerically; and tests the leading Hilbert-Schmidt modulus and critical decay exponent. These are independent finite numerical consistency tests, not an exhaustive parameter sweep or a proof of infinite-time convergence.

The mathematical proof is in `RESULT.md`, and in particular uses a nonvanishing analytic Gamma coefficient, finite-dimensional norm equivalence, an exact Poisson channel expansion and a matching qubit diamond-norm lower bound. No independent audit, human review or external formal certification has been performed.
