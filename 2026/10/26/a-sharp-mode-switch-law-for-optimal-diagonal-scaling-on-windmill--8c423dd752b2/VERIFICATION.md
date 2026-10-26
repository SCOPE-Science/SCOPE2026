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
# Verification and reproducibility

Run `python verify_windmill.py` using Python 3 with NumPy, SciPy and SymPy. The executable prints PASS summaries for the stated checks when all tests complete.

The executable performs exact symbolic checks of the eigenvalue-crossing polynomial, the mode-transition identity, and the Jacobi-optimality identity. It then validates the complete (unscaled and scaled) characteristic polynomials on five full rational matrices, compares closed forms with 75 full-matrix spectral decompositions, makes 75 independent bounded one-dimensional numerical minimizations, and checks 6,000 unrelated asymmetric diagonal scalings.

The mathematical proof is analytic and does not rely on statistical or finite checking. The symbolic checks verify displayed identities, not the group-averaging argument or every possible positive real parameter; the latter are established in `RESULT.md`. In particular, random trials are not exhaustive global optimization certificates. Independent mathematical review has not been performed.
