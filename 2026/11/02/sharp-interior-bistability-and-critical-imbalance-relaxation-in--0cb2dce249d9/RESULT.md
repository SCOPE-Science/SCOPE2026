# Sharp interior bistability and critical imbalance relaxation in quadratic cross-competition

## Finding
For the two-species deterministic system
\[
\dot x=x(1-x-a y^2),\qquad \dot y=y(1-y-a x^2),
\]
with \(0<a<1\) and strictly positive initial abundances, there is a sharp transition at \(a_c=3/4\). For \(0<a\le 3/4\), every interior solution converges to the single interior equilibrium \((r,r)\), where \(r=2/(1+\sqrt{1+4a})\). For \(3/4<a<1\), there are exactly two attracting asymmetric coexistence equilibria,
\[
E_\pm=\left(\frac{1/2\pm\sqrt{a-3/4}}{a},\frac{1/2\mp\sqrt{a-3/4}}{a}\right),
\]
separated by the stable manifold of the symmetric saddle \((r,r)\). The entire positive-quadrant basin boundary is simply \(x=y\): initial \(x>y\) selects \(E_+\), initial \(x<y\) selects \(E_-\), and initial equality selects \((r,r)\). The two axial monoculture equilibria are invadable throughout this bistable interval because invasion growth is \(1-a>0\).

At \(a=3/4\), every trajectory with \(x(0)\ne y(0)\) has the exact critical laws
\[
\lim_{t\to\infty}t(x(t)-y(t))^2=\frac{16}{3},\qquad
\lim_{t\to\infty}t\left(\frac{x(t)+y(t)}2-\frac23\right)=-\frac12.
\]
For initial \(x=y\), convergence takes place within the diagonal and is exponential. These statements are one theorem for the canonical quadratic cross-density competitive family.

## Assumptions and scope
The time variable is in normalized growth-rate units; \(a\) is the nonnegative quadratic inhibition coefficient and is restricted here to \(0<a<1\). All initial abundances lie in \((0,\infty)^2\). A 'coexistence equilibrium' means an equilibrium with both coordinates strictly positive. At the boundary the equilibria are \((0,0)\), \((1,0)\) and \((0,1)\); the theorem's global-basin conclusions refer exclusively to strictly positive initial data. The model is continuous-time deterministic, not an individual-based stochastic process. The non-additive cross-density term describes an effect quadratic in the competitor's abundance; no separate third species is assumed.

## Proof
**1. Positivity, boundedness and persistence.** Positive initial coordinates remain positive for finite times because each derivative is that coordinate times a continuous per-capita rate. Each obeys \(\dot x\le x(1-x)\), respectively \(\dot y\le y(1-y)\), so trajectories are global and bounded and \(\limsup_{t\to\infty}\max\{x(t),y(t)\}\le1\). Choose \(\varepsilon>0\) with \(a(1+\varepsilon)^2<1\). Eventually \(x,y\le1+\varepsilon\); hence each per-capita rate is at least \(1-a(1+\varepsilon)^2-x\), respectively \(1-a(1+\varepsilon)^2-y\). Scalar logistic comparison gives a strictly positive uniform lower bound on both coordinates eventually. Thus every positive orbit has a compact omega limit set lying strictly inside the quadrant.

**2. All equilibria.** The unique diagonal interior equilibrium solves \(r+a r^2=1\), hence \(r=2/(1+\sqrt{1+4a})\). Subtracting the two stationary per-capita relations yields
\[
(y-x)[1-a(x+y)]=0.
\]
For an off-diagonal positive equilibrium this forces \(x+y=1/a\). Substituting into the sum of stationary per-capita equations gives \(xy=(1-a)/a^2\). The two distinct positive roots therefore exist if and only if \(3/4<a<1\), and their coordinates are precisely \(E_\pm\). At equality \(a=3/4\), they coalesce with \((2/3,2/3)\); there is no distinct off-diagonal equilibrium.

**3. Stability and separatrix.** At any positive equilibrium, the Jacobian is the symmetric matrix
\[
J=\begin{pmatrix}-x&-2axy\\-2axy&-y\end{pmatrix}.
\]
At \((r,r)\), the symmetric and antisymmetric eigenvalues are \(-r-2ar^2<0\) and \(-r+2ar^2\), respectively. The second crosses zero exactly at \(a=3/4\). For \(E_\pm\), \(\operatorname{tr}J=-1/a<0\) and \(\det J=(1-a)(4a-3)/a^2>0\), so both are hyperbolic sinks. When \(3/4<a<1\), the diagonal equilibrium is a hyperbolic saddle whose stable eigendirection is the invariant diagonal. Since the diagonal scalar equation has a globally attracting positive equilibrium and uniqueness prevents off-diagonal trajectories from intersecting the diagonal, the full positive stable manifold of this saddle is exactly the diagonal. The sign of \(x-y\) is invariant, as is seen directly from the imbalance equation below.

**4. Global convergence.** The Dulac multiplier \(B(x,y)=1/(xy)\) on the simply connected positive quadrant gives
\[
\frac{\partial}{\partial x}(B\dot x)+\frac{\partial}{\partial y}(B\dot y)=-\frac1x-\frac1y<0.
\]
Thus no positive periodic orbit or homoclinic cycle is possible. The compact-interior omega limit sets from Step 1, the finite equilibrium list, and planar Poincare--Bendixson theory force convergence to an equilibrium: the only possible nontrivial cycle of connecting orbits for \(3/4<a<1\) would have to involve the sole interior saddle, and the sign-definite Dulac divergence prohibits a return loop; the other equilibria are sinks. For \(a<3/4\) the sole interior equilibrium is a sink, and at \(a=3/4\) the local center calculation in Step 5 establishes its local attraction. With global convergence proved, the diagonal invariant sign and the stable manifold in Step 3 identify every basin stated above. At each monoculture \((1,0)\) or \((0,1)\), the missing-species linear growth eigenvalue is \(1-a\), proving mutual invasibility for \(0<a<1\).

