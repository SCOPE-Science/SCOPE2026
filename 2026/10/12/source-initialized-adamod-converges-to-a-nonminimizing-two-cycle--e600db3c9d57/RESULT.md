# Source-initialized AdaMod converges to a nonminimizing two-cycle after initial descent
## Finding

Consider precisely Algorithm 2 of *An Adaptive and Momental Bound Method for Stochastic Learning* (AdaMod) with constant learning rate and its printed initial states. On the one-dimensional strongly convex quadratic
\[
f(x)=\frac h2 x^2,\qquad h>0,
\]
let \(\epsilon>0\) be the denominator stabilizer and \(\alpha>0\) the constant base learning rate. Set
\[
\beta_1=\beta_2=0,\quad
\frac7{100}\le d:=\beta_3\le\frac{13}{100},\quad
\frac{40}{11}\le\frac{\alpha h}{\epsilon}\le\frac{40}{9},\quad
r=\frac\alpha2-\frac\epsilon h>0,
\]
and initialize
\[
x_0=r,\qquad m_0=v_0=s_0=0.
\]

**The source run decreases the objective strictly at its first step, yet converges to a nonminimizing alternating orbit.** More precisely,
\[
x_1=(2d-1)r,\qquad 0<f(x_1)<f(x_0),
\]
and for every integer \(t\ge1\),
\[
\boxed{\left|x_t-(-1)^t r\right|\le
\frac{13}{50}\,r\left(\frac{24}{25}\right)^{t-1}.}
\]
Consequently,
\[
\lim_{t\to\infty} f(x_t)=\frac h2 r^2>0=f(0),
\]
and the actual rate-memory variable tends to \(2/h\) although the initial cap is active.

The same source-initialized, first-step-descending, nonminimizing alternating behavior **persists with both moment parameters strictly positive** in a sufficiently small parameter neighborhood of the explicit central instance
\[
d=\frac1{10},\qquad \frac{\alpha h}{\epsilon}=4,
\]
with \(0<\beta_1,\beta_2<\delta\) for some \(\delta>0\) independent of iteration number. For this extension put
\[
k=\frac{1-\beta_1}{1+\beta_1},\qquad
r_{\beta}=\frac{\alpha k}{2}-\frac\epsilon h>0,
\]
and use source initialization \(x_0=r_{\beta}\) and \(m_0=v_0=s_0=0\). Then
\[
0<f(x_1)<f(x_0),\qquad
x_t-(-1)^t r_{\beta}\longrightarrow0.
\]
The existence of a sufficiently small neighborhood is proved; no particular numerical value of \(\delta\) is claimed.

## Assumptions and scope

The precise printed scalar update is, for integers \(t\ge1\),
\[
\begin{aligned}
g_t&=hx_{t-1},\\
m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t,\\
v_t&=\beta_2v_{t-1}+(1-\beta_2)g_t^2,\\
\eta_t&=\frac{\alpha}{\sqrt{v_t/(1-\beta_2^t)}+\epsilon},\\
s_t&=\beta_3s_{t-1}+(1-\beta_3)\eta_t,\\
x_t&=x_{t-1}-\min\{\eta_t,s_t\}\frac{m_t}{1-\beta_1^t}.
\end{aligned}
\]
All states start at zero except the parameter \(x_0\), and the cap is **not** switched off or replaced by a stationary upper bound. A constant base rate is allowed by the source. The main theorem uses the admissible limiting moment settings \(\beta_1=\beta_2=0\); the positive-moment robustness statement uses small strictly positive values.

The claim concerns a deterministic scalar quadratic and this source algorithm, not all optimizers, stochastic gradients, the paper's default \(\beta_3\), or a global convergence theorem. Geometric convergence is toward a nonzero alternating orbit, **not** toward the optimum.

## Proof

### Exact source update

