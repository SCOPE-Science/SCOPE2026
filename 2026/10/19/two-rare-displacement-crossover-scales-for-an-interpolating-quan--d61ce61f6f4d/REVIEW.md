# Scientific review

## Correctness (C) — PASS

The exact Gaussian-arcsine mixture from Yoshino et al. gives a positive angular integral. The integrand identity and subtraction \(B_q(c)-c=q(1-2c^2-qc)/(1+2qc+q^2)\) yield an absolute, global \(8q(1+\eta)\) logarithmic comparison. The endpoint \(c=1\) of the angular integral has uniformly positive, nondegenerate curvature over \(q\in[0,1/4]\), so Laplace's method gives the precise universal prefactor and a uniform relative \(O(\eta^{-1})\) remainder. Algebraic combination with the classical \(I_0\) asymptotic proves both scaling limits. Separate fixed-parameter Laplace expansion and Gaussian Mills integration prove the one- and two-sided tail constants. A standalone checker passed 149 numerical checks; it is not substituted for the proof. Boundary \(q=0\) is used only as a uniform-parameter extension, while the walk's existing theorem applies at each \(q>0\).

## Originality (O) — PASS with stated risk

The 2025 source already proves the full Gaussian-arcsine limiting distribution; the new claim excludes that representation and its ordinary weak Gaussian limit. No uniform \(q,x\) Bessel comparison, second \(q^2x^2/r\) crossover, or quantitative far-tail prefactor was located in accessible main-text mathematical sections and discussion. The distinction is based on statements and implication: the exact source density determines the numbers in principle but does not furnish uniform asymptotic control or these joint scaling laws without the new estimates. Indexed searches of relevant normal variance-mixture and quantum-walk literature and semantic scientific records yielded no explicit dominating theorem. This review cannot prove absolute novelty; implicit coverage by more general uniform Watson/Laplace mixture results or uninspected supplementary text remains a real risk.

## Value (V) — PASS

Ordinary weak convergence obscures the tails most sensitive to rare quantum updates. The precise quantum-classical crossover at displacement \(\sqrt{r/q}\), the farther endpoint-saddle crossover at \(\sqrt r/q\), and the exact density/survival prefactors provide mathematically motivated, nontrivial uniform resolution of a double singular limit. They quantify when a classical Gaussian approximation fails for unusual scaled displacements, without pretending to establish a finite-time large deviation principle.

## Closest sources and limits

Yoshino et al., arXiv:2503.03021v1 and Entropy 27 (2025) 670, provide the exact mixing measure and source theorem, not the reported uniform two-scale asymptotics in the material inspected. General normal variance mixture theory provides the construction, and classical Laplace / Bessel methods are standard mathematical techniques. Direct complete-PDF and native full-text access was limited by journal rate limits and archival access challenges; indexed full-text source material covering the statement, key definitions, sections and discussion was read. Residual implicit-coverage risk and the fixed-time limitation are explicitly recorded.

Self-review: passed. Independent audit: not yet performed.
