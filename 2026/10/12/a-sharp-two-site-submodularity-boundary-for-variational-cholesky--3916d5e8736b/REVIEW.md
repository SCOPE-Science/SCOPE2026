# Scientific review

## Correctness — PASS

The stated scope has \(0<r<1\), fixed unit noise, exact Nyström subsets and \(a\ge0\). Explicit rank-one and full-rank determinants and inverses yield the claimed singleton/full gains and the precise defect. The scalar function defining the threshold is strictly positive for all permitted correlations by direct differentiation. Taylor coefficients prove weak-correlation failure at every fixed nonzero observation amplitude. The ordered large-amplitude/high-correlation limit proves the vanishing uniform weak-submodularity ratio, and the VFE directional derivative verifies monotonicity independently of submodularity. The standalone rational reconstruction program successfully checked the algebra, but finite tests are not the proof.

## Originality — PASS, with residual risk

The full publicly available text of Schaub and Zaspel (arXiv:2606.01821v1), its discussion of Cao et al., Cao et al.'s primary text (arXiv:1310.6007), and Titsias's original paper were compared at the statement level. The earlier papers develop the general VFE functional, exact pivot increments, and monotonicity; they do not assert the exact two-site submodularity boundary, failure for arbitrarily weak positive correlation at fixed nonzero observations, or the zero-infimum uniform weak-submodularity ratio. Published mathematical-results searches for these precise assertions and equivalent terminology did not identify direct coverage. The formulas are elementary consequences of prior VFE definitions, so unindexed prior two-site calculations remain a genuine residual risk; absence of a search hit is not a proof of global novelty.

## Value — PASS

The exact phase boundary addresses a motivated structural question for greedy data-aware kernel pivoting: monotone one-step gains need not admit the standard diminishing-returns or positive uniform weak-submodularity premise for greedy guarantees. A minimal two-site complete classification, a well-conditioned weak-correlation failure mechanism, and the scale-free zero-infimum boundary explain a limitation of such guarantees without asserting an algorithmic lower bound. This is more than a sign-check of a single arbitrary parameter point: it identifies the full natural threshold and its limiting mechanisms.

## Closest work and limitations

Schaub–Zaspel (2026) is the direct numerical-linear-algebra source, with Cao et al. (2013) and Titsias (2009) providing the same objective and precursor greedy formulas. Mutual-information submodularity is distinct. The result is confined to two sites with positive correlation, fixed unit noise and antipodal real outputs. It supplies neither multistep greedy performance bounds nor finite-precision conclusions; an equivalent unindexed primary treatment remains possible.

Self-review: passed. Independent audit: not yet performed.
