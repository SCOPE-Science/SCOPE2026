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
# Verification

The algebraic argument in RESULT.md is the proof. It derives the exact moment-generating functions, compares their signs, establishes a unique crossing of exponential-tilt means, differentiates the Legendre-rate difference, and treats both speed-saturation boundaries. No probabilistic finite experiment is used as a universal proof.

The standalone `verify.py` uses only the Python standard library. Executed from the actual candidate source, it reported:

```
PASS: 2,000 MGF identities; 6,000 direct speed comparisons; boundary/threshold tests
q_critical 0.145200330326436
q 0.125 R_switch 2.132710411412251 speed_at_switch 1.000000000000000
q 0.2 R_switch 1.449099457773091 speed_at_switch 0.802611100064735
```

Finite tests do not establish the theorem or coverage of all possible previous publications. The claimed mathematical speed is the linear-determinacy functional for the stated atomic kernels; additional assumptions are needed to transfer it to a particular nonlinear ecological model. Independent audit has not been performed.
