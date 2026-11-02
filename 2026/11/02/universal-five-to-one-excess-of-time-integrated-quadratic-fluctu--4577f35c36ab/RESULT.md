# Universal five-to-one excess of time-integrated quadratic fluctuations under resetting Brownian forcing

## Finding

Consider the stationary, linearly confined position of a particle driven by Brownian forcing that resets to zero at independent Poisson times. Compare it with a **Gaussian active Ornstein–Uhlenbeck (OU) model matched at every two-time position covariance**. The two models have identical stationary position variance and identical autocovariance functions, yet the long-time variance rates of their time-integrated squared positions are different for every positive reset and confinement rate.

Write the confinement rate as \(\mu>0\), forcing reset rate as \(r>0\), forcing diffusivity as \(D>0\), and linear coupling as \(\kappa>0\). For the centered quadratic additive functional
\[
Q_T=\int_0^T\left(X_t^2-\mathbb E_\pi[X^2]\right)\,dt,
\]
its asymptotic variance rate and the covariance-matched Gaussian rate are respectively
\[
\boxed{\Sigma_{\rm reset}=\lim_{T\to\infty}\frac{\operatorname{Var}_\pi Q_T}{T}
=\frac{8D^2\kappa^4\left(r^3+26r^2\mu+31r\mu^2+10\mu^3\right)}{\mu^3r^3(r+\mu)^3(r+2\mu)}}
\]
and
\[
\boxed{\Sigma_{\rm G}=\frac{8D^2\kappa^4(r^2+3r\mu+\mu^2)}{\mu^3r^3(r+\mu)^3}}.
\]
The excess is **strictly positive**:
\[
\boxed{\Sigma_{\rm reset}-\Sigma_{\rm G}
=\frac{8D^2\kappa^4\left(21r^2+24r\mu+8\mu^2\right)}{\mu^2r^3(r+\mu)^3(r+2\mu)}>0.}
\]
Moreover, setting \(z=r/\mu\), the scale-free amplification factor is
\[
\boxed{\mathcal R(z)=\frac{\Sigma_{\rm reset}}{\Sigma_{\rm G}}
=\frac{z^3+26z^2+31z+10}{(z+2)(z^2+3z+1)}}.
\]
It is strictly decreasing for every \(z>0\), with sharp unattained limits \(\mathcal R(0+)=5\) and \(\mathcal R(+\infty)=1\). Thus the **single dimensionless ratio of two quadratic long-time fluctuation rates uniquely determines \(r/\mu\)**. At \(r=\mu=D=\kappa=1\), the two variance rates are exactly \(68/3\) and \(5\), a ratio of \(68/15\).

Both centered additive functionals obey central limit theorems, with their respective rates as limiting Gaussian variances:
\[
T^{-1/2}Q_T\ \Longrightarrow\ N(0,\Sigma_{\rm reset}).
\]

## Assumptions and scope

Let \(W\) be Brownian motion, and let \(N\) be an independent Poisson process of constant rate \(r>0\). The resetting noise \(Y\) satisfies \(dY_t=\sqrt{2D}\,dW_t\) between jumps of \(N\), and at each jump instant \(Y_t=0\). The particle is **not** reset and satisfies the ordinary random differential equation
\[
\dot X_t=-\mu X_t+\kappa Y_t.
\]
All rates, \(D\), and \(\kappa\) are strictly positive. Denote the unique joint invariant law by \(\pi\), and start \((X,Y)\) in that law. The comparison process \((X^{\rm G},Y^{\rm G})\) is jointly stationary and given by
\[
\dot X^{\rm G}=-\mu X^{\rm G}+\kappa Y^{\rm G},
\qquad dY^{\rm G}=-rY^{\rm G}\,dt+2\sqrt D\,dB_t,
\]
where \(B\) is Brownian motion. Its forcing covariance agrees exactly with that of the resetting noise. In the source model, the coupling is \(\kappa=r\), obtained by substitution into all formulas. No assumption of an observation-noise channel or of full resets of the particle is made.

## Proof

