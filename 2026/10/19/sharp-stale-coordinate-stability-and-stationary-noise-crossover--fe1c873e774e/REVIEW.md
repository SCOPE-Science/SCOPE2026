# Scientific review

## Correctness — PASS

The claim is exactly the two-dimensional, one-step **remote-only** delayed randomized relaxation theorem. The proof constructs the actual four-dimensional Markov-switching state and its two update matrices. Its four-by-four stationary covariance satisfies all sixteen Lyapunov entries, as independently checked over 300 rational parameter sets; the closed-form eigenvalues establish strict positive definiteness throughout the proposed interval. The two-step covariance difference \(Q+\mathcal L(Q)\succ0\) is a bona fide contraction certificate rather than simulation, and the negative-eigenvalue/no-solution stationary obstruction establishes sharp necessity. A fresh-read comparator has its own independently verified two-by-two Lyapunov identity. Exact arithmetic checker: 6,908 assertions. Unverified scope: higher dimension, other delays, nonindependent noise, floating-point implementation.

## Originality — PASS, with residual bibliographic risk

The new claim is neither a restatement of asynchronous RGS convergence in expectation nor the known exact \(\beta=1\) delay-law recurrence. Carson–Ma (2026, Sections 3–5, full HTML) supplies a general **sufficient** convergence criterion, not the sharp two-coordinate frontier or positive-noise covariance. A published exact delayed Gauss–Seidel record (published-finding corpus 2026-09-20, `9ae0040f2dac`, full RESULT.md read) is restricted to unrelaxed overwrites and no additive-noise covariance; it does cover the special case \(\beta=1\) with zero noise. General earlier results by Beidas–Papavassilopoulos (1993) and Verkama (1996) were compared at available abstracts and references, not at inaccessible full text; a hidden specialization remains a material risk. Relevant sections of Moga–Dubois (1995) were inspected and describe different expected-trajectory/random-delay analysis. No prior checked statement was found that implies both the exact frontier and the strict under/over-relaxation sign switch. Lack of a hit alone is not taken as novelty proof.

## Mathematical value — PASS

At the same coordinate-update and noise budget, the exact risk comparison reveals a nonmonotone communication-staleness effect: a stale remote gradient **improves** stationary variance for all underrelaxed weights but **worsens** it for all overrelaxed weights. The structural boundary \(\beta=1\) is independent of the coupling and noise variance, while the sharp stability ceiling depends on coupling. This supplies a useful benchmark for distinguishing noise floor from convergence speed when choosing relaxation in distributed SPD solvers. It is not presented as a wall-clock speedup or a general performance guarantee.

## Closest literature and limits

Carson and Ma, arXiv:2609.15605v1 (full relevant manuscript); published published-finding corpus exact-delay law `9ae0040f2dac` (full result); Beidas and Papavassilopoulos, Parallel Computing 19 (1993), 281–302 (abstract only); Verkama, SIAM J. Sci. Comput. 17 (1996), 906–912 (abstract/reference list); Moga and Dubois, CENG 95-06 (selected report pages). No independent validation, formal proof certification, or extrapolation beyond the explicit stochastic model.

Self-review: passed. Independent audit: not yet performed.
