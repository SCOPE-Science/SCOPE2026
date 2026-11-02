# Scientific review: rank-one switching-work fluctuations

## Correctness — PASS
For a stationary finite collection of overdamped Brownian particles with independent thermal noises and a single shared symmetric Poisson on/off trap, the signed switching-work process is a quadratic jump additive functional. The corrector \(h_i(0,x)=\kappa_i x_i^2/2\), \(h_i(1,x)=-\kappa_iD_i/(2q)\) solves the exact generator Poisson equation and cancels every position-dependent work jump. Every corrected work stream has constant-magnitude synchronized switching increments and an individual continuous Brownian component; independent Brownian drivers have zero cross-bracket. The exact stationary second-moment identities give the diagonal bracket, completing the finite-time corrected-work covariance matrix and the asymptotic physical-work covariance rate. The multivariate martingale CLT and vanishing boundary terms prove the distributional claim. The bundled symbolic and finite-simulation checks passed; simulations are not substitutes for the proof.

## Originality — PASS, qualified
The 2023 shared-switch gas source derives stationary joint position distributions, spatial correlations and extreme statistics, while earlier and later on/off-trap thermodynamic studies establish stationary energies and *mean* dissipation. A single-particle work variance calculation is already available and reproduces the diagonal special case; its value is not claimed as new. The assessed contribution is the exact cross-particle switching-work law, universal rank-one covariance matrix, finite-time martingale correction, inference from cross-work rates, and non-self-averaging quadratic gas scaling. The full text of the closest main article and work sections of plausible other sources were inspected; separately hosted supplementary material and unindexed broader results leave genuine residual publication-priority uncertainty. Absence from searched texts is not a uniqueness proof.

## Mathematical value — PASS
The shared-switch input generates measurable correlations in thermodynamic *work currents* even with independent thermal forces. The exact off-diagonal law \(\Sigma_{ij}=\mu_i\mu_j/q\) determines the switching rate without calibrating the individual stiffness or diffusivity, while the rank-one matrix and large-population quadratic growth expose the environmental common-noise channel. This is a structural many-body/inverse result and not a numerical refinement of the single-particle variance.

## Scope and limitations
All exact formulas assume stationary initialization, fixed finite particle count, symmetric Markov on/off switching, positive parameters, independent Brownian drives and signed potential-change work. The Gaussian theorem takes long time before any population-size limit. Finite-sample identification errors, asymmetric clocks, independent clocks and alternative stochastic energetics conventions are not claimed. The exact time-proportional covariance belongs to corrected martingales, not raw work at arbitrary finite time.

## Literature and reproducibility
The closest model source is Biroli et al., arXiv:2312.02570v1 (2023); thermodynamic mean results include Alston et al., arXiv:2202.02630 (2022), and Frydel, arXiv:2407.12213v2 (2024). Wider work-fluctuation comparisons include arXiv:2607.05173, arXiv:2310.11267 and arXiv:2206.07618, with differing assumptions or observables. `RESULT.md` gives the full proof and `checker.py` provides actual executable symbolic and finite numerical diagnostics.

Self-review: passed. Independent audit: not yet performed.
