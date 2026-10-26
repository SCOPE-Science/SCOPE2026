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

# Reproducibility and verification

`check_icosahedral.py` is included as an ordinary standalone scientific checker. It enumerates the \(60\) even permutations on five letters and separates the two order-five classes by conjugation. It constructs every matrix entry directly from rotation class and evaluates the full \(60\times60\) spectrum using NumPy, separately from the character formulas. For exponents \(0.1\), \(0.5\), \(\log(4/3)/\log(3/2)\), \(0.73\), \(1\), and \(1.5\), every predicted eigenvalue and its multiplicity agrees with the direct symmetric-matrix spectrum to absolute error less than \(3.1\times10^{-13}\). Matrices of \(\exp(-t d^s)\) at \(t=0.005,0.1,2\) corroborate the change in sign at small damping. The checker reports `PROOF-SUPPLEMENT CHECKS PASSED`.

Run with Python 3 and NumPy: `python check_icosahedral.py`. These floating-point checks do not establish any universal real-parameter claim. The complete proof is elementary after central Fourier diagonalization and uses exact inequalities recorded in `RESULT.md`. At the endpoint the five-dimensional representation's convolution coefficient is exactly zero, creating a \(25\)-dimensional nullspace on zero-sum coefficients; the other three coefficients are proved strictly negative. The self-review has passed; independent audit and validation have not been performed.
