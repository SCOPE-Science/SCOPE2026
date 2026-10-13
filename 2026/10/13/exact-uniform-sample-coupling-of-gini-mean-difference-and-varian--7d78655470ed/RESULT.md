# Exact uniform-sample coupling of Gini mean difference and variance
## Finding
Let
\[
X_1,\ldots,X_n\stackrel{\mathrm{iid}}{\sim}\operatorname{Unif}[a,b],
\qquad n\ge2,
\qquad \ell=b-a>0.
\]
Define the sample Gini mean difference
\[
G_n=\binom n2^{-1}\sum_{1\le i<j\le n}|X_i-X_j|
\]
and the unbiased sample variance
\[
S_n^2
=
\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
=
\binom n2^{-1}
\sum_{i<j}\frac{(X_i-X_j)^2}{2}.
\]
Their means are
\[
\mathbb E G_n=\frac{\ell}{3},
\qquad
\mathbb E S_n^2=\frac{\ell^2}{12}.
\]
The exact finite-sample variances and covariance are
\[
\boxed{
\operatorname{Var}(G_n)
=
\frac{\ell^2(n+3)}{45n(n-1)}
},
\]
\[
\boxed{
\operatorname{Var}(S_n^2)
=
\frac{\ell^4(2n+3)}{360n(n-1)}
},
\]
and
\[
\boxed{
\operatorname{Cov}(G_n,S_n^2)
=
\frac{\ell^3(n+2)}{90n(n-1)}
}.
\]
Hence
\[
\boxed{
\operatorname{Corr}(G_n,S_n^2)
=
\frac{\sqrt2(n+2)}
{\sqrt{(n+3)(2n+3)}}
}.
\]
The squared-correlation deficit has the especially simple form
\[
\boxed{
1-\operatorname{Corr}(G_n,S_n^2)^2
=
\frac{n+1}{(n+3)(2n+3)}
}.
\]
It decreases strictly with \(n\), so the correlation increases strictly to one.

There is a sharper structural statement. Put
\[
C_n
=
\frac{G_n}{\ell}
-
2\frac{S_n^2}{\ell^2}
-
\frac16.
\]
Then
\[
\boxed{
\mathbb E C_n=0,
\qquad
\operatorname{Var}(C_n)=\frac1{90n(n-1)}.
}
\]
Moreover \(C_n\) is a degenerate order-two U-statistic. Thus the first-order Hoeffding projections of the normalized Gini statistic and twice the normalized sample variance coincide exactly, and their discrepancy is purely second-order.

## Assumptions and scope
The parent distribution is exactly uniform on a nondegenerate finite interval. The statistics use the ordinary unscaled Gini mean difference and the unbiased sample variance. The affine normalization by \(\ell=b-a\) makes the structural statement independent of location and interval length.

No claim is made for nonuniform parent laws. In particular, the analogous covariance is distribution-specific; the uniform law is special because the two first-order Hoeffding projections are exactly proportional.

## Proof
By affine equivariance it is enough to prove the result for
\[
X_i\sim\operatorname{Unif}[0,1].
\]
Write
\[
h(x,y)=|x-y|,
\qquad
g(x,y)=\frac{(x-y)^2}{2}.
\]
Both statistics are normalized order-two U-statistics with these kernels.

For two independent uniforms,
\[
\mathbb Eh(X_1,X_2)=\frac13,
\qquad
\mathbb Eg(X_1,X_2)=\frac1{12}.
\]
The same-pair centered moments are
\[
\operatorname{Var}(h(X_1,X_2))=\frac1{18},
\]
\[
\operatorname{Var}(g(X_1,X_2))=\frac7{720},
\]
and
\[
\operatorname{Cov}(h(X_1,X_2),g(X_1,X_2))
=
\frac1{45}.
\]

For a single shared observation \(X\), define
\[
a(x)=\mathbb E[h(x,Y)]
=x^2-x+\frac12
\]
and
\[
b(x)=\mathbb E[g(x,Y)]
=
\frac12\left(x^2-x+\frac13\right).
\]
Direct integration gives
\[
\operatorname{Var}(a(X))=\frac1{180},
\]
\[
\operatorname{Var}(b(X))=\frac1{720},
\]
and
\[
\operatorname{Cov}(a(X),b(X))=\frac1{360}.
\]
These are exactly the covariances of two kernels whose unordered index pairs share one observation.

