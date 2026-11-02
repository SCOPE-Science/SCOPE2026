# Three universal Zak zeros for an odd symmetric-pole rational window

## Finding
For the rational window
\[
g(s)=\frac{s}{(s^2+1)(s^2+4)},\qquad g_\beta(s)=g(s/\beta),\qquad\beta>0,
\]
define its Zak transform by
\[
Z_\beta(t,\xi)=\sum_{m\in\mathbb Z}g_\beta(t-m)e^{2\pi i m\xi}.
\]
**Theorem.** For **every** real \(\beta>0\), the complete zero set in the half-open fundamental square \([0,1)\times[0,1)\) is exactly
\[
\boxed{\{(0,0),(\tfrac12,0),(0,\tfrac12)\}.}
\]
Thus no additional Zak zeros can emerge as the window dilation varies. This is a statement about the scalar Zak transform, not a classification of Gabor frame lattices.

## Assumptions and scope
The variables \(t,\xi\) are real. The positive parameter \(\beta\) is arbitrary and fixed during each zero calculation. The series is absolutely convergent because \(g_\beta(t-m)=O_\beta(|m|^{-3})\), uniformly in \(t\) on compact sets. Quasiperiodicity and periodicity transfer the displayed fundamental-square result to every pair of real arguments.

The Fourier convention is \(\widehat f(\omega)=\int_{\mathbb R}f(s)e^{-2\pi i s\omega}\,ds\). For all real \(\omega\), with value zero at \(\omega=0\),
\[
\widehat {g_\beta}(\omega)=-\frac{i\pi\beta}{3}\operatorname{sgn}(\omega)
 \big(e^{-2\pi\beta|\omega|}-e^{-4\pi\beta|\omega|}\big).
\]
Indeed, \(g(s)=\tfrac13\big(s/(s^2+1)-s/(s^2+4)\big)\), and the Fourier transform of \(s/(s^2+a^2)\) is \(-i\pi\operatorname{sgn}(\omega)e^{-2\pi a|\omega|}\) for nonzero frequency, in the distributional sense, with the difference continuous at the origin. This immediately gives an absolutely summable Zak Fourier representation.

## Proof
**1. Rational form.** Put \(q=e^{-2\pi\beta}\in(0,1)\), \(z=e^{2\pi it}\), and for \(0\le\xi<1\) set \(x=q^\xi\) and \(y=q^{1-\xi}=q/x\). Poisson summation, which is applicable here because both \(g_\beta\) and its Fourier transform have integrable decay, gives
\[
Z_\beta(t,\xi)=-\frac{i\pi\beta}{3}e^{2\pi it\xi}F(z),\qquad
F(z)=\frac{x}{1-qz}-\frac{x^2}{1-q^2z}-\frac{y}{z-q}+\frac{y^2}{z-q^2}.
\]
For \(\xi=0\), the zero-frequency term vanishes, so the same formula follows directly by absolute convergence. None of the four denominators vanishes for \(|z|=1\).

Clearing denominators after multiplication by the nonzero \(x^2\), the equation \(Z_\beta=0\) is exactly \(N(z)=0\), where
\[
\begin{aligned}
N(z)={}&x^3\big[(1-x)+q(x-q)z\big](z-q)(z-q^2)\\
&-q\big[(x-q)z+q^2(1-x)\big](1-qz)(1-q^2z).
\end{aligned}
\]
Here \(N\) is a real-coefficient cubic in \(z\).

**2. Interior frequencies.** If \(0<\xi<1\), then \(q<x<1\). Write \(N(z)=a_3z^3+a_2z^2+a_1z+a_0\). Its leading and constant coefficients are
\[
a_3=q(x-q)^2(q^2+qx+x^2)>0,
\quad a_0=-q^3(x-1)^2(x^2+x+1)<0.
\]
A nonreal unit-circle root of a real cubic must occur together with its reciprocal conjugate. Factoring the cubic as \(a_3(z^2-2cz+1)(z-r)\) for real \(c,r\) implies the necessary coefficient identity
\[
a_3(a_1-a_3)-a_0a_2+a_0^2=0.
\]
An exact polynomial expansion gives
\[
\begin{aligned}
a_3(a_1-a_3)-a_0a_2+a_0^2
={}&q^2x(x^2-q)(q-1)^3(q^2+q+1)\\
&\times\big[x^4+(1+q)^2x^2+q^2\big].
\end{aligned}
\]
All factors other than \(x^2-q\) are strictly nonzero for \(0<q<x<1\). Hence any nonreal unimodular root requires \(x^2=q\), equivalently \(\xi=1/2\).

