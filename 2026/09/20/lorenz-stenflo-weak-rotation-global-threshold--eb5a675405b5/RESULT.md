# Exact weak-rotation global stability threshold for the Lorenz–Stenflo origin

## Result

Consider the classical Lorenz–Stenflo system
\[
\dot x=\sigma(y-x)+sv,\qquad
\dot y=\rho x-y-xz,\qquad
\dot z=xy-\beta z,\qquad
\dot v=-x-\sigma v,
\tag{1}
\]
with \(\sigma,\beta,\rho,s>0\).  Assume the rotation parameter is in the weak-rotation range
\[
0<s\le \frac{\sigma^2}{3}.
\tag{2}
\]
Then the origin is globally asymptotically stable **if and only if**
\[
\boxed{\rho\le \rho_c:=1+\frac{s}{\sigma^2}.}
\tag{3}
\]

The equality case is part of the theorem: at \(\rho=\rho_c\) the origin is nonhyperbolic, but it is still globally asymptotically stable.  Thus in the range (2), the global stability boundary closes exactly at the static pitchfork threshold already identified in the bifurcation literature; there is no finite-amplitude compact recurrent dynamics hidden on the stable side or at the threshold.

For \(\rho>\rho_c\), the origin is linearly unstable and the familiar pair of nonzero equilibria exists:
\[
v=-\frac{x}{\sigma},\qquad
y=\rho_c x,\qquad
z=\rho-\rho_c,\qquad
x^2=\frac{\beta(\rho-\rho_c)}{\rho_c}.
\tag{4}
\]

## Exact storage identity

Put
\[
k=\sqrt{\sigma^2-3s},\qquad K=\sigma^2+s,\qquad
M=\frac{\sigma^2}{K}.
\tag{5}
\]
Under (2), \(0\le k<\sigma\).  Define
\[
P=
\begin{pmatrix}
\dfrac{4\sigma-k}{\sigma(2\sigma+k)}
&
\dfrac{2(\sigma-k)}{2\sigma+k}
\\[1.2ex]
\dfrac{2(\sigma-k)}{2\sigma+k}
&
\dfrac{(\sigma-k)^2(4\sigma+k)}
{3\sigma(2\sigma+k)}
\end{pmatrix}
\tag{6}
\]
and
\[
S(x,v)=\frac12
\begin{pmatrix}x&v\end{pmatrix}
P
\binom{x}{v}.
\tag{7}
\]
Its determinant is
\[
\det P=
\frac{(\sigma-k)^2(2\sigma-k)}
{3\sigma^2(2\sigma+k)}>0,
\tag{8}
\]
and \(P_{11}>0\), so \(P\) is positive definite.

The \((x,v)\)-subsystem is linear when \(y\) is regarded as an input:
\[
\binom{\dot x}{\dot v}
=
\begin{pmatrix}-\sigma&s\\-1&-\sigma\end{pmatrix}
\binom{x}{v}
+\binom{\sigma}{0}y.
\tag{9}
\]
For
\[
\psi=
\sqrt{\frac{2}{K}}
\left[
\sigma y-(2\sigma-k)x
-\frac{(2\sigma-k)(\sigma-k)}{3}v
\right],
\tag{10}
\]
direct differentiation gives the exact factorization
\[
\boxed{M y^2-xy-\dot S=\frac12\psi^2.}
\tag{11}
\]

This identity is the key point: it is lossless at zero frequency precisely at the weak-rotation threshold and supplies the cross terms that the usual diagonal energy misses.

## Global proof

The quadratic Lorenz coupling cancels from the \((y,z)\)-energy:
\[
\frac12\frac{d}{dt}(y^2+z^2)
=\rho xy-y^2-\beta z^2.
\tag{12}
\]
Set
\[
V=\frac12(y^2+z^2)+\rho S(x,v).
\tag{13}
\]
Because \(P>0\), \(V\) is positive definite and radially unbounded.  Combining (11) and (12),
\[
\boxed{
\dot V
=-(1-\rho M)y^2-\beta z^2-\frac{\rho}{2}\psi^2.
}
\tag{14}
\]
Since \(1/M=1+s/\sigma^2=\rho_c\), equation (14) is nonpositive whenever \(\rho\le\rho_c\).  In particular all forward solutions are bounded and global.

