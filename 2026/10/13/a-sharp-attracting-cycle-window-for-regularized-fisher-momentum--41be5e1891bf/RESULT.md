# A sharp attracting-cycle window for regularized-Fisher momentum on strongly convex quadratics

## Finding

The scalar specialization of the published SOFIM algorithm can approach a nonminimizing, attracting two-cycle from an **open interval of source initializations**, even on a deterministic strongly convex quadratic. Its limiting autonomous system has an exact and sharp two-cycle stability window.

Let
\[
f(x)=\frac{h}{2}x^2,\qquad h>0,
\]
and use learning rate \(\eta>0\), Fisher regularization \(\rho>0\), and moment decay \(0\le\beta<1\). Retain the paper's zero initialization \(M_0=0\) and first-moment bias correction. Introduce dimensionless variables and parameters
\[
y_t=\frac{h x_t}{\sqrt\rho},\quad
u_t=\frac{M_t}{\sqrt\rho},\quad
c=\frac{\eta h}{\rho},\quad
q=\frac{1-\beta}{1+\beta},\quad
s=cq.
\]
The optimizer is **exactly**
\[
\begin{aligned}
 u_t&=\beta u_{t-1}+(1-\beta)y_{t-1},\\
 y_t&=y_{t-1}-c\,\frac{u_t/(1-\beta^t)}{1+[u_t/(1-\beta^t)]^2}
 \qquad(t\ge1).
\end{aligned}
\]

Remove only the vanishing bias-correction factor in the *limiting* state map. This autonomous map has a unique nonzero **sign-symmetric** two-cycle if and only if \(s>2\), with dimensionless parameter amplitude
\[
\boxed{
a=\frac{\sqrt{s/2-1}}{q}.
}
\]
It is linearly asymptotically stable **if and only if**
\[
\boxed{2<s<4.}
\]
At \(s=4\) it has a unit characteristic multiplier and is not hyperbolic; for \(s>4\) it is unstable. These statements concern sign-symmetric two-cycles, not the exclusion of other recurrent dynamics.

More strongly, the actual **bias-corrected, source-initialized SOFIM** converges to such a nonzero two-cycle for a full, explicitly certified open set of initial states. Fix
\[
c=3,\qquad 0\le\beta\le\frac1{100},\qquad M_0=0,
\]
and let the source parameter vary throughout
\[
\boxed{\left|\frac{h x_0}{\sqrt\rho}-\frac1{\sqrt2}\right|\le\frac1{100}.}
\]
With
\[
a_\beta^2=\frac{(1-5\beta)(1+\beta)}{2(1-\beta)^2},
\qquad q=\frac{1-\beta}{1+\beta},
\]
the actual iterates satisfy, for every integer \(t\ge1\),
\[
\boxed{
\max\left\{
\left|y_t-(-1)^t a_\beta\right|,
\frac14\left|u_t-(-1)^{t-1}q a_\beta\right|
\right\}
\le\frac{2}{125}\left(\frac23\right)^{t-1}.
}
\]
In particular, the objective has the strictly positive limit
\[
\boxed{
\lim_{t\to\infty}f(x_t)
=\frac{\rho(1-5\beta)(1+\beta)}{4h(1-\beta)^2}>0,
}
\]
although its unique minimum equals zero. For \(\beta=0\), the center of the displayed initialization interval is itself an exact period-two orbit from the first update. For strictly positive \(\beta\), the finite-time orbit is not claimed to be exactly periodic; it converges geometrically to the limiting two-cycle.

## Assumptions and scope

All gradients are exact and deterministic. The objective is one-dimensional and strongly convex, with constant positive curvature \(h\). It can also be realized, up to an additive constant, as the negative log likelihood of a one-observation Gaussian location model with known precision \(h\) and observed datum zero. All parameters are constant, with \(\rho>0\) and \(0\le\beta<1\). The actual recurrence includes the first-moment bias correction \(1-\beta^t\), and the source moment equals zero. SOFIM's regularized Fisher rank-one update is used exactly as printed in Algorithm 1 of the defining paper; there is no additional gradient clipping, line search, step decay, or weight decay.

