# Exact stationary feedback calibration and speed defects in the Thomas cyclic flow
## Finding
Consider the Thomas cyclic sine system
\[
\dot x=\sin y-bx,\qquad
\dot y=\sin z-by,\qquad
\dot z=\sin x-bz,
\]
with
\[
0<b<1.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact cyclic conditional laws
\[
\mathbb E_\mu[\sin y\mid x]=bx,
\]
\[
\mathbb E_\mu[\sin z\mid y]=by,
\]
and
\[
\mathbb E_\mu[\sin x\mid z]=bz.
\]

Since conditional expectations of sine take values in \([-1,1]\), the invariant support is confined to the sharp coordinatewise stationary box
\[
\operatorname{supp}\mu\subseteq
\left[-\frac1b,\frac1b\right]^3.
\]

The conditional residuals are exactly the coordinate speeds, and therefore
\[
\mathbb E_\mu[\dot x^2]
=
\operatorname{Var}_\mu(\sin y)-b^2\operatorname{Var}_\mu(x),
\]
\[
\mathbb E_\mu[\dot y^2]
=
\operatorname{Var}_\mu(\sin z)-b^2\operatorname{Var}_\mu(y),
\]
and
\[
\mathbb E_\mu[\dot z^2]
=
\operatorname{Var}_\mu(\sin x)-b^2\operatorname{Var}_\mu(z).
\]

Each of these three nonnegative defects vanishes exactly when \(\mu\) is supported on the equilibrium set. Consequently every compact invariant measure that is not equilibrium-supported satisfies the three strict inequalities
\[
b^2\operatorname{Var}_\mu(x)<\operatorname{Var}_\mu(\sin y),
\]
\[
b^2\operatorname{Var}_\mu(y)<\operatorname{Var}_\mu(\sin z),
\]
and
\[
b^2\operatorname{Var}_\mu(z)<\operatorname{Var}_\mu(\sin x).
\]

Equivalently, its total stationary activity has the exact budget
\[
\mathbb E_\mu[\dot x^2+\dot y^2+\dot z^2]
=
\mathbb E_\mu[\sin^2x+\sin^2y+\sin^2z]
-b^2\mathbb E_\mu[x^2+y^2+z^2],
\]
and the left side is strictly positive away from equilibrium-supported measures.

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the Thomas flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of the antiderivative test functions used in the proof.

The accepted domain is
\[
0<b<1.
\]
This is the nontrivial feedback regime below the critical damping threshold. The algebraic conditional identities actually remain valid for positive \(b\), but the theorem is deliberately stated in the regime containing the periodic and chaotic dynamics emphasized in the Thomas literature.

The equations are cyclically symmetric: each coordinate receives a nonlinear sine drive from the preceding coordinate and a linear damping term from itself. The conditioning in the theorem follows exactly this feedback architecture; it is not an arbitrary statistical slice.

The earliest verified public date for René Thomas's foundational feedback-circuit paper is 1 October 1999. A same-object bibliographic classification lists the work under MSC \(34C28\) and \(37D45\); the primary classification used here is \(34C28\).

## Proof
Let \(L\) denote the generator.

For any continuous function \(\phi\) on the compact \(x\)-range of the support, choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)(\sin y-bx).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(\sin y-bx)]=0
\]
for every continuous \(\phi\). Therefore
\[
\mathbb E_\mu[\sin y\mid x]=bx.
\]
Cyclic permutation gives the other two conditional identities.

Because
\[
\left|\mathbb E_\mu[\sin y\mid x]\right|\le1,
\]
we have
\[
|x|\le\frac1b
\]
for \(\mu\)-almost every point. The same holds for \(y\) and \(z\). Since the coordinate functions are continuous and the support is the closure of every full-measure set, the support itself lies in the displayed box.

Now
\[
\dot x=\sin y-bx.
\]
The conditional law makes this residual orthogonal in \(L^2(\mu)\) to every square-integrable function of \(x\). In particular,
\[
\mathbb E_\mu[x(\sin y-bx)]=0.
\]
Hence
\[
\mathbb E_\mu[\dot x^2]
=
\mathbb E_\mu[\sin^2y]-b^2\mathbb E_\mu[x^2].
\]
Also
\[
\mathbb E_\mu[\sin y]=b\mathbb E_\mu[x],
\]
so the right side is
\[
\operatorname{Var}_\mu(\sin y)-b^2\operatorname{Var}_\mu(x).
\]
Cyclic permutation yields the other two defect identities. Adding them gives the total activity budget.

