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

The recurrence and generating-function identities are proved algebraically in `RESULT.md`. `verify.py` independently constructs the exact finite labeled-substrate transition system, compares it with the reduced recurrence, tests the ordinary-generating-function coefficient equation in exact rational arithmetic, and evaluates the integral with high-precision quadrature. It also tests long finite recursions against the limiting quadrature. Running `python verify.py` with the dependency listed in `requirements.txt` produced the 646-assertion output in `verification_output.txt`.

The high-precision integration and finitely many system sizes are numerical corroboration only. They do not certify the infinite-system limit. The infinite limit is justified by the three-step stochastic-matrix contraction proof; the integral is evaluated using the first-order generating-function equation and Abelian convergence. No independent audit has been performed.
