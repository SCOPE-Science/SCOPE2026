# Review

## Correctness

PASS. The sufficient direction is a complete geometric-subsequence Borel--Cantelli argument. Finite \(\mathbb E\log(1+T)\) makes the exceedance probabilities summable on every geometric subsequence; bounded upward growth then fills the gaps, and a countable family of ratios tending to one forces \(\tau_n/n\to0\). The converse uses independent dyadic activation blocks with probabilities \(q_k=\Pr(T\ge2^k-1)\). Infinite logarithmic moment is exactly enough for \(\sum_kq_k=\infty\), pointwise stochastic domination holds throughout every block, and active block endpoints force limiting age ratio \(1/2\). The harmonic-window corollary follows from a direct logarithmic bound.

## Originality

PASS. The closest inspected source and its 2023 predecessor assume a finite positive moment of the common delay dominator and obtain sublinear age as an intermediate lemma. The 2024 dissertation treatment inspected for comparison retains that positive-moment hypothesis. The new claim weakens this to a finite logarithmic moment and supplies a matching universal converse, so it is not a restatement or parameter substitution of the cited results. Focused searches for logarithmic-moment, age-of-information, unbounded-delay, and stochastic-approximation formulations did not reveal an implication-equivalent published theorem. The 2022 time-varying-network paper has a materially different eventual-delivery assumption.

## Value

PASS. The source paper is explicitly about heavy-tailed information age and currently requires some positive power moment. The logarithmic criterion strictly enlarges the admissible tail class to distributions with no positive moments, and the converse identifies an exact structural boundary rather than merely another sufficient condition. The result also pinpoints the precise probabilistic input needed by the harmonic stale-window estimate.

## Closest literature and limitations

The primary comparison is Redder, Ramaswamy and Karl, arXiv:2609.27499v1. Their finite-positive-moment hypothesis is stronger, while the bounded one-step age growth used here is already part of their age-process mechanism. Ramaswamy, Redder and Quevedo, arXiv:2305.07091v1, gives the earlier positive-moment version. The 2024 dissertation DOI 10.17619/UNIPB/1-1997 retains that route. The 2022 IEEE TAC paper DOI 10.1109/TAC.2021.3108492 was compared through its accessible published statement and uses a different communication assumption.

The result does not claim a sharp threshold for arbitrary step-size sequences, nor does it remove any non-delay hypothesis from the cited stochastic-approximation convergence results. A stronger general probability theorem under different terminology remains a residual literature risk.

Same-model review: passed. Independent audit: not yet performed.
