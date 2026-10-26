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

Run `python CHECKER.py` using SymPy. The checker is self-contained apart from SymPy and uses exact arithmetic, not floating-point optimization. It verifies the degree-two Hermitian identity, factorization of the determinant, three-anchor kernel ranks and determinants for multiple circle/line geometries, an explicit right-angle circle, a nonorthogonal example, and two non-phase-equivalent polynomials indistinguishable on the whole unit circle and real axis. Compare its output with `verification_output.txt`.

The infinite theorem and the seven-measurement impossibility are derived analytically in `RESULT.md`: no finite test can certify the quantifiers over all complex coefficients and all anchor triples. No independent external audit has been performed.
