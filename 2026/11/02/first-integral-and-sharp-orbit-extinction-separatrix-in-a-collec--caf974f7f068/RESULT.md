# First integral and sharp orbit–extinction separatrix in a collective-risk feedback game

## Finding

The critical linear-feedback collective-risk game has a global first integral, a nonlinearly neutral center with an entire open annulus of periodic orbits, and an exact energy threshold separating those periodic trajectories from trajectories converging to universal full defection and maximal risk. At the threshold, the interior boundary of the periodic region is a heteroclinic orbit joining two distinct high-risk boundary equilibria. No isolated attracting limit cycle exists at the critical feedback parameter.

More precisely, under the assumptions below, define \(H\), its unique interior minimum \(H_{\min}\), and a finite separatrix value \(H_{\mathrm{sep}}\) as in the proof. For every interior initial state \(z_0\), with \(E=H(z_0)\):

* \(H_{\min}<E<H_{\mathrm{sep}}\): the complete orbit is periodic and each level set is one simple closed curve; adjacent periodic trajectories establish orbital neutrality.
* \(E=H_{\mathrm{sep}}\): the nonstationary trajectory is a heteroclinic orbit, from \((x_2,1)\) in backward time to \((x_1,1)\) in forward time.
* \(E>H_{\mathrm{sep}}\): the trajectory converges to \((0,1)\) in forward time.
* \(E=H_{\min}\): the unique interior equilibrium \((p,r_*)\).

Here \(0<x_1<p<x_2<1\) are the two solutions of \(h(x)=c\). The theorem describes *all* interior initial states, and \(H_{\min}<H_{\mathrm{sep}}\).

## Assumptions and scope

Let \(N,M\) be integers with \(N\ge3\) and \(2\le M<N\), and let \(b,c,\varepsilon>0\). Set \(\alpha=M-1\), \(\beta=N-M\), \(k=N-1=\alpha+\beta\), and

\[
h(x)=b\binom{N-1}{M-1}x^{\alpha}(1-x)^{\beta},\qquad
p=\frac{\alpha}{k},\qquad h_0=h(p).
\]

Require \(0<c<h_0\). Consider exactly the deterministic linear-feedback model of the originating article, with the critical feedback enhancement \(u=\alpha/\beta\):

\[
\varepsilon\dot{x}=x(1-x)[r h(x)-c],\qquad
\dot{r}=r(1-r)[u(1-x)-x]
=\frac{r(1-r)}{\beta}(\alpha-kx).
\]

The state is \((x,r)\in(0,1)^2\), where \(x\) is cooperator frequency and \(r\) is collective risk. Define \(r_*=c/h_0\in(0,1)\). No assertion is made for different risk feedback, parameters away from \(u=\alpha/\beta\), finite-population stochastic models, or \(c\ge h_0\).

## Proof

**Exact integral.** Put \(a=\beta c/\varepsilon>0\), \(I(r)=((1-r)/r)^a\), and

\[
H(x,r)=\frac{I(r)}{h(x)}+\frac{\beta}{\varepsilon}\int_{r_*}^{r}\frac{I(s)}{1-s}\,ds.
\]

