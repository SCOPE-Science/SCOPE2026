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

# Reproducibility and limits

Run `python3 artifacts/verify.py` from the extracted package root. It requires Python's standard library only. The script checks exactly, in the integral group ring, four Fourier cancellations for every prime congruent to three modulo eight below eight hundred. It also checks two-root quadratic-residue witnesses and uses integer cyclotomic-polynomial arithmetic to exhaust the normalized two- and three-point principal minors for primes three, eleven, and nineteen.

Expected output:

```
PRIMES_WITH_EXACT_FOUR_POINT_WITNESS 37
NONZERO_TWO_POINT_DETERMINANTS 488
NONZERO_THREE_POINT_DETERMINANTS 143576
VERIFY_OK
```

The exact integer computation does not rely on tolerance, but verifies only finitely many primes. Uniform correctness follows from the displayed proof, including the anisotropic quadratic form and the strictly positive sine-phase comparison. The theorem is limited to the standard dot-product Fourier transform on the stated family of finite vector spaces. Independent audit has not been performed.