Let
\[
M=\binom n2.
\]
Among ordered pairs of unordered sample pairs, there are \(M\) identical-pair terms and
\[
2M(n-2)
\]
distinct ordered terms sharing exactly one sample index. Disjoint kernel pairs are independent. Therefore
\[
\operatorname{Var}(G_n)
=
\frac1M
\left(
\frac1{18}
+
2(n-2)\frac1{180}
\right)
=
\frac{n+3}{45n(n-1)},
\]
\[
\operatorname{Var}(S_n^2)
=
\frac1M
\left(
\frac7{720}
+
2(n-2)\frac1{720}
\right)
=
\frac{2n+3}{360n(n-1)},
\]
and
\[
\operatorname{Cov}(G_n,S_n^2)
=
\frac1M
\left(
\frac1{45}
+
2(n-2)\frac1{360}
\right)
=
\frac{n+2}{90n(n-1)}.
\]
The affine powers of \(\ell\) restore the general-interval formulas.

For the structural statement, center the conditional kernel means:
\[
a(x)-\frac13
=
x^2-x+\frac16,
\]
while
\[
b(x)-\frac1{12}
=
\frac12\left(x^2-x+\frac16\right).
\]
Thus the first-order projections satisfy
\[
a(x)-\frac13
=
2\left(b(x)-\frac1{12}\right)
\]
pointwise. Hence the first-order projection of
\[
h-2g-\frac16
\]
vanishes identically.

Its same-pair variance is
\[
\operatorname{Var}\!\left(
|X_1-X_2|-(X_1-X_2)^2
\right)
=
\frac1{180}.
\]
Because the kernel is degenerate, all one-overlap covariances vanish. Therefore
\[
\operatorname{Var}(C_n)
=
\frac{1/180}{\binom n2}
=
\frac1{90n(n-1)}.
\]

Finally,
\[
\operatorname{Corr}(G_n,S_n^2)^2
=
\frac{2(n+2)^2}{(n+3)(2n+3)}
=
1-\frac{n+1}{(n+3)(2n+3)}.
\]
The deficit decreases strictly because its difference between successive sample sizes is
\[
\frac{2(n^2+3n+1)}
{(n+3)(n+4)(2n+3)(2n+5)}
>0.
\]

## Verification
The accompanying `checker.py` recomputes the required kernel moments using exact rational polynomial integration rather than inserting the displayed covariance formulas. It independently derives all same-pair and one-overlap moments, rebuilds the normalized U-statistic covariance decomposition, and verifies the closed forms for every \(2\le n\le10000\).

It also constructs the contrast kernel directly, verifies that its conditional expectation is constant as a polynomial identity, and checks the exact \(1/[90n(n-1)]\) variance and the strict squared-correlation monotonicity.

The finite loop is supplementary. The proof above establishes every \(n\ge2\).

## Relationship to prior work
Gerstenberger and Vogel compare Gini's mean difference with standard-deviation-based scale estimation. Their complete preprint gives the general finite-sample variance of the sample Gini mean difference, the exact finite-sample variance of empirical variance, and distribution-specific asymptotic efficiencies. For the uniform model their table reports equal asymptotic efficiency of Gini's mean difference and the standard deviation. The inspected article does not state their finite cross-covariance or a joint correlation formula. The projection identity above explains that asymptotic equality more sharply: after the natural normalization, the two relevant first-order components coincide pointwise.

Čiginas and Pumputis compare Gini's mean difference and empirical variance as degree-two U-statistics and derive their separate Hoeffding variance decompositions for finite-population sampling. The complete inspected preprint treats the two marginal decompositions separately and does not state a cross-covariance or joint law.

The exact covariance here is therefore not inferred from equality of two marginal efficiencies. It requires the mixed same-pair and one-overlap moments, and the degenerate contrast identifies why the uniform model is exceptional.

## Limitations
The exact proportionality of the first-order projections is specific to the uniform parent law. Other distributions generally give a nondegenerate first-order difference and a limiting correlation strictly below one.

The covariance calculation is an elementary order-two U-statistic argument once the mixed conditional moments are evaluated. Older Gini-mean-difference or U-statistic literature could contain the same mixed identity under different notation; no such statement was located in the inspected primary sources or exact-formula searches.

## References
1. C. Gerstenberger and D. Vogel, “On the efficiency of Gini's mean difference,” arXiv:1405.5027, first submitted 20 May 2014; later published in *Statistical Methods & Applications* 24 (2015), 569–596.
2. A. Čiginas and D. Pumputis, “Gini's mean difference and variance as measures of finite populations scales,” arXiv:1406.2275, first submitted 9 June 2014; later published in *Lithuanian Mathematical Journal* 55 (2015).
