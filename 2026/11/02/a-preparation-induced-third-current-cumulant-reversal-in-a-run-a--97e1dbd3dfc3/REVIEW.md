# Scientific review of a third-current-cumulant sign reversal

## Correctness

**PASS.** The theorem is carefully restricted to disorder-averaged conditional third cumulants and the standard step-density thermodynamic limit; it does not conflate these with cumulants of an unconditional disorder mixture. A Bernoulli-cumulant identity gives the exact positive gap between the two preparations. A one-flip Poisson expansion produces the opposite short-time signs and coefficients, and a bounded-jump martingale central limit theorem with uniform-integrability control proves the common strictly positive long-time scaling. The Gaussian integral is evaluated analytically. The standalone independent numerical implementations of the single-particle crossing probabilities agree and reproduce both asymptotic regimes. Numerical checks are not the proof.

**Technical limits:** A unique finite-time zero is not proved. The fourth-moment tail bound and positivity of the symmetric displacement law are essential for passing the long-time integral limit.

## Originality

**PASS, with residual risk.** Banerjee et al. (arXiv:2001.01923), Jose--Rosso--Ramola (arXiv:2306.13613) and the latter authors' follow-up (arXiv:2310.16811) give the current-generating-function framework, the four disorder prescriptions, exact propagators and second-cumulant results. All are acknowledged as prior work. The new conclusion compares the third cumulants strictly **for every time**, proves their opposite early signs, and evaluates a shared positive Gaussian-limit coefficient, forcing a negative-to-positive crossover only under full quenching. The parent paper explicitly identifies higher cumulants as further work, and the follow-up focuses on variance even for general orientation bias. No equivalent evaluated statement was identified in searched literature or related mathematical-record results.

**Residual risk:** Complete prior generating functions determine third cumulants implicitly, so a stronger unrecognized analysis of their derivatives might already imply the theorem. Publication-priority certification has not been performed. An unrelated general Poisson-binomial hierarchy provides no evaluated time-dependent crossing theorem for this specific run-and-tumble preparation.

## Mathematical value

**PASS.** The discovery addresses a specific gap raised in the originating active-current analysis: higher-than-second cumulants under quenched density and magnetization. It shows a qualitatively new preparation effect beyond the previously established variance exponent: freezing the initial orientations reverses the sign of skewness early on, while losing their memory produces the same positive late-time constant as annealed orientations. The strict all-time ordering is a structural identity, not an arbitrary parameter slice. Its sharp asymptotic coefficients permit falsifiable comparisons of preparation protocols.

**Scope limits:** Independent particles; unbiased initial velocity fractions; two-state Poisson velocity reversal; infinite-volume step density; disorder-averaged conditional cumulants. No claim of unique sign-crossing time, finite-population correction, entropy production, or interactions.

Self-review: passed. Independent audit: not yet performed.
