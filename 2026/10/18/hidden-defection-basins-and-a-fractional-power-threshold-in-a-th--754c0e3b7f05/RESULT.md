# Hidden defection basins and a fractional-power threshold in a three-actor governance replicator

## Finding

Consider the three-population binary evolutionary game specified below, with \(0<\rho<1\) and \(0<\varepsilon<\min\{3/4,1-\rho\}\). On the invariant symmetric subspace \(y=z=w\), every initial government share \(x_0\in(0,1)\) has **exactly one** critical partner share \(h_\varepsilon(x_0)\in(0,1)\). Initial values \(w_0<h_\varepsilon(x_0)\) converge to \((1,0,0)\), initial values \(w_0>h_\varepsilon(x_0)\) converge to \((1,1,1)\), and equality converges to the saddle \((1,\rho,\rho)\). The threshold obeys strict pointwise barriers

\[
\rho<h_\varepsilon(x)<\rho+\varepsilon(1-x),\qquad 0<x<1,
\]

is real analytic and strictly decreasing, and has exact endpoint limits \(h_\varepsilon(0+)=\rho+\varepsilon\) and \(h_\varepsilon(1-)=\rho\). Its right-end slope is

\[
h_\varepsilon'(1-)=-\frac{\rho(1-\rho)\varepsilon}{1+\varepsilon(1-\rho)+\rho(1-\rho)}.
\]

At the low-regulation endpoint the graph has a fractional-power cusp. Writing \(s=\rho+\varepsilon\),

\[
\kappa=\frac{s(1-s)}{1+\varepsilon(1-s)}\in(0,1),
\]

there exists \(C_{\rho,\varepsilon}\in(0,\infty)\) such that

\[
\lim_{x\downarrow0}\frac{s-h_\varepsilon(x)}{x^{\kappa}}=C_{\rho,\varepsilon}.
\]

For each fixed \(x\in(0,1)\), its weak-asymmetry response has the exact positive integral

\[
h_\varepsilon(x)=\rho+\varepsilon\rho(1-\rho)\int_0^\infty e^{-\rho(1-\rho)t}\frac{1-x}{1-x+xe^t}\,dt+O_x(\varepsilon^2),\qquad\varepsilon\downarrow0.
\]

In the **full three-dimensional model**, the open box \(0<y,z<\rho\) lies in the basin of \((1,0,0)\), while \(\rho+\varepsilon<y,z<1\) lies in the basin of \((1,1,1)\), for every \(0<x<1\). Thus the uniform-volume measures of these basins are at least \(\rho^2\) and \((1-\rho-\varepsilon)^2\), respectively. With \(\rho=1/20\) and \(\varepsilon=1/100\), all nine equal-coordinate starting points \((p,p,p)\), \(p\in\{1/10,2/10,\ldots,9/10\}\), converge to full cooperation, while the defection basin has strictly positive volume, at least \(1/400\). This is a theorem about an admissible **different parameter setting** of the source model, not a reanalysis of the source's own numerical parameter set.

## Assumptions and scope

The deterministic flow on \([0,1]^3\) is

\[
\begin{aligned}
\dot x&=x(1-x)[1+\varepsilon(1-y)],\\
\dot y&=y(1-y)[z-\rho-\varepsilon(1-x)],\\
\dot z&=z(1-z)[y-\rho-\varepsilon(1-x)].
\end{aligned}
\tag{1}
\]

Every quantified interior starting point means \((x,y,z)\in(0,1)^3\); the boundaries are invariant and are not subject to the same strict basins. The subspace \(y=z\) is invariant by uniqueness. On it, with common coordinate \(w\), equation (1) becomes

\[
\dot x=x(1-x)[1+\varepsilon(1-w)],\qquad
\dot w=w(1-w)[w-\rho-\varepsilon(1-x)].
\tag{2}
\]

Equation (1) is realized *without changing the payoff formulas* in Wang's three-actor governance game (source [1], Section 3.3) by

\[
\begin{gathered}
C_g=1,\quad\theta=1,\quad S=2,\quad F=1,\quad
\lambda_w=\frac14,\quad\lambda_s=\frac14+\varepsilon,\\
\delta=1,\quad B=1,\quad E=\frac12,\quad\alpha=1,\quad
c=\frac34+\rho+\varepsilon,\\
a=\frac12,\quad c_u=\frac12+\rho+\varepsilon,\quad q=1,\quad r=\varepsilon.
\end{gathered}
\tag{3}
\]

In (3), \(\delta\) denotes the source's *subsidy factor*, unrelated to an initial-condition perturbation. The parameters not appearing in the three payoff differences may be set to any source-admissible positive values. The constraints above imply positive costs and \(0<\lambda_w<\lambda_s<1\).

## Proof

**1. Invariance and monotone regulation.** Every vector field component in (1) has its appropriate boundary factors, so the cube is forward invariant. For interior solutions,

\[
\dot x\ge x(1-x)>0.
\]

Comparison with the unit-rate logistic equation gives \(x(t)\to1\). The diagonal plane \(y=z\) is invariant because the second and third right-hand sides coincide whenever \(y=z\).

