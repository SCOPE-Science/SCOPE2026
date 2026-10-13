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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and its standard library. The code generates all \(27\) basis-triple mixed identities from an arbitrary \(27\)-entry product, computes their rank and verifies the nine-parameter compatibility table. It then symbolically evaluates the full second-product associators with exact integer polynomials, checks the six decisive coefficients, verifies the determinantal restriction and the two affine component families, and compares full associativity with the geometric cases.

Exhaustive checks enumerate every compatible table parameter tuple over \(\mathbf F_2\) and \(\mathbf F_3\) (all \(512\) and \(19683\) tuples), finding respectively \(56\) and \(387\) associative products. Deterministic sample comparisons also run over \(\mathbf F_5,\mathbf F_7,\mathbf F_{11}\). The reported polynomial counts for those fields derive from the proof, not exhaustive enumeration.

The symbolic calculations use universal integer coefficients, but the dimension and irreducibility conclusions additionally depend on the explicit case split and standard rank-one determinantal geometry explained in `RESULT.md`. Code output alone is not a substitute for that proof. No claim is made concerning nilpotents in the full representing scheme, up-to-isomorphism classifications, or external independent verification.
