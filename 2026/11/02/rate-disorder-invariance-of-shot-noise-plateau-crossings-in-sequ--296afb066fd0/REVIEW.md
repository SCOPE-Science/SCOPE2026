# Scientific review

## Correctness — PASS

For any integer \(n\ge2\) and arbitrary positive cycle rates, the renewal-process noise expression and its equivalent polynomial form are exact. The all-parameter proof explicitly constructs \(H(s)=(P(s)-P(0))/s\), proves strict Hurwitz stability by \(|P(s)|>P(0)\) on the closed right half-plane except at zero, derives a strictly increasing lifted phase with total rotation \((n-1)\pi/2\), and counts each simple intersection at positive integer multiples of \(\pi\). This establishes the sign alternation analytically. The standalone generator-resolvent checker passed 2,221 assertions and is supporting numerical evidence, not the proof.

## Originality — PASS on the inspected evidence, with stated priority risks

Brandes (arXiv:0802.2233v1), read in its relevant full-text sections, derives both the complete arbitrary-rate waiting-time transform and its exact noise relation. The work therefore does not claim the spectral formula or physical model as new. The observed gap is the sharp positive-frequency plateau-crossing count and all-rate simplicity/alternation. An earlier equal-rate counting result covers only the uniform subfamily, not arbitrary rate disorder. Classical Hurwitz/Hermite–Biehler theory supplies related root-interlacing machinery, but the investigated sources do not establish the same transport classification. The 1996 Barkai–Eisenberg–Schuss paper was inspected only at abstract level, so stronger related results in its full text remain a material priority risk. General phase-type renewal spectral theory may independently imply the same invariant.

## Mathematical value — PASS

The theorem upgrades a parameter-specific spectral shape to a universal, rate-disorder-insensitive measurement invariant for serial transport. It identifies precisely which stage counts are compatible with a measured number of finite Poisson-plateau crossings, and establishes that arbitrary heterogeneity cannot create or destroy such crossings. The invariance is nontrivial: changing rates moves all frequencies but cannot change their number or simplicity. This is useful for assessing hidden serial steps without estimating each waiting-time scale.

## Scientific and verification limitations

The result needs a single fully directed renewal cycle with positive exponential holding rates, one marked reset transition, and exact stationary spectra. It does not address branching, backward steps, marked multiple transitions or finite-data statistical estimation. Full historical-priority exclusion and independent scientific audit have not been achieved. The code is a finite, deterministic cross-check, not a proof for arbitrary rates or stages.

Self-review: passed. Independent audit: not yet performed.
