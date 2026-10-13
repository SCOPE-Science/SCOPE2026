# Review

## Correctness

PASS. The source bias-correction coefficients telescope exactly after a single nonzero gradient. This yields closed first- and second-moment tails. The published StableAdamW RMS detector is then identically zero because its numerator uses the current gradient, so the learning-rate clip is exactly inactive. Maximizing the positive-\(\varepsilon\) normalized update over finite impulse amplitudes gives the stated envelope, and its geometric factor produces the necessary-and-sufficient boundary \(\beta_1^2\le\beta_2\). The alternative momentum-numerator cap follows from an elementary but exact denominator comparison.

Risk: the unbounded statement ranges over a family of increasing finite impulse amplitudes and times; each fixed finite impulse eventually decays.

## Originality

PASS. The defining StableAdamW paper gives the current-gradient detector and explicitly reports trying a squared-momentum detector, but it does not state the zero-gradient-tail bypass or its exact impulse envelope. Classical Adam analysis already reveals the importance of \(\beta_2-\beta_1^2\), so the inequality itself is not treated as new. The surviving claim is the StableAdamW-specific clipping implication and exact comparison with the source-discussed alternative.

Residual risk: an unindexed implementation note may contain the same scalar impulse calculation.

## Value

PASS. The source introduces StableAdamW precisely to stabilize changing gradient statistics and explicitly discusses the detector numerator choice. The result supplies a sharp mathematical design boundary: the published detector cannot see stale momentum after the current signal disappears, while the source-tested alternative would cap that scalar channel. It also clarifies that the source's reported hyperparameters remain on the bounded side.

Self-review: passed. Independent audit: not yet performed.
