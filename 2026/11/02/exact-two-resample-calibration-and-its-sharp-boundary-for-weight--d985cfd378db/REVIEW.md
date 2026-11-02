# Scientific review: exact two-resample calibration and first failure at three draws

## Correctness
**PASS.** Under an exchangeable null and distinct orbit statistics, the three index-collision partitions have probabilities \(1-3s_2+2s_3\), \(s_2-s_3\) per repeated-pair position and \(s_3\). The first case gives a uniform distinguished rank; involutive invariance gives a fair strict pair comparison in the second; the third forces \(P_2=1\). The resulting distribution is algebraically consistent at both support thresholds. Each unequal-to-equal transfer of transformation mass increases both rejection CDFs, with strictly positive derivatives, proving uniqueness. A fully exchangeable four-coordinate null supplies the exact three-draw counterexample. Recomputing every case with standard-library rational arithmetic yielded 5163 passing exact assertions; the derivation for arbitrary group size is analytical.

## Originality
**PASS, subject to historical priority uncertainty.** Ramdas et al. (arXiv:2204.13581, Theorems 2.2–2.3) already prove the generalized \(p\)-value's validity and exchangeable-rank representation, so no validity claim is new. Hemerik–Goeman (2018) and Phipson–Smyth (2010) establish classical exact random permutation testing and tie-aware methods, predominantly for uniform transformation sampling. The new finite power-sum distribution, sharp stochastic maximizer over arbitrary nonuniform weights in an involutive subgroup, and explicit first boundary example with three resamples were not located in the inspected primary full texts or actual research-record searches. Residual risk: historical equivalent analyses of small-sample ranks, particularly outside the inspected literature, might cover the same implication.

## Value
**PASS.** A motivating generalized-permutation reference explicitly identifies calibrating conservativeness under nonuniform transformations as worth understanding. The theorem gives an exact, statistic-independent finite-sample answer when only two random transformations are affordable, and a sharp global optimizer with an unambiguous caution: reducing null conservativeness need not optimize alternative power. The four-state witness shows exactly when that distribution-free simplification fails, preventing unjustified extrapolation to larger resampling budgets. The result is a natural boundary classification, not a generic restatement of validity.

## Limits and scope
The orbit score has no ties except repeated group draws. The main law assumes commuting involutions and iid sampling from a fixed \(q\); it is unconditional under the null and does not imply any power-optimality or general-distribution extension. The witness proves failure at three auxiliary draws, not a complete classification beyond that point. No independent audit or historical-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
