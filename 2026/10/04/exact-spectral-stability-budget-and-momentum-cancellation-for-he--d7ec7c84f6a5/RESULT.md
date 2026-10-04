# Exact spectral stability budget and momentum cancellation for Hessian-corrected heavy ball
## Finding

Consider the Hessian-corrected heavy-ball iteration
\[
y_k
=
x_k+\alpha(x_k-x_{k-1})
-\theta\bigl(\nabla h(x_k)-\nabla h(x_{k-1})\bigr),
\]
\[
x_{k+1}=y_k-\beta\nabla h(x_k),
\]
with
\[
0\le\alpha<1,\qquad \theta\ge0,\qquad \beta>0.
\]
Let
\[
h(x)=\frac12x^{\mathsf T}Qx,
\]
where \(Q\succ0\) is symmetric and
\[
\sigma(Q)\subset[\mu,L].
\]

Then the complete linear iteration is Schur stable for every initial pair if and only if
\[
L(\beta+2\theta)<2(1+\alpha).
\]

On a single eigenmode of curvature \(\lambda>0\), define
\[
m=\alpha-\theta\lambda,
\qquad
s=\beta\lambda.
\]
The mode satisfies
\[
u_{k+1}=(1+m-s)u_k-mu_{k-1}.
\]
It is Schur stable exactly when
\[
-1<m<1,
\qquad
0<s<2(1+m).
\]

For any fixed stable \(m\), optimizing over the step variable \(s\) gives the exact best asymptotic root factor
\[
q_{\min}(m)=\sqrt{|m|}.
\]
More precisely, if
\[
0\le m<1,
\]
every
\[
(1-\sqrt m)^2
\le s\le
(1+\sqrt m)^2
\]
is rate-optimal. If
\[
-1<m<0,
\]
the unique optimum is
\[
s=1+m.
\]

The correction therefore acts as an exact curvature-dependent momentum controller. At any selected curvature \(\lambda\), choosing
\[
\theta=\frac{\alpha}{\lambda},
\qquad
\beta=\frac1{\lambda}
\]
gives
\[
m=0,\qquad s=1,
\]
and hence
\[
u_{k+1}=0
\]
for every preceding pair \((u_{k-1},u_k)\). On an isotropic quadratic \(Q=\lambda I\), the whole state is annihilated in one update.

At the same time, the global stability condition shows the precise price of Hessian correction:
\[
\beta+2\theta<\frac{2(1+\alpha)}{L}.
\]
Thus one unit of correction consumes twice as much of the exact stability budget as one unit of ordinary gradient step.

## Assumptions and scope

The statement is deterministic and exact for symmetric positive-definite quadratics. The source algorithm is used with constant parameters. No line search, stochastic gradient, nonquadratic remainder, nonsymmetric linearization, or variable coefficient is present.

The restriction \(0\le\alpha<1\) makes the exact uniform spectral condition especially simple. It contains the source theorem's momentum range. The source paper proves convergence on a substantially broader nonconvex/strongly-quasiconvex class under sufficient parameter inequalities; the present result is a sharp spectral classification only for positive-definite quadratics.

The one-mode cancellation statement does not imply simultaneous one-step convergence on a general nonisotropic quadratic. A single correction coefficient can cancel the effective momentum at only one curvature unless all active eigenvalues coincide.

## Proof

Because
\[
\nabla h(x)=Qx,
\]
an eigenvector component with eigenvalue \(\lambda\) obeys
\[
y_k
=
u_k+\alpha(u_k-u_{k-1})
-\theta\lambda(u_k-u_{k-1}).
\]
With
\[
m=\alpha-\theta\lambda,
\qquad
s=\beta\lambda,
\]
this becomes
\[
u_{k+1}
=
(1+m-s)u_k-mu_{k-1}.
\]
The characteristic polynomial is
\[
p_\lambda(r)
=
r^2-(1+m-s)r+m.
\]

For a real monic quadratic
\[
r^2+a_1r+a_2,
\]
the Jury conditions are
\[
1+a_1+a_2>0,\qquad
1-a_1+a_2>0,\qquad
1-a_2>0.
\]
Here they reduce exactly to
\[
s>0,
\qquad
2+2m-s>0,
\qquad
1-m>0.
\]
Since \(s>0\) and \(s<2(1+m)\) force \(m>-1\), the mode is stable exactly when
\[
-1<m<1,
\qquad
0<s<2(1+m).
\]

Now suppose
\[
\sigma(Q)\subset[\mu,L],
\qquad
0\le\alpha<1.
\]
For every eigenvalue, the upper condition \(m<1\) is automatic because
\[
m=\alpha-\theta\lambda\le\alpha<1.
\]
The remaining nontrivial inequality is
\[
\beta\lambda
<
2(1+\alpha-\theta\lambda),
\]
or equivalently
\[
\lambda(\beta+2\theta)<2(1+\alpha).
\]
The left side is increasing in \(\lambda\), so all modes are stable exactly when
\[
L(\beta+2\theta)<2(1+\alpha).
\]
This inequality also implies
\[
\theta L<1+\alpha,
\]
and hence \(m>-1\) for every mode. This proves the exact global SPD stability criterion.

