# Scientific review

## Correctness — PASS

For any invariant finite null, the mass on a directed permutation cycle is uniform. Exactly one failure mechanism matters: \(T(gX)<T(X)\). On that event the number of comparisons exceeding or equaling the observation is binomial with identity probability \(a\); otherwise the reported p-value is one. Directed cycles have at least one non-descending edge; the maximal descent fraction is \(1-1/L\) and is achieved by a strictly descending profile with a single return edge. The full all-level criterion follows because the p-value lies on a finite grid. A binomial size-bias identity and a weak law establish the finite/infinite frontier without relying on simulation. The actual standalone rational checker passed 78,579 tests. Ties are covered because the strict-decrease event is used.

## Originality — PASS (historical-priority qualification)

Ramdas et al. (arXiv:2204.13581, Theorem 2) prove general validity after randomly re-centering the transformation draws; their theorem does not apply to the unmodified fixed-reference statistic here. Hemerik and Goeman (2018) prove validity with uniform subgroup sampling, not sharp safe biased mixture thresholds. Phipson and Smyth (2010) address appropriately randomized permutation p-values. Full-text sections covering the model, reference randomization and random group draws were compared for logical implication, not only keyword similarity. No exact simultaneous worst-case binomial calibration criterion for fixed-identity two-transform sampling was identified in the completed searches. Prior partial or less-visible literature may still contain an equivalent; external priority is not independently established.

## Value — PASS

The theorem answers a concrete inferential question: precisely when a computationally inexpensive, familiar but potentially invalid fixed-reference resampling p-value controls type-I error under a biased two-transform draw. The sharp all-level condition is directly checkable for any finite resampling budget, and the budget-reversal example shows that a procedure cannot be assumed safer merely by drawing more resamples. The longest-cycle dependence is structural, not an arbitrary parameter slice. This is not a general correction theorem, and corrected random-reference tests are preferable when arbitrary transformation distributions are needed.

## Limitations and comparison risk

The null must be invariant; the transformation sampler must be a two-atom iid identity/permutation mixture; extremal scores may be synthetic; group-order and maximal orbit length are not interchangeable for nonfree actions. Historical priority, and possible deductions from unexamined general calibration results, remain residual risks.

Self-review: passed. Independent audit: not yet performed.
