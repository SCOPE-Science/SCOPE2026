# Sharp scalar stability and rate-optimal splitting for averaged proximal reflected gradient
## Finding

Let
\[
g(x)=\frac{\mu}{2}x^2,\qquad F(x)=ax,
\qquad a>0,\quad \mu>0,
\]
and apply the fixed-step averaged proximal reflected gradient method
\[
x_{n+1}
=
\frac12x_n+
\frac12\operatorname{Prox}_{\tau g}
\left(x_n-\tau F(2x_n-x_{n-1})\right),
\qquad
x_{-1}=x_0.
\]
The mixed variational inequality has the unique solution \(x_\star=0\).

Define
\[
\gamma=\frac{\mu}{a},
\qquad
t=a\tau.
\]
Then
\[
x_{n+1}=A(t,\gamma)x_n+B(t,\gamma)x_{n-1},
\]
where
\[
A(t,\gamma)
=
\frac{2+(\gamma-2)t}{2(1+\gamma t)},
\qquad
B(t,\gamma)
=
\frac{t}{2(1+\gamma t)}.
\]

For every nonzero source initialization \(x_{-1}=x_0\), the iteration converges to \(0\) exactly in the following region:
\[
0<t<\frac{4}{3(1-\gamma)}
\quad\text{if}\quad
0<\gamma<1,
\]
and
\[
t>0\quad\text{arbitrary and finite}
\quad\text{if}\quad
\gamma\ge1.
\]
Equivalently, for \(0<\mu<a\),
\[
0<\tau<\frac{4}{3(a-\mu)},
\]
whereas for \(\mu\ge a\) every finite \(\tau>0\) is stable.

The exact asymptotic root factor is
\[
q(t,\gamma)
=
\frac{\sqrt{A(t,\gamma)^2+4B(t,\gamma)}
+
|A(t,\gamma)|}{2}.
\]
If
\[
0<\gamma<2,
\]
this factor has the unique global minimizer
\[
t_\star=\frac{2}{2-\gamma},
\qquad
q_\star=\frac1{\sqrt{\gamma+2}}.
\]
In the original parameters,
\[
\tau_\star=\frac{2}{2a-\mu},
\qquad
q_\star=\sqrt{\frac{a}{2a+\mu}}.
\]

If
\[
\gamma\ge2,
\]
then \(q(t,\gamma)\) is strictly decreasing for every finite \(t>0\), with
\[
\inf_{t>0}q(t,\gamma)
=
\lim_{t\to\infty}q(t,\gamma)
=
\frac12.
\]
The infimum is not attained at any finite step.

Thus the proximal quadratic curvature produces an exact stability and rate phase diagram that is much larger than the source paper's generic condition \(t<1\): any positive proximal curvature increases the scalar stable range, \(\mu\ge a\) removes the finite stability ceiling entirely, and for \(0<\mu<2a\) the exact fastest step lies strictly beyond the generic \(1/a\) bound.

## Assumptions and scope

The statement is one-dimensional, deterministic, fixed-step, and exact-arithmetic. The smooth forward operator is \(F(x)=ax\) with Lipschitz constant \(a\), and the proximal term is the strongly convex quadratic \(g(x)=\mu x^2/2\). The source algorithm initializes \(x_{-1}=x_0\), and that initialization is retained.

The result concerns averaged proximal reflected gradient itself. It is not a theorem for ordinary proximal reflected gradient, forward-reflected-backward splitting, projected reflected gradient, adaptive aPRG, nonlinear monotone operators, variable steps, or stochastic errors.

The limiting case \(\mu=0\) is excluded from the originality claim. In that case the method reduces, after the change of variables recorded in the source paper, to Popov's algorithm with half the aPRG step; the scalar stability endpoint then reduces to the known reflected-gradient value.

## Proof

