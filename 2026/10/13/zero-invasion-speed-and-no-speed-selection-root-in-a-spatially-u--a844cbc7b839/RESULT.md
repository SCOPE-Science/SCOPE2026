# Zero invasion speed and no speed-selection root in a spatially uncoupled COVID-19 model

## Finding

Alanazi's age-structured COVID-19 model (2.1) is written for \(x\in\mathbb R^n\) as
\[
\partial_t S(x,t)=-\eta S(x,t)Q(x,t),
\]
\[
\partial_t Q(x,t)=(1-\gamma)\int_0^\infty \ell(a)I(x,a,t)\,da-qQ(x,t),
\]
\[
\partial_t I(x,a,t)+\partial_a I(x,a,t)=-\ell(a)I(x,a,t),
\qquad I(x,0,t)=\eta S(x,t)Q(x,t).
\]
All right-hand sides use the same spatial location \(x\). Neither movement of the population nor spatially nonlocal transmission occurs. Therefore infection cannot expand its spatial support.

The same absence of spatial coupling forces an exact obstruction to the paper's purported positive spreading speeds. In the constant-susceptible-background setting used for its equation (3.7), define
\[
L(a)=\exp\left(-\int_0^a\ell(s)\,ds\right),
\qquad f(a)=\ell(a)L(a)=-L'(a),
\]
and
\[
F(u)=\frac{\eta(1-\gamma)S_0}{q+u}
\int_0^\infty e^{-ua}f(a)\,da.
\]
Then the paper's Laplace transform is exactly
\[
\mathcal L(c,\lambda)=F(c\lambda).
\]
For every admissible exit distribution with positive total exit mass,
\[
F'(u)<0\quad(u>0),\qquad F(u)\to0\quad(u\to\infty).
\]
Consequently the speed defined in the paper's equation (3.13) satisfies
\[
\boxed{c^*=0}
\]
for every admissible parameter choice, including locally supercritical cases with \(F(0)>1\). Its positive-speed stationarity equations (3.9),
\[
\mathcal L(c,\lambda)=1,
\qquad \partial_\lambda\mathcal L(c,\lambda)=0,
\]
have **no solution with \(c>0\) and \(\lambda>0\)**. Thus the positive speeds tabulated later in the paper cannot be derived from its displayed model and transform.

A simple exact example makes the contradiction explicit. For
\[
q=S_0=1,\qquad \eta=4,\qquad \gamma=0,\qquad\ell(a)=1,
\]
one has
\[
L(a)=e^{-a},\qquad
\mathcal L(c,\lambda)=\frac4{(1+c\lambda)^2},\qquad
F(0)=4.
\]
For every \(c>0\), the choice \(\lambda=2/c\) gives
\[
\mathcal L(c,2/c)=\frac49<1,
\]
while
\[
\partial_\lambda\mathcal L(c,\lambda)
=-\frac{8c}{(1+c\lambda)^3}<0.
\]
The level-one transform relation holds at \(c\lambda=1\), but is never stationary in \(\lambda\) at positive \(c\). That scalar value is a temporal exponential-growth parameter, not a spatial propagation speed.

## Assumptions and scope

Assume \(\eta,q>0\), \(0\le\gamma<1\), a continuous nonnegative latent-exit hazard \(\ell\) with \(f=\ell L\not\equiv0\), and nonnegative initial profiles for which the local classical or mild age-structured solution is unique. For the transform statement, take constant \(S_0>0\), as the source does in Section 3. Because \(L(0)=1\) and \(L\) is nonincreasing,
\[
0<\int_0^\infty f(a)\,da\le1.
\]

For the support conclusion, the initial infectious class \(Q_0\) and the entire initial latent-age profile \(I_0(\cdot,a)\) must vanish outside a common compact set \(K\). The susceptible profile may be positive outside \(K\); it stays constant there. This is a statement about **propagation of new spatial support**. It is not the assertion that a contour of an everywhere-positive initial infection must remain fixed.

The mathematical speed defined by (3.13) can be zero even if the local outbreak grows initially at every seeded location. The local quantity \(F(0)\) does not give any spatial transport mechanism.

## Proof

**Spatial support.** Fix a point \(x\) outside the initially infected set. The equations for \(S(x,\cdot)\), \(Q(x,\cdot)\), and \(I(x,\cdot,\cdot)\) have no dependence on any other spatial point. The initial data at this \(x\) satisfy
\[
Q(x,0)=0,\qquad I(x,a,0)=0\quad(a\ge0).
\]
The identically zero pair \((Q,I)=(0,0)\), together with \(S(x,t)=S_0(x)\), solves the equations and the age boundary condition at that location. Uniqueness of the local age-structured initial-value problem implies that this is the only solution there. Since the argument holds at every \(x\notin K\),
\[
\operatorname{supp}_x Q(\cdot,t)\subseteq K,
\qquad \operatorname{supp}_x I(\cdot,a,t)\subseteq K
\]
for all \(t,a\ge0\). A compact outbreak therefore cannot invade an initially infection-free location at any positive speed.

