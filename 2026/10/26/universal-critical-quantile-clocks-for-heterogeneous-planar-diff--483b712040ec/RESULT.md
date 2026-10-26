# Universal critical quantile clocks for heterogeneous planar diffusion under resetting

## Finding

Let \(a>0\), \(\beta\in[1/2,1]\), and \(q\in(0,1)\). Define the free radial probability
\[
F_\beta(t)=\frac{\gamma(\beta,a/t)}{\Gamma(\beta)},\qquad t>0,
\]
and, for an independent Poisson restart clock of rate \(r>0\), the fraction inside the observation radius at time \(t\),
\[
H_{\beta,r}(t)=e^{-rt}F_\beta(t)+r\int_0^t e^{-ru}F_\beta(u)\,du.
\]
Here \(\gamma\) is the lower incomplete gamma function. Let \(T_{\beta,q}(r)\) be the first finite time when \(H_{\beta,r}(t)=q\), or \(\infty\) if no such time exists. Set
\[
\Phi_\beta(z)=\frac{z^\beta K_\beta(z)}{2^{\beta-1}\Gamma(\beta)},
\]
and let \(z_{\beta,q}>0\) be the unique root \(\Phi_\beta(z_{\beta,q})=1-q\). Then
\[
r_c=\frac{z_{\beta,q}^2}{4a}
\]
is the exact threshold: \(T_{\beta,q}(r)<\infty\) and the crossing is unique for \(0<r<r_c\); no finite crossing occurs for \(r\ge r_c\). At fixed \(a,q\), \(r_c\) is strictly increasing in \(\beta\).

There is a sharp second-order transition clock. Define
\[
\epsilon=1-r/r_c,\quad L=\log(1/\epsilon),\quad
B=\frac{(ar_c)^\beta}{\Gamma(\beta)},\quad
C=\frac{z_{\beta,q}^{\beta+1}K_{\beta-1}(z_{\beta,q})}{2^\beta\Gamma(\beta)},\quad
\mathcal H=\frac{B}{C}=\frac{z_{\beta,q}^{\beta-1}}{2^\beta K_{\beta-1}(z_{\beta,q})}.
\]
For every fixed real \(\xi\), with \(t_\epsilon(\xi)=\{L-(\beta+1)\log L+\xi\}/r_c\),
\[
\lim_{\epsilon\downarrow0}\frac{H_{\beta,r_c(1-\epsilon)}(t_\epsilon(\xi))-q}{\epsilon}
=B e^{-\xi}-C.
\]
Consequently, the unique crossing obeys the **sharp universal critical clock**
\[
\boxed{\displaystyle
r_cT_{\beta,q}(r)=L-(\beta+1)\log L+\log\mathcal H+o(1),\qquad r\uparrow r_c.}
\]
For the Itô, Stratonovich, and Hänggi--Klimontovich prescriptions the coefficients of \(-\log L\) are respectively \(2\), \(7/4\), and \(3/2\). The leading logarithmic divergence alone does not resolve these three response classes.

## Assumptions and scope

The two-dimensional radially symmetric Fokker--Planck problem has heterogeneous diffusivity \(D(\rho)=D_0/\rho^2\), with \(D_0>0\), and stochastic-calculus interpolation \(\alpha\in[0,1]\). Its radial density (normalized against \(\rho\,d\rho\)) is the origin-started, zero-flux fundamental solution
\[
P_\alpha(\rho,t)=\frac{4\rho^{2-2\alpha}}{\Gamma(1-\alpha/2)(16D_0t)^{1-\alpha/2}}
\exp\!\left(-\frac{\rho^4}{16D_0t}\right).
\]
The correspondence is \(\beta=1-\alpha/2\), \(a=R^4/(16D_0)\), where \(R>0\) is the observation radius. The three standard prescriptions have \(\alpha=0,1/2,1\), respectively. Resets are instantaneous, complete returns to the origin at independent exponential times. No absorbing boundary is introduced at \(R\): the measured quantity is the fraction occupying the disk, *not* an ever-escaped fraction or a first-passage survival probability. The theorem also applies directly to the stated gamma-radial renewal family without an underlying diffusion interpretation.

## Proof

**Radial normalization.** Substitute \(w=\rho^4/(16D_0t)\) into \(\int_0^\infty P_\alpha(\rho,t)\rho\,d\rho\). The result is one. Direct differentiation verifies
\[
\partial_tP_\alpha=\frac{D_0}{\rho}\partial_\rho\left\{\rho^{1-2\alpha}\partial_\rho[\rho^{-2(1-\alpha)}P_\alpha]\right\}.
\]
The density concentrates at the origin as \(t\downarrow0\), and its radial flux vanishes at the origin. Integration to \(R\) gives \(F_\beta(t)\) exactly. Moreover
\[
-F'_\beta(t)=\frac{a^\beta}{\Gamma(\beta)}t^{-\beta-1}e^{-a/t}>0.
\]

