# Scientific review: sharp mean-square timing-jitter margin

## Correctness — PASS

The statement precisely specifies the plant, fixed feedback, independent positive two-point sampling law, and sample-instant mean-square norm. The exact plant integration gives the displayed \(2\times2\) sampled matrix; direct symmetric-square lifting gives the displayed \(3\times3\) covariance matrix and polynomial determinant. For every nonzero jitter magnitude strictly below one, invertibility of both sampled matrices and a nonsingular commutator force the normalized adjoint covariance map's Brouwer eigenmatrix to be positive definite. Its positive eigenvalue is the spectral radius by order domination and is therefore the exact expected quadratic-energy growth factor for every nonzero initial state. Continuous spectral radius, nilpotence at zero jitter, explicit spectral radius five at the endpoint, and unique crossing of the cubic yield the necessary-and-sufficient threshold. The independently formed formal-polynomial verifier passes 106 exact assertions and finite-path comparisons. An explicit strictly positive rational Lyapunov certificate covers the mixed stable/unstable witness. The infinite-horizon classification is analytical; finite enumeration alone would not establish it.

## Originality — PASS, qualified

General moment-stability criteria under random sampling and network delays predate this example (Sun, Sun and Chen, 2021), so the general spectral-radius reduction is **not** claimed as new. The contribution assessed here is the exact, one-crossing polynomial classification for this specific two-sample-deadbeat double integrator, for all positive equiprobable jitter magnitudes, together with a nonempty explicit parameter region where one individually unstable fixed period participates in a mean-square-stable stochastic mixture. The available publisher preview of Sun and colleagues discusses a general vectorized condition and a batch-reactor numerical example, but a full technical comparison was not available. Vallarella and Haimovich (2022) study stability under all sufficiently small nonuniform intervals, not the same random large-interval mean-square phenomenon. Su, Li and Lu (2021) work with random channel delays and fixed physical sampling periods. No exact duplicate was identified by searches for the problem, polynomial, threshold, and equivalences. This is evidence of a potentially unrecorded specialized classification, **not** a claim that a general second-moment method or switching-based stabilization is unprecedented. Full-text access and hidden specialized prior work are residual risks.

## Mathematical value — PASS

A unit-period, exactly two-step-deadbeat controller is a canonical aggressive sampled-data design, and timing uncertainty is a physically motivated robustness question. Instead of an unquantified small-jitter claim, the result gives a sharp algebraic tolerance and a complete below/at/above-threshold classification for every nonzero initial state. Its strict branch-instability paradox, supported by a rational Lyapunov certificate, distinguishes stochastic performance from worst-case switching analysis. The exact constants offer a reproducible benchmark for stochastic sampled-data stability calculations. The classification is narrow but is not an arbitrary parameter slice: the fixed gains are forced by the exact two-step-deadbeat condition at unit sampling period. The result is not a broader stochastic control design theorem.

## Closest literature and limitations

- H. Sun, J. Sun, J. Chen (2021), https://doi.org/10.1016/j.automatica.2020.109385: general random-sampling moment stability already addressed; its full technical paper was unavailable for an exhaustive specialization check.
- W. Su, J. Li, J. Lu (2021), https://arxiv.org/abs/2108.12795: full accessible paper describes stochastic channel delays on a fixed sampling clock.
- A. J. Vallarella, H. Haimovich (2022), https://arxiv.org/abs/2202.10549: accessible full-text nonuniform-sampling results have different quantifiers and a small-period focus.

The result applies to sampled states only, independent equiprobable intervals, the specified noiseless plant and gains, and exact arithmetic. General distributions, noisy measurements, floating-point effects and almost-sure stability are not covered. Complete publication-priority review remains open.

Self-review: passed. Independent audit: not yet performed.
