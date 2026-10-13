# Exact soft-threshold bypass and geometric non-identification in proximal nonlinear conjugate gradient
## Finding

Consider Algorithm 3 of Hamana--Narushima on the one-dimensional composite problem
\[
\min_{x\in\mathbb R} h(x),
\qquad
h(x)=\lambda|x|,
\qquad
\lambda>0,
\]
with smooth part
\[
g(x)\equiv0.
\]
The unique minimizer is
\[
x^\star=0.
\]

Fix
\[
\mu_{-1}=\mu>1
\]
and any admissible line-search parameters
\[
\delta\in(0,1),
\qquad
T>\delta,
\qquad
\theta,\bar t,\tau\in(0,1).
\]
If the nonzero initial point satisfies
\[
|x_0|
\le
\frac{\mu\lambda}{\max\{1,T\}},
\]
then every nonstationary iteration has the following exact properties:

\[
x_k^+=0,
\qquad
\eta_k=\frac{x_k}{\mu},
\qquad
d_k=-\eta_k,
\qquad
t_k=1,
\qquad
\alpha_k=1.
\]

Therefore
\[
x_{k+1}
=
\left(1-\frac1\mu\right)x_k,
\]
and hence
\[
x_k
=
\left(1-\frac1\mu\right)^k x_0.
\]

The algorithm thus computes the exact soft-thresholded minimizer
\[
x_k^+=0
\]
at every iteration but does not move to it. Under exact-stationarity stopping, every finite iterate remains nonzero. By contrast, the fallback proximal-gradient branch would set
\[
x_{k+1}=x_k^+=0
\]
in one update.

The geometric factor
\[
q=1-\frac1\mu
\]
can be made arbitrarily close to one by choosing a large admissible \(\mu\). Consequently the nonlinear-conjugate-gradient line-search branch can replace one-step active-set identification by an arbitrarily slow geometric tail.

## Assumptions and scope

The example uses Algorithm 3 for convex \(h\), the exact proximal map, exact arithmetic, and the source three-term Hestenes--Stiefel direction.

The problem is deliberately elementary:
\[
g\equiv0,
\qquad
h(x)=\lambda|x|.
\]
It is a canonical soft-threshold model for the sparsity mechanism that also appears in the paper's LASSO experiments.

The claim concerns the iterate path under exact-stationarity stopping. The source permits practical termination when the forward-backward residual is merely sufficiently small. With any fixed positive tolerance, the geometric sequence eventually meets that tolerance and terminates.

The result does not contradict the paper's global convergence theorem. The sequence converges to the minimizer. The finding is that the line-search branch does not preserve finite identification of the proximal point.

## Proof

Because
\[
g\equiv0,
\]
the source decrease condition for choosing \(\mu_k\) is
\[
0
\le
\frac{1}{2\mu_k}
\|x_k^+-x_k\|^2,
\]
which holds for every positive \(\mu_k\). Since Algorithm 3 selects the largest candidate from the geometric list beginning at the previous parameter,
\[
\mu_k=\mu
\]
for every \(k\).

The proximal point is
\[
x_k^+
=
\operatorname{prox}_{\mu\lambda|\cdot|}(x_k)
=
\operatorname{sign}(x_k)
\max\{|x_k|-\mu\lambda,0\}.
\]
The assumed basin gives
\[
|x_0|\le\mu\lambda.
\]
The recurrence proved below decreases \(|x_k|\), so
\[
|x_k|\le\mu\lambda
\]
for all \(k\). Hence
\[
x_k^+=0
\]
at every iteration.

By the source definition of the forward-backward residual,
\[
\eta_k
=
-\frac1\mu(x_k^+-x_k)
=
\frac{x_k}{\mu}.
\]

At \(k=0\), Algorithm 3 sets
\[
d_0=-\eta_0.
\]
For \(k\ge1\), write the source direction as
\[
d_k
=
-\eta_k+\beta_kd_{k-1}-\gamma_ky_{k-1},
\]
where
\[
\beta_k
=
\frac{\eta_ky_{k-1}}{d_{k-1}z_{k-1}},
\qquad
\gamma_k
=
\frac{\eta_kd_{k-1}}{d_{k-1}z_{k-1}}.
\]
All quantities are scalar. Whenever the source curvature condition makes the denominator well-defined,
\[
\beta_kd_{k-1}
=
\frac{\eta_ky_{k-1}}{z_{k-1}}
=
\gamma_ky_{k-1}.
\]
Thus the two correction terms cancel exactly and
\[
d_k=-\eta_k=-\frac{x_k}{\mu}.
\]

