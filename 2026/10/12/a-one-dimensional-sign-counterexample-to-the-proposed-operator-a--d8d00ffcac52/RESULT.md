# A one-dimensional sign counterexample to the proposed operator-alignment condition
## Finding

A recently proposed learning-augmented projected quasi-gradient framework imposes the alignment condition
\[
\langle b_k(x),x-x^\star\rangle
\le
\eta\langle Q(x),x-x^\star\rangle,
\qquad
0\le\eta<1,
\]
and then uses it to claim
\[
\langle Q(x)+b_k(x),x-x^\star\rangle
\ge
(1-\eta)\langle Q(x),x-x^\star\rangle.
\]
That implication is false: an upper bound on the bias inner product gives no lower bound preventing the bias from pointing strongly against the base direction.

The defect already appears in one dimension. Let
\[
\mathcal C=[-1,1],
\qquad
f(x)=\frac12x^2,
\qquad
x^\star=0,
\qquad
Q(x)=x,
\]
and choose the deterministic learned correction
\[
b_k(x)=-2x
\]
for every \(k\), with zero stochastic noise and
\[
\eta=0.
\]
Then
\[
\langle b_k(x),x-x^\star\rangle=-2x^2\le0
=
\eta\langle Q(x),x-x^\star\rangle,
\]
so the printed alignment condition holds everywhere on \(\mathcal C\).

Nevertheless,
\[
Q(x)+b_k(x)=-x,
\]
so the augmented direction reverses the gradient. With the source's diminishing step rule
\[
\alpha_k=\frac1{k+1},
\]
the projected iteration is
\[
x_{k+1}
=
\Pi_{[-1,1]}
\left(
\left(1+\frac1{k+1}\right)x_k
\right).
\]
Starting from
\[
x_0=\frac12,
\]
we obtain
\[
x_1=1
\]
and then
\[
x_k=1
\qquad
\text{for every }k\ge1.
\]
Hence
\[
\|x_k-x^\star\|^2=1
\]
for every \(k\ge1\), contradicting the asserted \(O(1/k)\) decay.

The directional condition that gives the intended proof step is instead
\[
\langle b_k(x),x-x^\star\rangle
\ge
-\eta\langle Q(x),x-x^\star\rangle.
\]
If the base operator separately satisfies
\[
\langle Q(x),x-x^\star\rangle
\ge
m\|x-x^\star\|^2,
\]
then the corrected condition yields
\[
\langle Q(x)+b_k(x),x-x^\star\rangle
\ge
(1-\eta)m\|x-x^\star\|^2.
\]
This is exactly the inequality used by the contraction argument.

## Assumptions and scope

The counterexample uses the source's strongly convex regime. The feasible set is nonempty, closed, convex, and compact. The objective is smooth and \(1\)-strongly convex. The base mapping \(Q(x)=x\) is a quasi-gradient in the source's sense because
\[
x^2
=
2\left(f(x)-f(x^\star)\right).
\]
It also has linear growth and is uniformly bounded on \(\mathcal C\).

The learned correction \(b_k(x)=-2x\) is deterministic, continuous, uniformly bounded on \(\mathcal C\), and satisfies the printed alignment condition with \(\eta=0\). The stochastic component is identically zero, so every stated variance requirement is satisfied with variance bound zero.

The finding is deliberately narrow: it isolates the sign defect in the alignment hypothesis and the contraction step depending on it. It does not assess unrelated claims or attempt to reprove the full framework under corrected assumptions.

## Proof

For
\[
f(x)=\frac12x^2
\]
on
\[
[-1,1],
\]
the unique minimizer is \(x^\star=0\), and \(f\) is \(1\)-strongly convex.

Take
\[
Q(x)=x.
\]
Then
\[
\langle Q(x),x-x^\star\rangle=x^2,
\]
so the base direction has the exact strong monotonicity relation needed in the source proof.

Now set
\[
b_k(x)=-2x.
\]
For every \(x\in[-1,1]\),
\[
\langle b_k(x),x-x^\star\rangle=-2x^2.
\]
With \(\eta=0\), the printed alignment condition becomes
\[
-2x^2\le0,
\]
which is true for every \(x\).

However,
\[
\langle Q(x)+b_k(x),x-x^\star\rangle
=
-x^2,
\]
whereas the source proof requires the lower bound
\[
x^2.
\]
Thus the algebraic implication used in the contraction lemma is reversed.