**Transform and speed.** By the source's equation (3.7), and setting \(u=c\lambda\),
\[
\mathcal L(c,\lambda)
=\frac{\eta(1-\gamma)S_0}{q+u}
\int_0^\infty e^{-ua}f(a)\,da
=:F(u).
\]
Write \(A=\eta(1-\gamma)S_0>0\) and \(M(u)=\int_0^\infty e^{-ua}f(a)\,da\). Since \(0\le M(u)\le1\),
\[
0\le F(u)\le\frac A{q+u}\to0.
\]
For any \(c>0\) select \(u>A\) and \(\lambda=u/c>0\). Then \(\mathcal L(c,\lambda)\le A/(q+u)<1\). Thus every \(c>0\) belongs to the set whose infimum defines \(c^*\) in (3.13), and its infimum over \(c\ge0\) is zero.

For every \(u>0\), differentiation under the integral is valid because \(f\) is integrable and \(ae^{-ua}\) is bounded. One obtains
\[
F'(u)=-A\left[
\frac{\int_0^\infty ae^{-ua}f(a)\,da}{q+u}
+\frac{\int_0^\infty e^{-ua}f(a)\,da}{(q+u)^2}
\right]<0.
\]
Hence for every \(c,\lambda>0\),
\[
\partial_\lambda\mathcal L(c,\lambda)
=cF'(c\lambda)<0.
\]
This rules out the double-root system (3.9) at positive speed. If \(F(0)>1\), strict monotonicity and continuity give one \(u_*>0\) such that \(F(u_*)=1\), but for any \(c>0\) the corresponding \(\lambda=u_*/c\) still has strictly negative derivative. The level-one condition alone selects a **local temporal rate**, never a distinguished positive spatial front speed.

**Exact witness.** With \(\ell\equiv1\), \(q=S_0=1\), \(\eta=4\), and \(\gamma=0\), direct integration yields \(F(u)=4/(1+u)^2\). The arithmetic identities in the Finding establish both a locally supercritical rate \(F(0)=4\) and zero speed under the published infimum.

## Verification

The bundled `verify.py` contains only exact rational arithmetic. It checks \(F(0)=4\), \(F(1)=1\), \(F(2)=4/9\), and, for several positive rational \(c\), chooses \(\lambda=2/c\) and verifies \(\mathcal L(c,\lambda)=4/9<1\) and a strictly negative partial derivative. It also checks that the separated-site right-hand sides do not depend on a neighboring site's state for the constant-hazard reduction.

These finite checks corroborate the explicit witness. The support-invariance and monotonicity arguments above establish the universal statements without relying on finite samples.

## Relationship to prior work

Alanazi's 2024 source explicitly derives the pointwise-in-\(x\) system (2.1), a temporal Volterra equation (3.6) in which there is no spatial convolution, and the transform (3.7). It then imposes stationary speed equations (3.9) and a speed infimum (3.13), and its Table 3 reports positive values of approximately \(0.23\) through \(3.5\) km/week. The present result proves that the speed construction and the claimed spatial invasion cannot both follow from those printed equations.

The 2024 two-dimensional epidemic paper by the same author formulates a genuinely spatial **reaction-diffusion** model: its model equations include diffusion coefficients multiplying spatial derivatives. Its reported traveling fronts therefore belong to a mathematically different, spatially coupled model; they do not repair the absence of coupling in the present source.

The earlier fox-rabies spreading-speed work of Alanazi, Jackiewicz, and Thieme likewise explicitly models diffusing rabid foxes and uses a space-time Laplace transform; this is a different mechanism from the present temporal-only transform. Thieme and Zhao's general integral-equation framework predates the source and may encompass degenerate no-dispersal examples. The generic principle that no new infection can cross uncoupled sites is not claimed as original; the new mathematical observation is its **specific contradiction of the 2024 paper's published positive numerical front speeds and its unsatisfiable speed-selection equations**.

The published simulation in Section 4.2 uses \(Q_0(x)=3e^{-|x|}>0\) at each finite \(x\). Thus moving contour levels in those plots cannot by themselves demonstrate movement of infection into an initially uninfected location.

## Limitations

This finding addresses exactly the equations and transforms as printed, not a hypothetical diffusion- or nonlocal-dispersal extension. It does not invalidate possible dynamics in the separate diffusion-based paper.

The local epidemic can be supercritical, and spatial contours for initial infection with unbounded support may move as different sites amplify or decay independently. The theorem instead excludes **positive propagation of new infection support** and yields zero under the paper's own variational definition.

The earlier general integral-equation theory and rabies article were available for abstract-level comparison but not complete full-text inspection; they may contain a generic no-dispersal limiting observation. No reviewed earlier source identifies this exact source-specific incompatibility.

## References

1. K. M. Alanazi, “The asymptotic spreading speeds of COVID-19 with the effect of delay and quarantine,” *AIMS Mathematics* 9(7) (2024), 19397–19413, DOI: 10.3934/math.2024945 (first online publication June 12, 2024).
2. K. M. Alanazi, “Modeling and Simulating an Epidemic in Two Dimensions with an Application Regarding COVID-19,” *Computation* 12 (2024), 34, DOI: 10.3390/computation12020034.
3. K. M. Alanazi, Z. Jackiewicz, H. R. Thieme, “Spreading speeds of rabies with territorial and diffusing rabid foxes,” *Discrete and Continuous Dynamical Systems B* 25 (2020), 2143–2183, DOI: 10.3934/dcdsb.2019222.
4. H. R. Thieme, X.-Q. Zhao, “Asymptotic speeds of spread and traveling waves for integral equations and delayed reaction-diffusion models,” *Journal of Differential Equations* 195 (2003), 430–470, DOI: 10.1016/S0022-0396(03)00175-X.
