# Exact norm and positivity defect of the affine \(L^2\) projector on the cross-polytope boundary

## Finding

For an integer \(d\geq2\), let
\[
B_1^d=\{x\in\mathbb R^d:\|x\|_1\leq 1\},\qquad X_d=\partial B_1^d,
\]
and let \(\mu_d\) be normalized \((d-1)\)-dimensional Hausdorff measure on \(X_d\). Let \(P_d\) be the \(L^2(X_d,\mu_d)\)-orthogonal projection onto the restrictions of affine functions \(x\mapsto a+b\cdot x\). Then
\[
\boxed{\displaystyle \|P_d\|_{L^\infty(\mu_d)\to L^\infty(\mu_d)}
=1+\frac{(d-1)(d+2)}{2d}\left(1-\frac{2}{d(d+1)}\right)^{d-1}.}
\]
For \(d=1\), the boundary is \(\{-1,1\}\), the affine range is the whole two-point function space, and the projector is the identity with norm \(1\) and positivity defect \(0\). For \(d\geq2\), the operator norm is attained at every coordinate vertex \(x=\pm e_i\) of the cross-polytope. The exact worst negative excursion of the projector on inputs satisfying \(0\leq f\leq1\) is
\[
\boxed{\displaystyle \sup_{0\leq f\leq1}\|(-P_df)_+\|_{L^\infty}
=\frac{(d-1)(d+2)}{4d}\left(1-\frac{2}{d(d+1)}\right)^{d-1}.}
\]
In particular, \(\|P_d\|_{\infty\to\infty}=d/2+O(1)\) as \(d\to\infty\). Thus this canonical polyhedral boundary has an exact, dimension-dependent instability constant for affine least-squares approximation.

## Assumptions and scope

The measure is the normalized Euclidean surface measure, not the cone measure, a vertex measure, or a measure supported on selected facets. Every facet of \(X_d\) has the same surface area. The range of \(P_d\) is the \((d+1)\)-dimensional affine-function space (with the evident interpretation in dimension one). The norm is the operator norm on equivalence classes in \(L^\infty(\mu_d)\). No claim is made for higher-degree polynomial projectors, nonuniform facet weights, or other measures on the same boundary.

## Proof

Assume first \(d\geq2\). Under \(\mu_d\), a random point \(Y\) can be represented as
\[
Y=(\varepsilon_1U_1,\ldots,\varepsilon_dU_d),
\]
where the signs \(\varepsilon_i\) are independent uniform signs and \(U=(U_1,\ldots,U_d)\) is uniform on the simplex \(u_i\geq0,\ \sum_i u_i=1\), independently of the signs. This follows by partitioning the boundary into its \(2^d\) congruent simplex facets. The Dirichlet moments give
\[
\mathbb E Y_i=0,\qquad \mathbb E(Y_iY_j)=0\ (i\ne j),\qquad
\mathbb E Y_i^2=\frac{2}{d(d+1)}.
\]
Consequently the affine Gram matrix is diagonal, and the projection has kernel
\[
K_d(x,y)=1+c_d\,x\cdot y,\qquad c_d=\frac{d(d+1)}2,
\]
so \(P_df(x)=\int_{X_d}K_d(x,y)f(y)\,d\mu_d(y)\).

The \(L^\infty\) norm is \(\sup_{x\in X_d}\Phi_d(x)\), where
\[
\Phi_d(x)=\mathbb E|1+c_d\,x\cdot Y|.
\]
For a continuous kernel on this compact full-support measure space, the operator norm is the supremum of these row integrals: the upper bound is immediate, and choosing the sign of a maximizing row gives equality (continuity makes the pointwise value contribute to the essential supremum). The function \(\Phi_d\) is convex in \(x\). Since \(B_1^d\) is the convex hull of its vertices \(\{\pm e_i\}\), convexity implies that its maximum on \(B_1^d\), and hence on its boundary, is attained at a vertex. Signed-permutation symmetry makes all these vertex values equal.

At \(x=e_1\), write \(Y_1=\varepsilon U_1\). The marginal \(U_1\) has density \((d-1)(1-u)^{d-2}\) on \([0,1]\). Averaging over the sign gives
\[
\mathbb E_{\varepsilon}|1+c_du\varepsilon|=\max\{1,c_du\}.
\]
With \(a=1/c_d=2/[d(d+1)]\) and \(q=1-a\), direct integration yields
\[
\begin{aligned}
\Phi_d(e_1)
&=\mathbb P(U_1\leq a)+c_d\,\mathbb E[U_1\mathbf 1_{\{U_1>a\}}]\\
&=1-q^{d-1}+c_d\left(q^{d-1}-\frac{d-1}{d}q^d\right)\\
&=1+\frac{(d-1)(d+2)}{2d}q^{d-1}.
\end{aligned}
\]
This proves the norm formula for \(d\geq2\). For \(d=1\), the affine range is all functions on the two-point boundary, so \(P_1\) is the identity with norm one.

Finally, \(\int K_d(x,y)\,d\mu_d(y)=1\). For any fixed \(x\), the largest possible value of \(-P_df(x)\) over \(0\leq f\leq1\) is the negative mass \(\int (K_d(x,y))_-\,d\mu_d(y)\), attained by the indicator of the negative-kernel region. If a row kernel has integral one, its negative mass is half its \(L^1\) norm minus one. Maximizing over \(x\) therefore gives the stated positivity defect, and the maximizing evaluation points are the coordinate vertices. The asymptotic \(d/2+O(1)\) follows directly from the exact formula and \((1-2/[d(d+1)])^{d-1}=1+O(1/d)\).

## Verification

The proof uses only the Dirichlet first and second moments, convexity, and an elementary one-variable integral. The accompanying `verification.py` checks the algebraic equivalence of the integral and simplified expressions with exact rational arithmetic for dimensions \(2\) through \(100\), and checks the dimension-one value separately. This finite check is a reproducibility aid; the proof above establishes the formula for every integer dimension.

## Relationship to prior work

Hangelbroek, Narcowich, Sun, and Ward study \(L^\infty\)-stability of \(L^2\) least-squares projectors for kernel-generated spaces on compact smooth manifolds. That work motivates exact projector-norm questions but does not cover the affine polynomial space on the Hausdorff-measured boundary of the cross-polytope. The closest related simplex calculation uses uniform volume measure on a simplex interior; it has a different Gram matrix and a different distribution of the evaluation kernel. Results about nearest-point projection onto a cross-polytope likewise concern a nonlinear metric projection, not this linear orthogonal projector. None of these statements implies the formula above.

## Limitations

The calculation depends on uniform Hausdorff surface measure and signed-permutation symmetry. It does not determine the norm for nonuniform facet weights, cone measure, higher-degree polynomial spaces, or other polytopes. The literature comparison is best-knowledge rather than a proof that no unindexed equivalent exists; independent mathematical and bibliographic audits have not been performed.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, “Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector,” arXiv:1005.2424, first publicly posted 2010-05-13; SIAM Journal on Mathematical Analysis 43 (2011), 662–684, DOI: 10.1137/100795334. The relevant discussion is the general \(L_\infty\)-stability problem for \(L^2\) projectors (Sections 1 and 4–5); it is contextual, not a source for the formula proved here.