**5. Critical algebraic rates.** Put \(s=(x+y)/2\) and \(d=(x-y)/2\). The exact equations are
\[
\dot s=s-s^2-a s^3+(as-1)d^2,\qquad
\dot d=d(1-2s+a s^2-a d^2).
\]
At \(a=3/4\), the equilibrium is \((s,d)=(2/3,0)\) and the linear eigenvalues are \(-4/3,0\). An invariant, reflection-even center manifold has
\[
s=\frac23-\frac38d^2+O(d^4).
\]
Solving its invariance equation through quadratic order gives coefficient \(-3/8\). Substitution into the exact imbalance equation gives
\[
\dot d=-\frac38d^3+O(d^5).
\]
This cubic is attracting on both nonzero sides. Standard local center-manifold tracking along the exponentially stable direction shows that every interior trajectory converging to this equilibrium with \(d(0)\ne0\) obeys these center asymptotics, with the exponentially decaying tracking error smaller than every inverse power used here. Integrating \(\frac{d}{dt}(d^{-2})=3/4+o(1)\) yields \(t d^2\to4/3\). Therefore \(t(x-y)^2\to16/3\) and \(t(s-2/3)\to(-3/8)(4/3)=-1/2\). On \(d=0\), the remaining scalar equation has derivative \(-4/3\) at its equilibrium, giving exponential convergence. This also supplies the local attraction used in Step 4.

## Verification
The included `verify.py` is standalone algebraic verification requiring Python and SymPy. It checks the exact mean/imbalance system, equilibrium factorization, asymmetric stationary coordinates, full Jacobian determinant and trace, a rational bistable witness, and center-manifold cubic coefficient and limits. Running `python verify.py` returns a final `PASS` message. It does not claim to computationally certify the nonlocal convergence theorem or replace the planar proof.

For example, at \(a=13/16\) the two stable positive equilibria are \((12/13,4/13)\) and \((4/13,12/13)\). Their Jacobian traces equal \(-16/13\), determinants equal \(12/169\), and both monoculture invasion eigenvalues equal \(3/16>0\). At the threshold, a representative numerical integration from \((0.9,0.25)\) through time \(40000\) gave \(t(x-y)^2\approx5.3351284\) and \(t(s-2/3)\approx-0.5001968\); those illustrations are not proofs of the limiting statements.

## Relationship to prior work
Cui et al. (2024, original arXiv release 2024-05-28) study a broad higher-order Lotka--Volterra model; their pure-competition results give structural sufficient conditions for uniqueness/global attraction and discuss multistability in larger competition systems. Those sufficient conditions do not supply the current zero-self-quadratic canonical family's two asymmetric attracting positive equilibria, exact sharp phase transition, global diagonal basin partition, or critical algebraic rates. This result stays within a two-species specialization of their polynomial interaction framework and does not claim originality for that framework.

Vet et al. (2018) provide an extended two-species microbial Lotka--Volterra model with both positive linear mutualism and negative quadratic cross-density interaction. Their supplementary discussion explicitly illustrates two stable positive equilibria in a broader parabolic-nullcline model. **Existence of two stable interior equilibria in nonlinear two-species systems is therefore prior knowledge, not a new standalone claim.** The present result adds an exact canonical *pure-competition* one-parameter classification, complete basins and a proved transition relaxation exponent with amplitude, which their reported bifurcation diagrams and sufficient conditions do not imply. Letten--Stouffer (2019) motivates non-additive phenomenological density terms but does not provide these numerical boundaries or critical limits. Taylor--O'Dwyer (2025) study multiple stable states in principally pairwise niche competition, often with different surviving species subsets, rather than the present two alternative fully positive states.

## Limitations
The model uses exchange symmetry, normalized linear self-limitation and a single quadratic cross-density coefficient. The theorem does not assert robustness to arbitrary asymmetric parameter perturbations, stochastic fluctuations, time delays, seasonal forcing or spatial dispersal. The critical limits are restricted to unequal positive initial conditions; the diagonal is exceptional. The analysis does not establish novelty relative to every unindexed ecological-dynamics treatise or preprint; an exact equivalent result in older dynamical-systems literature is possible. No independent mathematical audit or empirical validation has been performed.

## References
1. S. Cui, Q. Zhao, G. Zhang, H. Jardon-Kojakhmetov and M. Cao, *On the analysis of a higher-order Lotka-Volterra model: an application of S-tensors and the polynomial complementarity problem*, original arXiv release 2024-05-28, arXiv:2405.18333, https://arxiv.org/html/2405.18333v2 .
2. S. Vet et al., *Bistability in a system of two species interacting through mutualism as well as competition: Chemostat vs. Lotka-Volterra equations*, PLOS ONE **13** (2018), e0197462, doi:10.1371/journal.pone.0197462, https://pmc.ncbi.nlm.nih.gov/articles/PMC5991418/ .
3. A. D. Letten and D. B. Stouffer, *The mechanistic basis for higher-order interactions and non-additivity in competitive communities*, Ecology Letters **22** (2019), 423--436, doi:10.1111/ele.13211.
4. W. Taylor and J. O'Dwyer, *On the structure of multiple stable equilibria in competitive ecological systems*, Theoretical Ecology **18** (2025), doi:10.1007/s12080-025-00627-6.
