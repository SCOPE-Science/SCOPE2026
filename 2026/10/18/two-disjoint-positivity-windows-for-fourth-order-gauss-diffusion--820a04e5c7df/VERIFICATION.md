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

The Laplacian splits into two hub/leaf-mean blocks, symmetric and antisymmetric under hub exchange, and the within-leaf deviations at eigenvalue 1. Independent Cayley–Hamilton reduction of the antisymmetric rational function reproduces all five off-diagonal orbit numerators and positive denominators. The opposite-hub leaf and opposite-leaf entries are positive at positive h. The within-hub leaf numerator has a single positive root beyond 12, since it has one sign variation and is positive at 12. The own-leaf quartic has exactly one positive root in (2√3,12) by Descartes and opposite endpoint signs. For h below 2√3 the hub–hub quartic is bounded below by H_4 when m≤4, with its negative quadratic term dominated by the two positive AM–GM pairs; above 2√3 it is positive for every m. For m≥5 the signs at 0,2,2√3 certify exactly two simple crossings, exhausting the Descartes bound. These entry checks and the strictly positive eigenvalues give the claimed closed intervals, including h=0. Substituting h=c/m, h=2√3−d/m² and h=2√3+c/m and bracketing the sign changes on either side of each limiting simple zero yields all three constants. The m=5 examples agree. Row sums stay one; the frozen parenthetical uses 'row-stochastic' only in this row-sum sense when entries can be negative.

## originality

PASS

The supported distinct result is the complete finite-step positivity law on all balanced double stars, with a sharp family cutoff at 12 vertices and separate asymptotic boundary scales. Failure of uniform positivity for the integrator is known; neither that failure nor the inspected graph analogues supplies these windows.

## value

PASS

The family gives a sharp, natural reversible graph-heat example where positivity vanishes and returns in a fourth-order completed step even while the operator stays positive definite. The full orbit classification establishes both the first family size and the usable recovered window, whose width is asymptotically distinct from the small inner displacement near 2√3. This is more than a witness against uniform positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
