# Full counting statistics and a fast-reset crossover for an asymmetric Brownian ratchet

## Finding

The instantaneous-return limit of a periodically asymmetric Brownian resetting ratchet has an explicit **joint cycle transform**, a unique analytic scaled cumulant-generating function (SCGF) for completed-cell transport, and a full current large-deviation principle. At resetting rates tending to infinity while the ratchet apex is displaced by a Brownian diffusion length, the **entire SCGF**, not merely its first two cumulants, converges to a one-parameter non-Poisson law.

Precisely, for every real counting field \(q\), the SCGF \(\psi(q)\) is the unique root \(z\) of \(\Phi(q,z)=1\), with the explicit expression for \(\Phi\) in the proof. The completed-cell current \(C_t/t\) satisfies a full large-deviation principle with speed \(t\), and good strictly convex rate function
\[
I(j)=\sup_{q\in\mathbb R}\{qj-\psi(q)\}.
\]

For every fixed \(u>0\), choosing the ratchet apex \(a_r=u\sqrt{D/r}\) gives the uniform-on-compact-counting-fields limit
\[
\lim_{r\to\infty}\frac{\psi_r(q)}r=\zeta_u(q),\qquad
\boxed{\ \zeta_u(q)=\tfrac12e^{-u\sqrt{1+\zeta_u(q)}}(e^q-1)\ },
\]
where the displayed equation has exactly one real solution \(\zeta_u(q)>-1\). It extends continuously to \(u=0\), where \(\zeta_0(q)=(e^q-1)/2\). The limit is non-Poisson for every \(u>0\). In particular, putting \(b_u=e^{-u}/2\), its first three cumulant rates are
\[
\zeta_u'(0)=b_u,\quad
\zeta_u''(0)=b_u-u b_u^2,\quad
\zeta_u^{(3)}(0)=b_u-3ub_u^2+\frac{9u^2+3u}{4}b_u^3.
\]
These formulas give an evaluated third-current-cumulant prediction in addition to the all-order implicit counting law.

## Assumptions and scope

Fix \(r,D,L>0\) and \(0<a<L\). Between independent rate-\(r\) reset events a particle performs unbiased one-dimensional Brownian motion with generator \(D\partial_{xx}\). At a reset, a position in \([nL-(L-a),nL+a)\) is returned instantaneously to \(nL\). The integer \(K\) is that cycle's completed-cell displacement, and a fresh cycle starts from the returned lattice point.

Equivalently, take iid \(T_i\sim\operatorname{Exp}(r)\); conditionally on \(T_i=t\), take independent \(B_i\sim\mathcal N(0,2Dt)\), and put
\[
K_i=\left\lfloor\frac{B_i+L-a}{L}\right\rfloor,\quad S_n=\sum_{i=1}^nT_i,\quad C_t=\sum_{n\ge1:S_n\le t}K_n.
\]
Thus \(C_t\) counts signed **completed cycles** (not the number of crossings within an unfinished Brownian excursion). All exponential moments of \(C_t\) exist for finite \(t\). The exact formulas below apply for all \(q\in\mathbb R\). The fast-reset statement keeps \(D,L,u\) fixed, varies \(r\), and sets \(a=a_r\). For \(u=0\) it denotes the continuous endpoint limit of this family.

## Proof

**1. Exact weighted-cycle law.** For real \(z>Dq^2/L^2-r\), put
\[
k=\sqrt{\frac{r+z}{D}},\quad A=e^{-ka},\quad B=e^{-k(L-a)},\quad R=e^{-kL}.
\]
The Brownian resolvent at an independent rate-\(r\) time is
\[
\mathbb E[e^{-zT};\,B_T\in dx]
=\frac{r}{2(r+z)}k e^{-k|x|}\,dx.
\]
Integrating over the partition into return intervals gives the weighted probabilities, with \(c=r/[2(r+z)]\):
\[
\mathbb E[e^{-zT};K=0]=c(2-A-B),
\]
\[
\mathbb E[e^{-zT};K=n]=c(1-R)AR^{n-1}\ (n\ge1),
\]
\[
\mathbb E[e^{-zT};K=-n]=c(1-R)BR^{n-1}\ (n\ge1).
\]
Consequently, the **evaluated** joint generating function is
\[
\boxed{\Phi(q,z)=\mathbb E[e^{qK-zT}]
=\frac{r}{2(r+z)}\left[2-A-B+(1-R)\left(\frac{Ae^q}{1-Re^q}+\frac{Be^{-q}}{1-Re^{-q}}\right)\right].}
\]
The stated domain is exactly the domain of absolute convergence of both geometric tails. In particular \(\Phi(0,0)=1\).

**2. Existence and long-time counting law.** For each fixed \(q\in\mathbb R\), \(\Phi(q,z)\) is continuous and strictly decreasing in \(z\) throughout the stated domain: its derivative is \(-\mathbb E[Te^{qK-zT}]<0\). As \(z\) decreases to \(Dq^2/L^2-r\), one weighted geometric tail diverges (at \(q=0\), the exponential-time mass diverges), while \(\Phi(q,z)\to0\) as \(z\to\infty\). Hence a unique \(\psi(q)\) satisfies \(\Phi(q,\psi(q))=1\); the implicit-function theorem makes it analytic.