If \(\rho<\rho_c\), an invariant trajectory in \(\{\dot V=0\}\) must have \(y=z=\psi=0\).  Then \(\dot y=\rho x\) forces \(x=0\), and \(\dot x=sv\) forces \(v=0\).  LaSalle's invariance principle therefore gives convergence to the origin.

At the critical value \(\rho=\rho_c\), (14) only forces \(z=\psi=0\).  Let a complete bounded trajectory remain in this zero-dissipation set.  Since \(z\equiv0\),
\[
0=\dot z=xy.
\tag{15}
\]
If \(x\) were nonzero at some time, continuity would make \(x\ne0\) on an interval, hence \(y=0\) on that interval; but then
\[
\dot y=\rho_c x\ne0,
\]
a contradiction.  Thus \(x\equiv0\).  The remaining equations are
\[
\dot y=-y,\qquad \dot v=-\sigma v,\qquad \sigma y+sv=0.
\tag{16}
\]
Any nonzero solution of (16) is unbounded backward in time, so the only complete bounded trajectory contained in the zero-dissipation set is the origin.  LaSalle again yields global convergence.  The positive definiteness of \(V\) also gives Lyapunov stability, proving global asymptotic stability at equality.

For the converse, the \(z\)-direction of the linearization contributes the eigenvalue \(-\beta\).  The characteristic polynomial of the \((x,y,v)\)-block is
\[
p(\lambda)=
\lambda^3+(2\sigma+1)\lambda^2
+(\sigma^2+2\sigma+s-\sigma\rho)\lambda
+\sigma^2+s-\sigma^2\rho.
\tag{17}
\]
If \(\rho>\rho_c\), then \(p(0)<0\) while \(p(\lambda)\to+\infty\) as \(\lambda\to+\infty\).  Hence \(p\) has a positive real root, so the origin is unstable.  This proves the if-and-only-if statement.

## Why the condition \(s\le \sigma^2/3\) appears

The stable linear filter (9), from input \(y\) to output \(x\), has transfer function
\[
H(\lambda)=
\frac{\sigma(\lambda+\sigma)}
{(\lambda+\sigma)^2+s}.
\tag{18}
\]
On the imaginary axis,
\[
\Re H(i\omega)=
\frac{\sigma^2(\sigma^2+s+\omega^2)}
{\omega^4+2(\sigma^2-s)\omega^2+(\sigma^2+s)^2}.
\tag{19}
\]
Its maximum occurs at \(\omega=0\) exactly when \(s\le\sigma^2/3\), and then
\[
\max_{\omega\in\mathbb R}\Re H(i\omega)
=\frac{\sigma^2}{\sigma^2+s}=M.
\tag{20}
\]
Thus the weak-rotation condition is not an artifact of a rough estimate: it is the point at which the most dangerous passive gain remains the static mode.  For \(s>\sigma^2/3\) the maximizing frequency moves away from zero, so this storage mechanism no longer reaches the static pitchfork threshold.  No claim is made here that (3) is the global stability boundary in that stronger-rotation regime.

## Relation to prior literature

Stenflo introduced (1) as a four-dimensional extension of the Lorenz equations for finite-amplitude acoustic-gravity waves in a rotating atmosphere [1].  Xavier and Rech subsequently used Descartes' rule and Routh–Hurwitz analysis to locate the fixed-point pitchfork and Hopf bifurcations and mapped periodic and chaotic regimes [2].  The pitchfork location underlying (3) is therefore prior work; the contribution here is the nonlinear global closure of the origin's stability region, including the nonhyperbolic equality case, in the explicit weak-rotation parameter range.

