# Scientific review

## Correctness (PASS)

The binomial CDF power identity for the maximum is exact. For two underlying Bernoulli trials, the quadratic generating polynomial has nonnegative discriminant by convexity; all coefficients are positive. In dimensions at least three, coefficientwise convergence after rare-event rescaling to \(m(1+t)^n-(m-1)\) forces a nonreal root for every sufficiently small success probability. In the first failing case, the cubic discriminant identity yields the unique sharp algebraic threshold. The standalone exact-polynomial checker completed 2,615 checks, independently reconstructing the displayed discriminant factorization. Finite checks supplement rather than replace the universal proof.

## Originality (PASS on inspected evidence)

Badiella, del Castillo and Puig (2023) establish that discrete order statistics preserve ultra log-concavity; this does not imply Poisson-binomial decomposability, as the present negative-discriminant regimes demonstrate. Kim, Kim and Lee (2018) earlier proved ordinary log-concavity preservation. Tang and Tang's survey (2019), Theorem 4.1, gives the equivalence of Pólya-frequency, real-rooted, and Bernoulli-sum representations, but not the new exact family classification. Completed mathematics-record and literature searches included the corresponding aliases, rare-event description, concrete cubic polynomial and sharp parameter. No matching or dominating specific theorem was identified. The full 2018 article was not accessed, and older unindexed work remains a residual originality risk; database nonmatches are not novelty proofs.

## Value (PASS)

This is a natural complete boundary question at the interface of discrete order statistics and factorization of count laws. The all-sample-size preservation cutoff is sharp, and the first dimension beyond it admits a complete one-parameter phase diagram with an explicit algebraic constant. The results distinguish ultra log-concavity, known to be preserved, from the stronger Poisson-binomial property and identify when the latter may still be used for independent-count computations.

## Scope and verification limits

The result does not give a global parameter classification for arbitrary larger trial counts and sample sizes. The positivity neighborhood in each dimension at least three is existential. Scientific statements have undergone the review status below; they have not been independently audited. References and exact mathematical evidence are in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
