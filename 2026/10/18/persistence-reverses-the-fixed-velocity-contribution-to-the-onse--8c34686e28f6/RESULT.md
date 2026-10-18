# Persistence reverses the fixed-velocity contribution to the onset of beneficial resetting

## Finding

For a Brownian searcher on a reflecting–absorbing interval with weak Ornstein–Uhlenbeck propulsion, the *linear response* of the onset of beneficial Poisson resetting to a prescribed reset velocity changes sign between slow and fast propulsion relaxation. This contrasts two physically distinct effects of directing the searcher away from the absorbing target: persistent outward motion increases the range of starting positions where weak resetting helps, while rapidly relaxing outward motion decreases it.

Precisely, fix any \(\eta>0\), \(\sigma\in\{-1,+1\}\), and let \(x_*=1-1/\sqrt5\). For sufficiently small real \(a\), a smooth critical initial position \(x_c(a,\sigma,\eta)\) exists near \(x_*\), separating *locally* negative and positive derivatives of mean hitting time with respect to the Poisson reset rate at zero. It satisfies
\[
 x_c(a,\sigma,\eta)=x_*+\sigma a\,\chi(\eta)+O_\eta(a^2).
\]
The susceptibility \(\chi(\eta)\) is given exactly by the elementary Dirichlet–Neumann resolvent formula below, and obeys
\[
 \boxed{\lim_{\eta\downarrow0}\chi(\eta)=\frac4{125}>0,\qquad
 \chi(\eta)=-\frac1\eta+O(\eta^{-2})\quad(\eta\to\infty).}
\]
Thus at least one positive propulsion-relaxation parameter reverses the signed effect of the reset velocity on the resetting-benefit threshold. Direct numerical evaluation locates a crossing at approximately \(\eta=0.2112213694\), but uniqueness of this crossing is **not** claimed or proved.

## Assumptions and scope

Fix dimensionless diffusivity one and interval \([0,1]\). The position is absorbed on hitting zero and is instantaneously reflected at one (Skorokhod reflection). Between resets the independent Brownian motions \(W,B\) drive
\[
 dX_t=aY_t\,dt+\sqrt2\,dW_t-dK_t,\qquad
 dY_t=-\eta Y_t\,dt+\sqrt{2\eta}\,dB_t,
\]
with \(X_0=x\in(0,1)\), \(Y_0=\sigma\in\{-1,+1\}\); \(K\) is the upper reflecting regulator. The physical propulsion velocity is \(aY\); in particular, the strength of the OU fluctuations *and* the prescribed initial/reset propulsion velocity vanish proportionally to \(a\). This scaling is important and differs from a protocol that holds an order-one velocity fixed while taking the OU noise to zero.

At each independent Poisson reset of rate \(r\ge0\), both coordinates are returned to \((x,\sigma)\). Let \(\mathcal T_{a,\sigma,\eta}(x)\) be the hitting time of zero without resets, and let \(M(r,a,x,\sigma,\eta)\) be its mean with resets. The comparison concerns the derivative \(\partial_r M\) at \(r=0\), **not** the global optimal reset rate or finite-rate monotonicity. The local threshold is the root near \(x_*\) of \(\partial_r M(0,a,x,\sigma,\eta)=0\).

Write \(m_0(x)=x-x^2/2\), \(s_0(x)=2x/3-x^3/3+x^4/12\), and define the positive resolvent \(R_\eta=(-\partial_x^2+\eta)^{-1}\) with Dirichlet condition at zero and Neumann condition at one. Its *explicit kernel* is
\[
 G_\eta(x,y)=\frac{\sinh(\sqrt\eta\min\{x,y\})\cosh(\sqrt\eta[1-\max\{x,y\}])}
 {\sqrt\eta\cosh\sqrt\eta},\quad (R_\eta f)(x)=\int_0^1G_\eta(x,y)f(y)\,dy.
\]
Set \(u=R_\eta(1-x)\) and \(h=R_\eta(2/3-x^2+x^3/3)\). The exact all-\(\eta\) susceptibility is
\[
 \boxed{\chi(\eta)=\frac{15}{2\sqrt5}
 \left[h(x_*)+2(R_\eta u)(x_*)-4m_0(x_*)u(x_*)\right].}
\]
This is a finite, explicit one- and two-fold integral of elementary hyperbolic functions. Equivalently, with \(k=\sqrt\eta\), it is an elementary formula without any quadrature: \(R_\eta u=-\partial_\eta u\), where
\[
 u(x)=\frac{1-x}{k^2}+\frac{\sinh(kx)}{k^3\cosh k}
       -\frac{\cosh(k(1-x))}{k^2\cosh k},
\]
\[
 h(x)=\frac{2/3-x^2+x^3/3}{k^2}+\frac{2x-2}{k^4}
       -\left(\frac{2}{3k^2}-\frac2{k^4}\right)\frac{\cosh(k(1-x))}{\cosh k}
       +\left(\frac1{k^3}-\frac2{k^5}\right)\frac{\sinh(kx)}{\cosh k}.
\]
These expressions specify all parameters and eliminate any numerical or spectral cutoff from the theorem.