**2. The separating stable curve.** On (2), \((1,\rho)\) is a hyperbolic saddle. In coordinates \(u=1-x\), \(v=w-\rho\), the linearization has eigenvalues \(-L_1\), \(a_0\), where

\[
L_1=1+\varepsilon(1-\rho),\qquad a_0=\rho(1-\rho)>0.
\]

The stable eigentangent is \(v=(a_0\varepsilon/(a_0+L_1))u\). Its interior stable branch therefore begins at \(x<1\), \(w>\rho\), below the moving nullcline \(T(x)=\rho+\varepsilon(1-x)\). Because \(\dot T=-\varepsilon\dot x<0\), every contact with \(w=T(x)\) has \(d(w-T)/dt=-\dot T>0\), so a forward crossing can only be from below to above. Since the stable branch is below \(T\) near its forward endpoint, it remains below \(T\) throughout its backward extension. It also remains above \(\rho\): if \(w\le\rho\) at some finite time, then \(\dot w<0\) as long as \(w\in(0,\rho]\), preventing convergence from above to \(\rho\). Thus \(\rho<w<T(x)\) on the entire branch.

On this branch \(\dot w<0\) and \(\dot x>0\), so it is a strictly decreasing graph \(w=h_\varepsilon(x)\). Its backward orbit stays within the compact strip \(\rho\le w\le\rho+\varepsilon(1-x)<1\), and cannot cease at any finite \(x\in(0,1)\). Therefore the graph extends over all \((0,1)\). Its limit as \(x\downarrow0\) lies in \([\rho,\rho+\varepsilon]\). An alpha-limit point at \(x=0\) must be an equilibrium of the boundary flow \(\dot w=w(1-w)[w-(\rho+\varepsilon)]\). The only such equilibrium in this interval is \(w=s=\rho+\varepsilon\). Its right endpoint is the saddle \(\rho\), proving the stated bounds and endpoints. Smooth analytic dependence and the graph differential equation

\[
h_\varepsilon'(x)=\frac{h_\varepsilon(x)[1-h_\varepsilon(x)]\,[h_\varepsilon(x)-\rho-\varepsilon(1-x)]}{x(1-x)[1+\varepsilon(1-h_\varepsilon(x))]}
\tag{4}
\]

follow from analyticity of (2) and \(\dot x>0\).

**3. Complete classification on the symmetric plane.** For any trajectory on (2), define \(D(t)=w(t)-T(x(t))\). At every zero of \(D\) one has \(\dot D=-\dot T>0\); hence \(D\) crosses zero at most once, always from negative to positive. Consequently \(w(t)\) initially decreases and may subsequently increase, but it can never switch back from increasing to decreasing. Its limit exists. Since \(x(t)\to1\), every interior \(w\)-limit belongs to \(\{0,\rho,1\}\). An orbit converging to \(\rho\) belongs to the saddle's one-dimensional stable manifold and hence has exactly the graph initial condition \(w_0=h_\varepsilon(x_0)\). Scalar comparison in the non-autonomous \(w\)-equation (or uniqueness for the graph equation (4)) maintains the ordering of initial \(w\) relative to this graph. Initial states above the graph therefore converge to \(1\), and those below converge to \(0\). These alternatives exhaust the invariant plane.

**4. Endpoint derivative.** The stable eigentangent in Step 2 gives

\[
\lim_{x\uparrow1}\frac{h_\varepsilon(x)-\rho}{1-x}
=\frac{a_0\varepsilon}{a_0+L_1},
\]

which is the asserted left derivative at \(1\).

**5. Fractional-power cusp at the opposite endpoint.** Put \(v=s-w\) near the source equilibrium \((x,w)=(0,s)\). Its linearization in \((x,v)\) is

\[
\begin{pmatrix}\dot x\\\dot v\end{pmatrix}
=\begin{pmatrix}L&0\\-b\varepsilon&b\end{pmatrix}
\begin{pmatrix}x\\v\end{pmatrix}+O((x+|v|)^2),
\qquad L=1+\varepsilon(1-s),\quad b=s(1-s).
\tag{5}
\]

Here \(L>b>0\) (indeed \(b\le1/4<L\)). The fast eigendirection at eigenvalue \(L\) satisfies \(v/x=-b\varepsilon/(L-b)<0\). By the standard planar hyperbolic-node asymptotics, an orbit approaching this source in reverse time either lies on the unique fast-unstable curve or has a nonzero slow-mode coefficient: \(v(t)\sim B e^{bt}\), \(x(t)\sim A e^{Lt}\) as \(t\to-\infty\), with \(A>0\). On the threshold orbit, the strict barrier \(w<T(x)=s-\varepsilon x\) gives \(v=s-w>\varepsilon x>0\), excluding the fast curve (whose tangent has negative \(v/x\)). Therefore \(B>0\), and eliminating \(t\) yields

\[
v\sim BA^{-b/L}x^{b/L},
\]

