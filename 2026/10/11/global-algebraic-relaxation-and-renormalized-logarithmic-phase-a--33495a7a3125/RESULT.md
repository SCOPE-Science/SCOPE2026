# Global algebraic relaxation and renormalized logarithmic phase at a cubic Liénard weak focus

## Finding

For each real parameter \(\mu\), consider
\[
\dot x=y-\mu x^2-x^3,\qquad \dot y=-x.
\]
For every nonzero real initial point the forward solution is global, bounded, and tends to the origin. With \(r(t)=\sqrt{x(t)^2+y(t)^2}\), and with any continuous lift \(\theta(t)=\arg(x(t)-i y(t))\),
\[
\boxed{\lim_{t\to\infty}t\,r(t)^2=\frac43},\qquad
\boxed{\lim_{t\to\infty}\bigl[\theta(t)-t+\tfrac{2\mu^2}{9}\log t\bigr]=\Theta\in\mathbb R.}
\]
The constant \(\Theta\) depends on the initial condition and on the lift. The logarithmic coefficient is universal across initial conditions, is nonnegative in magnitude, is unchanged under \(\mu\mapsto-\mu\), and vanishes exactly at \(\mu=0\). These limits refer to the original Euclidean coordinates and time; no time reparameterization is used.

## Assumptions and scope

Here \(\mu\in\mathbb R\) is arbitrary and fixed; the initial condition belongs to \(\mathbb R^2\setminus\{(0,0)\}\). The polynomial vector field is locally Lipschitz. Define \(F(x)=\mu x^2+x^3\). The angular lift is well defined for all finite time because no nontrivial solution of this locally Lipschitz autonomous ODE can intersect an equilibrium in finite time. We require no a priori boundedness or smallness of initial data.

## Proof

