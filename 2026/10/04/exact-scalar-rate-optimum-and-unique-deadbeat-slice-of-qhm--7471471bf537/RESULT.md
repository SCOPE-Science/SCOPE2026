# Exact scalar rate optimum and unique deadbeat slice of QHM
## Finding

Consider deterministic quasi-hyperbolic momentum (QHM) on the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0.
\]
Use the normalized momentum convention of the defining QHM paper:
\[
g_{t+1}=\beta g_t+(1-\beta)\lambda x_t,
\]
\[
x_{t+1}
=
x_t-\alpha\left[(1-\nu)\lambda x_t+\nu g_{t+1}\right],
\]
with
\[
0<\beta<1,\qquad 0\le\nu\le1,\qquad \alpha>0.
\]
Put
\[
s=\alpha\lambda.
\]

The exact Schur-stable interval is
\[
0<s<
\frac{2(1+\beta)}{1+\beta-2\beta\nu}.
\]

More sharply, the best scalar asymptotic state factor over the stepsize can be written in closed form.

For
\[
0<\nu<1,
\]
the full two-state spectral radius is uniquely minimized at
\[
s_\star
=
\frac{1-\beta}{\left(1-\sqrt{\beta\nu}\right)^2},
\]
and the exact minimum is
\[
\rho_\star
=
\frac{\left|\beta-\sqrt{\beta\nu}\right|}
{1-\sqrt{\beta\nu}}.
\]

At the two endpoint immediate discounts, the minimizer becomes a plateau. If
\[
\nu=0,
\]
then
\[
\rho_{\min}=\beta
\]
for every
\[
1-\beta\le s\le1+\beta.
\]
If
\[
\nu=1,
\]
then
\[
\rho_{\min}=\sqrt{\beta}
\]
for every
\[
\frac{1-\sqrt{\beta}}{1+\sqrt{\beta}}
\le s\le
\frac{1+\sqrt{\beta}}{1-\sqrt{\beta}}.
\]

The interior formula has a unique zero:
\[
\rho_\star=0
\quad\Longleftrightarrow\quad
\nu=\beta.
\]
The defining QHM paper identifies this slice with Nesterov momentum. On that slice,
\[
s_\star=\frac{1}{1-\beta},
\]
and the complete two-state iteration matrix satisfies
\[
M^2=0.
\]
Hence every scalar initial state, including an arbitrary initial momentum buffer, is annihilated in at most two updates.

This gives a deterministic interpretation of QHM's immediate-discount parameter that is distinct from its original variance-versus-staleness motivation: for a single curvature mode, \(\nu\) moves the exact critical-damping rate floor, and the Nesterov slice \(\nu=\beta\) is the unique nondegenerate QHM interpolation with deadbeat scalar dynamics.

## Assumptions and scope

The objective is a deterministic one-dimensional positive quadratic. The theorem uses the normalized momentum buffer of the QHM paper and a constant learning rate.

The state whose spectral radius is optimized is the full pair \((x_t,g_t/\lambda)\), not the parameter coordinate alone. This matters at \(\nu=0\), where the parameter step reduces to gradient descent but the unused momentum buffer still decays at rate \(\beta\).

The finding is scalar. It does not claim that a single stepsize can annihilate every mode of a nontrivial spectral interval, nor that the scalar rate optimum is the minimax optimum on a general SPD quadratic.

The general stability inequality is included for completeness. A 2024 two-step momentum paper gives an equivalent stability condition after a parameter change; the novelty-bearing part here is the exact QHM scalar rate landscape and the unique deadbeat slice.

## Proof

Scale the momentum state by
\[
h_t=\frac{g_t}{\lambda}.
\]
Then
\[
\begin{bmatrix}
x_{t+1}\\
h_{t+1}
\end{bmatrix}
=
M(s)
\begin{bmatrix}
x_t\\
h_t
\end{bmatrix},
\]
where
\[
M(s)=
\begin{bmatrix}
1-s(1-\nu\beta)&-s\nu\beta\\
1-\beta&\beta
\end{bmatrix}.
\]
Its characteristic polynomial is
\[
p_s(z)=z^2-T(s)z+D(s),
\]
with
\[
T(s)=1+\beta-s(1-\nu\beta),
\]
and
\[
D(s)=\beta\left[1-s(1-\nu)\right].
\]

For a monic real quadratic \(z^2-Tz+D\), the second-order Jury conditions are
\[
1-D>0,\qquad
1-T+D>0,\qquad
1+T+D>0.
\]
Here they become
\[
1-\beta+\beta s(1-\nu)>0,
\]
\[
s(1-\beta)>0,
\]
and
\[
2(1+\beta)-s(1+\beta-2\beta\nu)>0.
\]
Because
\[
1+\beta-2\beta\nu\ge1-\beta>0,
\]
the exact stable interval follows.

Now assume
\[
0<\nu<1
\]
and put
\[
\tau=\sqrt{\beta\nu}.
\]
The discriminant
\[
\Delta(s)=T(s)^2-4D(s)
\]
vanishes at exactly two positive steps:
\[
s_-=\frac{1-\beta}{(1+\tau)^2},
\qquad
s_+=\frac{1-\beta}{(1-\tau)^2}.
\]
The corresponding repeated roots are
\[
r_-=\frac{\beta+\tau}{1+\tau},
\qquad
r_+=\frac{\beta-\tau}{1-\tau}.
\]
Between \(s_-\) and \(s_+\), the roots are a complex-conjugate pair. Since
\[
D(s)=\beta[1-s(1-\nu)]
\]
strictly decreases with \(s\), their common modulus
\[
\sqrt{D(s)}
\]
strictly decreases across that interval. Therefore the smallest modulus within the complex-root regime occurs at \(s_+\), with value
\[
|r_+|
=
\frac{|\beta-\tau|}{1-\tau}.
\]

