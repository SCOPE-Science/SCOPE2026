# Weibull limit for the natural support-boundary estimator in \(L_p\)-spherical copulas
## Finding
Let \(d\ge2\) and \(p>d-1\). Let
\[
X^{(1)},\ldots,X^{(M)}
\]
be iid observations from the \(d\)-dimensional positive \(L_p\)-norm spherical copula. Define
\[
\widehat p_M
=
\inf\left\{q>d-1:\ \|X^{(j)}\|_q<1
\text{ for all }j=1,\ldots,M\right\}.
\]
This is the support-boundary statistic proposed as a natural estimator in the motivating paper whenever at least one observation excludes values of \(q\) near \(d-1\); the definition above also covers the complementary finite-sample case by allowing the infimum to equal \(d-1\).

Set
\[
b=1-\frac{d-1}{p},
\qquad
W\sim\operatorname{Dirichlet}\!\left(\frac1p,\ldots,\frac1p\right),
\]
and write
\[
H(W)=-\sum_{i=1}^d W_i\log W_i,
\qquad 0\log0:=0.
\]
Define
\[
\kappa_{d,p}
=
\frac{\mathbb E[(H(W)/p)^b]}
{b\,B(d/p,b)}.
\]
Then
\[
\widehat p_M\longrightarrow p
\quad\text{almost surely},
\]
and
\[
M^{1/b}(p-\widehat p_M)
\Rightarrow T_{d,p},
\]
where
\[
\Pr\{T_{d,p}>x\}
=
\exp(-\kappa_{d,p}x^b),
\qquad x\ge0.
\]
Thus the estimator has the nonregular rate
\[
M^{-1/b}=M^{-p/(p-d+1)}.
\]

For the bivariate Euclidean case \(d=2\), \(p=2\),
\[
b=\frac12
\]
and
\[
\kappa_{2,2}
=
\mathbb E\!\left[
\sqrt{\frac{-W\log W-(1-W)\log(1-W)}{2}}
\right],
\qquad
W\sim\operatorname{Beta}\!\left(\frac12,\frac12\right),
\]
which numerically equals
\[
\kappa_{2,2}=0.4061168441\ldots .
\]
Hence \(M^2(2-\widehat p_M)\) has the stated Weibull-type limit.

## Assumptions and scope
The dimension \(d\) is fixed and \(p>d-1\). The observations are exactly iid from the positive \(L_p\)-norm spherical copula with uniform \((0,1)\) margins. The result concerns the support-boundary statistic \(\widehat p_M\), not a regularized maximum-likelihood estimator and not the circular version of the copula.

The limiting law is stated for the true finite parameter \(p\). The endpoint case \(p=d-1\), where the radial variable is identically one, and the limit \(p=\infty\) require different formulations.

## Proof
The stochastic representation in the motivating paper is
\[
X=RU,
\]
where \(R\) is independent of the positive \(L_p\)-sphere direction \(U\), and
\[
Y:=R^p
\sim
\operatorname{Beta}(a,b),
\qquad
a=\frac{d}{p},
\qquad
b=1-\frac{d-1}{p}.
\tag{1}
\]
Using the standard \(p\)-generalized-normal construction of the same direction, the vector
\[
W=(U_1^p,\ldots,U_d^p)
\]
has the Dirichlet law
\[
W\sim\operatorname{Dirichlet}\!\left(\frac1p,\ldots,\frac1p\right).
\tag{2}
\]

For one observation \(X\), define
\[
Q(X)
=
\inf\{q>d-1:\|X\|_q<1\}.
\]
Then
\[
\widehat p_M=\max_{1\le j\le M}Q(X^{(j)}).
\tag{3}
\]
Since \(X\) lies strictly inside the \(L_p\) unit ball almost surely, continuity of \(q\mapsto\|X\|_q\) gives \(Q(X)<p\) almost surely.

Fix \(t>0\) sufficiently small that \(p-t>d-1\). Conditional on \(U\),
\[
Q(X)>p-t
\]
is equivalent, up to a null boundary event, to
\[
R>
r_t(U)
:=
\left(\sum_{i=1}^d U_i^{p-t}\right)^{-1/(p-t)}.
\]
In terms of \(W_i=U_i^p\),
\[
r_t(U)^p
=
\left(
\sum_{i=1}^d W_i^{\,1-t/p}
\right)^{-p/(p-t)}.
\]
Put
\[
z_t(W)=1-r_t(U)^p.
\]
Differentiating at \(t=0\), where \(\sum_iW_i=1\), gives
\[
\frac{z_t(W)}{t}
\longrightarrow
\frac{H(W)}{p}.
\tag{4}
\]

This convergence can be averaged without an unproved interchange. If
\[
\alpha=1-\frac{t}{p},
\]
then the power-sum inequality gives
\[
\sum_{i=1}^dW_i^\alpha
\le d^{1-\alpha}.
\]
Since \(1-e^{-x}\le x\),
\[
0\le
\frac{z_t(W)}{t}
\le
\frac{\log d}{p-t}.
\tag{5}
\]
Thus the relevant powers of \(z_t(W)/t\) are uniformly bounded for small \(t\).

