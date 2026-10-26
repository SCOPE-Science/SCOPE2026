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

# Verification instructions

Run `python3 verify.py` using Python 3's standard library. The program reports the exact integer count of successful rational assertions and raises on the first failure. Its output was saved in `CHECKS.txt` and reproduced from the package.

The script checks the adjacent-eigenvalue polynomial identity at 501 nonnegative integer indices, three other exact polynomials, two resonance gaps, and first/second eigenindex orderings for 81 modes at 17 positive rational radii. It is finite algebraic corroboration, not an exhaustive numerical proof for every radius or index.

The proof of the infinitely many modes is entirely in `RESULT.md`: Gaussian angular diagonalization, the closed-form adjacent difference, the strict Gamma-mass comparison for \(x\le n\), exact low-index comparisons, and the sharp spectral-distance decomposition. Check the exponential Taylor inequalities \(e^2>6\) and \(e^3>20\) by finitely many positive series terms. At critical \(x=1\), the gap is to the next *distinct* eigenvalue and remains strictly positive even though the maximizing multiplicity is three. At \(x=2\), it is the runner-up multiplicity that is three.

Independent scientific examination and external priority certification have not been performed.
