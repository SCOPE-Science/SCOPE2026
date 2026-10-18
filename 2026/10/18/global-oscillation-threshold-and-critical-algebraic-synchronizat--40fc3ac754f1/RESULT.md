# Global oscillation threshold and critical algebraic synchronization in a three-gene logistic cycle

## Finding
Consider the three-component signed weighted-sum logistic network
\[
 \dot x_i=\sigma\bigl(4(x_i-x_{i-1})\bigr)-v x_i,
 \qquad i\in\mathbb Z/3\mathbb Z,\qquad
 \sigma(s)=\frac{1}{1+e^{-s}},\qquad v\ge1.
\]
The cyclic indexing convention is \(x_0=x_3\). The interaction consists of self-activation and inhibition from one predecessor at equal magnitude, with zero activation thresholds and equal degradation rates. This is a natural symmetric three-node instance of the signed weighted-sum logistic regulatory class described and compared by Belgacem (2026).

For every real initial state, the system has a global forward solution. Put
\[
 d_i=x_i-x_{i-1},\qquad R(t)=d_1(t)^2+d_2(t)^2+d_3(t)^2.
\]
Its only equilibrium for \(v\ge1\) is \((1/(2v),1/(2v),1/(2v))\). The following sharp trichotomy holds for every nonsynchronous initial state (equivalently, \(R(0)>0\)):

1. If \(v>3/2\), the state converges to that equilibrium. Moreover, for a positive constant depending on the initial state,
\[
 \lim_{t\to\infty}e^{2(v-3/2)t}R(t)=C(x(0),v)\in(0,\infty).
\]
2. If \(v=3/2\), the state converges to the equilibrium with the universal critical law
\[
 \boxed{\lim_{t\to\infty}tR(t)=\tfrac12.}
\]
3. If \(1\le v<3/2\), the distance from the trajectory to some nonconstant periodic orbit tends to zero. In particular, at least one periodic orbit exists, and no nonsynchronous trajectory tends to an equilibrium. This is not a uniqueness or hyperbolicity claim for the periodic orbit.

Every initially synchronous solution remains synchronous and converges exponentially to equilibrium, including below the transverse threshold. Thus the global transition is in the transverse dynamics, and the boundary rate is explicitly algebraic.

## Assumptions and scope
The state variables are real and indexed modulo three, \(v\) is a fixed real parameter with \(v\ge1\), and solutions are classical. The biologically natural nonnegative cube is forward invariant for nonnegative initial states; the conclusions also hold for arbitrary real initial data. The logistic gain is fixed to four, giving unit maximal derivative in each signed regulatory input. No delay, noise, other graph, or unequal parameter is included. Convergence to a periodic orbit refers to distance to its compact trajectory, without claiming a unique asymptotic phase.

## Proof
### Boundedness and the exact transverse planar subsystem
Since \(0<\sigma(s)<1\) and \(v>0\), comparison with \(\dot u=-vu\) and \(\dot u=1-vu\) bounds every coordinate forward for any initial state. The vector field is smooth and globally Lipschitz, so solutions exist for all positive times; \([0,1/v]^3\) is forward invariant.

