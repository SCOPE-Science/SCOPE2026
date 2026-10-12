# Uniform local descent covariance with Spearman's rho
## Finding
Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). For
\[
1\le i<n,
\]
put
\[
I_i=\mathbf 1\{\Pi(i)>\Pi(i+1)\},
\]
and let
\[
A_n=\sum_{i=1}^{n-1}I_i
\]
be the total number of descents. Define squared rank displacement
\[
D_n=\sum_{j=1}^n(\Pi(j)-j)^2
\]
and Spearman's no-ties rank coefficient
\[
R_n=1-\frac{6D_n}{n(n^2-1)}.
\]

Every adjacent position has the same exact covariance with the global squared displacement:
\[
\boxed{
\operatorname{Cov}(I_i,D_n)=\frac{n+1}{6}
}
\qquad(1\le i<n).
\]
Equivalently,
\[
\boxed{
\operatorname{Cov}(I_i,R_n)=-\frac1{n(n-1)}
}.
\]
Because
\[
\mathbb P(I_i=1)=\frac12
\qquad\text{and}\qquad
\mathbb E R_n=0,
\]
this local covariance is the conditional-mean identity
\[
\boxed{
\mathbb E[R_n\mid I_i=1]=-\frac{2}{n(n-1)},
\qquad
\mathbb E[R_n\mid I_i=0]=\frac{2}{n(n-1)}.
}
\]
Thus a descent at any adjacent position has exactly the same mean effect on Spearman's coefficient, including positions near the boundary.

Summing the local identities gives
\[
\boxed{
\operatorname{Cov}(A_n,D_n)=\frac{n^2-1}{6}
}
\]
and
\[
\boxed{
\operatorname{Cov}(A_n,R_n)=-\frac1n.
}
\]
Using
\[
\operatorname{Var}(A_n)=\frac{n+1}{12},
\qquad
\operatorname{Var}(R_n)=\frac1{n-1},
\]
one obtains
\[
\boxed{
\operatorname{Corr}(A_n,R_n)
=
-\frac1n\sqrt{\frac{12(n-1)}{n+1}}.
}
\]
Consequently
\[
n\,\operatorname{Corr}(A_n,R_n)\longrightarrow-2\sqrt3.
\]
The descent count and Spearman's coefficient are therefore asymptotically uncorrelated, but with an exact first-order correlation scale \(n^{-1}\).

## Assumptions and scope
The probability law is uniform over all \(n!\) permutations. This is the usual no-ties permutation null for two complete rankings.

A descent is the local event \(\Pi(i)>\Pi(i+1)\). Spearman's coefficient uses squared rank displacement. The theorem does not cover tied ranks, partial rankings, weighted descents, or nonuniform permutation laws.

The local statement is stronger than the global covariance: it identifies the contribution of every adjacent position separately and shows that the conditional mean shift is position-independent.

## Proof
Set
\[
L_n=\sum_{j=1}^n j\,\Pi(j).
\]
Since
\[
\sum_j\Pi(j)^2=\sum_j j^2,
\]
we have
\[
D_n=2\sum_{j=1}^n j^2-2L_n.
\]
Hence \(R_n\) is also affine in \(L_n\):
\[
R_n=
1-\frac{12\sum_jj^2}{n(n^2-1)}
+\frac{12L_n}{n(n^2-1)}.
\]

Fix \(i\). Conditional on \(I_i=1\), the ordered pair
\[
(\Pi(i),\Pi(i+1))
\]
is obtained by choosing an unordered two-element subset of \(\{1,\ldots,n\}\) uniformly and placing its larger element first. The expected larger and smaller values are
\[
\mathbb E[\Pi(i)\mid I_i=1]=\frac{2(n+1)}3,
\]
\[
\mathbb E[\Pi(i+1)\mid I_i=1]=\frac{n+1}3.
\]
Every other position has conditional mean \((n+1)/2\). Relative to the unconditional mean \((n+1)/2\), the two affected positions therefore shift by
\[
+\frac{n+1}{6}
\qquad\text{and}\qquad
-\frac{n+1}{6}.
\]
It follows that
\[
\mathbb E[L_n\mid I_i=1]-\mathbb E L_n
=
i\frac{n+1}{6}
-(i+1)\frac{n+1}{6}
=
-\frac{n+1}{6}.
\]
The cancellation of \(i\) is the source of the position-independence.

