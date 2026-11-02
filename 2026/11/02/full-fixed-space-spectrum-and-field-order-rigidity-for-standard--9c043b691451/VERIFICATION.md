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

# Verification of the exact fixed-space spectrum

Run `python3 verify.py` in this directory; no external dependencies or downloaded data are required. The checker independently enumerates valid generator images and verifies every defining bracket and invertibility condition before accumulating a histogram of actual nullities of \(\phi-I\). It compares the histogram with the theorem formula, rather than merely checking that a formula implementation agrees with itself.

The checked field/algebra pairs are `(q,m)=(2,3),(2,4),(3,3),(3,4),(4,3),(5,3)` and several field-order existence boundaries. The nonprime field of order four is implemented directly as a polynomial quotient. Recorded results:

```
PASS q= 2 m= 3 |Aut|= 32 |FPF|= 0 fixed-space: {1: 8, 2: 14, 3: 9, 4: 1}
PASS q= 2 m= 4 |Aut|= 128 |FPF|= 0 fixed-space: {1: 32, 2: 56, 3: 22, 4: 17, 5: 1}
PASS q= 3 m= 3 |Aut|= 972 |FPF|= 0 fixed-space: {1: 756, 2: 183, 3: 32, 4: 1}
PASS q= 3 m= 4 |Aut|= 8748 |FPF|= 0 fixed-space: {1: 6075, 2: 2376, 3: 210, 4: 86, 5: 1}
PASS q= 4 m= 3 |Aut|= 9216 |FPF|= 0 fixed-space: {1: 8768, 2: 372, 3: 75, 4: 1}
PASS q= 5 m= 3 |Aut|= 50000 |FPF|= 12500 fixed-space: {0: 12500, 1: 35750, 2: 1605, 3: 144, 4: 1}
VERIFY_OK: independent generator enumeration and field-order threshold
```

The full general proof is provided in `RESULT.md`: intrinsic automorphism structure, finite characteristic-power unit normalization, uniform norm image, direct sum by residue classes, and exact valuations. Checking finitely many q and m does not substitute for the general argument, does not determine automorphism-conjugacy classes, and does not establish originality. No independent mathematical audit has yet been performed.