Initially \(\eta_1=\alpha/(hr+\epsilon)=2/h\), so the first memory state is \(s_1=2(1-d)/h\), the cap is active, and
\[
x_1=r-\frac{2(1-d)}h (hr)=(2d-1)r.
\]
Our \(d\) interval makes \(-1<2d-1<0\), hence strict first-step objective descent.

### Explicit invariant contraction for all subsequent source steps

Define the curvature-scale parameter
\[
\kappa=\frac{hr}{hr+\epsilon}=1-\frac{2\epsilon}{\alpha h}
\in\left[\frac9{20},\frac{11}{20}\right].
\]
For an iterate of sign \((-1)^t\), put
\[
u_t=\frac{|x_t|}{r},\qquad z_t=\frac h2s_t,
\qquad H(u)=\frac1{1+\kappa(u-1)}.
\]
The rate-memory recurrence is exactly
\[
z_{t+1}=dz_t+(1-d)H(u_t).
\]
If its next step changes sign, the magnitude recurrence is exactly
\[
u_{t+1}=u_t\left(2\min\{H(u_t),z_{t+1}\}-1\right).
\]
These two maps define \(T(u,z)\). The point \((1,1)\) is a fixed point, and the post-first-step source state is
\[
(u_1,z_1)=(1-2d,1-d).
\]

