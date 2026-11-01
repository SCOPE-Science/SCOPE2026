# Exact annual extinction-basin ray under unequal overwinter survival in the Aedes seasonal competition model

## Finding
Consider the seasonal Aedes competition model of the references, with the **common density-dependence coefficient** \(\xi_1=\xi_2=\xi\) and **unequal winter survival factors** \(\delta_1\ne\delta_2\). The annual Poincaré map admits an **explicit straight-line global basin separatrix** in the strictly bistable regime. Its slope has a closed formula, including the degenerate equality of favorable-season net growth rates. More precisely, every initial point in the positive quadrant below this ray tends to the Aedes-aegypti-only annual state, every point above tends to the Aedes-albopictus-only annual state, and every point on the ray tends to the unique positive annual saddle. The slope is independent of the shared density parameter \(\xi\), while its dependence on mating competitiveness \(\alpha\) is exactly inverse proportionality.

Set \(g_i=\beta_i-\mu_i\), \(A=g_2+\mu_1\), \(C=g_1-g_2\), \(s=\delta_1/\delta_2\), and \(\Lambda_i=\delta_i e^{g_i\tau}\). Assume
\[
\beta_i>\mu_i>0,\quad \xi>0,\quad\alpha>0,\quad \tau>0,\quad 0<\delta_i\le 1,\quad \delta_1\ne\delta_2,\quad 1<\Lambda_2<\Lambda_1.
\]
The slope \(q_*>0\), namely the equation \(y=q_*x\), is
\[
q_*=\frac{1}{\alpha}\begin{cases}
\displaystyle\frac{C}{A}\frac{H-1}{H-s}, & C\ne0,\quad H=(s e^{C\tau})^{A/\beta_1},\\[8pt]
\displaystyle\frac{1-s^{-1}}{A\tau-\log s},& C=0.
\end{cases}
\]
All denominators in these formulas are nonzero under the stated assumptions. There is precisely one fixed point of the annual map in the positive quadrant; it lies on this ray and is a hyperbolic saddle.

## Assumptions and scope
The favorable-season dynamics of duration \(\tau\) are
\[
\dot x=x\left(\frac{\beta_1 x}{x+\alpha y}-\mu_1-\xi(x+y)\right),\qquad
\dot y=y\left(g_2-\xi(x+y)\right),
\]
for \(x,y>0\). At the subsequent unfavorable-season transition, the populations are replaced by \((\delta_1 x,\delta_2 y)\). The state is sampled immediately before each favorable season. The full annual map is \(P(x,y)=(\delta_1 x(\tau),\delta_2 y(\tau))\). The positive axes are interpreted by continuity and are invariant.

The conclusion applies to **every** strictly positive initial population pair and every parameter tuple satisfying the displayed inequalities. It makes no assertion that the basin boundary is a straight line at intermediate within-season times, nor when \(\xi_1\ne\xi_2\). If \(\delta_1=\delta_2\), the older continuous-favorable-season straight-line result already provides the corresponding ray, and that previously covered parameter case is not claimed as novel.

Define the two positive axial annual states by
\[
R_1=(X_1,0),\quad X_1=\frac{g_1(\Lambda_1-1)}{\xi(e^{g_1\tau}-1)},\qquad
R_2=(0,Y_2),\quad Y_2=\frac{g_2(\Lambda_2-1)}{\xi(e^{g_2\tau}-1)}.
\]
The theorem asserts \(P^n(x_0,y_0)\to R_1\) if \(y_0/x_0<q_*\), \(P^n(x_0,y_0)\to R_2\) if \(y_0/x_0>q_*\), and convergence to the unique positive saddle \(E\) if \(y_0/x_0=q_*\).

## Proof
**1. An exact autonomous ratio equation.** For \(q=y/x>0\), the common logistic competition term cancels:
\[
\frac{d}{dt}\log q=g_2+\mu_1-\frac{\beta_1}{1+\alpha q}
=A-\frac{\beta_1}{1+\alpha q}.
\]
Writing \(w=\alpha q\) gives
\[
\dot w=w\frac{Aw-C}{1+w},\qquad C=\beta_1-A=g_1-g_2.
\]
Let \(\varphi_t(q)\) denote the positive solution at elapsed favorable time \(t\) from ratio \(q\). The annual ratio map is the autonomous scalar function
\[
Q(q)=\frac{\delta_2}{\delta_1}\varphi_\tau(q)=s^{-1}\varphi_\tau(q).
\]
In particular, both the annual ratio map and its positive fixed ratios are independent of the population magnitude and of \(\xi\).

