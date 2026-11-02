# Global basins and logarithmically corrected fold relaxation in a bimolecular switch

## Finding
For the explicit, strictly positive-inflow, equal-removal mass-action switch below, all positive initial states converge to an equilibrium. Its parameter-dependent attractor diagram is globally complete, and at the nondegenerate positive fold the concentration has a universal inverse-time asymptotic with a **nonzero logarithmic correction**. This last term distinguishes trajectories from the leading saddle-node scaling.

In the bistable range, the positive quadrant splits into two attracting basins with the stable manifold of the intermediate saddle as their exact common boundary. The saddle-node has an open one-sided basin, and all generic trajectories in that basin obey the rate law stated below.

## Assumptions and scope
For \(a>0\), study the autonomous ordinary differential equation on the positive quadrant
\[
\dot x=a-x+20y-\frac{50}{9}x^2-10xy,\qquad
\dot y=\frac1{90}-11y+\frac{50}{9}x^2.
\]
It is the species order of the three-reaction switch \(Y\to2X\), \(2X\to X+Y\), \(X+Y\to Y\), with rates \(10,50/9,10\), positive inflows \(a,1/90\), and equal linear removals of rate one.

Write \(c=50/9\), \(b=1/90\), and define
\[
\phi(x)=\frac{b+cx^2}{11},\quad
P_a(x)=-\frac{500}{9}x^3+50x^2-\frac{100}{9}x+11a+\frac29,
\quad s=\frac{9-\sqrt{21}}{30},\quad a_+=\frac1{99}+\frac{7\sqrt{21}}{891}.
\]
The identity \(11\dot x|_{y=\phi(x)}=P_a(x)\) holds. The equilibrium counts, the fold location, and its local nondegeneracy were already established in the motivating paper; they are not claimed here as new.

Set \(y_s=\phi(s)\). For an exact algebraic expression for the new critical-time constants, define
\[
p=\frac{2cs}{11},\quad F=20-10s,\quad D=1+\frac{Fp}{11},\quad
A=\frac{-c-10p+Fc/11}{D},\quad
q=\frac{c-pA}{11},\quad
B=-\frac{q(10+2FA/11)}D,\quad L=-\frac BA.
\]
These satisfy \(A=1.8507800878575\ldots>0\), \(B=-6.2318442921878\ldots<0\), and \(L=3.3671446613637\ldots>0\). Their defining radical formulas, rather than the decimal approximations, are exact.

For \(0<a<a_+\), every positive solution approaches one of the three equilibria. The smallest and largest equilibria are sinks; the middle one is a hyperbolic saddle. Its global stable set in the positive quadrant is exactly the boundary of the two sink basins. In the positively invariant strip \(0<x<2\), the saddle's stable set is a strictly decreasing graph over its projection on the \(x\)-axis (where defined). For \(a>a_+\), the unique positive equilibrium attracts all positive states.

At \(a=a_+\), each positive solution converges either to \((s,y_s)\) or to the unique larger hyperbolic sink. The fold has an open one-sided attracting region. If a solution converges to the fold but does not lie on its one-dimensional strong stable manifold, then it approaches from \(x<s\), and there exists a finite trajectory-dependent constant \(C\) such that
\[
\boxed{\frac1{s-x(t)}=At+L\log t+C+o(1)\qquad (t\to+\infty).}
\]
The exceptional strong-stable trajectories converge exponentially and are not asserted to obey this algebraic law. No statement concerns nonpositive initial concentrations, the parameter boundary \(a=0\), or perturbed reaction rates.

## Proof
**1. Positivity, bounds, and compactness.** On \(x=0\), \(\dot x=a+20y>0\), and on \(y=0\), \(\dot y=b+cx^2>0\). Thus the nonnegative quadrant is strictly inward-pointing on its axes. If \(x\ge2\), then \(20-10x\le0\) and
\[
\dot x=a-x-cx^2+(20-10x)y\le a-x-cx^2.
\]
A large constant upper bound for \(x\), depending only on \(a,x(0)\), follows. The linear equation \(\dot y=b+cx^2-11y\) then bounds \(y\). A large inward rectangle with both lower faces strictly positive is absorbing: at \(x=\varepsilon\) the drift is positive after choosing \(\varepsilon\) small against the bounded \(y\); at \(y=\varepsilon\), \(\dot y\ge b-11\varepsilon>0\). Hence all positive trajectories are forward complete, eventually lie in a compact subset of the *open* quadrant, and have compact omega limit sets there.

**2. Exclusion of non-equilibrium recurrence and global convergence.** The divergence is strictly negative throughout the quadrant:
\[
\partial_x\dot x+\partial_y\dot y=-12-\frac{100}{9}x-10y<0.
\]
Bendixson's criterion eliminates periodic orbits. A heteroclinic or homoclinic polygon would be a closed union of flow trajectories and equilibria bounding positive area, also impossible by the divergence theorem (zero boundary flux contradicts the strictly negative area integral). The Poincaré–Bendixson alternatives for a bounded planar forward orbit with finitely many equilibria therefore reduce to a singleton equilibrium. This holds at the nonhyperbolic fold as well. The root and Jacobian signs of \(P_a\), as established in the source paper, now imply the claimed global convergence regimes.

