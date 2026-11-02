# Self-review

## Correctness — PASS

The exact rational stability map, the upper-bidiagonal transient Jordan block, mass conservation, and the generating-function factorization reconstruct all entries. The distinct sign laws for nearest-neighbor transient coefficients and absorbing-column tails give necessary **and sufficient** inequalities, yielding the full all-length classification. The proof covers zero step, all endpoints, and the exceptional single-step n=13 case. The embedded independent Fraction solver verifies 27,584 exact assertions at twelve rational timesteps for each of n=2 through n=18. The all-n conclusion is analytic; the finite verifier is supplementary.

## Originality — PASS, with residual literature risk

Zappavigna–Colaneri–Kirkland–Shorten (2012), Section 4, show small-step negativity for an eight-dimensional nilpotent/Metzler system, not the entire stochastic absorbing-chain step classification. Lóczi–Ketcheson (2013 preprint) give the general zero absolute-monotonicity radius of the [2/2] map, which does not imply the sharp positive-step existence cutoff. The published published-finding corpus eight-state pure-birth record proves the exact n=8 interval and the seven-state local guarantee. Both are openly acknowledged as prior coverage, rather than presented as new. The present theorem additionally proves all dimensions, the maximum n=13, the isolated n=13 feasible step, and impossibility for every n>=14. Searches for equivalent Chebyshev/Padé/Markov-tail formulations found no stronger exact classification, but search incompleteness and the abstract-only check of the 2026 Itkin–Kazbek paper are residual originality risks.

## Value — PASS

A finite-state threshold for existence of **any** stochastic Gauss–Legendre step is a natural structural invariant of a basic absorbing Markov generator. The unexpected abrupt loss after thirteen states and the exact dimension-dependent recovery windows are relevant to selecting or rejecting a time integrator on longer one-way chains. This resolves a motivated classification question rather than supplying an arbitrary isolated numerical value.

## Scientific limits

The theorem concerns exactly the unmodified fourth-order Padé endpoint, uniform unit-rate absorbing pure-birth chains, and exact entrywise signs. No claims about arbitrary generators, unequal rates, internal stages, numerical accuracy at coarse steps, or independent validation. Exact-rational tests of finite instances cannot establish the all-length theorem without the proof.

Self-review: passed. Independent audit: not yet performed.
