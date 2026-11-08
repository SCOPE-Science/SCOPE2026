---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Independently integrate quadratic Lagrange polynomials at nodes 0,-previous,-current to obtain the exact variable-step AB3 companion matrix and 2-step product; independent SymPy symbolic expansion reproduced all three claimed cubic characteristic coefficients and exact determinant at z=1. With C>0, B<1, C<1, A>C>0 under s<6/(5+2q), the cubic Schur inequalities reduce to that one determinant. At equality the unit root is simple and residual quadratic strictly stable; above root >1 by sign at z=1. q=r/(1+r)^2 yields reciprocal ratio intervals, and a rank-one r^-1 limit of large-step transfer yields the norm constant. These are for fixed positive ratio and real negative test eigenvalue, not uniform transient robustness for arbitrary step grids.

## originality

PASS

Best-of-knowledge qualified originality after exact statement/implication comparisons; primary work covers key ingredients, but the final parameter-specific classification is not established in inspected prior results. Residual risks explicitly retained.

## value

PASS

An exact spectral stability phase diagram for alternating genuine variable-step AB3 and sharp counterexample to interpreting two-step decay as stepwise transient robustness resolves a motivated numerical-methods issue; unexpected split stable ratio regimes and precise 11/10 mean-step gain are concrete invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