For the actual iteration, zero noise gives
\[
x_{k+1}
=
\Pi_{[-1,1]}
\left(
x_k-\alpha_k(Q(x_k)+b_k(x_k))
\right)
=
\Pi_{[-1,1]}
\left(
(1+\alpha_k)x_k
\right).
\]
Under the source schedule
\[
\alpha_k=\frac1{k+1},
\]
we have
\[
x_1
=
\Pi_{[-1,1]}(2x_0).
\]
Choosing
\[
x_0=\frac12
\]
gives \(x_1=1\). For every later \(k\),
\[
(1+\alpha_k)x_k>1,
\]
so projection returns \(x_{k+1}=1\). Therefore
\[
x_k=1
\]
for all \(k\ge1\), and no decay to \(x^\star\) occurs.

The source's one-step recursion also fails eventually for every fixed finite bound \(G\) on \(Q(x_k)\). Once \(x_k=1\), its asserted right-hand side has the form
\[
1-2\alpha_k+\alpha_k^2(2G^2+8).
\]
For every finite \(G\), this is strictly below \(1\) whenever
\[
0<\alpha_k<\frac{2}{2G^2+8},
\]
while the left-hand side equals \(1\). Since \(\alpha_k\to0\), such iterates necessarily occur.

Finally, the corrected directional hypothesis
\[
\langle b_k(x),x-x^\star\rangle
\ge
-\eta\langle Q(x),x-x^\star\rangle
\]
immediately gives
\[
\langle Q(x)+b_k(x),x-x^\star\rangle
\ge
(1-\eta)\langle Q(x),x-x^\star\rangle.
\]
Combining this with any independently justified lower bound
\[
\langle Q(x),x-x^\star\rangle
\ge
m\|x-x^\star\|^2
\]
restores the intended contraction term.

## Verification

The standalone script `artifacts/verify_alignment_sign.py` uses exact rational arithmetic. It checks the printed alignment condition on a rational grid, replays the source diminishing-step schedule, verifies finite-time absorption at the wrong boundary point, and checks an explicit violation of the claimed one-step recursion.

The computation is only a replay. The counterexample and the corrected implication are proved symbolically above.

## Relationship to prior work

The primary paper states the upper alignment inequality and explicitly says that it prevents the learned correction from counteracting too much of the descent geometry. In its strongly convex proof, however, it uses that upper bound as though it were a lower bound and derives the opposite-sided conclusion.

Targeted searches for the article title, DOI, alignment condition, sign corrections, and counterexamples did not locate a published correction or an equivalent counterexample. Published-result searches using operator-alignment, biased-gradient, adversarial-bias, and relative-error aliases also did not locate this source-specific obstruction.

The broader inexact-gradient literature commonly controls errors by norm-relative conditions or two-sided error models. Such hypotheses can prevent an error from reversing the gradient direction, but they do not imply that the printed one-sided upper inner-product condition is sufficient. Recent work on relative gradient errors and composite relative-plus-absolute noise reinforces that directional robustness requires genuine magnitude or angle control rather than a one-sided upper bound alone.

## Limitations

The result establishes failure of the stated strongly convex alignment hypothesis and the contraction conclusions that depend on the invalid sign implication. It does not claim that every numerical experiment in the source is unstable.

The proposed lower alignment inequality repairs the specific sign step only when the base mapping already has the required positive lower bound against \(x-x^\star\). The source's broader quasi-gradient normalization and its PL, nonconvex, mirror, and architecture-specific extensions are not re-certified here.

No claim is made that the corrected condition is the weakest possible robust assumption.

## References

1. G. Pérez-Lechuga, M. A. Coronel García, A. L. Martínez Salazar, *Learning-Augmented Quasi-Gradient Operators for Constrained Optimization: A Contraction–Bias–Variance Decomposition*, Mathematics 14(7), 1202, 2026. DOI: 10.3390/math14071202.
2. A. Vasin et al., *On Solving Minimization and Min-Max Problems by First-Order Methods with Relative Error in Gradients*, arXiv:2503.06628, 2025.
3. A. Vasin, A. Gasnikov, *Lower and upper bounds of the convergence rate of gradient methods with composite noise in gradient*, arXiv:2603.12376, 2026.
4. O. Gannot, *A frequency-domain analysis of inexact gradient methods*, arXiv:1912.13494, 2019.