**Stationary threshold and uniqueness.** Differentiating the renewal formula cancels its two reset terms:
\[
H'_{\beta,r}(t)=e^{-rt}F'_\beta(t)<0.
\]
Its stationary limit \(h_\beta(r)=r\int_0^\infty e^{-rt}F_\beta(t)dt\) is strictly increasing continuously from zero to one as \(r\) runs from zero to infinity: the exponential age becomes stochastically smaller as its rate increases. Let \(G\sim\operatorname{Gamma}(\beta,1)\). The identity \(F_\beta(t)=\Pr(a/G\ge t)\) and Tonelli's theorem show
\[
1-h_\beta(r)=\mathbb E[e^{-ra/G}]
=\frac{2(ar)^{\beta/2}}{\Gamma(\beta)}K_\beta(2\sqrt{ar}).
\]
Thus the positive root \(r_c\) is unique, and strict temporal monotonicity establishes all finite-crossing assertions. If \(\beta_2>\beta_1\), couple \(G_{\beta_2}=G_{\beta_1}+G_{\beta_2-\beta_1}\) with independent positive summands. The free and stationary inside fractions decrease strictly as \(\beta\) increases, proving strict increase of \(r_c\).

**Exact relaxation excess.** Integrating by parts, using \(F_\beta(\infty)=0\), gives
\[
H_{\beta,r}(t)-h_\beta(r)
=-\int_t^\infty e^{-ru}F'_\beta(u)du
=\frac{a^\beta}{\Gamma(\beta)}\int_t^\infty e^{-ru-a/u}u^{-\beta-1}du.
\]
For \(r\) in a fixed compact subinterval of \((0,\infty)\), substituting \(u=t+v\) and applying dominated convergence with a first-order Taylor estimate yields uniformly
\[
H_{\beta,r}(t)-h_\beta(r)
=\frac{a^\beta}{r\Gamma(\beta)}e^{-rt}t^{-\beta-1}\bigl(1+O(t^{-1})\bigr).
\]
The algebraic factor \(t^{-\beta-1}\), caused by cancellation between the reset-age terms, is essential for the second-order clock.

**Critical window.** The identity \((z^\beta K_\beta(z))'=-z^\beta K_{\beta-1}(z)\) gives
\[
r_ch'_\beta(r_c)=C>0.
\]
Therefore \(h_\beta(r_c(1-\epsilon))=q-C\epsilon+O(\epsilon^2)\). With \(t=t_\epsilon(\xi)\), \(rt=L-(\beta+1)\log L+\xi+o(1)\) and \(t^{-(\beta+1)}=r_c^{\beta+1}L^{-(\beta+1)}(1+o(1))\). Substitution in the exact excess formula gives \(\epsilon B e^{-\xi}(1+o(1))\), uniformly for \(\xi\) in compact sets. This proves the stated window limit. Its sign changes exactly at \(\xi=\log(B/C)\); strict monotonicity of \(H_{\beta,r}\) brackets its unique crossing between any two fixed offsets on opposite sides, proving the \(o(1)\) time law.

## Verification

Run `python3 verify.py` using Python, SciPy, and NumPy. The checker independently integrates the radial density, compares the Bessel stationary law with quadrature of the reset-age mixture, verifies the integration-by-parts identity, calculates the critical rates, checks strict ordering across the three conventional interpretations, and numerically tests the nested-log transition law at several critical distances. Numerical truncation and finite parameter testing do not replace the proof above.

At \(D_0=R=1\), the median critical rates are approximately \(6.321718476330\), \(4.010245505803\), and \(1.921812055673\) for the Itô, Stratonovich, and Hänggi--Klimontovich cases, respectively.

## Relationship to prior work

Sandev, Fumeron, Henkel, and Lenzi (2026) give the three free radial distributions, the Poisson renewal equation, the stationary mass, and the median-confinement threshold with a qualitative logarithmic divergence (especially their Sec. 2.4, Eqs. (47)--(51)); their Sec. 3.4 treats memory-dependent threshold curves. These are prior inputs, not claimed as discoveries here. The finding is the **universal sharp finite-time window with explicit intercept and convention-dependent \(-\log\log\) coefficient**, plus the continuous-interpretation gamma classification and exact parameter monotonicity. The general Poisson-reset renewal mechanism originates in the established resetting literature, including Evans and Majumdar (2011). General Laplace endpoint asymptotics and Bessel identities are standard proof tools, not new inventions.

## Limitations

The claim is about disk occupancy, not first passage, and holds for a fixed observation radius, fixed quantile, and fixed stochastic interpretation as the resetting rate approaches its critical value from below. It assumes exponential resetting and an origin-started zero-flux radial law. It does not cover finite-duration returns, a target that absorbs walkers, nonexponential reset clocks, subdiffusive operational-time memory, or a joint limit in which \(q\) or \(\beta\) varies with the critical distance. The status of global literature priority requires independent review; the numerical checks do not establish novelty or infinite-parameter validity.

## References

1. T. Sandev, S. Fumeron, M. Henkel, and E. K. Lenzi, *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting*, arXiv:2609.24427v1, first publicly submitted 2026-09-21, https://arxiv.org/html/2609.24427 .
2. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Physical Review Letters **106** (2011), 160601, arXiv:1102.2704, https://arxiv.org/abs/1102.2704 .
3. A. G. Cherstvy, A. V. Chechkin, and R. Metzler, *Particle invasion, survival, and non-ergodicity in 2D diffusion processes with space-dependent diffusivity*, Soft Matter **10** (2014), 1591--1601, doi:10.1039/C3SM52846D .
