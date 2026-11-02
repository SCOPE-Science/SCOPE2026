# Minimum-gap independence characterizes the uniform Dirichlet law

## Finding
Let \(n\ge3\), \(\alpha>0\), and \(X=(X_1,\ldots,X_n)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\). Define the minimum component, quadratic dispersion, and normalized residual dispersion by
\[
M=\min_iX_i,\qquad G=\sum_{i=1}^nX_i^2,\qquad
T=\frac{nG-1}{(1-nM)^2}.
\]
The denominator is nonzero almost surely. The following is an exact characterization **within the symmetric Dirichlet family**:
\[
\boxed{M\ \text{and}\ T\ \text{are independent}\quad\Longleftrightarrow\quad\alpha=1.}
\]
In the independence case, if \(Y\sim\operatorname{Dirichlet}_{n-1}(1,\ldots,1)\), then
\[
1-nM\sim\operatorname{Beta}(n-1,1),\qquad
T\overset{d}=n\sum_{i=1}^{n-1}Y_i^2-1,
\]
and the two displayed random variables are independent. Thus the **entire conditional distribution** of \(G\) given \(M=m\) is the law of
\[
\frac1n+\frac{(1-nm)^2}{n}T,
\]
with the same \(T\)-law for all \(0<m<1/n\). In particular,
\[
\begin{aligned}
\mathbb E[G\mid M=m]&=\frac{1+(1-nm)^2}{n},\\
\operatorname{Cov}(M,G)&=-\frac{2(n-1)}{n^3(n+1)(n+2)},\\
\operatorname{Corr}(M,G)&=-\frac1n\sqrt{\frac{(n+1)(n+3)}{n+2}}.
\end{aligned}
\]
The conditional law of \(G\) is strictly decreasing in stochastic order as \(m\) increases, and the correlation is asymptotic to \(-n^{-1/2}\).

For \(\alpha\ne1\), using the continuous conditional-density version specified below, the diagnostic conditional means have distinct endpoint limits:
\[
\lim_{m\downarrow0}\mathbb E[T\mid M=m]
=\frac{n(\alpha+1)}{(n-1)\alpha+1}-1,
\qquad
\lim_{m\uparrow1/n}\mathbb E[T\mid M=m]=1.
\]
Their difference is \((n-2)(1-\alpha)/((n-1)\alpha+1)\), nonzero precisely when \(\alpha\ne1\).

## Assumptions and scope
The density is that of the symmetric finite-dimensional Dirichlet family with \(n\ge3\) and \(\alpha>0\). Ties for the minimum have probability zero. No statement is made about arbitrary distributions on the simplex. The restriction \(n\ge3\) is sharp: at \(n=2\), the statistic \(T\) is identically \(1\), and hence independent of \(M\) for every \(\alpha>0\).

For the statistical interpretation, take the \(n\) consecutive spacings (including the two boundary spacings) induced by \(n-1\) independent observations from a specified continuous distribution after its probability integral transform. Under the specified null, these spacings have the \(\operatorname{Dirichlet}_n(1,\ldots,1)\) law. Here \(G\) is Greenwood's quadratic spacing statistic. If \(c_\eta\) is a continuous-distribution upper-tail \(\eta\)-critical value of \(T\) under that null, then for every minimum-spacing selection event \(A\) with \(\Pr(A)>0\),
\[
\Pr\{T>c_\eta\mid A\}=\eta.
\]
Consequently, the residual statistic has an exact null calibration even after selection based solely on the shortest spacing. For \(n\ge3\), the null law of \(T\) has no atoms.

## Proof
**1. Conditioning on the unique minimum.** Let \(J\) be the almost surely unique index at which \(M\) is attained. For \(0<m<1/n\), write \(b=1-nm\), set \(Z_J=0\), and set \(Z_i=(X_i-m)/b\) for \(i\ne J\). Then \(Z_i>0\) for \(i\ne J\), and \(\sum_{i\ne J}Z_i=1\). On each chamber \(J=j\), the transformation from the Dirichlet density to \((m,Z)\) has a Jacobian proportional to \(b^{n-2}\). Its density, up to a positive constant independent of \((m,z)\), is
\[
 b^{n-2}m^{\alpha-1}
 \prod_{i\ne j}\bigl(m+bz_i\bigr)^{\alpha-1}.
\tag{1}
\]
Exchangeability makes \(J\) uniform over the indices.

**2. The uniform case and the pivot.** At \(\alpha=1\), expression (1) is constant as a function of \(z\). Hence \(Z\), conditional on \(J=j\), has one zero coordinate and an independent uniform Dirichlet law on the remaining \(n-1\) coordinates, with no dependence on \(m\). The same statement holds without conditioning on \(J\), up to a uniformly chosen zero position. The simplex-volume identity
\[
\Pr\{M>m\}=(1-nm)^{n-1},\qquad 0\le m\le1/n,
\]
gives \(B=1-nM\sim\operatorname{Beta}(n-1,1)\), independent of the residual shape.

Since \(X_i=M+BZ_i\), \(nM=1-B\), and \(\sum Z_i=1\), an exact algebraic identity gives
\[
G=\frac1n+B^2\left(\sum_iZ_i^2-\frac1n\right),
\quad\text{so}\quad
T=n\sum_iZ_i^2-1.
\tag{2}
\]
This proves both independence and the stated distribution of \(T\).

