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
# Reproducibility

Execute `python verify.py` from this package with packages in `requirements.txt` installed. The script checks the proposed weights and Fourier eigenvalues for 98 graph sizes; for 30 sizes it constructs the full transition matrix and compares its dense spectrum and the result of an independent SciPy linear-programming optimizer; it tests 980 other feasible invariant matrices against the analytical lower bound; it checks the complete parity-dependent heuristic spectra through 80 vertices in the parameter and exact low-order identities. It prints the line in `verification_output.txt` on success.

The proof in `RESULT.md`, not computational sampling, establishes the infinite-domain theorem. SciPy optimizers and random or deterministic finite samples do not certify global optimality; that claim rests on the explicit convex-averaging argument, sharp three-constraint linear dual bound and exact spectral endpoint checks. No independent external review has occurred.
