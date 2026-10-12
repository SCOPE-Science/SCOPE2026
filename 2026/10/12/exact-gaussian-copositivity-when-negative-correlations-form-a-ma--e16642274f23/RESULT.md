# Exact Gaussian copositivity when negative correlations form a matching
## Finding
Let \(X=(X_1,\ldots,X_d)\) be a centered Gaussian vector with unit marginal variances and correlation matrix
\[
R=(\rho_{ij}).
\]
Assume that the graph whose edges are the negatively correlated pairs,
\[
E_-=\{\{i,j\}:\rho_{ij}<0\},
\]
is a matching: every coordinate is incident to at most one edge of \(E_-\). Define
\[
\rho_*=\min\!\left(0,\min_{i<j}\rho_{ij}\right).
\]
For the distribution-copositivity coefficient introduced by Sei,
\[
\beta(\mu)=
\inf_{0\ne T\in\mathcal T_{\mathrm{cw}*}(\mu)}
\frac{\left\|\sum_iT_i(X_i)\right\|_2^2}
{\sum_i\|T_i(X_i)\|_2^2},
\]
where each \(T_i\) is nondecreasing, centered, and square-integrable, one has
\[
\boxed{\beta(\mu)=1+\rho_*}.
\]
The matrix strict-copositivity constant of the same correlation matrix,
\[
\alpha(R)=
\inf_{w_1,\ldots,w_d>0}
\frac{w^\top Rw}{\sum_iw_i^2},
\]
has the identical value
\[
\boxed{\alpha(R)=1+\rho_*}.
\]
Thus
\[
\beta(\mu)=\alpha(R)
\]
throughout this class. In particular, the Gaussian law is copositive exactly when
\[
\rho_*>-1.
\]

This verifies Sei's Gaussian copositivity conjecture, and the stronger coefficient-equality conjecture stated in the same paper, for every Gaussian correlation matrix whose negative-correlation graph is a matching. The class includes singular correlation matrices.

## Assumptions and scope
The Gaussian vector is centered and every marginal variance is one. This normalization is harmless for \(\beta\): Sei proves that the coefficient is invariant under coordinate-wise transformations, and positive marginal rescaling converts any nondegenerate Gaussian marginal to unit variance.

The joint Gaussian law may be singular. The only structural hypothesis is that no coordinate has negative correlation with two different coordinates. Positive correlations are unrestricted subject to positive semidefiniteness of \(R\).

The theorem does not settle Sei's conjecture for arbitrary signed correlation patterns. In particular, it does not cover a vertex incident to two or more negative-correlation edges.

## Proof
For each admissible coordinate transform, write
\[
Y_i=T_i(X_i),\qquad
s_i=\|Y_i\|_2.
\]
The variables \(Y_i\) are centered.

