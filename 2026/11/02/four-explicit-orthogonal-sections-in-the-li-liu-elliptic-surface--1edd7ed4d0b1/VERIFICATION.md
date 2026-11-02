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

Run `python verify.py` with SymPy installed. The exact-arithmetic checker returns `VERIFY_OK` if its polynomial and local-model assertions hold. It checks the three point identities in the quotient by \(b^6+b^2+1\), the squarefreeness of the two relevant defining polynomials, the equations of the four sections near ramified infinity, the nonsingularity of that fiber at the common point, the rational antecedent's \(c_4\) and discriminant orders, and the height-matrix determinant arithmetic. The checker was run successfully.

Geometric implications not independently certified by code: rational-point extension to sections on the Kodaira–Néron model; that distinct local \(Y\)-slopes imply intersection multiplicity one at a smooth point; Shioda's height formula and quadratic base-change scaling; and the Oguiso–Shioda identification of the rational elliptic surface's Mordell–Weil lattice with \(D_4^*\). They are stated and justified in `RESULT.md` with relevant primary references. This verification is not an independent mathematical audit. No whole-family rank-equality claim is made.
