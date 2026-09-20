# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source paper's exact intensity reduction was checked in the bounded-mark section, including the definitions of `G_{d,rho}`, the coefficient family `alpha_{i,d}`, the fact that every correct shift differs from `log rho^d` by `o(log rho^d)`, the Poisson approximation in Proposition 3.10, and the maximum-cell mapping argument. The identity `c_{1,d}=d 2^{d-2}` gives `alpha_{1,d}=d(v_d gamma)^{2/d}`, which fixes the endpoint scale. At mark distance `y/t_{d,rho}` from the endpoint, the `i=1` exponent tends to `-2Ay`; every `i>=2` endpoint variation is smaller by `(log rho^d)^(-2(i-1)/d)`. Karamata/Laplace asymptotics then give the Gamma(shape beta, rate 2A) law.

The three-dimensional shift follows directly from equation (1.7) after applying the same endpoint Laplace asymptotic. The version-1 correction is algebraic: equation (1.7) includes `+log gamma`, while equations (3.23) and (3.24) omit it. Substitution into `G_{3,rho}` shows that the uncorrected displayed shifts normalize the expected exceedance count to `gamma`, not `1`, unless `gamma=1`. Numerical checks independently reproduce both this normalization effect and the endpoint Gamma limit.

## Originality

**PASS, to the best of our knowledge.** The recent source paper was read in HTML through its theorem statements, intensity calculations, correct-shift derivation, examples, Poisson approximation and maximum-cell corollary. It proves only unscaled convergence of higher-dimensional extreme-cell marks to the endpoint `A`; no non-degenerate endpoint rescaling or Gamma law was found, and the full-text search contains no Gamma endpoint refinement. Searches combining Poisson–Laguerre, large inradii, endpoint localization, Gamma limits, and the arXiv identifier did not locate a prior equivalent statement.

The one-dimensional exponential-tilting mechanism is not claimed as novel. Balkema--Klüppelberg--Resnick (1999, 2003) study Gamma domains of attraction for natural exponential families, and classical Karamata Laplace--Stieltjes theory supplies the regular-variation transform asymptotic. The novelty claim is restricted to transporting this endpoint structure through the large-inradius intensity and stabilization argument to obtain the refined marked Poisson limit and maximum-cell law, plus the explicit d=3 shift and the version-1 normalization correction.

Residual originality risk remains from older stochastic-geometry extreme-value literature and from general exponential-family domain-of-attraction results that might make parts of the endpoint calculation a recognizable specialization. No source located in the search states the Poisson–Laguerre refined marked limit or the Example 3.11 correction. The full texts of the 1999/2003 exponential-family papers and the 1987 regular-variation monograph were not inspected in full; their abstracts/standard theorem roles were used only to delimit prior art, not to claim absence of coverage.

## Value

**PASS.** The source theorem collapses all higher-dimensional bounded-mark extremes to a point mass at the endpoint. The refinement recovers the lost second-order mark information, supplies an explicit dimension-dependent localization rate and an independent Gamma mark for the maximal cell, and gives a systematic endpoint interpretation of lower-order correct-shift terms. The d=3 corollary generalizes the source's selected continuous example to an endpoint-tail class and also fixes a normalization error in the current v1 formulas for arbitrary intensity `gamma`.

## Limitations

The theorem assumes a bounded endpoint with `Q([A-y,A])~C y^beta`, beta>0; atoms at the endpoint form a different regime already illustrated by the source paper. No convergence rate is proved. The explicit shift expansion is only developed for d=3. A slowly varying endpoint factor is not included. The correction is version-specific to arXiv:2609.20750v1 and may disappear after author revision. Independent audit has not been performed.
