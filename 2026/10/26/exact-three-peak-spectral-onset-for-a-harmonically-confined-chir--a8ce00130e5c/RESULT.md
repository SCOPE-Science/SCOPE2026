# Exact three-peak spectral onset for a harmonically confined chiral Brownian swimmer

## Finding
Consider a planar chiral active Brownian swimmer in an isotropic harmonic trap, observed in a stationary regime. The power spectral density of one Cartesian coordinate has an exact mode-count transition. In the natural matched-relaxation case in which the trap relaxation rate equals the rotational decorrelation rate, a central peak persists at all chirality strengths, while **two additional sideband peaks first appear at the sharp threshold**
\[
\frac{\omega^2}{\gamma^2}=\frac{108}{17}.
\]
Below threshold the spectrum is strictly decreasing with absolute frequency. At the threshold it has two horizontal nonextremal shoulders. Above it exactly three strict local maxima and two strict minima occur. The newly appearing sideband frequencies separate with an exact square-root law. For more general trap rates, an explicit open region has a central spectral minimum instead of the persistent central maximum of the matched case.

## Assumptions and scope
Let \(v,\kappa,\gamma>0\), \(\omega\in\mathbb R\). With independent standard Brownian angular increments let
\[
 d\phi_s=\omega\,ds+\sqrt{2\gamma}\,dW_s \pmod{2\pi},\qquad
 d\mathbf R_s=\bigl(-\kappa\mathbf R_s+v(\cos\phi_s,\sin\phi_s)\bigr)ds.
\]
There is **no translational thermal noise** in this theorem. Initialize the angular dynamics with its stationary uniform distribution, and define the stationary position as the convergent convolution from the infinite past. Write \(X_s\) for its first coordinate. Define the two-sided spectral density with convention
\[
 S_X(\nu)=\int_{\mathbb R}e^{-i\nu u}\,\mathbb E[X_{s+u}X_s]du.
\]
The covariance is absolutely integrable. Let \(h=(\kappa/\gamma)^2\), \(t=(\omega/\gamma)^2\), and \(z=(\nu/\gamma)^2\). An exact identity is
\[
 S_X(\nu)=\frac{v^2\gamma}{2(\kappa^2+\nu^2)}
 \left[\frac1{\gamma^2+(\nu-\omega)^2}+
 \frac1{\gamma^2+(\nu+\omega)^2}\right]
 =\frac{v^2}{\gamma^3}\frac{1+t+z}{(h+z)\bigl[z^2+2(1-t)z+(1+t)^2\bigr]}.
\]
All assertions below refer to the strictly positive **continuous spectral density** of the stationary coordinate, not to multimodality of its stationary position density.

**Matched relaxation: \(\kappa=\gamma\).** Put \(t_c=108/17\) and \(z_c=55/17\).

* If \(0\le t<t_c\), \(S_X\) strictly decreases as \(|\nu|\) grows, so \(\nu=0\) is its unique local and global maximum.
* If \(t=t_c\), this strict decrease persists except for stationary (horizontal) shoulders at \(\nu=\pm\gamma\sqrt{z_c}\). These shoulders are **not** maxima or minima.
* If \(t>t_c\), there are exactly three strict local maxima at \(\nu=0\) and \(\nu=\pm\gamma\sqrt{z_+(t)}\), and two strict local minima at \(\nu=\pm\gamma\sqrt{z_-(t)}\), where \(0<z_-(t)<z_+(t)\) are the two positive real roots of the explicit cubic below. As \(t\downarrow t_c\),
\[
 z_\pm(t)=\frac{55}{17}\pm\frac2{\sqrt5}\sqrt{t-\frac{108}{17}}+O\left(t-\frac{108}{17}\right).
\]
For large chirality, \(\nu_+=|\omega|-\gamma^2/|\omega|+O(\gamma^4/|\omega|^3)\) and the sideband-to-central peak height ratio tends to \(1/2\).

**Unequal relaxation.** For arbitrary \(h>0\), the origin is a strict local spectral minimum **with positive second frequency derivative** if and only if
\[
 h>\frac{16}{9},\qquad
 \frac{3h-2-\sqrt{h(9h-16)}}2<t<
 \frac{3h-2+\sqrt{h(9h-16)}}2.
\]
In this open region there is exactly one positive stationary squared-frequency, and the spectral density has precisely two off-centre strict maxima. The boundary surfaces, at which the second derivative at the origin is zero, are not classified by this positive-curvature criterion.

