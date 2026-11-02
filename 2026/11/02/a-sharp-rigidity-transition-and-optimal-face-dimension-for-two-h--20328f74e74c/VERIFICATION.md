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

# Verification record

The standalone `VERIFY.py` uses Python 3 standard-library exact fractions and explicitly checks the claimed transition matrices, row sums, nonnegativity, support, Walsh spectra, interpolation identities and distinct perturbation optimizers. Replaying it directly from this package produced:

```
VERIFY_OK 228683 exact assertions
```

It checks the rational mode bounds for dimensions 2 through 120, full matrices for dimensions 2 through 7, the nonuniform optimal perturbations for dimensions 5 through 7, and linearly independent pair-weight directions in dimensions 5 through 10. Every test uses exact rational arithmetic. The proof of the theorem for all integers \(d\ge2\) is mathematical and is given in `RESULT.md`; the finite checks are consistency checks, not an exhaustive infinite certificate. Historical literature coverage, especially the inaccessible full text of Karlin–Lindqvist–Yao (1993), and independent mathematical validation are not settled by this script.
