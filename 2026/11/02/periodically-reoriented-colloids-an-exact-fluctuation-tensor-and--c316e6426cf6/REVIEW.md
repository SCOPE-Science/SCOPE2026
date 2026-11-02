# Scientific review

## Correctness — PASS

The exact Itô decomposition into a bounded angular endpoint displacement and an independent conditional Gaussian martingale follows from the Schur complement of the positive-definite mobility. First and second angular Fourier harmonics provide the mean and one-cycle covariance. Deterministic reset times make cycle increments iid; the strong law and multivariate central limit theorem yield the asserted drift and covariance-growth limit after control of the bounded-duration final cycle. The isotropic-block eigenbasis and gap formula reduce to exact scalar algebra. Strict convexity of \(e^{2z}-1-4z\), combined with endpoint behavior of the objective, yields the single nonzero global optimum. A standalone numerical consistency script passed 56 finite matrix and optimization checks and a separate finite Monte Carlo cross-check. Its finite tests do not establish an infinite-time theorem.

## Originality — PASS, with residual priority risk

The full text of Cleuren–Eichhorn [1] provides the exact mean displacement for periodically reoriented *cross-coupled* colloids but not the centered covariance-growth formula or the positive finite-period maximum of coupling-induced anisotropy. The full text of Chaki–Olsen–Löwen [2] analyzes covariance under *Poisson* angular resets and independent translational/angular Brownian drivers. The absence of a cross-mobility vector in [2] prevents it from implying the stated special case with isotropic translational mobility and nonzero cross mobility. Earlier unreset hydrodynamic studies [3] do not include repeated fixed-angle resetting. These are substantive comparison-of-hypotheses distinctions, not just differences of title or terminology. A generic covariance theorem for periodically regenerated Markov-additive systems could reproduce some derivations, and a broader hydrodynamic treatment could contain an equivalent formula; no independently certified priority claim is made.

## Value — PASS

The motivating reset-based colloid sorting model explicitly raises second-moment modulation and enhanced diffusion as physically motivated open uses. The exact tensor separates thermal and rotation-endpoint fluctuation mechanisms; the isotropic-translation case uncovers a mechanism absent from independently driven anisotropic Brownian models, with a sharp dimensionless optimal reset interval. The theorem gives a physically interpretable prediction for anisotropic broadening around the separation drift, and a way to tune the dispersion profile, without conflating that optimum with optimal sorting performance.

## Closest literature and boundaries

[1] B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1, Eqs. (4)–(8), Fig. 4 and closing discussion.

[2] S. Chaki, K. Stølevik Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2, Secs. II and V, especially Eqs. (1)–(3), (63)–(64).

[3] S. Chakrabarty et al., *Brownian Motion of Arbitrarily Shaped Particles in Two Dimensions*, arXiv:1410.6057; background on unreset coupling only.

The theorem is for a single force-free colloid with constant body-frame SPD mobility and deterministic fixed-angle resets, not nonlinear many-body transport, instantaneous position resets, or an optimized classifier. Independent literature-wide priority and independent mathematical validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
