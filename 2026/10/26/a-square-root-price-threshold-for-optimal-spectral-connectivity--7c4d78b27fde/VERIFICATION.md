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

# Reproducibility and claim-to-evidence

Run `python3 verify_star.py` in an environment with Python 3, NumPy and their standard dependencies. The independently assembled star Laplacian is symmetric, and exact finite-dimensional minors use `fractions.Fraction`; random experiments use a fixed seed.

The checker directly verifies the budget identity and positive semidefinite slack for 3,601 integer-square price configurations, matches the exact formula with full Laplacian eigenvalues, compares 11,550 asymmetric feasible allocations, and independently checks 770 real-price choices plus the sharp threshold. The expected console output is embedded as `verification_output.txt`.

The complete infinite mathematical argument is the algebraic dual proof in `RESULT.md`. Finite eigenvalue experiments do not establish optimality or prove global novelty. The independent audit status above is unperformed, not an attestation.
