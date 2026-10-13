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

# Verification and mathematical limits

Execute `python verify.py` with Python 3 and no third-party dependencies. The expected terminal output is:

`VERIFY_OK exact_rational_identities=2014 stable_trajectories=372 root=1.472229260972032 scalar_divergence_witness=1`

The rational-arithmetic checker reconstructs the derivative factorization, the exact critical-maximum identity, the cubic difference identity, and the polynomial residual expansion at 2,014 parameter/evaluation combinations. The decimal checker isolates the cubic root within a high-precision bracket and independently checks the exceptional fixed point at that root. Scalar trajectories exercise 372 fixed/switching coefficient cases within the recommended range and one explicit supercritical escape configuration.

The proof, not the program, justifies the global matrix statement: positive singular values evolve under a common scalar residual recurrence, an explicit interval is invariant for every admissible coefficient, and monotonicity forces each residual to zero. Numerical tests alone do not prove this for infinitely many dimensions, coefficients or iteration counts. The theorem makes no claim about coefficient policies above the threshold or about floating-point stability. No independent audit has been performed.
