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

# Reproducing the mathematical checks

Run `python verify_orthant.py` using Python 3 with NumPy and SymPy. The test script directly evaluates positive-orthant fourth monomial moments using gamma functions and creates the entire degree-two matrix in independent orthonormal bases for each integer dimension \(3\le n\le10\). It compares every eigenvalue (counting multiplicities) against the proposed four-branch formula, and verifies the trace of the region-restricted operator.

For dimension three, the script also computes the region matrix by Gauss-Legendre surface quadrature over the positive spherical octant, **not** by inserting the gamma moments or the spectral formula. The eigenvalues agree at absolute error below \(10^{-12}\). Finally SymPy checks three exact polynomial identities: a top-versus-standard comparison, the lower-branch determinant factorization, and the full-trace identity. The supplied `verification_output.txt` is output from a local execution of that exact script.

The proof's central nonstandard step is the block reduction via the unsigned vertex-edge incidence matrix; its identities are displayed in `RESULT.md`. Matrix tests and symbolic simplifications are not substitutes for the analytic argument in dimensions beyond those tested. The strict sign of the lower-branch determinant uses \(3<\pi<22/7\), and the complete eigenspace count uses the full-rank property of the incidence matrix for integer \(n\ge3\). The finite experiments do not verify originality, and no external independent validation is claimed.
