# Exact Bayesian-bootstrap coupling of weighted mean and variance
## Finding
Fix real observations
\[
x_1,\ldots,x_N,
\qquad N\ge2,
\]
and draw ordinary Bayesian-bootstrap weights
\[
(W_1,\ldots,W_N)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
Define
\[
M=\sum_{i=1}^N W_i x_i
\]
and
\[
V=\sum_{i=1}^N W_i(x_i-M)^2.
\]
Write
\[
\bar x=\frac1N\sum_{i=1}^N x_i
\]
and
\[
\mu_r=\frac1N\sum_{i=1}^N(x_i-\bar x)^r.
\]

Then
\[
\mathbb E M=\bar x,
\qquad
\operatorname{Var}(M)=\frac{\mu_2}{N+1},
\]
\[
\mathbb E V=\frac{N}{N+1}\mu_2,
\]
and
\[
\boxed{
\operatorname{Cov}(M,V)
=
\frac{N\mu_3}{(N+1)(N+2)}.
}
\]
The exact posterior variance of the weighted variance is
\[
\boxed{
\operatorname{Var}(V)
=
\frac{
N\left((N+1)^2\mu_4-(N^2-3)\mu_2^2\right)
}{
(N+1)^2(N+2)(N+3)
}.
}
\]

Consequently the Bayesian-bootstrap location-dispersion covariance has exactly the sign of the empirical third central moment. It vanishes exactly when
\[
\mu_3=0.
\]
For nonconstant data,
\[
\boxed{
\operatorname{Corr}(M,V)^2
=
\frac{
N(N+1)(N+3)\mu_3^2
}{
(N+2)\mu_2
\left((N+1)^2\mu_4-(N^2-3)\mu_2^2\right)
}.
}
\]

For a sequence of empirical distributions whose second through fourth central moments converge, with limiting \(\mu_2>0\) and \(\mu_4>\mu_2^2\),
\[
\operatorname{Corr}(M,V)
\longrightarrow
\frac{\mu_3}{\sqrt{\mu_2(\mu_4-\mu_2^2)}}.
\]

## Assumptions and scope
The observations are fixed. All randomness is in one Bayesian-bootstrap draw with the uniform Dirichlet law on the probability simplex.

The variance functional
\[
V=\sum_iW_i(x_i-M)^2
\]
is the population variance of the random discrete distribution supported on the observed values. It is not the reliability-weight correction sometimes used for deterministic survey weights.

Repeated values are allowed. The correlation formula requires nonconstant data and nondegenerate weighted-variance uncertainty.

## Proof
Translate the data by \(\bar x\). Put
\[
y_i=x_i-\bar x,
\qquad
\sum_i y_i=0,
\]
and define
\[
A=\sum_iW_i y_i,
\qquad
B=\sum_iW_i y_i^2.
\]
Then
\[
M=\bar x+A,
\qquad
V=B-A^2.
\]

For the uniform Dirichlet law,
\[
\mathbb E\!\left[\prod_iW_i^{r_i}\right]
=
\frac{\prod_i r_i!}{N(N+1)\cdots(N+r-1)},
\qquad
r=\sum_i r_i.
\]
Thus
\[
\mathbb EA=0,
\qquad
\mathbb EA^2=\frac{\mu_2}{N+1},
\qquad
\mathbb EB=\mu_2.
\]
It follows that
\[
\mathbb EV=\frac{N}{N+1}\mu_2.
\]

Let
\[
p_r=\sum_i y_i^r=N\mu_r.
\]
Direct Dirichlet moment reduction gives
\[
\mathbb E[AB]=\frac{p_3}{N(N+1)}
\]
and
\[
\mathbb EA^3=\frac{2p_3}{N(N+1)(N+2)}.
\]
Therefore
\[
\operatorname{Cov}(M,V)
=
\mathbb E[A(B-A^2)]
=
\frac{N\mu_3}{(N+1)(N+2)}.
\]

For the variance of \(V\),
\[
\mathbb EB^2
=
\frac{p_4+p_2^2}{N(N+1)},
\]
\[
\mathbb E[BA^2]
=
\frac{p_2^2+2p_4}{N(N+1)(N+2)},
\]
and
\[
\mathbb EA^4
=
\frac{3p_2^2+6p_4}{N(N+1)(N+2)(N+3)}.
\]
Since
\[
V^2=B^2-2BA^2+A^4,
\]
substitution of
\[
p_2=N\mu_2,
\qquad
p_4=N\mu_4
\]
and subtraction of \((\mathbb EV)^2\) yield
\[
\operatorname{Var}(V)
=
\frac{
N\left((N+1)^2\mu_4-(N^2-3)\mu_2^2\right)
}{
(N+1)^2(N+2)(N+3)
}.
\]
Combining this with
\[
\operatorname{Var}(M)=\frac{\mu_2}{N+1}
\]
gives the correlation formula. The asymptotic relation follows directly from the exact expression.

## Verification
The accompanying `checker.py` evaluates Dirichlet monomial expectations directly from the factorial moment formula.

For several integer data sets at each \(2\le N\le8\), it expands the relevant linear and quadratic forms by explicit index sums with exact rational arithmetic, reconstructs
\[
\operatorname{Var}(M),
\quad
\mathbb E V,
\quad
\operatorname{Cov}(M,V),
\quad
\operatorname{Var}(V),
\]
and compares them with the displayed closed forms.

The analytic proof establishes all \(N\). The finite exact checks are supplementary.

## Relationship to prior work
Rubin's Bayesian bootstrap assigns Dirichlet weights to the observed support and explicitly illustrates the posterior distribution of weighted means. The complete original article also notes that commonly estimated parameters such as the mean and variance are sensitive to the bootstrap model, but it does not state the exact joint posterior moments of the weighted mean and weighted variance given here.

Cheng studies moment consistency for exchangeably weighted bootstrap procedures. The full article explicitly identifies normalized exponential weights with the Bayesian bootstrap and proves asymptotic moment-consistency results for semiparametric estimators. Those results are asymptotic and model-generic; they do not state the finite fixed-data covariance and variance identities above.

The formulas here use standard Dirichlet moments as ingredients. The finding is the resulting exact finite joint uncertainty law for two basic Bayesian-bootstrap functionals, including the empirical-skewness sign characterization.

## Limitations
The result is specific to ordinary uniform-Dirichlet Bayesian-bootstrap weights. General Dirichlet concentration parameters change the coefficients.

The derivation concerns the random discrete distribution supported on observed values. It does not cover prior smoothing outside the observed support, hierarchical Bayesian bootstraps, or weighted-likelihood-bootstrap parameter estimates.

A short closed-form identity of this kind may exist in older unindexed bootstrap or Dirichlet-moment literature.

## References
1. D. B. Rubin, “The Bayesian Bootstrap,” *The Annals of Statistics* 9 (1981), 130–134. DOI: 10.1214/aos/1176345338.
2. G. Cheng, “Moment Consistency of the Exchangeably Weighted Bootstrap for Semiparametric M-Estimation,” arXiv:1109.4204, first submitted 20 September 2011.