Since \(\mathbb P(I_i=1)=1/2\),
\[
\operatorname{Cov}(I_i,L_n)
=
\frac12
\left(
\mathbb E[L_n\mid I_i=1]-\mathbb E L_n
\right)
=
-\frac{n+1}{12}.
\]
The affine formulas now give
\[
\operatorname{Cov}(I_i,D_n)
=
-2\operatorname{Cov}(I_i,L_n)
=
\frac{n+1}{6},
\]
and
\[
\operatorname{Cov}(I_i,R_n)
=
\frac{12}{n(n^2-1)}
\operatorname{Cov}(I_i,L_n)
=
-\frac1{n(n-1)}.
\]
Because \(\mathbb E R_n=0\), the two conditional means follow from
\[
\operatorname{Cov}(I_i,R_n)
=
\frac12\mathbb E[R_n\mid I_i=1]
\]
and the law of total expectation.

Summing over \(i\) proves the two global covariance identities.

For completeness, the descent-indicator calculation gives
\[
\operatorname{Var}(A_n)=\frac{n+1}{12}.
\]
Indeed, each indicator has variance \(1/4\), adjacent indicators have covariance \(-1/12\), and nonadjacent indicators are independent.

To obtain the Spearman variance directly, note that under a uniform permutation
\[
\operatorname{Var}(\Pi(j))=\frac{n^2-1}{12},
\qquad
\operatorname{Cov}(\Pi(j),\Pi(k))=-\frac{n+1}{12}
\quad(j\ne k).
\]
Centering the deterministic coefficients \(j\) in \(L_n\) yields
\[
\operatorname{Var}(L_n)
=
\frac{n^2(n-1)(n+1)^2}{144}.
\]
Therefore
\[
\operatorname{Var}(D_n)
=
4\operatorname{Var}(L_n)
=
\frac{n^2(n-1)(n+1)^2}{36},
\]
and the affine normalization of \(R_n\) gives
\[
\operatorname{Var}(R_n)=\frac1{n-1}.
\]
Combining the variances with \(\operatorname{Cov}(A_n,R_n)=-1/n\) proves the correlation formula and its limit.

## Verification
The accompanying `checker.py` uses exact rational arithmetic.

For every \(2\le n\le9\), it exhaustively enumerates all permutations and checks every local covariance, both local conditional means, the two global covariances, the two marginal variances, and the correlation-squared identity.

A second check, independent of permutation enumeration, evaluates the conditional expected maximum and minimum of a uniformly chosen two-element subset and reconstructs the conditional \(L_n\) shift for every position through \(n=500\).

The finite checks are supplementary. The proof above establishes every \(n\ge2\).

## Relationship to prior work
Conger studies the joint distribution of the first permutation value and the number of descents, including exact conditional expectations when the descent count is fixed. That work develops refined Eulerian information about local ordering but does not state a joint law with Spearman's squared rank displacement.

Jiang studies joint asymptotic relationships among permutation metrics and treats the Spearman family, including the squared-displacement statistic underlying Spearman's coefficient. The complete inspected article contains no descent statistic.

The present identity links these two classical directions: a local Eulerian statistic has a position-independent exact covariance with the global Spearman statistic, and summation yields an exact \(n^{-1}\) correlation law for the total descent count.

## Limitations
The covariance is a null-distribution identity. It does not compare the power of descent-based and Spearman-based tests under structured alternatives.

The proof is short once the conditional two-position means are recognized. An equivalent covariance may occur in older permutation-statistics literature under different notation; targeted searches and the closest inspected primary sources did not locate it.

## References
1. M. Conger, “A Refinement of the Eulerian Numbers, and the Joint Distribution of \(\Pi(1)\) and \(\operatorname{Des}(\Pi)\) in \(S_n\),” arXiv:math/0508112, first submitted 5 August 2005.
2. Y. Jiang, “Asymptotic correlations of metrics on the symmetric groups,” arXiv:1110.0807, first submitted 4 October 2011.
