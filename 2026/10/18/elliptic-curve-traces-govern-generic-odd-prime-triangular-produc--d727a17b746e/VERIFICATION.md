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

# Verification and reproducibility

The formula is proved algebraically in `RESULT.md`; the executable checker `verify.py` is supplementary. On Python 3 with no external dependencies run `python verify.py` from the extracted artifact directory. The checker computes finite-field character sums, zero counts and quartic elliptic traces independently for all generic shifts at eight primes, then compares the two exact-rational density expressions. It checks Hasse's inequality and verifies that finite congruence square frequencies bracket the p-adic Haar density, with the width predicted by smooth p-adic lifting.

Observed output from the embedded code:

```
VERIFICATION_OK
finite_field_cases: 108
modular_bracketing_cases: 5
examples: delta_5(2)=4/75, delta_7(1)=149/196
```

The general proof relies on Haar-preserving coordinate substitution, nonvanishing partial derivatives on the relevant zero classes, elementary quadratic character sums, a smooth genus-one quartic point count, and Hasse's theorem. None of the finite enumerations is asserted to certify the theorem for all primes. No independent audit has been conducted.
