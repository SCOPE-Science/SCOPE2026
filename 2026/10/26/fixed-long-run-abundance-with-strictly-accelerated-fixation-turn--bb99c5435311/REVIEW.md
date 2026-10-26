# Scientific review

## Correctness
PASS. Focal hypergeometric conditional probabilities give the displayed payoff-difference formula. Pascal's identities telescope each multiplier contribution to an explicitly nonnegative binomial coefficient, with a strictly positive witness at the corresponding interior count. The Fermi birth–death first-step recurrence yields both fixation probabilities and an exact common ratio, so strict two-direction monotonicity follows without a weak-selection approximation. The reduced two-state spectral calculation is elementary, and the large-population exponent follows from uniform falling-factorial convergence and maximum-term bounds. The independent direct-payoff and reverse-mutant checks in `verify.py` passed; finite checks are not substituted for the proof.

## Originality
PASS subject to ordinary historical-priority uncertainty. Wang et al. (2026) give the exact *terminal* sum cancellation and weak-selection abundance, not partial-sum kernel positivity or all-selection two-way fixation monotonicity. Hauert and McAvoy (2024) provide fixation formulas and some weak-selection endpoint-return effects for a linear return family, not the arbitrary-return strict theorem or logarithmic spectral-gap exponent. Traulsen et al. (2006) already supply the general two-strategy Fermi transition/fixation formulas, and Fudenberg and Imhof (2006) establish rare-mutation reduction. Thus the exact stationary logistic identity is an acknowledged consequence of existing tools, not separately novel; the contribution is the positive *every-partial-sum* kernel and its all-intensity dynamical consequences. Scientific search comparisons and their limitations are recorded in AUDIT.json.

## Mathematical value
PASS. The analysis proves that a family of ecological games with indistinguishable long-run homogeneous-state frequencies can have arbitrarily different substitution rates, exponentially separated in the population size for every fixed group size at least three. The strict positivity of an otherwise sign-indefinite payoff perturbation after cumulative sampling is the structural mechanism. This is motivated by the specific finite- versus weak-selection gap in recent work and distinguishes stationary evolutionary success from temporal responsiveness; it is not merely a reformulation of the terminal cancellation.

## Sources and limitations
Wang et al., arXiv:2607.16809 (Sections 2, Appendix B); Hauert and McAvoy, DOI 10.1098/rsif.2024.0334 (Sections 4.1–4.2); Traulsen et al., arXiv:q-bio/0609020 (Fermi transitions and fixation); Fudenberg and Imhof, DOI 10.1016/j.jet.2005.04.006 (rare-mutation reduction). The last source was checked at abstract level. An earlier equivalence under different notation cannot be conclusively excluded. The two-state spectral gap is not the absorption-time gap of the full process, and independent scientific review has not occurred.

Self-review: passed. Independent audit: not yet performed.
