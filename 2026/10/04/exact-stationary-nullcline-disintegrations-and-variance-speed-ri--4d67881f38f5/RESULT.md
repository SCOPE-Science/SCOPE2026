# Exact stationary nullcline disintegrations and variance-speed rigidity in the Hindmarsh–Rose neuron
## Finding
Consider the canonical three-dimensional Hindmarsh–Rose neuron
\[
\dot x=y-a x^3+b x^2-z+I,
\qquad
\dot y=c-dx^2-y,
\qquad
\dot z=r\bigl[s(x-x_R)-z\bigr],
\]
with
\[
d>0,\qquad r>0,\qquad s>0.
\]

For every compactly supported invariant probability measure \(\mu\), the two recovery coordinates satisfy exact stationary nullcline disintegrations:
\[
\mathbb E_\mu[x^2\mid y]=\frac{c-y}{d},
\qquad
\mathbb E_\mu[x\mid z]=x_R+\frac{z}{s}.
\]
In particular,
\[
y\le c
\]
for \(\mu\)-almost every state.

The first two stationary moments also satisfy the exact parabola defect
\[
c-\mathbb E_\mu[y]
-d\left(x_R+\frac{\mathbb E_\mu[z]}{s}\right)^2
=
d\,\operatorname{Var}_\mu(x)
\ge0.
\]
Equality here holds exactly for a single equilibrium atom.

More strongly, the conditional residuals are exactly the coordinate speeds. Hence
\[
d^2\operatorname{Var}_\mu(x^2)-\operatorname{Var}_\mu(y)
=
\mathbb E_\mu[\dot y^2]
\ge0,
\]
and
\[
s^2\operatorname{Var}_\mu(x)-\operatorname{Var}_\mu(z)
=
\frac{1}{r^2}\mathbb E_\mu[\dot z^2]
\ge0.
\]
Equality in either variance defect holds exactly for probability measures supported on the equilibrium set. Consequently every compact invariant probability measure that gives positive mass to genuinely time-dependent dynamics satisfies both strict inequalities.

For the frequently used coefficients
\[
d=5,\qquad s=4,
\]
the identities become
\[
\mathbb E[x^2\mid y]=\frac{1-y}{5}
\]
when \(c=1\), and
\[
25\operatorname{Var}(x^2)-\operatorname{Var}(y)=\mathbb E[\dot y^2],
\qquad
16\operatorname{Var}(x)-\operatorname{Var}(z)=r^{-2}\mathbb E[\dot z^2].
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the autonomous Hindmarsh–Rose flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all functions used below and makes every trajectory in the support bounded and complete.

The parameters \(a,b,c,I,x_R\) may be arbitrary real numbers for the identities themselves; only
\[
d>0,\qquad r>0,\qquad s>0
\]
are needed for the stated signs and normalizations. The usual neuronal regime additionally takes positive cubic and quadratic-shape parameters.

The equations are the standard three-variable Hindmarsh–Rose bursting model after the slow adaptation equation is introduced. The earliest verified public source date for the model is 22 March 1984.

## Proof
Let \(L\) denote the generator of the flow.

For any continuous function \(\phi\) on the compact \(y\)-range of the support, choose a continuously differentiable antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH=\phi(y)(c-dx^2-y).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(y)(c-dx^2-y)]=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[x^2\mid y]=\frac{c-y}{d}.
\]
Because a conditional expectation of the nonnegative variable \(x^2\) is nonnegative,
\[
y\le c
\]
almost surely.

Likewise, for any continuous function \(\psi\) on the compact \(z\)-range and an antiderivative \(K\),
\[
LK=\psi(z)r\bigl[s(x-x_R)-z\bigr].
\]
Thus
\[
\mathbb E_\mu[x\mid z]=x_R+\frac{z}{s}.
\]
Taking expectations yields
\[
\mathbb E[x^2]=\frac{c-\mathbb E[y]}{d},
\qquad
\mathbb E[x]=x_R+\frac{\mathbb E[z]}{s}.
\]
Subtracting the square of the second identity from the first gives
\[
c-\mathbb E[y]
-d\left(x_R+\frac{\mathbb E[z]}{s}\right)^2
=d\operatorname{Var}(x).
\]

If this defect vanishes, then \(x\) is constant on the invariant support. Along a bounded complete support trajectory, the equation
\[
\dot y=c-dx^2-y
\]
with constant \(x\) has only its constant bounded complete solution. The first equation then makes \(z\) constant, and the third equation forces the equilibrium relation. Thus the support is one equilibrium point. The converse is immediate.