It remains to show that no step outside the complex-root interval is better. For
\[
s<s_+,
\]
one has
\[
D(s)>D(s_+)=r_+^2,
\]
so the root-product bound implies
\[
\rho(M(s))>|r_+|.
\]

For
\[
s>s_+,
\]
set
\[
R=|r_+|.
\]
If \(\nu<\beta\), then \(r_+=R>0\). A necessary Jury inequality for both roots to lie in the closed disk of radius \(R\) is
\[
R^2-RT(s)+D(s)\ge0.
\]
It is exactly zero at \(s=s_+\), while its derivative is
\[
R(1-\beta\nu)-\beta(1-\nu)
=
-(1-\beta)\sqrt{\beta\nu}<0.
\]
Hence it fails for every \(s>s_+\).

If \(\nu>\beta\), then \(r_+=-R\). The corresponding necessary inequality is
\[
R^2+RT(s)+D(s)\ge0.
\]
It is again zero at \(s=s_+\), and its derivative is
\[
-R(1-\beta\nu)-\beta(1-\nu)<0.
\]
Thus it also fails immediately and forever to the right. This proves uniqueness of the optimum for \(0<\nu<1\).

When
\[
\nu=0,
\]
the matrix is triangular with eigenvalues
\[
1-s,\qquad \beta,
\]
which gives the stated plateau.

When
\[
\nu=1,
\]
the determinant is the constant \(\beta\), so
\[
\rho(M(s))\ge\sqrt{\beta}.
\]
Equality holds exactly when the active roots are complex or repeated, which is equivalent to the displayed interval.

Finally, for \(0<\nu<1\),
\[
\rho_\star=0
\]
if and only if
\[
\beta=\sqrt{\beta\nu},
\]
which, because \(\beta>0\), is equivalent to
\[
\nu=\beta.
\]
At that parameter value,
\[
s_\star=\frac{1}{1-\beta},
\]
and both the trace and determinant vanish. Hence
\[
p_{s_\star}(z)=z^2.
\]
By the Cayley-Hamilton theorem,
\[
M(s_\star)^2=0,
\]
proving two-step annihilation of every initial state.

## Verification

The accompanying `verify.py` reconstructs the exact QHM state matrix, checks the Jury boundary, derives the two discriminant roots, compares the closed-form optimum against dense deterministic searches, verifies both endpoint plateaus, and checks the nilpotent Nesterov slice in exact rational arithmetic.

The numerical searches are not used as proofs of global optimality. The product bound, discriminant analysis, and scaled Jury inequalities above provide the exhaustive argument.

## Relationship to prior work

Ma and Yarats introduced QHM as a weighted average of normalized momentum and plain SGD, with \(\beta\) controlling historical discount and \(\nu\) controlling immediate discount. They explicitly identify \(\nu=\beta\) with Nesterov momentum, connect QHM to a broad family of two-state methods, and give a linear-operator representation of the optimizer. Their inspected full text does not optimize the exact scalar quadratic spectral radius over the learning rate and does not state the unique deadbeat property.

Krivovichev and Sergeeva analyze a different-looking two-step gradient method with two momentum parameters. Its quadratic characteristic polynomial becomes exactly the QHM scalar polynomial under
\[
h=\alpha(1-\beta),
\]
\[
\beta_1=\beta,
\]
and
\[
\beta_2=\frac{\beta(1-\nu)}{1-\beta}.
\]
Their convergence condition therefore recovers the stability interval stated here. That stability clause is not claimed as new. Their paper studies interval convergence and parameter optimization for its own parameterization; the inspected text does not give the QHM fixed-\((\beta,\nu)\) scalar rate minimum, the closed form
\[
\frac{|\beta-\sqrt{\beta\nu}|}{1-\sqrt{\beta\nu}},
\]
or the unique nilpotent slice.

Targeted database and web searches for QHM scalar quadratics, spectral radii, repeated roots, finite-time annihilation, and Nesterov deadbeat behavior did not identify the complete rate-optimal statement above.

## Limitations

The result is exact only for a single deterministic curvature mode. On an SPD quadratic with more than one distinct eigenvalue, one learning rate generally cannot place all modes at their individual scalar optima.

The theorem optimizes asymptotic spectral radius, not transient norm amplification.

The two-step nilpotence at \(\nu=\beta\) requires exact knowledge of the scalar curvature through
\[
\alpha\lambda=\frac{1}{1-\beta}.
\]
It is therefore a structural benchmark rather than a curvature-free practical tuning rule.

The result uses constant \(\beta\), \(\nu\), and \(\alpha\). Stochastic gradients, schedules, and adaptive second moments are outside scope.

An equivalent critical-damping calculation may exist under a different two-state momentum parameterization; the 2024 comparison above is the closest inspected source.

## References

1. Jerry Ma and Denis Yarats, “Quasi-hyperbolic momentum and Adam for deep learning,” arXiv:1810.06801v1, 2018.
2. Gerasim V. Krivovichev and Valentina Yu. Sergeeva, “Analysis of a Two-Step Gradient Method with Two Momentum Parameters for Strongly Convex Unconstrained Optimization,” Algorithms 17(3):126, 2024, DOI:10.3390/a17030126.
