# Scientific review of the beta-mixture switching-trap theorem

## Correctness

**PASS.** The conditional variance exists by positive averaged stiffness and obeys a one-dimensional piecewise-deterministic flow. The invariant two-state transport equations, zero-flux boundary condition, fractional-linear change of variables, beta normalizations, and Gaussian-mixture identity together prove the exact law. Beta endpoint integration establishes both the positive power-law constant and the sharp moment threshold; the equal Gaussian factor in the two environmental components yields the stiffness-only rare-event state bias. No finite computation is treated as an infinite proof. The checker independently solves second/fourth-moment generator systems and evaluates conditional-beta integrals at 36 admissible parameter sets, together with 144 large-variance tail and state-bias comparisons.

## Originality

**PASS on available published comparisons, provisional historical priority.** Guyon–Iovleff–Yao (2004) already prove existence and moment criteria, including a two-state explosive-regime example. De Saporta–Yao (2005) already prove regular variation and give the two-state tail exponent. Those known statements subsume **neither** the explicit normalized conditional beta law nor the tail **constant** nor the rate-independent extreme-environment composition, and none of those is claimed to make the known tail exponent itself new. Their complete available primary texts were read in pertinent mathematical portions, including the two-state examples and the tail theorem. Zhang–Wang's 2016-public accepted manuscript assumes nonpositive drift coefficients in each regime, excluding the repulsive branch. A 2021 Kac–OU article uses a different telegraph-driving mechanism. Relevant mathematical research records and accessible earlier claims were compared for aliases and implications; no equivalent normalized beta law with stiffness-only extreme-state bias was found. Residual risk: early telegraph-driven linear-diffusion work or a different parametric representation may already encode this same law; completeness of historical coverage and novelty are not independently certified.

## Value

**PASS.** Earlier theory supplies an existence criterion and tail exponent but leaves the *observable law and tail amplitude* implicit for the natural mixed stable/unstable trap. The explicit positive beta mixture makes the entire spatial law computable without solving coupled spatial Fokker–Planck equations, quantifies rare-event probabilities, and isolates an unexpected rate-independent experimental composition effect. This is substantive beyond a tail-exponent restatement or numerical example. It is specific to an experimentally interpretable two-state physical idealization and no broader theorem is asserted.

## Closest sources and boundaries

- Guyon, Iovleff, Yao (2004), *Linear diffusion with stationary switching regime*, DOI 10.1051/ps:2003017, full manuscript inspected, especially §§1–3 and the two-state example.
- De Saporta, Yao (2005), *Tail of a linear diffusion with Markov switching*, DOI 10.1214/105051604000000828, full manuscript text examined at the stated main theorems and section 8.
- Zhang, Wang (accepted-author version publicly posted 2016-01-20), DOI 10.1080/03610918.2015.1132321, Assumption (A) and Theorem 2.1 checked.
- Ratanov (2021), arXiv:2102.13308, introductory equations and relevant invariant/scaling sections checked; its Kac process differs.

The claim does not cover arbitrary multi-state environments, arbitrary diffusion amplitudes per state, or any inference theorem from finite observations. Older sources' already-proved stationary existence, regular variation, and exponent are not presented as new.

Self-review: passed. Independent audit: not yet performed.
