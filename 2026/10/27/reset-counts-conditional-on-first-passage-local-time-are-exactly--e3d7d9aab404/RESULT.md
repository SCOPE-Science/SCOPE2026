# Reset counts conditional on first-passage local time are exactly Poisson

## Finding

Let a one-dimensional continuous-path diffusion be absorbed at the origin and restarted to the same interior point \(a>0\) at independent Poisson times of rate \(r>0\), until absorption. Let \(N\) be its number of resets and let \(L\) be the accumulated occupation-density local time at the reset point. Write \(q\in(0,1)\) for the one-attempt probability of absorption before a reset, and let \(G\in(0,\infty)\) be its exponentially discounted killed Green density at \(a\), both defined below. Then, for every \(n\in\mathbb N_0\) and \(\ell>0\), the exact joint density is
\[
\Pr(N=n,L\in d\ell)=\frac qG e^{-\ell/G}\frac{[(1-q)\ell/G]^n}{n!}\,d\ell.
\]
Consequently \(N\mid L=\ell\sim\operatorname{Poisson}((1-q)\ell/G)\), while \(L\mid N=n\sim\operatorname{Gamma}(n+1,\text{scale }G)\). The marginal \(L\sim\operatorname{Exp}(\text{mean }G/q)\) and \(N\sim\operatorname{Geometric}(q)\), counting failures before success. The observable count–local-time correlation is
\[
\operatorname{Corr}(N,L)=\sqrt{1-q}.
\]
These statements are exact, not long-time or weak-reset approximations.

For Brownian diffusion with generator \(D\partial_{xx}\), diffusion coefficient \(D>0\), the explicit parameters are
\[
q=e^{-a\sqrt{r/D}},\qquad G=\frac{1-e^{-2a\sqrt{r/D}}}{2\sqrt{Dr}},\qquad
\frac{1-q}{G}=\frac{2\sqrt{Dr}}{1+e^{-a\sqrt{r/D}}}.
\]
Thus observing \(L=\ell\) predicts the reset count through an exactly calibrated Poisson distribution, without observing the reset events.

## Assumptions and scope

