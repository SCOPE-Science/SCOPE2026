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

# Reproducible verification

Execute `python3 verification.py` using Python 3 and its standard library. The verifier constructs addition and multiplication tables directly (including binary extension fields from irreducible polynomials) and enumerates every bijection of each explicitly listed finite ring of size at most nine. It checks injectivity of both transformed maps directly. Exactly fourteen small rings/fields are exhaustively searched: twelve yield no simultaneous map, \(\mathbb F_4\) yields two, and \(\mathbb F_8\) yields six. The same program confirms the constructive scalar family in \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\), three products of binary extension fields, and both separate one-operation complete mappings on \(\mathbb F_2\times\mathbb F_4\).

The code does not enumerate arbitrary rings, nor is its finite evidence used in place of the proof of the universal classification. The proof depends on principal-ideal invariance under a finite permutation, the standard finite-reduced-ring structure theorem, the product of the nonzero elements of an odd finite field, and Frobenius bijectivity in finite fields of characteristic two. All boundary cases, including rings with nilpotents, the field of two elements, products, and the excluded zero ring, are made explicit in `RESULT.md`.
