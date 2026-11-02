# Scientific assessment: two phase-resolved Pareto spatial tails

## Correctness — PASS

The regenerative cycle has finite mean because the OU first-hit-time function grows only logarithmically in its starting distance, while finite mean exploration time controls the Gaussian starting-position first moment. The proof obtains both exact Brownian occupancy and OU absorbed-flux identities. Gaussian conditioning yields exact positive functions for the finite-distance tails; dominated convergence and Laplace endpoint asymptotics give the reported constants. The OU Poisson equation proves the return-phase moment equivalence for every positive real order, and renewal reward gives the stationary normalization. All leading constants and the critical moment boundaries have been independently recomputed from these identities. The 56 finite consistency assertions in `verify.py` confirm selected integrals and algebra, but the universal proof is analytical.

## Originality — PASS (qualified, best-knowledge)

The special harmonic equipartition identity was already expressly noted by Frydel (2025) and is treated as **previously known**, not as the novel conclusion. Generic Pareto renewal tails for instantaneous resetting are also known from Nagar and Gupta (2016). Gupta et al. (2020) establish stochastic returns under Poisson exploration; Gupta and Plata (2022) give a general path formulation for arbitrary exploration clocks but chiefly solve work statistics with Poisson clocks, and their full text does not state either stationary phase-specific Pareto spatial tail or its sharp constants. Zhou et al. (2021) use prescribed deterministic return trajectories. Xu and Xue (2026) analyze Poisson exploration and constant-speed noisy return according to an available abstract, not the model's OU first-hit/Pareto combination; its full text was inaccessible. The reviewed contribution is specifically the paired exact exponents and amplitudes and the different moment thresholds in the coupled Brownian/OU return system. A general return-occupation treatment could imply parts of this result without matching its statement; independent priority confirmation remains outstanding.

## Value — PASS

The evaluated mathematical question is whether non-instantaneous, noisy harmonic returns inherit the same heavy-tail fluctuations as the freely spreading phase. The theorem identifies a strict two-power gap between their stationary tail indices, determines precise coefficients and all real-order moment cutoffs, and identifies a positive-recurrent regime with diverging whole-position variance but finite trapped-phase second moment. Those contrasts distinguish measurement during escape and recapture, providing a concrete, physically motivated observable not determined by the previously known phase-weighted energy identity alone. The result needs no arbitrary parameter tuning beyond a natural Pareto clock.

## Closest literature and limitations

The most directly overlapping sources are Frydel (arXiv:2511.14646), Gupta et al. (arXiv:2004.11679), Gupta and Plata (arXiv:2206.07618), Zhou et al. (arXiv:2105.12571), and Nagar and Gupta (arXiv:1512.02092). The theorem assumes a one-dimensional Brownian outward phase, independent positive-mean i.i.d. exploration durations, harmonic OU inward motion with the same diffusivity, and termination at the first hit of zero. No finite-time mixing statement, multidimensional extension or generality beyond the stated clock-tail class is asserted. Xu–Xue (2026) full text was not accessible; although the available abstract concerns a different return law, this remains a literature-access risk. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
