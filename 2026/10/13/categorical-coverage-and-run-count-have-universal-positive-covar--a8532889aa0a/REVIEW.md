# Review
## Correctness
PASS. The proof reduces the mixed statistic to the covariance of a symbol-presence indicator with one adjacent-change indicator. The relevant joint probability is computed exactly from the iid law. Summing over symbols yields the displayed finite covariance. Strict positivity follows from a monotone tilted-moment ratio whose one-step decrease is exactly controlled by Cauchy--Schwarz. Exact weighted enumeration over nonuniform rational probability vectors independently agrees with the identity and its uniform specialization.

## Originality
PASS, with a specific older generating-function risk. The inspected run literature treats multi-state run and pattern distributions but not categorical coverage. The inspected occupancy literature treats distinct-symbol and occupancy-frequency statistics but not adjacent transitions or run count. Exact-form and alias searches did not locate the covariance or its universal positive-sign theorem.

Prior results on fixed-composition binary transition covariances do not involve random coverage, and prior results on occupancy richness versus occupancy-frequency counts discard order entirely. Neither statement implies the present iid mixed covariance.

## Value
PASS. Coverage and run count are canonical global and local summaries of a categorical sequence. The theorem gives an exact arbitrary-probability dependence law and a universal sign mechanism rather than a single numerical case. The uniform conditional identity gives a direct interpretation: one forced local switch raises expected global richness by an explicit amount.

## Closest literature and limitations
The closest run source is Johnson and Fu's multi-state run and pattern framework. The closest occupancy source is Ben-Hamou, Boucheron, and Ohannessian's iid occupancy-count framework. The theorem assumes iid sampling and does not extend automatically to Markov or fixed-composition sequences. It is a covariance result, not a full joint-distribution or general association theorem.

Self-review: passed. Independent audit: not yet performed.