## Proof

**1. The passive restarting boundary.** At \(a=0\), the propulsion process decouples from position. The first two nonreset hitting-time moments solve the backward equations \(m_0''=-1\), \(s_0''=-2m_0\), each with zero value at \(x=0\) and zero derivative at \(x=1\). Integrating gives the polynomials above. For an arbitrary nonnegative completion time \(T\) with two moments, the renewal identity for full Poisson restart gives
\[
 M(r)=\frac{1-\mathbb E[e^{-rT}]}{r\,\mathbb E[e^{-rT}]},\qquad
 \left.\partial_rM\right|_{r=0}=(\mathbb ET)^2-\tfrac12\mathbb ET^2.
\]
Define the benefit discriminant \(\mathcal B=\mathbb ET^2-2(\mathbb ET)^2\). Weak resetting helps exactly when \(\mathcal B>0\). The passive polynomial factorization is
\[
 \mathcal B_0(x)=s_0(x)-2m_0(x)^2
       =-\frac{x(x-2)(5x^2-10x+4)}{12}.
\]
Its only interior zero is \(x_*\), it is positive for \(0<x<x_*\), negative for \(x_*<x<1\), and
\[
 \mathcal B_0'(x_*)=-\frac{2\sqrt5}{15}\ne0.
\]

**2. Linear response to a fixed reset orientation.** The no-reset backward generator on the joint position–OU state is
\[
 \mathcal L_a=\partial_x^2+a y\partial_x+\eta(\partial_y^2-y\partial_y).
\]
The two hitting-time moments \(m_a,s_a\) solve \(\mathcal L_a m_a=-1\), \(\mathcal L_a s_a=-2m_a\), with absorbing Dirichlet and reflecting Neumann conditions in \(x\). The initial OU value is \(y=\sigma\). At first order in \(a\), use the ansatz
\[
 m_a(x,y)=m_0(x)+a y\,u(x)+O_\eta(a^2),\qquad
 s_a(x,y)=s_0(x)+a y\,v(x)+O_\eta(a^2).
\]
Since the OU generator takes \(y\) to \(-\eta y\), coefficient comparison yields exactly
\[
 (-\partial_x^2+\eta)u=m_0'=1-x,
 \quad (-\partial_x^2+\eta)v=s_0'+2u.
\]
All four coefficient boundary conditions are Dirichlet at zero and Neumann at one, giving \(u=R_\eta m_0'\), \(v=R_\eta s_0'+2R_\eta^2m_0'\). The displayed kernel follows by matching homogeneous solutions at the point source and their derivative jump. The closed hyperbolic formulas follow by direct differentiation and enforcement of both boundary conditions.

Differentiability of moments at \(a=0\) can also be justified without a formal series: on a finite time interval use the standard stopped-path drift change of measure relative to the reflected Brownian process. The OU path is Gaussian, and for sufficiently small \(|a|\) its exponential quadratic moment grows at a rate smaller than the strictly positive killed Brownian spectral gap. Truncation at large times then permits differentiation of the integral representations for the first two hitting-time moments. The displayed backward problems are the resulting unique first variations. This argument is for each fixed \(\eta>0\) and for \(x\) in a compact interior neighborhood of \(x_*\).

Consequently, evaluated at \(y=\sigma\),
\[
 \mathcal B_a(x,\sigma)=\mathcal B_0(x)
 +a\sigma\,[v(x)-4m_0(x)u(x)]+O_\eta(a^2).
\]
The implicit-function theorem at the simple passive zero gives the claimed local root and, using \(\mathcal B_0'(x_*)=-2\sqrt5/15\), the exact \(\chi(\eta)\).

**3. The slow-relaxation sign.** The resolvent converges at \(\eta\downarrow0\) to the Dirichlet–Neumann inverse of \(-\partial_x^2\). Integrating the relevant polynomial forcing gives
\[
 u_0(x)=\frac{x}{2}-\frac{x^2}{2}+\frac{x^3}{6},\quad
 h_0(x)=\frac{5x}{12}-\frac{x^2}{3}+\frac{x^4}{12}-\frac{x^5}{60},
\]
\[
 (R_0u_0)(x)=\frac{x}{8}-\frac{x^3}{12}+\frac{x^4}{24}-\frac{x^5}{120}.
\]
The first variation of the benefit discriminant at the passive zero simplifies *exactly* to
\[
 [h_0+2R_0u_0-4m_0u_0](x_*)=\frac{8\sqrt5}{1875}.
\]
Therefore \(\chi(0+)=4/125>0\).

**4. The rapid-relaxation sign.** At the interior point \(x_*\), the displayed elementary hyperbolic formulas or standard resolvent estimates give
\[
 u(x_*)=\frac{m_0'(x_*)}{\eta}+O(\eta^{-2}),\qquad
 h(x_*)=\frac{s_0'(x_*)}{\eta}+O(\eta^{-2}),\qquad
 (R_\eta u)(x_*)=O(\eta^{-2}).
\]
The exponentially small boundary-layer terms do not affect these estimates because \(0<x_*<1\). Hence the bracket in the formula for \(\chi\) equals \(\mathcal B_0'(x_*)/\eta+O(\eta^{-2})\). Multiplication by \(15/(2\sqrt5)\) yields \(\chi(\eta)=-1/\eta+O(\eta^{-2})\). The Green resolvent depends continuously on \(\eta\), including at zero, so these opposite signs force at least one reversal by the intermediate value theorem. This concludes the proof.

## Verification

The standalone `verify.py` reproduces the \(4/125\) limit using exact rational and algebraic identities, compares the elementary susceptibility with independently nested Green-kernel quadratures at six positive relaxation rates, and tests the predicted coefficient against a direct finite-amplitude backward generator discretization with seven Hermite modes of the OU variable. The latter discretization independently computes the first two hitting-time moments and estimates the derivative of the resetting-benefit root using central differences in \(a\). Differences from the exact linear response are below \(4\times10^{-6}\) at the three reported rates. These numerical checks corroborate the analytical proof and are **not** used to assert uniqueness of a reversal or to replace the continuum argument.

## Relationship to prior work

Georgiou, Bressloff and Bertrand (2026) introduce the same reflecting–absorbing AOUP hitting-time/resetting setting, derive weak-activity results for Gaussian velocity reinitialization, and report *numerical-only* phase boundaries for protocols with a prescribed initial/reset velocity (their Sec. 3.4, especially discussion of Fig. 9). Their numerical phase plots fix velocity to \(\pm1\) **in the rescaled OU coordinate**, which is consistent with a physical reset velocity proportional to the activity amplitude as specified here; the article does not calculate the resulting zero-amplitude susceptibility or its persistence asymptotics. The relevant full-text sections were inspected. This paper's new statement is the analytic, all-persistence first variation for the fixed-velocity protocol and the rigorous existence of an orientation-response sign reversal in the weak-amplitude regime.

Pal and Reuveni (2017) establish the general restart renewal law and the criterion involving coefficient of variation, both used as known machinery above; those results alone do not determine the OU fixed-orientation susceptibility. Wang (2021) develops weak-activity Hermite perturbations near boundaries; this general method likewise does not state the present signed reset-onset asymptotics. Exact fixed-drift Brownian results correspond only to the singular \(\eta\downarrow0\) end, not the persistence-dependent reversal.

## Limitations

The result proves a *local* shift of the onset of beneficial infinitesimal resetting, not a global classification for every reset rate or every initial position. The theorem does not show that the zero of \(\chi(\eta)\) is unique, despite the observed numerical crossing near \(0.21122\). The prescribed velocity and OU fluctuation amplitude scale together with \(a\); results should not be extrapolated to protocols with fixed order-one initial speed at vanishing noise. The proof treats strictly positive translational diffusion, finite confinement, and a reset of **both** position and velocity. All external comparisons remain subject to the possibility of unlocated more general perturbation formulas.

## References

1. D. K. Georgiou, P. C. Bressloff and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein–Uhlenbeck particle*, arXiv:2609.21124v1, first posted 2026-09-17. https://arxiv.org/abs/2609.21124
2. A. Pal and S. Reuveni, *First Passage Under Restart*, Physical Review Letters **118** (2017), 030603; arXiv:1607.06048. https://arxiv.org/html/1607.06048v3
3. M. Wang, *On the effect of boundaries on noninteracting weakly active particles in different geometries*, Physical Review E **103** (2021), 042609; arXiv:2102.00711. https://arxiv.org/abs/2102.00711
