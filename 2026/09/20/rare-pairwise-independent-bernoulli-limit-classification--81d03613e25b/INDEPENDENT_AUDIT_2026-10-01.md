# Independent audit — 2026-10-01

## Record

**Weak-limit classification for rare pairwise-independent Bernoulli sums**

Final claim: Under \(\max_i p_{n,i}\to0\) and \(\sum_i p_{n,i}\to\lambda\in(0,\infty)\), the weak limits of pairwise-independent Bernoulli sums are exactly the nonnegative-integer laws with mean \(\lambda\) and variance at most \(\lambda\); every such law is realizable by exchangeable rows with identical marginals \(\lambda/n\).

Disposition: **PASSED**

## Correctness — PASS

Necessity follows from the exact first two moments, uniform integrability of the sums, and lower semicontinuity of the second moment. For sufficiency, exchangeability reduces pairwise independence to two exact factorial-moment constraints on the count. The finite-support perturbations preserve mass and mean and adjust the second factorial moment by exactly the required amount; tail replacement by adjacent integers lowers variance, and a slow diagonal choice yields every admissible target. The explicit \(\lambda=1\) example also checks directly.

## Originality — PASS

The finite pairwise-independent Bernoulli literature characterizes or bounds probabilities from the first two moments, and Gupta–Hu–Kehne–Levin exhibit specific non-Poisson symmetric limits. Those results supply ingredients and examples but do not imply the iff weak-limit classification or realization of every admissible law. Targeted Resultary and primary-literature searches did not locate that complete asymptotic classification.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Source inspections distinguish material actually read from inaccessible full text.

## Scientific value — PASS

This is a natural complete boundary theorem for the law of small numbers under exactly pairwise independence. It pinpoints the only surviving weak-limit constraints and explains the escape of second-moment mass. The result is structurally useful for limited-independence models and is more than an isolated counterexample.

## Checked scientific sources

- A. K. Ramachandra and K. Natarajan, Tight Probability Bounds with Pairwise Independence, SIAM J. Discrete Math. 37 (2023), DOI:10.1137/21M1408294; arXiv:2006.00516.
- A. Gupta, J. Hu, G. Kehne and R. Levin, Pairwise-Independent Contention Resolution, arXiv:2406.15876; Math. Programming 216 (2026).
- E. Boros and A. Prékopa, Closed Form Two-Sided Bounds for Probabilities that At Least r and Exactly r Out of n Events Occur, Math. Oper. Res. 14 (1989).
- Resultary semantic search for rare pairwise-independent Bernoulli weak limits, exchangeability, and factorial moments.

## Residual risks

- Older discrete-moment, finite-exchangeability, or orthogonal-array literature may contain an equivalent asymptotic moment-realization theorem under different language.

## Verification boundary

The audit reconstructed the mathematical argument from the record and performed fresh logical or algebraic checks where needed. Existing package logs were treated only as reproducibility evidence. No formal proof-assistant verification or expert attestation is asserted.
