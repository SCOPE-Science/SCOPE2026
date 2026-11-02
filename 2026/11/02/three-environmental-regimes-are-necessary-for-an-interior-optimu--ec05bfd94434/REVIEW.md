# Scientific review: sharp regime-count boundary for stationary patch occupancy

## Correctness — PASS
Joint stationary balance for two regimes gives a rational-linear function of the common environmental switching-speed multiplier, with derivative of fixed sign for all positive local colonization, extinction and switching base rates. Symmetric all-to-all environmental transitions lead to a weighted-ratio stationary law in any number of regimes. Substitution of the three explicit positive rate pairs produces a strictly increasing then strictly decreasing occupancy law, attaining the unique exact positive finite maximum. The 319 exact joint-generator comparisons and symbolic verification in `verify.py` support algebraic reproducibility; they are not the universal proof.

## Originality — PASS (historical priority provisional)
MacKenzie et al. (2003) established dynamic colonization–extinction occupancy. Yackulic et al. (2015, inspected full text) treats variation with fixed environmental identity; Fidino et al. (2018, inspected full text) derives general multistate occupancy and stationary probabilities, without a sharp classification of a common autonomous environmental switching-speed parameter. Smith (2017) considers stochastic-environment metapopulations, but only its abstract was accessible. Targeted research-record checks compared environmental Markov modulation, monotone two-regime occupancy and possible three-regime interior optima; closest retrieved results treated different objects such as stationary alternating-renewal time laws or species-count covariances. Ordinary Markov-chain inversion can derive each finite example but does not itself state the structural two-versus-three sharpness. An inaccessible historical source or broader stochastic-switching theorem may establish equivalent coverage; no exhaustive-priority claim is made.

## Mathematical value — PASS
The result isolates a meaningful minimum complexity for nonmonotonic response to frequency of environmental change, beyond endpoint averaging. The three-regime example has identical infinitely-slow and infinitely-fast occupancy limits yet a provably better intermediate switching speed with a unique exact optimum. This directly answers a natural stochastic ecological modeling question and separates two-regime rigidity from genuinely three-regime effects.

## Limitations and interpretation
The environment is autonomous and finite-state; colonization/extinction are Markovian in one binary patch; only environmental switching rates are scaled. The symmetric three-regime witness is a construction rather than an empirical calibration. The theorem does not predict arbitrary ecological or metapopulation behavior. Primary access and historical priority qualifications appear in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
