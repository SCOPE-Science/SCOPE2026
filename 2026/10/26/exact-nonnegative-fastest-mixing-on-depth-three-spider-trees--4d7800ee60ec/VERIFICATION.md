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

# Reproducibility of the depth-three spider theorem

Run `python verify.py` with a Python 3 interpreter and installed packages specified in `requirements.txt`. A successful run prints `VERIFY_OK symbolic_identities=5 reduced_spectra=28 full_laplacians=12 feasibility_trials=2800`, followed by numerical examples; the complete output is stored in `verification_output.txt`.

Exact SymPy calculations verify five displayed algebraic identities: the positive-contrast eigenvector relation, tridiagonal determinant factorization, the quadratic evaluation at \(2-\gamma\), the characteristic determinant at \(\gamma\), and the Rayleigh upper-bound identity. Floating-point spectral tests then independently construct all \(3k+1\) vertices for \(k=3,\ldots,14\), compare reduced spectra for \(k=3,\ldots,30\), and test 2,800 feasible randomized probability triples. These test instances check implementation consistency but do not constitute a global numerical search, proof of uniqueness outside symmetric matrices, or proof for infinitely many graph orders.

The analytic proof in `RESULT.md` is the mathematical justification for the universal statement. It uses a positive eigenvector certificate, monotonicity of a Rayleigh quotient, and an exact radial spectral factorization. The statement excludes the unconstrained symmetric averaging problem with potentially negative diagonals.
