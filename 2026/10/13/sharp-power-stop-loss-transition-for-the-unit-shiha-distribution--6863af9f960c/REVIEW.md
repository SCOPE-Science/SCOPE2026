# Scientific review: sharp power stop-loss transition for unit Shiha laws

## Correctness — PASS
The claim fixes positive \(\omega\), orders two strictly positive \(\eta\)-parameters, and allows every positive power \(r\). The density and CDF follow from the published formula. Strict concavity of the one-crossing function gives exactly one interior crossing; exact integration gives the power-moment gap with sign change only at \(2\omega\). Stop-loss differentiation and endpoint signs prove the complete phase diagram, including uniqueness and parameter invariance of the deductible reversal. The critical-power mean, convex ordering, and exact variance envelope follow algebraically. The standalone checker passed 1,850 finite tests; the infinite-parameter statements rest on the displayed proof, not computation.

## Originality — PASS, with residual risk
The relevant sections and references of arXiv:2602.04400v1 and its original-lifetime antecedent arXiv:2602.02875v1 were examined. Both provide formulas; the unit paper itself (including its later journal version) already observes a qualitative quantile reversal near rank \(0.57\), while its earlier lifetime antecedent notes a similar reversal near rank \(0.43\). Neither inspected result establishes the complete powered stop-loss/convex-order classification, the exact universal deductible reversal, or the critical-power variance envelope as an ordering theorem. Classical stochastic-order equivalences are used as established results. Searches of mathematical research records and the literature found no stronger result covering this precise comparison, but coverage cannot be ruled out for unindexed results or material not fully accessible. The source formulas, the prior qualitative unit and lifetime quantile reversals, and general stop-loss theory are not claimed as novel.

## Value — PASS
This is an exact all-parameters classification for a model proposed for reliability and unit-valued risk data. It states which power transformations guarantee uniformly lower excess-loss premiums at all deductibles, and proves that weaker powers cause a unique deductible-dependent preference reversal rather than simply a change in a single moment. The boundary yields a natural, entire mean-preserving contraction family; its universal variance envelope quantifies dispersion reduction. These are motivated structural decisions, not merely a parameter substitution or an isolated numerical gain.

## Scope and uncertainty
No order statement is made when both shape parameters vary. Neither a published priority search nor finite numerical diagnostics establishes independent validation or universal novelty. Inference and real-data performance were not re-evaluated.

Self-review: passed. Independent audit: not yet performed.
