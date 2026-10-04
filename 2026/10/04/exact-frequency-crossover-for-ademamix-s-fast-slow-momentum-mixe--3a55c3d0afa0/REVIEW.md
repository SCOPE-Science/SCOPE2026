# Review

## Correctness

PASS. The fixed AdEMAMix momentum states are scalar EMA filters, so their harmonic gains are exact. The derivative of the slow-to-fast squared-gain ratio has a fixed sign, which proves strict monotonicity and uniqueness of the crossover. Constant and alternating gradients have exactly constant squared magnitude, so the bias-corrected Adam-style denominator is identical to the baseline and the endpoint normalized-update ratios are exact.

Risk: the full adaptive update at intermediate frequencies is not characterized because its second moment need not be constant.

## Originality

PASS. The defining AdEMAMix paper motivates the fast/slow split and supplies all recurrences and source-typical parameter values, but the inspected full text does not state the exact crossover frequency or the DC-versus-Nyquist gain contrast. The closest later theoretical paper connects AdEMAMix to accelerated stochastic-gradient methods rather than harmonic response. Focused published-record searches found no implication-equivalent result.

Residual risk: an equivalent frequency-domain calculation may exist in unindexed implementation notes.

## Value

PASS. The result quantifies AdEMAMix's central design question—when the old-gradient channel actually dominates the recent-gradient channel. At source-typical settings it places that boundary at periods of roughly \(6.3\)k to \(16.2\)k steps and simultaneously shows large DC amplification with less than one-percent extra Nyquist response. This is a direct structural interpretation of the optimizer's core hyperparameters.

Same-model review: passed. Independent audit: not yet performed.