**2. Exactly one unstable annual fixed ratio.** Write \(f(q)=A-\beta_1/(1+\alpha q)\). Because \(f'(q)=\alpha\beta_1/(1+\alpha q)^2>0\), scalar order preservation implies that \(Q(q)/q=s^{-1}\exp(\int_0^\tau f(\varphi_t(q))\,dt)\) is strictly increasing in \(q\). Its endpoint limits are
\[
\lim_{q\downarrow0}\frac{Q(q)}q=\frac{\Lambda_2}{\Lambda_1}<1,
\qquad
\lim_{q\uparrow\infty}\frac{Q(q)}q=\frac{\delta_2}{\delta_1}e^{A\tau}>1.
\]
The last strict inequality follows from \(\delta_2e^{g_2\tau}=\Lambda_2>1\), \(\delta_1\le1\), and \(A=g_2+\mu_1>g_2\). Consequently there is a unique \(q_*>0\) with \(Q(q_*)=q_*\), and strict monotonicity implies \(Q'(q_*)>1\). The sequence \(q_{n+1}=Q(q_n)\) decreases to zero when \(q_0<q_*\), increases without bound when \(q_0>q_*\), and stays constant when \(q_0=q_*\). Indeed, any finite positive limit would have to be the unique fixed ratio, contradicting monotonicity away from it.

**3. Integration and explicit slope.** For \(C\ne0\), separation of the \(w\) equation along any trajectory not stationed at its interior continuous-time equilibrium gives
\[
C\tau=-\log\frac{w(\tau)}{w(0)}
+\frac{\beta_1}{A}\log\left|\frac{Aw(\tau)-C}{Aw(0)-C}\right|.
\]
At an annual fixed ratio \(w(\tau)=s w(0)\), and \(Aw(\tau)-C\) and \(Aw(0)-C\) have the same sign (no trajectory crosses an equilibrium). Hence
\[
\frac{Asw_*-C}{Aw_*-C}=H=(s e^{C\tau})^{A/\beta_1},
\]
so \(w_*=(C/A)(H-1)/(H-s)\). The exceptional case of a continuously stationary ratio would require \(s=1\), excluded here. Under \(1<\Lambda_2<\Lambda_1\), \(H\ne1\); furthermore \(H=s\) would imply \(s=e^{A\tau}\), contrary to \(\delta_2e^{A\tau}>1\ge\delta_1\). Therefore the formula is well-defined and positive by the unique-fixed-ratio argument.

When \(C=0\), integration of \(\dot w=Aw^2/(1+w)\) gives
\[
A\tau=\frac1{w(0)}-\frac1{w(\tau)}+\log\frac{w(\tau)}{w(0)}.
\]
The annual boundary condition yields \(w_*=(1-s^{-1})/(A\tau-\log s)\), with both numerator and denominator positive by \(\Lambda_2<\Lambda_1\) and the upper endpoint ratio condition. This finishes the explicit formula and its critical \(C=0\) case.

**4. Radial evolution on the ray.** At \(q=q_*\), put \(q(t)=\varphi_t(q_*)\). The \(y\) coordinate solves a nonautonomous logistic equation
\[
\dot y=g_2y-\xi(1+1/q(t))y^2.
\]
With
\[
J=\int_0^\tau e^{g_2t}\left(1+\frac1{q(t)}\right)dt>0,
\]
its exact annual restriction to the ray is
\[
y_{n+1}=\frac{\Lambda_2y_n}{1+\xi J y_n}.
\]
Because \(\Lambda_2>1\), this map attracts every \(y_n>0\) to \(Y_*=(\Lambda_2-1)/(\xi J)\). Thus every positive point on the ray tends to \(E=(Y_*/q_*,Y_*)\), the unique positive annual fixed point. In coordinates \((q,y)\), the derivative of the annual map at \(E\) is triangular with eigenvalues \(Q'(q_*)>1\) and \(\Lambda_2^{-1}<1\): \(E\) is a hyperbolic saddle and the whole positive ray is its global stable set.

**5. Global off-ray convergence.** If \(q_n\to0\), the favorable-season ratio \(q_n(t)\) tends uniformly to zero for \(0\le t\le\tau\). The \(x\) component has the exact annual form
\[
x_{n+1}=\frac{a_n x_n}{1+b_nx_n},
\quad a_n=\delta_1e^{\int_0^\tau h_n(t)dt},
\quad b_n=\xi\int_0^\tau e^{\int_0^t h_n(u)du}(1+q_n(t))dt,
\]
where \(h_n(t)=\beta_1/(1+\alpha q_n(t))-\mu_1\). Hence \(a_n\to\Lambda_1>1\) and \(b_n\to\xi(e^{g_1\tau}-1)/g_1\). Reciprocation yields \(1/x_{n+1}=(1/x_n+b_n)/a_n\), an asymptotically contracting affine recurrence, so \(x_n\to X_1\) and \(y_n=q_nx_n\to0\).

If \(q_n\to\infty\), then \(q_n(t)\to\infty\) uniformly on the favorable interval, and the \(y\) component obeys
\[
y_{n+1}=\frac{\Lambda_2y_n}{1+\tilde b_n y_n},\quad
\tilde b_n=\xi\int_0^\tau e^{g_2t}\left(1+\frac1{q_n(t)}\right)dt
\longrightarrow\frac{\xi(e^{g_2\tau}-1)}{g_2}.
\]
The same reciprocal-affine contraction proves \(y_n\to Y_2\) and \(x_n=y_n/q_n\to0\). These alternatives exhaust the positive quadrant and prove all basin claims.

## Verification
The standalone `verify.py` contains a fourth-order Runge–Kutta implementation of the scalar ratio equation and the planar favorable-season flow. It tests three admissible parameter tuples with \(C>0\), \(C=0\), and \(C<0\), respectively. It compares the closed slope to the numerically advanced annual ratio, checks the direction of movement on both sides of the separatrix, checks planar invariance of a point on the ray, and checks the positivity of the axial states. Run `python verify.py` with Python 3; no third-party packages are needed. The recorded output is reproduced in `VERIFICATION.md`. Numerical tests do not establish the universal or infinite-time assertions; those follow from the analytic proof above.

## Relationship to prior work
Zheng, Chang, Guo and Yu (2025), Theorem 2.3(i), already establish a straight stable separator **for the autonomous favorable-season flow** when the density coefficients coincide. That result is not claimed as novel here. Its flow-invariant line generally is **not** preserved when the two species have unequal overwintering survival. Niu, Wang, Xie and Zheng (2026), Theorem 3.1 and Corollary 3.2, prove bistability and existence of an abstract continuous invariant annual basin-separating curve for the switched model. They do not supply the explicit annual ray or a closed threshold slope at unequal winter survival. Its Section 4 also mentions a straight line for the bistability boundary in the **winter-survival parameter plane** \(\delta_1,\delta_2\); that is not a line separating initial population states \(x,y\) and cannot imply the present state-space ray. The new contribution is the exact quantitative solution of the **switched** problem for the natural equal-crowding slice, incorporating unequal winter survival, including the limiting equal-growth case and the complete initial-ratio classification. No claim is made that the standard scalar logistic or ratio transformations themselves are new.

## Limitations
The theorem concerns annual population samples and fixed seasonal parameters with common density dependence. Within-season separation may move in phase space. The hypotheses exclude one-species nonpersistence and threshold equality; the geometry with unequal density-dependence coefficients is not resolved here. A more general theorem on projective skew-product population maps could potentially subsume the exact-ray statement; historical-priority assessment beyond the inspected closest texts remains open. No independent audit has been performed.

## References
1. Lei Niu, Yi Wang, Xizhuang Xie, Bo Zheng, *Bistable Dynamics and Complete Classifications of A Seasonal Competition Model Between Aedes aegypti and Aedes albopictus*, arXiv:2610.29233v1 (first posted October 21, 2026), https://arxiv.org/html/2610.29233v1, especially model (1), Theorem 3.1 and Corollary 3.2.
2. Bo Zheng, Lijie Chang, Hongpeng Guo, Jianshe Yu, *Global Competitive Dynamics of Aedes aegypti and Aedes albopictus with Favorable-unfavorable Seasonal Shifts*, SIAM J. Appl. Math. 85 (2025), 1189–1211, https://doi.org/10.1137/24M1694744, especially Theorem 2.3(i) and Section 3.