**Global boundedness.** Since \(F(x)\sim x^3\), the number
\[
K=\max\{0,\sup_{x\le0}F(x),\sup_{x\ge0}[-F(x)]\}
\]
is finite. Fix \(Y>K+1\). On any part of an orbit with \(y\ge Y\) and \(x\le0\), one has \(\dot x=y-F(x)\ge Y-F(x)>0\), while \(\dot y=-x\ge0\); thus the total increase in \(y\) before \(x=0\) is at most
\[
C_+=\int_{-\infty}^0\frac{-x}{Y-F(x)}\,dx<\infty.
\]
The integral is finite because the denominator grows cubically at the negative end. While \(y\ge Y\) and \(x\ge0\), one has \(\dot y\le0\). Crossing from \(x\ge0\) to \(x<0\) is impossible at such a height, because \(\dot x|_{x=0}=y>0\). Hence \(y(t)\le \max\{y(0),Y\}+C_+\) throughout the forward lifespan. By the symmetric argument, on \(y\le-Y\), \(x\ge0\),
\[
C_-=\int_0^\infty\frac{x}{Y+F(x)}\,dx<\infty
\]
bounds any additional downward excursion, giving \(y(t)\ge\min\{y(0),-Y\}-C_-\). Since \(y\) is bounded and \(x'=y-F(x)\) points inward for all sufficiently large positive or negative \(x\), the coordinate \(x\) is also bounded. Polynomial local well-posedness then implies global forward existence.

**Exact dissipation.** For \(\mu\ne0\), set
\[
H_\mu(x,y)=\frac12e^{-2\mu y}x^2+
\frac{1-(1+2\mu y)e^{-2\mu y}}{4\mu^2}.
\]
For \(\mu=0\), set \(H_0=(x^2+y^2)/2\). The function \(u\mapsto(1+u)e^{-u}\) has its global maximum \(1\) at \(u=0\), so \(H_\mu\ge0\), with equality only at the origin. A direct differentiation valid for every \(\mu\) gives
\[
\dot H_\mu=-e^{-2\mu y}x^4\le0
\]
(with the factor equal to \(1\) at \(\mu=0\)). The bounded positive orbit has a nonempty compact omega-limit set. On that set \(\dot H_\mu=0\), hence \(x=0\), and the only invariant subset of \(x=0\) is the origin, because \(\dot x=y\) there. LaSalle's invariance argument yields \((x(t),y(t))\to(0,0)\). Notice that \(H_\mu\) is not claimed to be globally proper: the preceding boundedness argument is indispensable.

**Return-radius and physical-time jets.** Let \(x=r\cos\theta\), \(y=-r\sin\theta\), \(c=\cos\theta\), \(s=\sin\theta\). Direct calculation gives
\[
\dot r=-\mu c^3r^2-c^4r^3,\qquad
\dot\theta=1+\mu c^2sr+c^3sr^2.
\]
For sufficiently small positive radius \(\dot\theta>0\). On the section \(\theta=0\) let \(\rho\) be the initial radius, \(P(\rho)\) the radius after one positive turn, and \(T(\rho)\) the duration in the original time. Uniform Taylor expansion of the smooth polar equations gives
\[
\frac{dr}{d\theta}=-\mu c^3r^2+(\mu^2c^5s-c^4)r^3+O(r^4),
\qquad
r(\theta)=\rho-\mu\bigl(s-s^3/3\bigr)\rho^2+O(\rho^3).
\]
Integrating the cubic term through a full turn, all odd-trigonometric pieces vanish and \(\int_0^{2\pi}c^4\,d\theta=3\pi/4\). Hence
\[
P(\rho)=\rho-\frac{3\pi}{4}\rho^3+O(\rho^4).
\]
Similarly, substitute the radial expansion into \(dt/d\theta=1/\dot\theta\). The coefficient of \(\rho\) integrates to zero. At order \(\rho^2\), the surviving integral is
\[
\mu^2\int_0^{2\pi}\left[c^2s(s-s^3/3)+c^4s^2\right]d\theta
=\mu^2\left(\frac\pi4-\frac\pi{24}+\frac\pi8\right)
=\frac{\pi\mu^2}{3}.
\]
Therefore
\[
T(\rho)=2\pi+\frac{\pi\mu^2}{3}\rho^2+O(\rho^3).
\]
The remainder orders follow from smoothness and a compact one-turn interval; no finite numerical integration is used as a proof.

**Conversion to full-time asymptotics.** As all nonzero orbits converge to the origin, they eventually cross the positive radial section once per turn. Enumerate their section radii by \(\rho_n>0\), and their crossing times by \(t_n\). The return map implies
\[
\rho_{n+1}^{-2}-\rho_n^{-2}=\frac{3\pi}{2}+O(\rho_n).
\]
First this yields \(\rho_n=O(n^{-1/2})\), then summing gives
\[
\rho_n^{-2}=\frac{3\pi}{2}n+O(\sqrt n),\qquad
\rho_n^2=\frac{2}{3\pi n}+O(n^{-3/2}).
\]
Consequently \(\sum_{k<n}\rho_k^2=(2/(3\pi))\log n+C_1+o(1)\), whereas \(\sum_{k<n}\rho_k^3\) converges. Summing the original-time return periods yields
\[
t_n=2\pi n+\frac{2\mu^2}{9}\log n+C_2+o(1).
\]
At each crossing \(\theta(t_n)=2\pi n+\theta_0\) with an integer-fixed angular offset. Thus \(\theta(t_n)-t_n+(2\mu^2/9)\log t_n\) tends to a finite constant. Between successive crossings, \(r=\rho_n+O(\rho_n^2)\) and \(\dot\theta=1+O(\rho_n)\), over intervals of bounded duration, so the correction differs from its section value by \(o(1)\). This proves the full-time renormalized phase limit. Finally \(t_n\rho_n^2\to4/3\), and the same within-turn comparison proves \(t r(t)^2\to4/3\). \(\square\)

## Verification

A standalone exact symbolic checker (`checks/verify_coefficients.py`) verifies the polynomial dissipation identity, the finite Taylor-integral coefficients \(3\pi/4\) and \(\pi\mu^2/3\), and the resulting log-phase coefficient \(2\mu^2/9\). The global boundedness argument, invariant-set argument, and infinite-iteration asymptotics above are analytic and are not replaced by the finite algebra check. A direct one-turn numerical integration for \(\mu=1\) and radii \(0.10\), \(0.05\) gives period-ratio approximations \(0.956\), \(1.004\) against the limit \(\pi/3\approx1.047\); these are sanity checks only.

## Relationship to prior work

Gasull and Giacomini study this exact degree-three Liénard family; their Corollary 7.4 excludes periodic solutions for every nonnegative linear damping coefficient. Guo (2018) gives global qualitative phase portraits for the cubic polynomial Liénard family, and Oliveira, Sánchez-Sánchez and Torregrosa (2021) derive Lyapunov/period constants for the corresponding local even/odd monomial families. These cover the qualitative absence of cycles and relevant local jets; those ingredients are **not** asserted novel. The present result concerns the precise **global**, original-time amplitude law and the existence of a finite **renormalized asymptotic angular phase** on every nontrivial orbit, including its parameter-exact logarithmic coefficient. No source inspected states that combined quantitative conclusion. Normal-form connections make residual priority risk nonzero.

## Limitations

The result is specific to the cubic coefficient normalized to \(1\) and the linear oscillator normalized to unit frequency, and to the critical zero-linear-damping surface. It does not assert a uniform convergence rate in the initial condition or in unbounded \(\mu\), nor a corresponding phase law for perturbed equations. The phase offset is coordinate- and lift-dependent; only the logarithmic coefficient has the stated invariance. Qualitative global phase portraits and the local focus/period jets predate this work. The closed-form constants are derived analytically and only for the stated parameter family.

## References

1. A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, arXiv:2210.15803 (first public 2022-10-27); *Qualitative Theory of Dynamical Systems* 22 (2023), 44, DOI: 10.1007/s12346-023-00746-7. In particular Section 7.2 and Corollary 7.4.
2. F. Guo, *Global Analysis of a Liénard System with Quadratic Damping*, *Discrete Dynamics in Nature and Society* (2018), article 1249620, DOI: 10.1155/2018/1249620. Qualitative global portrait analysis.
3. R. D. S. Oliveira, I. Sánchez-Sánchez and J. Torregrosa, *Simultaneous Bifurcation of Limit Cycles and Critical Periods*, *Qualitative Theory of Dynamical Systems* 21 (2022), 20, online 2021-12-19, DOI: 10.1007/s12346-021-00546-x. In particular Theorem 11 on local Lyapunov and period constants.