Write
\[
 \phi(s)=\sigma(4s)-\tfrac12=\tfrac12\tanh(2s).
\]
Then \(\phi\) is smooth, odd, bounded, and \(0<\phi(s)<s\) for \(s>0\); its derivative is \(\phi'(s)=\operatorname{sech}^2(2s)\le1\). Subtract consecutive equations to obtain the autonomous difference system
\[
 \dot d_i=-v d_i+\phi(d_i)-\phi(d_{i-1}),\qquad
 d_1+d_2+d_3=0.\tag{1}
\]
Thus all transverse motion lies on a two-dimensional invariant plane. If \(d\equiv0\), every coordinate obeys \(\dot x=1/2-vx\).

### Uniqueness of equilibrium for \(v\ge1\)
At a difference equilibrium, equation (1) becomes
\[
 v d_i-\phi(d_i)=-\phi(d_{i-1}).\tag{2}
\]
For \(v\ge1\), the function \(s\mapsto vs-\phi(s)\) vanishes only at zero and has the same strict sign as \(s\) elsewhere. If one \(d_i\) vanishes, equation (2) forces every \(d_i\) to vanish. Otherwise, equation (2) requires the signs of every two cyclic neighbors to alternate. This is impossible around an odd cycle of length three. Therefore \(d=0\). At equilibrium the synchronous coordinate must be \(1/(2v)\), proving uniqueness.

### Rearrangement dissipation
Define \(\psi(s)=s-\phi(s)\). Its derivative is \(\psi'(s)=\tanh^2(2s)\), so \(\psi\) is strictly increasing. For any real triple, the rearrangement inequality (strict unless all three entries coincide) implies
\[
 T(d):=\sum_i d_i\psi(d_i)-\sum_i d_i\psi(d_{i-1})\ge0,
\]
with equality on \(\sum_i d_i=0\) only at \(d=0\). Since \(\sum_i d_id_{i-1}=-R/2\) whenever \(\sum d_i=0\), equation (1) yields the *exact* balance
\[
 \boxed{\tfrac12\dot R=(\tfrac32-v)R-T(d).}\tag{3}
\]
This is a strict global Lyapunov law at and above the critical value.

### Supercritical convergence and the exact decay exponent
For \(v>3/2\), put \(\alpha=v-3/2>0\). Equation (3) gives \(0<R(t)\le R(0)e^{-2\alpha t}\) for all nonsynchronous trajectories (uniqueness prohibits their reaching \(R=0\) at finite time). Because \(\psi(s)=O(s^3)\) as \(s\to0\), one has \(0\le T(d)/R=O(R)\) near the origin, and \(\int_0^\infty T(d(t))/R(t)\,dt<\infty\). Integration of
\[
 \frac d{dt}\log\bigl(e^{2\alpha t}R(t)\bigr)=-2T(d(t))/R(t)
\]
proves convergence of \(e^{2\alpha t}R(t)\) to a finite *positive* constant. The mean coordinate \(m=\frac13\sum_i x_i\) obeys \(\dot m=-vm+\frac13\sum_i\sigma(4d_i)\); since \(d\to0\), it follows that \(m\to1/(2v)\) and hence \(x\to(1/(2v),1/(2v),1/(2v))\).

### Critical constant
At \(v=3/2\), (3) gives \(\dot R=-2T(d)<0\) away from synchronization. Boundedness and compactness imply \(R(t)\to0\): any positive limiting value would give a compact positive-distance invariant set on which \(\dot R<0\), impossible. Near zero, the Taylor expansion is
\[
 \psi(s)=\frac43s^3+O(s^5).
\]
For \(d_1=a\), \(d_2=b\), \(d_3=-a-b\), direct polynomial expansion yields the exact identity
\[
 \sum_i\bigl(d_i^4-d_id_{i-1}^3\bigr)
 =3(a^2+ab+b^2)^2=\frac34 R^2.\tag{4}
\]
Combining (4) with \(\psi(s)=\frac43s^3+O(s^5)\), uniformly in direction as \(d\to0\), gives
\[
 T(d)=R^2+O(R^3),\qquad
 \dot R=-2R^2+O(R^3).
\]
For every nonsynchronous trajectory, \(R>0\), so \(\frac d{dt}(1/R)=2+O(R)\to2\). Integration and division by \(t\) prove \(1/(tR(t))\to2\), equivalently \(tR(t)\to1/2\). Convergence of the full state follows from the same stable mean equation.

### Subcritical periodicity
For \(1\le v<3/2\), the planar linearization of (1) at \(d=0\) has the complex-conjugate eigenvalues
\[
 \lambda_\pm=\frac32-v\pm i\frac{\sqrt3}{2}.
\]
Thus zero is a hyperbolic repeller in the difference plane. Equation (1) has bounded forward orbits, because \(\phi\) is bounded. There is no other difference equilibrium by the preceding sign argument. A nonsynchronous planar orbit cannot approach, or have in its omega limit, the hyperbolic source. Its nonempty compact omega-limit set therefore contains no equilibria. The Poincaré–Bendixson theorem implies that the omega limit is a periodic orbit. In particular such periodic orbits exist and the distance to one of them tends to zero.

For the full three-dimensional system, reconstruct the mean coordinate \(m=(x_1+x_2+x_3)/3\) from the differences: it is driven linearly by \(g(d)=\frac13\sum_i\sigma(4d_i)\) and exponentially damped at rate \(v\). For any periodic difference orbit, this scalar forced equation has exactly one periodic response of the same period. The omega limit of the bounded full trajectory projects onto that difference orbit. Every bounded *entire* solution of the scalar driven mean equation above a periodic difference orbit is necessarily its unique periodic solution (variation of constants backwards, using exponential decay forwards). Therefore the full omega limit is contained in the corresponding compact periodic lift, and the distance to that lift tends to zero. The lifted orbit is nonconstant because its differences are nonconstant. This completes the trichotomy.

## Verification
The standalone `verify.py` checks the polynomial identity (4) exactly using integer arithmetic, evaluates strict finite-sample rearrangement inequalities, reproduces the predicted linear eigenvalues, and integrates representative trajectories on both sides of the boundary and at criticality. In the critical test it checks that the observable approaches the proven coefficient \(1/2\). These finite checks are independent diagnostics, not substitutes for the infinite-time argument above. The only analytical ingredients not reducible to finite computation are the rearrangement inequality, the strict Lyapunov/compactness argument, and Poincaré–Bendixson on the difference plane.

## Relationship to prior work
Belgacem, *A Bias-Corrected Weighted Logistic Model for Gene Regulatory Networks* (first public version June 3, 2026, arXiv:2606.04709v1), develops and compares general logistic genetic regulatory laws, explicitly including the signed weighted-sum class of the present system (its §1.1 and §2). Its contraction criterion gives useful sufficient stability regions for related models, and its two-gene example exhibits a Hopf bifurcation, but the inspected text does not give the exact global three-node threshold, the all-initial-condition planar periodicity statement, or the inverse-time critical constant proved here. This result concerns the *uncorrected signed weighted-sum* formulation, not Belgacem's separate bias-corrected formulation; no equivalence between those two formulations is asserted.

A later source, Pokutnyi and Sadyrbaev, *The influence of decay in dynamic models of gene regulatory networks* (arXiv:2610.18261v1, publicly posted October 13, 2026, after the present eligibility anchor), studies the same signed \(3\)-cycle weight matrix at logistic gain four and reports linear eigenvalues and numerical attracting periodic orbits at particular decay rates. Its relevant full-text sections (§2, §3.1 and conclusions) do not supply the global sharp threshold, uniqueness-of-equilibrium argument, or critical inverse-time constant. It is comparative supporting literature, **not** the earlier eligible source used to date this result.

Arcak and Sontag, *A Passivity-Based Stability Criterion for a Class of Interconnected Systems and Applications to Biochemical Reaction Networks* (2007, arXiv:0705.3188), derive nonlinear passivity/secant sufficient stability conditions for cyclic feedback networks and explicitly caution that local stability need not preclude cycles. Their displayed monotone cyclic model has additive scalar input/output components, unlike the mixed state difference within each sigmoid here. Even where a general small-gain theorem could imply a stable subrange, such a sufficient criterion does not entail our sharp oscillatory side or universal critical relaxation amplitude. Poincaré–Bendixson is classical and supplies the final periodic-orbit implication after our model-specific planar reduction and equilibrium exclusion.

Searches of publicly indexed mathematical records, close network variants, and the accessible private claim history yielded no directly covering global trichotomy. As with any literature-limited novelty check, equivalent statements in other network terminology remain a residual risk.

## Limitations
The finding is an exact mathematical result for three identical signed logistic nodes, a fixed logistic slope four, and decay \(v\ge1\). The physical interpretation of a zero-threshold inhibitory edge is not validated experimentally. Oscillatory trajectories converge in distance to a periodic orbit but its uniqueness, attraction rate, waveform and period are not classified. Other choices of weights, thresholds, graph sizes, delays or stochastic perturbations are not covered. The independence of the mathematics is not externally certified and the originality comparison is limited to sources actually inspected.

## References
1. Ismail Belgacem, *A Bias-Corrected Weighted Logistic Model for Gene Regulatory Networks: Functional Equivalence with the Product-of-Logistics and Comparison with Weighted-Sum Formulations*, arXiv:2606.04709v1, first posted 2026-06-03. https://arxiv.org/abs/2606.04709
2. Oleksandr Pokutnyi and Felix Sadyrbaev, *The influence of decay in dynamic models of gene regulatory networks*, arXiv:2610.18261v1, posted 2026-10-13. https://arxiv.org/html/2610.18261v1
3. Murat Arcak and Eduardo D. Sontag, *A Passivity-Based Stability Criterion for a Class of Interconnected Systems and Applications to Biochemical Reaction Networks*, arXiv:0705.3188v1, 2007-05-22. https://arxiv.org/html/0705.3188v1
4. Classical rearrangement inequality and the Poincaré–Bendixson theorem (used in their standard planar forms).
