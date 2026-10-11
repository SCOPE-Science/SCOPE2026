# Scientific review

## Correctness — PASS

The exact population covariance is the variance-weighted sum of the OU target and nuisance covariance. Differentiation gives the stated positive-prefactor sign equation; if the target damping is at or below the nuisance spectral infimum it is uniformly negative. Above the infimum the sign equation starts with strictly negative slope, is strictly convex, and grows exponentially, hence crosses once. Implicit differentiation proves the strict monotone phase curve. A finite nuisance first moment justifies the short-lag expansion. Integration by parts and dominated convergence prove the Laplace edge asymptotic and its logarithmic coefficient. This argument covers both atomic and continuous edge mass and all positive lags. The symbolic derivative and three-rate numerical cross-check agree; neither experiment is used as infinite proof.

## Originality — PASS, subject to residual literature risk

The closest 2026 work (Ditlevsen and Ditlevsen, arXiv:2609.01164v1) contains the underlying two-component covariance identity and asymptotic warning behavior but no global necessary-and-sufficient reversal condition, no monotone phase boundary for arbitrary nuisance mixtures, and no spectral-edge boundary layer. The 2023/2024 Morr–Boers–Ashwin paper (arXiv:2311.18597v2) uses *correlated* stochastic forcing to obtain deceptive signals and does not dominate the present independent-noise sign classification. A 2018 neuronal model conference abstract concerns slow-eigenvalue masking without the quantitative claims. Other terminology from completely monotone covariance or relaxation-spectrum literature might conceal an equivalent theorem; the searches cannot exclude that possibility.

## Mathematical value — PASS

The problem comes from the practical ambiguity of autocorrelation as a critical-slowing warning in multiscale observations. A single rigorous classification across any number, including a continuum, of nuisance relaxation rates identifies the precise damping threshold for a **false-direction** trend and proves there can be no multiple reversals. The sharp edge-dependent coefficient distinguishes isolated slow nuisance modes from continuous rate spectra; this is more than restating the weighted-covariance formula. The theorem makes no unsupported claims about finite samples, nonlinear tipping or exact forecast skill.

## Closest literature and limits

The original two-component mixture identity is a necessary starting point, not itself a theorem about the global sign phase diagram. The 2023 coupled-noise obstruction is a different mechanism. The analysis depends on independent stationary components, fixed amplitudes, positive completely monotone nuisance covariance, and a finite nuisance mean. The long-lag refinement additionally assumes a regular edge mass law.

Same-model review: passed. Independent audit: not yet performed.
