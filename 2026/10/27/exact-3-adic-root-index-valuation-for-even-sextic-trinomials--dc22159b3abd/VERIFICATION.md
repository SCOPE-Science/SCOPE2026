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

The \(m=2\) and \(m=4\) expansions were multiplied out symbolically and agree with the defining polynomial. Modulo \(3\), \(\overline F=(x^2+1)^3\), with \(x^2+1\) irreducible over \(\mathbb F_3\). The coefficient valuations give the polygon described in RESULT.md. Its only positive lattice point on or below the polygon is \((1,1)\), contributing \(2\) to the \(\phi\)-index. The principal sides have degree-one residual polynomials, so the 3-regular equality case of Ore's theorem applies.

Boundary checked: if the constant coefficient in the \(\phi\)-expansion is zero, the left-hand side is absent but the vertex \((1,1)\) and the remaining residual polynomial persist. No finite search is used to infer an infinite claim. The statement is limited to the index of the defining root; field monogenity and the common index remain unresolved here.
