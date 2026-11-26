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

An independent symbolic four-labelled-person absorption calculation, starting from masks (susceptible, infected)=(14,1) and using payoff 4 minus the susceptible count at absorption, reproduces both endpoint values and derivatives for symbolic b, the full rational G_4, the eight-degree derivative numerator, all nine transformed coefficients, and the exact positive difference 295591073/32512225144680. The quartic has one sign change and takes opposite signs at 3 and 4. The denominator of G_b'(1) is positive and the numerator is minus b times this quartic, so adding within-patch contact (decreasing epsilon from 1) has the reported signs. Also G_b'(0)>0; for b>b_* neither endpoint maximizes the continuous mean. At b=4 the substitution t=epsilon/(1-epsilon) gives exactly one coefficient sign change and opposite signs at zero and infinity. With the original positive denominator this gives exactly one strict global maximum, not just one located critical point. In the equal one-person-per-patch case the only potential secondary infection competes directly with the seed recovery, giving the strictly increasing function in the record. The row sums fix the nominal disease-free next-generation spectral radius at b throughout.

## originality

PASS

The exact finite endpoint threshold and b=4 global uniqueness remain distinct in the inspected material. The closest source contains the underlying epidemic model; its large-subpopulation weak-coupling approximation neither evaluates the finite endpoint nor supplies a global derivative sign certificate. The closest catalogue reversal has a different stochastic law and a different comparison.

## value

PASS

A fixed-radius reversal is a meaningful counterexample to a mixing monotonicity heuristic. The exact transmission threshold identifies when this reversal is possible at the endpoint; the degree-eight uniqueness certificate and minimal equal-patch population put analytic, not merely numerical, limits on the example. The gain in mean size is tiny, but its mathematical value is the strict sign and provable threshold, not a claimed practical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
