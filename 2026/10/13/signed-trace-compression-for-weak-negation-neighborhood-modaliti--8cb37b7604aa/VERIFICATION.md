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

# Reproducibility and logical checks

Place `verify_polarity.py` and `verify_certificates.py` in the same directory as this file. Run `python3 verify_polarity.py` and `python3 verify_certificates.py` with a Python 3 standard-library interpreter. Both tests have deterministic pseudorandom seeds. The observed outputs were:

```
VERIFY_OK cases=2700 with_modal=2028 max_worlds=5 max_subformulas=23
VERIFY_OK certificates=1500 boolean_translation_instances=9600
```

`verify_polarity.py` independently reconstructs signed valuations over the selected root-preserving witness set from four unrestricted neighborhood functions and asserts complete equality of the restricted positive and negative columns on every subformula. It also checks the \(2k-1\) bound whenever modal operands exist. `verify_certificates.py` checks truth-table and neighborhood extensionality column conditions against random valid signed models, probes deliberate extensionality violations where the tested columns permit them, and checks 9,600 values of the classical-tautology reduction.

The mathematical proof, not the random finite experiments, establishes the infinite-world preservation statement, simultaneous trace sharpness and complexity classifications. The bound is sharp for the specified trace-separation obligation; no minimum-countermodel-size theorem is asserted. The complexity result applies only to unrestricted signed neighborhood membership semantics and finite-premise local consequence. The related 2018 and 2023 classical modal results limit any claim that the abstract complexity class itself is novel.
