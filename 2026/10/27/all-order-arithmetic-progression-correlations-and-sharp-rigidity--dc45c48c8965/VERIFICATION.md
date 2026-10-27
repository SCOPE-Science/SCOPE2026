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

# Mathematical verification

Run `python3 verify.py` in this directory. The checker uses only Python standard-library `fractions.Fraction` and integer arithmetic. The verified output is:

```text
VERIFY_OK: 4096 exact all-order recurrence values; 24 precisely predicted sharp orders; 256 independently evaluated 2-adic cylinder tests with error bounds; even-order parity separation checked for 2048 lengths
```

The two-adic-cylinder checks construct periodic residue-class sums independently of the rational recurrences and compare with an explicit error bound \(2m/2^L\). All exact computations use finite integers or rational numbers, not floating-point approximations.

The unrestricted proof is mathematical: cylinder-periodization establishes existence of every Cesàro correlation, Haar-scaling and parity classes yield the formulas, and induction proves all sharp-index assertions. Finite sampling is not treated as an infinite proof. The statement is restricted to equally spaced samples; possible earlier equivalent specializations of general model-set formulas remain a historical-priority risk.