From the beta law (1),
\[
\Pr\{Y>1-z\}
\sim
\frac{z^b}{b\,B(a,b)}
\qquad(z\downarrow0).
\tag{6}
\]
Combining (4), (5), (6), and dominated convergence yields the one-observation endpoint expansion
\[
\Pr\{Q(X)>p-t\}
=
\kappa_{d,p}t^b+o(t^b),
\tag{7}
\]
where
\[
\kappa_{d,p}
=
\frac{\mathbb E[(H(W)/p)^b]}
{b\,B(d/p,b)}.
\]

Equation (7) first gives strong consistency. For every fixed \(\varepsilon>0\),
\[
\Pr\{Q(X)>p-\varepsilon\}>0.
\]
Therefore the iid maximum in (3) eventually exceeds \(p-\varepsilon\) almost surely, while it is always below \(p\). Hence
\[
\widehat p_M\to p
\quad\text{almost surely}.
\]

Finally, for fixed \(x\ge0\), put
\[
t_M=xM^{-1/b}.
\]
By independence and (7),
\[
\Pr\!\left\{
M^{1/b}(p-\widehat p_M)>x
\right\}
=
\left[
1-\kappa_{d,p}\frac{x^b}{M}
+o(M^{-1})
\right]^M,
\]
which converges to
\[
e^{-\kappa_{d,p}x^b}.
\]
This is exactly the claimed Weibull-type limit.

For \(d=2\), \(p=2\), one has \(a=1\), \(b=1/2\) and
\[
W\sim\operatorname{Beta}\!\left(\frac12,\frac12\right),
\]
giving the displayed one-dimensional formula for \(\kappa_{2,2}\).

## Verification
The bundled `verify.py` uses only the Python standard library. It independently evaluates the \(d=2,p=2\) constant after the substitution \(W=\sin^2\theta\), checks the finite-\(t\) one-observation endpoint probability against its predicted \(\sqrt t\) law, and checks the directional derivative
\[
\frac{z_t(W)}{t}\to\frac{H(W)}{p}
\]
at several deterministic points.

A successful run ends with a line beginning
`VERIFY_OK kappa_2_2=0.4061168441`.

These numerical checks are not used to prove the infinite-sample limit.

## Relationship to prior work
Bernard, Müller, and Oesting characterize positive \(L_p\)-norm spherical copulas, prove the radial law
\[
R^p\sim
\operatorname{Beta}\!\left(\frac{d}{p},1-\frac{d-1}{p}\right),
\]
and give the explicit support-dependent density. In their inference discussion they define the same support boundary
\[
p^*
=
\inf\{q>d-1:\|x^{(j)}\|_q<1\text{ for every observation }j\}
\]
when the data restrict the admissible parameter set. They observe that the likelihood can diverge as \(q\downarrow p^*\), so an ordinary maximum-likelihood estimator need not exist, and state that \(p^*\) can be viewed as a natural estimator. The inspected manuscript does not derive consistency, a convergence rate, or a limiting distribution for this estimator.

Smith's general theory of nonregular likelihood problems explains why moving-support parameters can have non-Gaussian asymptotics. Its accessible abstract treats scalar support boundaries with local power-law densities. It does not state the present copula-specific statistic, the dimension-dependent exponent \(p/(p-d+1)\), or the entropy-mixture constant \(\kappa_{d,p}\). The full Smith paper was not available in the inspected public material, so possible implication through a sufficiently general theorem remains a bibliographic risk.

A 2024 paper on uniform and radial Dirichlet copulas revisits related radial copulas and their Dirichlet structure. Its searchable full text contains no estimation or inference discussion, and no asymptotic law for the support-boundary statistic was located.

Targeted searches for the estimator, its support-boundary formulation, the Weibull rate, and the Dirichlet-entropy constant did not locate a published statement implying (7) or the sample limit.

## Limitations
The theorem assumes the exact positive \(L_p\)-norm spherical copula model and a fixed finite \(p>d-1\). It does not analyze efficiency, bias correction, robustness to copula misspecification, or a regularized likelihood estimator.

The constant \(\kappa_{d,p}\) is explicit as a Dirichlet expectation but generally is not reduced to elementary special functions. The numerical decimal for \(d=2,p=2\) is a quadrature value, not part of the proof.

## References
1. C. Bernard, A. Müller, and M. Oesting, “\(L_p\)-norm spherical copulas,” arXiv:2206.10180v1, 21 June 2022; *Journal of Multivariate Analysis* 201 (2024), 105262. DOI: 10.1016/j.jmva.2023.105262.
2. R. L. Smith, “Maximum likelihood estimation in a class of nonregular cases,” *Biometrika* 72 (1985), 67–90. DOI: 10.1093/biomet/72.1.67.
3. D. Sundgren, “Uniform and radial Dirichlet copulas,” Research Square preprint, 16 January 2024. DOI: 10.21203/rs.3.rs-3857082/v1.
