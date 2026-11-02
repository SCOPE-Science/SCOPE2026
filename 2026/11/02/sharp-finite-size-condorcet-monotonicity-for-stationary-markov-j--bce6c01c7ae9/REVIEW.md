# Review: sharp finite-size Condorcet monotonicity for stationary Markov juries

## Correctness — PASS

The proof explicitly fixes a stationary two-state Markov law with strictly positive transition probabilities. Stationary nesting of committees gives an exact gain-minus-loss decomposition. Complementing paths bijects the two pivotal events; the transition products match because both 01/10 and 00/11 transition counts coincide for the relevant paths. The stationary initial ratio is exactly \(s/t\), yielding \(J_{m+1}-J_m=(s-t)G_m/s\) for all nonnegative integers \(m\). Strict positivity follows from positive transitions, and the Markov ergodic theorem gives limits. The embedded exact-rational checker passed 1043 assertions, including separate dynamic programming and enumeration. Finite checks are supporting evidence, not the universal proof.

## Originality — PASS within the inspected evidence, provisional

The closest primary papers are Berend–Sapir (2007), Kaniovski's 2007 correlated-vote manuscript, Xia–Zhang (2009) on Markov-binomial laws, Zaigraev–Kaniovski (2012) on correlation-truncated binary trials, Peleg–Zamir (2012), and Pivato (2016). The accessible results concern random heterogeneous/dependent subcommittees, equicorrelated families, approximation bounds or asymptotic conditions. They do not establish the claimed universal Markov pivotal identity and sharp sign theorem. The full Berend–Sapir (2007) article was not accessible and remains the principal historical-priority risk; originality is not independently certified.

## Value — PASS

The question is a natural finite-size strengthening of the Condorcet jury theorem when decisions are dependent along an ordered population. A sharp and uniform answer covers both positive and negative autocorrelation and supplies an exact nonnegative pivotal-event factor measuring the finite marginal benefit of two more jurors. It clarifies a genuine difference between Markov dependence and homogeneous equicorrelation models. The result is mathematical and does not establish a real jury's statistical reliability.

## Limitations

Only stationary binary first-order chains with strictly positive transitions and consecutive odd committees are treated. Strategic votes, common informational shocks and arbitrary dependence need separate analysis. Historical priority risk remains as specified above.

Self-review: passed. Independent audit: not yet performed.
