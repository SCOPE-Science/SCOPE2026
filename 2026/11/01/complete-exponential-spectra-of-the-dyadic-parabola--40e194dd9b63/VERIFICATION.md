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

# Exact finite checks

Run `python3 check_dyadic_spectra.py` in the directory containing the two files. Only Python 3 standard-library modules are needed. This code reduces all character sums modulo the cyclotomic polynomial \(X^{2^{k-1}}+1\), which is an exact zero test for primitive \(2^k\)-th roots. It does not use floating-point approximations.

The checked program produces:

```
DYADIC_PARABOLA_SPECTRA_OK 1 2 bases 4
DYADIC_PARABOLA_SPECTRA_OK 2 4 bases 64
DYADIC_PARABOLA_SPECTRA_OK 3 8 bases 16384
DYADIC_GAUSS_ZERO_CLASSIFICATION_OK 4 16 frequencies 256
DYADIC_GAUSS_ZERO_CLASSIFICATION_OK 5 32 frequencies 1024
DYADIC_GAUSS_ZERO_CLASSIFICATION_OK 6 64 frequencies 4096
```

For each modulus from \(2\) through \(64\), every two-coefficient quadratic sum is compared against the claimed valuation/lowest-differing-bit rule. The program enumerates every predicted spectrum for moduli \(2\), \(4\), and \(8\), checking pairwise orthogonality and nonduplication. At moduli \(2\) and \(4\) it also independently checks every possible subset of the full frequency square of the requisite cardinality, verifying completeness. The unlimited-level theorem follows from the symbolic proof in `RESULT.md`; these tests are finite corroboration only.

No external validation or independent mathematical audit has been performed.
