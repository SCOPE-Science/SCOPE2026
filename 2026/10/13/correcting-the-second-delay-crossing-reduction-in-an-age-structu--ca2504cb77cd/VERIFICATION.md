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

In the replacement, at each specified ω>0 write z=e^(−iωτ₂), v=e^(−iωτ₁). The root equation is (a+bz)+(c+H₁z)v=0. The modulus equality is sufficient as well as necessary when τ₁ can vary: take the unit ratio v if its denominator is nonzero, and take any phase if both complex terms vanish. The squared-modulus difference has constant |a|²+|b|²−|c|²−H₁²=K₂ and mixed coefficient a·conj(b)−cH₁=−U₂−iV₂, so both printed square-sign errors and the erroneous imaginary coefficient/phase are resolved. If R₂>0, the equation is K₂=2R₂ cos(θ+φ₂) with |K₂|<=2R₂ necessary and sufficient and endpoints allowed. If R₂=0 it is either inconsistent (K₂≠0) or puts no constraint on τ₂ (K₂=0). The numerical coefficients, interval, and printed formulas were verified in the primary PDF. With those exact decimals, 4(U₂²+V₂²)−K₂² is strictly positive while the corresponding printed expression is strictly negative, and both numerators are positive. Independent values 0.873811900596866 and 1.242308499247486 match the finding; assembling the other phase gave two positive delay pairs with tiny root residuals as a diagnostic. This is a projection of the imaginary-root locus, not a transversality or fixed-τ₁ assertion.

## originality

PASS

The generic phase construction and regular formulas as its specialization are covered, not claimed as new. The distinct supported finding is the explicit diagnosis of incompatible equations in this 2026 paper and the counterexample to the paper's own printed frequency test using its reported data. The zero-amplitude clarification repairs scope, and is not counted as an independent novelty. No inspected prior correction is equivalent to the supported distinct claim.

## value

PASS

The error changes admissibility, not merely notation: one explicit frequency inside the paper's interval is rejected by the equations printed to construct the same boundary. Correct coefficient and branch conditions are necessary to reproduce the analytic crossing locus; the exact rational sign witness makes the discrepancy independently testable. This justifies the narrow correction without claiming the broader established method or a corrected plotted stability region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
