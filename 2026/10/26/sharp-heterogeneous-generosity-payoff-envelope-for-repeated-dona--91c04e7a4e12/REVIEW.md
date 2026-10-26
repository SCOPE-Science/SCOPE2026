# Scientific review

## Correctness — PASS

The donation-game pair payoff is obtained from the explicit four-state stochastic transition matrix and geometric stopping rule. The symmetrical iid expectation reduces to a positive-coefficient series of moments, with a first positive \(\delta^3\) variance contribution. Jensen's inequality and endpoint-chord inequalities prove the strict sign, exact sharp endpoint envelope and equality cases. A standalone standard-library rational program checks the pair formula independently against four-state linear solves, the sharp bounds in finite rational examples and the exact illustration. The proof covers all probability laws on a compact interval; the numerical tests are only corroborative.

## Originality — PASS

The closest source, Alistarh et al. (2023), explicitly derives the payoff kernel and stationary distribution, and compares exact heterogeneous and homogeneous average-generosity payoffs numerically. The new statement is a strict universal sign rule, a quantitative lower variance bound, convex-order monotonicity and sharp universal fixed-mean endpoint extremizers. The 2015 reactive-strategy replicator study concerns an infinite repeated game and different evolutionary dynamics. The 1992 heterogeneous TFT paper is context; only its abstract was accessible. Broad priority risk remains because the new conclusions use an existing pairwise formula and classical moment comparison tools. The checked full source passages did not present these envelope implications.

## Value — PASS

A representative-strategy substitution is often used to approximate heterogeneous populations. The result gives the direction of its error without estimating the full generosity law, produces sharp worst-case bounds from an observed mean and range, and proves that the discrepancy need not disappear at large population size. The all-distribution envelope and equality classification, not merely one example or a routine recalculation, define the contribution.

## Scope and risk

Assumptions include geometrically stopped repeated donation payoffs, common first-round cooperation probability \(1/2\), iid generosity in a bounded interval, and the stated GTFT response. No claim is made for correlated pairing, all payoff matrices or other dynamics. The source's formula is acknowledged as established; independent publication-priority audit remains necessary.

Self-review: passed. Independent audit: not yet performed.