**3. Uniqueness within the Dirichlet family.** For general \(\alpha>0\), conditionally on \(M=m,J=j\), the normalized residual has density on its \((n-2)\)-simplex proportional to the product in (1). As \(m\downarrow0\), its normalized density converges to the \(\operatorname{Dirichlet}_{n-1}(\alpha,\ldots,\alpha)\) density. As \(m\uparrow1/n\), it converges to the uniform \(\operatorname{Dirichlet}_{n-1}(1,\ldots,1)\) density. Dominated convergence applies: near \(m=0\), when \(\alpha<1\), the product is bounded by a constant times \(\prod_{i\ne j}z_i^{\alpha-1}\), which is integrable; when \(\alpha\ge1\), it is uniformly bounded. At the other endpoint the factors approach positive constants uniformly.

For a symmetric Dirichlet vector of length \(k\) and parameter \(a>0\), the beta-moment formula gives
\[
\mathbb E\sum_{i=1}^{k}Y_i^2=\frac{a+1}{ka+1}.
\]
Combining this with (2) gives the two endpoint limits displayed in the Finding. If \(T\) and \(M\) were independent, the continuous version of \(m\mapsto\mathbb E[T\mid M=m]\) would be constant, forcing equality of these limits. Since \(n\ge3\), their difference vanishes only when \(\alpha=1\). Step 2 gives the converse.

**4. Regression, covariance and correlation.** For \(\alpha=1\), write \(k=n-1\) and \(Q=\sum_{i=1}^{k}Y_i^2\). Dirichlet integration yields
\[
\mathbb EQ=\frac{2}{k+1},\qquad
\mathbb EQ^2=\frac{4(k+5)}{(k+1)(k+2)(k+3)}.
\]
The beta law gives \(\mathbb EB^r=(n-1)/(n-1+r)\) for \(r\ge0\). In particular, \(\mathbb E[T]=1\), \(\operatorname{Var}(T)=4(n-2)/((n+1)(n+2))\), and
\[
\operatorname{Var}(M)=\frac{n-1}{n^4(n+1)},\quad
\operatorname{Var}(G)=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)}.
\]
Using \(M=(1-B)/n\) and \(G=1/n+B^2T/n\), with \(T\) independent of \(B\), gives
\[
\operatorname{Cov}(M,G)
=-\frac{\mathbb E[T]}{n^2}
\bigl(\mathbb EB^3-\mathbb EB\,\mathbb EB^2\bigr)
=-\frac{2(n-1)}{n^3(n+1)(n+2)}.
\]
Dividing by the displayed standard deviations proves the correlation formula. Since \(T>0\) almost surely, (2) also gives strict conditional stochastic ordering. This completes the proof.

## Verification
The included `verify.py` uses only standard Python and exact rational arithmetic. It checks the independent beta/Dirichlet moment expansion, regression consequences, covariance and correlation identities for every \(2\le n\le100\), tests endpoint separation for six shape parameters and every \(3\le n\le100\), and checks a directly integrated three-component \(\alpha=2\) conditional density. It reports **1192 exact rational checks passed**. These finite computations verify algebra and boundary examples; the displayed change-of-variables argument is the proof for arbitrary dimension and shape parameter.

## Relationship to prior work
Royen's 2010 study gives exact **marginal** distributions and quantiles for sums of squares of Dirichlet variables, including Greenwood's statistic. Its formulas yield the \((n-1)\)-dimensional reference law appearing in (2), but its inspected results do not describe the joint distribution with the *minimum* component or the independence characterization above. Pyke's classic survey reviews uniform spacings, and Sakowicz–Wesołowski characterize Dirichlet distributions through independence associated with **fixed index partitions**, a different form of neutrality than the order-selected minimum and quadratic excess considered here.

The comparison is at the level of mathematical implication, not wording: knowing a marginal squared-norm distribution does not determine its conditional law given an extreme coordinate, and fixed-index neutrality does not by itself impose the stated minimum-selected factorization. More specialized historical formulas may nevertheless provide the same result indirectly; exhaustive historical priority is not claimed.

## Limitations
The equivalence is proved only within the finite symmetric Dirichlet family, and the selective calibration applies only under the specified uniform-spacing null and selection measurable with respect to the minimum spacing. For \(n=2\), \(T\) is deterministic, so uniqueness fails. Full access to Pyke's historical survey and the Sakowicz–Wesołowski publisher full text was unavailable during comparison; equivalence hidden in those sources cannot be ruled out. No claim is made of independent scientific validation.

## References
1. T. Royen, *The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic*, arXiv:1008.4059v1 (first public version 2010-08-24), https://arxiv.org/abs/1008.4059.
2. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B 27 (1965), 395–436; DOI 10.1111/j.2517-6161.1965.tb00602.x.
3. A. Sakowicz and J. Wesołowski, *Dirichlet distribution through neutralities with respect to two partitions*, Journal of Multivariate Analysis 129 (2014), 1–15; DOI 10.1016/j.jmva.2014.04.004.
