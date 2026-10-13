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

The standalone `verify.py` artifact was read from its packaged path before replay.

It checks the complete six-type forcing census, exhaustively tests all \(2^{18}\) subsets in the small graph \(\operatorname{AG}(\mathbb F_3^3)\), and directly reconstructs annihilator adjacency in \(\mathbb F_3\times\mathbb F_3\times\mathbb F_5\) from coordinate multiplication and annihilator sets.

It also checks exact rational rank \(4\) for the quotient and representative blowups, verifies the symmetric-coefficient identities, and replays field-order recovery on repeated and unequal examples.

Exact replay output:

```text
PROFILE_CENSUS_OK {0: 1, 1: 6, 2: 15, 3: 20, 4: 12} [(1, 2, 5, 6), (1, 3, 4, 6), (2, 3, 4, 5)]
FULL_BRUTE_F3_CUBE_OK {14: 864, 15: 504, 16: 132, 17: 18, 18: 1}
DIRECT_UNEQUAL_F3_F3_F5_OK [8, 8, 4, 4, 2, 2] 28
RANK_FOUR_OK
RECOVER (3, 3, 3) -> (3, 3, 3) coeff_min 864
RECOVER (3, 3, 5) -> (3, 3, 5) coeff_min 4160
RECOVER (3, 5, 7) -> (3, 5, 7) coeff_min 48192
RECOVER (4, 5, 9) -> (4, 5, 9) coeff_min 215040
RECOVER (5, 7, 11) -> (5, 7, 11) coeff_min 1604160
VERIFY_OK
```

The finite calculations corroborate the proof. The arbitrary-field-order statement follows from the symbolic weighted-census and coefficient-inversion arguments.
