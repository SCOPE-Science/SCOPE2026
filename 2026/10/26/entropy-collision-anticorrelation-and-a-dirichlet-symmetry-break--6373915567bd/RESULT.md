# Entropy–collision anticorrelation and a Dirichlet symmetry-breaking threshold

## Finding

Let \(K\ge2\), let \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_K)\) have strictly positive coordinates, and let \(P\sim\operatorname{Dirichlet}(\boldsymbol\alpha)\). Define Shannon diversity and collision concentration by
\[
H(P)=-\sum_{i=1}^{K}P_i\log P_i,\qquad Q(P)=\sum_{i=1}^{K}P_i^2.
\]
Write \(A=\sum_i\alpha_i\), \(w_i=\alpha_i/A\), and \(\psi\), \(\psi_1\) for the di- and trigamma functions. For any vectors \(u,v\), let \(\operatorname{Cov}_w(u,v)=\sum_iw_i(u_i-\sum_jw_ju_j)(v_i-\sum_jw_jv_j)\). Then the exact mixed covariance is
\[
\boxed{\operatorname{Cov}(H(P),Q(P))=
-\frac{A^2-\sum_i\alpha_i^2}{A(A+1)^2(A+2)}
-\frac{2\operatorname{Cov}_w(\boldsymbol\alpha,\psi(\boldsymbol\alpha+\mathbf1))}{(A+1)(A+2)}<0.}
\]
The digamma expression is evaluated componentwise. Both terms are nonpositive, and the first is strictly negative. Thus the sign does not require a symmetric prior. In particular, with equal shapes \(\alpha_i=a\),
\[
-\operatorname{Cov}(H(P),Q(P))=\frac{(K-1)a}{(Ka+1)^2(Ka+2)}.
\]

There is also a sharp **local stability transition** when the total concentration \(A\) is held fixed and the component shapes become unequal. Define \(V(\boldsymbol\alpha)=-\operatorname{Cov}(H,Q)>0\), and put \(a=A/K\). For each real vector \(v=(v_1,\ldots,v_K)\) with \(\sum_iv_i=0\),
\[
V(a\mathbf1+\varepsilon v)=V(a\mathbf1)+\varepsilon^2\,\frac{2a(Ka+1)\psi_1(a+1)-1}{Ka(Ka+1)^2(Ka+2)}\sum_iv_i^2+O_{K,a,v}(\varepsilon^3).
\]
There exists **exactly one** \(a_*(K)>0\) satisfying
\[
2a_*(K)(Ka_*(K)+1)\psi_1(a_*(K)+1)=1.
\]
Consequently, among strictly positive Dirichlet shape vectors with the same total concentration, the equal-shape vector is a strict local maximum of \(V\) when \(A<K a_*(K)\), and a strict local minimum of \(V\) when \(A>K a_*(K)\). At equality the quadratic variation vanishes; no claim of a strict extremum is made there. Numerically, the critical total concentrations are approximately \(0.5535880\) for \(K=2\), \(0.7202551\) for \(K=3\), and \(0.9891574\) for \(K=5\).

## Assumptions and scope

All statements are for a fixed finite integer \(K\ge2\) and arbitrary strictly positive Dirichlet concentration coordinates. The logarithm is natural and \(0\log0=0\) at boundary points, which occur with probability zero. The second statement compares the negative entropy–collision covariance across **priors**, not across realizations, under fixed \(\sum_i\alpha_i=A\). The local expansion holds for each fixed direction and sufficiently small real \(\varepsilon\) maintaining positivity; it does not assert a global optimizer. The ordinary Gini–Simpson diversity equals \(1-Q\), so its covariance with \(H\) is the positive opposite of the displayed quantity.

## Proof

The standard Dirichlet moment identity, for real exponents where it is integrable, is
\[
\mathbb E\prod_iP_i^{r_i}=\frac{\Gamma(A)}{\Gamma(A+\sum_ir_i)}\prod_i\frac{\Gamma(\alpha_i+r_i)}{\Gamma(\alpha_i)}.
\]
It can be differentiated with respect to each exponent in a neighborhood of the exponents used below, since all \(\alpha_i>0\). Let \(S_2=\sum_i\alpha_i(\alpha_i+1)\). Differentiation with exponent \(1\) gives
\[
\mathbb E H=\psi(A+1)-\frac1A\sum_i\alpha_i\psi(\alpha_i+1),\qquad
\mathbb E Q=\frac{S_2}{A(A+1)}.
\]
Standard third moments further give, for each \(j\),
\[
\mathbb E[P_jQ]=\frac{\alpha_j[S_2+2(\alpha_j+1)]}{A(A+1)(A+2)},
\quad\operatorname{Cov}(P_j,Q)=\frac{2\alpha_j[(\alpha_j+1)-S_2/A]}{A(A+1)(A+2)}.
\]

For \(i\ne j\), exponent differentiation shows
\[
\mathbb E[P_i^2P_j\log P_j]=\mathbb E[P_i^2P_j][\psi(\alpha_j+1)-\psi(A+3)],
\]
and, for \(i=j\), the bracket is \(\psi(\alpha_j+3)-\psi(A+3)\). Substituting in \(\mathbb E[HQ]\), subtracting \(\mathbb EH\,\mathbb EQ\), and using the recurrences \(\psi(z+1)-\psi(z)=1/z\) gives
\[
\operatorname{Cov}(H,Q)=\frac{S_2-A(A+1)}{A(A+1)^2(A+2)}-\sum_j\psi(\alpha_j+1)\operatorname{Cov}(P_j,Q).
\]
Here \(S_2-A(A+1)=\sum_j\alpha_j^2-A^2\). The weighted mean of the \(\alpha_j\) under \(w\) is \(S_2/A-1\), so the last sum becomes \(2\operatorname{Cov}_w(\boldsymbol\alpha,\psi(\boldsymbol\alpha+\mathbf1))/[(A+1)(A+2)]\). This proves the exact formula.

