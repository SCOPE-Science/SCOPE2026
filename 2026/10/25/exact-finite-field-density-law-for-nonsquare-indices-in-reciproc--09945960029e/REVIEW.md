# Mathematical review

## Correctness — PASS

The reduced recurrence and square-failure criterion follow by explicit coprime numerator/denominator arithmetic. The three local valuation cases account for every initial positive integer and every prime dividing \(h\). The finite-state first-zero hitting criterion is equivalent to divisibility of a reduced numerator at exactly one positive iterate; Chinese remaindering enumerates all initial residue classes with no omitted case. Idempotent monomials record a union of indices rather than falsely adding collisions. The direct residue verifier reproduces the detailed \(h=145\) census. Infinite applicability is established by the local valuation and CRT proof, not by finite experiments.

## Originality — PASS, with residual risk

The source's Theorem B gives an upper bound on the number of failures and its Remark 4.2 describes the prime-by-prime obstruction, but Section 7 explicitly asks for exact proportions. The finite idempotent product computes the full law, including distributions with two or more *distinct* failures and coincidences at one index. Known prime-restricted zero/one-failure classifications do not imply this unrestricted theorem or its exact \(h=145\) count. Arboreal Galois-group literature concerns different invariants. The related companion preprint has not been inspected and an equivalent table could exist elsewhere; neither is asserted absent.

## Mathematical value — PASS

This determines a natural limiting statistic explicitly posed as an open computation in the motivating work, across all prime-power parameters \(h\). It supplies a finite decision procedure for every failure pattern and proves the period \(h\operatorname{rad}(h)\). The collision case \(h=145\) demonstrates why a naïve independent-prime Bernoulli count fails: twelve classes have simultaneous prime obstructions but only one bad index. This is materially different from the established per-prime upper bound.

## Literature and scope

Closest source: Matijasevick, Rodríguez and Salazar, arXiv:2610.00765v1, especially Proposition 4.1, Remark 4.2, and Question 1 in Section 7. Background: Jones–Manes, arXiv:1101.4339, on arboreal Galois representations. The companion Matijasevick preprint cited in the first paper was not accessible in full. The statement is fixed-parameter and provides no uniform error as \(h\) grows.

Self-review: passed. Independent audit: not yet performed.
