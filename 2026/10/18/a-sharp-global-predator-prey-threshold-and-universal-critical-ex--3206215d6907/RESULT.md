# A sharp global predator–prey threshold and universal critical extinction law under fear and refuge

## Finding

Consider the fear–refuge population model
\[
\dot u=u\left(\frac{r}{1+kv+\alpha u}-au-bv\right),\qquad
\dot v=v(cbu-m-\eta v).
\]
Write \(u_1>0\) for the unique solution of \(r=au_1(1+\alpha u_1)\), put \(h=cb\), and define the predator invasion excess \(\Theta=hu_1-m\). **For every strictly positive initial condition**, the following is a complete classification.

When \(\Theta\le0\), the solution converges to the prey-only state \((u_1,0)\). When \(\Theta>0\), there is exactly one positive equilibrium \((u_*,v_*)\), and every strictly positive solution converges to it. In either regime the system has no nonconstant periodic orbit in the positive quadrant and no positive-equilibrium Hopf bifurcation. These statements remain true at zero predator self-competition \(\eta=0\) and require no auxiliary coefficient restriction for boundedness.

At the boundary \(\Theta=0\), the predator disappears **algebraically, not exponentially**. With
\[
D_1=1+\alpha u_1,\qquad
\sigma=a+\frac{r\alpha}{D_1^2},\qquad
\kappa=b+\frac{rk}{D_1^2},\qquad
q=\eta+\frac{h\kappa}{\sigma}>0,
\]
every strictly positive trajectory satisfies the two exact limits
\[
\lim_{t\to\infty}t\,v(t)=\frac1q,\qquad
\lim_{t\to\infty}t\bigl(u(t)-u_1\bigr)=-\frac{\kappa}{\sigma q}.
\]
Thus the critical decay coefficient remains positive when \(\eta=0\): prey feedback alone regularizes predator extinction.

## Assumptions and scope

The variables \(u(t)>0\) and \(v(t)>0\) are prey and predator densities. Assume \(r,a,b,c,m>0\) and \(k,\alpha,\eta\ge0\). The original model uses \(b=\beta(1-\delta)\), with \(\beta>0\), \(0\le\delta<1\), and \(0<c\le1\), and ordinarily assumes \(k,\alpha,\eta>0\). Allowing zero values of the last three parameters is a mathematical boundary extension. Results hold for all \(t\ge0\) and all finite strictly positive initial data. They assert deterministic ODE dynamics, not ecological predictions under delay, stochasticity, diffusion, or alternative functional responses.

The prey-only equilibrium is \(u_1=r/a\) when \(\alpha=0\) and otherwise
\[
u_1=\frac{\sqrt{1+4\alpha r/a}-1}{2\alpha}.
\]
The threshold is equivalently \(r\gtrless (am/h)(1+\alpha m/h)\) for the two strict regimes.

## Proof

**1. Positivity, global continuation and an unconditional absorbing bound.** Each component is its positive initial value times the exponential of its integrated per-capita growth. Put \(H=u+v/c\). The predation transfers cancel exactly:
\[
\dot H=\frac{ru}{1+kv+\alpha u}-au^2-\frac{m}{c}v-\frac{\eta}{c}v^2.
\]
In particular,
\[
\dot H+mH\le (r+m)u-au^2\le\frac{(r+m)^2}{4a}.
\]
Hence \(H(t)\le H(0)e^{-mt}+\frac{(r+m)^2}{4am}(1-e^{-mt})\). This proves positive forward global existence and boundedness even when \(\eta=0\), without assuming any quadratic-form positivity involving \(b,c,a,\eta\).

