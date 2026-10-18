# Scientific evaluation

## Correctness — PASS

The allele-mass transformation follows from genotype Hardy–Weinberg weights, and both continuous and impulsive updates are reconstructed in full in the proof. Positivity of the Metzler semigroup supplies uniform cross-stage mixing; a two-step max contraction proves fixation. Perron comparison yields the exact exponential log rate in the heterozygote-selective regime. Under full dominance, an exact weighted quadratic drift, a reciprocal bound and stochastic-matrix oscillation contraction yield the universal sharp inverse-pulse coefficient. Symbolic and numerical checks in `verify.py` were replayed; the theorem does not rest on finite simulation.

## Originality — PASS, with historical caveat

The motivating study proves qualitative fixation and numerically explores stage-specific selection, but its inspected text gives neither the sharp stagewise log rate nor the weighted \(k^{-1}\) coefficient. Fixed-pulse spectral radius theory applies to ecology without yielding the nonlinear resistance-ratio law; classical dominant-allele slow fixation does not identify this specific stage-mixing amplitude. Related stage-structured resistance work could not be inspected in full, and an unrecognized equivalent result is a residual priority risk. Literature searching is not a proof of absolute historical uniqueness.

## Mathematical value — PASS

Resistance management depends on *how quickly* treatment selects resistance, not only whether fixation eventually occurs. This theorem exhibits a qualitative boundary between two rates and provides explicit, population-structure-sensitive coefficients. In the source's four-stage fly parameters, the coefficient ranks life stages via Perron reproductive values rather than survival or transition rates alone. Neither a routine relabeling nor a recomputation of the qualitative fixation theorem yields this sharp transition.

## Scope and closest literature

The assumptions are strictly positive mixing, positive resistant and heterozygote survival, repeated fixed pulses, genotype-independent inter-pulse dynamics, and no density feedback. The main reference is D'Ovidio Long–Adjei–Patel (2026), Theorem 5 and Section 4. Further relevant sources include Patel–De Leenheer (periodic spectral radii), Taylor (class reproductive values), and Patel et al. (2025; full text unavailable). Stochastic fixation, finite-time uniform estimates, environmental variation and degenerate pulse survival remain open.

Self-review: passed. Independent audit: not yet performed.
