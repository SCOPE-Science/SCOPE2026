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

`verify.py` is self-contained for the exact witness portion, using Python's standard library. Execute with `python verify.py`. If NumPy is installed, the program also computes independent symmetric-eigensolver spectral projectors and checks mixing matrix entries, ranks, and unmarked special cases.

For \(3\le n\le22\) and four integer nonzero marks, 80 exact integer moment determinants equal \((-1)^{\lfloor n/2\rfloor}\tau^{\lfloor n/2\rfloor}\). With NumPy, the code checks 96 spectral profiles and 12,624 average-mixing entries for orders \(3\le n\le18\), including \(\tau=0\), negative marks and nonintegral positive marks.

Successful reproducible output:

```
EXACT_WITNESS_OK 80
VERIFY_OK exact_witness_profiles=80 numerical_spectral_profiles=96 numerical_entries=12624 moment_det=(-1)^floor(n/2)*potential^floor(n/2)
```

NumPy uses finite-precision eigenvalue clustering; these computations test examples and cannot prove claims for arbitrary real potentials or unrestricted graph order. The proof in `RESULT.md` supplies the unrestricted upper bound, the closed-walk lower bound and the unmarked cycle boundary. No human or independent external audit is implied.
