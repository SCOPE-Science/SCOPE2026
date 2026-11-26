---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Derivations are exactly (Av,Bv+ρ(A)w), since the commutator ideal is W and the bracket is the exterior product. At any point with v≠0 prescribe Av=Pv and use the free Bv to match the entire central component; the only constraint is Rw∈ρ(End V)w for every w∈W. Applying that to e_i∧e_j forbids entries involving neither index. Evaluation on e_i∧(e_j+e_l) equates the coefficients replacing i by h for each pair of partners j,l (at n=3 there is only one). Subtracting that off-diagonal induced action leaves d_ij. In the four coordinates of (e_i+e_h)∧(e_j+e_l), the tangent entries are sums of row and column scalars, hence d_ij+d_hl=d_il+d_hj in any characteristic. Using anchors 1 and 2 the differences s=d_1i−d_2i are constant for i≥3; setting c=d_12+s, a_1=0, a_j=d_1j−c gives d_ij=a_i+a_j+c, also for n=3 where s=d_13−d_23. No division or density over an infinite field is needed. For sufficiency, split the alternating form on V* associated to w into nondegenerate two-dimensional blocks and a radical (valid also in characteristic two); acting by 1 on one vector and 0 on the other in each dual bivector pair realizes I_W pointwise. The kernel of ρ is zero outside characteristic two and the scalars in characteristic two; there three pairwise equations a_i+a_j=1 rule out I_W in the image. The central-block dimension is therefore n² in both cases, giving the stated dimensions and finite-field ratio. The finite checker was inspected, not run; the all-field argument is algebraic.

## originality

PASS

The supported distinct contribution is the characteristic-two reflexive-hull defect, the division-free all-field computation, and the resulting invariant census that includes the modular case. The characteristic-not-two classification has an explicit matching indexed statement; it is credited as overlap, not claimed separately here. The inspected Lie-closure or existence theorems do not compute the required hull, and the odd-characteristic matching proof cannot be specialized to characteristic two by substituting parameters.

## value

PASS

The derived action loses rank in characteristic two, yet its pointwise reflexive hull regains exactly that rank in a direction that is not induced by any fixed generator endomorphism. This structural classification explains why the local census remains uniform even over F₂ and goes beyond finding a proper local derivation or recording a dimension alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