For the rate calculation, write
\[
A=1+m-s.
\]
The roots satisfy
\[
r_\pm=\frac{A\pm\sqrt{A^2-4m}}2.
\]

If
\[
0<m<1
\]
and
\[
A^2\le4m,
\]
the roots are a conjugate pair whose product is \(m\), so both have modulus
\[
\sqrt m.
\]
No smaller spectral radius is possible because the product of the two root moduli is \(m\). The condition
\[
A^2\le4m
\]
is exactly
\[
(1-\sqrt m)^2
\le s\le
(1+\sqrt m)^2.
\]
These endpoints lie inside the stability interval. The case \(m=0\) reduces to roots \(0\) and \(1-s\), whose unique optimum is \(s=1\).

If
\[
-1<m<0,
\]
the roots are always real and have opposite signs. Their maximal modulus is
\[
q(A)
=
\frac{\sqrt{A^2-4m}+|A|}{2},
\]
which is strictly increasing in \(|A|\). Its unique minimum is therefore at
\[
A=0,
\]
that is,
\[
s=1+m,
\]
where the roots are
\[
\pm\sqrt{-m}.
\]
Thus in every stable case
\[
q_{\min}(m)=\sqrt{|m|}.
\]

Finally, setting
\[
\theta=\frac{\alpha}{\lambda},
\qquad
\beta=\frac1{\lambda}
\]
gives
\[
m=0,\qquad s=1,
\]
so the mode recurrence becomes identically
\[
u_{k+1}=0.
\]

## Verification

The standalone script `artifacts/verify_hessian_corrected_hb.py` checks the modal recurrence, the Jury inequalities, the uniform SPD stability reduction, the optimal-rate formulas on positive and negative effective momentum, and the matched-curvature one-step cancellation.

The script uses exact rational arithmetic for the algebraic identities and floating-point roots only for independent spectral-radius spot checks. Those finite checks are supporting evidence; the all-parameter result follows from the Jury and root-product arguments above.

## Relationship to prior work

Hadjisavvas, Lara, Marcavillaca, and Vuong introduce the heavy-ball Hessian-correction iteration analyzed here. Their convergence theorem treats strongly quasiconvex objectives under sufficient restrictions coupling momentum, Hessian correction, step size, and the gradient Lipschitz constant. The full text does not give an exact quadratic spectral stability region or the curvature-matched cancellation law above.

For positive momentum, the source theorem requires
\[
\theta<\frac{\alpha}{L\sqrt3}.
\]
On the isotropic quadratic with curvature \(L\), exact momentum cancellation requires
\[
\theta=\frac{\alpha}{L}.
\]
Thus the generic sufficient theorem cannot reach the exact cancellation point when \(\alpha>0\). This is not a contradiction: the theorem protects a much broader function class, whereas the present result is an exact quadratic calculation.

Attouch, Chbani, Fadili, and Riahi develop inertial optimization schemes with Hessian-driven damping implemented through gradient differences and derive accelerated convergence properties. Their discrete algorithms and coefficient structure differ from the constant-parameter heavy-ball correction used here. The inspected spectral discussion concerns a different strongly-convex inertial system and does not imply the characteristic polynomial above.

A targeted published-research database comparison found a nearby result on the classical heavy-ball method showing a real-root acceleration barrier over spectral intervals. That result has no Hessian-correction term and therefore corresponds only to a different parameter family; it does not imply the exact budget
\[
L(\beta+2\theta)<2(1+\alpha)
\]
or the matched-curvature momentum cancellation.

## Limitations

The exact uniform criterion relies on a symmetric positive-definite quadratic Hessian. Nonnormal linear systems, nonquadratic objectives, and varying Hessians do not decouple into the scalar modes used in the proof.

The rate-optimal formula is modewise. Tuning the correction to cancel one curvature generally changes the effective momentum on every other curvature, so the result is not a minimax rate theorem over a nontrivial spectral interval.

Older inertial and gradient-difference literature is extensive. Targeted searches and the closest inspected sources did not reveal the same constant-parameter phase diagram, but an equivalent elementary calculation under different notation remains the main historical-originality risk.

## References

1. N. Hadjisavvas, F. Lara, R. T. Marcavillaca, P. T. Vuong, *Heavy Ball and Nesterov Accelerations with Hessian-Driven Damping for Nonconvex Optimization*, arXiv:2506.15632v1, 2025; Applied Mathematics & Optimization 93, 63, 2026, DOI: 10.1007/s00245-026-10406-2.
2. H. Attouch, Z. Chbani, J. Fadili, H. Riahi, *First-order optimization algorithms via inertial systems with Hessian driven damping*, arXiv:1907.10536v2; Mathematical Programming 193, 2022, DOI: 10.1007/s10107-020-01591-1.
