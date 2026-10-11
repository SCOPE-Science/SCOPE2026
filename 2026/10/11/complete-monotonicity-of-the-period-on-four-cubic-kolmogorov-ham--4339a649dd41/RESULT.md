# Complete monotonicity of the period on four cubic Kolmogorov Hamiltonian centers

## Finding
For every triple \(a,b,C>0\), the cubic Hamiltonian system
\[
\dot x=x(C-a x^2-3b y^2),\qquad
\dot y=y(3a x^2+b y^2-C)
\]
possesses four bounded period annuli, one in each quadrant inside the ellipse \(a x^2+b y^2=C\). Write \(H(x,y)=xy(a x^2+b y^2-C)\). On each annulus the absolute Hamiltonian level \(h=|H|\) varies over \(0<h<h_*:=C^2/(8\sqrt{ab})\). All four annuli have the same minimal period in the original time, namely
\[
T(h)=\frac{4}{C\sqrt{1+t}}K\!\left(\sqrt{\frac{1-t}{1+t}}\right),\qquad t=\frac{8h\sqrt{ab}}{C^2},
\]
where the modulus-convention complete elliptic integral is \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\phi)^{-1/2}\,d\phi\).

The period is **strictly completely monotone**: \((-1)^n T^{(n)}(h)>0\) for every integer \(n\ge0\) and every \(0<h<h_*\). Its center and outer-boundary laws are
\[
\lim_{h\uparrow h_*}T(h)=\frac{\sqrt2\pi}{C},\qquad
T(h)=\frac2C\log\!\left(\frac{C^2}{h\sqrt{ab}}\right)+o(1)\quad(h\downarrow0).
\]
In particular the period has no interior critical value, is strictly convex, and diverges at every outer separatrix.

## Assumptions and scope
The three parameters \(a,b,C\) are strictly positive. Energy is measured by the positive absolute value \(h\) of the displayed *specific* Hamiltonian, rather than by a time-reparameterized or normalized energy. Both the period and its asymptotics refer to the original physical time in the displayed differential equations. The four annuli are the bounded portions of the four open quadrants satisfying \(a x^2+b y^2<C\); their limiting axes and ellipse belong to the zero-energy separatrix graph, not to periodic ovals. The four centers occur at \((\pm\sqrt{C/(4a)},\pm\sqrt{C/(4b)})\). This assertion is not for polynomial factors with an \(xy\) cross term.

## Proof
**Hamiltonian geometry.** Direct differentiation gives \(\dot x=-\partial_yH\) and \(\dot y=\partial_xH\); in particular \(H\) is constant on trajectories. The positive, invertible linear scaling \(X=\sqrt{a/C}\,x\), \(Y=\sqrt{b/C}\,y\), \(\tau=Ct_{\mathrm{physical}}\) reduces the vector field to
\[
\frac{dX}{d\tau}=X(1-X^2-3Y^2),\quad
\frac{dY}{d\tau}=Y(3X^2+Y^2-1),\quad
H=\frac{C^2}{\sqrt{ab}}XY(X^2+Y^2-1).
\]
In the unit first-quadrant disk, \(f=XY(1-X^2-Y^2)>0\), and \(\log f=\log X+\log Y+\log(1-X^2-Y^2)\) has everywhere negative-definite Hessian: the two logarithmic-coordinate terms already contribute a strictly negative-definite diagonal Hessian, while the final term is concave. It tends to minus infinity at the boundary. Its unique maximizer is \(X=Y=1/2\), with maximum \(1/8\). Consequently each intermediate level \(f=e\), \(0<e<1/8\), is a smooth simple compact strictly convex oval (the boundary of a strictly convex superlevel set), with nowhere vanishing Hamiltonian vector field. Each is one periodic orbit. Coordinate reflections conjugate the flow without changing time, proving the four-annulus assertion.

**Exact physical-time quadrature.** Work in the reduced system's time \(\tau\), where \(X=r\cos\theta\), \(Y=r\sin\theta\), \(z=r^2\) and \(0<\theta<\pi/2\). An explicit calculation gives
\[
\frac{dz}{d\tau}=2z(1-z)\cos(2\theta),\qquad e=\frac12z(1-z)\sin(2\theta).
\]
Set \(q=2e\in(0,1/4)\) and \(t=4q=8e=8h\sqrt{ab}/C^2\). A complete orbit consists of two traversals, in opposite radial directions, between \(z_\pm=(1\pm\sqrt{1-t})/2\). Therefore the minimal reduced-time period is exactly
\[
\mathcal T(e)=\int_{z_-}^{z_+}\frac{dz}{\sqrt{z^2(1-z)^2-q^2}}.
\]
Substitute \(z=(1+\sqrt{1-t}\cos\phi)/2\); cancellation of the factor \(\sqrt{1-t}\sin\phi\) yields
\[
\mathcal T(e)=4\int_0^{\pi/2}\!\frac{d\phi}{\sqrt{1+t-(1-t)\sin^2\phi}}
=\frac4{\sqrt{1+t}}K\!\left(\sqrt{\frac{1-t}{1+t}}\right).
\]
Because \(\tau=Ct_{\mathrm{physical}}\), the original-time period is \(T=\mathcal T/C\). The formula also reads
\[
T(h)=\frac4C\int_0^{\pi/2}\!\big[\cos^2\phi+t(1+\sin^2\phi)\big]^{-1/2}\,d\phi.
\]
No change of physical time remains hidden in this identity.