## Proof
**1. Spectrum as a harmonic filter.** Uniformity of the initial angle, independent increments, and the Fourier coefficients of Brownian motion on the circle give, for all \(u\in\mathbb R\),
\[
 \mathbb E[\cos\phi_{s+u}\cos\phi_s]
 =\tfrac12e^{-\gamma|u|}\cos(\omega u).
\]
In the stationary construction,
\[
 X_s=v\int_{-\infty}^{s} e^{-\kappa(s-a)}\cos\phi_a\,da.
\]
The convolution is pathwise bounded by \(v/\kappa\) and its covariance is integrable. Fourier transformation of the displayed angular correlation yields the two Lorentzians with factor \(\gamma/2\). The harmonic impulse response has transfer function \((\kappa+i\nu)^{-1}\); multiplying by its squared modulus yields the spectral expression in the theorem. This derivation uses no Gaussian approximation to orientation.

**2. Cubic derivative identity.** Write \(F_{h,t}(z)=(1+t+z)/Q_{h,t}(z)\), where
\[
 Q_{h,t}(z)=(h+z)\left[z^2+2(1-t)z+(1+t)^2\right].
\]
The quadratic factor is exactly \(\bigl(1+(\sqrt z-\sqrt t)^2\bigr)\bigl(1+(\sqrt z+\sqrt t)^2\bigr)>0\) for \(z\ge0\), so \(Q>0\). Differentiation yields \(F'_{h,t}=P_{h,t}/Q_{h,t}^2\) with
\[
 \begin{aligned}
 P_{h,t}(z)={}&-2z^3-(5+h+t)z^2\\
 &+2(1+t)(2t-2-h)z\\
 &-(1+t)\bigl[(1+t)^2+h(1-3t)\bigr].
 \end{aligned}
\]
Because the relation \(z=\nu^2/\gamma^2\) is strictly increasing for \(\nu>0\), the positive roots and signs of this cubic completely determine all nonzero spectral extrema. The origin is always stationary by evenness.

**3. Exact discriminant at matched relaxation.** Set \(h=1\), and abbreviate \(P_t=P_{1,t}\). Then
\[
 P_t(0)=-(1+t)(t^2-t+2)<0,
 \qquad P'_t(0)=2(1+t)(2t-3),
\]
while \(P''_t(z)=-12z-2(6+t)<0\) for \(z\ge0\). If \(t\le3/2\), \(P_t\) is strictly negative on \([0,\infty)\). If \(t>3/2\), \(P_t\) has a unique positive local maximum and at most two positive roots. Its exact cubic discriminant is
\[
 \operatorname{Disc}_z(P_t)=16t^4(1+t)(17t-108).
\]
For \(3/2<t<t_c\) it has one real root, which must be negative because \(P_t(-\infty)=+\infty>P_t(0)\). Thus \(P_t<0\) for positive \(z\). At \(t=t_c\), exact factorization gives
\[
 P_{t_c}(z)=-\frac{2}{4913}(17z-55)^2(17z+215).
\]
It is nonpositive on \([0,\infty)\) and vanishes only at \(z_c\); this is a horizontal, nonextremal shoulder. For \(t>t_c\), there are three simple real roots by the positive discriminant. The unique positive critical point is a local maximum, while the negative critical point is a local minimum; in conjunction with \(P_t(0)<0\), the three-root configuration forces two roots \(0<z_-<z_+\) and one negative root. The derivative signs are negative, positive, negative across these positive roots, giving a local minimum at \(z_-\), local maximum at \(z_+\), and the even continuation across zero yields the stated five extrema. No others are possible by cubic degree.

**4. Fold asymptotics.** The two degenerate-root equations are \(P_{t_c}(z_c)=\partial_zP_{t_c}(z_c)=0\). Exact derivatives are
\[
 \partial_tP_t(z)|_{(z_c,t_c)}=\frac{432}{17},\qquad
 \partial^2_zP_t(z)|_{(z_c,t_c)}=-\frac{1080}{17}.
\]
A second-order Taylor expansion around this fold gives
\[
 0=\frac{432}{17}(t-t_c)-\frac{540}{17}(z-z_c)^2
 +O\bigl((t-t_c)|z-z_c|+|z-z_c|^3+(t-t_c)^2\bigr),
\]
which proves the square-root coefficient \(2/\sqrt5\) and the remainder \(O(t-t_c)\). At \(|\omega|/\gamma\to\infty\), rescale frequency within \(O(\gamma)\) of \(|\omega|\) in the Lorentzian formula: the second Lorentzian is lower order and the trap factor expands smoothly. Maximizing its leading corrected Lorentzian gives the stated location and the height ratio \(1/2\); equivalently, expand the cubic's larger positive root in powers of \(t^{-1}\).

**5. The off-centre doublet.** For general \(h\),
\[
 P_{h,t}(0)=-(1+t)\left[t^2+(2-3h)t+1+h\right].
\]
The bracket is negative precisely inside the positive-root interval in the finding, and only for \(h>16/9\). Thus \(P(0)>0\) there, so the origin is a strict local minimum with positive second derivative in \(\nu\). Since \(P''_{h,t}(z)=-12z-2(5+h+t)<0\) for \(z\ge0\) and \(P\to-\infty\), a strictly concave cubic beginning positive crosses zero exactly once for positive \(z\): its derivative decreases strictly, so it first increases at most once and subsequently decreases. That root gives one pair of strict off-centre maxima.

## Verification
The accompanying standalone `spectral_verify.py` uses exact SymPy polynomial arithmetic and rational root isolation. It checks the derivative numerator, discriminant, threshold factorization, fold coefficients, origin-curvature expression, and independent parameter examples on both sides of the mode transition. The program passed **21 deterministic assertions**. The analytic sign and discriminant arguments, rather than these finite test cases, establish the global theorem. Execute with `python spectral_verify.py` with SymPy installed.

## Relationship to prior work
Pattanayak, Shee, A. Chaudhuri, and D. Chaudhuri (2026) define the same two-dimensional confined chiral active Brownian dynamics, and compute dynamical second and fourth moments, steady-state moments and kurtosis, including oscillatory behavior. Those results are **not** claimed as new. Caprini, Löwen and Marconi (2023) give the same orientation autocorrelation \(e^{-\gamma|u|}\cos(\omega u)\), as well as chiral confinement physics. The displayed Lorentzian spectral identity is an elementary consequence of that known autocorrelation and harmonic filtering; it is presented as a starting identity, **not as a new standalone discovery**. The assessed finding is the sharp and complete mode-bifurcation classification with exact threshold \(108/17\), its fold scaling and unequal-relaxation central-curvature region. The 2017 circle-swimmer harmonic-trap study concerns spatial excursions; its full text was not inspected, creating a residual coverage risk. An existing unpublished or unlocated spectral-peak classification may already imply the result.

## Limitations
The argument concerns stationary second-order frequency spectra, not transient kurtosis, spatial-density mode counts or thermal-noise-dominated observations. It excludes translational Brownian noise, delayed trap response, nonharmonic traps, and anisotropic noise. Matched relaxation is an experimentally meaningful section of the full model, but the theorem does not give the entire two-parameter mode-count phase diagram for all \(h\), nor the exact classification on the unequal-relaxation boundary surfaces. A spectral feature's mathematical existence does not establish its instrumental visibility. Earlier correlation formulas implicitly determine the power spectrum itself, so novelty is restricted to the nontrivial sharp peak-count statements; prior coverage by inaccessible historical primary literature remains possible. No independent assessment has been performed.

## References
1. A. Pattanayak, A. Shee, A. Chaudhuri, D. Chaudhuri, *Exact dynamics and dimensional effects in torque-driven trapped active Brownian particles*, arXiv:2603.26967, initial public version 27 March 2026; https://arxiv.org/html/2603.26967 .
2. L. Caprini, H. Löwen, U. M. B. Marconi, *Chiral active matter in external potentials*, Soft Matter 19 (2023), arXiv:2306.11133; https://arxiv.org/abs/2306.11133 .
3. S. Jahanshahi, H. Löwen, B. ten Hagen, *Brownian motion of a circle swimmer in a harmonic trap*, Phys. Rev. E 95, 022606 (2017); https://doi.org/10.1103/PhysRevE.95.022606 .
4. S. Barman, *Confinement-Induced Delay in Chiral Active Brownian Particles*, publicly available preprint (2025), source inspected for the two-time correlation discussion.