The moment generating function \(F_q(t)=\mathbb E e^{qC_t}\) satisfies the renewal equation
\[
F_q(t)=e^{-rt}+\int_0^t r e^{-rs}\,\mathbb E[e^{qK}\mid T=s]F_q(t-s)\,ds.
\]
Multiplying by \(e^{-\psi(q)t}\) turns the convolution kernel into a nonlattice probability density with finite positive mean, because \(r+\psi(q)>Dq^2/L^2\). The remainder \(e^{-(r+\psi(q))t}\) is directly Riemann integrable. The continuous key renewal theorem therefore yields
\[
0<\lim_{t\to\infty}e^{-\psi(q)t}F_q(t)<\infty,
\]
proving the claimed SCGF. Differentiation of the tilted-cycle normalization gives \(\psi'(q)=\mathbb E_q[K]/\mathbb E_q[T]\) and
\[
\psi''(q)=\frac{\mathbb E_q[(K-\psi'(q)T)^2]}{\mathbb E_q[T]}>0,
\]
where \(d\mathbb P_q=e^{qK-\psi(q)T}d\mathbb P\) on single cycles. Nondegeneracy gives strict positivity. Moreover \(\psi(q)>Dq^2/L^2-r\), so convexity implies \(\psi'(q)\to\pm\infty\) as \(q\to\pm\infty\). Exponential moment bounds provide exponential tightness and the differentiable Gärtner--Ellis theorem establishes the full stated large-deviation principle. Strict convexity of \(I\) follows from strict convexity and full slope range of \(\psi\).

**3. Universal high-rate window.** Fix \(u>0\) and \(a=u\sqrt{D/r}\). Substitute \(z=r\zeta\) into the exact transform. For every \(\zeta>-1\), one has \(A=e^{-u\sqrt{1+\zeta}}\) exactly, while \(B\) and \(R\) tend to zero exponentially in \(\sqrt r\). Therefore
\[
\Phi_r(q,r\zeta)\longrightarrow
\frac{1+\frac12e^{-u\sqrt{1+\zeta}}(e^q-1)}{1+\zeta}.
\]
This limit is the positive Laplace transform of a Gaussian-sign-marked exponential cycle and is strictly decreasing in \(\zeta\). It has a unique crossing of one; bracketing and uniform convergence on compact sets give \(\psi_r(q)/r\to\zeta_u(q)\) uniformly on compact \(q\)-sets. Local smooth convergence of the implicit equations supplies convergence of all fixed derivatives at \(q=0\). Three differentiations yield the displayed cumulants.

For \(u=0\), the mark is one exactly when the Brownian excursion ends to the positive side, independently of its length. Positive marks then form a Poisson thinning at rate \(r/2\), explaining \(\zeta_0(q)=(e^q-1)/2\). For \(u>0\), the success mark is correlated with the duration; the limiting variance-to-mean ratio is \(1-ue^{-u}/2<1\). This last second-order consequence is also implied by the previously known exact dispersion law and is **not** claimed as an independent novelty.

## Verification

The accompanying `verification/ratchet_counting.py` evaluates the cycle transform by two mathematically independent computations: integration of the Gaussian conditional law over exponential waiting times, and the closed geometric-resolvent formula. It then checks implicit derivatives against the exact renewal-reward mean/variance, confirms the fast-reset SCGF scaling at several counting fields and parameter values, and checks the evaluated third edge cumulant by finite differences. All tests passed on extraction from the delivered package. The numerical tests are finite checks and do not replace the analytic proof.

## Relationship to prior work

Roberts, Sezik and Lardet (2024), arXiv:2405.10698, establish the physical sawtooth resetting protocol, stationary currents and the **known mean current** in its instantaneous limit. Ghosh et al. (2023), arXiv:2307.06202, study related autonomous ratcheting and empirical diffusivity for a different reset protocol. The accessible earlier exact asymmetric-ratchet dispersion result (claim ID `e9c08adb-a980-44ea-8126-d111e288451f`) already covers the complete first and second cumulant formulas and their straightforward asymptotic consequences; the present novelty claim expressly excludes those results. The new mathematical contribution is the **entire evaluated joint tilted-cycle transform, its full current SCGF and large deviations, and the non-Poisson fast-reset counting-field crossover including third and higher cumulants**.

General renewal-based large-deviation methods, including Meylahn, Sabhapandit and Touchette (2015), are established prior methodology. Pamulaparthy and Harris (2026) analyze large deviations for a different active-walk ratchet with memory-dependent direction reversals. Neither source was used to claim the renewal principle itself as new; the evaluated asymmetric Brownian-cell counting law is the object of the present result.

## Limitations

This is the **instantaneous-return** mathematical limit, not a theorem for all finite-height piecewise-linear ratchets. The observable counts only signed displacement of **completed** reset cycles; the full unwrapped position during a partially completed Brownian excursion is not included in the large-deviation assertion. The limit concerns the fast-reset parameter window \(a\asymp\sqrt{D/r}\), not a fixed interior apex. The cumulant calculations alone do not establish global statistical optimality of any finite-rate ratchet. A general published renewal theorem may provide an alternative proof of the SCGF existence step, and publication priority for the evaluated formula has not been independently certified.

## References

1. C. Roberts, E. Sezik and E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698 (first public version, 2024-05-17). https://arxiv.org/abs/2405.10698
2. P. K. Ghosh, S. Nayak, J. Liu, Y. Li and F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting*, arXiv:2307.06202 (2023). https://arxiv.org/abs/2307.06202
3. J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, arXiv:1510.02431 (2015). https://arxiv.org/abs/1510.02431
4. V. D. Pamulaparthy and R. J. Harris, *Memory-induced active particle ratchets: Mean currents and large deviations*, arXiv:2602.23327 (2026); different non-potential model. https://arxiv.org/abs/2602.23327
