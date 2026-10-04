# Coercive scalar reversal of reflection tuning in generalized FRB
## Finding

Consider the constant-reflection generalized forward-reflected-backward iteration
\[
x_{k+1}
=
\operatorname{prox}_{\tau g}
\left(
x_k-\tau\bigl[(1+\alpha)F(x_k)-\alpha F(x_{k-1})\bigr]
\right),
\qquad
\alpha>\frac12.
\]
On the one-dimensional strongly monotone problem
\[
g\equiv0,
\qquad
F(x)=ax,
\qquad
a>0,
\]
write
\[
t=a\tau.
\]
Then the exact recurrence is
\[
x_{k+1}
=
\bigl[1-(1+\alpha)t\bigr]x_k+\alpha t\,x_{k-1}.
\]

Its characteristic polynomial is Schur stable exactly when
\[
0<t<\frac{2}{1+2\alpha}.
\]
Thus for every initial pair the recurrence converges to the unique zero whenever the inequality holds. With the initialization
\[
x_{-1}=x_0\ne0
\]
used by the source algorithms, convergence holds if and only if the same strict inequality holds.

Inside the stable interval the exact asymptotic root factor is
\[
q(t,\alpha)
=
\frac{
\sqrt{\bigl(1-(1+\alpha)t\bigr)^2+4\alpha t}
+
\left|1-(1+\alpha)t\right|
}{2}.
\]
For every \(\alpha>1/2\), this factor has the unique minimizer
\[
t_\star=\frac{1}{1+\alpha},
\qquad
q_\star=\sqrt{\frac{\alpha}{1+\alpha}}.
\]

Consequently, on this coercive scalar mode, both stability and asymptotic rate improve as the reflection coefficient decreases toward its admissible endpoint:
\[
\frac{2}{1+2\alpha}\uparrow1,
\qquad
q_\star\downarrow\frac1{\sqrt3}
\quad\text{as}\quad
\alpha\downarrow\frac12.
\]
Neither limiting optimum is attained because the generalized FRB theory requires \(\alpha>1/2\).

This direction is the reverse of the source paper's generic Lyapunov safety coefficient, which is largest at \(\alpha=2\). The calculation therefore isolates a genuine geometry dependence in reflection tuning: the parameter favored by the worst-case monotone analysis need not be the parameter favored by a purely coercive scalar mode.

## Assumptions and scope

The statement is deterministic, one-dimensional, unconstrained, fixed-step, and exact-arithmetic. The forward operator is the positive scalar map \(F(x)=ax\), whose Lipschitz and strong-monotonicity constants both equal \(a\). The proximal term is absent.

The reflection coefficient is restricted to \(\alpha>1/2\), matching the tight admissible coefficient range identified by the recent source for sufficiently small constant steps. The result does not enlarge the source theorem for arbitrary monotone operators. In particular, skew-symmetric modes impose different restrictions and lead to a different robust tuning problem.

The standard FRB slice \(\alpha=1\) is not an originality claim. It gives
\[
t_{\mathrm{stab}}=\frac23,
\qquad
t_\star=\frac12,
\qquad
q_\star=\frac1{\sqrt2},
\]
consistent with earlier reflected-gradient analyses on the identity operator. The new claim is the full positive-scalar \(\alpha\)-dependent phase diagram and its joint reflection/step tuning consequence.

## Proof

Put
\[
A=1-(1+\alpha)t,
\qquad
B=\alpha t.
\]
The recurrence is
\[
x_{k+1}=Ax_k+Bx_{k-1},
\]
so the characteristic polynomial is
\[
p(r)=r^2-Ar-B.
\]
Since \(B>0\), the two characteristic roots are real and have opposite signs.

For a real monic quadratic of this form, the Jury conditions are
\[
1-A-B>0,
\qquad
1+A-B>0,
\qquad
1+B>0.
\]
Here they simplify exactly to
\[
t>0,
\qquad
2-(1+2\alpha)t>0,
\qquad
1+\alpha t>0.
\]
Thus Schur stability is equivalent to
\[
0<t<\frac{2}{1+2\alpha}.
\]

At the finite boundary
\[
t_b=\frac{2}{1+2\alpha},
\]
one has
\[
p(-1)=0,
\]
and the other root is
\[
r_2=\alpha t_b=\frac{2\alpha}{1+2\alpha}\in(0,1).
\]
Hence the boundary is nonconvergent for generic initial data.

For the source initialization \(x_{-1}=x_0\), the first update satisfies
\[
x_1=(1-t)x_0.
\]
The number \(1-t\) is never a characteristic root at a positive step because
\[
p(1-t)=-\alpha t^2\ne0.
\]
Therefore neither characteristic mode is canceled when \(x_0\ne0\). At the boundary the coefficient of the \(-1\) mode is nonzero, and above the boundary the negative root has modulus greater than one with a nonzero coefficient. This proves the stated if-and-only-if convergence result for the source initialization.

