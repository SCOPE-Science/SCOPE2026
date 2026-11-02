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

The proof uses the explicit stationary GKLS Bloch system and exact rational identities, plus sign arguments for the derivative and for a single positive quadratic root. No finite experiment is used as an infinite proof.

Run the standalone `verify.py` with `python verify.py` using Python, NumPy and SymPy. It constructs the actual two-level Lindblad matrices and solves the trace-preserving stationary linear equations, checks positive eigenvalues and equations of motion, compares all three Bloch components against the closed forms, tests the ergotropy and purity signs across a parameter grid, verifies the symbolic Bloch-norm identity and derivative, and checks the exact physical-integer step criterion. The executed program completed 1,832 checks successfully.

The tests cover a finite parameter grid only. The universal claims require the analytical positivity, uniqueness and factorization arguments in `RESULT.md`. No independent verification is asserted. The oscillator ancillas enter via the exact thermal Lindblad rates, rather than a finite Fock-space truncation. Physical integer clusters must be distinguished from the real-valued algebraic threshold used to classify them. Numerical witness rounding is illustrative and does not provide an exact certificate for arbitrary parameters.