The integral is finite for every interior \(r\) and fixes an immaterial additive constant. The polynomial identity
\[
\frac{h'(x)}{h(x)}=\frac{\alpha-kx}{x(1-x)}
\]
and \(I'(r)=-aI(r)/[r(1-r)]\) yield
\[
H_x=-\frac{Ih'}{h^2},\quad
H_r=\frac{\beta I}{\varepsilon r(1-r)}\left(r-\frac{c}{h(x)}\right),\quad
\frac{dH}{dt}=0.
\]

**Energy geometry.** The function \(h\) strictly increases on \((0,p)\), strictly decreases on \((p,1)\), and vanishes at both endpoints. Consequently, for each fixed \(r\), \(H(x,r)\) has its strict global minimum at \(x=p\), with \(H\to\infty\) as \(x\to0,1\). Let \(G(r)=H(p,r)\). Direct differentiation gives
\[
G'(r)=\frac{\beta I(r)}{\varepsilon r(1-r)}(r-r_*).
\]

Thus \(G\) decreases strictly from \(+\infty\) on \((0,r_*)\), increases strictly on \((r_*,1)\), and uniquely minimizes at \(r_*\). Moreover, since \(a>0\),
\[
H_{\mathrm{sep}}=\lim_{r\uparrow1}G(r)=\frac{\beta}{\varepsilon}\int_{r_*}^{1}\frac{(1-s)^{a-1}}{s^a}\,ds
\]
is finite and strictly larger than \(H_{\min}=G(r_*)=I(r_*)/h_0\). The Hessian at \((p,r_*)\) is positive definite: its off-diagonal entries vanish, while
\[
H_{xx}=-\frac{I(r_*)h''(p)}{h_0^2}>0,\qquad
H_{rr}=\frac{\beta I(r_*)}{\varepsilon r_*(1-r_*)}>0.
\]

For \(H_{\min}<E<H_{\mathrm{sep}}\), the equation \(G(r)=E\) has exactly two solutions \(0<r_-<r_*<r_+<1\). Every intermediate \(r\) has exactly two solutions \(x_-(r)<p<x_+(r)\) of \(H(x,r)=E\); they join smoothly at \(r_\pm\) into one regular compact simple closed curve. The interior vector field is nonzero away from \((p,r_*)\); every such curve is therefore a periodic orbit. At the minimum lies the nonlinear center.

For \(E\ge H_{\mathrm{sep}}\), only the lower turning point \(r_-<r_*\) remains in the open square, and the two branches extend toward \(r=1\). Write
\[
\frac{I(r)}{h(x)}=E-H_{\mathrm{sep}}+\frac{\beta}{\varepsilon}\int_r^1\frac{I(s)}{1-s}\,ds.
\]

When \(E>H_{\mathrm{sep}}\), the right side tends to a strictly positive constant and \(I(r)\to0\), so \(h(x)\to0\): the left branch tends to \(x=0\), the right branch to \(x=1\). Since \(\dot r\) is positive to the left of \(p\) and negative to its right, the forward flow passes the lower turning point toward the left branch and hence converges to \((0,1)\). There can be no return because the level set has no upper turning point.

For \(E=H_{\mathrm{sep}}\), l'Hôpital's rule or the elementary endpoint asymptotic of a positive power gives
\[
\lim_{r\uparrow1}\frac{\int_r^1 I(s)/(1-s)\,ds}{I(r)}=\frac1a.
\]

Therefore \(h(x_\pm(r))\to c\), forcing the distinct endpoints \(x_1<p<x_2\) satisfying \(h(x_i)=c\). The positive risk direction on the left branch and negative risk direction on the right prove that the open interior separatrix connects \((x_2,1)\) in backward time to \((x_1,1)\) in forward time. Boundary points are only asymptotically reached, because the smooth vector field preserves the open square for finite time. All cases are exhaustive. Conservation prevents any nonstationary interior orbit from being attracting relative to nearby distinct energy levels.

## Verification

Run `python check_critical_collective_risk.py` with Python 3.10+, SymPy, NumPy, and SciPy. The included script establishes 36 exact symbolic cancellation identities across all \(N=3,\ldots,10\), \(2\le M<N\), and tests an ordinary numerical trajectory for 200 time units with a conserved-energy drift below \(6\times10^{-9}\). Finite checks independently corroborate but do not establish the all-parameter analytic theorem.

For the originating article's illustrative parameters \((N,M,b,c,\varepsilon,u)=(6,3,1,1/10,1/10,2/3)\), the critical equilibrium is \((p,r_*)=(2/5,125/432)\). Here \(a=3\), and
\[
H(x,r)=\frac{(1-r)^3}{r^3h(x)}+30\bigl(F(r)-F(125/432)\bigr),\quad
F(r)=-\frac1{2r^2}+\frac2r+\log r.
\]

The test gives \(H_{\min}\approx42.86584148\), \(H_{\mathrm{sep}}\approx54.00239553\), and \(H(2/5,1/2)\approx51.10149863\), strictly inside the periodic annulus.

## Relationship to prior work

Liu, Chen and Szolnoki formulate exactly these coupled equations (their System I), give the critical value \(u=(M-1)/(N-M)\), and discuss a numerically inferred supercritical Hopf bifurcation and a stable limit cycle. Their article and appendix do not derive the invariant above or the full energy-level trichotomy. The exact first integral implies that, at this critical value, every sufficiently small nonstationary interior trajectory is periodic and none is an isolated attracting limit cycle; in particular, ordinary nondegenerate Hopf criticality cannot be concluded from a numerically tiny first Lyapunov coefficient.

Weitz et al. (2016) derive a conserved quantity and neutral cycles in a *different*, factorable two-strategy matrix-payoff feedback game. That conservation result does not imply an invariant or a separatrix threshold for the present nonlinear binomial collective-risk payoff, which includes both the additive cost and risk-dependent multiplier.

## Limitations

The global classification is restricted to the critical feedback parameter of the linear-feedback model, a strictly interior equilibrium, and deterministic infinite-population trajectories. In particular, it does not settle off-critical nonlinear attractors or the exponential-feedback variant. Search results cannot exclude an equivalent unindexed derivation. An independent scientific audit has not been performed.

## References

1. Liu, L., Chen, X., and Szolnoki, A., *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*. First public preprint: bioRxiv 10.1101/2022.12.19.520980 (20 December 2022); arXiv:2305.00253; eLife 12:e82954 (2023).
2. Weitz, J. S., Eksin, C., Paarporn, K., Brown, S. P., and Ratcliff, W. C., *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*. Preprint doi:10.1101/043299 (2016); PNAS 113 (2016), E7518–E7525.