**3. Basin boundary and monotone geometry.** In \(0<a<a_+\), the two sinks have open basins. All remaining positive points converge to the only saddle, hence form its stable manifold; any boundary point of either sink basin belongs to that stable manifold, and both branches of the saddle's unstable manifold enter opposite sink basins. Indeed, all three equilibria are in \(0<x<2\); on \(x=2\) the first velocity is \(a-2-200/9<0\), giving a forward-invariant strip. There the cross derivatives \(\partial_y\dot x=20-10x>0\) and \(\partial_x\dot y=100x/9>0\) define a strongly cooperative flow. At the saddle, the unstable eigenvector has two positive entries and the stable eigenvector opposite-signed entries. Standard planar strong-order preservation (or the variational cone argument) makes its stable separatrix strictly order-antichain: two distinct points of it cannot be coordinatewise comparable, for eventual convergence to the saddle would contradict the positive unstable eigendirection. Consequently it is a decreasing graph in the strip. Its stable branches partition the two sink basins; points with \(x\ge2\) join the strip in finite forward time and inherit this assignment.

**4. Exact center-manifold coefficients.** At \(a=a_+\), the fold Jacobian has one zero eigenvalue and one strictly negative eigenvalue, with center eigenvector \((1,p)\). Use \(u=x-s\) as the center coordinate and write the local center manifold as
\[
y=y_s+pu+qu^2+ru^3+O(u^4),\qquad \dot u=Au^2+Bu^3+O(u^4).
\]
Invariance of \(y\) at second and third order gives \(q=(c-pA)/11\) and \(r=-(pB+2qA)/11\). The first differential equation gives \(A=-c-10p+Fq\) and \(B=-10q+Fr\). Solving these four identities yields the exact formulas given above, with \(A>0\), \(B<0\), and \(L=-B/A>0\). The signs follow directly by exact real-radical comparison and are independently checked in the accompanying symbolic script. The fold therefore has a locally open attracting parabolic sector on \(u<0\), while the \(u>0\) center side repels. Its transverse stable foliation decays exponentially. Any convergent trajectory outside the strong stable curve tracks this center graph exponentially and eventually has \(u<0\).

**5. The logarithmic asymptotic and the finite constant.** With \(w=-1/u=1/(s-x)\) for such a trajectory, the center expansion and stable-fiber tracking give
\[
\dot w=A-\frac B{w}+O(w^{-2})+O(e^{-\kappa t}w^2)
\]
for some \(\kappa>0\); the exponential perturbation is integrable, and \(w\sim At\). First integration yields \(w=At+O(\log t)\). Reinsert this into \(-B/w\): the difference from \(-B/(At)\) is \(O(\log t/t^2)\), integrable at infinity. Hence \(w-At+(B/A)\log t\) converges to a finite constant \(C\), proving the exact asserted rate and its nonzero logarithmic term.

## Verification
The accompanying `verification/check.py` uses exact SymPy arithmetic to check \(P_{a_+}(s)=P'_{a_+}(s)=0\), the fold curvature, eigenvalue signs, and the center-manifold coefficient identities through cubic order. It also checks exact inequalities for \(A,B,L\) and three rational bistable equilibrium roots at \(a=4/99\). The script is executable after installing SymPy. These finite algebraic checks support rather than replace the planar global argument and asymptotic integration.

## Relationship to prior work
Bo Peng, *Bistability with equal and independent removal in small bimolecular networks*, arXiv:2610.32739v1 (2026), §4, already gives the same network, positive equilibrium cubic, three-equilibrium region, saddle and sink classifications, and exact fold value. None of those is newly asserted here. The added conclusion is the *complete fate of every positive trajectory*, its global basin separator, the open fold basin, and the explicit first logarithmic correction to algebraic fold relaxation. Earlier work by Banaji–Boros–Hofbauer and Póta shows that planar bimolecular reaction kinetics cannot have isolated limit cycles; exclusion of cycles by itself is likewise not the novel claim. The present proof combines a direct dissipativity and divergence argument with an exact higher-order reduction at this particular fold.

## Limitations
The result is deterministic, planar, and for the given fixed reaction coefficients. The claimed strict separatrix monotonicity is confined to the invariant strip \(0<x<2\), not to arbitrary points outside it. The critical asymptotic excludes the strong stable manifold and depends on the choice of concentration coordinate \(x\) and original time normalization. The classification does not extend automatically to nonautonomous inputs, stochastic kinetics, extra species, or other network topologies. The originality comparison is based on the named accessible sources and semantic mathematical-record searches, not on proof of absolute historical priority. No independent audit has been performed.

## References
1. Bo Peng, *Bistability with equal and independent removal in small bimolecular networks*, arXiv:2610.32739v1, submitted 23 October 2026. https://arxiv.org/html/2610.32739v1
2. M. Banaji, B. Boros, and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, Nonlinear Dynamics 112 (2024), 21425–21448. https://doi.org/10.1007/s11071-024-10068-1
3. M. Banaji, B. Boros, and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, Studies in Applied Mathematics 152 (2024), 249–278. https://doi.org/10.1111/sapm.12639
