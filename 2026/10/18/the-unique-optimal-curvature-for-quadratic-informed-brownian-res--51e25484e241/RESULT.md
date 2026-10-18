# The unique optimal curvature for quadratic informed Brownian resetting

## Finding

Let a one-dimensional Brownian searcher with generator \(D\partial_{xx}\), \(D>0\), start at \(L>0\), be absorbed on reaching zero, and reset instantaneously to \(L\) at position-dependent Poisson intensity \(\kappa x^2\) with \(\kappa>0\), whenever it is alive. Put \(\lambda=L(\kappa/D)^{1/4}\), and define the positive decreasing function
\[
 u(z)=\frac{\sqrt{2z}}{\Gamma(1/4)}K_{1/4}(z^2/2),\quad u(0)=1,\qquad I(z)=\int_z^\infty u(t)\,dt.
\]
Here \(K_{1/4}\) denotes the modified Bessel function of the second kind. The exact mean absorption time is
\[
 \mathbb E_L[\tau_0]=\frac{L^2}{D}\,\Phi(\lambda),\qquad
 \Phi(\lambda)=\frac1{\lambda^2}\int_0^\lambda\frac{I(s)}{u(s)^2}\,ds.
\]
There is **exactly one** optimal positive curvature. Let \(h(z)=I(z)/u(z)^2\) and \(m(z)=\int_0^z h(s)\,ds\). Then \(\lambda_*\) is the **unique positive** solution of the fully specified analytic equation
\[
 \lambda_* h(\lambda_*)=2m(\lambda_*),\qquad
 \kappa_*=\frac{D}{L^4}\lambda_*^4.
\]
Numerical quadrature (not certified interval arithmetic) gives \(\lambda_*\approx1.5484851757\), \(\lambda_*^4\approx5.7494752406\), and the dimensionless optimum \(\Phi(\lambda_*)\approx0.9392900105\). These numbers refine the previously simulation-based estimate of about \(5.6\) for the same parabolic curvature.

## Assumptions and scope

Space is the half-line \([0,\infty)\), with absorbing endpoint zero. Motion between resets is Brownian diffusion of variance \(2Dt\); the instantaneous reset rate at position \(x\) is exactly \(\kappa x^2\), with no refractory or travel time. Each reset renews the process from the *fixed* point \(L\). The result holds for every \(D,L,\kappa>0\); it is not a theorem about finite-sensing-range sigmoidal reset rates. The scientific source's limit \(b\gg L\) motivates this exact parabolic model but no finite-\(b\) approximation error is asserted.

## Proof

**1. First-reset renewal and the killed oscillator.** Scale space by \((\kappa/D)^{1/4}\) and time by \((D\kappa)^{-1/2}\). The scaled diffusion has generator \(\partial_{zz}\), killing/reset intensity \(z^2\), and initial/reset coordinate \(\lambda\). Let \(T\) be its hitting time of zero without resets, and \(R\) the first state-dependent reset alarm. Its success probability \(p(z)=\mathbb P_z(T<R)\) satisfies the Feynman–Kac boundary problem
\[
 p''(z)=z^2p(z),\qquad p(0)=1,\quad p(\infty)=0.
\]
The unique decaying solution is \(p=u\), with \(u\) as above. Write \(q(z)=\mathbb E_z[\min(T,R)]\). It solves \(-q''+z^2q=1\), \(q(0)=0\), with its bounded-at-infinity solution. Since the process restarts independently at \(\lambda\), the renewal identity is \(M=q(\lambda)+(1-u(\lambda))M\), hence \(M=q(\lambda)/u(\lambda)\).