with strictly positive finite constant. The exponent \(\kappa=b/L\) is below one, so the threshold cannot have a finite left derivative at zero. The slow-mode assertion may also be obtained by variation of constants in (5): the nonlinear remainders are quadratically small and integrable along backward exponential orbits; the unique zero-slow-amplitude branch has the fast, negative-slope tangent.

**6. Weak-asymmetry response.** At \(\varepsilon=0\), the threshold is the constant \(w=\rho\) and the regulatory coordinate has logistic trajectory

\[
X_x(t)=\frac{xe^t}{1-x+xe^t}.
\]

For each fixed \(x\in(0,1)\), parameter-smooth stable-manifold dependence gives \(h_\varepsilon(x)=\rho+\varepsilon U(x)+O_x(\varepsilon^2)\). Linearizing the \(w\)-equation along this unperturbed threshold yields

\[
\dot U=a_0[U-(1-X_x(t))].
\]

Boundedness at future infinity selects the unique initial value

\[
U(x)=a_0\int_0^\infty e^{-a_0t}(1-X_x(t))\,dt,
\]

which is the displayed integral. Its integrand is strictly positive for all \(t\ge0\), proving that increasing the asymmetry from zero shifts the required cooperative initial share upward.

**7. Basins in the full cube.** If initially \(0<y,z<\rho\), the two corresponding growth brackets in (1) remain strictly negative, so \(y,z\) decrease; their limits cannot be positive because then the growth brackets remain bounded away from zero, hence both tend to zero. If instead \(\rho+\varepsilon<y,z<1\), then both brackets remain strictly positive because \(x\in(0,1)\), so both coordinates increase to one. In either case \(x\to1\) by Step 1. The initial-condition boxes have Lebesgue volumes \(\rho^2\) and \((1-\rho-\varepsilon)^2\) within the unit cube, respectively. For the rational witness \((\rho,\varepsilon)=(1/20,1/100)\), the protective box begins at \(3/50\) and contains each of the nine equal-coordinate points \(p=1/10,\ldots,9/10\), while the defection box has volume \((1/20)^2=1/400\).

## Verification

Run the standalone standard-library checker with `python3 verify.py`. It verifies exact rational parameter-to-payoff substitution, the node exponents and endpoint slope, the two forward-invariant basin boxes, finite sampled trajectories, and numerical agreement between the stable-manifold shooting approximation and the weak-asymmetry integral. A passed numerical check is **not** a proof of global convergence or the fractional-power limit: those conclusions follow from Steps 1–7.

## Relationship to prior work

Wang [1] supplies exactly the three-actor payoff differences used in (1), and reports that nine symmetric starting states reach cooperation for one *different*, fixed numerical incentive regime. It explicitly states that its sampled basin is not a continuous-state-space global-basin theorem. The present result proves a continuous separator, local-to-global basin classification on an invariant symmetric slice, and its singular endpoint law in a separate admissible parameter family. The nine-state observation in the theorem illustrates a finite-grid blind spot and **does not overturn the source's stated results**.

Fu and coauthors [2] analyze basin stability, a saddle separator, and critical disturbances in a different three-actor emergency-governance model. Their identified separatrix mechanism and numerical basin emphasis are prior context; their reported model/payoffs do not specialize to (1), nor do their inspected results furnish the graph bounds, fractional-power asymptotics, or first-order formula above. Classical replicator theory and hyperbolic invariant-manifold theory [3–5] already provide the general methods; this theorem does not claim originality for these tools or for the generic existence of saddle separatrices.

## Limitations

The exact global classification is proved **only on the invariant surface \(y=z\)**. In three dimensions only two explicit basin subsets and their volume lower bounds are certified; their complete geometry and exact volumes are not computed. The finite nine-point demonstration uses a different parameter choice from the numerical experiment in [1]. The limit \(\varepsilon\downarrow0\) is pointwise for fixed \(x\in(0,1)\), not uniform as \(x\downarrow0\); indeed the cusp is singular in that endpoint regime. The theorem concerns deterministic population shares, not stochastic learning convergence, finite population sampling, real-world transport, or optimal policy design. No claim of literature-complete novelty is made.

## References

1. Y. Wang, *Evolutionary Stability Does Not Guarantee Learning Accessibility: A Multi-Agent Reinforcement Learning Perspective on Cooperation Emergence* (first posted 2026-09-23), arXiv:2609.27664, especially Sections 3.3–3.4, 7.5 and Appendix A/C. https://arxiv.org/abs/2609.27664
2. Y. Fu et al., *Evolutionary Game Analysis and Capability Reconstruction of Coal Mine Disaster Emergency Governance Oriented Toward Collaborative Resilience*, Systems 14 (2026), 1142, doi:10.3390/systems14091142. https://doi.org/10.3390/systems14091142
3. P. D. Taylor and L. B. Jonker, *Evolutionarily stable strategies and game dynamics*, Mathematical Biosciences 40 (1978), 145–156.
4. J. Hofbauer and K. Sigmund, *Evolutionary Games and Population Dynamics*, Cambridge University Press, 1998.
5. W. H. Sandholm, *Population Games and Evolutionary Dynamics*, MIT Press, 2010.
