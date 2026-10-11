# Global attraction and two-term critical relaxation at the multiple-exposure disease-free degeneracy

## Finding
Consider
\[
\dot S=A-dS-(\beta_1+\beta_0 I)SI,\qquad
\dot I=(\beta_1+\beta_0 I)SI-\rho I,
\]
with \(A,d,\rho>0\), \(\rho>d\), and nonnegative initial data. At
\[
\beta_1=\frac{d\rho}{A},\qquad \beta_0=\frac{d\rho^2}{A^2},
\]
the only equilibrium in the nonnegative quadrant is \(E_0=(A/d,0)\), and it is globally asymptotically stable.

For every interior solution, meaning \(I(0)>0\),
\[
I(t)=\frac{A}{\sqrt{2}\,\rho^{3/2}}t^{-1/2}+
\frac{A(d-\rho)}{2d\rho^2}t^{-1}+O(t^{-3/2}\log t),
\]
and
\[
S(t)-\frac{A}{d}=-\frac{A}{d\sqrt{2\rho}}t^{-1/2}+
\frac{A(\rho-d)}{2d^2\rho}t^{-1}+O(t^{-3/2}\log t).
\]
The local center equation in the physical infection coordinate is
\[
\dot I=-\frac{\rho^3}{A^2}I^3+
\frac{\rho^4(d-\rho)}{A^3d}I^4+O(I^5).
\]
The cubic coefficient was already displayed in the motivating article. The new content is the global threshold theorem, the next center coefficient, and the resulting two-term critical relaxation law.

## Assumptions and scope
The statement concerns the planar \((S,I)\) subsystem printed in the source. The removed class is dynamically downstream and is not needed here. Parameters satisfy \(A,d,\rho>0\) and \(\rho>d\), as in the epidemiological interpretation \(\rho=d+\mu+\delta\) with positive removal or disease mortality. No smallness assumption is imposed on the initial population.

The result is only for the exact codimension-two disease-free parameter above. It does not classify nearby Bogdanov–Takens dynamics at positive endemic equilibria.

