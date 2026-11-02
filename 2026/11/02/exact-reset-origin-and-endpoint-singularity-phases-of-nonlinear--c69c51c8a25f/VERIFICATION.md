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

# Reproducible mathematical checks

The analytical calculation in `RESULT.md` supplies all the necessary proofs. A separate finite numerical verifier tests the same stationary transport equations, not simulations of unrestricted long-time paths.

Install the packages listed in `requirements.txt` and run `python verify.py` in the directory containing both files. The script integrates the stationary current system inward from near its regular-singular endpoint for seven parameter triples of tangent or hyperbolic-tangent drag and rate settings. The solution is scaled using the *independently derived* reset source-current identity \(J(0+)=r/2\). For each case it compares the finite-difference derivative at zero with the closed expression, the fitted endpoint log-log exponent with \((r+\lambda)/k_*-1\), and the ratio of inward/outward endpoint current magnitudes with \(\lambda/(r+\lambda)\). A successful execution reports 21 comparisons passed.

These checks are necessarily at finite distances from the endpoints and use numerical ODE integration. They establish neither the mathematical asymptotic limits nor the originality of the claims. The proof gives the complete infinite-domain argument, including positivity of the edge coefficient. The local-morphology reversal and coexistence threshold are exact inequalities and do not depend on numerical evidence.

Independent external validation has not been performed.
