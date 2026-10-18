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

# Verification
The independent standard-library Python program `VERIFY.py` enumerates finite-step first-return probabilities by direct evolution of the radial two-orientation Markov chain, then compares them exactly to coefficients of the algebraic generating function. It verifies the return-probability formula and the mean identity with exact fractions, and checks the strict exponential-base range numerically.

Execution: `python VERIFY.py` — `PASS: 720 checks (finite first-return coefficients, exact identities and exponential rate).`

The program tests finite horizons. The proof of all-horizon identities uses the regenerative first-step equations and of the asymptotic uses the square-root singularity and coefficient transfer; neither is obtained from finite enumeration. An external independent assessment has not been performed.
