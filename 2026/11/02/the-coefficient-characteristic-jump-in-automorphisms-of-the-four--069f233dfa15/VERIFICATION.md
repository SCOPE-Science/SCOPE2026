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

# Reproducibility and verification

`verify.py` requires Python 3 standard library only. Execute `python verify.py` within the directory containing the script. It constructs products from the defining multiplication \(e_i e_j=e_{2j-i\pmod4}\); determines coordinate multiplication in the characteristic-dependent bases; enumerates every invertible block map preserving the intrinsic right annihilator; and checks all sixteen defining basis products. Because every algebra automorphism must preserve that right annihilator, this enumeration is exhaustive for the finite fields tested, without assuming the proposed normal forms.

Actual output:

```
F_2: 576 annihilator-preserving invertible matrices checked, 32 automorphisms; expected 32: PASS
F_3: 186624 annihilator-preserving invertible matrices checked, 8 automorphisms; expected 8: PASS
VERIFY_OK
```

The implementation also checks that the accepted matrices coincide exactly with the claimed group normal forms. This is finite verification only; it does not certify fields outside these two tests. General-field correctness follows from the two-case symbolic proof in `RESULT.md`. No independent external audit has been performed.
