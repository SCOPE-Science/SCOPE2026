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

# Verification of the rank-classification theorem

Execute `python verify.py` with Python 3 and NumPy. This script was run on the standalone file using the same exact input bytes included here and returned:

```
PASS: 7401 independent finite arithmetic/matrix checks
```

It tests 1,600 positive-integer rank-two spectra in exact rational arithmetic, the exact higher-rank invariant rays through rank twenty, necessary-step equal-singular-value obstructions, and 3,000 randomly rotated rank-two rectangular matrices through SVD. It checks the rank-raising discontinuity on both fixed-step and exact-line-search representations. These finite tests do not establish any infinite universal theorem; the proof in `RESULT.md` does so through exact algebra.

The complete proof is independent of pseudorandom sampling, tolerance choices, or any uninspected external executable. Numerical polar factors can handle tiny singular values differently from the exact-rank model; this limitation is central to the perturbation statement.