Because
\[
\operatorname{Prox}_{\tau g}(v)
=
\frac{v}{1+\tau\mu},
\]
the update becomes
\[
x_{n+1}
=
\frac12x_n+
\frac{x_n-\tau a(2x_n-x_{n-1})}
{2(1+\tau\mu)}.
\]
Substituting \(t=a\tau\) and \(\gamma=\mu/a\) gives
\[
x_{n+1}=Ax_n+Bx_{n-1},
\]
with
\[
A=\frac{2+(\gamma-2)t}{2(1+\gamma t)},
\qquad
B=\frac{t}{2(1+\gamma t)}.
\]

The characteristic polynomial is
\[
p(r)=r^2-Ar-B.
\]
Since \(B>0\), its two real roots have opposite signs. The Jury conditions for a real monic quadratic \(r^2-Ar-B\) are
\[
1-A-B>0,\qquad
1+A-B>0,\qquad
1+B>0.
\]
Here
\[
1-A-B
=
\frac{(\gamma+1)t}{2(1+\gamma t)}>0
\]
and
\[
1+A-B
=
\frac{4+3(\gamma-1)t}{2(1+\gamma t)}.
\]
The third condition is automatic. Therefore Schur stability is equivalent to
\[
4+3(\gamma-1)t>0.
\]
This gives
\[
t<\frac4{3(1-\gamma)}
\]
when \(0<\gamma<1\), and no finite upper bound when \(\gamma\ge1\).

At the finite boundary,
\[
p(-1)=1+A-B=0,
\]
so \(-1\) is a characteristic root. The other root is
\[
B=\frac{2}{\gamma+3}\in(0,1).
\]
For \(x_0\ne0\), the prescribed initialization has a nonzero coefficient on the \(-1\) mode. Indeed, using \(x_1=(A+B)x_0\), that coefficient is proportional to
\[
B-(A+B)=1-B\ne0
\]
after the boundary identity \(A=B-1\) is used. Hence the boundary is genuinely nonconvergent for the source initialization. Above the boundary, the negative root has modulus larger than one. The unstable coefficient cannot vanish: if the stable root were \(r_s\), vanishing of the unstable coefficient would require \(A+B=r_s\), but
\[
A+B-r_s=r_u(1-r_s)\ne0,
\]
because the unstable root \(r_u\ne0\) and \(r_s\ne1\), the latter following from
\[
p(1)=1-A-B>0.
\]

Since the roots have opposite signs, the spectral factor is
\[
q(t,\gamma)
=
\frac{\sqrt{A^2+4B}+|A|}{2}.
\]

Suppose first that \(0<\gamma<2\). Then \(A\) changes sign exactly once, at
\[
t_\star=\frac2{2-\gamma}.
\]
This point lies strictly inside the stable interval when \(0<\gamma<1\), because
\[
\frac4{3(1-\gamma)}
-
\frac2{2-\gamma}
=
\frac{2(\gamma+1)}
{3(2-\gamma)(1-\gamma)}
>0.
\]

