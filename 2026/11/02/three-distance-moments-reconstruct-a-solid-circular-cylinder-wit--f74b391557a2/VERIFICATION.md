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

Volume-uniform sampling factorizes into a disk and an interval. Independently averaging the squared disk difference using complex coordinates gives its j-th moment as R^(2j) times sum_i binom(j,i)^2/[(i+1)(j-i+1)]; the triangular interval law gives 2H^(2j)/[(2j+1)(2j+2)]. Exact rational expansion and coefficient comparison reproduced the moment polynomials, elimination identity, denominator minimum and both rational witness values. On 0<v/s<1 the normalized second moment is 45/31+(31/15)(v/s−10/31)^2; at 45/31 one preimage is attained, at 5/3 the second preimage is excluded by v=0, and 12/5 is not attained. The elimination identity makes m3 affine in v on each two-moment fiber with nonzero slope 3Q/13454. This proves the inverse and the sharp branch separation (the infimum is approached as the two distinct roots coalesce). Necessity is for the first two consecutive even moments; this is not a noisy-data bound or a claim about every choice of two statistics. RESULT.md §§1–4 and VERIFICATION.md were checked; the packaged simulations are corroboration only.

## originality

PASS

The supported distinction is the inverse classification for filled cylinders: exact feasible region, two-to-one interval, globally defined inverse, and sharp resolution on a two-moment fiber. The forward law is credited to Kellerer. The closest same-day record treats the lateral surface and has a different moment map and fold; this comparison does not assume an ordering of same-day records. No inspected source was found to cover the supported distinction.

## value

PASS

Two parameters do not guarantee identification by the first two moments. The exact ambiguity interval and the strict, optimally scaled third-observation separation resolve that issue for a natural sampling model; a forward distribution or an inverse for a different surface law does not give these thresholds. The useful claim is the sharp inverse and ambiguity characterization, not the elementary product decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