First consider a pair with
\[
\rho_{ij}\ge0.
\]
For a bivariate standard Gaussian pair with nonnegative correlation, covariance of nondecreasing square-integrable functions is nonnegative. A direct proof is available without any multivariate association theorem. Write
\[
X_j=\rho_{ij}X_i+\sqrt{1-\rho_{ij}^2}\,Z
\]
with \(Z\) independent standard normal. If
\[
h(x)=\mathbb E[T_j(\rho_{ij}x+\sqrt{1-\rho_{ij}^2}\,Z)],
\]
then \(h\) is nondecreasing. For an independent copy \(X_i'\),
\[
\operatorname{Cov}(T_i(X_i),h(X_i))
=
\frac12\mathbb E[
(T_i(X_i)-T_i(X_i'))
(h(X_i)-h(X_i'))
]\ge0.
\]
Hence
\[
\operatorname{Cov}(Y_i,Y_j)\ge0.
\tag{1}
\]

Now suppose
\[
\rho_{ij}<0.
\]
The Gaussian maximal-correlation bound gives
\[
|\operatorname{Cov}(Y_i,Y_j)|
\le
|\rho_{ij}|s_is_j.
\tag{2}
\]
For completeness, expand centered square-integrable functions in the probabilists' Hermite basis:
\[
T_i(x)=\sum_{k\ge1}a_kH_k(x),\qquad
T_j(x)=\sum_{k\ge1}b_kH_k(x).
\]
Then
\[
\operatorname{Cov}(Y_i,Y_j)
=
\sum_{k\ge1}k!a_kb_k\rho_{ij}^k.
\]
Because
\[
|\rho_{ij}|^k\le|\rho_{ij}|,
\]
Cauchy--Schwarz gives (2). Since \(\rho_{ij}<0\), equation (2) implies
\[
\operatorname{Cov}(Y_i,Y_j)
\ge
\rho_{ij}s_is_j.
\tag{3}
\]

Combining (1) and (3),
\[
\operatorname{Var}\!\left(\sum_iY_i\right)
\ge
\sum_i s_i^2+
2\sum_{\{i,j\}\in E_-}\rho_{ij}s_is_j.
\tag{4}
\]
Because \(E_-\) is a matching, the quadratic form on the right decomposes into disjoint two-coordinate blocks and isolated coordinates. For each negative edge,
\[
s_i^2+s_j^2+2\rho_{ij}s_is_j
-
(1+\rho_{ij})(s_i^2+s_j^2)
=
-\rho_{ij}(s_i-s_j)^2\ge0.
\]
Since
\[
\rho_{ij}\ge\rho_*,
\]
every such block is at least
\[
(1+\rho_*)(s_i^2+s_j^2).
\]
Each isolated coordinate contributes
\[
s_i^2\ge(1+\rho_*)s_i^2.
\]
Therefore (4) yields
\[
\operatorname{Var}\!\left(\sum_iY_i\right)
\ge
(1+\rho_*)\sum_i s_i^2.
\]
Taking the infimum over admissible nonzero transforms gives
\[
\beta(\mu)\ge1+\rho_*.
\tag{5}
\]

If \(\rho_*<0\), choose a pair \((p,q)\) with
\[
\rho_{pq}=\rho_*,
\]
take
\[
T_p(x)=x,\qquad T_q(x)=x,
\]
and take all other coordinate transforms equal to zero. Sei's extended class \(\mathcal T_{\mathrm{cw}*}\) permits such constant coordinates. The quotient is
\[
\frac{\operatorname{Var}(X_p+X_q)}{2}
=
1+\rho_*.
\]
If there are no negative correlations, use only one nonzero coordinate, giving quotient one. Thus
\[
\beta(\mu)\le1+\rho_*,
\]
which together with (5) proves
\[
\beta(\mu)=1+\rho_*.
\tag{6}
\]

The matrix identity is parallel. For every positive vector \(w\), discard the nonnegative off-diagonal terms:
\[
w^\top Rw
\ge
\sum_iw_i^2+
2\sum_{\{i,j\}\in E_-}\rho_{ij}w_iw_j
\ge
(1+\rho_*)\sum_iw_i^2.
\]
Hence
\[
\alpha(R)\ge1+\rho_*.
\]
If \(\rho_*<0\), choose equal weights on a most-negative pair and let all other positive weights tend to zero. If there is no negative edge, make one weight dominant and let the rest tend to zero. This proves
\[
\alpha(R)\le1+\rho_*.
\]
Therefore
\[
\alpha(R)=\beta(\mu)=1+\rho_*.
\]

A concrete singular family is obtained from independent standard normals \(U,V\):
\[
X_1=U,\qquad
X_2=V,\qquad
X_3=\cos\theta\,U-\sin\theta\,V,
\qquad 0<\theta<\frac{\pi}{2}.
\]
Its correlation matrix is
\[
R_\theta=
\begin{pmatrix}
1&0&\cos\theta\\
0&1&-\sin\theta\\
\cos\theta&-\sin\theta&1
\end{pmatrix}.
\]
It has rank two, and its only negative edge is \(\{2,3\}\). Consequently,
\[
\beta(\mu)=\alpha(R_\theta)=1-\sin\theta>0.
\]
This is a continuous family of singular Gaussian laws covered by the result.

## Verification
The proof is analytic and applies to every dimension and every positive-semidefinite correlation matrix satisfying the matching hypothesis.

The bundled `verify.py` checks three algebraic components independently. It verifies the two-coordinate block inequality in exact rational arithmetic over a deterministic grid; verifies finite Hermite expansions against the Gaussian maximal-correlation inequality in exact rational arithmetic; and checks the singular example
\[
\cos\theta=\frac35,\qquad
\sin\theta=\frac45,
\]
for which
\[
\det R_\theta=0,\qquad
\beta(\mu)=\alpha(R_\theta)=\frac15.
\]
A successful replay ends with
`VERIFY_OK block_cases=1764 hermite_cases=192 singular_beta=1/5`.

These finite checks are reproducibility checks only; they are not used to establish the infinite theorem.

## Relationship to prior work
Sei introduced the distribution-copositivity coefficient \(\beta(\mu)\), proved that it is invariant under coordinate-wise transformations, and observed that it depends only on the collection of bivariate marginal copulas. For Gaussian laws, the paper computes the relaxed coefficient \(\beta_{\mathrm L}(\mu)\) as the minimum eigenvalue of the correlation matrix, which proves copositivity when the Gaussian covariance is nonsingular.

The same paper explicitly leaves the singular case open as Conjecture 4: a Gaussian distribution should be copositive whenever its covariance matrix is strictly copositive. It also conjectures, for Gaussian laws, equality between \(\beta(\mu)\) and the matrix copositivity expression used in its linear scaling theorem. The theorem above verifies both statements on the negative-matching class and supplies the exact coefficient.

The proof uses only two pairwise Gaussian facts: nonnegative correlation preserves nonnegative covariance for increasing transforms, and the absolute covariance of arbitrary centered square-integrable transforms is bounded by the Gaussian maximal-correlation coefficient. Both are compatible with the Hermite-expansion machinery already used in Sei's Gaussian appendix.

Targeted searches for the source title, Conjecture 4, Gaussian copositive distributions, negative-correlation matchings, maximal-correlation formulations, and the exact coefficient \(1+\rho_*\) did not locate a published result implying this matching-graph theorem.

## Limitations
The negative-correlation graph must be a matching. The method does not determine \(\beta(\mu)\) when a coordinate participates in multiple negative edges, because then the pairwise lower bounds no longer separate into disjoint two-coordinate blocks.

Search noncoverage is evidence rather than proof of bibliographic uniqueness. A short equivalent argument may exist under classical Gaussian association, maximal-correlation, or signed-correlation terminology not indexed together with distribution copositivity.

## References
1. T. Sei, “Coordinate-wise transformation of probability distributions to achieve a Stein-type identity,” *Information Geometry* 5 (2022), 325–354. First published online 28 June 2021. DOI: 10.1007/s41884-021-00051-9.
2. H. O. Lancaster, “Some properties of the bivariate normal distribution considered in the form of a contingency table,” *Biometrika* 44 (1957), 289–292. Cited in Sei's discussion of Gaussian maximal correlation.
