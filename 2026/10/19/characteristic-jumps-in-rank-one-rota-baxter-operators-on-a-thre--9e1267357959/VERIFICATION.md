---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For R=f(-)u, taking one argument in ker f shows f composed with each of left and right multiplication by u is proportional to f. The identity then gives u²=(α+β)u. A nonzero α+β would give a nonzero idempotent in a local algebra, hence u=(α+β)1; substitution gives α+β=2(α+β), a contradiction in every characteristic. With u²=0 the multiplication maps are square-zero, so α=β=0. These conditions are sufficient and imply R²=0. For u=v+w+z in the radical, u²=2v∧w. With v nonzero in characteristic different from two, w∈v∧V and z∈v∧Λ²V, so u is v times a unit and the left-plus-right span is vE=Ev. In characteristic two any radical element squares to zero and replacing v by u in a basis of generators is an automorphism: it preserves the exterior relations and is invertible on the radical filtration. The degree-two and degree-three leading cases give spans of dimensions two and one, and the degree-one case gives four. Counting projective lines yields q^(3+ε)(q²+q+1), q(q²+q+1), and 1; for each line the nonzero maps into it that vanish on its multiplication span are a punctured (8−r)-dimensional fiber. This proves the count for every prime power. Over an algebraically closed field the strata are affine bundles over projective leading-term lines (and a point for degree three); their base dimensions are (5,3,0) outside characteristic two and (6,3,0) in characteristic two. The annihilator ranks are constant on each stratum; taking the nonzero parts of the corresponding Hom bundles gives dimensions 9 and 10, including characteristic zero in the former case. Independent small prime-field enumeration confirmed the line counts, ideal ranks and totals; the general conclusions use the algebraic argument, not enumeration.

## originality

PASS

Best-of-knowledge pass for the complete rank-exactly-one operator census and the dimension jump. The odd-characteristic degree-one image-line enumeration is already present in equivalent form in the earlier three-generator retraction record and should not be credited as new. Its result does not give the Rota–Baxter functional fibers, the remaining leading degrees, the characteristic-two count or the dimension jump. The two-generator classifications and tables do not cover the full claim.

## value

PASS

This is the full smallest nonzero-rank stratum on the first exterior algebra beyond the plane where v∧w can obstruct square-zero elements. It quantifies the new geometry when 2 vanishes, giving both exact counts for every finite field and the dimensions of the geometric strata. These are useful benchmarks for classification and finite-field computations; the value is in the operator fibers and characteristic comparison, not in re-counting the previously known odd-field image base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
