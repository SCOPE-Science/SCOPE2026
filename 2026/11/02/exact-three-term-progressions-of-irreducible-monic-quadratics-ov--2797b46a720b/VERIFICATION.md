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

# Verification details
Run `python3 verify.py` with the Python standard library. It creates prime-power fields as polynomial quotients by monic irreducible moduli, determines nonsquares from explicit squares, enumerates every nonzero-slope affine step, and for each step counts all monic quadratic coefficient pairs satisfying the three discriminant tests. The exact integer formula is checked with assertions on each case.

Verified field orders: 3, 5, 7, 9, 11, 13, 17, 19, 25, 27. Total step cases: 2322. Observed result: `VERIFY_OK shift_cases 2322`.

The finite checks are not an exhaustive verification over all prime powers. The proof of the universal theorem instead rests on an invertible coefficient change, a quadratic-character identity, and an exact correction for the three zero-discriminant lines. Independent audit: not performed.