**1. Invariant moments and matched two-point laws.** The joint generator of the resetting system is
\[
\mathcal L f(x,y)=(-\mu x+\kappa y)\partial_x f+D\partial_{yy}f
+r\,[f(x,0)-f(x,y)].
\]
Coupling two copies with a common noise and reset clock shows that their forcing coordinates agree from the first common reset onward, and their position discrepancy thereafter decays as \(e^{-\mu t}\). This constructs the unique invariant regime. All its polynomial moments exist: the reset forcing has a Gaussian law conditional on its exponentially distributed age; the confined position is an exponentially weighted integral of that forcing. The same coupling, with polynomial moment bounds, gives integrability of all polynomial stationary correlations used below.

Set \(M_{ij}=\mathbb E_\pi[X^iY^j]\). Stationarity of monomials gives, for nonnegative integers \(i,j\) other than \((0,0)\),
\[
(i\mu+r\mathbf1_{\{j>0\}})M_{ij}
=i\kappa M_{i-1,j+1}+Dj(j-1)M_{i,j-2},
\]
with terms having negative indices omitted and \(M_{00}=1\). The relevant initial moments are
\[
M_{02}=\frac{2D}{r},\qquad M_{11}=\frac{2D\kappa}{r(\mu+r)},
\qquad M_{20}=\frac{2D\kappa^2}{\mu r(\mu+r)}.
\]
The independent resetting forcing has stationary covariance
\(\mathbb E_\pi[Y_0Y_t]=(2D/r)e^{-rt}\) for \(t\ge0\). The Gaussian OU forcing has exactly that covariance. Linear filtering therefore gives identical position autocovariances in both systems:
\[
C_X(t)=M_{20}\frac{r e^{-\mu t}-\mu e^{-rt}}{r-\mu}
\quad(r\ne\mu,\ t\ge0),
\]
with continuous resonant expression \(C_X(t)=M_{20}(1+\mu t)e^{-\mu t}\) at \(r=\mu\).

**2. Exact quadratic Poisson equation.** Put \(g(x,y)=x^2-M_{20}\). The quadratic polynomial
\[
h(x,y)=\frac{x^2}{2\mu}
+\frac{\kappa xy}{\mu(\mu+r)}
+\frac{\kappa^2y^2}{\mu r(\mu+r)}
\]
solves \(-\mathcal Lh=g\) identically, including the constant term. To verify this directly, the \(x^2\), \(xy\), and \(y^2\) coefficients are respectively \(-1\), \(0\), \(0\) in \(\mathcal Lh\), and the constant term equals \(M_{20}\).

The polynomial moment recurrence yields
\[
\begin{aligned}
M_{04}&=\frac{24D^2}{r^2},\\
M_{13}&=\frac{\kappa M_{04}+6D M_{11}}{\mu+r},\\
M_{22}&=\frac{2\kappa M_{13}+2D M_{20}}{2\mu+r},\\
M_{31}&=\frac{3\kappa M_{22}}{3\mu+r},\qquad
M_{40}=\frac{\kappa M_{31}}{\mu}.
\end{aligned}
\]
Writing \(h=A x^2+Bxy+Cy^2\), the Poisson identity and the stationary Green–Kubo formula give
\[
\begin{split}
\Sigma_{\rm reset}=2\mathbb E_\pi[gh]=2\{&A(M_{40}-M_{20}^2)
+B(M_{31}-M_{20}M_{11})\\
&+C(M_{22}-M_{20}M_{02})\}.
\end{split}
\]
Substituting the displayed moments and reducing common factors gives exactly the boxed formula for \(\Sigma_{\rm reset}\).

**3. Independent martingale-variance identity and central limit theorem.** Itô's formula, including the jumps of the forcing, shows that
\[
\mathcal M_T=h(X_T,Y_T)-h(X_0,Y_0)+Q_T
\]
is a square-integrable martingale with predictable quadratic-variation density
\[
\Gamma h(x,y)=2D(Bx+2Cy)^2+r(Bxy+Cy^2)^2.
\]
The stationary identity \(\mathbb E_\pi[\Gamma h]=2\mathbb E_\pi[gh]\) gives a second, positive-sum computation of the exact same variance rate. The stationary ergodic theorem yields \(T^{-1}\langle\mathcal M\rangle_T\to\mathbb E_\pi[\Gamma h]\). Polynomial moment finiteness implies the jump Lindeberg condition; the continuous Brownian martingale part has its usual conditional variance. The martingale central limit theorem applies. The endpoint difference \(h(X_T,Y_T)-h(X_0,Y_0)\) has uniformly bounded second moment, and hence vanishes upon division by \(\sqrt T\). This proves the stated central limit theorem. Moreover, \(\mathbb E[\mathcal M_T^2]=T\mathbb E_\pi[\Gamma h]\) and Cauchy–Schwarz make the endpoint contribution to \(T^{-1}\operatorname{Var}(Q_T)\) vanish, establishing the variance limit as well.

