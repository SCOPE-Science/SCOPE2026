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

Independently integrated derivatives of the reference quadratic Lagrange basis (the products are quadratic, hence the Lobatto rule is exact here), used the basis integrals for the nodal quadrature weights, assembled before boundary restriction, and inverted the entire polynomial matrix 18tS(t) over Z[t] by characteristic-polynomial arithmetic, without parity blocks or the frozen script. Verified the 625 entries and their 55 reflection/exchange/transposition classes. The exact recalculation found 45 zero-variation and 10 one-variation classes, positive denominator coefficients up to allowed zeros, and strictly positive numerator constants. Only the (1,3) orbit is negative at 21/5; every other numerator is strictly positive there, hence positive throughout (0,21/5] by Descartes' rule, including multiplicities. The recomputed witness is the stated -3Q divided by the stated positive denominator. Q has one sign variation and opposite signs at 41999/10000 and 21/5, so its only positive root is simple. At that root the eight witness entries alone vanish, and at every larger t the witness is negative. The rational value at 5 and the displayed root digits agree. S is SPD by the Dirichlet energy with a positive diagonal 1D mass and SPD 1D stiffness. Right multiplication by M_2 preserves signs. This is exactly the stated homogeneous Dirichlet nodal inverse criterion, not a general boundary or time-stepping result.

## originality

PASS

The inspected primary papers and strongest related indexed result provide a sufficient mesh condition, an experiment on a different mesh, and a different time-discretization threshold, not a covering theorem for the exact spatial transition. Pass is limited to the present family and to the best knowledge supported by accessible evidence. The Li dissertation remains a real priority risk.

## value

PASS

This is a natural graded family with a single interior element adjustable independently of overall rescaling, and with a nontrivial discrete monotonicity issue even though stiffness remains SPD. The exact interval, complete critical zero pattern and rational failure witness are useful as a graded-mesh benchmark and distinguish a genuinely sharp limit from conservative sufficient mesh bounds. The value is not a claim of new general finite-element convergence or stability theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
