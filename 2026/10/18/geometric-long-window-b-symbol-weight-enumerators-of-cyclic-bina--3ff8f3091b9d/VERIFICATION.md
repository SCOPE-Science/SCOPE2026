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

# Verification instructions

Run `python3 verify.py` (Python 3 standard library only). The checker builds the cyclic parity-check columns in a polynomial basis using primitive field polynomials `0b1011`, `0b10011`, and `0b100101` for degrees 3, 4 and 5 respectively. It independently calculates every cyclic window weight by inspecting its binary coordinates, rather than using the weight formula under review.

The tests: full parity-syndrome enumeration of all length-7 and length-15 words for all window widths above half length; enumeration of codewords with endpoints one in anchored arcs up to length 7 (degree 4) or 15 (degree 5); direct verification of their window weights; and a literal uniqueness check over all 31 rotations of every supported degree-five codeword. Every coefficient equals the formula and all assertions must pass.

Expected terminal markers:
```
FULL_OK m=3 length=7 words=16 windows=4
FULL_OK m=4 length=15 words=2048 windows=8
SHORT_OK m=4 length=15 anchored_length_counts={5: 1, 6: 1, 7: 2} rotation_unique=False
SHORT_OK m=5 length=31 anchored_length_counts={6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 16, 12: 32, 13: 64, 14: 128, 15: 256} rotation_unique=True
VERIFY_OK cyclic_hamming_long_window
```

The mathematical theorem for arbitrary degree follows from parity-column rank, zero-run uniqueness and endpoint counting; finite enumerations do not establish that infinite assertion alone. External independent audit has not been performed.
