# Scientific review: exact high-start Zipf-disaster mixing

## Correctness — PASS

The invariant law follows by one-step flux balance. The proof gives a direct sign certificate for the renewal coefficients, including the inequality \(u_m\ge\zeta(\beta)^{-1}\), by an induction on the reciprocal of a log-convex power series. This yields the exact zero-start total-variation tail and an explicit bound on delayed-renewal contamination. Under the stated sufficient inequality, every ordinary reachable state has less mass than under stationarity, while the no-reset state has more. The signed positive and negative maximizers are therefore precisely the singleton and its complement. The strict finite condition holds eventually on every time window proportional to the initial state. The mixing-time ceiling follows from this exact finite identity and Markov contraction. A union bound for excursion maxima proves negligible macroscopic returns after the first disaster, giving the Skorokhod limit. A standalone finite checker reproduces 10,523 assertions; no infinite statement is inferred from those tests.

## Originality — PASS, with historical-priority qualification

Huillet (arXiv:2610.29974v1, Section 3) establishes the transition mechanism, excursion distribution and stationary Zipf law but does not give a high-start total-variation maximizer, a finite-horizon strict comparison against stationarity, a state-dependent mixing threshold or this process limit. Chevyrev–Korepanov (arXiv:2501.10169v1, Theorem 2.8 and Lemma 2.9) already establish substantial stronger *zero-start* renewal comparison theory; our use of the exact zero-start tail is auxiliary, not a novelty claim. Their temporal-shift results do not imply the asserted **high-initial-state** sign decomposition without the delayed-renewal comparison proved here. Goncalves–Huillet (arXiv:2101.03853v1) study other total-disaster probabilities and general first-return behavior, whereas Fontes–Schinazi (arXiv:1907.05357v1) study an absorbing model with partial binomial catastrophes and changing model parameters. Targeted mathematical-record and published-literature searches found no directly covering theorem. Possible differently worded earlier delayed-renewal results remain a priority risk; this assessment is not a global novelty certificate.

## Mathematical value — PASS

The exact event attaining total variation is an unusually strong structural statement: on each fixed initial-height-scale window, the entire positive discrepancy relative to equilibrium sits on one surviving high-state atom. This gives an exact integer mixing-time law, not merely a polynomial upper bound or an asymptotic exponent, even when the excursion variance is infinite. The path limit explains this sharp mixing profile through a single Pareto-timed catastrophe followed by negligible visible regrowth. High-initial-state relaxation is natural for the reliability/population model, and its initial-height dependence prevents uniform ergodicity. The finding does not merely restate the known renewal law or stationary Zipf distribution.

## Scope and outstanding limitations

Fixed \(\\(\beta>1\)\) and each bounded linear-time horizon only; the precise event need not remain optimal on arbitrarily longer time scales. No conclusion for null recurrence, varying exponents or all-start uniform rates. No independent proof audit was performed. Older renewal-aging sources could contain general implications requiring broader historical comparison.

Self-review: passed. Independent audit: not yet performed.
