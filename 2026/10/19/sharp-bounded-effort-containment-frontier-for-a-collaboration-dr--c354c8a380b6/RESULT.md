# Sharp bounded-effort containment frontier for a collaboration-driven population threshold

## Finding

An increasing per-capita growth response creates a sharp and globally optimal intervention schedule: among all time-dependent proportional removals with the same cumulative effort and the same rate cap, **spending the effort immediately minimizes the population at every subsequent time**. For the collaboration-driven population law of Crawley and Tanaka [1], this observation gives an exact intervention-rate feasibility condition, the minimum integrated effort to reach the uncontrolled takeoff threshold, and a strictly decreasing cost-versus-rate frontier. Neither instantaneous suppression nor an unspecified large total budget can replace the cap condition.

More precisely, suppose the controlled evolution is
\[
\dot N(t)=N(t)\bigl[a-bN(t)^{-\beta}-u(t)\bigr],\qquad
0\le u(t)\le U,
\]
with \(a,b,\beta>0\), cumulative per-capita effort \(H(t)=\int_0^t u(s)\,ds\), and an initial population \(N_0>N_c=(b/a)^{1/\beta}\). Set
\[
Y_0=N_0^\beta,\qquad Y_c=b/a,\qquad
g_0=a-\frac{b}{Y_0}>0.
\]

**Fixed-budget ordering.** For any finite horizon \(T>0\) and any budget \(0\le B\le UT\), let
\[
u_F(t)=U\,\mathbf 1_{[0,B/U]}(t),\qquad
u_L(t)=U\,\mathbf 1_{[T-B/U,T]}(t).
\]
For every measurable admissible \(u\) with \(H(T)=B\), the corresponding solutions satisfy
\[
N_F(t)\le N_u(t)\quad(0\le t\le T),\qquad
N_F(T)\le N_u(T)\le N_L(T).
\]
The finite-time comparisons are taken only while the modeled populations remain in their stated admissible domain. If \(0<B<UT\), the first and last terminal inequalities are strict unless the competing control coincides almost everywhere with the relevant extreme control. Thus the front-loaded and back-loaded controls are the unique terminal minimizer and maximizer, respectively, up to null sets.

**Exact threshold-access cost.** A bounded intervention can bring \(N\) from \(N_0>N_c\) to \(N_c\) in finite time if and only if
\[
\boxed{U>g_0.}
\]
When this holds, the smallest cumulative effort over all schedules and all times is \(B_c(U)=U t_c(U)\), attained uniquely by applying \(u=U\) from the initial time until the first threshold hit. Writing \(d=a-U\),
\[
\boxed{
t_c(U)=
\begin{cases}
\displaystyle\frac{1}{\beta d}
\log\!\left(\frac{Y_c-b/d}{Y_0-b/d}\right),&d\ne0,\\[7pt]
\displaystyle\frac{Y_0-Y_c}{\beta b},&d=0.
\end{cases}}
\]
The logarithm has a strictly positive argument in the stated domain and yields \(t_c>0\). Every schedule with total cumulative effort strictly below \(B_c(U)\) fails to reach the threshold at any time. For an observation deadline \(T\), weak threshold access is feasible exactly when \(T\ge t_c(U)\) and the available budget is at least \(B_c(U)\). Strict crossing below \(N_c\) needs effort strictly greater than \(B_c(U)\); it can be achieved by keeping the maximum-rate control active slightly beyond \(t_c\).

For \(U>g_0\), the critical budget also has the exact integral representation
\[
\boxed{B_c(U)=\int_{N_c}^{N_0}\frac{U}{U-g(N)}\,\frac{dN}{N},\qquad
g(N)=a-bN^{-\beta}.}
\]
Consequently it is strictly decreasing in \(U\), satisfies
\[
B_c(U)>\log(N_0/N_c),\qquad
\lim_{U\to\infty}B_c(U)=\log(N_0/N_c),
\]
and diverges logarithmically as the rate cap approaches the growth rate from above. Specifically, putting \(\varepsilon=U-g_0\downarrow0\),
\[
B_c(U)=\frac{g_0}{\beta(a-g_0)}\log\!\left(
\frac{Y_c g_0}{Y_0\varepsilon}
\right)+o(1).
\]
These limits distinguish an unattainable instantaneous-removal cost from the larger effort required at every finite admissible intervention rate.

## Assumptions and scope

