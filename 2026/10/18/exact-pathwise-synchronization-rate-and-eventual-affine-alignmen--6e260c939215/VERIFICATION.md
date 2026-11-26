---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The prior graph is interior, equivariant, and its current coordinate is uniform and independent of the current symbol (past dependence, or the product projection of Proposition 6.2). The two long branches have length 1−c with slope a, so ergodicity gives log D_n/n→(1−c)log a+c log b=H(c)−log 2<0. The probability of a sub-e^(−ηn) approach to the selected breakpoint is at most 2e^(−ηn). Borel–Cantelli then gives d_n/D_n→∞ for sufficiently small η, and the absence of exact kink hits makes the infimum over n strictly positive. On the resulting affine neighborhood, induction establishes exact displacement by D_n at every step. Ergodic returns to neighborhoods with radius bounded below, together with the source's simultaneous attraction, yield permanent entry for each interior orbit on one common event. For each pair strict monotonicity gives a positive prefactor and exact gaps for all n after both entries. One-sided measurability can be seen by bracketing each pair's distance above and below by rational pairs with the same exponent. Independent rational replay checked endpoints and continuity for c=1/4 and 1/3 and 30 common-branch steps for c=1/4 with final gap 268435456/205891132094649; this is an algebra check, not an infinite-time test. The submitted script was inspected but not executed.

## originality

PASS

The inspected source states qualitative simultaneous synchronization and computes the stationary graph exponent; both are credited. The new part is the sharp finite-distance exponent for all interior pairs on one event and the stronger eventual exact affine identity. This requires quantitative avoidance of the chosen breakpoint, construction of a positive random affine neighborhood, and its simultaneous use through recurrence, none supplied by the inspected qualitative or local exponential statements.

## value

PASS

This resolves an exact pathwise rate for a standard example previously analyzed through qualitative synchronization and stationary derivatives. The exact eventual identity is a structural strengthening: it specifies why every interior gap eventually uses the same cocycle, not merely a local or annealed estimate. It does not promise entrance times uniform over the open interval or cover the fixed endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