**2. Exact equilibrium diagram.** Define the per-capita prey function \(f(u,v)=r/(1+kv+\alpha u)-au-bv\). Its partial derivatives are
\[
f_u=-a-\frac{r\alpha}{(1+kv+\alpha u)^2}<0,\qquad
f_v=-b-\frac{rk}{(1+kv+\alpha u)^2}<0.
\]
The unique prey-axis equilibrium is \((u_1,0)\), while the origin is a saddle. For \(\eta>0\) an interior equilibrium lies on \(v=(hu-m)/\eta\), requiring \(u>m/h\). Along this line, \(f\) decreases strictly from \(f(m/h,0)\) to a negative value, so an intersection exists uniquely if and only if \(u_1>m/h\), equivalently \(\Theta>0\). For \(\eta=0\), the predator nullcline instead fixes \(u=m/h\) and the strictly decreasing function \(v\mapsto f(m/h,v)\) has one positive root under exactly the same condition. No other interior equilibria exist.

**3. Local attraction and a strict no-cycle certificate.** At an interior equilibrium, the Jacobian entries are
\[
J_{11}=u_*f_u<0,\quad J_{12}=u_*f_v<0,\quad
J_{21}=hv_*>0,\quad J_{22}=-\eta v_*\le0.
\]
Thus \(\operatorname{tr}J<0\) and \(\det J>0\) for every admissible parameter value, including \(\eta=0\). In particular, the positive equilibrium is a sink and cannot experience a Hopf crossing. On the open positive quadrant use the Dulac factor \(B(u,v)=1/(uv)\). Direct differentiation gives
\[
\frac{\partial(B\dot u)}{\partial u}
+\frac{\partial(B\dot v)}{\partial v}
=-\frac{a+r\alpha/(1+kv+\alpha u)^2}{v}-\frac{\eta}{u}<0.
\]
The Bendixson–Dulac theorem excludes every nonconstant positive periodic orbit. The strict sign persists even if \(\eta=0\) or \(\alpha=0\), since \(a>0\).

**4. Global convergence.** All positive trajectories have nonempty compact omega-limits by Step 1. On the predator-free axis the scalar prey equation approaches \(u_1\) from every positive state. On the prey-free axis predator density decreases to zero. The origin has an inward-prey unstable direction and its local stable manifold is the prey-free axis. At \((u_1,0)\), the axial eigenvalue is \(-u_1\sigma<0\) and the transverse eigenvalue is \(\Theta\). If \(\Theta>0\), its local stable manifold is exactly the predator-free axis; no positive trajectory converges to that boundary saddle. If \(\Theta<0\), this is a sink and no interior equilibrium exists. If \(\Theta=0\), Step 5 shows that it attracts from the interior locally. There can be no boundary heteroclinic polygon: the only boundary connections move from the origin toward the prey-only equilibrium along the prey axis or toward the origin along the predator axis; neither can close a directed cycle. The planar Poincaré–Bendixson alternatives, together with Step 3 and the finite equilibrium list, now imply that every strictly positive trajectory approaches an equilibrium, and the boundary stable-manifold facts select exactly the equilibrium stated in the finding. Equivalently, the only possible omega-limit graph without a periodic orbit would need a closed heteroclinic circuit, already excluded by the boundary geometry and the fact that every interior equilibrium is a sink.

**5. The sharp nonhyperbolic boundary.** At \(\Theta=0\), write \(x=u-u_1\), \(y=v\). A Taylor expansion yields
\[
\dot x=-u_1\sigma x-u_1\kappa y+O((|x|+|y|)^2),\qquad
\dot y=hxy-\eta y^2.
\]
The one-dimensional center manifold through the prey-only equilibrium has
\[
x=-\frac\kappa\sigma y+O(y^2),\qquad
\dot y=-q y^2+O(y^3),\qquad
q=\eta+\frac{h\kappa}{\sigma}>0.
\]
This proves its local attraction on the positive side and establishes the leading center decay \(y(t)\sim1/(qt)\). Since the only local strong-stable manifold is the invariant axis \(y=0\), every positive orbit converging to the equilibrium is asymptotic to its positive center manifold, giving \(x(t)\sim-\kappa/(\sigma qt)\). Step 4 supplies global entry into this local regime; the limits hold for **every** positive initial state.

## Verification

