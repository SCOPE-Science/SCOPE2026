# Dual stationary conditional laws and equilibrium-straddling in the Selkov oscillator
## Finding
Consider the positive Selkov oscillator
\[
\dot x=1-xy^\gamma,
\qquad
\dot y=\alpha y(xy^{\gamma-1}-1)
=\alpha(xy^\gamma-y),
\]
with
\[
\alpha>0,
\qquad
\gamma\in\{2,3,\ldots\}.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure whose support lies in
\[
(0,\infty)^2.
\]
Define the reaction-flux observable
\[
Q=xy^\gamma.
\]
Then
\[
\boxed{
\mathbb E_\mu[Q\mid x]=1
}
\]
and
\[
\boxed{
\mathbb E_\mu[Q\mid y]=y
}.
\]
Equivalently,
\[
\boxed{
\mathbb E_\mu[y^\gamma\mid x]=\frac1x
}
\]
and
\[
\boxed{
\mathbb E_\mu[x\mid y]=y^{1-\gamma}
}.
\]

Thus the same nonlinear reaction flux is mean-independent of the substrate coordinate \(x\), while its conditional mean given the product coordinate \(y\) is exactly \(y\).

Taking expectations gives
\[
\boxed{
\mathbb E_\mu[Q]=1,
\qquad
\mathbb E_\mu[y]=1
}.
\]
The conditional laws also give
\[
\boxed{
\operatorname{Cov}_\mu(x,Q)=0
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(y,Q)=\operatorname{Var}_\mu(y)
}.
\]

The two evolution equations identify the regression residuals exactly:
\[
Q=1-\dot x
\]
and
\[
Q=y+\frac{\dot y}{\alpha}.
\]
Therefore
\[
\boxed{
\mathbb E_\mu[\dot x^2]
=
\operatorname{Var}_\mu(Q)
=
\operatorname{Var}_\mu(y)
+
\frac1{\alpha^2}\mathbb E_\mu[\dot y^2]
}.
\]

The equilibrium atom
\[
\delta_{(1,1)}
\]
is the unique compact stationary state for which either
\[
\mathbb E_\mu[\dot x^2]=0
\]
or
\[
\mathbb E_\mu[\dot y^2]=0.
\]

Every other compact stationary state satisfies the strict mean inequalities
\[
\boxed{
\mathbb E_\mu[x]>1
}
\]
and
\[
\boxed{
\mathbb E_\mu[1/x]>1
}.
\]
Consequently it places positive invariant mass on both sides of the equilibrium substrate level:
\[
\boxed{
\mu\{x<1\}>0,
\qquad
\mu\{x>1\}>0
}.
\]
Since
\[
\mathbb E[y]=1
\]
and a non-equilibrium stationary state cannot have \(y=1\) almost surely, it also satisfies
\[
\boxed{
\mu\{y<1\}>0,
\qquad
\mu\{y>1\}>0
}.
\]

For every non-equilibrium compact stationary state,
\[
\boxed{
0<
\operatorname{Corr}_\mu(y,Q)
<
1
}
\]
with the exact activity formula
\[
\boxed{
\operatorname{Corr}_\mu(y,Q)
=
\left(
1+
\frac{\mathbb E_\mu[\dot y^2]}
{\alpha^2\operatorname{Var}_\mu(y)}
\right)^{-1/2}
}.
\]

In particular, every nonconstant positive periodic orbit crosses each equilibrium concentration level
\[
x=1
\quad\text{and}\quad
y=1
\]
at least twice per least period.

## Assumptions and scope
The theorem concerns the dimensionless Selkov system
\[
\dot x=1-xy^\gamma,
\qquad
\dot y=\alpha y(xy^{\gamma-1}-1),
\]
with \(\alpha>0\) and integer \(\gamma>1\), exactly as used in the modern rigorous analysis of the Selkov oscillator.

Compact support strictly inside the positive quadrant ensures all observables are integrable and permits the one-coordinate generator tests. No ergodicity assumption is made.

Selkov's original 1968 work introduced the positive glycolytic oscillator, showed the existence of a unique positive equilibrium in the normalized model, and analyzed self-oscillation and limit cycles. Those orbit-level facts are prior work.

The modern rigorous study proves the Hopf bifurcation, uniqueness alternatives for periodic solutions, the global phase portrait of bounded solutions, and the existence of unbounded solutions. Those results are also prior work.

The finding here is the dual invariant-measure disintegration of the nonlinear reaction flux, its exact derivative-energy decomposition, and the strict stationary straddling theorem.

The earliest checked public source date is 1 March 1968. A modern mathematical record for the Selkov oscillator lists \(34C25\) first in its Mathematics Subject Classification; that primary code is used here.

## Proof
Let
\[
Q=xy^\gamma.
\]

Fix a continuous function \(\phi\) on the compact \(x\)-projection of the support and choose an antiderivative \(F\) satisfying
\[
F'(x)=\phi(x).
\]
For the flow generator \(L\),
\[
LF
=
\phi(x)(1-Q).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(1-Q)]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[Q\mid x]=1.
\]
Because \(x>0\),
\[
\mathbb E_\mu[y^\gamma\mid x]=\frac1x.
\]

