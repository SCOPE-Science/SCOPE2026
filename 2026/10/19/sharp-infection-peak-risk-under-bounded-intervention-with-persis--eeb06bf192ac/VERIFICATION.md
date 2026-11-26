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

For fixed bounded progressive controls the stopped infected solution is exponential and positive, and the integrating-factor formula for the susceptible equation gives strict positivity and S<=max(s,b/δ). This bounds the infected drift coefficient on every finite interval and rules out explosion. Dividing by the common-driver geometric Brownian path cancels both the diffusion and its Itô correction: log(I/Z) is the time integral of nonnegative residual transmission and unused treatment capacity. The identity holds simultaneously in time and does not require independence of controls and the Brownian motion. The admissible constants α=1 and η=H make the integral zero, so the stochastic order for both terminal and peak events is attained. For h>0, Brownian reflection at zero drift and endpoint exponential tilting give the stated two Gaussian contributions for the peak. The terminal law alone gives only the first. As T→∞ the tail term vanishes and the other tends to exp(-2kh/σ²); with k>0 the envelope tends to zero, so sup>=L is equivalent to finite hitting for the envelope. For arbitrary controls the common-driver hitting inclusion is enough. For L<=i hitting occurs at the initial time. For a comparison law supported in I<=L, test I>L; the conditioned envelope law on I<=L attains the resulting bound among arbitrary supported laws, not necessarily among reflecting solutions. With random nonnegative initial data the i_* bound is weighted by the initial event probability, by independence of future Brownian increments. The finite numerical check (python /workspace/branches/independent_replay.py 5) integrated the tilted reflected endpoint density, not the frozen first-passage-density integration, and reproduced .0406539545173381, .189799045911191 and .233258247884202 for the example. The frozen verifier was inspected but not run.

## originality

PASS

Pass for identifying and attaining the joint terminal/peak lower envelope in the specified controlled diffusion and its bounded-support obstruction. The Brownian tail, reflection law and conditioning identity are classical and are not independently original. The motivating paper discusses related noise specifications but its numerical model is not the specialization analyzed here; available related records do not establish the control-uniform sharp risk claim.

## value

PASS

The useful result is not the textbook Brownian formula alone. It isolates a modeling boundary for capacity objectives: even the strongest admissible policy cannot eliminate peak risk when the infected noise persists, and the same pathwise extremum turns unbounded support into a quantitative error floor for every comparison law confined below a fixed cap. Endpoint exceedance misses much of that peak risk in the given example. This is not a hard limit for finite-population epidemics, models with noise that vanishes under suppression or a particular zero-flux numerical solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
