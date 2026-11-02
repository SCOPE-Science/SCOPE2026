---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The multiplication xy=T_m(x⊙y) is bounded because l²·l²⊂l¹; T_m has the displayed isometric right inverse, operator norm sqrt(m), and exact head-sum-zero kernel. Every l¹ vector factors as a product via its l¹ right-inverse preimage. For a second orthonormal natural basis, all pairwise coefficient products belong to l¹∩ker T_m. The tail rows each have one unit coefficient in distinct columns, leaving m head columns; their unitary matrix Q has Q^tQ diagonal, and after unimodular square-root diagonal removal becomes a real orthogonal matrix. Conversely every O(m) head rotation works. Injective T|l¹ forces any basis change monomial. Checked exact rational Householder head rotations m=2..7 and finite-window rank equations independently. The infinite conclusion follows from the explicit analytic proof, not finite windows.

## originality

PASS

No located exact or dominating covering result after primary-paper and Resultary comparisons; all four named comparison checks and residual priority risks are separately documented.

## value

PASS

A concrete negative resolution of an explicit infinite-dimensional density/rigidity problem, with the smallest possible nonzero kernel and exact positive-dimensional natural-basis moduli, supplies a reusable structural boundary and a one-way general injectivity criterion; not merely a renamed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