Likewise, for a continuous function \(\psi\) of \(y\), choose an antiderivative \(G\) with
\[
G'(y)=\psi(y).
\]
Then
\[
LG
=
\alpha\psi(y)(Q-y).
\]
Stationarity gives
\[
\mathbb E_\mu[Q\mid y]=y.
\]
Since \(y>0\),
\[
\mathbb E_\mu[x\mid y]=y^{1-\gamma}.
\]

Taking expectations in the first law gives
\[
\mathbb E[Q]=1.
\]
Taking expectations in the second gives
\[
\mathbb E[y]=1.
\]

The first law implies
\[
\mathbb E[xQ]
=
\mathbb E[x],
\]
so
\[
\operatorname{Cov}(x,Q)=0.
\]
The second gives
\[
\mathbb E[yQ]
=
\mathbb E[y^2],
\]
hence
\[
\operatorname{Cov}(y,Q)
=
\operatorname{Var}(y).
\]

The first differential equation gives
\[
Q-1=-\dot x.
\]
Since
\[
\mathbb E[Q]=1,
\]
\[
\operatorname{Var}(Q)
=
\mathbb E[\dot x^2].
\]

The second differential equation gives
\[
Q-y=\frac{\dot y}{\alpha}.
\]
The conditional law
\[
\mathbb E[Q\mid y]=y
\]
is equivalent to
\[
\mathbb E[\dot y\mid y]=0.
\]
Thus \(\dot y/\alpha\) is orthogonal to every square-integrable function of \(y\). Therefore
\[
\operatorname{Var}(Q)
=
\operatorname{Var}(y)
+
\frac1{\alpha^2}\mathbb E[\dot y^2].
\]
Combining the two expressions for \(\operatorname{Var}(Q)\) proves the activity identity.

If
\[
\mathbb E[\dot x^2]=0,
\]
then \(\dot x=0\) on invariant support and
\[
Q=1.
\]
Along every support trajectory \(x\) is constant. The second equation becomes
\[
\dot y=\alpha(1-y).
\]
The only complete bounded trajectory of this scalar equation is
\[
y=1.
\]
Then \(Q=1\) gives
\[
x=1.
\]

If instead
\[
\mathbb E[\dot y^2]=0,
\]
then \(y\) is constant along every support trajectory. The second equation gives
\[
Q=y.
\]
The first becomes
\[
\dot x=1-y.
\]
Compact completeness forces
\[
y=1,
\]
and then \(Q=1\) forces
\[
x=1.
\]
Thus either defect vanishes exactly at the equilibrium atom.

Now use
\[
\mathbb E[x\mid y]=y^{1-\gamma}.
\]
Because
\[
t\mapsto t^{1-\gamma}
\]
is strictly convex on the positive axis and
\[
\mathbb E[y]=1,
\]
Jensen's inequality gives
\[
\mathbb E[x]
=
\mathbb E[y^{1-\gamma}]
\ge1.
\]
Equality holds only when \(y=1\) almost surely, which has already been classified as the equilibrium atom. Hence every non-equilibrium state has
\[
\mathbb E[x]>1.
\]

