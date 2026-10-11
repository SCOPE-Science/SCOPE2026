# Fiberwise feedback calibration and a stationary speed budget in the Thomas cyclic sine flow
## Finding
Consider the Thomas cyclic sine flow
\[
\dot x=\sin y-bx,
\qquad
\dot y=\sin z-by,
\qquad
\dot z=\sin x-bz,
\qquad
b>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. No ergodicity, cyclic symmetry of the measure, or uniqueness of the attractor is assumed.

Then each directed feedback edge is calibrated exactly on the receiving coordinate:
\[
\boxed{
\mathbb E_\mu[\sin y\mid x]=bx
},
\qquad
\boxed{
\mathbb E_\mu[\sin z\mid y]=by
},
\qquad
\boxed{
\mathbb E_\mu[\sin x\mid z]=bz
}.
\]

Thus the nonlinear input on every coordinate fiber has conditional mean exactly equal to the linear damping on that fiber.

The residuals are the coordinate speeds, so conditional orthogonality gives three exact variance defects:
\[
\boxed{
\operatorname{Var}_\mu(\sin y)
=
b^2\operatorname{Var}_\mu(x)
+
\mathbb E_\mu[\dot x^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(\sin z)
=
b^2\operatorname{Var}_\mu(y)
+
\mathbb E_\mu[\dot y^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(\sin x)
=
b^2\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}.
\]

The same calibrations fix the three directed feedback covariances:
\[
\boxed{
\operatorname{Cov}_\mu(x,\sin y)
=
b\operatorname{Var}_\mu(x)
},
\]
with the two cyclic analogues.

Write
\[
A=\operatorname{Var}_\mu(x),
\quad
B=\operatorname{Var}_\mu(y),
\quad
C=\operatorname{Var}_\mu(z),
\]
and
\[
U=\mathbb E_\mu[\dot x^2],
\quad
V=\mathbb E_\mu[\dot y^2],
\quad
W=\mathbb E_\mu[\dot z^2].
\]

Because the sine function is one-Lipschitz,
\[
\operatorname{Var}(\sin Y)\le\operatorname{Var}(Y)
\]
for every square-integrable real random variable \(Y\). Therefore every compact stationary Thomas state satisfies the cyclic speed inequalities
\[
B\ge b^2A+U,
\qquad
C\ge b^2B+V,
\qquad
A\ge b^2C+W.
\]

Summing gives the global stationary speed budget
\[
\boxed{
U+V+W
\le
(1-b^2)(A+B+C)
}.
\]

Substitution around the feedback cycle gives three sharper directional budgets:
\[
\boxed{
b^4U+b^2V+W
\le
(1-b^6)A
},
\]
\[
\boxed{
b^4V+b^2W+U
\le
(1-b^6)B
},
\]
\[
\boxed{
b^4W+b^2U+V
\le
(1-b^6)C
}.
\]

Whenever \(A>0\), the exact feedback coherence is
\[
\operatorname{Corr}_\mu(x,\sin y)
=
\left(
1+
\frac{U}{b^2A}
\right)^{-1/2},
\]
and cyclically. Thus the loss of perfect directed feedback correlation is exactly the normalized mean-square coordinate speed.

Finally, every bounded complete trajectory satisfies the causal-past representation
\[
\boxed{
x(t)
=
\int_0^\infty e^{-bs}\sin y(t-s)\,ds
},
\]
together with the two cyclic analogues. Hence every compact invariant set lies in
\[
\boxed{
[-1/b,1/b]^3
}.
\]

The established global-stability threshold at \(b\ge1\) is not part of the originality claim. The contribution assessed here is the fiberwise stationary calibration, the exact variance defects, and the resulting quantitative speed budgets.

## Assumptions and scope
The vector field is the three-dimensional cyclic sine system introduced in the labyrinth-chaos literature. The damping parameter satisfies
\[
b>0.
\]

Compact support guarantees all moments and generator tests used below. The conditional laws themselves require only the corresponding integrability, but compact support is retained for a uniform statement and for the compact-invariant-set corollary.

The theorem is deliberately measure-by-measure. This matters because the same parameter can support several distinct attracting cycles or strange attractors, so an invariant measure need not inherit the full cyclic symmetry of the vector field.

The foundational labyrinth-chaos article was published on 1 October 1999. Mathematical bibliographic metadata classifies that work under MSC \(34C28\) and \(37D45\); the present result uses primary MSC \(34C28\).

## Proof
Let \(L\) denote the generator of the flow.

Take any continuous function \(\phi\) on the compact \(x\)-range of the support, and choose a continuously differentiable antiderivative \(H\) satisfying
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
for every such \(\phi\). Continuous functions determine conditional expectation on the compact \(x\)-support, so
\[
\mathbb E_\mu[\sin y-bx\mid x]=0.
\]
Therefore
\[
\mathbb E_\mu[\sin y\mid x]=bx.
\]
The other two conditional laws follow by cyclic permutation.

Set
\[
R_x=\sin y-bx=\dot x.
\]
The conditional law gives
\[
\mathbb E[R_x\mid x]=0.
\]
Hence \(R_x\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(x\), in particular to \(x-\mathbb E[x]\). Therefore
\[
\operatorname{Var}(\sin y)
=
\operatorname{Var}(bx+R_x)
=
b^2\operatorname{Var}(x)
+
\mathbb E[R_x^2].
\]
This is the first variance defect. Cyclic permutation gives the other two.

The same orthogonality yields
\[
\operatorname{Cov}(x,\sin y)
=
\operatorname{Cov}(x,bx+R_x)
=
b\operatorname{Var}(x).
\]

For the one-Lipschitz variance contraction, let \(Y\) be any square-integrable real random variable. Since variance minimizes quadratic distance to constants,
\[
\operatorname{Var}(\sin Y)
\le
\mathbb E[(\sin Y-\sin\mathbb E[Y])^2]
\le
\mathbb E[(Y-\mathbb E[Y])^2].
\]
Thus
\[
\operatorname{Var}(\sin Y)
\le
\operatorname{Var}(Y).
\]

Applying this to the exact defects gives
\[
B\ge b^2A+U,
\qquad
C\ge b^2B+V,
\qquad
A\ge b^2C+W.
\]
Summing proves
\[
U+V+W
\le
(1-b^2)(A+B+C).
\]

For the first directional budget, substitute the first inequality into the second and then into the third:
\[
A
\ge
b^2C+W
\ge
b^4B+b^2V+W
\ge
b^6A+b^4U+b^2V+W.
\]
Rearrangement gives
\[
b^4U+b^2V+W
\le
(1-b^6)A.
\]
The other two follow cyclically.

If \(A>0\), then
\[
\operatorname{Var}(\sin y)
=
b^2A+U
\]
and
\[
\operatorname{Cov}(x,\sin y)=bA.
\]
Therefore
\[
\operatorname{Corr}(x,\sin y)
=
\frac{bA}{\sqrt{A(b^2A+U)}}
=
\left(
1+\frac{U}{b^2A}
\right)^{-1/2}.
\]

For the bounded-complete-trajectory representation, solve
\[
\dot x+bx=\sin y
\]
backward over a time interval of length \(T\):
\[
x(t)
=
e^{-bT}x(t-T)
+
\int_0^T e^{-bs}\sin y(t-s)\,ds.
\]
On a bounded complete trajectory, the first term tends to zero as
\[
T\to\infty.
\]
Dominated convergence gives
\[
x(t)
=
\int_0^\infty e^{-bs}\sin y(t-s)\,ds.
\]
Consequently
\[
|x(t)|
\le
\int_0^\infty e^{-bs}\,ds
=
\frac1b.
\]
The two cyclic formulas give the full cube bound.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the abstract variance decomposition generated by a conditional residual with zero conditional mean, the covariance identity, the summed speed budget, and the three-step cyclic substitution producing the directional coefficient pattern
\[
b^4,\quad b^2,\quad 1.
\]

It also verifies the elementary exponential-kernel normalization
\[
\int_0^\infty e^{-bs}\,ds=\frac1b
\]
symbolically at the coefficient level.

The stored checker output is `VERIFY_OK`.

The conditional-expectation theorem and the bounded-complete-trajectory representation are analytic proofs; they are not inferred from finite trajectory sampling.

## Relationship to prior work
Thomas introduced labyrinth chaos as a feedback-circuit construction in 1999. The foundational article establishes the feedback architecture and the many-equilibrium chaotic setting.

Sprott and Chlouverakis study exactly
\[
\dot x=\sin y-bx,
\qquad
\dot y=\sin z-by,
\qquad
\dot z=\sin x-bz.
\]
Their complete 2007 article analyzes the route from equilibria to periodic motion and chaos, Lyapunov and correlation dimensions, multistability, several coexisting cycles and strange attractors, numerical trajectory standard deviations and kurtosis, the conservative limit, diffusion, and symbolic dynamics.

That article is especially close because it uses long-time standard deviations and interprets trajectory averages through an ergodic hypothesis. Its statistic is a global radial average for selected natural measures. It does not implication-wise supply the present all-invariant-measures conditional relations on individual coordinate fibers. Full-document searches found no conditional-expectation, variance, or moment theorem; the numerical standard-deviation calculation is not the same statement.

Recent work on the Thomas system continues to study stable regimes, limit cycles, fixed-point sequences, bifurcations, multiple attractors, and the low-damping limit. Those orbit-structure results do not imply the three conditional regressions.

The known global-stability threshold at and above critical damping is explicitly excluded from the originality claim. The accepted statement instead quantifies stationary feedback transfer throughout the recurrent regime and applies separately to each coexisting invariant state.

## Limitations
The theorem does not determine which invariant measures exist for a given
\[
b.
\]
It does not classify periodic windows, crises, bifurcations, or strange-attractor geometry.

The cube
\[
[-1/b,1/b]^3
\]
is a universal bounded-complete-trajectory envelope, not asserted to be the smallest trapping region.

The speed budgets are necessary stationary constraints. They do not determine the three variances separately.

The correlation formula is stated only when the receiving coordinate has positive variance.

The complete foundational 1999 publisher text was not used for a blanket whole-document novelty exclusion; the complete 2007 same-object article provides the principal full-text comparison.

Because the generator argument is short, a differently phrased equivalent fiberwise identity could remain in unindexed literature.

## References
1. R. Thomas, “Deterministic Chaos Seen in Terms of Feedback Circuits: Analysis, Synthesis, ‘Labyrinth Chaos’,” International Journal of Bifurcation and Chaos 9, 1889–1905 (1999), DOI 10.1142/S0218127499001383.
2. J. C. Sprott and K. E. Chlouverakis, “Labyrinth Chaos,” International Journal of Bifurcation and Chaos 17, 2097–2108 (2007), DOI 10.1142/S0218127407018245.
3. I. Sorin and M. Tulchinsky, “Infinite Bifurcations in Thomas system,” arXiv:2408.09525 (2024).