**Every derivative has the strict alternating sign.** For \(h\) in any compact subinterval of \((0,h_*)\), the integrand and all its \(h\)-derivatives are jointly bounded by integrable functions. Dominated differentiation gives for each integer \(n\ge0\), with \((1/2)_0=1\),
\[
(-1)^nT^{(n)}(h)=\frac4C\left(\frac{8\sqrt{ab}}{C^2}\right)^n(1/2)_n
\int_0^{\pi/2}\frac{(1+\sin^2\phi)^n\,d\phi}
{[\cos^2\phi+t(1+\sin^2\phi)]^{n+1/2}}>0.
\]
Here \((1/2)_n=\prod_{j=0}^{n-1}(j+1/2)\) for \(n\ge1\). Every factor and the integral are strictly positive. This proves complete monotonicity, including strict decrease and strict convexity, and excludes critical periods without a finite-order truncation.

**Endpoints.** Dominated convergence at \(t\uparrow1\) gives \(T\to(4/C)(\pi/2)/\sqrt2=\sqrt2\pi/C\). At \(t\downarrow0\), the complementary elliptic modulus satisfies \(k'^2=1-k^2=2t/(1+t)\). The standard elliptic asymptotic \(K(k)=\log(4/k')+O(k'^2\log(1/k'))\) then yields
\[
T(h)=\frac2C\log\frac8t+O\!\left(t\log(1/t)\right)
=\frac2C\log\frac{C^2}{h\sqrt{ab}}+O\!\left(\frac{h\sqrt{ab}}{C^2}\log\frac{C^2}{h\sqrt{ab}}\right),
\]
where the last bound is understood as \(h\downarrow0\) for fixed parameters. This proves the stated sharp additive normalization and the center limit. \(\square\)

## Verification
The independent algebraic steps of the proof are the Hamiltonian derivatives, positive scaling, polar radial equation, substitution endpoints, and the last positive-integral derivative formula. The standalone `verify_period.py` checks multiple parameter-scaled numerical quadratures against an independently evaluated arithmetic–geometric-mean elliptic integral and confirms sample endpoint constants. Run with Python 3 standard library: `python verify_period.py`. The script is a finite reproducibility check, **not** a certificate for the infinite family of derivative inequalities; those follow from the displayed exact integral and justified differentiation.

## Relationship to prior work
He, Liu and Xiao (arXiv:2303.14403, first public 2023-03-25) classify cubic Hamiltonian Kolmogorov systems with four centers, their invariant lines, and the corresponding phase-portrait types; the relevant Section 5.1 supplies topological background, not a period formula or higher derivative signs. The separable-Hamiltonian period theory of Villadelprat and Zhang (2019 online / 2020 volume) gives general monotonicity and critical-point criteria, but its inspected full text presents neither the specific axis-aligned four-center family nor the stated exact elliptic period and strict all-orders inequalities. Nascimento (2026) develops related sufficient conditions for monotonicity of separable Hamiltonians; those first-derivative criteria do not state this complete-monotonicity result. The present calculation also gives the explicit separatrix additive constant and the original-time normalization; generic Hamiltonian topology alone implies none of these quantitative identities.

## Limitations
The result does **not** assert strict complete monotonicity for every cubic Hamiltonian with four centers, for general cross terms in the quadratic factor, or for non-Hamiltonian Kolmogorov fields. It does not address perturbative persistence of periodic orbits or a general classification of critical periods outside the displayed family. A general period criterion may independently imply weaker monotonicity without giving the complete sequence of strict derivatives. Reproducibility checks sample finitely many parameters; the universal statements rest solely on the analytic proof. Publication priority is not a claim of exhaustive coverage of all literature.

## References
- H. He, C. Liu and D. Xiao, *Centers and invariant straight lines of planar real polynomial vector fields and its configurations*, arXiv:2303.14403v1 (25 March 2023), especially Section 5.1. https://arxiv.org/abs/2303.14403
- J. Villadelprat and X. Zhang, *The period function of Hamiltonian systems with separable variables*, Journal of Dynamics and Differential Equations **32** (2020), 741–767; DOI:10.1007/s10884-019-09759-w. An openly available full-text copy was inspected.
- F. J. S. Nascimento, *Monotonicity of the Period Function in Planar Separable Hamiltonian Systems: An Extension of Chicone's Criterion*, Qualitative Theory of Dynamical Systems **25** (2026), article 166; DOI:10.1007/s12346-026-01595-w.
- A. Gasull, A. Guillamon, V. Mañosa and F. Mañosas, *The Period Function for Hamiltonian Systems with Homogeneous Nonlinearities*, Journal of Differential Equations **139** (1997), 237–260; DOI:10.1006/jdeq.1997.3296.
