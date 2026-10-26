# Self-review

## Correctness — PASS

The claim holds for every integer \(n\ge3\) and all real cyclic datasets with nonzero input-difference variation. Continuous piecewise-linearity reduces the modulus to realized three-neighbor coordinate selectors. The cyclic TV unit ball modulo constants decomposes exactly into consecutive-arc indicators. Locality limits each selected arc image to three connected components; the small-cycle counting bounds and exact strict-order witnesses prove every branch. The same proof treats ties by continuity. A separate threshold-majority/coarea argument proves individual-data contraction. Standalone exhaustive and exact-integer witness regressions passed (see VERIFICATION.md); they supplement, not replace, the universal proof.

## Originality — PASS, with residual risk

The closest classical material concerns threshold decomposition (Qiu 1994), one-input variation smoothing (Restrepo--Chacón 1994), and statistical risk under noise (Arias-Castro--Donoho 2006/2009). None of the materially inspected relevant claims implies the exact **two-input** cyclic BV modulus with dimension threshold at six. Accessible prior-record claims concern five-cycle quadratic Sobolev stability or a different nonlinear graph maximal operator; they do not imply this cyclic variation result. The Restrepo--Chacón and Gallagher--Wise full texts were not inspected, so an equivalent historical formulation remains possible. Failure to find such a formulation is not offered as a uniqueness proof.

## Mathematical value — PASS

A locally robust smoother may decrease the roughness of each input yet amplify a perturbation threefold in the same variation geometry. The exact modulus is uniform over all cycle lengths, is attained by one-arc perturbations, and first saturates on six sites. This gives a directly usable worst-case BV stability constant, including the exceptional finite-size regime, for periodic median signal processing; it is not a standalone numerical table or a routine improvement to an existing sharp constant.

## Scope and uncertainty

One pass of a scalar three-point cyclic median with uniform edge variation; not nonperiodic windows, weighted graphs, higher-order differences, or multistep median iteration. The 1994 smoothing paper could not be read in full; its abstract addresses one-data smoothing and a different finite-boundary convention, but cannot exclude stronger unpublished or unindexed comparisons.

Self-review: passed. Independent audit: not yet performed.
