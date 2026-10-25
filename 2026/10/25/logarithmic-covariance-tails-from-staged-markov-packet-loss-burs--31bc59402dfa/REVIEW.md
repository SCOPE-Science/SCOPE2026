# Self-review

**Correctness — PASS.** A direct binomial expansion of the nilpotent loss-state shift yields the exact all-stage survival probability, and the Kalman one-step update gives uniform upper and lower multiplicative bounds on peak covariance. These imply the tail law, exact positive-moment criterion including critical divergence, and quantile order. Exact rational recurrence checks are corroborative, not substituted for proof.

**Originality — PASS (subject to explicit risks).** Huang–Dey (2006, 2007) concerns a binary loss model, Mo–Sinopoli (2012) establishes logarithmic tail decay rates for a binary Gilbert–Elliott model and notes broader methodological applicability, and Wu et al. (2015) assumes a finite bound on loss-run lengths. None of these stated findings supplies the staged, unbounded-burst two-sided logarithmic factor. The familiar phase-type Jordan-block mechanism makes this a sharply delimited mathematical application rather than a claim to invent phase-type tails. A stronger specialized theorem could still imply it and is a residual literature risk.

**Value — PASS.** The logarithmic multiplier and quantile inflation detect substantial rare-error risk differences between loss channels that share the same spectral tail exponent and moment threshold. The family covers every number of progressive failure stages rather than an unmotivated single parameter value.

**Limitations.** The theorem applies only to scalar systems, specified positive transition parameters, and prediction covariance at the first recovered measurement following a nonempty burst. It does not produce an asymptotic constant or an independent external check.

Self-review: passed. Independent audit: not yet performed.
