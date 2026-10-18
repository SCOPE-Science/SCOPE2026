# Review of the two-thirds binomial log-concavity classification

## Correctness — PASS

The finding specifies an integer trial count \(n\ge1\), an interior success probability \(0<p<1\), the integer floor map, and ordinary (not ultra-) log-concavity. Its normalized masses follow directly from the binomial formula. Equation (1) is the exact first log-concavity gap. The finite cases are complete because their support has at most four occupied atoms, and the only second gap for \(n=5\) factors positively. At six trials, two necessary inequalities demand disjoint odds intervals. Above six trials, the exact discriminant of the first-gap polynomial is negative, with a strictly positive shifted quartic proving the statement for **all** larger integers. The attached checker reproduced every nonstandard identity and 1,200 additional exact-rational cases. The finite checks are supporting evidence rather than a substitute for the infinite proof.

## Originality — PASS on inspected evidence

The motivating primary work, Tang and Tang [1,2], treats the same quantized object but establishes failure of real-rootedness and ultra-log-concavity, and studies related transport and root-location questions. None of those conclusions forces **failure of ordinary log-concavity**. Relevant sections of the full available preprint (including its appendix) and the published article were inspected for the same coefficients and possible dominating inequalities. Equivalent searches using log-concavity, binomial rounding, rational fractions, grouped coefficients, and exact algebraic cutoffs found no claim equivalent to the full sharp phase diagram. Previously established properties of equal-block rounding or nearest-integer rounding address different maps. A separately published supplement was not accessible in full; its possible stronger treatment is an explicit residual risk, alongside unindexed equivalents. Absence of a search hit alone is not regarded as proof of novelty.

## Value — PASS

The object \(\lfloor2X/3\rfloor\) is singled out by an existing research problem on rational fractions of Poisson-binomial variables. Log-concavity is a natural intermediate property between unimodality and the previously studied real-rootedness/Newton conditions. Determining exactly when that intermediate property survives is not a textbook substitution: the three-, four-, and five-trial boundaries are different nontrivial algebraic windows, whereas at six trials every parameter fails. The uniform higher-trial obstruction is structural and exhaustive, not a finite census or tiny numerical gain. The fact delineates when shape-based reasoning can even begin for this canonical rational quantizer.

## Literature, scope, and remaining risks

[1] Tang and Tang, *The Poisson binomial distribution -- Old & New*, arXiv:1908.10024v1 (2019), Section 4, Appendix A. [2] Tang and Tang, *Statistical Science* 38 (2023), 108–119, DOI: 10.1214/22-STS852, Section 4. The proof does not classify heterogeneous Bernoulli sums, other rational maps, or strong-Rayleigh/real-rootedness properties. Independent external mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
