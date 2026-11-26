# First-order dependence between extremal pre-reset energy and the selected cycle age

## Setting and finding

Consider a one-dimensional overdamped Ornstein–Uhlenbeck process \(dX_t=-\mu X_t\,dt+\sqrt{2D}\,dB_t\), with \(\mu,D>0\), started at zero and reset to zero at the times of an independent Poisson process of rate \(r>0\). For complete cycle \(i\), let \(T_i\) be its duration and \(E_i=\mu(X_i^-)^2/(2D)\) its dimensionless potential energy immediately before resetting. Let \(M_n\) and \(J_n\) be the maximum and its almost surely unique index over the first \(n\) cycles. Write
\[
\beta=\frac{r}{2\mu},\qquad \kappa=\beta+\tfrac12,\qquad c_1=\kappa(\beta+1),\qquad
g_\beta(v)=\frac{v^{\beta-1}e^{-v}}{\Gamma(\beta)},\qquad
g(x)=e^{-x}e^{-e^{-x}}.
\]
For \(n\ge2\) define the exact energy quantile \(b_n>0\) by \(n\Pr(E_1>b_n)=1\). Denote by \(p_n\) the joint density of \((M_n-b_n,\,b_n e^{-2\mu T_{J_n}})\). There is the compact-uniform local expansion, for \(x\in\mathbb R\), \(v>0\),
\[
\boxed{\displaystyle
p_n(x,v)=g(x)g_\beta(v)\left[1+\frac{c_1-x/2+v/2-v(x+v)+\kappa x e^{-x}}{b_n}+O(b_n^{-2})\right].}
\]
In particular the Gumbel and Gamma limits are independent, but the first correction includes a genuine mixed term \(-xv/b_n\). For example, at fixed \(x_1\ne x_2\) and \(v_1\ne v_2>0\), the ratio
\[
\frac{p_n(x_1,v_1)p_n(x_2,v_2)}{p_n(x_1,v_2)p_n(x_2,v_1)}
=1-\frac{(x_1-x_2)(v_1-v_2)}{b_n}+O(b_n^{-2})
\]
isolates the dependence from the marginal corrections. Since \(b_n\sim\log n\), its leading size is inverse logarithmic. The limiting age itself satisfies \(2\mu T_{J_n}-\log\log n\Rightarrow-\log V\), where \(V\) has density \(g_\beta\).

Only independent complete cycles and endpoint energy are considered. This is not a continuous-path maximum or a model of the work required by a finite-time reset protocol.

## Proof

**One-cycle joint density.** The OU stochastic integral given \(T_i=t\) has variance \((D/\mu)(1-e^{-2\mu t})\); normalization gives standard normals \(Z_i\) independent of the entire duration sequence. The independent cycle pairs can therefore be represented by
\[
U_i=e^{-2\mu T_i},\quad \Pr(U_i\le u)=u^\beta\ (0<u<1),\quad E_i=(1-U_i)Z_i^2/2.
\]
Consequently the joint density at energy \(w>0\) and \(0<u<1\) is
\[
f(w,u)=\frac{\beta u^{\beta-1}}{\sqrt{\pi w(1-u)}}e^{-w/(1-u)}.
\]
The energy is continuous with strictly positive density on \((0,\infty)\), so the maximum is unique and the defining tail quantile exists uniquely.

