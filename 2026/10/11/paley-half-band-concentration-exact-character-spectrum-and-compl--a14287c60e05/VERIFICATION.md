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

# Reproducibility and proof checks

The executable `VERIFY.py` recomputes Fourier Gram matrices and the quadratic Legendre kernel for prime moduli congruent to \(3\) modulo \(4\) up to \(101\). It then separately compares complete numerical eigenvalue spectra against the restricted Jacobi-sum character formula and verifies the exact centered variance identity numerically. It also tests the inversion sign pairing and central-level absence when the subgroup order is prime.

Run: `python VERIFY.py` (Python 3 and NumPy). Observed output concludes:

`VERIFY_OK primes=13 eigenvalue_characters=265 Gram_identity=PASS complementary_pairs=PASS centered_moment=PASS safe_prime_gap=PASS`

The calculation is finite and floating-point, not a computer proof of the general theorem. Exact algebraic reconstruction is in `RESULT.md`: quadratic Gauss sum, multiplicative-character diagonalization, Fourier Parseval, and the prime-order cyclotomic polynomial argument. Strict positivity and contractivity require the external prime-order uncertainty theorem, not a finite eigenvalue test. Near-singular finite examples need extra precision for accurate small eigenvalues; no floating-point result is used to infer exact zero/nonzero.
