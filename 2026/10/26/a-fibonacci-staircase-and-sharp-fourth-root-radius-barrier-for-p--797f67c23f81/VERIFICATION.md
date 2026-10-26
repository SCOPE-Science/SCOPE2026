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

# Verification details

`CHECK.py` tests the exact Farey enclosure, threshold formula, convex-cone separating functional and explicit positive coefficients for all integral widths from \(1\) to \(89\). It enumerates every lattice vector in the prescribed square and computes with integers, rationals and exact quadratic algebraic numbers using SymPy. The included `CHECK_OUTPUT.txt` is the actual run's output. Assertions cover 972,414 independently evaluated algebraic or integer conditions. The program uses no random input or external network calls.

The infinite statements are proved in the result: Farey adjacency excludes all new rational slopes until the next Fibonacci width, exact cone separation rules out any smaller regularization, a two-direction stencil attains equality, and Binet's formula yields sharp upper and lower asymptotic constants. The finite computation cannot establish those universal statements on its own.

The strongest literature priority uncertainty comes from earlier optimally compact two-dimensional stencil results and Voronoi lattice-reduction constructions that could contain an equivalent derived special case. No independent validation or external certification is asserted.