**Tail correction and exact quantile.** Write \(S(w)=\Pr(E_1>w)\) and \(C_\beta=\Gamma(\beta+1)/\sqrt\pi\). The conditional Gaussian tail gives
\[
S(w)=\beta\int_0^1u^{\beta-1}\operatorname{erfc}\sqrt{w/(1-u)}\,du.
\]
Use \(z=wu\) and the expansion \(\operatorname{erfc}\sqrt y=e^{-y}(\pi y)^{-1/2}[1-1/(2y)+O(y^{-2})]\) for \(y\ge w\to\infty\), obtained by two integrations by parts in the incomplete gamma integral. After division by \(C_\beta e^{-w}w^{-\kappa}\), the resulting integral is against \(g_\beta(z)\,dz\) on \((0,w)\), with multiplier
\[
\sqrt{1-z/w}\; e^{-z^2/(w-z)}\left[1-\frac{1-z/w}{2w}+O(w^{-2})\right].
\]
On \(0<z\le w/2\) this multiplier equals \(1-(z/2+z^2+1/2)/w\) with absolute error bounded by \(w^{-2}\) times a fixed polynomial in \(z\). For the exponential use \(|e^{-t}-1+t|\le t^2/2\) for \(t\ge0\), and \(|z^2/(w-z)-z^2/w|\le 2z^3/w^2\); for the square root use its Taylor bound on \([0,1/2]\). On \(w/2<z<w\) the multiplier is uniformly bounded, and the omitted gamma tails, even with polynomial weights, are exponentially small. Since the first two moments of \(g_\beta\) are \(\beta\) and \(\beta(\beta+1)\),
\[
S(w)=C_\beta e^{-w}w^{-\kappa}\left(1-\frac{c_1}{w}+O(w^{-2})\right).
\]
This gives \(b_n=\log n-\kappa\log\log n+\log C_\beta+o(1)\) and, at \(b=b_n\),
\[
n C_\beta e^{-b}b^{-\kappa}=1+c_1/b+O(b^{-2}),\qquad
n S(b+x)=e^{-x}\bigl(1-\kappa x/b+O(b^{-2})\bigr)
\]
uniformly for bounded \(x\).

**Density of the selected cycle.** Independence between cycles gives the exact density
\[
p_n(x,v)=\frac{n}{b} f(b+x,v/b)[1-S(b+x)]^{n-1},
\qquad x>-b,\quad 0<v<b.
\]
In the first factor, the exponential after taking out \(e^{-b}\) is \(\exp[-(x+v)/(1-v/b)]\). The two square-root factors after scaling are \((1+x/b)^{-1/2}\) and \((1-v/b)^{-1/2}\). Their Taylor expansions and the exact-quantile normalization yield
\[
\frac{n}{b}f(b+x,v/b)
=e^{-x}g_\beta(v)\left(1+\frac{c_1-x/2+v/2-v(x+v)}{b}+O(b^{-2})\right).
\]
For the second factor, \((n-1)\log(1-S(b+x))=-n S(b+x)+O(n^{-1})\) locally uniformly in \(x\). Using the tail ratio above and \(n^{-1}=o(b^{-2})\) gives \([1-S(b+x)]^{n-1}=e^{-e^{-x}}[1+\kappa x e^{-x}/b+O(b^{-2})]\). This proves the joint expansion. In the four-point ratio all additive functions of \(x\) alone or \(v\) alone cancel. The leading density integrates to one, so pointwise convergence of the joint densities also yields convergence in total variation. Taking the logarithm of the positive mark and using \(\log b_n=\log\log n+o(1)\) proves the stated age limit.

## Relationship to prior work and verification

Trajanovski et al. ([arXiv:2301.12304](https://arxiv.org/abs/2301.12304), §III.B) give the stationary OU marginal as the propagator mixed over exponential ages; this gives the same one-cycle position marginal here. The leading energy tail is a special case of the random-contraction law of Hashorva, Pakes and Tang ([arXiv:1008.0126](https://arxiv.org/abs/1008.0126), Theorem 3.1(a)) with base variable \(Z^2/2\) and contraction \(1-U\). The critical quadratic exponential-moment threshold belongs to that one-cycle marginal analysis and is not asserted as a contribution; see also the broader partial-reset result [Gaussian-tail rigidity and the critical quadratic tilt of a partially reset harmonic diffusion](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-gaussian-tail-rigidity-and-the-critical-quadratic-tilt-of-a-part--8652cc621e2b). In the [simultaneously reset Brownian gas](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-gaussian-edge-leakage-and-a-gumbel-boundary-layer-in-a-simultane--4cd7cf34fdd1), an extreme also selects a doubly logarithmic age, but there is one shared age for all particles in a stationary snapshot, not a winning age among independent completed cycles. The contribution here is the local joint-density correction and its mixed term for this independent-cycle model. The accompanying one-cycle numerical checks do not verify that correction; the expansion and its remainder follow from the analytic calculation above. No global uniform correction in the two coordinates or historical priority certification is claimed.