Consider the closed convex square
\[
B=\left[\frac7{10},\frac{13}{10}\right]^2.
\]
On \(B\), \(H(u)\ge1/(1+33/200)>1/2\) and the next smoothed state \(z'\ge7/10\); therefore the minimum is at least \(7/10\), every update strictly reverses the parameter sign, and the magnitude chart is valid.

Set
\[
F(u,\kappa)=H(u)+uH'(u)=
\frac{1-\kappa}{[1+\kappa(u-1)]^2}.
\]
Elementary endpoint monotonicity on the displayed rectangle gives the sharp convenient bounds
\[
\frac{18000}{54289}\le F\le\frac{22000}{29929},
\qquad
|H'(u)|\le\frac{22000}{27889}.
\]
For completeness, the lower value of \(F\) is at \((\kappa,u)=(11/20,13/10)\), the upper value is at \((9/20,7/10)\), and \(|H'|\) is maximal at \((11/20,7/10)\). The relevant derivatives have the following bounds in the supremum norm.

If \(H(u)\le z'\) (unclipped branch),
\[
\left|\frac{\partial u'}{\partial u}\right|
=|2F-1|<\frac{12}{25}.
\]
If \(z'<H(u)\) (clipped branch),
\[
\frac{\partial u'}{\partial u}
=2dz+2(1-d)F-1,
\qquad
\frac{\partial u'}{\partial z}=2du.
\]
The first derivative lies between \(-0.286\) and \(0.618\); the second has magnitude at most \(0.338\). More sharply, the maximal first-row absolute sum is bounded by the exact rational number
\[
\left(\frac{13}{50}\frac{13}{10}
 +2\frac{87}{100}\frac{22000}{29929}-1\right)
 +\frac{13}{50}\frac{13}{10}
 <\frac{24}{25}.
\]
(The endpoint expression uses \(2dz\) at its maximum, not a bound with independent choices of \(d\).) The memory row has absolute derivative sum at most
\[
d+(1-d)\frac{22000}{27889}<\frac{24}{25}.
\]
Across the \(\min\)-switch boundary the map is continuous and piecewise differentiable. Integrating the above uniformly bounded derivatives along any line segment within the convex square shows
\[
\|T(U)-T(V)\|_\infty\le\frac{24}{25}\|U-V\|_\infty
\qquad(U,V\in B).
\]
As \(T(1,1)=(1,1)\) and \(\|U-(1,1)\|_\infty\le3/10\) on \(B\), the same inequality shows \(T(B)\subset B\). Thus the source trajectory remains in the square, alternates in sign at every step, and satisfies
\[
\|(u_t,z_t)-(1,1)\|_\infty
\le\left(\frac{24}{25}\right)^{t-1}
\|(u_1,z_1)-(1,1)\|_\infty
\le\frac{13}{50}\left(\frac{24}{25}\right)^{t-1}.
\]
This proves the global-in-time estimate and the nonzero objective limit.

### Robustness to small positive first- and second-moment decay

Fix \(d=1/10\), \(\alpha h/\epsilon=4\), and let \(\beta_1,\beta_2\) vary near zero. Set \(k=(1-\beta_1)/(1+\beta_1)\), \(r_\beta=\alpha k/2-\epsilon/h\), and \(E=2/(kh)\). At step \(t\), assume the source parameter has the expected sign \((-1)^{t-1}\). Normalize the previous first-moment state by writing
\[
x_{t-1}=(-1)^{t-1}r_\beta u,
\qquad m_{t-1}=(-1)^t h r_\beta w,
\qquad v_{t-1}=h^2r_\beta^2 V,
\qquad s_{t-1}=E z.
\]
Define
\[
\begin{aligned}
W&=(1-\beta_1)u-\beta_1w,\\
V'&=\beta_2V+(1-\beta_2)u^2,\\
H_t&=\frac{hr_\beta+\epsilon}{hr_\beta\sqrt{V'/(1-\beta_2^t)}+\epsilon},\\
z'&=dz+(1-d)H_t,\\
u'&=\frac2k\min\{H_t,z'\}
\frac{W}{1-\beta_1^t}-u,\\
w'&=W.
\end{aligned}
\]
Whenever \(u'>0\), this is exactly the next signed chart of the printed, bias-corrected algorithm; the fourth coordinate is \(V'\). Omitting the two bias-correction powers gives the autonomous tail map. Its fixed point is
\[
(u,w,V,z)=(1,k,1,1),
\]
which corresponds to the nonzero symmetric two-cycle. Indeed \(W=k\), \(V'=1\), \(H_t=1\) in the autonomous map, and its capped rate equals \(E\).

At \(\beta_1=\beta_2=0\), the \((u,z)\)-subsystem is the just-proved strict contraction, while \(w'=u\) and \(V'=u^2\) are slaved outputs with no feedback. On a sufficiently small closed neighborhood of \((1,1,1,1)\), the product norm
\[
\|(\Delta u,\Delta w,\Delta V,\Delta z)\|_*
=\max\{|\Delta u|,|\Delta z|,\tfrac1{10}|\Delta w|,
\tfrac1{10}|\Delta V|\}
\]
makes every branch derivative have operator norm strictly below one: the first two rows retain their strict bound below \(24/25\), and the weighted slaved rows are bounded by \(1/10\) and approximately \(1/5\) near \(u=1\). By continuity of both smooth branches and compactness of a sufficiently small neighborhood, the autonomous tail maps for all sufficiently small nonnegative \(\beta_1,\beta_2\) have a common contraction factor \(\rho<1\), preserve a small ball around their fixed point, and keep \(u'>0\). The continuous minimum of the two branches inherits the same Lipschitz bound by segment integration.

At zero decay, the actual initialized trajectory converges to the fixed point. Choose a finite time \(N\) for which the signed source state is strictly inside the small contraction ball. Every one of the first \(N\) bias-corrected update formulas and its sign branch depends continuously on \((\beta_1,\beta_2)\) near \((0,0)\), so the perturbed source trajectory still enters that ball if both parameters are small enough. On it, the bias corrections are a uniformly bounded vanishing perturbation satisfying
\[
\|T_t(Y)-T_\infty(Y)\|_*
\le C(\beta_1^t+\beta_2^t),
\]
with a constant \(C\) independent of \(t\). Shrinking the parameter neighborhood also makes the perturbation small enough to keep the entire future trajectory within the contraction ball. Thus its distance \(e_t\) to the tail fixed point obeys
\[
e_{t+1}\le\rho e_t+C(\beta_1^{t+1}+\beta_2^{t+1}),
\]
which tends to zero by the geometric convolution bound. The actual bias-corrected source run therefore tends to the nonminimizing alternating cycle, without asserting any exact finite-time periodicity for positive moment decays.

Finally, its first source step satisfies
\[
\frac{x_1}{x_0}=1-\frac{2(1-d)}k,
\]
so strict first-step objective descent persists whenever \(k>1-d\), which holds for sufficiently small positive \(\beta_1\). The robustness statement follows.

## Verification

The accompanying standalone `verify.py` replays the printed source equations with both the zero-decay and small positive-decay moments, checks the first-step identity, calculates exact rational derivative certificates for the entire contraction square, and compares the observed signed trajectory with the proved geometric bound. It also checks the limiting autonomous tail fixed point with nonzero moments and the first-step descent condition.

Finite numerical iterations are diagnostic and cannot establish convergence or basin invariance. Those infinite-time conclusions instead follow from the explicit rational Lipschitz certificate and the perturbative contraction argument above.

## Relationship to prior work

Ding, Ren, Luo, and Sun introduce AdaMod's exponential moving average of adaptive learning rates and the \(\min\)-cap precisely to suppress unexpectedly large early learning rates (Algorithm 2). Their primary source contains empirical stability results and no theorem determining the nonzero asymptotic state of a source-initialized strongly convex quadratic in the parameter regime above.

Bock and Weiß establish nontrivial two-cycles for **Adam** and their attraction under bias-corrected dynamics. That prior fact is not claimed as new, and it does not settle AdaMod's additional memory state, active transient cap, and exact invariant source basin. The exact one-step attenuation of AdaMod's cap is elementary and already known; the new statement concerns the entire actual source trajectory, including convergence to a nonzero cycle despite initial descent.

AdaBound's time-varying manually prescribed upper/lower learning-rate bounds and their convergence theory are structurally different from AdaMod's recursively smoothed data-dependent cap. A recent optimization-algorithm survey reports observed AdaMod deterioration after its best iterate. Its accessible excerpt does not resolve the exact two-cycle comparison; its full text was not inspected, which is a residual access risk.

Searches for AdaMod non-convergence, limit cycles, scalar quadratic source initialization, adaptive-rate-memory recurrences, and equivalence with Adam did not reveal the established explicit invariant square or its positive-moment continuation. Absence of a search hit is not a uniqueness certificate.

## Limitations

The proved explicit interval uses \(0.07\le\beta_3\le0.13\), not the paper's common smoothing defaults close to one. It therefore proves existence of a robust failure regime, not failure under all recommended hyperparameters. The strictly positive moment extension is existential in its neighborhood radius, not a uniform quantitative bound across standard defaults. The theorem assumes a constant base learning rate and a deterministic one-dimensional strongly convex objective. It does not contradict learning-rate-decay convergence results for other methods.

The optimizer trajectory is not exactly periodic at finite time when positive moment decays retain bias corrections: only its asymptotic signed two-cycle is asserted. Exact numerical tests alone do not prove an infinite-time theorem. No independent audit has been performed.

## References

1. Jianbang Ding, Xuancheng Ren, Ruixuan Luo, Xu Sun, *An Adaptive and Momental Bound Method for Stochastic Learning*, arXiv:1910.12249v1, first posted 2019-10-27. Algorithm 2; full primary text.
2. Sebastian Bock and Martin Weiß, *Non-Convergence and Limit Cycles in the Adam Optimizer*, arXiv:2210.02070v1, 2022-10. Full primary text.
3. Liangchen Luo, Yuanhao Xiong, Yan Liu, Xu Sun, *Adaptive Gradient Methods with Dynamic Bound of Learning Rate*, arXiv:1902.09843v1, 2019-02-26.
4. *First-order optimization algorithms: state of the art, classification, and performance: a practitioner's guide*, DOI:10.1007/s00521-026-12014-1, 2026, qualitative numerical AdaMod discussion; the full text was not accessible in the available route, so not relied on for a negative whole-document claim.
