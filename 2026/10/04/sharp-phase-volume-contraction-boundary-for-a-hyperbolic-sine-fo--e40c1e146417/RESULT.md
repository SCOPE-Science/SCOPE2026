# Sharp phase-volume contraction boundary for a hyperbolic-sine four-dimensional flow
## Finding
Consider the smooth vector field
\[
\begin{aligned}
\dot x_1&=\beta_1\left(x_2+\frac15(x_1-\epsilon\sinh x_1)\right),\\
\dot x_2&=\beta_2x_1-x_2+x_3+x_4,\\
\dot x_3&=-\beta_3x_2+x_4,\\
\dot x_4&=-\beta_4x_1.
\end{aligned}
\]
For \(\beta_1,\epsilon>0\), its divergence is
\[
D(x_1)=\frac{\beta_1}5(1-\epsilon\cosh x_1)-1.
\]
Therefore uniform strict phase-volume contraction holds if and only if
\[
\beta_1(1-\epsilon)<5.
\]
At equality, \(D\le0\) with equality at \(x_1=0\); above the boundary, \(D>0\) near \(x_1=0\), so uniform contraction fails. For the parameter choice \(\beta_1=9\), \(\epsilon=1/2\) highlighted in the source,
\[
D(x_1)=\frac45-\frac9{10}\cosh x_1\le-\frac1{10},
\]
so every phase-volume element along an existing trajectory contracts by at least the factor \(e^{-t/10}\).

For every compactly supported ergodic invariant probability measure \(\mu\), the sum of its four Lyapunov exponents satisfies
\[
\sum_{j=1}^4\lambda_j
=\frac{\beta_1}5-1-\frac{\beta_1\epsilon}5\int\cosh x_1\,d\mu.
\]
In particular, at the highlighted parameters this sum is at most \(-1/10\).

## Assumptions and scope
The parameters \(\beta_1\) and \(\epsilon\) are positive; the other displayed parameters may be arbitrary real values for the divergence calculation. The Liouville formula is asserted on any time interval on which the corresponding classical solution exists. The Lyapunov-sum statement is for compactly supported ergodic invariant probability measures, which makes the derivative cocycle integrable. The result concerns phase-volume contraction, not the stronger existence of a compact absorbing set.

## Proof
Differentiating the first component with respect to \(x_1\) gives
\[
\frac{\partial\dot x_1}{\partial x_1}=\frac{\beta_1}5(1-\epsilon\cosh x_1).
\]
The diagonal derivatives of the remaining three components are \(-1\), \(0\), and \(0\). Hence their trace is exactly
\[
D(x_1)=\frac{\beta_1}5(1-\epsilon\cosh x_1)-1.
\]
Liouville's formula for the variational flow gives
\[
\det D\phi_t
=\exp\left(\int_0^t D(x_1(s))\,ds\right)
=\exp\!\left[\left(\frac{\beta_1}5-1\right)t-
\frac{\beta_1\epsilon}5\int_0^t\cosh(x_1(s))\,ds\right].
\]
Because \(\cosh u\ge1\), with equality exactly at \(u=0\),
\[
\sup_{x_1\in\mathbb R}D(x_1)=\frac{\beta_1(1-\epsilon)}5-1.
\]
This proves the sharp condition for uniform strict contraction. If the right-hand side is positive then continuity gives an open neighborhood of \(x_1=0\) on which \(D>0\), proving failure of uniform contraction. Substitution of \(\beta_1=9\) and \(\epsilon=1/2\) gives the stated \(-1/10\) upper bound.

For a compactly supported ergodic invariant probability measure, Oseledets' theorem and Liouville's determinant identity give the standard trace-average relation
\[
\sum_{j=1}^4\lambda_j=\int D\,d\mu,
\]
which becomes the displayed formula after substituting \(D\).

## Verification
The included `verification/check.py` reconstructs the diagonal Jacobian coefficients using exact rational arithmetic, checks the incompatibility of the source's printed divergence with the stated vector field, verifies the sharp threshold, and verifies the showcased-parameter margin. Its recorded output is `VERIFY_OK`.

A coefficient comparison is also decisive: the source prints \(-4/5-\epsilon\cosh x_1\). Equality with the actual divergence would require simultaneously \(\beta_1=1\) from the constant term and \(\beta_1=5\) from the \(\cosh x_1\) coefficient, which is impossible for \(\epsilon>0\).

## Relationship to prior work
The introducing article states the same four-dimensional vector field but prints the divergence as \(-0.8-\epsilon\cosh x_1\), followed by a volume expression in which the state-dependent \(\cosh x_1\) is treated as constant in time. The present result replaces both formulas by the exact divergence and Liouville integral, identifies the sharp parameter boundary \(\beta_1(1-\epsilon)=5\), and derives the invariant-measure Lyapunov-sum identity. Targeted literature and database searches found no result covering this correction or threshold; the closest located published database item concerns a different Nosé--Hoover flow and only shares the general theme of converting divergence information into Lyapunov-sum information.

## Limitations
This result does not prove existence, boundedness, hyperchaos, or uniqueness of an attractor. It does not validate the numerical Lyapunov spectra, synchronization analysis, or image-encryption application in the source. At the equality boundary it proves nonpositive instantaneous divergence, not uniform strict contraction. The originality search cannot exclude unindexed or differently phrased work.

## References
1. T. Nestor, A. Belazi, B. Abd-El-Atty, M. N. Aslam, C. Volos, N. J. De Dieu, and A. A. Abd El-Latif, “A New 4D Hyperchaotic System with Dynamics Analysis, Synchronization, and Application to Image Encryption,” *Symmetry* 14 (2022), 424. DOI: 10.3390/sym14020424. First public version: 2022-02-21.
2. MSC2020, 37C10, “Dynamics induced by flows and semiflows.”
