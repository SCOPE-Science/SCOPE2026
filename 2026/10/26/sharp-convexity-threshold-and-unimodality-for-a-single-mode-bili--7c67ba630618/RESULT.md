# Sharp convexity threshold and unimodality for a single-mode bilinear-control benchmark

## Finding

Consider a normalized eigenfunction \(\phi\) of a positive self-adjoint fractional elliptic operator with eigenvalue \(\kappa>0\). Restrict the coefficient control to constants \(c\in[a,b]\), where \(0<a<b\), and choose source and target aligned with \(\phi\), with positive amplitudes \(F,D>0\). The state is then \(y(c)=F(\kappa+c)^{-1}\phi\), and the reduced objective is

\[
j(c)=\frac12\left(\frac{F}{\kappa+c}-D\right)^2+\frac{\lambda}{2}c^2,\qquad c\in[a,b],\quad \lambda>0.
\]

Put \(t_a=\kappa+a\), \(t_b=\kappa+b\), and let

\[
t_* = \min\!\left\{t_b,\max\!\left\{t_a,\frac{2F}{D}\right\}\right\},\qquad
q(t)=\frac{2FDt-3F^2}{t^4},\qquad
\lambda_c=\max\{0,q(t_*)\}.
\]

Then \(j\) is strictly convex on \([a,b]\) if and only if \(\lambda\ge\lambda_c\). For every \(\lambda>0\), including the nonconvex regime \(0<\lambda<\lambda_c\), \(j\) has exactly one global minimizer on \([a,b]\). Thus loss of convexity in this natural single-mode reduction does not create multiple local minima.

## Assumptions and scope

The operator is positive and self-adjoint with an eigenpair \((\kappa,\phi)\), \(\kappa>0\), \(\|\phi\|_{L^2}=1\). The source is \(F\phi\), the desired state is \(D\phi\), and the admissible control is restricted to the constant functions \(c\in[a,b]\) with \(0<a<b\). The objective is the squared state-tracking error plus quadratic control regularization. These assumptions make the state equation diagonal on the chosen mode. The result is a complete statement for this restricted benchmark, not a convexity or uniqueness theorem for spatially varying controls in the full PDE problem.

## Proof

Write \(t=\kappa+c\). The reduced state equation gives \(y(c)=F t^{-1}\phi\), so the objective above follows from normalization of \(\phi\). Direct differentiation gives

\[
j'(c)=\lambda c-\frac{F^2}{t^3}+\frac{FD}{t^2},\qquad
j''(c)=\lambda+\frac{3F^2}{t^4}-\frac{2FD}{t^3}=\lambda-q(t).
\]

For convexity, \(q'(t)=6F(2F-Dt)/t^5\). Hence \(q\) increases up to \(2F/D\) and decreases afterwards; its maximum on \([t_a,t_b]\) is \(q(t_*)\). Therefore \(j''\ge0\) everywhere exactly when \(\lambda\ge q(t_*)\). Since \(\lambda>0\), this is equivalent to \(\lambda\ge\lambda_c\). At equality, \(j''\) can vanish only at the single maximizer of the nonconstant function \(q\), so \(j\) is still strictly convex. If \(\lambda<\lambda_c\), then \(j''(c_*)<0\) at the maximizing point, proving nonconvexity. This proves the sharp threshold.

For uniqueness of the minimizer, whenever \(F-Dt\le0\), the derivative satisfies

\[
j'(c)=\lambda c+\frac{F(Dt-F)}{t^3}>0.
\]

On the remaining interval, where \(F-Dt>0\), define

\[
R(c)=\frac{F(F-Dt)}{c t^3}>0.
\]

There, \(j'(c)=c(\lambda-R(c))\), and logarithmic differentiation yields

\[
\frac{R'(c)}{R(c)}=-\frac{D}{F-Dt}-\frac1c-\frac3t<0.
\]

Thus \(R\) is strictly decreasing wherever it is positive, and it tends to zero at the endpoint \(F-Dt=0\). Consequently \(\lambda-R(c)\) can cross zero at most once, and only from negative to positive. Beyond that endpoint, \(j'\) is positive. The derivative therefore has at most one zero, with a negative-to-positive crossing; if no crossing occurs on \([a,b]\), the objective is strictly monotone there. In all cases there is exactly one global minimizer on the compact interval.

## Verification

The derivative identities and threshold are exact algebraic consequences of the stated objective. The included rational-arithmetic checker evaluates a parameter instance with \(\lambda<\lambda_c\), verifies negative curvature at the maximizing point, and checks opposite derivative signs on either side of the unique minimizer. This finite check illustrates the formulas only; the all-parameter statements follow from the analytic proof above, not from numerical sampling.

## Relationship to prior work

The motivating literature studies the nonconvex PDE-constrained problem \(( -\Delta)^s y+uy=f\), pointwise control bounds, first- and second-order optimality conditions, and a posteriori error estimators. The present claim restricts that model to constant controls and data aligned with one eigenfunction, where the state is explicit. The inspected papers provide the general control framework and local second-order conditions, but do not state the exact global convexity threshold \(\lambda_c\) together with the all-regularization unimodality result. The general local sufficient conditions do not by themselves imply this global classification. No claim is made about the full spatially varying control problem.

## Limitations

The theorem requires positive amplitudes \(F,D\), positive eigenvalue \(\kappa\), a strictly positive control interval, a single eigenmode, and quadratic regularization. It does not classify mixed-mode data, sign-changing amplitudes, nonconstant controls, or the full PDE reduced objective. The literature search cannot prove global novelty; a notation-different prior treatment of the same one-dimensional threshold remains a residual risk. The rational checker verifies only its stated example.

## References

1. F. Wang, Q. Wang, and Z. Zhou, “Adaptive finite element approximation of bilinear optimal control with fractional Laplacian,” arXiv:2310.05059v1, first submitted 2023-10-08. Model, control constraints, optimality conditions, and a posteriori error analysis.
2. F. Bersetche, F. Fuica, E. Otárola, and D. Quero, “Bilinear optimal control for the fractional Laplacian: analysis and discretization,” arXiv:2301.13058, first submitted 2023-01-30. Related analysis of the same class of bilinear fractional-control problems and second-order optimality conditions.
