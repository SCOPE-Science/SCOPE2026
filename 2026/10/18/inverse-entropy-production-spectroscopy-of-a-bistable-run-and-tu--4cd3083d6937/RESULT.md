# Inverse entropy-production spectroscopy of a bistable run-and-tumble particle

## Finding
Fix a known thermal diffusion constant \(T>0\). For any \(a,b>0\), let the symmetric cusp double-well potential be
\[
U_{a,b}(x)=b\bigl||x|-a\bigr|.
\]
Let \(\sigma_t\in\{-1,+1\}\) flip at Poisson rate \(r>0\), independently of standard Brownian motion \(B_t\). The particle obeys
\[
 dX_t=\bigl[-U_{a,b}'(X_t)+v\sigma_t\bigr]dt+\sqrt{2T}\,dB_t.
\]
The force at the three corners is immaterial, since these points have zero occupation time. For \(|v|<b\) the system has a unique steady law. Let \(\Pi_{a,b}(v,r)\) be its stationary *total* entropy-production rate including the orientation state, with the normalization given by the stationary-current formula below. Define the weak-propulsion response
\[
\chi_{a,b}(r)=\lim_{v\to0}\frac{\Pi_{a,b}(v,r)}{v^2}.
\]
Then this limit exists for every \(r>0\) and is strictly positive, strictly increasing, strictly concave, and real analytic on \((0,\infty)\). Its two asymptotic tails are
\[
\boxed{\lim_{r\downarrow0}\frac{T^2\chi_{a,b}(r)}{2r}=\frac{2T^2}{b^2}+\frac{2a^2}{2-e^{-ab/T}}},
\qquad
\boxed{\lim_{r\to\infty}2rT^2\left(\frac1T-\chi_{a,b}(r)\right)=b^2}.
\]
Consequently **the two asymptotic response coefficients alone determine both \(a\) and \(b\) uniquely when \(T\) is known**. In fact, knowledge of \(\chi_{a,b}\) on any nonempty open subinterval of positive rates determines both parameters uniquely, in the mathematical exact-data sense. More generally the whole response curve determines the equilibrium positional covariance function, not just these two parameters.

## Assumptions and scope
All \(a,b,T,r\) are strictly positive, and the order of limits is stationary state first, propulsion amplitude \(v\to0\) second, followed by \(r\to0\) or \(r\to\infty\). The weak-propulsion response is not a claim about the monotonicity of entropy production at arbitrary fixed nonzero \(v\). The external force is \(f=-U'\) almost everywhere; it has magnitude \(b\) away from three cusp points. The entropy-production convention is
\[
\Pi(v,r)=\frac{v}{T}\int_{\mathbb R}(J_+(x)-J_-(x))\,dx,
\quad J_\pm=(f\pm v)p_\pm-T\partial_xp_\pm,
\]
where \(p_\pm\) are the stationary joint spatial densities (not the conditional densities). This is the full-state stationary dissipation convention used in the cited primary literature; it is not the entropy production of the position-only coarse-grained process.

## Proof
**Step 1 (equilibrium operator).** At \(v=0\), the equilibrium position density is \(\pi(x)=Z^{-1}e^{-U_{a,b}(x)/T}\). On the weighted space \(L^2(\pi dx)\), let
\[
L=T\partial_{xx}+f\partial_x,
\qquad K=-L.
\]
The diffusion is reversible, so \(K\) is nonnegative self-adjoint. The exponential tails and finite one-dimensional barrier ensure a Poincare spectral gap; its kernel consists of constants. The centered observable \(g(x)=x-\int x\pi(dx)=x\) lies in the generator domain, and \(Kg=-f\). Integration by parts gives the exact Dirichlet energy
\[
\langle g,Kg\rangle_\pi=T\int|g'|^2\pi(dx)=T.
\]
The force is bounded, so \(\|Kg\|^2_\pi=\int f^2\pi(dx)=b^2\).

**Step 2 (weak-propulsion stationary response).** Write \(P=p_++p_-\) and \(D=p_+-p_-\). The stationary Fokker--Planck equations are exactly
\[
0=L^*P-v\partial_xD,\qquad0=(L^*-2r)D-v\partial_xP.
\]
At fixed positive \(r\), the spectral gaps of the reversible diffusion and the orientation mode permit differentiation of the unique normalized stationary solution around \(v=0\) (the first-order drift perturbation is relatively bounded in the appropriate weighted Sobolev graph norm). In particular,
\[
P=\pi+O(v^2),\qquad D=vq+O(v^3),
\quad q=-(2r-L^*)^{-1}\pi'.
\]
These relations also follow directly by differentiating the matched stationary ODE solutions separately across the three cusps, with continuous densities and fluxes and exponential decay at infinity. Detailed balance implies \(L^*(\pi h)=\pi Lh\); since \(\pi'=(f/T)\pi\),
\[
q=-\frac\pi T(2r+K)^{-1}f.
\]
The exact entropy-production current identity reduces to
\[
\Pi(v,r)=\frac{v^2}{T}+\frac vT\int f(x)D(x)\,dx,
\]
because \(\int\partial_xD=0\), \(\int P=1\), and the stationary total positional current vanishes on the confining line. Thus
\[
\chi(r)=\frac1T-\frac1{T^2}\langle f,(2r+K)^{-1}f\rangle_\pi.
\]

**Step 3 (positive spectral measure).** Let \(\mu\) be the positive spectral measure of \(g\) for \(K\), supported on positive spectral values since \(g\) is centered. Using \(f=-Kg\) and \(\int\lambda\,\mu(d\lambda)=T\), obtain
\[
\boxed{\chi(r)=\frac{2r}{T^2}\int_{(0,\infty)}\frac{\lambda}{\lambda+2r}\,\mu(d\lambda)}.
\]
Nonzero \(g\) makes \(\mu\) nonzero. Differentiating for each \(r>0\), with the spectral moment bound, yields
\[
\chi'(r)=\frac2{T^2}\int\frac{\lambda^2}{(\lambda+2r)^2}\,\mu(d\lambda)>0,
\quad
\chi''(r)=-\frac8{T^2}\int\frac{\lambda^2}{(\lambda+2r)^3}\,\mu(d\lambda)<0.
\]
The same resolvent is holomorphic off the negative real spectral axis, proving real analyticity for positive \(r\). Moreover \(0<\chi(r)<1/T\).

**Step 4 (the exact two tails).** Since constants have been projected away, dominated convergence gives
\[
\lim_{r\downarrow0}\frac{T^2\chi(r)}{2r}=\mu((0,\infty))=\operatorname{Var}_\pi(X).
\]
Also, from the resolvent expression in Step 2,
\[
\lim_{r\to\infty}2rT^2\left(\frac1T-\chi(r)\right)
=\lim_{r\to\infty}\langle f,2r(2r+K)^{-1}f\rangle_\pi
=\|f\|^2_\pi=b^2.
\]
Both limits use spectral dominated convergence, not an interchange of flip-rate and propulsion limits.

**Step 5 (closed equilibrium variance and inverse identification).** Set \(\alpha=b/T\). Symmetry makes the mean zero. Directly integrating on the positive half-line gives
\[
\int_0^\infty e^{-\alpha||x|-a|}dx=\frac{2-e^{-\alpha a}}\alpha,
\quad
\int_0^\infty x^2e^{-\alpha||x|-a|}dx
=\frac{2a^2}\alpha+\frac{4-2e^{-\alpha a}}{\alpha^3}.
\]
Therefore
\[
V(a,b,T)=\operatorname{Var}_\pi(X)=\frac{2T^2}{b^2}+\frac{2a^2}{2-e^{-ab/T}}.
\]
The high-rate coefficient first determines \(b\) as its positive square root. For fixed \(b,T\), the derivative of the second term in \(V\) is
\[
\frac{2a[4-(2+\alpha a)e^{-\alpha a}]}{(2-e^{-\alpha a})^2}>0
\quad(a>0),
\]
since \((2+t)e^{-t}\le2\) for \(t\ge0\). Hence the low-rate coefficient then determines the unique \(a>0\). If two response curves coincide on a nonempty open interval, real analyticity makes them coincide for all positive \(r\), and the two tails give identical \(a,b\).

**Step 6 (covariance spectroscopy).** The equilibrium time covariance is \(C(t)=\langle g,e^{-tK}g\rangle_\pi=\int e^{-\lambda t}\mu(d\lambda)\). Its Laplace transform obeys, for every \(s>0\),
\[
\int_0^\infty e^{-st}C(t)dt
=\frac{V-(T^2/s)\chi(s/2)}{s},
\qquad
V=\lim_{r\downarrow0}\frac{T^2\chi(r)}{2r}.
\]
Uniqueness of the Laplace transform recovers \(C(t)\) from the full exact response curve. Neither explicit eigenvalues nor a finite-mode approximation is assumed.

## Verification
The standalone `CHECK.py` is an independent *finite-grid consistency test*, not a proof of convergence or of any infinite-dimensional spectral result. Run it using Python with NumPy and SciPy (`python CHECK.py`). It independently quadratures the equilibrium variance, checks the positive symmetric discretization of \(K\), compares the direct resolvent response with the spectral identity, tests strict signs of the first two rate derivatives, and checks numerical small- and large-rate coefficients for several choices of positive \(a,b,T\). At packaging the checker completed 116 assertions. The analytical arguments in Steps 1--6 establish the claims for all admissible parameters.

## Relationship to prior work
Singh and Aghion (arXiv:2610.08029, first posted 2026-10-06), especially Section 7 and its stationary entropy-production Equations (44)--(46), provide the underlying bistable model and finite-propulsion dissipation expression; these are **not** novel contributions here. Paoluzzi, Puglisi and Angelani (2024) provide the general full-state entropy-production framework and the known harmonic and heterogeneous cases; those formulas are also prior work. Garcia-Millan and Pruessner (2021) calculate harmonic-trap entropy production, not the present exact inverse identification for a cusp double-well. Farago (arXiv:2509.08565) provides a different inverse-Clausius mapping to effective local temperature and entropy flux, not a tumble-rate response inversion for fixed double-well parameters. Standard reversible diffusion spectral theory and linear response are essential prior mathematical ingredients. The present result isolates their consequence for the weak-activity cusp-well *inverse problem*: identification of both well geometry parameters from two different physical response tails and complete equilibrium covariance recovery. A broader prior inverse-response theorem might subsume these claims; this literature risk remains open.

## Limitations
The theorem is a stationary weak-propulsion statement; rates tending to zero or infinity are considered only after extracting the coefficient of \(v^2\). It assumes a fixed known positive thermal diffusivity, a symmetric exactly piecewise-linear double-well, unbiased symmetric flipping, and strictly positive \(a,b\). Exact analytic reconstruction does not imply noise-robust or finite-sample reconstruction; analytic continuation and asymptotic extrapolation can be ill-conditioned. No corresponding uniqueness theorem is asserted for arbitrary potentials or for position-only entropy production. A closely related 2022 entropy-production publication by Frydel was checked to the extent of its accessible abstract, but its full text was inaccessible during the comparison, leaving a specific implicit-coverage risk.

## References
1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential*, arXiv:2610.08029v1 (first public posting 2026-10-06), https://arxiv.org/abs/2610.08029.
2. M. Paoluzzi, A. Puglisi and L. Angelani, *Entropy Production of Run-and-Tumble Particles*, Entropy 26 (2024), 443, https://doi.org/10.3390/e26060443.
3. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, J. Stat. Mech. (2021) 063203, https://doi.org/10.1088/1742-5468/ac014d.
4. O. Farago, *Inverse Clausius Thermodynamics in Run-and-Tumble Dynamics*, arXiv:2509.08565 (first posted 2025-09-10), https://arxiv.org/abs/2509.08565.
5. D. Frydel, *Intuitive view of entropy production of ideal run-and-tumble particles*, Phys. Rev. E 105 (2022), 034113, https://doi.org/10.1103/PhysRevE.105.034113.
