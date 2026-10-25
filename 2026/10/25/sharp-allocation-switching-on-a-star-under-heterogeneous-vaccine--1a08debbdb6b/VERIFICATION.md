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

Execute the accompanying self-contained Python 3 file with `python3 verify.py`.
Its completed execution returned `VERIFY_OK 20706 assertions` (20,706 separate assertions).
The program independently constructs symmetric full-size star epidemic matrices and computes their eigenvalues by Jacobi rotation rather than using the stated two-dimensional formula. It checks the clipped optimizer against sampled allocations, verifies analytic differentiation and switching threshold cases, and checks exact-rational examples. No third-party packages or network access are needed.

The proof of all-real-parameter and arbitrary-star-size uniqueness is the strict Perron eigenvalue convexity argument and two-dimensional symbolic analysis in RESULT.md, not any finite random search. Numerical tolerances apply only to numerical corroboration. No claim concerning nonlinear epidemic dynamics, arbitrary mobility graphs, or budgets with binding susceptible caps is certified here. Independent audit has not been performed.
