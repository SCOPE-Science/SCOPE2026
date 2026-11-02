# Self-review

## Correctness — PASS

The singular diffusion is specified by a natural-scale, nonsticky origin and a fixed diffusion normalization. The \({}_0F_1\) even and odd solutions have the required initial conditions, solve the backward ODE, and yield the unique two-sided exit transform. The renewal equation reproduces the full finite-time transform. The crossing estimate \(p_{ab}\le2p_ap_b\) uses continuous paths, the strong Markov property, and exponential memorylessness. A Poisson-count sandwich correctly accommodates the last incomplete renewal interval and proves the joint independent-Gumbel limit; Taylor mapping proves the range and logistic limits. The standalone checker passed 142 checks covering exact Brownian identities, ODE residuals, finite-volume comparisons and rare-event scaling. Neither finite tests nor logs are used as an infinite proof.

## Originality — PASS (qualified best knowledge)

Frimpong's 2026 arXiv paper derives the one-sided maximum Laplace transform and Gumbel normalization, not the bilateral joint law, the opposite-excursion bound, or the range/imbalance law. Singh–Pal (2021) and Godrèche–Luck (2022) concern one-sided maxima and records. Dębicki–Hashorva–Michna (2026) examines reset Brownian supremum, infimum tail events, and two-time positions, not the observed joint bilateral extreme vector. Méndez–Masó-Puigdellosas–Campos (2022) derives interval-exit resetting formulas, so the abstract renewal step is prior theory; the new claim is the singular-diffusion closed form and joint scaling, not renewal itself. A broader marked-renewal theorem may imply the limiting independence without identical wording, and priority in less visible interval-exit literature remains a residual risk. Similarity searches cannot establish uniqueness.

## Mathematical value — PASS

A particle's explored spatial range and orientation of its furthest excursion cannot be reconstructed from the one-sided maximum law. The joint law identifies whether opposite extreme events remain dependent, gives an arbitrary-time bilateral survival transform useful for a pair of absorbing targets, and distinguishes the non-Gumbel range from a universal logistic signed imbalance. The rare-event overlap bound identifies the mechanism responsible for asymptotic independence, while the explicit singular diffusion coefficients make the statement reproducible for all finite sluggishness exponents. Its value is the structurally motivated two-sided classification, not mere reuse of the already known one-sided marginal.

## Scientific limitations and residual risk

The theorem is restricted to fixed sluggishness and reset rate, the nonsticky symmetric origin, and independently exponential resets. The two-dimensional Gumbel limit is weak convergence, not a moment claim. No independent validation or exhaustive publication-priority review has occurred. General renewal and absorbing-interval theory provide a plausible avenue for an equivalent rederivation, even though no direct matching result was found in inspected work.

Self-review: passed. Independent audit: not yet performed.
