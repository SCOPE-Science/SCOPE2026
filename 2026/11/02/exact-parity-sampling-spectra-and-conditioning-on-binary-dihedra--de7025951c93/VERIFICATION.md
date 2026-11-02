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

# Verification scope

Run `python3 artifacts/verify.py` with Python 3 standard library. The script checks the exact Fourier-residue counts, all rank cases, all predicted nonzero condition-number ratios, and the spectral translation for 8,460 dimension/degree pairs. It also constructs the actual \(S^3\) points and Chebyshev kernel entries for six sizes, verifies the circular Fourier transforms, checks the orthogonal cross-circle blocks, and directly confirms the matrix translation identity; this gives 114 direct block/degree runs. The expected output is:

```
EXACT_SPECTRAL_CHECKS_OK 8460
DIRECT_BLOCK_AND_SHIFT_CHECKS_OK 114
```

These finite checks do not prove the all-order assertion. The analytic proof uses a complete Fourier diagonalization and integer residue counts, including the constant-mode split and antipodal symmetry. No independent external verification has been performed.
