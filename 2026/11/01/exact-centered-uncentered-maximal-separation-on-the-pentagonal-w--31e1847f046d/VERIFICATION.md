---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The graph K1 join C5 has precisely six singleton balls, five four-point rim neighborhoods and one full ball. For each output v the maximal average can be linearized by choosing one eligible averaging row. Counting gives 2*3^5=486 centered matrices and 7*5^5=21,875 uncentered. Independent construction and exhaustive integer Bareiss positive-definiteness tests on 216I-(12A)^T(12A) and 5832I-25(12A)^T(12A) found exactly one and five exceptions, respectively, with no floating-point tolerance. The exceptional centered winner has norm^2=3/2 with simple positive eigenvector (5,1^5). The five rotated uncentered winners have simple positive Perron eigenvectors (1,1,y,z,z,y) with lambda solving 64lambda^3-120lambda^2+27lambda-1=0 in (1.62,1.621). Strict ball-selection inequalities establish that these linear candidates attain the nonlinear operator and exhaust extremizers, up to signs and rotations. The exact finite enumeration is exhaustive, not an extrapolation or an opaque output log.

## originality

PASS

Best-of-knowledge, after implication-aware prior/source comparisons: The wheel theorem is not a corollary of published exact star/K_n constants or generic Perron theory without its new exhaustive and geometric computation.

## value

PASS

The pentagonal wheel is the smallest natural nontrivial wheel separating strong-L2 centered and uncentered graph-ball maximal norms in this audited family, with a nontrivial algebraic constant and rigorous all-extremizer symmetry breaking. Exact nonlinear norm and equality cases are mathematically reusable benchmarks for maximal inequalities on graph metrics, despite the single six-vertex focus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
