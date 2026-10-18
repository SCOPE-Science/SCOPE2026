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

# Reproducibility and scientific limits

Run `python verify.py` with Python 3 and NumPy. The script reconstructs the unnormalized character evaluation matrices from the stated groups and compares their directly computed Gram eigenvalues, squared determinants, basis classifications, and optimizer counts to the theorem. Its recorded output is `verification_output.txt`; it must terminate with `ALL CHECKS PASSED`.

The proof's critical all-parameter identities are the occupancy pigeonhole argument, Fourier-orthogonality inversion, the codimension-one projection of the deleted basis vector, the matrix determinant lemma, Sherman--Morrison, and the three-level rank-one secular determinant. These identities are derived in `RESULT.md` and do not depend on finite enumeration.

The exhaustive computational cases are finite examples only; they cannot establish absence of exceptional configurations for larger groups or moduli. The matrix spectra were checked with floating-point arithmetic and tolerance, while the infinite-family proof is algebraic. The odd-modulus global optimum for the condition-number ratio remains unproved; only a universal lower bound and the spectrum of determinant-optimal bases are asserted.

The self-review is recorded separately. No independent scientific audit or certification is claimed.
