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

Running `python3 verify.py` with Python 3.8 or later and no third-party libraries reproduces exact-integer checks:

```text
VERIFY_OK crt_cases=464 independent_exhaustive_cases=150 nonprimitive_representations=222 threshold_pairs=5
```

The test evaluates the CRT congruences for \(k=2,3,4,5,6,7\) and coprime parameter pairs above the corresponding primorial. It confirms that the constructed integer is positive and divisible by the prescribed primorial, that every candidate nonnegative representation has both multipliers divisible by its assigned prime, and that the exact lower bound holds. An independent exhaustive enumeration over \(150\) small constructed integers finds \(222\) nonnegative representations, none primitive. Five additional coprime pairs satisfy the displayed strict fourfold threshold via the \(k=5\) witness.

These are finite sanity checks, not an exhaustive test of all pairs or a substitute for the Chinese remainder theorem proof. The uniform asymptotic requires the prime number theorem, used only as a classical analytical input. Verification of other work or any independent audit is not claimed.