The motivating population law [1, Equations (4), (16), and (18)] has
\[
p(N)=1-(1-p_{\mathrm{ref}})(N/N_{\mathrm{ref}})^{-\beta},\qquad
\tau\dot N=N[\kappa p(N)-\mu].
\]
Choose \(\tau,\kappa,\mu,N_{\mathrm{ref}},\beta>0\) and \(0\le p_{\mathrm{ref}}<\mu/\kappa<1\). The new control \(u\) represents an **added per-capita loss intensity**, not a change of the published success-probability law. Its definition is the explicitly extended equation
\[
\tau\dot N=N[\kappa p(N)-\mu-\tau u(t)].
\]
Dividing by \(\tau\) gives the displayed differential equation with
\[
a=(\kappa-\mu)/\tau,\qquad
b=\kappa(1-p_{\mathrm{ref}})N_{\mathrm{ref}}^\beta/\tau.
\]
The uncontrolled critical population is \(N_c=(b/a)^{1/\beta}>N_{\mathrm{ref}}\). The initial population \(N_0>N_c\) is arbitrary. Controls are Lebesgue measurable with \(u\in[0,U]\) almost everywhere; a finite total budget is an \(L^1\) integral of this rate. Time is continuous and population is a positive real variable, as in the source's deterministic model.

Since the published probability formula is physically calibrated for populations \(N\ge N_{\mathrm{ref}}\), the threshold-access assertion uses solutions only until their first encounter with \(N_c>N_{\mathrm{ref}}\). The finite-horizon ordering applies on intervals for which the compared trajectories stay at least \(N_{\mathrm{ref}}\). It does not assert that the probability law retains empirical meaning below the reference scale.

## Proof

**1. Exact controlled reduction.** Set \(Y=N^\beta\). Wherever the solution is positive, the chain rule gives
\[
\dot Y=\beta(a-u(t))Y-\beta b.
\]
Let \(H(t)=\int_0^t u(s)\,ds\). Multiplication by the integrating factor \(e^{-\beta at+\beta H(t)}\) proves, for every admissible measurable control,
\[
\boxed{
Y_u(t)=e^{\beta(at-H(t))}
\left[Y_0-\beta b\int_0^t e^{-\beta(as-H(s))}\,ds\right].}
\]
The identity holds on the positive solution interval. It also supplies uniqueness and is consistent with the Carathéodory ODE for bounded measurable controls.

**2. Strict terminal ordering.** Fix \(T,B,U\). The cumulative effort of any admissible control satisfies
\[
\max\{0,B-U(T-t)\}=H_L(t)\le H_u(t)
\le H_F(t)=\min\{Ut,B\}.
\]
At the common terminal total \(H(T)=B\), the exact formula gives the identity
\[
\begin{aligned}
Y_u(T)-Y_F(T)
&=\beta b\,e^{\beta(aT-B)}
\int_0^T e^{-\beta as}
\bigl(e^{\beta H_F(s)}-e^{\beta H_u(s)}\bigr)\,ds\ge0.
\end{aligned}
\]
Similarly \(Y_L(T)-Y_u(T)\ge0\). Since \(b,\beta>0\), the difference is strictly positive whenever the cumulative curves differ on a set of positive measure. Equality implies \(H_u=H_F\) everywhere by continuity, hence \(u=u_F\) almost everywhere; the analogous statement holds for \(u_L\). The map \(Y\mapsto N=Y^{1/\beta}\) is strictly increasing.

For the pointwise lower bound, at each \(t\), \(H_F(t)\ge H_u(t)\) and \(H_F(s)\ge H_u(s)\) for \(0\le s\le t\). In the explicit formula, the front-loaded outside factor is no larger and its bracket is no larger. Both brackets are positive while the populations are positive, proving \(Y_F(t)\le Y_u(t)\), as required.

**3. Feasibility of crossing the natural threshold.** The uncontrolled per-capita growth \(g(N)=a-bN^{-\beta}\) increases strictly with \(N\) and is positive for \(N>N_c\). If \(U\le g_0=g(N_0)\), even the constant maximal intervention has \(\dot N(0)\ge0\), and its scalar autonomous trajectory cannot decrease from \(N_0\); indeed \(g(N)\ge g_0\) for \(N\ge N_0\). Every smaller intervention is pointwise less effective by the scalar comparison theorem. Thus no admissible control can reach \(N_c\).

If \(U>g_0\), the constant intervention \(u=U\) gives \(\dot N<0\) throughout \([N_c,N_0]\), so it hits \(N_c\) exactly once in finite time. Solving the scalar affine equation for \(Y\) at constant \(U\) yields the stated logarithmic time formula, or its linear limit when \(d=0\). The argument is positive: if \(d>0\), \(b/d>Y_0>Y_c\); if \(d<0\), \(b/d<0<Y_c<Y_0\).

For any candidate strategy with total effort at most \(B\), its cumulative curve is bounded above by \(\min\{Ut,B\}\), the curve generated by applying \(U\) immediately for time \(B/U\) and then stopping. The pointwise ordering therefore says the latter trajectory is no larger until threshold access. If \(B<B_c(U)\), that immediately exhausted trajectory stops while still above \(N_c\) and subsequently increases, never reaching it. Thus no such candidate can reach \(N_c\). At \(B=B_c(U)\) the maximal initial control reaches \(N_c\) at time \(t_c\) and stays there if the control is released. Uniqueness of the minimizer follows from strict terminal ordering; a trajectory that has passed below \(N_c\) cannot subsequently return above it with \(u\ge0\). This also establishes the claimed deadline and strict-crossing distinctions.

