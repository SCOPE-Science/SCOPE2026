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

# Verification procedure

Execute `python3 verify.py` using Python 3.9 or later from a directory containing the included verification script. The program factors every multiple of four at most \(100000\), keeps exactly the integers with four distinct prime factors, constructs their sixteen unitary divisors, and checks both exact equal-sum partition criteria without invoking the theorem's abundance inequalities. The complete verification prints:

```
FINITE_CENSUS up_to= 100000 four_support_divisible_by_four= 5851 unitary_zumkeller= 274 unitary_half= 274
CERTIFICATES_OK
VERIFY_OK
```

It separately verifies the explicit finite partition certificates and several prime-power instances of the infinite family. The proof of completeness for every unbounded integer is in `RESULT.md`, not in this finite experiment. The computational tests do not establish originality, and no independent audit or independent validation has been performed.