**4. Gaussian benchmark, excess and sharp monotonicity.** A centered stationary Gaussian process satisfies the exact Wick relation
\(\operatorname{Cov}((X_0^{\rm G})^2,(X_t^{\rm G})^2)=2C_X(t)^2\). Hence
\[
\Sigma_{\rm G}=4\int_0^\infty C_X(t)^2\,dt.
\]
Termwise integration of the three exponentials, followed by continuity at \(r=\mu\), gives the second boxed formula. Subtracting yields the displayed strictly positive excess. In terms of \(z=r/\mu\), differentiation gives
\[
\mathcal R'(z)=-\frac{21z^4+48z^3-3z^2-4z+8}
{(z+2)^2(z^2+3z+1)^2}.
\]
The numerator is strictly positive: for \(0<z\le1\), its constant and negative terms alone give at least \(8-3-4=1\); for \(z\ge1\), the grouping \(21z^4+z(48z^2-3z-4)+8\) is positive. The endpoint limits are \(5\) and \(1\). This proves strict monotonicity, the sharp strict bound \(1<\mathcal R(z)<5\), and unique reconstruction of the rate ratio from this normalized quadratic fluctuation measurement.

## Verification

The standalone file `verify.py` reconstructs all joint stationary moments through total degree four using exact rational arithmetic and the generator recurrence. For 150 rational parameter tuples it separately evaluates the Green–Kubo/Poisson expression, the quadratic-variation expression, the claimed closed form, the Gaussian autocorrelation integral (including resonance), the excess, and the normalized ratio. All checks pass. It also verifies the unit-rate instance and the endpoint/strict-derivative algebraic certificates. Run `python3 verify.py` with the standard library only.

These finite parameter diagnostics do not establish positivity for all real rates or a stochastic central limit theorem; those statements are proved analytically above.

## Relationship to prior work

Guéneau, Majumdar and Schehr [1] introduced and analyzed this harmonically confined particle driven by Brownian forcing reset at Poisson epochs (with \(\kappa=r\)). In particular, their sections on stationary moments, stationary two-time position covariance and time-dependent one-time moments, and appendices E, G and H, provide existing results used as input here. The covariance-matched active OU comparison is also suggested there. The present claim **does not** assert novelty of the model, its stationary second/fourth moments, the reset-forcing autocovariance, the position covariance or the Poisson-equation technique. Its target is instead the integrated **two-time fourth-order** observable, the exact variance-rate excess over a genuinely covariance-indistinguishable Gaussian process, and the sharp five-to-one monotone identification law. Two-time covariance equality or an excess fourth moment at a single time does not alone determine the sign or magnitude of the integrated squared-position covariance.

The chain study [2] treats multiple coupled oscillators driven by reset Brownian boundary noise and studies stationary non-Gaussianity and velocity two-time correlations, rather than this scalar quadratic time-average comparison. The general resetting review [3] supplies background but not the specific variance ratio. These source comparisons are not a proof of publication priority.

## Limitations

Only the stated linear one-dimensional harmonic trap, independent Poisson resets of the **forcing only**, positive parameters, and stationary starts are covered. The Gaussian reference is a covariance-matched comparator, not an assertion of thermodynamic equilibrium. The strict ratio endpoints are limits rather than attainable positive-rate parameter values. At vanishing coupling or diffusivity both variance rates vanish and the ratio is undefined; these boundary cases are excluded. The result does not establish large-deviation rates, finite-time fluctuation dominance, noisy-observation identifiability, or an analogous theorem for non-Poisson reset clocks. No independent scientific validation has been performed; unindexed broader nonlinear-functional literature might overlap the specific result.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, first submitted June 15, 2023. https://arxiv.org/html/2306.09453v2 (especially §§4–5 and Appendices E, G, H).
2. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127, first submitted July 12, 2023. https://arxiv.org/abs/2307.06127.
3. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A 53 (2020), DOI:10.1088/1751-8121/ab7cfe.