**4. The cost frontier.** Along the declining maximal-control trajectory \(dt=-dN/[N(U-g(N))]\). This proves the integral formula. For \(N_c<N\le N_0\), \(0<g(N)\le g_0<U\). Hence the integrand \(U/(U-g(N))\) is strictly greater than one and has strictly negative derivative \(-g(N)/(U-g(N))^2\) with respect to \(U\); dominated convergence yields the impulse-limit logarithm. For \(U=g_0+\varepsilon\) and \(\varepsilon\downarrow0\), put \(r=b/Y_0=a-g_0>0\), so \(d=r-\varepsilon\). Substitution into the hitting-time formula gives the exact identity
\[
\frac{Y_c-b/d}{Y_0-b/d}
=\frac{Y_c(g_0+\varepsilon)}{Y_0\varepsilon},
\]
whence \(B_c(U)=\frac{g_0+\varepsilon}{\beta(r-\varepsilon)}\log\bigl[Y_c(g_0+\varepsilon)/(Y_0\varepsilon)\bigr]\). Since \(r=a-g_0\), this establishes the displayed asymptotic with an \(o(1)\) remainder.

## Verification

A standalone `verify.py` checks 162 exact rational identities for the power transformation, exact threshold times in the following witness, monotonicity on seven finite rate-cap values, and a numerical consistency check for the integral formula measuring the difference between early and uniform policies. The general theorems follow from the displayed exact algebra and comparison, **not** from finitely many sampled profiles.

Choose \(\tau=1\), \(\kappa=2\), \(\mu=1\), \(N_{\mathrm{ref}}=1\), \(p_{\mathrm{ref}}=0\), \(\beta=1\), and \(N_0=4\). Then \(a=1\), \(b=2\), \(N_c=2\), and \(g_0=1/2\). A cap \(U=1/2\) cannot reach \(N_c\); cap \(U=1\) reaches \(N_c\) after one unit of time at budget \(B_c=1\); cap \(U=2\) reaches \(N_c\) at time \(\log(3/2)\) with budget \(2\log(3/2)\). The impulse lower limit is \(\log2\). This is an exact rational-and-logarithmic instance of the full feasibility frontier.

## Relationship to prior work

Crawley and Tanaka [1] derive the uncontrolled population law, its success scaling and the threshold \(N_c\). Their discussion motivates population pacing but contains no bounded cumulative-intervention theorem or sharp removal-cost frontier; their Appendix A considers finite search-depth corrections and Appendix B considers alternative collaboration laws. The present theorem adds a specified loss control and characterizes **all** admissible time-varying schedules for a fixed budget and cap.

The general facts that integrating factors solve linear scalar equations and that early bang-bang actions can be optimal in some harvesting problems are established principles, not claimed independently as new. Cid, Hilker and Liz [2] study the influence of impulsive within-season harvest timing on discrete nonlinear population maps, including Allee effects, with a different state recurrence and different budget notion. Grey, Lenhart, Hilker and Franco [3] optimize harvest timing, yield and costs for discrete seasonal Beverton–Holt/Ricker-type maps, and obtain regimes where intermediate harvesting can be preferred. Neither paper states the exact all-measurable-control cumulative-effort ordering or the critical integrated-loss frontier for law [1]. Lu, Liu and Li [4] study economic-optimal harvesting in an interacting two-species Allee system, not this one-dimensional takeoff-threshold access problem. These are mathematical distinctions, not assertions that analogous optimal-control methods were previously unknown.

## Limitations

The model is deterministic and homogeneous; intervention removes a fixed per-capita fraction per unit time. The cumulative effort \(\int u\) is not the number of removed individuals or a monetary expenditure, and neither variable unit costs nor intervention delays are included. The threshold criterion describes access to the *uncontrolled* declining basin, not long-term extinction below the calibration scale \(N_{\mathrm{ref}}\). No claims are made for the source's congestion model, where growth need not be increasing, or for stochastic, network-resolved or discrete-population dynamics. Optimality under those different assumptions is open here. An unindexed general monotone-control theorem could subsume the scheduling lemma; the specific sharp frontier is proved in full, but independent originality validation has not been performed.

## References

[1] E. Crawley and H. Tanaka, *Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff*, arXiv:2610.12436v1 (first posted 8 October 2026), https://arxiv.org/html/2610.12436v1 .

[2] B. Cid, F. M. Hilker and E. Liz, *Harvest timing and its population dynamic consequences in a discrete single-species model*, Mathematical Biosciences 248 (2014), 78–87, DOI: 10.1016/j.mbs.2013.12.003.

[3] S. Grey, S. Lenhart, F. M. Hilker and D. Franco, *Optimal control of harvest timing in discrete population models*, Natural Resource Modeling (2021), DOI: 10.1111/nrm.12321.

[4] C. Lu, X. Liu and Z. Li, *The dynamics and harvesting strategies of a predator-prey system with Allee effect on prey*, AIMS Mathematics 8 (2023), 28897–28925, DOI: 10.3934/math.20231481.
