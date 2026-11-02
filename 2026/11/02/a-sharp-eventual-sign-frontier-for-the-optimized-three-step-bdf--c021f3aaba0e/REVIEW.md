# Mathematical review

## Correctness — PASS

The claimed scalar causal Green recurrence follows by substituting the decay test equation into the specified BDFL three-step formula and using zero prehistory. Its generating function has a cubic with strictly negative discriminant for every positive scaled step, so there is one positive real root and a nonreal pair. The exact real-root parameterization and Vieta product establish the unique modulus crossing at \(\mu=15/16\). For smaller steps, the residue of the dominant positive root is strictly positive. For larger steps, the nonreal conjugate pair dominates and contributes infinitely many coefficients of both signs. At the exact crossing, the explicitly computed oscillatory-to-positive residue amplitude exceeds one, and the phase is irrational, so both signs still recur infinitely. A rational sixth-coefficient witness establishes negative transient weights strictly below the eventual-sign threshold. The zero-frequency generating-function identity establishes finite normalized convolution gain and the asserted strict excess when a negative coefficient occurs. The analytic arguments handle all indices; finite checks are supplementary.

## Originality — PASS with historical-priority uncertainty

Jensen, Ketcheson and Lóczi, *Optimized linear multistep methods for stiff problems* (arXiv:2610.22685v1, Sections 2–4), develop the second-order BDFL methods and their A-/L-stability and truncation errors. Vatsa, Carpenter and Lockard (NASA NTRS 20100002944, especially its original BDF2OPT stability discussion) examine a related optimized scheme and its numerical stability. Neither inspected comparison reports the exact positive-real-versus-conjugate root crossover, the endpoint residue amplitude, or the negative sixth-impulse coefficient below the eventual-positivity boundary. General eventual-positivity criteria give principles rather than a value for this scheme. Classical BDF2 and higher-order BDF3 impulse thresholds belong to different coefficient recurrences and do not imply the present cutoff. A specialized earlier rational recurrence or Green-kernel analysis could remain undiscovered; publication priority is not independently settled.

## Mathematical value — PASS

The exact \(15/16\) step-size boundary is a natural stability diagnostic for the causal response of a published, optimized stiff integrator, not an arbitrary polynomial parameter slice. Its factor \(15/8\) improvement relative to the BDF2 scalar eventual-sign frontier is quantitative, but the transient negative coefficient prevents conflation of eventual positivity with monotone convolution response. The strict normalized gain greater than one makes this distinction operational for bounded forcing. These are method-specific exact structural and boundary facts, not a claim about nonlinear positive-cone dynamics or universal optimality.

## Closest literature and limitations

- T. Jensen, D. I. Ketcheson and L. Lóczi (2026), arXiv:2610.22685v1, https://arxiv.org/html/2610.22685v1.
- V. N. Vatsa, M. H. Carpenter and D. P. Lockard (2010), NASA NTRS 20100002944, https://ntrs.nasa.gov/citations/20100002944.
- A. Sootla (2019), *Properties of eventually positive linear input–output systems*, https://doi.org/10.1049/iet-cta.2018.5231.
- Z. Li (2026), *Positivity of arbitrary-order P-recursive sequences with a unique dominant root*, https://arxiv.org/abs/2605.17013.

The theorem is restricted to a scalar constant-step, zero-prehistory recurrence; it neither addresses arbitrary initial triples nor gives a sharp all-index positivity frontier. An equivalent specialized historical formula remains a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
