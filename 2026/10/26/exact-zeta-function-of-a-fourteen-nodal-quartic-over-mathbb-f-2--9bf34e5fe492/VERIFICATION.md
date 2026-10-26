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

# Verification and scope

Run `python3 verify.py` from a directory containing the accompanying `count.c` and `verify.py`. Python standard library plus a C11 compiler are required. The test runs field-polynomial irreducibility and multiplicative sanity checks, direct low-degree point enumerations, algebraic Frobenius action on all fourteen geometric nodes in \(\mathbb F_{64}\), and exhaustive character sums for degrees 1 through 12. Exact rational Newton identities, K3 reciprocal symmetry, cyclotomic factor multiplication, and exceptional-curve cancellation are checked without floating point. The observed final token is `VERIFY_OK`.

This checks the finite arithmetic inputs to a mathematical proof. The infinite all-extension conclusion additionally uses standard K3 cohomology and Weil bounds; the code does not search infinitely many fields. The self-review is included in `REVIEW.md` and `AUDIT.json`. Independent audit or outside verification has not taken place. In the coefficient-field check, the Frobenius node-orbit decomposition is computed in the full \(\mathbb F_{64}\), rather than assumed from the desired zeta factor.
