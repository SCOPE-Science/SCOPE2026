# Sharp greed-dependent extinction boundary in an Allee common-pool game

## Finding
Consider the Allee-resource evolutionary game described below. There is a unique critical resource density \(h_w(x)\) for every initial cooperator fraction \(0<x<1\). Initial resources below it become extinct; those above it converge to the positive resource equilibrium after cooperation vanishes; equality converges to the positive saddle equilibrium. The boundary is strictly decreasing in the initial cooperator fraction and strictly increasing with the greed response rate \(w\). It is **not** the straight line joining the two frozen-strategy Allee thresholds. Moreover, the difference between the moving threshold and the frozen threshold admits the explicit, uniform bound

\[
0<h_w(x)-r_-(x)\le \frac{(d-c)w}{4T\lambda_0^2}\left(1-e^{-4T\lambda_0 x/w}\right)<\frac{(d-c)w}{4T\lambda_0^2},
\qquad 0<x<1,
\]

where \(\lambda_0=\sqrt{(1-A)^2-4Ad}/A\). This yields a sharp global basin classification and a quantitative slow-greed approximation throughout the interior of the biological square.

## Assumptions and scope
Let \(0<A<1\), \(0<c<d<(1-A)^2/(4A)\), \(T>0\) and \(0<w\le1\). Consider the smooth autonomous system

\[
\dot R=TR\left[\left(\frac RA-1\right)(1-R)-d+(d-c)x\right],\qquad
\dot x=-wRx(1-x),
\]

with \((R(0),x(0))\in(0,1)^2\). Here \(R\) is resource abundance and \(x\) is the fraction following a less exploitative strategy. Write \(\Delta=d-c\), \(e(x)=d-\Delta x\), and

\[
r_\pm(x)=\frac{1+A\pm\sqrt{(1-A)^2-4Ae(x)}}{2},\qquad
\lambda(x)=\frac{\sqrt{(1-A)^2-4Ae(x)}}{A}.
\]

