---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof in `RESULT.md` evaluates the pointwise Green–Kubo kernel by a Laplace resolvent, bounds the conditional finite-time remainder by the first lag moment, and sums the geometric series and its first moment for the lattice. Strict monotonicity follows from differentiating the single-anchor summand; subtracting the one-sided phase limits leaves exactly the boundary term. These steps are analytic and require no numerical extrapolation.

The unchanged `check_hyperuniform.py` and `checker_output.txt` concern the earlier finite checks on the local kernel, its spatial integral, and the annealed plateau. They are supplemental and do not independently check the phase-resolved variance formula or the phase spread.
