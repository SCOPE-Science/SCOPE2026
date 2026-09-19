# Exact FGM nesting thresholds and failure of unrestricted copula substitution

## Result

Let
\[
C_\theta(u,v)=uv\{1+\theta(1-u)(1-v)\},\qquad -1\le \theta\le 1,
\]
be the bivariate Farlie--Gumbel--Morgenstern (FGM) copula, and let
\[
\Pi_m(x_1,\dots,x_m)=\prod_{i=1}^m x_i,
\qquad
\Pi_n(y_1,\dots,y_n)=\prod_{j=1}^n y_j
\]
be independence copulas. Consider the direct substitution
\[
F_{m,n,\theta}(x,y)
 =C_\theta\!\left(\Pi_m(x),\Pi_n(y)\right).
\]
Then this candidate is a copula **if and only if**
\[
\boxed{
-\frac{1}{(2^m-1)(2^n-1)}
\le \theta\le
\frac{1}{\max\{2^m-1,2^n-1\}}.
}
\]
Thus arbitrary substitution of copulas into copula arguments is not closed within the class of copulas. In particular, an admissible outer FGM parameter may cease to be admissible after a multivariate inner substitution.

The same example also shows that the entropy-additivity formula proposed for unrestricted substitution does not hold even where the substituted function remains a valid absolutely continuous copula. Near independence,
\[
H(F_{m,n,\theta})
=-\frac{\theta^2}{2}
\left[\left(\frac43\right)^m-1\right]
\left[\left(\frac43\right)^n-1\right]
+O(\theta^3),
\]
where \(H(C)=-\int c\log c\) is copula entropy. For the outer FGM copula itself,
\[
H(C_\theta)=-\frac{\theta^2}{18}+O(\theta^4).
\]
For example, at \((m,n)=(2,1)\),
\[
H(F_{2,1,\theta})-H(C_\theta)
=-\frac{2}{27}\theta^2+O(\theta^3),
\]
while both inner independence copulas have entropy zero. Hence additivity already fails at quadratic order within the valid range \(|\theta|\le 1/3\).

## Why the naive density product fails

For a smooth bivariate outer copula \(C\), put
\[
u=\prod_{i=1}^m x_i,\qquad v=\prod_{j=1}^n y_j,
\]
and let \(c=\partial_u\partial_v C\). Define Euler operators
\[
D_u=u\partial_u,\qquad D_v=v\partial_v.
\]
A direct repeated differentiation gives
\[
\boxed{
\frac{\partial^{m+n}}{
\partial x_1\cdots\partial x_m\partial y_1\cdots\partial y_n}
C(u,v)
=(1+D_u)^{m-1}(1+D_v)^{n-1}c(u,v).
}
\]
Indeed, for a one-variable function \(f\),
\[
\partial_{x_1}\cdots\partial_{x_m}
 f\!\left(\prod_i x_i\right)
=u^{-1}D_u^m f(u)
=(1+D_u)^{m-1}f'(u).
\]
The extra Euler-operator terms are the higher chain-rule contributions that disappear only when the corresponding inner block has arity one.

For FGM,
\[
c_\theta(u,v)=1+\theta(1-2u)(1-2v),
\]
and therefore
\[
\boxed{
g_{m,n,\theta}(x,y)
=1+\theta(1-2^m u)(1-2^n v).}
\]
Because
\[
1-2^m u\in[-(2^m-1),1],\qquad
1-2^n v\in[-(2^n-1),1],
\]
the product of these two factors has minimum
\(-\max\{2^m-1,2^n-1\}\) and maximum
\((2^m-1)(2^n-1)\). Nonnegativity of the smooth full mixed derivative is therefore equivalent to the displayed parameter interval. Groundedness and the uniform one-dimensional margins hold automatically, so this density criterion is also sufficient.

## Explicit counterexample

Take \(m=2,n=1,\theta=1\). Then the outer FGM copula and both inner copulas are individually valid, but
\[
F(x,y,z)=C_1(xy,z)
\]
has density
\[
g(x,y,z)=1+(1-4xy)(1-2z).
\]
At
\[
(x,y,z)=\left(\frac78,\frac78,\frac18\right)
\]
one gets
\[
\boxed{g=-\frac{35}{64}<0.}
\]
By continuity, a neighborhood has negative density, hence some rectangular increment is negative and \(F\) is not a copula. The exact admissible interval for this nesting is only \([-1/3,1/3]\). For \((m,n)=(2,2)\) it is \([-1/9,1/3]\).

## Entropy curvature

Under Lebesgue measure on the inner coordinates, let
\[
U=\prod_{i=1}^m X_i,
\qquad X_i\stackrel{\mathrm{iid}}\sim\operatorname{Unif}(0,1).
\]
Then
\[
\mathbb EU=2^{-m},\qquad \mathbb EU^2=3^{-m},
\]
so
\[
\mathbb E(1-2^mU)=0,
\qquad
\mathbb E(1-2^mU)^2=\left(\frac43\right)^m-1.
\]
Writing the valid substituted density as \(1+\theta h\) and expanding
\(-(1+\theta h)\log(1+\theta h)\) gives the entropy formula above. This also pinpoints a second failure in the proposed substitution argument: for a multivariate copula \(\Psi\), the scalar random variable \(\Psi(V)\) is not generally uniform. For example, \(\Pi_2(X_1,X_2)=X_1X_2\) with independent uniform coordinates is not uniform.

## Relation to recent and prior literature

Lu (2026), *Copula Operad and Copula Entropy* (arXiv:2609.20512), defines unrestricted substitution of multivariate copulas and states closure, a simple Jacobian-product density formula, and entropy additivity for the resulting composition. The explicit FGM/product-inner family above contradicts unrestricted closure and gives the corrected full mixed derivative for this product-inner setting.

The broader fact that hierarchical copula constructions need compatibility conditions is not new. Nested Archimedean copulas, for example, are developed under nontrivial nesting conditions in McNeil (2008) and subsequent work such as Hofert--Maechler (2011). No novelty is claimed for the generic principle that arbitrary nesting can fail. The contribution here is the exact FGM threshold family, the explicit differential operator for product-inner substitution, and the entropy-curvature defect. Searches did not locate these formulas or an equivalent statement; originality is claimed only to the best of our knowledge.

## Limitations

The exact admissibility interval is proved for a bivariate FGM outer copula with independence copulas in the two inner blocks. Arbitrary outer and inner copulas require a more general multivariate chain-rule analysis and are not characterized here. The entropy comparison is a local expansion around \(\theta=0\), sufficient to disprove additivity but not intended as a closed form for all admissible parameters. Existing nested-copula literature is broad, and an equivalent special-case formula could remain in older or differently phrased work.

## Verification

`artifacts/verify_fgm_substitution.py` uses exact rational arithmetic to check the negative-density counterexample, the \((2,1)\) and \((2,2)\) admissible intervals, and the entropy second-derivative coefficients. Its captured output is in `artifacts/verification.txt`.

## References

1. X. Lu, *Copula Operad and Copula Entropy*, arXiv:2609.20512v1, 17 September 2026. https://arxiv.org/abs/2609.20512
2. A. J. McNeil, *Sampling nested Archimedean copulas*, Journal of Statistical Computation and Simulation 78 (2008), 567--581. https://doi.org/10.1080/00949650701255834
3. M. Hofert and M. Maechler, *Nested Archimedean Copulas Meet R: The nacopula Package*, Journal of Statistical Software 39(9) (2011), 1--20. https://doi.org/10.18637/jss.v039.i09
