---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Because a is nonsquare and char(k) is not two, K=k(s), s^2=a, is a separable quadratic extension. The vectors g_+=x+sy and g_-=x-sy become group-like. For a two-point group-like coalgebra, compatibility forces each basis product to be 0,g_+, or g_-, and generalized self-distributivity becomes the finite table identity (uv)w=(uw)(vw). Exact enumeration gives 21 split tables. The nontrivial Galois automorphism swaps g_+ and g_-; faithful scalar descent says a product is defined over k exactly when its table is fixed by this simultaneous swap. Exactly five of the 21 are fixed, and changing basis gives precisely the displayed five products. Counit multiplicativity requires all four group-like table entries to have counit one rather than zero, leaving three. If a is square the group-like basis already lies over k, so all 21 occur. The frozen verifier independently enumerates the 81 raw tables, confirms 21/5/3, symbolically changes basis, and brute-forces the F3 nonsquare case.

## originality

PASS

Bardakov--Kozlovskaya--Talalaev give a full two-dimensional counital classification over C and, for the type-3 coalgebra, their full primary PDF explicitly labels the displayed multiplication list as partial and uses square-root(a) formulas. Over C every nonzero a is square, so that classification does not address descent over a ground field where a is nonsquare. Carter--Crans--Elhamdadi--Saito supply the split two-group-like table classification. The audited quadratic-Galois fixed-table argument exactly resolves the missing nonsquare form and yields the 21-to-5 square-class jump.

## value

PASS

The exact square-class jump resolves a genuine field-of-definition gap left by a complex two-dimensional classification. It identifies the complete nonsplit product set and its counital subfamily uniformly over every characteristic-not-two field, a natural structural classification rather than a single finite-field census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
