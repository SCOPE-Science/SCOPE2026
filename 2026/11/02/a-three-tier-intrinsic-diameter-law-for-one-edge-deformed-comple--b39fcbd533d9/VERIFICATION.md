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

# Mathematical verification

The proof is fully analytic and applies to every real \(\lambda>0\) and integer \(n\ge3\). Edge-to-edge shortest routes reduce to four endpoint choices; their pointwise minimum is piecewise affine. The analytic case split yields matching upper/lower bounds. Strict derivative signs determine normalized optimality without numeric optimization.

Executed `python3 CHECK.py` using Python's exact `fractions.Fraction` arithmetic. It independently formed every edge pair of \(K_n\), maximized four endpoint routes over the two edge coordinates by enumerating pairwise affine-equality and rectangle-boundary intersections, and checked the asserted diameter for \(n=3,4,5,6\) at seven positive rational deformations each. This gave 28 complete rational configurations, plus 320 exact normalized comparisons. Result: `PASS`.

This finite checker is not a proof for infinitely many \(n\) or \(\lambda\). The universal conclusion is justified only by the quantified exhaustive edge-type argument and the derivative calculations in `RESULT.md`. An independent scientific audit has not yet been conducted.
