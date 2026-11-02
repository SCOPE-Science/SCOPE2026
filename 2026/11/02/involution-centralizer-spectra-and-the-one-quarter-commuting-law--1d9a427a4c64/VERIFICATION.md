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

# Verification record

Run the included `ut4_even_involution_verify.py` with Python 3; it has no dependencies. It constructs finite fields with irreducible binary polynomials of degrees one, two, and three, checks matrix products, and enumerates unitriangular square-one matrices.

Observed execution:

```
q=2, involutions=28, commuting ordered pairs=448, checked centralizers=28
q=4, involutions=496, commuting ordered pairs=96256, checked centralizers=496
q=8, involutions=8128, commuting ordered pairs=20905984, checked centralizers=4
VERIFY_OK involution commutation and centralizers in UT4 over even fields
```

Every involution centralizer and every ordered pair were checked at field orders two and four. At order eight the involution enumeration and classification were exhaustive, but only one representative centralizer was recomputed in each class; the ordered pair count there follows from the proved category formula, not exhaustive pair enumeration. The proof in `RESULT.md` supplies the unrestricted calculation for all field orders \(q=2^m\).

The centralizer notion is restricted to square-one elements; no full-group centralizer size has been misidentified as a restricted count. Independent auditing has not been performed.
