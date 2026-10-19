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

The analytic argument uses the full-minor theorem for the prime cyclic Fourier matrix, the complete dihedral irreducible decomposition, and a root-count argument for the symmetric determinant of each two-dimensional Fourier block.

To corroborate explicit equality witnesses, run `python3 check_profile.py` using Python 3. The checker constructs the full left convolution matrix on five sample prime dihedral groups, checks its ranks over auxiliary finite fields, and independently verifies the two prime-frequency zeros of the three-tap witness in the cyclotomic quotient. It prints `CHECK_OK` on success.

Residue-field experiments do not prove the complex rank bound at arbitrary primes and do not replace the analytic argument. In particular the prime Fourier-minor property is used as an external established theorem, not claimed as a new computation.

Independent audit has not been performed.
