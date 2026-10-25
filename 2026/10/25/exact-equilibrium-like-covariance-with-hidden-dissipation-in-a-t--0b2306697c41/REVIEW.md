# Scientific review

## Correctness

**PASS.** The proof specifies the two-state continuous-time Markov environment, stationary initialization, all positive parameters, and the physical entropy convention. Conditional Brownian integration and a two-by-two Feynman–Kac matrix give an exact time-lag covariance ODE. Its exponential condition factors as \((ab-\kappa^2)(4ab-(a+b)^2)=0\), giving a sharp necessary and sufficient nontrivial cancellation. Exact inversion of the stationary fourth-moment system yields the positive cumulant and the \(K\)-to-\(\Sigma\) identity. `checks/check.py` directly and reproducibly checks the nonstandard algebra and finite examples; its output is embedded. The proof is analytical, and finite numerical tests are supplementary rather than substitutes for infinite-parameter reasoning.

## Originality

**PASS on inspected evidence, subject to independent priority assessment.** The full motivating primary source [Alston–Cocconi–Bertrand, arXiv:2202.02630, §4] already gives stationary conditional second moments and entropy production for this exact model; both are credited. The new claim is the sharp equality of the *entire stationary two-time covariance* with equilibrium OU at the geometric-mean switching rate, plus a strictly positive fourth-order diagnostic that quantitatively recovers the joint entropy production. The exact claim was compared against the accessible primary work on two-state OU stationary densities, on/off harmonic switching, continuously fluctuating stiffness, and broad semi-Markovian switching, as well as targeted published-finding corpus claims involving OU autocorrelations and identification. None of the inspected implications entails the complete finite-rate cancellation together with its calibrated fourth cumulant. Generic moment recurrences and Feynman–Kac methods nevertheless leave a residual risk of equivalent earlier specialization.

## Value

**PASS.** Complete two-time statistics are a natural experimental measurement and are used for equilibrium-versus-nonequilibrium inference. The result isolates a codimension-one manifold with no detectable dissipation from stationary linear correlation or spectrum, even though the *joint physical entropy production can diverge while those observables remain exactly fixed*. It then supplies an exact experimentally measurable fourth-cumulant witness and invertible dissipation calibration within the stated model. This is a sharp structural identifiability limit, not a routine isolated numerical fit or small perturbative coefficient.

## Closest literature and limitations

Alston, Cocconi and Bertrand, arXiv:2202.02630, §4, Eqs. (37)–(43), supply the exact thermodynamic baseline; Zhang and Wang (2017) study stationary densities; Santra, Das and Nath (2021) and Frydel (2024) study on/off traps; Cocconi et al. (2024) study continuous OU stiffness noise; Frydel (2026) treats semi-Markovian two-stiffness dynamics and stationary moments. None of these inspected texts supplies an already evaluated claim covering the theorem's full joint conditions. Residual risk is an unrecognized equivalent specialization of more general regime-switching/covariance literature. The result does not imply equality of position laws, finite-dimensional distributions or pathwise entropy; its entropy formula is for the joint physical model. No independent priority or experimental validation has been performed.

Self-review: passed. Independent audit: not yet performed.
