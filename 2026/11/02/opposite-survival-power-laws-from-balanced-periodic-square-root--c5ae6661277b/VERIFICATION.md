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

# Reproducibility and limitations

Run `python3 verify.py` using Python's standard library. The script recomputes the exact rational block coefficients for both absolute-time phases and both cyclic classes, checks the stationary and response equations, independently checks the two-factor polynomial matrix identity, verifies the stated stochastic support and killing constraints, and compares finite-horizon normalized survival log-slopes with the analytically derived powers.

The recorded run in `verification_output.txt` passed 56 exact and diagnostic assertions. The rational checks establish the finite matrix identities for the stated four-state model. The long-horizon calculation is a diagnostic only; finite computation does not prove convergence of the infinite-horizon powers. The latter depends on the analytical block expansion, primitive stochastic contraction, the second-order normalization formula and a summable-error logarithmic product argument given in `RESULT.md`.

The general theorem applies only to fixed finite state spaces, fixed transition support, periodic coefficients aligned with the primitive-block period, and a vanishing first-order stationary block mean. The proof does not assert the same power law outside the centering hypothesis. Historical priority of possible abstract asymptotic difference-equation reductions has not been independently resolved.