**2. Exact quadrature.** Define \(v(z)=u(z)\int_0^z u(t)^{-2}dt\). It satisfies \(v(0)=0\), \(v'(0)=1\), and the homogeneous equation, with Wronskian \(uv'-u'v=1\). The half-line Dirichlet Green kernel of \(-\partial_{zz}+z^2\) is \(G(z,t)=v(\min\{z,t\})u(\max\{z,t\})\). Therefore
\[
 \frac{q(z)}{u(z)}=\int_0^zv(t)dt+\frac{v(z)}{u(z)}\int_z^\infty u(t)dt.
\]
Differentiation, using \((v/u)'=u^{-2}\), gives \((q/u)'=I/u^2=h\). Since \(q(0)=0\), we obtain \(M=m(\lambda)\) and the stated physical-time formula.

**3. Strict convexity lemma.** We prove \(h''(z)>0\) on \([0,\infty)\), rather than assuming numerical unimodality. Put \(a=-u'/u>0\) and \(b=I/u>0\). Then
\[
 a'=a^2-z^2,\qquad b'=ab-1,\qquad
 h''=\frac{2}{u}\left[(3a^2-z^2)b-\frac32a\right].
\]
First, \((u'^2-z^2u^2)'=-2zu^2\), and decay of \(u,u'\) at infinity proves \(a'>0\). To see \(a'<1\), use the independent positive-integral representation
\[
 u(z)=e^{-z^2/2}\frac{\int_0^\infty t^{-1/2}e^{-t^2/2-\sqrt2zt}\,dt}{\int_0^\infty t^{-1/2}e^{-t^2/2}\,dt}.
\]
The logarithmic second derivative of this expression is \(-1+2\operatorname{Var}_z(t)\), where the variance is computed under its exponentially tilted positive density. Thus \(0<a'(z)=1-2\operatorname{Var}_z(t)<1\). In particular, \(a(z)>z\) for \(z>0\).

Set \(H=(3a^2-z^2)b-3a/2\). The standard small-argument Bessel expansion and a Bessel integral give
\[
 a(0)=\frac{2\Gamma(3/4)}{\Gamma(1/4)},\qquad b(0)=I(0)=\frac{\sqrt\pi}{2}.
\]
Consequently \(H(0)>0\) is equivalent to \(2\sqrt\pi\,\Gamma(3/4)>\Gamma(1/4)\). For an elementary strict proof, Euler reflection gives \(\Gamma(1/4)\Gamma(3/4)=\pi\sqrt2\), while the positive-term expansion \(\log\Gamma(1-t)=\gamma t+\sum_{j\ge2}\zeta(j)t^j/j\) at \(t=1/4\), together with \(\gamma>1/2\), yields \(\Gamma(3/4)^2>e^{1/4}>\sqrt{\pi/2}\).

As \(z\to\infty\), Bessel asymptotics give \(a(z)\sim z\), \(b(z)\sim1/z\), and \(H(z)\sim z/2>0\). At *any* positive zero of \(H\), differentiation and substitution of \(H=0\) yield the exact identity
\[
 H'(z)=\frac{z\,[3a'(z)z-6a(z)-2z^3]}{2(3a(z)^2-z^2)}<0,
\]
using \(a'<1\) and \(a>z\). Since \(H\) is positive both at zero and eventually, and every positive zero would have strictly negative derivative, it has no zero. Therefore \(H>0\) and \(h''>0\) everywhere.

**4. Global uniqueness.** Let \(F(z)=zh(z)-2m(z)\). Then \(F(0)=0\), \(F'(0)=-h(0)<0\), and \(F''(z)=zh''(z)>0\) for every \(z>0\). The large-argument Bessel expansion gives \(u(z)\asymp z^{-1/2}e^{-z^2/2}\), \(I(z)\sim u(z)/z\), and \(m(z)\sim h(z)/z\), so \(F(z)\to+\infty\). Strict convexity yields exactly one positive zero, crossing from negative to positive. Finally, \(\Phi'(z)=F(z)/z^3\); also \(\Phi(z)\to\infty\) at zero and infinity. Hence this stationary point is the sole global minimum, proving the theorem.

## Verification

The included `verify.py` independently evaluates the Bessel quadrature and finite-difference absorbing-boundary generator. Its root solve, dimensionless minimum, and scaling tests can be reproduced with Python 3, NumPy and SciPy by running `python verify.py`. A finite-difference grid on \([0,7]\) with mesh \(0.0125\) and remote reflecting boundary agrees with the exact mean at five positive curvatures to better than \(2.3\times10^{-5}\); mesh halving exhibits the expected second-order error reduction. This finite computation is not a proof of continuum uniqueness, and the printed root digits are non-certified numerical approximations.

## Relationship to prior work

Keidar, Blumer, Hirshberg and Reuveni introduced informed position-dependent resetting and, in the small-curvature/large-sensing-range parabolic regime, reported a simulation-based estimate \(\kappa_*L^4/D\simeq5.6\) while explicitly identifying the lack of an analytical optimizer expression. The exact Feynman–Kac and renewal frameworks are their prior art; the finding here is the exact scalar special-function criterion together with the **global uniqueness proof** for the quadratic profile, not the general adaptive-reset framework. Roldán and Gupta previously solved harmonic-oscillator path integrals and stationary densities for quadratic reset intensities. Their inspected analysis concerns propagators, first-reset distributions, and stationary confinement rather than the absorbing half-line first-passage optimizer. Related constant-rate first-passage optimization does not subsume the quadratic position-dependent control. The source-to-claim comparison remains subject to independent mathematical review.

## Limitations

The optimal curvature is characterized as the unique zero of an explicit analytic integral equation, not as an elementary closed-form number. The numerical value uses non-validated floating-point quadrature. No finite-\(b\) error bound for the sigmoid \(r_0 x^2/(b^2+x^2)\), robustness to drift, or higher-dimensional analogue is established. Broader unpublished equivalent results or implicit consequences of spectral theory cannot be excluded by literature search alone; independent originality verification remains outstanding.

## References

1. T. D. Keidar, O. Blumer, B. Hirshberg and S. Reuveni, *Adaptive Resetting for Informed Search Strategies and the Design of Non-equilibrium Steady-States*, arXiv:2409.14419v1 (first public 22 September 2024), full arXiv v2 (17 March 2025), Nature Communications 16, 7259 (2025), DOI:10.1038/s41467-025-62398-2; particularly the environmental-information search and its equation (8), Fig. 3, and stated open analytic curvature question.
2. E. Roldán and S. Gupta, *Path-integral formalism for stochastic resetting: Exactly solved examples and shortcuts to confinement*, arXiv:1703.10615 (2017), Physical Review E 96, 022130 (2017); especially Sec. III.2 on parabolic resetting and the first-reset/steady-state analysis.
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters 106, 160601 (2011), for the classical fixed-rate resetting framework.