## Proof
Write \(x=S-A/d\) and \(y=I\). At the stated parameter,
\[
\dot x=-dx-\rho y-\frac{d\rho}{A}xy-\frac{\rho^2}{A}y^2-
\frac{d\rho^2}{A^2}xy^2,
\]
\[
\dot y=\frac{d\rho}{A}xy+\frac{\rho^2}{A}y^2+
\frac{d\rho^2}{A^2}xy^2.
\]
The linear eigenvalues are \(-d\) and \(0\). Parameterize a local center manifold by the physical infected coordinate,
\[
x=h(y)=a_1y+a_2y^2+a_3y^3+O(y^4).
\]
Coefficient matching in \(h'(y)\dot y=\dot x\) gives
\[
a_1=-\frac{\rho}{d},\qquad a_2=0,\qquad
 a_3=\frac{\rho^3(d-\rho)}{A^2d^2}.
\]
Substitution into the \(y\)-equation yields
\[
\dot y=-c y^3+q y^4+O(y^5),\qquad
c=\frac{\rho^3}{A^2},\qquad
q=\frac{\rho^4(d-\rho)}{A^3d}.
\]
Since \(c>0\), the origin is locally asymptotically stable; the strong stable manifold is exactly the invariant boundary \(I=0\).

Global attraction follows from planarity. Positivity is forward invariant, and for \(N=S+I\),
\[
\dot N=A-dS-\rho I\le A-dN,
\]
so every nonnegative solution is bounded. At the critical parameter the endemic-equilibrium equation reduces to a positive constant times \(I^2=0\), hence \(E_0\) is the only nonnegative equilibrium. A periodic orbit lying in the open quadrant would have Poincaré index one and therefore enclose an equilibrium, impossible because there is no interior equilibrium. Thus an interior bounded omega-limit set cannot avoid equilibria: by the Poincaré–Bendixson theorem it would otherwise be periodic. The only compact invariant subset of the boundary is \(E_0\); once an orbit enters a local attracting neighborhood of \(E_0\), it converges to it. Boundary solutions with \(I=0\) satisfy \(\dot S=A-dS\). Hence all nonnegative solutions converge to \(E_0\).

For an interior trajectory, the strong-stable manifold cannot contain it, so the center asymptotics apply. With \(W=y^{-2}\),
\[
\dot W=2c-2qy+O(y^2).
\]
First \(y(t)\sim(2ct)^{-1/2}\). Integrating the displayed equation then gives
\[
W(t)=2ct-\frac{4q}{\sqrt{2c}}\sqrt t+O(\log t).
\]
Inverting this expansion gives
\[
y(t)=\frac{1}{\sqrt{2c}}t^{-1/2}+
\frac{q}{2c^2}t^{-1}+O(t^{-3/2}\log t),
\]
which is the stated formula for \(I\). Finally \(x=h(y)+O(e^{-\gamma t})\) for some local tracking rate \(\gamma>0\), and \(a_2=0\), so the two displayed terms for \(S-A/d\) follow.

## Verification
The accompanying `verify.py` reconstructs the original vector field with exact symbolic arithmetic, derives the center-manifold coefficients through cubic order, checks the cubic and quartic reduced coefficients, verifies the critical equilibrium polynomial, and verifies the asymptotic constants algebraically. It also checks the normalized system used in the boundedness and equilibrium arguments. Running the script from the package directory prints `VERIFY_OK`.

The proof of global attraction is analytic; no finite numerical experiment is used as evidence for the infinite-time statement.

## Relationship to prior work
Li and Ma introduce this multiple-exposure contact rate and analyze equilibria and local bifurcations. Their Theorem 2 treats the disease-free threshold \(\beta_1=d\rho/A\); at \(\beta_0=d\rho^2/A^2\), their proof explicitly obtains the cubic reduction \(\dot y=-(\rho^3/A^2)y^3+O(y^4)\), while the theorem calls the disease-free equilibrium a saddle-node and assigns codimension two. Their numerical phase portraits also label an open parameter region with a globally stable disease-free equilibrium, but no analytic global theorem at the degenerate boundary or critical decay law is supplied.

Earlier nonlinear-incidence epidemic literature establishes generic forward/backward transcritical criteria, global-stability results under other incidence hypotheses, and rich Hopf/Bogdanov–Takens dynamics. Those statements do not imply the model-specific quartic center coefficient or the exact two-term boundary relaxation above. In particular, the 2007 two-compartment nonlinear-incidence study gives backward, Hopf, and Bogdanov–Takens analysis at statement level, while the 2016 Lyapunov paper proves global disease-free stability for a different class of nonlinear-incidence assumptions.

## Limitations
The global theorem uses the exact critical equality; it is not a robustness statement for nearby parameters. The asymptotic expansion applies to interior solutions \(I(0)>0\); boundary solutions decay exponentially in \(S-A/d\) and have \(I\equiv0\). The result does not bound transient outbreak size, classify the nearby endemic bifurcation set, or rule on higher-order dynamics away from the disease-free degeneracy. Search cannot exclude an unindexed derivation of the same boundary theorem.

## References
1. J. Li and M. Ma, “Bogdanov–Takens Bifurcation of Kermack–McKendrick Model with Nonlinear Contact Rates Caused by Multiple Exposures,” *Symmetry* 16 (2024), 688. DOI: 10.3390/sym16060688.
2. J. Li, Y. Zhou, J. Wu, and Z. Ma, “Complex dynamics of a simple epidemic model with a nonlinear incidence,” *Discrete and Continuous Dynamical Systems B* 8 (2007), 161–173. DOI: 10.3934/dcdsb.2007.8.161.
3. P. van den Driessche and J. Watmough, “A simple SIS epidemic model with a backward bifurcation,” *Journal of Mathematical Biology* 40 (2000), 525–540. DOI: 10.1007/s002850000032.
4. J. Li, Y. Yang, Y. Xiao, and S. Liu, “A class of Lyapunov functions and the global stability of some epidemic models with nonlinear incidence,” *Journal of Applied Analysis & Computation* 6 (2016), 38–46. DOI: 10.11948/2016004.