It remains to verify both line-search stages. Since \(\mu>1\),
\[
x_k+d_k
=
\left(1-\frac1\mu\right)x_k
\]
has the same sign as \(x_k\). Therefore the first-stage condition at \(t=1\) is
\[
\lambda|x_k|
\left(1-\frac1\mu\right)
-
\lambda|x_k|
\le
-T\frac{x_k^2}{\mu^2}.
\]
This is equivalent to
\[
|x_k|
\le
\frac{\mu\lambda}{T}.
\]
The initial basin
\[
|x_0|
\le
\frac{\mu\lambda}{\max\{1,T\}}
\]
implies this bound, and the recurrence preserves it. Hence the largest trial value is always
\[
t_k=1.
\]
Because
\[
\bar t<1,
\]
Algorithm 3 enters its Armijo stage.

At \(\alpha=1\), the Armijo inequality becomes
\[
\lambda|x_k|
\left(1-\frac1\mu\right)
\le
\lambda|x_k|
-
\delta\frac{x_k^2}{\mu^2},
\]
which is equivalent to
\[
|x_k|
\le
\frac{\mu\lambda}{\delta}.
\]
Since
\[
\delta<1
\]
and the basin implies
\[
|x_k|\le\mu\lambda,
\]
the full Armijo step is accepted:
\[
\alpha_k=1.
\]

Consequently
\[
x_{k+1}
=
x_k+d_k
=
\left(1-\frac1\mu\right)x_k.
\]
Because
\[
0<1-\frac1\mu<1,
\]
the closed form follows:
\[
x_k
=
\left(1-\frac1\mu\right)^k x_0.
\]
For nonzero \(x_0\), this is nonzero at every finite \(k\), while
\[
x_k\to0.
\]

The source corrected vector is also well-defined on this path. Once the recurrence holds,
\[
s_{k-1}=d_{k-1},
\qquad
y_{k-1}=\frac{d_{k-1}}{\mu},
\]
and
\[
z_{k-1}
=
d_{k-1}
\left(\frac1\mu+\nu_k\right).
\]
Since
\[
\nu_k\ge0,
\]
one has
\[
d_{k-1}z_{k-1}
=
d_{k-1}^2
\left(\frac1\mu+\nu_k\right)
>
0.
\]
Thus no denominator degeneracy is being hidden by the scalar cancellation.

## Verification

The standalone script `artifacts/verify_soft_threshold_tail.py` replays the exact scalar formulas for several rational choices of \(\mu\), \(\lambda\), \(T\), \(\delta\), and admissible correction parameters.

It checks the proximal point, forward-backward residual, exact cancellation of the two Hestenes--Stiefel correction terms, both full-step line-search inequalities, positivity of the corrected denominator, and the geometric recurrence.

The quantified proof is analytic. The finite checks are supporting evidence rather than an exhaustive argument.

## Relationship to prior work

The primary source extends nonlinear conjugate-gradient ideas to composite optimization by replacing the gradient with a forward-backward residual. Its line-search branch updates along a three-term Hestenes--Stiefel direction, while a fallback branch takes the proximal point itself. The paper proves global convergence and includes sparse \(\ell_1\)-regularized experiments such as LASSO.

Finite activity identification of forward-backward methods is established in earlier literature under partial smoothness and nondegeneracy conditions. For the present scalar model, ordinary forward-backward iteration identifies the active manifold
\[
\{0\}
\]
immediately because its first proximal point is already zero.

The classical three-term Hestenes--Stiefel literature establishes sufficient-descent properties for smooth nonlinear conjugate-gradient directions. Those smooth results do not address whether a composite line-search relaxation preserves a proximal active-set hit.

The finding here isolates the interaction of these two structures: the source direction can be perfectly descent-compatible while its accepted relaxed iterate systematically bypasses a proximal point that is already the exact minimizer.

Targeted searches by the primary preprint identifier, forward-backward residual, finite identification, active manifold, soft thresholding, and three-term Hestenes--Stiefel terminology did not locate an equivalent source-specific statement.

## Limitations

The exact recurrence is one-dimensional and uses
\[
g\equiv0.
\]
It is a structural benchmark, not a claim that the source's LASSO experiments exhibit the same tail.

The basin is sufficient for full acceptance of both line-search stages. Outside it, backtracking or the fallback branch can change the trajectory.

A positive practical stopping tolerance terminates the sequence once the residual becomes small enough, so “never identifies” refers to exact stationarity of the iterates, not to endless execution of a tolerance-based implementation.

The result does not classify finite identification for higher-dimensional partly smooth objectives or for the paper's weakly convex extension.

## References

1. S. Hamana, Y. Narushima, *Proximal Nonlinear Conjugate Gradient Methods for Composite Optimization*, arXiv:2604.11150v1, first public 13 April 2026; revised as arXiv:2604.11150v2.
2. J. Liang, J. Fadili, G. Peyré, *Activity Identification and Local Linear Convergence of Forward--Backward-type Methods*, SIAM Journal on Optimization 27(1), 2017. DOI: 10.1137/16M106340X.
3. L. Zhang, W. Zhou, D.-H. Li, *Some descent three-term conjugate gradient methods and their global convergence*, Optimization Methods and Software 22(4), 2007. DOI: 10.1080/10556780701223293.
