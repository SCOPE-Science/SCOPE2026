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
# Reproducibility

Run `python3 artifacts/verify.py` with Python 3 standard library from the extracted package root. The exact-integer script returned:

```
PASS: 164 exact coefficient, direct-history, and inversion-count checks
Direct histories exhausted for n=0,...,9 (9! paths at n=9).
General n,r statements require the separate analytic proof.
```

The verifier constructs finite-prefix coefficients for surplus values 0 through 9, independently enumerates all admissible histories up to nine time steps, compares the Mahonian inversion-count distribution, and tests the leading Newton coefficients. Its exhaustive scope is finite; the proof in `RESULT.md` establishes every asserted parameter case. The relative asymptotic applies at fixed integer surplus at least three. Independent audit has not been performed.