The underlying unreset process \(Y_t\) starts at \(a>0\), has continuous paths on \((0,\infty)\), and is a nonexplosive regular one-dimensional Itô diffusion with generator \(\mathcal Lf=b(x)f'(x)+D(x)f''(x)\), locally regular coefficients and \(D(x)>0\). It is killed at \(\tau=\inf\{t\ge0:Y_t=0\}\); the killed semigroup has a jointly continuous transition density \(p_t^0(x,y)\) with respect to spatial Lebesgue measure at the interior point \(a\). A fresh exponential reset clock of rate \(r>0\), independent of the diffusion, returns the trajectory instantaneously to \(a\), independently renewing the diffusion and its clock. Absorption stops the experiment. Assume
\[
q=\mathbb E_a[e^{-r\tau};\tau<\infty]\in(0,1),\qquad
G=\int_0^\infty e^{-rt}p_t^0(a,a)dt\in(0,\infty).
\]
The convention \(e^{-r\infty}=0\) applies. The occupation-density local time is
\[
L_t^a=\lim_{\varepsilon\downarrow0}\frac1{2\varepsilon}
\int_0^{t\wedge\tau}\mathbf1_{\{|Y_s-a|<\varepsilon\}}\,ds
\]
with its jointly continuous modification, so \(\mathbb E_a\int_0^{\tau}e^{-rt}\,dL_t^a=G\). Local time accumulates across reset attempts without being erased by a reset. This *time-occupation* normalization differs from the semimartingale local-time convention by the local quadratic-variation coefficient. Reset times are not counted as local time. Results apply to regular diffusions satisfying these resolvent hypotheses, including an Ornstein–Uhlenbeck process of positive diffusivity on the absorbed half-line. They need not apply if resets change the reset point, reset accumulated local time to zero, or depend on the trajectory.

## Proof

**Step 1: One-attempt success and failure transforms.** Consider a single attempt ending at \(T=\tau\wedge E\), where \(E\sim\operatorname{Exp}(r)\) independently. Write \(J=\mathbf1_{\{\tau<E\}}\) and \(\Lambda=L_T^a\). Let \(R_0\) denote the killed, exponentially discounted resolvent,
\[
R_0f(x)=\mathbb E_x\int_0^\tau e^{-rt}f(Y_t)dt.
\]
For \(s\ge0\), the local-time-penalized resolvent is \(R_sf(x)=\mathbb E_x\int_0^\tau e^{-rt-sL_t^a}f(Y_t)dt\). The strong Markov property at successive visits to \(a\), equivalently the Feynman–Kac resolvent identity for a point-supported measure, gives
\[
R_sf(x)=R_0f(x)-sR_0(x,a)R_sf(a),
\qquad R_0(x,a)=\int_0^\infty e^{-rt}p_t^0(x,a)dt.
\]
This identity can be proved first for bounded approximations of the delta measure and then by occupation-density convergence; finiteness of \(G\) justifies the limiting point-resolvent identity. At \(x=a\),
\[
R_sf(a)=\frac{R_0f(a)}{1+sG}.
\]
Let \(H_s(x)=\mathbb E_x[e^{-r\tau-sL_\tau^a};\tau<\infty]\). The same one-point Feynman–Kac identity with absorption boundary data gives \(H_s(x)=H_0(x)-sR_0(x,a)H_s(a)\). Since \(H_0(a)=q\),
\[
\mathbb E_a[e^{-s\Lambda};J=1]=H_s(a)=\frac{q}{1+sG}.
\]
For the failed attempt, integration over the independent exponential reset time gives
\[
\mathbb E_a[e^{-s\Lambda};J=0]=rR_s1(a)
=\frac{rR_01(a)}{1+sG}=\frac{1-q}{1+sG},
\]
where \(rR_01(a)=\mathbb E_a[1-e^{-r\tau}]=1-q\). Both conditional Laplace transforms therefore equal \((1+sG)^{-1}\): \(\Lambda\) is exponential of mean \(G\) and is independent of whether that attempt ends in absorption or resetting. This conditional independence is the critical step; it does not follow merely from the known marginal local-time distribution.

**Step 2: Repeated attempts and the joint law.** The renewal assumption makes successive \((J,\Lambda)\) pairs i.i.d. with \(\Pr(J=1)=q\). Hence \(N\) is the number of failed attempts preceding the first success, with \(\Pr(N=n)=q(1-q)^n\). Conditional on \(N=n\), \(L\) is a sum of \(n+1\) independent exponentials of mean \(G\), giving the asserted Gamma conditional law. Equivalently, for \(s\ge0\) and \(|z|\le1\),
\[
\mathbb E[z^Ne^{-sL}]
=\sum_{n\ge0}\frac q{1+sG}
\left(\frac{z(1-q)}{1+sG}\right)^n
=\frac q{1+sG-(1-q)z}.
\]
Inverting the \(s\)-transform at fixed \(z\) gives
\[
\mathbb E[z^N;L\in d\ell]=\frac qG\exp\left(-\frac{1-(1-q)z}{G}\ell\right)d\ell.
\]
Coefficient extraction yields the joint density. Summation over \(n\) gives \(f_L(\ell)=(q/G)e^{-q\ell/G}\); division yields the Poisson conditional law. From \(\mathbb E[N\mid L]=(1-q)L/G\), \(\operatorname{Var}(L)=(G/q)^2\), and \(\operatorname{Var}(N)=(1-q)/q^2\), one obtains \(\operatorname{Corr}(N,L)=\sqrt{1-q}\) exactly.

**Step 3: Brownian specialization.** The unique bounded solution of \(Du''=ru\) on \((0,\infty)\) with \(u(0)=1\) is \(u(x)=\exp(-x\sqrt{r/D})\); hence \(q=u(a)\). The absorbed Brownian resolvent kernel is the method-of-images expression
\[
R_0(x,y)=\frac1{2\sqrt{Dr}}
\left(e^{-|x-y|\sqrt{r/D}}-e^{-(x+y)\sqrt{r/D}}\right).
\]
Putting \(x=y=a\) gives the displayed \(G\) and the conditional Poisson intensity. As \(r\downarrow0\), the formulas continuously reduce to \(N=0\) and exponentially distributed \(L\) with mean \(a/D\), as they should.

## Verification

The accompanying `check_joint_localtime.py` evaluates the two-variable discounted boundary-value/resolvent equations independently on finite birth–death chains with absorption, including biased chains and reflecting upper endpoints. It compares direct matrix inversions of the joint transform against the renewal formula for 729 parameter combinations. It also checks 135 continuum Brownian identities (864 assertions in total). Finite-state calculations are cross-checks of algebra and normalization, **not** a substitute for the continuous diffusion proof. Reproduce using Python 3 and NumPy: `python check_joint_localtime.py`.

## Relationship to prior work

Singh and Pal (arXiv:2202.02715, Sec. 3, Eqs. (20)–(22)) already derive the exact **marginal** exponential distribution of first-passage local time at the reset site for Brownian motion; that marginal, its mean and all its moments are not new claims. Dubey and Pal (arXiv:2304.05226, Sec. 3) investigate the corresponding first-passage local-time mean in an Ornstein–Uhlenbeck potential, and Pal et al. (arXiv:1902.00907) study local-time distributions at a **fixed observation horizon**. Standard killed-resolvent perturbations and restart renewal equations are antecedent tools.

The present claim concerns the **joint distribution with the previously unobserved intervention count**: conditional Poisson count reconstruction, Gamma local-time laws conditional on count, exact count–local-time correlation, and diffusion-invariant formulation. The single-observable Feynman–Kac transforms in the cited papers do not by themselves specify the coupling between count and local time. General excursion-process marking results might imply this joint statement; determining whether it was previously formulated elsewhere remains a priority risk, not an assertion of absolute novelty.

## Limitations

The reset site must equal the local-time measurement site and remain fixed; the accumulated local time cannot itself be reset. The clock is Poisson and independent of the motion. The origin is absorbing and the process begins at the reset site. The theorem is an exact distributional identity, not an experimental validation: finite local-time estimates from spatial bins have discretization bias. No claim is made about non-exponential reset clocks, multi-site resetting, or inference when \(q,G\) are unknown.

## References

1. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715 (first public 2022-02-06), especially Sec. 3: https://arxiv.org/abs/2202.02715.
2. A. Dubey and A. Pal, *First-passage functionals for Ornstein Uhlenbeck process with stochastic resetting*, arXiv:2304.05226 (first public 2023-04-11), Sec. 3: https://arxiv.org/abs/2304.05226.
3. A. Pal, R. Chatterjee, S. Reuveni and A. Kundu, *Local time of diffusion with stochastic resetting*, arXiv:1902.00907 (first public 2019-02-03), Secs. III–IV: https://arxiv.org/abs/1902.00907.
4. P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868 (first public 2022-03-09): https://arxiv.org/abs/2203.04868.
