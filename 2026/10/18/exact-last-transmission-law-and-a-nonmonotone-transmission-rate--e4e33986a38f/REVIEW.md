# Review of the last-new-transmission law

## Correctness

**PASS.** The local rates imply a first-infection clock of rate \(2\lambda\), an active one-sided tip with forward-infection rate \(\lambda\) and independent stifling rate \(1\), and a competing pair of clocks at the source for starting the opposite side. The time of the last successful transmission on each side, measured from the first infection, has CDF \(1-ae^{-t}\), including its atom at zero. The two side offsets are independent by disjoint local Poisson marks; their maximum, convolved with the first-infection clock, proves the CDF, transform and mean. Direct differentiation yields a cubic with one positive root. An independently implemented sitewise Gillespie process and exact-rational checks passed. The simulations do not prove the infinite-system statement.

## Originality

**PASS, qualified.** The October 2026 motivating paper establishes extinction and geometric **final spatial reach**, but does not state or imply elapsed last-new-transmission time from the range-only data. The closely related 2025/2026 cycle-paper full text concerns finite-network final counts and discrete transition counts rather than the elapsed time of the last new infection. The 2017 small-world paper uses different topology and final reach. The 2019 complete-network paper treats dissemination time to all nodes rather than this no-forgetting infinite-line stopping observable. Relevant publication/database searches and comparisons found no stronger covering theorem. General exponential-killing identities are old and are explicitly acknowledged; priority risk remains if an unlocated graphical temporal lemma directly covers the two-front assembly.

## Mathematical value

**PASS.** The last newly informed site's physical time is a natural temporal counterpart to the cited model's exact final spatial range. Its exact distribution and Laplace transform permit direct temporal predictions, and its uniquely nonmonotone expected duration reveals a genuine transmission-rate tradeoff: sufficiently rapid propagation spreads farther yet extends the expected window of *new* transmissions. This is neither the final-size result nor a generic reparameterization and does not require a claim about ultimate stifling time.

## Closest literature and boundaries

See RESULT.md References 1–4. Scientific scope excludes forgetting, finite cycles, long-range connections, and the terminal stifling time. The 2019 complete-network abstract was accessible but its full original article was not inspected; that is a residual priority risk, mitigated by its different network and time-to-all-vertices objective.

Self-review: passed. Independent audit: not yet performed.
