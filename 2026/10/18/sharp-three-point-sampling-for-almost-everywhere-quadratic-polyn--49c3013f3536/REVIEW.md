# Scientific review: sharp three-point quadratic phase retrieval

## Correctness — PASS
The proof obtains the exact four independent cyclic autocorrelation moments from the six squared magnitudes. The derivative moments force two and only two possible positive magnitudes for the quadratic coefficient; the mixed moment then determines the constant coefficient by an invertible real-linear equation. For fixed nondegenerate middle and quadratic coefficients, the false branch's energy mismatch is a nonzero real quadratic polynomial in the constant coefficient, with nonzero value at zero. Fubini's theorem yields a measure-zero exceptional locus. The maximal-rank/constant-rank argument correctly excludes generic injectivity with fewer than three roots per channel. The integer counterexample was recomputed independently of floating-point tolerances.

## Originality — PASS with residual search limits
The originating 2022 article proves *all-signal* recovery using five roots per channel and supplies an all-signal counterexample using four, while explicitly asking when smaller meshes give almost-everywhere recovery. Neither statement implies three-point generic recovery. An earlier general almost-everywhere phase-retrieval theorem treats generic measurement arrays, not this fixed derivative-weighted Fourier array. Searches for the exact three-root quadratic case, equivalent masked-DFT formulations, and two-branch inversions did not identify a published formula that implies this result. A negative search is not proof against unindexed or unpublished coverage; that remains a genuine residual originality risk.

## Mathematical value — PASS
This settles the smallest nontrivial quadratic instance of an explicit published sampling-rate question at its sharp mesh size. The three-root scheme has only six intensity observations, versus ten for the cited uniform-recovery construction in the same dimension. Its two-branch inversion and exact nongeneric ambiguity show what is gained and lost by passing from uniform to almost-everywhere identification; neither is merely a rearrangement of a known generic-measurement counting bound.

## Scope and limitations
The result concerns degree at most two at equally spaced roots. Singular coefficient strata, higher degrees, arbitrary meshes, and stability constants are not classified. The review is internal to the reported mathematical argument and its reproducibility checks; no independent audit was carried out.

Self-review: passed. Independent audit: not yet performed.
