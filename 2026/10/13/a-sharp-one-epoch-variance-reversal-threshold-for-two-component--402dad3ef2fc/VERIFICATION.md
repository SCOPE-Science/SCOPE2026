---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Recomputed each two-update affine endpoint from T_i(x)=(1−ηλ_i)x∓ηc, namely (1,2):ηc(ηλ2), (2,1):−ηc(ηλ1), (1,1):−ηc(2−ηλ1), (2,2):ηc(2−ηλ2). RR averages mixed pair squares, IID averages all four pair squares; subtraction is η²c²[η(λ1+λ2)−2]. Objective gap is positive factor (λ1+λ2)/4 of x². Setting λi=L witnesses sharp eta=1/L despite each map contracting for eta<2/L. With equal λ the common deterministic r²x0 cancels and both noises mean-zero; difference of variances is 2η²c²(ηL−1) for arbitrary x0. Rational witness λ=3/2,η=c=1 gives RR 9/4,IID 5/4. Algebra covers all parameters; inspected finite-rational verifier source 1000+500 tests as corroboration.

## originality

PASS

General RR non-dominance is known (De Sa 2020), credited. Liu 2026 proves worst-case averaged-iterate rate dominance, not pathwise or single-instance last iterate dominance; no contradiction. Domingo-Enrich stationary spectral-noise variance is a different horizon. No same-model exact two-step scalar frontier found in published searches; near-elementary identity could appear implicitly in extended Liu appendix or unindexed stochastic-gradient folklore. The relevant complete Liu paper could not be independently retrieved; this risk is material but insufficient alone to fail O.

## value

PASS

The natural smallest non-interpolating strongly convex finite-sum model has an exact RR/IID crossover inside individually stable step sizes. Its sharp uniform cutoff is half the per-component stability ceiling and equal-curvature reversal survives every start. This clarifies the precise scope of rate-dominance claims and supplies a meaningful algorithm-comparison boundary even though its algebra uses only four trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