For \(A\ge0\), \(q\) is the positive characteristic root and satisfies
\[
q^2-Aq-B=0.
\]
Differentiating,
\[
q'
=
\frac{A'q+B'}{2q-A},
\]
where
\[
A'=-\frac{\gamma+2}{2(1+\gamma t)^2},
\qquad
B'=\frac1{2(1+\gamma t)^2}.
\]
Thus
\[
\operatorname{sgn}(q')
=
\operatorname{sgn}\bigl(1-(\gamma+2)q\bigr).
\]
On the \(A\ge0\) branch,
\[
q\ge q(t_\star,\gamma)=\frac1{\sqrt{\gamma+2}}
>
\frac1{\gamma+2},
\]
so \(q'<0\).

For \(A\le0\), the dominant root is negative in sign and its modulus satisfies
\[
q^2+Aq-B=0.
\]
Hence
\[
q'
=
\frac{B'-A'q}{2q+A}>0.
\]
Therefore \(q\) decreases strictly up to \(t_\star\) and increases strictly afterwards. At \(t_\star\), \(A=0\), so
\[
q_\star^2=B(t_\star,\gamma)=\frac1{\gamma+2}.
\]

Finally suppose \(\gamma\ge2\). Then \(A>0\) for every finite \(t>0\). The same derivative formula gives \(q'<0\); moreover,
\[
\lim_{t\to\infty}A
=
\frac{\gamma-2}{2\gamma},
\qquad
\lim_{t\to\infty}B
=
\frac1{2\gamma},
\]
and direct substitution into the positive-root formula gives
\[
\lim_{t\to\infty}q(t,\gamma)=\frac12.
\]
This completes the phase diagram.

## Verification

The standalone script `artifacts/verify_aprg_scalar_split.py` checks the recurrence coefficients, the exact Jury expressions, the finite stability boundary, the rate-optimal step for several rational split ratios, and the supercritical large-step limit. It also directly compares characteristic-root moduli on both sides of the predicted rate optimum.

The script is a finite consistency check. The quantified result follows from the algebraic Jury and derivative arguments above.

## Relationship to prior work

Chang, Li, and Yang introduce averaged proximal reflected gradient and prove global convergence for the fixed-step method under the generic condition
\[
0<\tau<\frac1{L_F}.
\]
Their paper treats general monotone locally Lipschitz operators and convex proximal terms and proves an ergodic sublinear rate. It does not state a strongly convex quadratic scalar stability phase diagram or an exact rate-optimal fixed step.

The same paper records that when \(g=0\), aPRG is exactly Popov's algorithm with step \(\tau/2\). Accordingly, the zero-proximal-curvature slice is not claimed as new here.

Malitsky's projected reflected gradient work proves convergence, including linear convergence under strong monotonicity, for a different unaveraged projected method. Malitsky and Tam's forward-reflected-backward method applies a resolvent to a different reflected-forward recurrence. General linear-convergence results for those methods do not imply the exact coefficients above for aPRG with a strongly convex proximal quadratic.

Three close database records were inspected at statement level. One gives the sharp strongly monotone stability threshold for unaveraged affine reflected gradient; two others analyze forward-reflected-backward on split-skew rotation families, including exact reflection tuning and rate-optimal steps. Their recurrences contain either no proximal quadratic averaging or a skew resolvent and therefore do not imply the symmetric split phase diagram here.

A useful contrast is that the source's generic \(t<1\) guarantee depends only on the forward Lipschitz constant \(a\). The exact calculation shows that proximal curvature \(\mu\) fundamentally changes both stability and rate: once \(\mu\ge a\), every finite step is stable, while the fastest finite step for \(0<\mu<2a\) is
\[
\tau_\star=\frac2{2a-\mu},
\]
which is strictly larger than \(1/a\).

## Limitations

The result is exact only for the scalar symmetric split \(F(x)=ax\), \(g(x)=\mu x^2/2\). It does not establish enlarged steps for arbitrary nonlinear, nonnormal, constrained, or multidimensional problems. In several dimensions with noncommuting forward and proximal curvature operators, modal decoupling can fail.

For \(\mu\ge2a\), the asymptotic factor approaches \(1/2\) only in the limit \(\tau\to\infty\); no finite rate-optimal step exists. The analysis concerns asymptotic root factors, not finite-horizon transient constants or floating-point effects.

## References

1. X. Chang, J. Li, J. Yang, *Averaged proximal reflected gradient method for monotone variational inequalities*, arXiv:2609.06409v1, 2026.
2. Y. Malitsky, *Projected Reflected Gradient Methods for Monotone Variational Inequalities*, SIAM Journal on Optimization 25(1), 502--520, 2015. DOI: 10.1137/14097238X.
3. Y. Malitsky, M. K. Tam, *A Forward-Backward Splitting Method for Monotone Inclusions Without Cocoercivity*, SIAM Journal on Optimization 30(2), 1451--1472, 2020. DOI: 10.1137/18M1207260.
