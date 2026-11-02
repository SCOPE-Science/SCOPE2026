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

# Verification of the exact affine-plane fiber theorem

Every mathematical equality in `RESULT.md` is proved symbolically. The standalone `verify.py` checks the characteristic polynomial using a full determinant, checks diagonalizability through eigenspaces, enumerates square-zero matrices, and verifies all per-spectrum multiplicities for four fields.

```
q=2: square_zero=22, diagonalizable_sums=0, distinct_spectra=0, fiber=4, PASS
q=4: square_zero=316, diagonalizable_sums=16, distinct_spectra=1, fiber=16, PASS
q=8: square_zero=4600, diagonalizable_sums=448, distinct_spectra=7, fiber=64, PASS
q=16: square_zero=69616, diagonalizable_sums=8960, distinct_spectra=35, fiber=256, PASS
VERIFY_OK
```

Run `python3 verify.py` with Python 3.9 or later. The implementation requires no nonstandard dependencies. The listed cases are not a proof for arbitrarily large fields; that role is supplied by the determinant-lemma parameterization and spectral-count argument. Historical priority beyond the inspected sources is unverified. Independent audit is not performed.
