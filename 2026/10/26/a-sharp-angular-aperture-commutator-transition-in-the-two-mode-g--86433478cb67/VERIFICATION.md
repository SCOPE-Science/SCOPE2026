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

# Verification of the angular-aperture commutator theorem

Run `python verify.py` with Python 3, SymPy, NumPy, and SciPy installed. The script reports its assertion count and the critical radii used for numerical cross-checks; `verification_output.txt` contains the actual output of the packaged checker.

Analytical verification consists of: (i) polar integration in the orthonormal basis of constant and linear Fock monomials; (ii) a sharp first-Fourier-coefficient rearrangement with a unique-arc equality case; (iii) a two-by-two Hermitian commutator cross-product identity, followed by concave quadratic optimization; and (iv) a monotonic-integral representation proving the transition radius is unique for every pair of angular fractions strictly between zero and one.

The symbolic tests independently verify the commutator and both optimization branches. Numerical quadrature checks Gaussian normalization; finite sampled angular masks test only a subset of all measurable sets. Neither these finite samples nor finite root computations certify the universal claim. The proof uses no computer-assisted infinite certificate. No independent external mathematical audit has been performed.
