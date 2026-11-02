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

The proof is mathematical and does not rely on exhaustive enumeration. `verify.py` is a standalone executable Python 3 script using only the standard library, with exact rational arithmetic and no external files.

Run `python3 verify.py` from the directory containing the script. Expected output:

```text
PASS: 394 exact-rational assertions (the curvature tolerance check is a rational inequality).
```

The checker independently assembles and solves the full finite absorbing-state transition system for alphabet sizes up to four, comparing expected hitting time and PGF values with the closed subset-sum formulas. It also checks published uniform special cases through size eight, explicit two-type mean penalties, strict weighted pair-balancing transform improvement and exact mean-gap identities through size seven, and local Hessian consistency in a rational small-perturbation test.

The checks establish consistency of the displayed formulas at tested inputs; they are not an exhaustive verification over continuous parameters or unbounded alphabet size. The all-size proof uses the product semigroup, resolvent strong Markov identity, and pointwise pair-balancing argument in `RESULT.md`. Independent audit remains not performed.
