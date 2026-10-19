# Scientific review: cusp-order switching-time law

## Correctness — PASS
For strictly positive height and non-boundary orbits, every excursion through the upper branch resets the horizontal coordinate to \(1-\lambda x\) and is followed by at least one lower-branch step. As long as the lower branch is active, the ratio of height to the \(p\)-th horizontal power increases strictly. The resulting exact first-return equation (1) in RESULT.md is obtained by solving a strict logarithmic inequality, with floor and integer-boundary cases accounted for. Its uniformly bounded additive deviation from a linear recurrence yields a strictly positive exponential-growth coefficient, not just a ratio limit. The critical integer-ceiling argument at \(p=2\) handles resonant heights. Standalone exact-rational and floating-logarithmic stress tests returned `VERIFY_OK`; infinite conclusions follow from the proof rather than testing.

## Originality — PASS, qualified
The closest primary antecedent is Catsigeras, Guiraud, Meyroneinc and Ugalde, arXiv:1108.1501, whose Example 4.2 provides the parabolic \(p=2\) model, countable attractor and existence of repeated switching. Reading its relevant construction and proof does not reveal the logarithmic number of visits, the exponent depending on cusp order, or the eventual exact affine doubling formula. The proof here supplies a new return-time calculation with explicit parameters. General periodicity and complexity results for other piecewise contractions concern different regimes and do not imply the claim. Targeted statement searches did not establish another equivalent result; that is not proof of worldwide uniqueness. The model is source-derived and the remaining bibliographic risk is explicitly acknowledged.

## Mathematical value — PASS
For exceptional piecewise contractions, the attractor can be countably infinite despite strict contraction on each continuity piece. The frequency with which trajectories return to the switching region is therefore a natural quantitative invariant absent from an attractor description. The theorem determines its growth law for every positive-height orbit in an explicit parameter regime, shows that cusp contact order alone determines the exponential return-time factor, and identifies a stronger arithmetic rigidity for the original parabola. This is an infinite-time classification, not a renamed finite calculation or unsupported application.

## Scope and remaining risks
The result is restricted to two specified affine branches and exact power-law cusps, excluding orbits that land on the discontinuity. No wider attractor classification or invariant probability distribution is asserted. The closest comparison is an existing construction, so another treatment could have derived these return-time scales without using the same wording; independent literature verification would be useful.

Self-review: passed. Independent audit: not yet performed.
