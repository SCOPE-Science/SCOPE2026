# Exact modal pinning and saturation in a harmonically confined process with Poisson resetting

## Finding
Consider overdamped Ornstein–Uhlenbeck diffusion in a confining harmonic potential, reset at independent Poisson times to a fixed point strictly to the right of the trap minimum. Its stationary density is **strictly unimodal**, and its mode has a universal saturation law: once the reset point lies beyond a rate-dependent intrinsic position, moving the reset point still farther does not move the mode.

More precisely, let \(a,D,x_0,r>0\) and let \(X\) evolve between resets by
\[
 dX_t=-aX_t\,dt+\sqrt{2D}\,dB_t,
\]
with instantaneous resets to \(x_0\) at the points of an independent rate-\(r\) Poisson process. Define the dimensionless reset position and rate
\[
 y_0=x_0\sqrt{a/D}>0,\qquad s=r/a>0.
\]
For every \(s>0\) and real \(y\), put
\[
 U_s(y)=\int_0^\infty t^{s-1}\exp(yt-t^2/2)\,dt,
 \qquad m_s(y)=\frac{U_s'(y)}{U_s(y)}.
\]
For \(0<s<1\), let \(\zeta(s)\) be the **unique** positive solution to
\[
 m_s(\zeta)=\zeta.
\]
For \(s\ge1\), set \(\zeta(s)=+\infty\) solely as a convention. The unique stationary mode is
\[
 \boxed{x_{\rm mode}=\sqrt{D/a}\;\min\{y_0,\zeta(s)\}.}
\]
The finite function \(\zeta:(0,1)\to(0,\infty)\) is strictly increasing, with
\[
 \lim_{s\downarrow0}\zeta(s)=0,\qquad
 \lim_{s\uparrow1}\zeta(s)=+\infty,\qquad
 \zeta(s)\sim \sqrt{\pi/2}\,s\quad(s\downarrow0).
\]
Consequently, for every fixed \(y_0>0\), there is exactly one pinning threshold \(s_c(y_0)\in(0,1)\), determined by
\[
 \boxed{m_{s_c(y_0)}(y_0)=y_0.}
\]
The mode lies strictly between the trap center and reset point for \(0<s<s_c(y_0)\), and equals the reset point for \(s\ge s_c(y_0)\). The threshold is strictly increasing in \(y_0\), tends to zero as \(y_0\downarrow0\), tends to one as \(y_0\to\infty\), and satisfies
\[
 s_c(y_0)\sim\sqrt{2/\pi}\,y_0\quad(y_0\downarrow0).
\]
At equality the stationary density has zero derivative immediately to the left of the reset point and a strictly negative derivative immediately to its right; there is never a second mode.

## Assumptions and scope
All four physical parameters \(a,D,r,x_0\) are strictly positive. The process is defined on the entire real line, with a centered stable harmonic potential, additive Brownian noise, and state-independent Poisson resets to one fixed point. It has a unique stationary probability law because the Poisson-reset renewal representation is a mixture of OU transition laws. Reflection handles negative reset positions; reset exactly at the trap minimum gives the stationary mode at that minimum and is excluded from the nontrivial threshold statement. The zero-reset limit is not itself a resetting process in the stated parameter domain.

The dimensionless stationary density \(\rho_{s,y_0}(y)\) of \(Y=X\sqrt{a/D}\) can also be written exactly. Put \(h=s/[m_s(y_0)+m_s(-y_0)]\). Then
\[
 \rho_{s,y_0}(y)=h\exp\!\left(\frac{y_0^2-y^2}{2}\right)
 \begin{cases}
 U_s(y)/U_s(y_0),&y\le y_0,\\
 U_s(-y)/U_s(-y_0),&y\ge y_0.
 \end{cases}
\]
This density is continuous at \(y_0\), integrates to one, and has derivative jump \(\rho'(y_0+)-\rho'(y_0-)=-s\). The physical density is \(\sqrt{a/D}\,\rho_{s,y_0}(x\sqrt{a/D})\).

## Proof
**1. Stationary resolvent and density.** In dimensionless time, free motion has generator \(Lf=f''-yf'\) and transition density
\[
 k_\tau(y_0,y)=\frac{\exp[-(y-y_0e^{-\tau})^2/(2(1-e^{-2\tau}))]}{\sqrt{2\pi(1-e^{-2\tau})}}.
\]
The last-reset formula supplies a positive, normalized stationary density
\[
 \rho(y)=\int_0^\infty s e^{-s\tau}k_\tau(y_0,y)\,d\tau.
\]
Away from \(y_0\) it solves \(\rho''+(y\rho)'-s\rho=0\), with \(\rho'(y_0+)-\rho'(y_0-)=-s\). Substitution \(\rho=e^{-y^2/2}u\) gives \(u''-yu'-su=0\). Differentiation under the integral and one integration by parts verify that \(U_s(y)\) solves this equation. Its behavior as \(y\to-\infty\) is \(U_s(y)\sim\Gamma(s)|y|^{-s}\), whereas the other independent solution \(U_s(-y)\) has a nonintegrable right-growing component in the left tail when multiplied by \(e^{-y^2/2}\). Thus the integrable solution on \(( -\infty,y_0)\) is proportional to \(e^{-y^2/2}U_s(y)\); reflection gives \(e^{-y^2/2}U_s(-y)\) on \((y_0,\infty)\). Continuity and the derivative jump yield the stated positive height \(h\). Integrating the stationary equation and using the vanishing boundary flux proves normalization; it also agrees with the renewal law, establishing uniqueness.

**2. A one-crossing identity.** Under the probability density proportional to \(t^{s-1}e^{yt-t^2/2}\) on \(t>0\), the number \(m_s(y)\) is the mean of \(t\). The differential equation gives
\[
 m_s'(y)=s+ym_s(y)-m_s(y)^2.
\]
For \(q_s(y)=m_s(y)-y\), this becomes
\[
 \boxed{q_s'(y)=s-1-m_s(y)q_s(y).}
\]
For \(y\le0\), \(q_s(y)>0\) since \(m_s(y)>0\). For \(0<s<1\), \(q_s(0)>0\) and Laplace's method gives
\[
 m_s(y)=y+(s-1)y^{-1}+O(y^{-3})\quad(y\to+\infty),
\]
so \(q_s\) is eventually negative. At every zero the identity gives \(q_s'=s-1<0\). All zeros are therefore positive-to-negative crossings, proving existence and uniqueness of \(\zeta(s)\). At \(s=1\),
\[
 U_1(y)=e^{y^2/2}\int_{-y}^\infty e^{-z^2/2}\,dz,
 \qquad q_1(y)=1/U_1(y)>0.
\]
Moreover,
\[
 \partial_s m_s(y)=\operatorname{Cov}_{s,y}(t,\log t)>0,
\]
because both factors are strictly increasing, under a nondegenerate distribution. Hence \(q_s(y)>0\) for \(s\ge1\), and \(\zeta(s)\) is strictly increasing for \(0<s<1\): implicit differentiation at its simple root gives \(\zeta'(s)=\partial_s m_s(\zeta)/(1-s)>0\). The pointwise limits \(m_s(y)\to0\) as \(s\downarrow0\) and \(q_s(y)\to q_1(y)>0\) as \(s\uparrow1\) yield the two endpoint limits. As \(s\downarrow0\), the numerator of \(m_s(0)\) tends to \(\int_0^\infty e^{-t^2/2}dt=\sqrt{\pi/2}\), while its denominator is asymptotic to \(1/s\); the one-crossing identity then gives \(\zeta(s)\sim s\sqrt{\pi/2}\).

**3. Global mode and sharp pinning.** For \(y<y_0\), the logarithmic density derivative is \(\rho'/\rho=q_s(y)\), so part 2 classifies every critical point to the left. For \(y>y_0>0\), it is \(\rho'/\rho=-y-m_s(-y)<0\). Thus no right-side peak exists, and the global unique mode is \(\min\{y_0,\zeta(s)\}\). At each fixed \(y_0>0\), \(m_s(y_0)\) is strictly increasing in \(s\), while \(m_s(y_0)\to0<y_0\) as \(s\downarrow0\) and \(m_1(y_0)>y_0\), yielding exactly one threshold in \((0,1)\). Its inverse relationship to the strictly increasing bijection \(\zeta:(0,1)\to(0,\infty)\) proves strict monotonicity and endpoints; inversion of the small-\(s\) asymptotic proves the small-\(y_0\) law.

## Verification
The standalone `verify.py` uses two mathematically independent numerical expressions: the cylinder-function closed form for the Green density and a direct Gaussian-age renewal integral. It compares 120 parameter/position combinations, confirms monotonicity and sign brackets at six free-mode and six threshold examples, and checks the exact \(s=1\) identity. All tests passed; maximum observed relative density discrepancy was \(1.43\times10^{-10}\). For \(a=D=1\), at \(s=1/2\) the unpinned mode is \(\zeta(1/2)\approx0.764950867389776\), whereas the reset-position threshold at \(y_0=1\) is \(s_c(1)\approx0.611761705293214\).

The proof, rather than the finite calculations, establishes the all-parameter classification. Run the reproducibility program with `python verify.py`, with NumPy and SciPy installed. No simulation data, fitting, or finite truncation is invoked to deduce uniqueness.

## Relationship to prior work
Pal (arXiv:1408.1230, publicly posted 2014-08-06) introduced the reset Ornstein–Uhlenbeck stationary density in a harmonic potential and observed the shift of its peak between the trap center and reset point. Trajanovski and collaborators (arXiv:2301.12304, Sec. III, 2023) gave an independent stationary-resolvent treatment and described the high-rate reset-point peak. The present finding does **not** claim the density, resolvent, or general resetting mechanism as new. Its narrower mathematical claim is a complete, globally rigorous mode-location formula, a rate-dependent mode location independent of a sufficiently distant reset point, and the strictly monotone exact pinning threshold below the trap relaxation rate. Olsen (arXiv:2310.04840, 2023) addresses closed stationary moments for arbitrary reset-location distributions rather than the point-reset density's precise modal classification.

## Limitations
The classification is for scalar additive-noise OU dynamics with constant drift coefficient and deterministic point resets, not distributed, state-dependent, non-Poisson, inertial, or nonharmonic reset models. The original stationary density and qualitative peak motion predate this analysis. Although inspected sources and targeted mathematical-results searches did not yield the precise theorem, absence from searches does not establish priority; unindexed or uninspected literature may contain equivalent deductions. The findings have received only a self-review and no independent validation.

## References
1. A. Pal, *Diffusion in a potential landscape with stochastic resetting*, arXiv:1408.1230 (first public version 2014-08-06); Phys. Rev. E **91**, 012113 (2015). https://arxiv.org/abs/1408.1230
2. P. Trajanovski, P. Jolakoski, K. Zelenkovski, A. Iomin, L. Kocarev and T. Sandev, *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (2023); Phys. Rev. E **107**, 054129 (2023). https://arxiv.org/abs/2301.12304
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (2023); Phys. Rev. E **108**, 044120 (2023). https://arxiv.org/abs/2310.04840
