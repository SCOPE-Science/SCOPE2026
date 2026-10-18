# Review of reciprocal random-action consensus rate

**Correctness — PASS.** The precise stochastic update and conditional independence permit a closed two-dimensional moment recurrence. Its matrix has a strictly positive Perron eigenpair and spectral radius below 1 for every \(0<\alpha<1\); a martingale and Borel–Cantelli argument identifies the random binary consensus and the exact expected terminal quadratic loss. The derivative has precisely one genuine interior zero; the other algebraic root is extraneous. The packaged exact-arithmetic program checks all nonstandard polynomial and moment identities, not the infinite-time statements.

**Originality — PASS with limitations.** The 2017/2018 foundational paper presents the random-actions model, herding, and a trajectory-local fast-descent heuristic \(1-\alpha\). The 2024 convergence paper proves almost-sure and moment convergence but does not give this expected terminal squared-error spectrum or its exact gain optimum. Targeted searches of published literature and indexed mathematical findings identified no implication of the full result; algebraic agreement with an unsearched two-state stochastic process cannot be excluded. The 2024 related thesis was not inspected in full and is a documented risk, not used to claim absence of coverage.

**Value — PASS.** The result solves a natural quantitative gap in an established model: it distinguishes transient ensemble convergence from the rapid final pathwise phase and finds a unique nonobvious optimal influence coefficient. It also gives a complete exact two-agent benchmark and exposes a concrete near-periodic source of slow convergence at large influence. It is not asserted to hold for larger networks.

**Closest sources:** Leshem–Scaglione (2018), Sections I and III; Abrahamsson–Danev–Larsson (2024), Sections II–IV and appendix. **Residual risks:** possibly equivalent two-state consensus calculations in older stochastic-process literature and a not-fully-read related 2024 thesis.

Self-review: passed. Independent audit: not yet performed.