The two roots are
\[
r_\pm
=
\frac{A\pm\sqrt{A^2+4B}}2.
\]
Because they have opposite signs, the spectral factor is
\[
q(t,\alpha)
=
\max\{r_+,-r_-\}
=
\frac{\sqrt{A^2+4B}+|A|}{2}.
\]

The sign of \(A\) changes exactly at
\[
t_\star=\frac{1}{1+\alpha}.
\]
This point lies strictly below the stability boundary because
\[
\frac{2}{1+2\alpha}-\frac{1}{1+\alpha}
=
\frac{1}{(1+\alpha)(1+2\alpha)}>0.
\]

When \(A\ge0\), the dominant root is \(q=r_+\) and
\[
q^2-Aq-B=0.
\]
Differentiation gives
\[
q'
=
\frac{\alpha-(1+\alpha)q}{2q-A}.
\]
On this branch,
\[
q\ge q(t_\star,\alpha)
=
\sqrt{\frac{\alpha}{1+\alpha}}
>
\frac{\alpha}{1+\alpha},
\]
so \(q'<0\).

When \(A\le0\), the dominant modulus satisfies
\[
q^2+Aq-B=0,
\]
and hence
\[
q'
=
\frac{\alpha+(1+\alpha)q}{2q+A}>0.
\]
Thus \(q\) decreases strictly before \(t_\star\) and increases strictly afterwards. At \(t_\star\), \(A=0\) and
\[
q_\star^2=B(t_\star)
=
\frac{\alpha}{1+\alpha}.
\]

Finally,
\[
t_{\mathrm{stab}}(\alpha)=\frac{2}{1+2\alpha}
\]
is strictly decreasing in \(\alpha\), while
\[
q_\star(\alpha)=\sqrt{\frac{\alpha}{1+\alpha}}
\]
is strictly increasing. Their endpoint limits give the final tuning statement.

## Verification

The standalone script `artifacts/verify_generalized_frb_scalar.py` checks the exact Jury identities and boundary factorization in rational arithmetic. It then evaluates characteristic roots for representative reflection coefficients on both sides of the stability boundary and verifies that the predicted \(t_\star\) beats nearby steps.

The finite replay is a consistency check only. The quantified statement follows from the exact Jury and derivative arguments above.

## Relationship to prior work

Ou, Themelis, and Latafat introduce exactly the constant-reflection family analyzed here. Their full preprint proves that the reflection coefficient range \(\alpha>1/2\) is tight for general monotone problems and gives a sufficient constant-step coefficient \(c(\alpha)\). Their sharp coefficient obstruction is a skew-symmetric two-dimensional example, and their displayed generic safety coefficient is maximized at \(\alpha=2\). The full text does not state the positive-scalar phase diagram or the exact rate-optimal step above.

A close published database result studies the same constant-reflection parameter on a split-skew family and finds a different robust max-min coefficient, \((1+\sqrt3)/4\). That result is an exact skew-resolvent obstruction and does not imply the positive scalar recurrence here. Another close result gives the conditioning-dependent sharp threshold for standard reflected gradient, but fixes the reflection coefficient at its classical value and therefore recovers only the \(\alpha=1\) slice.

Soe, Vetrivel, and Yao analyze a different generalized FRB that contains an additional older operator value. Their full preprint explicitly studies \(B=I\) and records the standard FRB rate near \(1/\sqrt2\), then obtains faster specially initialized trajectories by tuning a third-order recurrence. That method and its rate construction do not imply the two-step constant-reflection \(\alpha\)-phase diagram here.

Malitsky and Tam's forward-reflected-backward splitting is the classical \(\alpha=1\) member. The present finding therefore does not claim novelty for the standard identity-operator calculation by itself; its content is the exact dependence on the newly variable reflection coefficient and the resulting reversal of the tuning preference between coercive and skew-dominated geometry.

## Limitations

The result is an exact modal calculation for \(F(x)=ax\). It does not prove that choosing \(\alpha\) close to \(1/2\) is robustly best on a general strongly monotone operator, and it does not contradict the source's generic monotone Lyapunov analysis.

Multidimensional normal positive-definite operators reduce modewise, but a single step must then balance a spectral interval; nonnormal, nonlinear, constrained, or composite operators can behave differently. Adaptive reflection and adaptive steps are also outside the claim.

Older optimistic-gradient and inertial-splitting literature is extensive. Although targeted searches and the closest full texts did not reveal the same positive-scalar parameterized law, an equivalent elementary calculation under different terminology remains the principal residual originality risk.

## References

1. H. Ou, A. Themelis, P. Latafat, *An Adaptive Linesearch-free Method for Monotone Variational Inequalities under Local Lipschitz Continuity*, arXiv:2609.15936v1, 2026.
2. S. Soe, V. Vetrivel, J.-C. Yao, *On Generalized Forward-Reflected-Backward Method for Monotone Inclusion Problems*, arXiv:2509.02005v2, 2026.
3. Y. Malitsky, M. K. Tam, *A Forward-Backward Splitting Method for Monotone Inclusions Without Cocoercivity*, SIAM Journal on Optimization 30(2), 1451--1472, 2020. DOI: 10.1137/18M1207260.
