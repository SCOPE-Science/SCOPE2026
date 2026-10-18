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

The analytical derivation is given in `RESULT.md`; no external formal or independent audit has been performed.

The standalone `verify.py` integrates two independent exact-renewal expressions using 45-decimal-place mpmath arithmetic. It reports Pearson correlations for normalized distances \(z=1,2,3,5,8,12,20\), and ratios to the large-\(z\) formula. A separate numerical experiment samples two Brownian first-passage times through the exact Lévy distribution, with one common exponential-reset clock and irreversibly recorded first hits. For the preset seed and 250,000 pairs at \(z=3\), this experiment gave correlation about 0.01187 compared with the integral value 0.01229. The strict-positivity theorem does not rely on finite experiments.

The simultaneous-success integral was separately checked against its predicted Bessel/Laplace asymptotic at \(z=15,30,60\), with respective ratios approximately 0.918, 0.955, and 0.976. These finite checks do not establish the infinite-limit statement; the saddle-point bound and exact renewal identities in the proof do. The leading large-reset prediction is inaccurate at small and moderate \(z\), and no physical interactions, non-Poisson clocks or noninstantaneous reset travel time are modeled.