The first part characterizes only sign-symmetric nonzero period-two orbits of the limiting autonomous map. The second part establishes geometric attraction for the **actual** nonautonomous bias-corrected recurrence over a nondegenerate interval of source parameters and an explicit positive-momentum interval. It does not establish a global basin or enumerate higher-period cycles.

## Proof

### 1. Exact scalar reduction

Algorithm 1 updates
\[
M_t=\beta M_{t-1}+(1-\beta)h x_{t-1},
\qquad
\widehat M_t=\frac{M_t}{1-\beta^t}
\]
and uses the regularized rank-one Fisher inverse on \(\widehat M_t\). In one dimension, Sherman--Morrison reduces exactly to
\[
(\widehat M_t^2+\rho)^{-1}\widehat M_t
=\frac{\widehat M_t}{\rho+\widehat M_t^2}.
\]
Multiplying the parameter update by \(h/\sqrt\rho\) gives the displayed dimensionless recurrence, without approximations.

Write
\[
\psi(v)=\frac{v}{1+v^2}.
\]
The limiting autonomous state map, acting on the old state \((y,u)\), is
\[
H_\beta(y,u)=\left(y-c\psi(\beta u+(1-\beta)y),\,
\beta u+(1-\beta)y\right).
\]
The actual step at time \(t\) replaces \(\psi(m)\) in its first component by \(\psi(m/(1-\beta^t))\), where \(m=\beta u+(1-\beta)y\).

### 2. Exact sign-symmetric period-two orbit and sharp stability

Look for a sign-symmetric two-cycle of \(H_\beta\) whose state before a positive-to-negative transition is
\[
(y,u)=(a,-qa),\qquad a>0.
\]
The new moment is \(qa\), because \(\beta(-qa)+(1-\beta)a=qa\) is precisely equivalent to \(q=(1-\beta)/(1+\beta)\). To reach \((-a,qa)\), the parameter equation must satisfy
\[
2a=\frac{cqa}{1+q^2a^2}.
\]
Since \(a>0\), this is equivalent to
\[
1+q^2a^2=\frac{cq}{2}=\frac s2.
\]
Thus exactly one positive amplitude exists if and only if \(s>2\), and it is the amplitude in the finding. Oddness gives the return transition.

