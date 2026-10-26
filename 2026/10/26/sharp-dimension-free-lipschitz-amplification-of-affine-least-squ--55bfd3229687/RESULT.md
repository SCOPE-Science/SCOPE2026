# Sharp dimension-free Lipschitz amplification of affine least-squares projections on cubes

## Finding
Let \(Q_d=[-1,1]^d\) carry uniform probability measure and the metric \(\rho_\infty(x,y)=\max_i|x_i-y_i|\). The canonical \(L^2\)-orthogonal projection \(P_d\) onto affine polynomials is uniformly bounded as an operator on real Lipschitz seminorms. Write
\[A_d=\sup_{\operatorname{Lip}_\infty(f)\le1}\operatorname{Lip}_\infty(P_df).\]
For every positive odd integer \(d\),
\[\frac32\left(1-\frac1{d+2}\right)\le A_d\le\frac32\left(1-\frac2{(d+1)(d+2)}\right).\]
For every positive even integer \(d\),
\[\frac32\left(1-\frac1{d+1}\right)\le A_d\le\frac32\left(1-\frac2{(d+1)(d+2)}\right).\]
In particular, the smallest dimension-free constant is exactly \(3/2\):
\[\sup_{d\ge1}A_d=\lim_{d\to\infty}A_d=\frac32,\qquad A_d<\frac32\text{ for each finite }d.\]
For \(d=3\), the explicit median input shows \(A_3\ge6/5>1\). Thus the projection is uniformly Lipschitz stable while it need not be nonexpansive.

## Assumptions and scope
Each \(d\) is a positive integer. Functions are real-valued and Lipschitz on the closed cube for the maximum-coordinate metric. The measure is normalized product Lebesgue measure. This is the canonical orthogonal projection in \(L^2(Q_d)\) onto \(\operatorname{span}\{1,x_1,\ldots,x_d\}\), acting on continuous Lipschitz inputs. The statement concerns the Lipschitz **seminorm**, not the supremum norm of an operator on all bounded functions. No claim is made that the displayed finite-dimensional lower and upper estimates coincide.

## Proof
**Projection formula.** Let \(Y\) be uniform on \(Q_d\). Symmetry and independence give \(\mathbb EY_i=0\), \(\mathbb EY_iY_j=0\) for \(i\ne j\), and \(\mathbb EY_i^2=1/3\). Consequently
\[(P_df)(x)=\mathbb Ef(Y)+\sum_{i=1}^d a_i x_i,\qquad a_i=3\mathbb E[Y_i f(Y)].\]
An affine function \(a_0+\sum_i a_ix_i\) has maximum-coordinate Lipschitz seminorm exactly \(\sum_i|a_i|\).

**Weighted gradient identity.** Since \(f\) is Lipschitz, its weak first derivatives are bounded; one-dimensional integration by parts on slices is valid. The boundary term in
\[\int_{-1}^1 y f(y,\widehat y)\,dy=\frac12\int_{-1}^1(1-y^2)\partial_i f(y,\widehat y)\,dy\]
vanishes because \(1-y^2=0\) at both endpoints. Therefore
\[a_i=\frac32\mathbb E[(1-Y_i^2)\partial_i f(Y)].\]
Rademacher differentiability and duality of \(\ell_\infty^d\) with \(\ell_1^d\) give \(\sum_i|\partial_i f(Y)|\le1\) almost surely whenever \(\operatorname{Lip}_\infty(f)\le1\). Thus
\[\begin{aligned}\operatorname{Lip}_\infty(P_df)&=\sum_i|a_i|\\&\le\frac32\mathbb E\sum_i(1-Y_i^2)|\partial_i f(Y)|\\&\le\frac32\mathbb E\max_i(1-Y_i^2)=\frac32(1-\mathbb E\min_i|Y_i|^2).\end{aligned}\]
For \(0\le t\le1\), independence yields \(\Pr\{\min_i|Y_i|>t\}=(1-t)^d\). Tail integration gives
\[\mathbb E\min_i|Y_i|^2=\int_0^1 2t(1-t)^d\,dt=\frac2{(d+1)(d+2)},\]
proving the upper estimate. Its strict inequality to \(3/2\) holds for every finite \(d\).

**Median witness.** Fix an odd integer \(k=2m+1\le d\) and put \(f(y)=\operatorname{median}(y_1,\ldots,y_k)\), independent of the other coordinates. Changing every input by at most \(\varepsilon\) changes its median by at most \(\varepsilon\), so \(\operatorname{Lip}_\infty(f)=1\). Outside the null set of coordinate ties, exactly one of the first \(k\) partial derivatives equals \(1\) and all others vanish; its index identifies the median observation \(M_k\). Each coefficient \(a_i\) is nonnegative by the gradient identity. Summing them yields
\[\operatorname{Lip}_\infty(P_df)=\frac32\mathbb E[1-M_k^2].\]
Under the affine map \(U=(M_k+1)/2\), the order statistic has the beta distribution with parameters \(m+1,m+1\). Its mean is \(1/2\) and variance is \(1/[4(k+2)]\); hence \(\mathbb E M_k^2=1/(k+2)\). Therefore
\[\operatorname{Lip}_\infty(P_df)=\frac32\left(1-\frac1{k+2}\right).\]
Set \(k=d\) when \(d\) is odd and \(k=d-1\) otherwise. This proves both lower bounds (for even \(d\ge2\)). Both lower bounds converge to \(3/2\), forcing the asserted sharp dimension-free constant and limit. The example \(d=k=3\) gives \(6/5\). No finite-dimensional function can attain the universal value \(3/2\) because the universal upper bound is strict in every fixed dimension. \(\square\)

## Verification
The bundled `check.py` recomputes, in exact rational arithmetic, the integral \(\int_0^1 2t(1-t)^d\,dt\), the beta order-statistic second moment, and the resulting two-sided bounds for sample dimensions, including \(d=1\) and \(d=3\). These finite checks are corroboration, not proof of the statements for all dimensions; the analytic argument above proves those statements.

## Relationship to prior work
Affine and multivariate least-squares polynomial approximation, interpolation and Lebesgue-function stability are established subjects; see the cited primary studies. Their inspected results concern approximation, interpolation, discrete sampling, or supremum norms rather than this uniform sharp maximum-metric Lipschitz bound for the continuous affine orthogonal projection. The product-cube gradient identity, the strict dimensionwise upper bound, and the asymptotically matching median lower witnesses jointly determine the universal Lipschitz amplification constant. No claim of global uniqueness against all historical literature is asserted.

## Limitations
Exact values of \(A_d\) for arbitrary fixed \(d\) are not determined by these estimates. The measure is the uniform product measure, the input metric is \(\ell_\infty\), and the range consists of degree-at-most-one polynomials; the result does not apply verbatim to weighted product measures, other metrics, higher polynomial degrees, or discrete least squares. A differently formulated earlier theorem may exist outside the examined literature.

## References
1. L. Bos, J.-P. Calvi, N. Levenberg, A. Sommariva and M. Vianello, *Geometric Weakly Admissible Meshes, Discrete Least Squares Approximations and Approximate Fekete Points*, arXiv:0902.0215v1 (2009-02-02).
2. *Optimal Point Sets for Total Degree Polynomial Interpolation in Moderate Dimensions*, arXiv:1407.3291v1 (2014-07-11). [The cited title concerns polynomial interpolation; see original bibliographic metadata for full authorship.]
3. Białas-Cież, Kenne, Sommariva and Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656v1 (2023-11-30).