Run `python verify.py` in the directory containing the attached verifier; it requires Python, `sympy`, and `scipy`. The verifier checks the general balance identity and Dulac derivative symbolically, then checks 648 exact-rational critical-rate and balance configurations. It integrates sample parameter sets across extinction, coexistence, and critical boundaries, including \(\eta=0\); finite integrations illustrate the conclusions but are not proofs for all time.

For the exact parameters \(r=2\), \(a=b=c=k=\alpha=1\), the prey-only density is \(u_1=1\). With \(m=1\) and \(\eta=1\), the critical coefficients are \(\sigma=\kappa=3/2\), \(q=2\), and both critical limits have magnitude \(1/2\). With \(\eta=0\), they instead have magnitude \(1\). With \(m=1/2\), the positive equilibria are exactly \((3/4,1/4)\) for \(\eta=1\) and \((1/2,1/2)\) for \(\eta=0\). With \(m=3/2\), all interior trajectories approach \((1,0)\) when \(\eta=1\).

## Relationship to prior work

Ramraj and Poornima (2026), DOI `10.3389/frai.2026.1868693`, introduce exactly the stated ecological equations, prove positivity, establish a boundedness theorem under an auxiliary coefficient inequality, characterize local equilibria, and numerically observe apparent global convergence. Their Section 7.2 identifies a global analytical theorem and the weak-predator-interference limit as open tasks. Here the contribution is an all-parameter global convergence and no-cycle classification, unconditional boundedness, and explicit universal critical extinction coefficients, including zero predator self-interference. The source's local stability and extinction threshold are previously established and are not independently claimed as new.

He and Li (2022), DOI `10.1080/17513758.2022.2091800`, prove global stability for related fear and interference predator–prey systems, but their birth response and interference terms are not the joint denominator \(1+kv+\alpha u\) with quadratic predator mortality used here; their theorem is not a statement covering this full parameterized model. Wang, Zanette and Zou (2016), DOI `10.1007/s00285-016-0989-1`, study another fear model that can have Hopf bifurcations. Hou and Baigent (2015), DOI `10.3934/cpaa.2015.14.1205`, develop general Kolmogorov global-stability criteria; their cited inward-positive-origin hypothesis does not apply to the present predator equation \(\dot v/v=-m\) at the origin. General Bendixson–Dulac and planar-limit-set methods remain established mathematical tools, not new concepts claimed here.

## Limitations

This is a deterministic continuous-time two-species theorem and uses bilinear predation and a monotonically decreasing fear–crowding birth term. It does not extend to Holling-II saturating consumption, age structure, time delay, spatial diffusion, noise, generalist predators, or discontinuous refuge laws. The stated algebraic constants apply only at exact invasion equality, not off-critical exponential convergence. The results do not show empirical calibration or that oscillations are impossible in other fear-based predator–prey models. The originality comparison is literature-based, not a guarantee against unindexed or unpublished proofs; no independent scientific audit is claimed.

## References

1. G. Ramraj and T. Poornima, “Fear-driven predator–prey dynamics with prey refuge: analytical framework and physics-informed neural network approach,” *Frontiers in Artificial Intelligence* 9 (2026), article 1868693, first online 10 August 2026. DOI `10.3389/frai.2026.1868693`; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13500610/ .
2. M. He and Z. Li, “Stability of a fear effect predator–prey model with mutual interference or group defense,” *Journal of Biological Dynamics* 16 (2022), 480–498. DOI `10.1080/17513758.2022.2091800`.
3. X. Wang, L. Zanette and X. Zou, “Modelling the fear effect in predator–prey interactions,” *Journal of Mathematical Biology* 73 (2016), 1179–1204. DOI `10.1007/s00285-016-0989-1`.
4. Z. Hou and S. Baigent, “Global stability and repulsion in autonomous Kolmogorov systems,” *Communications on Pure and Applied Analysis* 14 (2015), 1205–1238. DOI `10.3934/cpaa.2015.14.1205`; lawful open full text: https://repository.londonmet.ac.uk/753/1/GlobStabKolv.pdf .
