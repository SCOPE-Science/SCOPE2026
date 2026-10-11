# The Morley dihedral limiting equation forces an infinite Fourier spectrum
## Finding
Let \(\gamma:\mathbb R/\mathbb Z\to\mathbb R\) be continuous, let \(\tau>0\), assume \(\gamma(0)=1\), and suppose that for every \(x\in\mathbb R/\mathbb Z\),
\[
4\tau\left(\int_0^1\gamma(y)\gamma(y-x)\,dy-\left(\int_0^1\gamma(y)\,dy\right)^2\right)
=\frac{3\gamma(x)-\gamma(x)^3}{2}.
\]
Write
\[
\widehat\gamma(k)=\int_0^1\gamma(x)e^{-2\pi i kx}\,dx,
\qquad k\in\mathbb Z.
\]
Then
\[
\int_0^1\gamma(x)^3\,dx=3\int_0^1\gamma(x)\,dx,
\]
and, for every nonzero \(k\in\mathbb Z\),
\[
\widehat{\left(\frac{3\gamma-\gamma^3}{2}\right)}(k)
=4\tau\lvert\widehat\gamma(k)\rvert^2\ge 0.
\]
In particular, every nonzero Fourier coefficient of the nonlinear term is real and nonnegative. Moreover, \(\gamma\) has infinitely many nonzero Fourier coefficients. Therefore no trigonometric polynomial can solve the normalized limiting equation.

## Assumptions and scope
The statement is conditional on an exact continuous real-valued solution of the displayed periodic integral equation with \(\tau>0\) and \(\gamma(0)=1\). Evenness is not required for the proof, although the Morley-dihedral limiting profile proposed in the source is even. The result concerns the continuous limiting equation itself; it does not assert that such a solution exists or that the finite-dimensional dihedral systems converge to one.

## Proof
Set
\[
\mu=\int_0^1\gamma(x)\,dx,
\qquad
C(x)=\int_0^1\gamma(y)\gamma(y-x)\,dy.
\]
Fubini's theorem and periodicity give
\[
\int_0^1 C(x)\,dx
=\int_0^1\gamma(y)\left(\int_0^1\gamma(y-x)\,dx\right)dy
=\mu^2.
\]
Integrating the limiting equation over one period therefore makes its left-hand side vanish and yields
\[
0=\frac12\left(3\mu-\int_0^1\gamma(x)^3\,dx\right),
\]
which proves the cubic moment identity.

Because \(\gamma\) is real and continuous, the Fourier coefficient of its autocorrelation is
\[
\widehat C(k)=\widehat\gamma(k)\widehat\gamma(-k)=\lvert\widehat\gamma(k)\rvert^2.
\]
The constant \(\mu^2\) affects only the zero Fourier mode. Taking the \(k\)-th Fourier coefficient of the limiting equation for \(k\ne0\) gives
\[
\widehat{\left(\frac{3\gamma-\gamma^3}{2}\right)}(k)
=4\tau\lvert\widehat\gamma(k)\rvert^2,
\]
so every such coefficient is real and nonnegative.

It remains to exclude finite Fourier support. A constant solution is impossible: \(\gamma(0)=1\) would force \(\gamma\equiv1\), for which the autocovariance side is zero while the nonlinear side equals \(1\). Suppose instead that \(\gamma\) is a nonconstant trigonometric polynomial. Since \(\gamma\) is real, choose the largest integer \(m\ge1\) with \(a_m=\widehat\gamma(m)\ne0\). The autocovariance \(C-\mu^2\) has Fourier support only in \(\{-m,\ldots,m\}\), so its coefficient at \(3m\) is zero. The linear term \(3\gamma/2\) also has zero coefficient at \(3m\). In \(\gamma^3\), however, the only triple of frequencies from \(\{-m,\ldots,m\}\) whose sum is \(3m\) is \((m,m,m)\). Hence
\[
\widehat{\gamma^3}(3m)=a_m^3\ne0.
\]
The \(3m\)-th Fourier coefficient of the limiting equation would therefore read
\[
0=-\frac12a_m^3,
\]
a contradiction. Thus every normalized continuous solution has infinitely many nonzero Fourier modes.

## Verification
The proof uses only periodic Fubini, the standard Fourier identity for autocorrelation, and a maximal-frequency argument. The boundary cases are explicit: \(\tau>0\) is used for the positivity conclusion, while the infinite-spectrum contradiction itself only needs the displayed equation and \(\gamma(0)=1\). The maximal-frequency step is exhaustive because three integers each at most \(m\) can sum to \(3m\) only when all three equal \(m\).

## Relationship to prior work
Tran derives the displayed nonlinear autocorrelation equation formally from the proposed large-dimensional limit of the dihedral Morley-simplex system, records the \(x=0\) variance consequence, and states that existence of the profile and convergence of the discrete solutions remain open. The same paper proposes solving this integral equation and controlling its linearization as one possible route to the remaining dimensions. The source does not state the integrated cubic-moment identity, the modewise Fourier-positivity identity, or the obstruction to finite Fourier support. These consequences sharpen the structural information available about any exact solution of the proposed limiting equation and rule out every exact finite-harmonic ansatz.

## Limitations
This result is a necessary-condition theorem, not an existence theorem. It does not prove convergence of the discrete dihedral solutions, does not establish regularity beyond continuity, and does not rule out approximating an exact solution by finite Fourier truncations. The source equation itself is presented as a formal continuum limit, so any application back to finite Morley simplices still requires a separate convergence and error analysis.

## References
Quang Hung Tran, *Morley Simplices in Higher Dimensions: Regularity, Reflections, and Counterexamples*, arXiv:2610.01216v1, 2026. In particular, Section 9 gives the formal limiting integral equation and Section 11.1 proposes solving it as a route to the remaining dimensions.
