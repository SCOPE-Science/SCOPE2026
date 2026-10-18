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
# Verification record

The supplied `CHECKER.py` is an executable rational-arithmetic witness; run `python3 CHECKER.py` on Python 3 without external dependencies.

The computation constructs the tetrahedron, the three-dimensional cube, and the dodecahedral generalized Petersen graph; enumerates all adjacency-preserving bijections through exhaustive constraint-compatible recursion; and verifies the group orders \(24,48,120\), full edge orbits, and vanishing cut–cycle character inner products. The code computes grounded Laplacian solutions over exact `fractions.Fraction` objects, checks every Kirchhoff equation, and obtains cut norms \(3/2,2,38/15\), cycle norms \(3/2,11/6,34/15\), and source-edge effective resistances \(1/2,7/12,19/30\). Planar duality obtains the remaining two graph rows.

Independent scientific audit and validation have not been performed. No floating-point tolerance, stochastic sampling, or unbounded experimental extrapolation is used. The certificate checks the finite group and linear system only; the accompanying proof explains why those values are globally optimal across **all** projections and why duality applies.
