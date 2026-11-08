---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: The Lie brackets on ordered (h,e,f,u,v) completely specify a 50×25 matrix over Z[δ] for ten basis pairs and five output coordinates. The actual verifier gives 14 ±1 unit pivots and 19 residual rows, with 11 remaining variables, so no characteristic-sensitive inversion is required; the residual equations split into 2 dimensions at δ=1, 2 at (δ−1)(δ+2)=0, 2 at δ=−2, and the 3-variable block contributing two at δ=1 or one at 2δ=1 otherwise. This yields dim Derδ=4 I(δ=1)+2 I((δ−1)(δ+2)=0)+2 I(δ=−2)+I(2δ=1) for all char≠2, including collisions characteristic 3 (dim8 at δ1) and 5 (dim5 at δ−2=1/2). Independently constructed the full defining matrix from brackets and checked rank for every δ in eight prime fields p=3,5,7,11,13,17,19,23. These finite checks corroborate the characteristic-uniform integral elimination, not replace it.

## originality

PASS

PASS, qualified: A 2026 special-affine Lie-algebra paper already identifies the complex δ=−2 four-dimensional space; it is credited. The assessed new claim is the all-odd-characteristic spectrum, especially collisions in p=3 and p=5. Broader modular classifications under quasi-derivation terminology remain a risk. Full text of the closest paper was unavailable after lawful retrieval attempts.

## value

PASS

PASS: the full exceptional-parameter spectrum of a natural smallest special-affine semidirect Lie algebra and characteristic 3/5 jumps demonstrate genuine modular behavior invisible over C. These are intrinsic algebraic invariants and a complete classification, not a routine renaming of the known complex special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
