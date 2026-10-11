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

# Reproducibility and verification boundaries

Run the included self-contained `verification.py` with Python 3.10 or later:

```sh
python3 verification.py
```

The checked run printed `VERIFY_OK; assertions=67861`. All assertions use exact integer bitmasks and characteristic-two arithmetic; no random seeds, external files, downloaded packages, or floating-point assumptions are required.

The checker independently constructs each row of the \(2^n\)-vertex distance-two graph by enumerating all two-bit coordinate flips. It then adds the identity exactly when \(\binom n2\) is odd and checks the predicted shifted matrix rank by Boolean elimination for each integer \(2\le n\le10\). For every such dimension, it also verifies the shifted matrix squares to zero on every basis vector. At \(n=2,3,4\), exhaustive enumeration of the complete configuration space checks the two-step orbit identities, fixed-state counts, two-cycle counts, and one-step-versus-two-step extinction counts.

These tests corroborate the exact formulas only over the enumerated finite dimensions. The theorem for all dimensions relies on the invertible generator substitution in even dimensions and the alternating-form/Künneth homology computation in odd dimensions. The verification makes no claim of an independent audit or external certification.