For the first variance defect, define
\[
R_y=x^2-\frac{c-y}{d}.
\]
The conditional law gives
\[
\mathbb E[R_y\mid y]=0,
\]
while the differential equation gives
\[
R_y=-\frac{\dot y}{d}.
\]
Orthogonality of a conditional-expectation residual to every square-integrable function of \(y\) gives
\[
\operatorname{Var}(x^2)
=
\frac{1}{d^2}\operatorname{Var}(y)
+
\mathbb E[R_y^2].
\]
Therefore
\[
d^2\operatorname{Var}(x^2)-\operatorname{Var}(y)
=
\mathbb E[\dot y^2].
\]

Similarly, define
\[
R_z=x-x_R-\frac{z}{s}.
\]
Then
\[
\mathbb E[R_z\mid z]=0,
\qquad
R_z=\frac{\dot z}{rs}.
\]
Hence
\[
\operatorname{Var}(x)
=
\frac{1}{s^2}\operatorname{Var}(z)
+
\frac{1}{r^2s^2}\mathbb E[\dot z^2],
\]
which is equivalent to
\[
s^2\operatorname{Var}(x)-\operatorname{Var}(z)
=
\frac1{r^2}\mathbb E[\dot z^2].
\]

It remains to classify equality in the variance defects. If \(\mathbb E[\dot y^2]=0\), continuity implies \(\dot y=0\) on the invariant support. Thus \(y\) and \(x^2\) are constant along each support trajectory. Continuity of a trajectory makes \(x\) itself constant, the first equation then fixes \(z\), and the third equation is zero. Every support trajectory is therefore an equilibrium. Conversely every measure supported on equilibria has \(\dot y=0\).

If \(\mathbb E[\dot z^2]=0\), then \(z\) is constant on each support trajectory and the third equation makes \(x\) constant. The first equation then makes \(y\) constant, and the second equation vanishes. Again the support consists only of equilibria, and the converse is immediate.

## Verification
The accompanying exact-arithmetic checker verifies the polynomial generator identities
\[
L\left(\frac{y^2}{2}\right)=y(c-dx^2-y),
\]
\[
L\left(\frac{z^2}{2}\right)=rz\bigl[s(x-x_R)-z\bigr],
\]
and the cleared residual identities
\[
dx^2-c+y=-\dot y,
\qquad
r\bigl[s(x-x_R)-z\bigr]=\dot z.
\]

It also verifies the standard coefficient specializations for \(d=5\) and \(s=4\). The stored checker output is `VERIFY_OK`.

The checker validates the algebraic premises. The conditional laws use arbitrary one-variable test functions, and the equality classifications use invariance of compact support and bounded complete trajectories; neither step is a finite numerical experiment.

## Relationship to prior work
The original Hindmarsh–Rose paper develops the three-variable model to explain triggered and periodic neuronal bursting. Its analysis emphasizes equilibrium structure, phase-plane geometry of the fast subsystem, slow adaptation, and numerical burst generation.

A later energy analysis derives a generalized Hamiltonian-like energy for the Hindmarsh–Rose system and studies long-run energy consumption and synchronization. Its global average-energy balance is different from the coordinatewise conditional laws here: the latter identify the exact conditional voltage power at every recovery level and the exact conditional mean voltage at every adaptation level.

A modern mathematical treatment of admissible perturbations writes the same general three-dimensional equations and studies preserved dynamical phenomena such as periodic and strange attractors. The present statement instead concerns every compactly supported invariant probability measure and supplies exact stationary disintegrations and variance-speed defects.

Targeted searches for conditional-expectation, variance-defect, derivative-energy, nullcline-regression, and equivalent moment formulations did not locate a same-object statement implying the result. Published exact stationary laws for other chaotic flows are not reductions of the Hindmarsh–Rose equations.

## Limitations
The theorem assumes compact support and does not prove that every parameter choice has a compact attractor or a non-equilibrium invariant measure.

The identities constrain selected conditional means and variances; they do not determine the complete stationary distribution or firing statistics.

Measures supported on several equilibria can realize equality in the two variance-speed defects. The separate mean-parabola defect is stricter: its equality case is a single equilibrium atom.

The energy literature contains other global balance functions, and short moment identities can appear incidentally under different notation. The novelty claim is restricted to the two coordinatewise conditional laws, their exact variance-speed defects, and the equality rigidity stated above.

## References
1. J. L. Hindmarsh and R. M. Rose, “A model of neuronal bursting using three coupled first order differential equations,” Proceedings of the Royal Society of London. Series B 221, 87–102 (1984), DOI 10.1098/rspb.1984.0024.
2. F. J. Torrealdea, A. d’Anjou, M. Graña, and C. Sarasola, “Energy aspects of the synchronization of model neurons,” Physical Review E 74, 011905 (2006), DOI 10.1103/PhysRevE.74.011905.
3. “Admissible perturbations of the three-dimensional Hindmarsh–Rose neuron model,” Journal of Applied Analysis and Computation 13 (2023), DOI 10.11948/20210098.
