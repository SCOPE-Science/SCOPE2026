# Scientific review

## Correctness — PASS

The object is a centered finite-support scalar quadratic gradient law with ordinary norm clipping, and the cap varies while the distribution remains fixed. The bias is a continuous piecewise-affine function with zeros at cap zero and beyond the largest magnitude; the number of sign-components gives an upper bound of \(m-2\) reversals. The constructive signed masses telescope to a zero-mean probability law with odd denominator, and exact interpolation yields a crossing at each prescribed half-integer cap. The odd denominator excludes constant zero plateaus in the clipped mean field and proves uniqueness; monotone \(1\)-Lipschitz mean drift proves convergence of the population update for \(0<\eta<2\). All critical steps can be reconstructed from `RESULT.md`; `verify.py` corroborates finite instances but is not substituted for the arbitrary-dimension proof.

## Originality — PASS (qualified)

Huber's clipped-score formulation is not new, and previous work supplies both the basic scalar clipping map and examples of fixed-cap biased equilibria. Chen, Wu, and Hong (2020, pp. 1–4) give finite examples of drift away from an optimum and a flat equilibrium interval. Koloskova, Hendrikx, and Stich (2023, Sections 3.1–3.2 and Appendix C.5) derive two-point bias lower bounds and general noise-dependent convergence guarantees. Qian et al. (2021) analyze convergence and clipping-induced bias. None of the inspected claims states the sharp \(m-2\) count across changing caps for a *fixed centered law*, or constructs all sharp counts with unique equilibria. Relevant accessible published mathematical records on clipping, heavy-ball cycles, and capped Polyak steps concern different iteration maps or parameter caps. The classical Huber location-estimator literature may contain an equivalent path-complexity result; its exhaustive verification remains outstanding.

## Value — PASS

The precise question is motivated by a possible false inference from monotone bounds on clipping-bias *magnitude*: increasing the cap need not move population drift consistently toward the true gradient direction. The sharp support law proves a qualitative obstruction at the smallest possible complexity and permits arbitrarily many sign reversals with bounded finite noise. Uniqueness and convergence of the associated mean-field equilibrium make these sign changes an algorithmically interpretable fact, rather than merely a pointwise cancellation at the optimum. The theorem is a structural bound and explicit boundary family, not a claim of privacy or stochastic sample-path performance.

## Closest literature and limitations

Closest: Chen, Wu, and Hong (arXiv:2006.15429, pp. 1–4); Koloskova, Hendrikx, and Stich (PMLR 202, 2023, Sections 3.1–3.2 and Appendix C.5); Qian et al. (PMLR 130, 2021). Huber's general location M-estimation is an equivalent formulation, but a specialized path-count theorem there remains an originality risk. The complete result is one-dimensional and finitely supported; deterministic population updates must not be confused with constant-step stochastic gradient iterates.

Self-review: passed. Independent audit: not yet performed.