Similarly,
\[
\mathbb E[1/x]
=
\mathbb E[y^\gamma]
\ge
\mathbb E[y]^\gamma
=
1,
\]
with equality only at the equilibrium atom. Thus
\[
\mathbb E[1/x]>1
\]
away from equilibrium.

If a non-equilibrium state had
\[
x\ge1
\]
almost surely, then
\[
1/x\le1
\]
almost surely, contradicting the strict reciprocal-mean inequality. If it had
\[
x\le1
\]
almost surely, it would contradict
\[
\mathbb E[x]>1.
\]
Therefore it has positive mass on both sides of \(x=1\).

Since
\[
\mathbb E[y]=1
\]
and \(y\) is not almost surely constant in a non-equilibrium state, it likewise has positive mass on both sides of \(y=1\).

Finally,
\[
\operatorname{Corr}(y,Q)
=
\frac{\operatorname{Var}(y)}
{\sqrt{\operatorname{Var}(y)\operatorname{Var}(Q)}}
=
\sqrt{
\frac{\operatorname{Var}(y)}
{\operatorname{Var}(Q)}
}.
\]
Substituting the variance decomposition gives the displayed formula and strict bounds.

For a nonconstant periodic orbit, its normalized time measure is invariant. Positive invariant mass on both sides of either equilibrium level means the corresponding continuous periodic coordinate takes values on both sides, forcing at least two crossings per least period.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the two residual identities
\[
Q-1=-\dot x,
\qquad
Q-y=\frac{\dot y}{\alpha},
\]
the covariance consequences of the two conditional laws, and the exact activity decomposition
\[
\mathbb E[\dot x^2]
=
\operatorname{Var}(y)
+
\alpha^{-2}\mathbb E[\dot y^2].
\]

It also verifies the convexity exponents for integer \(\gamma>1\) and the algebraic equilibrium conditions.

The stored checker output is `VERIFY_OK`.

The conditional-expectation quantifiers, strict Jensen cases, complete-trajectory equality classification, and periodic crossing count are analytic arguments and are not inferred from finite simulation.

## Relationship to prior work
Selkov's original paper introduces the glycolytic self-oscillation model, analyzes its equilibrium and phase portrait, and establishes a limit-cycle regime. Its complete searchable text contains no `conditional`, `average`, or `moment` formulation; the only `variance` match is the ordinary prose phrase “at variance with,” not a statistical variance theorem.

Brechmann and Rendall give a modern rigorous analysis of the same dimensionless Selkov system. Their complete public text writes
\[
\dot x=1-xy^\gamma,
\qquad
\dot y=\alpha y(xy^{\gamma-1}-1),
\]
proves the Hopf bifurcation, determines the global alternatives for bounded solutions, and analyzes the Poincaré compactification and unbounded trajectories. Full-document searches found no `conditional`, `variance`, `average`, or `moment` formulation.

The accepted theorem concerns a distinct statistical layer. The first conditional law calibrates the nonlinear reaction flux at every substrate concentration, while the second calibrates it at every product concentration. Their combination forces strict arithmetic and reciprocal mean shifts and therefore recurrent crossing of both equilibrium concentration levels.

## Limitations
The theorem is restricted to invariant probability measures with compact support strictly inside the positive quadrant. It does not apply to unbounded solutions, whose existence is a known feature of the Selkov system.

It determines two conditional means and selected second-order statistics, not the full invariant distribution or the limit-cycle period.

The strict straddling theorem concerns stationary compact recurrence and does not claim that every positive initial condition is bounded.

Because the generator argument is short, an equivalent weighted stationary identity could remain in older unindexed glycolysis literature.

## References
1. E. E. Sel'kov, “Self-Oscillations in Glycolysis 1. A Simple Kinetic Model,” *European Journal of Biochemistry* 4, 79–86 (1968), DOI 10.1111/j.1432-1033.1968.tb00175.x.
2. P. Brechmann and A. D. Rendall, “Dynamics of the Selkov oscillator,” *Mathematical Biosciences* 306, 152–159 (2018), DOI 10.1016/j.mbs.2018.09.012; arXiv:1803.10579.
