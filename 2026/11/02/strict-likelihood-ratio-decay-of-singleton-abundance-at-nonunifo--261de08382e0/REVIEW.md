# Scientific review

## Correctness — PASS

Independent Poisson splitting yields the stated last-arrival density and winner weights. Conditioning the other counts on being positive produces independent singleton Bernoulli indicators. The mixture over last-arrival types is exactly the size-biased Poisson-binomial pmf, including all boundary terms. The nonstandard likelihood-ratio step is justified by the coordinatewise formula and log-concavity of a Poisson-binomial distribution; every parameter decreases strictly with elapsed time. Strict negative covariance follows from conditional monotonicity and positivity of the completion-time density. An independent finite-state rational recursion agrees with numerical Poissonized integration, and the standalone checker reports 16,538 passed assertions. Infinite-size correctness rests on the analytic proof, not the tests.

## Originality — PASS, with historical-priority risk

The classical equal-probability joint law in Myers–Wilf (2003), equation (44), does not cover unequal probabilities. The general-probability Poissonized expectation calculations in Adler–Oren–Ross (2003), Section 3, do not assert a time-conditioned full distribution or likelihood-ratio order. Long (2026) proves a different monotonicity result across the number of types and general nonuniform expectations; the inspected relevant sections do not give the claim. Published semantic searches of conditional singleton laws, parameterized size-biased Poisson-binomial sums and likelihood-ratio order did not reveal a statement implying this nonuniform theorem. A more general older conditional point-process theorem could still contain an equivalent specialization; publication priority is not certified.

## Value — PASS

Completion time and leftover singletons are two directly interpretable diagnostics of collection efficiency. An all-parameter likelihood-ratio comparison is substantially stronger than a mean or covariance identity, and applies to arbitrary unequal types rather than a balanced case; it controls every increasing utility or tail threshold and fixes a structural negative dependence mechanism. The exact conditional pgf permits direct finite-sample calculations for nonuniform collection schemes.

## Scientific boundaries

The order concerns the continuous Poissonized time and is not asserted for discrete completion draw count; no uniform quantitative covariance margin is claimed. Finite numerical assertions are reproducibility checks rather than an infinite proof. Historical-priority uncertainty remains despite direct comparison with highly relevant primary full text.

Self-review: passed. Independent audit: not yet performed.
