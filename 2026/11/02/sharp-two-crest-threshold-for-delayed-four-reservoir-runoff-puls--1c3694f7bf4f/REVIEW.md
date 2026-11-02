# Scientific review: delayed four-reservoir runoff crest threshold

## Correctness — PASS

The statement specifies identical, equal-volume, instantaneous inputs and a four-stage Nash cascade with strictly positive common outflow rate. The proof differentiates the exact impulse sum and obtains a cubic polynomial for every physical time after the second arrival. Direct coefficient expansion gives \(\operatorname{Disc}P=-108\tau^2e^{2\tau}F(\tau)\). The power series for \(F'\), bounded by a strictly negative quintic, proves the unique threshold, and the signs of the cubic on the physical intervals classify all local extrema, including equality and arrival-time boundaries. The finite checker supports these steps with exact rational discriminant tests, high-precision bisection and independent derivative and root-count checks (3,491 assertions). The proof, not the finite tests, establishes the universal parameter claim. No field measurements are claimed.

## Originality — PASS within inspected evidence, with risk

Nash (1957) supplies the single-input gamma kernel but not an equal two-impulse bimodality threshold. Pattison and collaborators (2014) study the effect of tributary timing in a hydraulic case study, but the inspected material does not state a universal algebraic crest-count transition; the accepted-manuscript PDF could not be retrieved, so whole-text exclusion is not asserted. Santos and collaborators (2018) specify Nash-cascade routing and a single pulse's time to peak, without classifying the delayed sum. A related mathematical record on a **two-stage parallel-route rectangular-rainfall** hydrograph treats a different kernel and input class; neither implies the four-stage two-impulse discriminant or sharp root. Direct overlap queries for aliases including translated gamma mixtures and Erlang pulses found no comparable established statement. This is not a proof of world-first priority; hidden classical shifted-gamma-mixture analyses remain possible.

## Value — PASS

A second local discharge crest is a natural qualitative property for interpreting tributary synchronization and possible two-wave runoff. The theorem supplies a sharp criterion that is not the obvious separated single-pulse peak time: the second crest appears at \(2.958808\ldots\) dimensionless time constants, strictly before the isolated pulse's peak at three. The simple exact classification is useful for benchmark hydrograph superposition and helps distinguish model-intrinsic bimodality from numerical artefacts. It makes no assertion about economically optimal catchment intervention, peak flood stage, unequal sources or nonlinear channel processes.

## Sources and limitations

Primary inspected source: J. E. Nash, *The Form of the Instantaneous Unit Hydrograph* (1957), pp. 114–121, including derivation, examples and discussion; https://iahs.info/uploads/dms/045011.pdf. Closely relevant original study: Pattison, Lane, Hardy and Reaney (2014), https://doi.org/10.1002/2013WR014067 (metadata, indexed portions and conclusion available; accepted manuscript download inaccessible). Later full-text comparison: Santos, Thirel and Perrin (2018), https://doi.org/10.5194/gmd-11-1591-2018, particularly §§2.2–2.4. A general prior theorem for translated-gamma mixtures could subsume the result without mentioning Nash cascades. The result has not been checked by an independent auditor.

Self-review: passed. Independent audit: not yet performed.