At either cycle state, the Jacobian is identical because
\[
\psi'(v)=\frac{1-v^2}{(1+v^2)^2}
\]
is even. Put \(k=c\psi'(qa)\). The Jacobian, its trace and its determinant are
\[
J=\begin{pmatrix}
1-(1-\beta)k&-\beta k\\
1-\beta&\beta
\end{pmatrix},
\quad
\operatorname{tr}J=1+\beta-(1-\beta)k,
\quad
\det J=\beta.
\]
Using \(q^2a^2=s/2-1\) gives the **exact** quadratic Jury quantities
\[
\begin{aligned}
1-\operatorname{tr}J+\det J
 &=\frac{2(1+\beta)(4-s)}{s},\\
1+\operatorname{tr}J+\det J
 &=\frac{4(1+\beta)(s-2)}{s},\\
1-\det J&=1-\beta.
\end{aligned}
\]
A real quadratic polynomial has both characteristic roots strictly inside the unit disk precisely when all three displayed quantities are positive. Since \(0\le\beta<1\) and the two-cycle requires \(s>2\), the condition is precisely \(s<4\). The two-step cycle map has derivative \(J^2\), so the same strict stability condition applies. At \(s=4\), \(J\) has eigenvalue \(+1\), and for \(s>4\) the first Jury inequality is negative, yielding instability.

### 3. An explicit source-initialized attracting basin

Fix \(c=3\), \(0\le\beta\le1/100\), and let
\[
a_0=\frac1{\sqrt2},\qquad
 a_\beta^2=\frac{(1-5\beta)(1+\beta)}{2(1-\beta)^2}.
\]
Direct differentiation shows \(a_\beta^2\) decreases on this interval, while
\[
q^2a_\beta^2=\frac{1-5\beta}{2(1+\beta)}
\]
also decreases. Elementary rational endpoint comparisons give
\[
\frac{699}{1000}<a_\beta<\frac{708}{1000},
\qquad
\frac{685}{1000}<q a_\beta<\frac{708}{1000}.
\]
The limiting cycle states at successive phases are
\[
P_+=\big(a_\beta,-q a_\beta\big),
\qquad
P_-=\big(-a_\beta,q a_\beta\big).
\]
For state perturbations use the norm
\[
\|(v,w)\|_* =\max\{|v|,\tfrac14|w|\}.
\]

Consider either closed ball of radius \(1/20\) around \(P_+\) or \(P_-\) in this norm. Its old parameter and moment have opposite signs. The new uncorrected moment \(m=\beta u+(1-\beta)y\) has the same sign as the old parameter and satisfies
\[
\frac35\le|m|\le\frac45.
\]
Indeed, at the positive phase \(y\in[0.649,0.758]\) and \(u\in[-0.908,-0.485]\), giving \(m\in[0.633,0.758]\) for the stated parameter range; the other phase follows by oddness.

On \(3/5\le |v|\le4/5\), direct differentiation shows
\[
\frac{13}{100}<\psi'(v)<\frac{35}{100}.
\]
The weighted-sup induced norm of the Jacobian of \(H_\beta\) is therefore bounded by the larger of
\[
|1-3(1-\beta)\psi'(m)|+12\beta|\psi'(m)|
\le\frac{614}{1000}+\frac{42}{1000}
=\frac{82}{125}<\frac23
\]
and
\[
\frac14(1-\beta)+\beta\le\frac{26}{100}<\frac23.
\]
Each ball is convex and its map is Lipschitz there with contraction factor \(2/3\), **relative to the opposite cycle phase**.

The actual corrected update at time \(t\ge2\) differs in its first coordinate by at most
\[
3\left|\psi\left(\frac{m}{1-\beta^t}\right)-\psi(m)\right|
\le\frac{3|m|\beta^t}{1-\beta^t}
\le3\beta^t.
\]
Here \(|\psi'|\le1\) globally, \(|m|\le4/5\), and \(\beta^t\le10^{-4}\).

At the source step \(u_0=0\), correction is exact: \(u_1=(1-\beta)y_0\), so
\[
y_1=y_0-3\psi(y_0).
\]
For \(|y_0-a_0|\le1/100\), the derivative of \(v-3\psi(v)\) has absolute value less than \(1/2\) on the containing interval \([0.69,0.72]\). In particular
\[
|y_1+a_0|\le\frac1{200}.
\]
Combining this with the preceding rational amplitude intervals yields
\[
\|(y_1,u_1)-P_-\|_*<\frac{15}{1000}.
\]
(For the moment component, use \(|(1-\beta)y_0-q a_\beta|<0.033\), which is multiplied by \(1/4\) in the norm.)

Let \(e_t\) be the norm distance from \((y_t,u_t)\) to \(P_-\) for odd \(t\) and to \(P_+\) for even \(t\). The last estimate starts the induction inside the cycle neighborhood. As long as \(e_{t-1}\le1/20\), contraction and the bias-correction remainder give
\[
e_t\le\frac23e_{t-1}+3\beta^t,
\qquad t\ge2.
\]
The right side is at most \(\frac23\frac1{20}+3\cdot10^{-4}<1/20\), so the induction is valid for all time. Summing the recurrence gives
\[
\begin{aligned}
e_t
&\le\left(\frac23\right)^{t-1}
\left[e_1+\frac{3\beta^2}{\frac23-\beta}\right]\\
&<\left(\frac23\right)^{t-1}
\left[\frac{15}{1000}+\frac{3(10^{-2})^2}{\frac23-10^{-2}}\right]\\
&<\frac2{125}\left(\frac23\right)^{t-1}.
\end{aligned}
\]
This proves the asserted geometric approach of the **actual, bias-corrected** recurrence to the alternating orbit. Since \(a_\beta>0\), the objective limit is \(\rho a_\beta^2/(2h)\), giving the stated positive expression.

## Verification

`verify.py` requires only the Python standard library. It recomputes the dimensionless update from the scalar Sherman--Morrison identity, tests the exact rational Jury equalities over a grid of moment decays and cycle amplitudes, checks the rational inequalities used in the contraction proof, and replays the actual source-initialized recurrence for multiple strictly positive momenta and source parameters. All universal statements are proved above; finite numerical trajectories are corroboration, not a substitute for the argument.

Run from the package directory with `python verify.py` and expect `verification passed`.

## Relationship to prior work

Sen and coauthors introduce SOFIM's bias-corrected first moment, regularized rank-one Fisher matrix, and Sherman--Morrison inverse update. Their full Algorithm 1 and convex-convergence discussion do not identify a nonminimizing periodic attractor or the exact window \(2<cq<4\). The paper refers to a local approximate-Newton guarantee from Ye, Luo, and Zhang; that theorem requires a Hessian approximation satisfying quantitative spectral comparison, and is not a global guarantee for arbitrary learning rate or a Fisher matrix assembled from moment products.

Bock and Weiss prove nonconvergent periodic orbits for Adam on scalar strongly convex quadratics, including bias-corrected dynamics. That related phenomenon is prior. However, their Adam state includes a separate exponentially accumulated squared-gradient moment and a distinct normalized update, whereas SOFIM uses the **square of the bias-corrected first moment itself** in a regularized rank-one inverse. The Adam results neither contain the SOFIM map nor imply its explicit Fisher-to-momentum thresholds, its closed two-state Jury identities, or this source-initialized quantitative attraction basin.

General fixed-step overshoot and stability phenomena for gradient descent are also prior; the finding is the exact nonlinear attracting-phase diagram and persistent nonzero error for the specific regularized-Fisher momentum recurrence. Searches using SOFIM, Fisher normalization, quadratic stability, periodic orbits, and rank-one moment preconditioning did not identify an implication-equivalent published result. Absence of indexed results alone does not certify novelty.

## Limitations

This is a deterministic scalar-quadratic result for constant steps and positive Fisher regularization; it is not a statement about the stochastic training regime in which SOFIM was evaluated. For general momentum the full bias-corrected system is nonautonomous, so the sharp \(2<cq<4\) criterion applies to the **limiting autonomous sign-symmetric cycle**. The explicit actual-trajectory guarantee is proved only for \(c=3\), \(0\le\beta\le1/100\) and the displayed source interval, not for every attracting-cycle parameter choice. The result neither classifies nonsymmetric cycles nor higher periods, nor claims anything about decaying learning-rate schedules.

## References

1. Mrinmay Sen, A. K. Qin, Gayathri C, Raghu Kishore N, Yen-Wei Chen, and Balasubramanian Raman, “SOFIM: Stochastic Optimization Using Regularized Fisher Information Matrix,” arXiv:2403.02833, first public version 2024-03-05, revised 2024-05-01. Algorithm 1 and Sections III–IV.
2. Sebastian Bock and Martin Georg Weiss, “Non-Convergence and Limit Cycles in the Adam Optimizer,” arXiv:2210.02070v1, 2022-10-05. Algorithm 1, Sections 2–3, Theorem 2.
3. Haishan Ye, Luo Luo, and Zhihua Zhang, “Approximate Newton Methods and Their Local Convergence,” Proceedings of the 34th International Conference on Machine Learning, PMLR 70:3931–3939, 2017. Theorems 3–4 and approximation assumptions.