Because \(\psi\) is strictly increasing on \((0,\infty)\),
\[
\operatorname{Cov}_w(\boldsymbol\alpha,\psi(\boldsymbol\alpha+\mathbf1))=
\frac12\sum_{i,j}w_iw_j(\alpha_i-\alpha_j)[\psi(\alpha_i+1)-\psi(\alpha_j+1)]\ge0.
\]
The rational numerator \(A^2-\sum_i\alpha_i^2=2\sum_{i<j}\alpha_i\alpha_j\) is positive because \(K\ge2\). Therefore the claimed strict anticorrelation follows, including all asymmetric shapes.

For the local transition, write \(\alpha_i=a+\varepsilon v_i\) with \(\sum_iv_i=0\). Then \(A=Ka\) is fixed and \(\sum_i\alpha_i^2=Ka^2+\varepsilon^2\sum_iv_i^2\). A Taylor expansion of the weighted covariance around equal arguments gives
\[
\operatorname{Cov}_w(\boldsymbol\alpha,\psi(\boldsymbol\alpha+\mathbf1))=
\frac{\varepsilon^2\psi_1(a+1)}K\sum_iv_i^2+O_{K,a,v}(\varepsilon^3).
\]
Inserting both expressions in the formula for \(V\) proves the quadratic coefficient. It has one sign, independent of the nonzero tangent direction, away from its zero.

To prove that the coefficient changes sign **exactly once**, use the integral representation
\[
a\psi_1(a+1)=\int_0^\infty e^{-u}\frac{u/a}{e^{u/a}-1}\,du.
\]
For each \(u>0\), the function \(t\mapsto t/(e^t-1)\) is strictly decreasing on \((0,\infty)\), so this integral is strictly increasing in \(a\). It increases from zero to one as \(a\) goes from zero to infinity (by dominated convergence). Therefore \(2(Ka+1)a\psi_1(a+1)\) increases continuously and strictly from zero to infinity, crossing one at a unique positive \(a_*(K)\). The positive/negative definite quadratic form gives the asserted strict local minimum/maximum for \(V\). This completes the proof.

## Verification

The companion `verify.py` recomputes \(\operatorname{Cov}(H,Q)\) by a separate calculation from the *unsimplified* Dirichlet mixed moments and their logarithmic derivatives. For two categories it also integrates the beta density numerically; for several dimensions it compares the quadratic perturbation against the derived Hessian coefficient and brackets the unique positive transition. The script passed 20 checks covering nine nondegenerate concentration vectors and four values of \(K\), with separate numerical quadrature and curvature comparisons. The code is reproducible with Python, `mpmath` and no private inputs. Numerical checks support but do not replace the symbolic proof, which covers every finite \(K\) and all positive real shape parameters.

## Relationship to prior work

The Dirichlet moment formula and entropy and Simpson statistics are standard, not claimed as new. Willis and Martin (2020) motivate joint interpretation of ecological diversity indices but study estimation under network-aware compositional models, not this covariance sign and fixed-concentration curvature classification. Botha, Ferreira and Bekker (2021) develop alternative Dirichlet priors and power-sum functional moments for entropy estimation; those general moments are ingredients from which mixed quantities can be derived. The contribution here is the explicit *universal sign decomposition* plus the *unique prior-symmetry curvature switch* under fixed total concentration; neither follows from a stated theorem about marginal means/variances alone without an additional mixed calculation and monotonicity analysis. Bissiri, Corradin and Ongaro (2026) discuss Gini–Simpson prior/posterior dispersion and symmetric versus richness-dependent concentration, but not cross-covariance with Shannon entropy or local asymmetric shape perturbations. A broad joint-moment identity in further literature could imply the raw formula, so an exhaustive priority claim is not made.

## Limitations

This is not a claim of stochastic order, monotone sample-path relation, or independence. The local stability switch is not a global extremal classification, and nothing is asserted about the degenerate threshold's higher-order behavior. No inference guarantee is claimed beyond the stated exact prior law. The originality comparison is based on accessible publications and research-record searches, not an exhaustive review of every possible derivation; independent historical priority assessment remains outstanding.

## References

1. A. D. Willis and B. D. Martin (2020), *Estimating diversity in networked ecological communities*, **Biostatistics**. First verified online date 2020-05-20. https://doi.org/10.1093/biostatistics/kxaa015
2. T. Botha, J. Ferreira and A. Bekker (2021), *Alternative Dirichlet Priors for Estimating Entropy via a Power Sum Functional*, **Mathematics** 9(13), 1493. First verified online date 2021-06-25. https://doi.org/10.3390/math9131493
3. P. G. Bissiri, R. Corradin and A. Ongaro (2026), *Nonparametric Bayesian inference for the Gini–Simpson index*, arXiv:2607.25737, initial version 2026-07-28. https://arxiv.org/abs/2607.25737
