# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces to two independently checkable asymptotics and one exact telescoping identity.

The dominant-solution estimate starts from the published positive double-binomial formula for A_n. Its entropy phase is strictly concave on the interior of the admissible domain, has a unique maximizer at (3/4,3/4), and has negative-definite Hessian with determinant 512/3 there. Uniform Stirling expansion and the two-dimensional lattice Laplace method give the explicit leading constant 2 sqrt(6)/(3 pi^2). Boundary and off-saddle terms are exponentially smaller because the maximizer is unique and interior.

The Casoratian identity is exact and is also stated and proved in Bachmann's paper. Stirling's formula gives W_n ~ (2 sqrt(2)/pi)64^n/n^4. Dividing by A_n A_{n+1} gives the exact leading increment of C_n/A_n. Since Bachmann proves that these quotients increase to zeta(3)/7, the error is the positive tail of those increments; the consecutive increment ratio tends to 1/64, giving the geometric factor 64/63 and the final constant sqrt(2) pi^3/84.

The verification artifact independently regenerates the recurrence, checks the binomial representation at small indices, verifies the exact Casoratian through n=99, and numerically confirms both scaled limits at high precision.

## Originality

**PASS, to the best of our knowledge.** The full text of Bachmann's 2026 preprint was inspected. It proves the limit C_n/A_n -> zeta(3)/7, records the same double-binomial formula for A_n and the exact Casoratian, and gives a qualitative convergence argument, but it does not state an asymptotic for A_n, a 64^{-n} error equivalent, or the leading constant sqrt(2) pi^3/84.

The Calabi-Yau operator database entry for AESZ no. 28 was checked; it records the operator, coefficients and local exponents, but no matching sharp quotient-error constant was located. Searches were also made for the exact recurrence, the initial values 1,6,126,3948,149310, the limit zeta(3)/7, the constants 2 sqrt(6)/(3 pi^2) and sqrt(2) pi^3/84, and equivalent language involving Apéry-limit error rates and AESZ 28. No prior statement of the result was found.

Chamberland--Straub's survey on Apéry limits was inspected. It explains Poincaré--Perron theory and characteristic-root growth for recurrence solutions, so exponential convergence at a characteristic-root ratio is part of the general background. That theory does not by itself provide the explicit connection constant proved here. The 2008 Almkvist--van Straten--Zudilin work establishes a broad Calabi-Yau Apéry-limit context, but its full text was not exhaustively checked for this exact asymptotic constant.

The largest residual originality risk is N. Sato and K. Tasaka, *Multivariate Apéry-like numbers, interpolations, and modular L-values*, which Bachmann cites as "in preparation" and as another source proving the underlying limit. No public full text was located. Because that work treats the same A_n,C_n pair, it could contain sharper asymptotic information not visible from Bachmann's citation. This risk is explicitly retained rather than treated as evidence of absence.

## Value

**PASS.** The result converts a qualitative Apéry limit into an exact first-order approximation law, including the closed constant. It also supplies an explicit asymptotic for the integral AESZ no. 28 solution itself. The proof is short enough to reuse: positive binomial saddle asymptotics plus an exact Casoratian yield a general mechanism for sharp constants in recurrence quotients when both ingredients are available.

## Scope and limitations

No claim is made for arbitrary Apéry recurrences, for Bachmann's q-root-of-unity construction, or for the odd-weight analogues. No new irrationality result or irrationality measure for zeta(3) is claimed. The result is not independently validated or formally verified.