The only real points on \(|z|=1\) are \(z=1\) and \(z=-1\). Their exact values factor as
\[
N(1)=(x-q)(x^2-q)(q-1)^3(q+1)(x-1)
\]
and
\[
\begin{aligned}
N(-1)={}&-(x-q)(q+1)(q^2+1)(x-1)\\
&\times(q^2+qx^2+2qx+q+x^2).
\end{aligned}
\]
Thus \(z=-1\) cannot be a zero at interior frequencies; \(z=1\) requires \(\xi=1/2\).

It remains to exclude nonreal unit-circle roots at \(\xi=1/2\). Set \(u=\sqrt q\in(0,1)\), so \(x=u\), \(q=u^2\). Direct factorization yields
\[
N(z)=u^3(u-1)^2(u^2+u+1)(z-1)
\left[u^3(z^2+1)+(u^6+u^4+2u^3+u^2+1)z\right].
\]
For \(|z|=1\), divide the bracket by \(z\). Its first term is \(u^3(z+z^{-1})\), a real number of magnitude at most \(2u^3\), whereas the remaining positive constant is
\(u^6+u^4+2u^3+u^2+1>2u^3\). Hence the bracket never vanishes. The sole interior-frequency zero is \((t,\xi)=(0,1/2)\).

**3. Boundary frequency.** At \(\xi=0\), we have \(x=1\), and the cubic simplifies exactly to
\[
N(z)=q(q-1)^2(q^2+q+1)z(z-1)(z+1).
\]
On the unit circle, the only zeros are \(z=1\) and \(z=-1\), giving \((0,0)\) and \((1/2,0)\). These three points are distinct in the chosen half-open fundamental square, completing the proof.

## Verification
The accompanying `checker.py` recomputes the rational clearing-of-denominators identity, the coefficient obstruction, all four special factorizations, and the middle-frequency quadratic factor with exact symbolic algebra. It also compares the Fourier-series formula with convergent direct Zak sums at three sample triples. Execute `python checker.py` after installing the dependencies in `requirements.txt`. The symbolic factorization checks verify algebra; the strict inequalities and zero-set exhaustiveness follow from the analytical proof above, not from finite sampling.

## Relationship to prior work
Ghosh [1] introduces this exact window and its partial-fraction Zak representation, proves a reciprocity identity for the associated cubic, and studies rational-density Gabor frame matrices. In particular, the polynomial at frequency \(1/2\) is known to be anti-self-reciprocal. The present conclusion is different: it identifies **all** scalar Zak zeros for **every** positive dilation parameter, excluding off-symmetry zeros through a coefficient obstruction and a strict quadratic inequality. Neither the frame theorems nor the reflection identity alone imply this three-point zero set.

Belov, Kulikov and Lyubarskii [2] prove rational-function frame results for Herglotz windows and a generic irrational-density criterion; these concern frame membership, not an all-dilation scalar Zak-zero census. Janssen [3] and Kloos–Stöckler [4] analyze few-zero Zak transforms for one-sided, nonnegative, superconvex, or totally positive windows. The present window changes sign and has imaginary-axis poles on both sides, so those window-class classifications do not directly give this claim.

## Limitations
A scalar Zak-zero census does not solve the rational-density frame-set problem, since the latter is governed by ranks of coupled Zibulski–Zeevi matrices. No claim is made for higher members of the rational-window family, general odd rational functions, or nonrectangular frames. The algebraic proof is complete under the stated definitions; novelty is assessed against the inspected sources, with possible implicit equivalent formulations in older literature remaining a historical-priority risk. No independent mathematical audit is asserted.

## References
[1] R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568, first public version 2026-08-11, https://arxiv.org/abs/2608.10568.

[2] Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959 (2021), https://arxiv.org/abs/2103.08959.

[3] A. J. E. M. Janssen, *Zak Transforms With Few Zeros and the Tie*, in *Advances in Gabor Analysis*, 2003, DOI:10.1007/978-1-4612-0133-5_3.

[4] T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, *Journal of Approximation Theory* 184 (2014), 209–237, arXiv:1311.7359.
