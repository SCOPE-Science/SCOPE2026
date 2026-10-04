# Same-model review

## Correctness

PASS. In the published fitting specialization, the source equations give
\[
\dot H=\delta I-mH,
\qquad
\dot R=\gamma I+mH.
\]
Therefore
\[
\frac{d}{dt}(H+R)=(\delta+\gamma)I.
\]
The same source defines \(I\) as non-confirmed and \(\delta I\) as the transition into the confirmed class, so a cumulative-confirmation counter satisfies
\[
\dot C=\delta I.
\]
The exact ratio follows by integration. No numerical experiment is used to prove the general claim.

## Originality

PASS. The primary full text contains both the direct natural-recovery flow and the use of \(H+R\) as cumulative confirmed, but it does not separate the corresponding counters. A 2022 stochastic follow-up reproduces the same SIHR transition semantics while studying stochastic thresholds rather than this observation map. Exact-title, DOI, direct-recovery, and cumulative-observable searches did not locate a published correction or an equivalent source-specific identity.

## Value

PASS. The affected quantity is the target of the source's parameter fit and its principal cumulative-confirmed forecast. With the printed fitted values, the discrepancy is an exact approximately \(10.0763\%\) inflation of every post-start \(H+R\) increment relative to the model-consistent confirmation counter. The result therefore changes how the calibration and forecast can be interpreted.

## Closest literature and limitations

The closest source is Jiao and Huang (2020), DOI 10.3934/math.2020431. Hou et al. (2022), DOI 10.3934/mbe.2022195, inherit the same deterministic SIHR compartment structure but do not provide this correction. He, Tang, and Rong (2020), DOI 10.3934/mbe.2020153, use a different model that fits reported transition flows separately.

The result does not refit the Hubei data. In particular, the same-trajectory conversion to \(C\approx63731.45\) is not a corrected empirical forecast.

Same-model review: passed. Independent audit: not yet performed.
