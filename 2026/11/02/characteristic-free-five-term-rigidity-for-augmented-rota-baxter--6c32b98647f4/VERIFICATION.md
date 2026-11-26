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

The units give a+b=c+d=1. On the square-zero ideal test, P(1)=0 and P²=−λP; I,e,P are independent also at λ=0 and in characteristic two. In the associator expansion, terms PII, Pee, PIe and IIP, eeP, eIP give the idempotence and mixed-product equations, while PIP and PeP give h(a−c)=h(b−d)=0. Unequal pairs therefore give the two announced vectors. At weight zero the equal pairs give left side y⊗y and right side 2y⊗y or 0. On dual numbers at nonzero weight, the inner argument is −λt⊗t, and its two evaluations force h=±λ⁻¹ as claimed. In the first equal-pair case, the three-point prefix test has zero inner argument and nonzero product λ²(δ₁+δ₂)⊗(δ₁+δ₂). In the second, the four-point witness has zero inner argument and product λ²(δ₂+δ₃)⊗δ₃, nonzero in characteristic two. The prefix operator identity follows by partitioning index pairs by their order. For sufficiency, expand the tensor identity for T=I⊗P+P⊗e on simple tensors: the I⊗P part reduces to the identity in the second factor plus the two cross terms; the P⊗e part reduces to the identity in the first factor times the product of the two augmentations, using εP=0. Both parenthesizations expand to I⊗I⊗P+I⊗P⊗e+P⊗e⊗e. The other orientation is obtained by reversing factors. Naturality and unit compatibility follow directly. This checks the universal ordinary associator/unit claim without relying on finite tests.

## originality

PASS

The supported distinction is the all-characteristic completion of the known five-term rigidity theorem, not the two positive constructions or the characteristic-zero classification. The remaining nonzero-weight obstruction in characteristic two is genuinely absent from the closest inspected proof. The related all-field no-braiding theorem has a different conclusion.

## value

PASS

The restriction is the natural one from the motivating rigidity theorem. A concrete obstruction in characteristic two settles the only resonant coefficient case missed by the known proof and gives the same classification without a characteristic restriction. It is not merely an example of a failed tensor formula without a universal consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