It remains to classify equality. Suppose
\[
\mathbb E_\mu[\dot x^2]=0.
\]
The function \(\dot x^2\) is continuous and nonnegative, so
\[
\dot x=0
\]
on the entire support. The support of an invariant probability measure is invariant under the flow. Thus along every support trajectory, \(x\) is constant and
\[
\sin y=bx
\]
is constant.

A continuous real-valued function of time whose sine is constant must itself be constant: the level set of a fixed sine value is discrete, while the continuous image of a connected time interval is connected. Therefore \(y\) is constant. The second equation then gives
\[
\sin z=by,
\]
so the same argument makes \(z\) constant. The third equation is then zero as well. Every support trajectory is an equilibrium.

Thus zero first defect implies support on equilibria. Conversely any probability measure supported on equilibria has zero coordinate speeds. By cyclic symmetry the same equality classification holds for each defect separately.

Therefore any compact invariant probability measure not supported on equilibria has all three speed defects strictly positive.

## Verification
The accompanying exact checker uses sparse-polynomial arithmetic after treating
\[
S_x=\sin x,\qquad S_y=\sin y,\qquad S_z=\sin z
\]
as formal drive variables.

It verifies the three residual identities
\[
\dot x=S_y-bx,
\qquad
\dot y=S_z-by,
\qquad
\dot z=S_x-bz,
\]
and the algebraic decompositions
\[
(S_y-bx)^2-(S_y^2-b^2x^2)=-2bx(S_y-bx),
\]
with the two cyclic analogues. The final term has zero stationary expectation by the corresponding conditional orthogonality.

It also verifies the summed activity identity by exact expansion.

The stored checker output is `VERIFY_OK`.

The checker verifies algebraic certificates only. Conditional expectation, support confinement, and equality rigidity are analytic consequences of invariance and are not inferred from numerical trajectories.

## Relationship to prior work
Thomas introduced the cyclic feedback construction as a route to deterministic chaos and labyrinthine dynamics. Later detailed work by Sprott and Chlouverakis writes the exact three-dimensional sine-ring equations used here, analyzes the bifurcation route to chaos, and studies attractor dimension, multistability, diffusion, and symbolic dynamics.

That complete same-object article was inspected throughout its model, bifurcation, attractor, diffusion, and symbolic-dynamics sections. It contains a special conservative discussion at \(b=0\), including a uniform-measure description of the chaotic sea and an RMS-speed calculation. That is outside the accepted domain \(0<b<1\) and does not imply the damped invariant-measure conditional laws above.

Published work on the Thomas flow also establishes a sharp global damping threshold at and above \(b=1\). The accepted result is deliberately stated below that threshold, where non-equilibrium compact recurrence is the relevant phenomenon. Stability of the origin for \(b\ge1\) does not implication-wise supply the conditional drive-to-state laws for \(0<b<1\).

Later studies address anomalous diffusion, delay, bifurcation structure, and generalized Thomas systems. Targeted searches for invariant-measure conditional moments, stationary sine-drive regressions, variance defects, and derivative-energy balances did not locate a same-object statement implying the theorem.

## Limitations
The theorem is a necessary stationary law. It does not prove existence or uniqueness of a periodic, chaotic, or physical invariant measure for a given \(b\).

The support box
\[
[-1/b,1/b]^3
\]
is a stationary-support consequence and is not asserted to be a sharp absorbing box for arbitrary transients.

The conditional laws determine only the conditional means of the nonlinear drives, not their full conditional distributions.

The theorem does not classify the equilibrium set or compute Lyapunov exponents, entropy, attractor dimension, or diffusion coefficients.

Because the generator proof is short, a differently phrased version could remain in unindexed nonlinear-dynamics literature. No novelty is claimed for the Thomas equations, the route to chaos, the critical damping threshold, or conservative \(b=0\) statistics.

## References
1. R. Thomas, “Deterministic chaos seen in terms of feedback circuits: analysis, synthesis, ‘labyrinth chaos’,” International Journal of Bifurcation and Chaos 9, 1889–1905 (1999), DOI 10.1142/S0218127499001383.
2. J. C. Sprott and K. E. Chlouverakis, “Labyrinth Chaos,” International Journal of Bifurcation and Chaos 17, 2097–2108 (2007), DOI 10.1142/S0218127407018245.
3. G. Rowlands and J. C. Sprott, “Chaotic dynamics on large networks,” Chaos 18 (2008), DOI 10.1063/1.2969429.
4. M. A. F. Sanjuán and A. M. W. Thomas, “The Thomas attractor with and without delay,” Dynamics of Nature and Society (2020), DOI 10.5890/DNC.2020.03.003.