Wang, Li and Hu studied solution bounds for the Lorenz–Stenflo system [3], while Zhang and Xiao proved global boundedness and constructed globally attractive sets for all positive parameters [4].  These global trapping results do not state convergence of every trajectory to the origin up to the pitchfork boundary.  Passivity has also been used for controlled Lorenz–Stenflo synchronization and chaos suppression [5], whereas (11) is an unforced storage identity used to obtain an intrinsic parameter threshold.

A 2023 symbolic-computation study derives parameter conditions for local stability and zero-Hopf bifurcation [6].  A 2023 Journal of Nonlinear Science study treats periodic attractors and transport at large Rayleigh number and explicitly includes Lorenz–Stenflo as an extended Lorenz model [7].  Neither accessible statement gives the weak-rotation global if-and-only-if theorem above.  A 2026 paper on nonautonomous extended Lorenz-84 and high-order Lorenj–Stenflo systems reports global stability results for different generalized models with time-varying parameters [8]; its full theorem statements were not available for direct comparison, so it remains a residual prior-coverage risk rather than evidence of coverage.

To the best of our knowledge, the exact theorem (3), the explicit factorization (11), and the proof that the pitchfork boundary itself remains globally attracting in the classical four-dimensional Lorenz–Stenflo system have not been stated previously.

## Limitations

- The exact if-and-only-if global threshold is proved only for \(0<s\le\sigma^2/3\).  Stronger rotation is not classified.
- The result concerns the classical autonomous four-dimensional Lorenz–Stenflo equations (1), not fractional, stochastic, controlled, modified, or high-order extensions.
- The theorem identifies the complete global stability boundary of the origin in the stated range but does not classify the dynamics after the pitchfork.
- The 2023 symbolic-stability chapter and the 2026 nonautonomous generalized-system paper could not be checked in full; they are the most relevant residual originality risks found.
- Originality is asserted only to the best of our knowledge.

## Reproducibility

`artifacts/verify_storage.py` symbolically checks the storage identity, the determinant of \(P\), and the characteristic polynomial after the weak-rotation parametrization \(s=(\sigma^2-k^2)/3\).  `artifacts/verification.txt` records the verified zero residuals.

## References

1. L. Stenflo, *Generalized Lorenz equations for acoustic-gravity waves in the atmosphere*, Physica Scripta **53** (1996), 83–84. https://doi.org/10.1088/0031-8949/53/1/015
2. J. C. Xavier and P. C. Rech, *Regular and Chaotic Dynamics of the Lorenz–Stenflo System*, International Journal of Bifurcation and Chaos **20** (2010), 145–152. https://doi.org/10.1142/S0218127410025466
3. P. Wang, D. Li and Q. Hu, *Bounds of the hyper-chaotic Lorenz-Stenflo system*, Communications in Nonlinear Science and Numerical Simulation **15** (2010), 2514–2520. https://doi.org/10.1016/j.cnsns.2009.09.015
4. F. Zhang and M. Xiao, *Complex Dynamical Behaviors of Lorenz-Stenflo Equations*, Mathematics **7** (2019), 513. https://doi.org/10.3390/math7060513
5. Y. Uyaroğlu and S. Emiroğlu, *Passivity-based chaos control and synchronization of the four dimensional Lorenz-Stenflo system via one input*, Journal of Vibration and Control **21** (2015), 1657–1664. https://doi.org/10.1177/1077546313501186
6. B. Huang, X. Li, W. Niu and S. Xie, *Stability and Zero-Hopf Bifurcation Analysis of the Lorenz–Stenflo System Using Symbolic Methods*, in Computer Algebra in Scientific Computing, LNCS (2023), 183–198. https://doi.org/10.1007/978-3-031-41724-5_10
7. I. Ovsyannikov, J. D. M. Rademacher, R. Welter and B.-Y. Lu, *Time Averages and Periodic Attractors at High Rayleigh Number for Lorenz-like Models*, Journal of Nonlinear Science (2023). https://doi.org/10.1007/s00332-023-09933-x
8. M. F. M. Naser, M. Abdel Aal and G. Gumah, *Global stability analysis of two nonautonomous generalized Lorenz systems with time-varying parameters*, SeMA Journal (2026). https://doi.org/10.1007/s40324-026-00429-8
