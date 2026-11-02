# Self-review

## Correctness — PASS

For every payoff \(u>1\), the small group's size-two binomial response is \(2p-p^2\). When the other group's optimal response requires one observation, the population drift is positive. When it requires exactly two, the odds-coordinate drift is a polynomial with constant \(2\alpha-1\) and strictly positive higher coefficients. It has either no interior root or one repelling root. When at least three observations are required, an explicit rational share \(\alpha=1/2+1/(128\binom{k}{3}^2)\) produces a strictly positive drift near zero and one but a negative drift at \(p=1/(4\binom{k}{3})\); hence an attracting interior equilibrium exists. The threshold is precisely \(k>2(u+1)\). The standalone exact verifier passed 227 coefficient, payoff-boundary and witness tests. Finite tests are supplemental to the all-size symbolic proof.

## Originality — PASS, with residual priority uncertainty

Arigapudi, Heller and Schreiber, *Heterogeneous Noise and Stable Miscoordination* (arXiv:2305.10301; originally 2023), already prove that sufficiently large sample-size heterogeneity can stabilize miscoordination, and that homogeneous sampling does not. Their 2025 full-text Theorem 2, Section 2.6 and Appendix A.6 do not identify the smallest admissible larger sample size at each payoff, or a sharp closed-form staircase including all rational tie points. A narrower known five-observation boundary in the first payoff cell is credited as a special case rather than a separately new result. The present theorem covers every \(u>1\) and supplies a uniform all-degree obstruction and constructive rational witness, not merely a further numerical cutoff. Source searches did not locate a broader published implication; unindexed or inaccessible specialist work remains possible.

## Mathematical value — PASS

The source's qualitative insight—that better-informed agents can stabilize miscoordination—raises the direct economic question of the least required information. This theorem gives a sharp observation-budget rule for the entire payoff range, identifies discontinuous changes at exact best-response ties, and supplies a reusable positivity argument for binomial response mixtures. It establishes a structural infinite family of thresholds, not an arbitrary fixed payoff instance, while retaining the source's dynamics and behavioral assumptions.

## Scope and scientific limits

The finding concerns a two-point sample-size mixture, with the smaller size fixed to two, and local attracting interior states of the deterministic one-population ODE. It does not assert global convergence or extend to arbitrary mixture supports. The source comparison includes an accessible complete version of the most relevant manuscript but does not eliminate unindexed prior work. Independent external validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
