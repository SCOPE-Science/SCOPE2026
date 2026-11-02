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

# Verification notes

The exact formulas for the individual responses and scalar return map were derived in the proof in `RESULT.md`, including all gain and parity cases. Run `python3 VERIFY.py` from the extracted package with Python 3 and its standard library only. The deterministic check prints:

```
PASS: 53550 exact composition comparisons, 510 critical checks, 6480 supercritical orbit checks, 4 exact examples
```

The checker uses rational numbers throughout, comparing direct sequential best responses with the proposed clipped-affine return map. It additionally compares the squared map at unit gain, tests finite entry into a fixed point of the increasing return under supercritical gain, and checks homogeneous exact examples at unit and double weights. The finite counts are checks of derived identities and examples, not exhaustive enumeration of all real parameters or a substitute for the mathematical proof.

No human review, formal proof assistant, or independent validation is represented by these checks. The stated scientific limits and publication-priority risk remain applicable.