Both roots are strictly between zero and one, \(r_-(x)<r_+(x)\), \(r_-'(x)=-\Delta/\lambda(x)<0\), and \(\lambda(x)\ge\lambda_0>0\). The invariant biological square is \([0,1]^2\), and the classification concerns strictly interior initial conditions. The original study also treats a physically narrower harvesting range \(c<1<d\).

The unique threshold \(h_w:(0,1)\to(0,1)\) is smooth, extends continuously to \([0,1]\), and satisfies

\[
h_w(0)=r_-(0),\qquad h_w(1)=r_-(1),\qquad r_-(x)<h_w(x)<r_-(0),\qquad h_w'(x)<0.
\]

For each \(0<x_0<1\) and \(0<R_0<1\), the limits of the corresponding forward trajectory are

\[
\begin{cases}
R(t)\to0,&R_0<h_w(x_0),\\
(R(t),x(t))\to(r_-(0),0),&R_0=h_w(x_0),\\
(R(t),x(t))\to(r_+(0),0),&R_0>h_w(x_0).
\end{cases}
\]

In the first case no convergence claim about \(x(t)\to0\) is made (in fact its limit is positive). For \(0<w_1<w_2\le1\), \(h_{w_1}(x)<h_{w_2}(x)\) at every \(x\in(0,1)\). The boundary solves the invariant graph equation

\[
h_w'(x)=-\frac{T}{w}\frac{\big(h_w(x)/A-1\big)(1-h_w(x))-e(x)}{x(1-x)},
\qquad h_w'(0)=-\frac{T\Delta}{w+T\lambda_0}.
\]

## Proof
**1. Geometry and local stable branch.** Put \(g(R,x)=(R/A-1)(1-R)-e(x)=(R-r_-(x))(r_+(x)-R)/A\). The resource boundary \(R=0\) and strategy boundaries \(x=0,1\) are invariant, and at \(R=1\), \(\dot R=-Te(x)<0\); hence the unit square is forward invariant. The equilibrium \(P=(r_-(0),0)\) has linearized eigenvalues \(Tr_-(0)\lambda_0>0\) and \(-wr_-(0)<0\). Its one-dimensional stable manifold has a positive-\(x\) branch tangent to \(h_w'(0)=-T\Delta/(w+T\lambda_0)<0\). Since \(r_-'(0)=-\Delta/\lambda_0\), this branch initially lies strictly above \(r_-(x)\) and below \(r_-(0)\). Because \(x\) strictly decreases along positive trajectories, the branch is a graph of resource density against strategy frequency.

**2. Global continuation of the separator.** On any graph segment, division by \(\dot x=-wRx(1-x)\) yields the displayed graph equation. At the upper barrier \(R=r_-(0)\), one has \(g=\Delta x>0\), so the graph derivative is negative. At the lower moving barrier \(R=r_-(x)\), the graph derivative is zero, while \(r_-'(x)<0\), making \((h_w-r_-)'(x)>0\) at any contact. These two strict barriers preclude either crossing as \(x\) is increased from zero. Standard continuation for the smooth scalar equation on compact subintervals therefore extends the branch to every \(0<x<1\), preserving \(r_-(x)<h_w(x)<r_-(0)\) and \(h_w'(x)<0\). The decreasing bounded graph has a limit as \(x\uparrow1\). If that limit exceeded \(r_-(1)\), the quantity \(g(h_w(x),x)\) would be bounded strictly above zero near one (the other root exceeds \(r_-(0)\)), forcing \(h'_w(x)\le-C/(1-x)\), impossible for a bounded graph. Thus \(h_w(1)=r_-(1)\).

**3. All positive trajectories converge to one of the three limits.** On the open square \(\dot x<0\), so \(x(t)\downarrow x_\infty\ge0\). If \(x_\infty>0\), then the identity \(d\log[x/(1-x)]/dt=-wR\) implies \(\int_0^\infty R(t)\,dt<\infty\). Boundedness of \(\dot R\) and nonnegativity yield \(R(t)\to0\). If \(x_\infty=0\), the resource equation is asymptotically the scalar equation \(\dot R=TRg(R,0)\). For any level \(u\in(0,1)\) outside its three zeros \(\{0,r_-(0),r_+(0)\}\), the resource derivative at \(R=u\) eventually has a fixed nonzero sign. Such a level cannot be crossed indefinitely in both directions. The compact forward orbit therefore has a singleton resource limit, necessarily one of those zeros. Every interior orbit tending to \(P\) lies on the stable manifold, hence on \(h_w\).

The scalar graph equation for trajectories as functions of their strictly decreasing \(x\) gives uniqueness and **strict order preservation** relative to \(h_w\). A trajectory initially below the graph cannot tend to \(r_+(0)>h_w(0)\); it cannot tend to \(P\) without lying on the stable manifold. It must therefore become extinct. An initially above-graph trajectory cannot tend to zero, because then its resource coordinate eventually falls below the positive graph at the same \(x\), contradicting order preservation, and it cannot tend to \(P\). It therefore approaches \((r_+(0),0)\). This proves the exhaustive basin classification.

**4. Strict dependence on greed.** Set \(k=T/w\). The initial slope \(-k\Delta/(1+k\lambda_0)\) is strictly decreasing in \(k\). Hence if \(k_1>k_2\), the \(k_1\)-separator starts below the \(k_2\)-separator. At any first proposed crossing from below, their derivatives differ by \(-(k_1-k_2)g(h,x)/[x(1-x)]<0\), contrary to upward crossing. Therefore \(h_{k_1}(x)<h_{k_2}(x)\) for all \(x>0\), or equivalently \(h_{w_1}(x)<h_{w_2}(x)\) for \(w_1<w_2\).

**5. Uniform slow-greed estimate.** Set \(z(x)=h_w(x)-r_-(x)>0\). Direct differentiation yields

\[
z'=-\frac{T}{w}\frac{z(r_+(x)-h_w(x))}{Ax(1-x)}+\frac\Delta{\lambda(x)}.
\]

Since \(r_+(x)-h_w(x)\ge r_+(0)-r_-(0)=A\lambda_0\), \(\lambda(x)\ge\lambda_0\), and \(x(1-x)\le1/4\), comparison gives \(z'\le-4T\lambda_0 z/w+\Delta/\lambda_0\) with \(z(0)=0\). Integrating the linear comparison proves the stated estimate. The strict final inequality holds at every finite \(x>0\). This establishes uniform convergence to the instantaneous lower Allee root as \(w\downarrow0\).

## Verification
The accompanying `verify_boundary.py` uses only the Python standard library and independently integrates the invariant graph in the logit coordinate \(\log[x/(1-x)]\). It checks barrier bounds, the strict ordering in \(w\), the explicit \(O(w)\) error estimate for 60 seeded parameter tuples, and forward trajectories on both sides of the source parameter threshold. The code supplies finite numerical corroboration, not a proof of the continuum claims.

With \(A=1/10\), \(c=1/2\), \(d=3/2\), \(T=2\), \(w=1\), and \(x=1/2\), it obtains \(h_1(1/2)\approx0.23295910703656\). Linear interpolation between the two frozen-strategy thresholds instead gives \((r_-(0)+r_-(1))/2=(22-\sqrt{21}-\sqrt{61})/40\approx0.24017936572844\). Their exact endpoint derivatives already differ: \(h_1'(0)=-2/(1+2\sqrt{21})\) versus the line's slope \((\sqrt{21}-\sqrt{61})/20\); the discrepancy is therefore structural, not numerical.

## Relationship to prior work
Tu, Menegazzo, D'Odorico and Suweis (arXiv:2405.01271, version publicly available May 2, 2024) present the same cubic Allee resource/replicator coupling and a qualitative phase-plane treatment of the bistable regime. Their boundary is illustrated using straight-line interpolation between frozen-strategy tipping points. The present result characterizes the full nonlinear boundary, proves the complete global basin trichotomy, establishes strict response-rate monotonicity, and gives a uniform explicit slow-greed error bound. These facts are not consequences of linear interpolation.

The closely related resource-game analysis by Tu, Chen, Fan and Yang (arXiv:2401.11269) treats logistic resource replenishment without the Allee cubic and does not imply a two-positive-root threshold. Tilman, Plotkin and Akçay (2020) and Ito and Yamamichi (2024) provide broader evolutionary-game/environmental-feedback classifications but do not supply the equation-specific sharp basin divider or its explicit response-rate error bound. These comparisons concern mathematical implications, not paper titles.

## Limitations
The theorem assumes strictly positive harvest rates below the cubic's maximum, a genuine Allee bistability region, and strictly interior initial conditions. It does not cover parameter coalescence at the fold, stochastic perturbations, seasonality, finite-population noise, spatial diffusion, or parameter variation over time. The boundary is characterized by an ODE rather than elementary closed form; the example uses numerical integration solely as corroboration. Unindexed later specialist literature remains a possible originality risk.

## References
1. Tu, Menegazzo, D'Odorico, Suweis, *The role of the Allee effect in common-pool resource games with environmental feedback*, arXiv:2405.01271 (first public May 2, 2024). https://arxiv.org/abs/2405.01271
2. Tu, Chen, Fan, Yang, *Evolutionary dynamics of common-pool resource systems with feedback*, arXiv:2401.11269 (2024). https://arxiv.org/abs/2401.11269
3. Tilman, Plotkin, Akçay, *Evolutionary games with environmental feedbacks*, Nature Communications (2020). https://doi.org/10.1038/s41467-020-14531-6
4. Ito and Yamamichi, *A complete classification of evolutionary games with environmental feedback*, 2024. https://academic.oup.com/pnasnexus/article/3/10/pgae422/7821427
