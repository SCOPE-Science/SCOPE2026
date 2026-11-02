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

The companion `verify.py` uses standard Python only. It generates every row-reduced echelon subspace of the ambient five-dimensional vector space without duplicate subspaces and computes Lie brackets from the exact defining structure constants. For each generated subspace it checks closure under the bracket for every unordered basis pair, and separately detects abelian three-dimensional subalgebras. It implements the characteristic-two extension field with an irreducible quadratic polynomial.

Run `python3 verify.py`. Verified output ends in `VERIFY_OK`. Exhaustive dimension-count profiles are `(1,31,43,19,3,1)` for q=2, `(1,121,157,49,4,1)` for q=3, and `(1,341,421,101,5,1)` for q=4. The exhaustive counts of abelian three-dimensional subalgebras are respectively 7, 13 and 21. These directly check the formula for small fields. The proof in `RESULT.md` establishes the stated identities for every prime power; finite enumeration alone is not used to infer the all-field result.

No independent external review or certification is represented by these checks.
