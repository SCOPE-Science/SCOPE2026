# Exact local excedance covariance with rank scores and Spearman rho
## Finding
Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). For each position define the excedance indicator
\[
E_i=\mathbf 1\{\Pi(i)>i\},
\qquad 1\le i\le n,
\]
and let
\[
X_n=\sum_{i=1}^nE_i
\]
be the total number of excedances. For arbitrary deterministic real weights \(w_1,\ldots,w_n\), put
\[
L_w=\sum_{j=1}^nw_j\Pi(j),
\qquad
W=\sum_{j=1}^nw_j.
\]
Then every local excedance has the exact covariance law
\[
\boxed{
\operatorname{Cov}(E_i,L_w)
=
\frac{i(n-i)}{2n(n-1)}\left(nw_i-W\right).
}
\]
Thus the covariance with any linear rank score depends only on the current weight relative to the global mean weight.

For squared rank displacement
\[
D_n=\sum_{j=1}^n(\Pi(j)-j)^2
\]
and Spearman's no-ties rank coefficient
\[
R_n=1-\frac{6D_n}{n(n^2-1)},
\]
the local identities become
\[
\boxed{
\operatorname{Cov}(E_i,D_n)
=
\frac{i(n-i)(n+1-2i)}{2(n-1)}
}
\]
and
\[
\boxed{
\operatorname{Cov}(E_i,R_n)
=
-\frac{3i(n-i)(n+1-2i)}{n(n-1)^2(n+1)}.
}
\]
Because
\[
\mathbb P(E_i=1)=\frac{n-i}{n}
\qquad\text{and}\qquad
\mathbb ER_n=0,
\]
this is equivalently
\[
\boxed{
\mathbb E[R_n\mid E_i=1]
=
-\frac{3i(n+1-2i)}{(n-1)^2(n+1)}.
}
\]
The sign therefore reverses across the center: an excedance at an early position has negative conditional mean Spearman coefficient, an excedance at a late position has positive conditional mean, and when \(n\) is odd the central position \(i=(n+1)/2\) is exactly uncorrelated with \(R_n\).

Summing over positions yields
\[
\boxed{
\operatorname{Cov}(X_n,D_n)=\frac{n(n+1)}{12}
}
\]
and
\[
\boxed{
\operatorname{Cov}(X_n,R_n)=-\frac1{2(n-1)}.
}
\]
Since
\[
\operatorname{Var}(X_n)=\frac{n+1}{12},
\qquad
\operatorname{Var}(R_n)=\frac1{n-1},
\]
we obtain the exact correlation
\[
\boxed{
\operatorname{Corr}(X_n,R_n)
=-\sqrt{\frac{3}{n^2-1}}.
}
\]
Consequently
\[
n\,\operatorname{Corr}(X_n,R_n)\longrightarrow-\sqrt3.
\]

## Assumptions and scope
The permutation is uniform on the full symmetric group. Excedance means the position-wise event \(\Pi(i)>i\). The weight vector in the general covariance law is deterministic and arbitrary.

Spearman's coefficient is the ordinary complete-ranking statistic without ties. The theorem is a finite permutation-null statement and does not assert independence.

## Proof
Fix a position \(i\). Its excedance probability is
\[
\mathbb P(E_i=1)=\frac{n-i}{n}.
\]
Conditional on \(E_i=1\), the value \(\Pi(i)\) is uniform on
\[
\{i+1,\ldots,n\},
\]
so
\[
\mathbb E[\Pi(i)\mid E_i=1]
=
\frac{n+i+1}{2}.
\]
The unconditional mean of every coordinate is \((n+1)/2\), hence the conditional shift at the distinguished position is
\[
\frac{i}{2}.
\]
All other positions are exchangeable under the conditioning. Because the total permutation sum is deterministic,
\[
\sum_{j=1}^n\Pi(j)=\frac{n(n+1)}2,
\]
each position \(j\ne i\) has conditional mean
\[
\mathbb E[\Pi(j)\mid E_i=1]
=
\frac{n^2-i-1}{2(n-1)}
=
\frac{n+1}{2}-\frac{i}{2(n-1)}.
\]
Therefore
\[
\mathbb E[L_w\mid E_i=1]-\mathbb EL_w
=
\frac{i}{2(n-1)}\left(nw_i-W\right).
\]
For an indicator \(E_i\),
\[
\operatorname{Cov}(E_i,L_w)
=
\mathbb P(E_i=1)
\left(\mathbb E[L_w\mid E_i=1]-\mathbb EL_w\right),
\]
which proves the general local law.

Now set \(w_j=j\) and
\[
L=\sum_{j=1}^n j\Pi(j).
\]
Because a permutation preserves the sum of squares,
\[
D_n
=
2\sum_{j=1}^n j^2-2L.
\]
Also
\[
W=\frac{n(n+1)}2.
\]
Substitution into the local linear-score formula gives
\[
\operatorname{Cov}(E_i,L)
=
\frac{i(n-i)(2i-n-1)}{4(n-1)},
\]
so
\[
\operatorname{Cov}(E_i,D_n)
=
\frac{i(n-i)(n+1-2i)}{2(n-1)}.
\]
The affine definition of \(R_n\) then yields its local covariance and conditional-mean formulas.

The polynomial sum
\[
\sum_{i=1}^{n-1}i(n-i)(n+1-2i)
=
\frac{n(n-1)(n+1)}6
\]
gives
\[
\operatorname{Cov}(X_n,D_n)=\frac{n(n+1)}{12},
\]
and hence
\[
\operatorname{Cov}(X_n,R_n)=-\frac1{2(n-1)}.
\]

For completeness, the excedance variance follows directly from indicator covariances. For \(i<j\),
\[
\mathbb P(E_i=1,E_j=1)
=
\frac{(n-j)(n-i-1)}{n(n-1)},
\]
so
\[
\operatorname{Cov}(E_i,E_j)
=
-\frac{i(n-j)}{n^2(n-1)}.
\]
Together with
\[
\operatorname{Var}(E_i)=\frac{i(n-i)}{n^2},
\]
elementary summation gives
\[
\operatorname{Var}(X_n)=\frac{n+1}{12}.
\]

To verify the Spearman variance without appealing to an asymptotic result, let
\[
a_i=i-\frac{n+1}{2},
\qquad
Q=\sum_i a_i^2=\frac{n(n^2-1)}{12}.
\]
Then
\[
R_n=\frac1Q\sum_i a_i a_{\Pi(i)}.
\]
For distinct positions,
\[
\mathbb E[a_{\Pi(i)}a_{\Pi(j)}]
=-\frac{Q}{n(n-1)},
\]
while
\[
\mathbb E[a_{\Pi(i)}^2]=\frac Qn.
\]
Using \(\sum_i a_i=0\) gives
\[
\operatorname{Var}\left(\sum_i a_i a_{\Pi(i)}\right)
=
\frac{Q^2}{n-1},
\]
and therefore
\[
\operatorname{Var}(R_n)=\frac1{n-1}.
\]
Combining the two variances with the covariance proves the correlation formula.

## Verification
The accompanying `checker.py` exhaustively enumerates every permutation for \(2\le n\le9\). It checks the local covariance law for four distinct weight families, including a constant-weight zero-covariance case, and separately checks every local squared-displacement and Spearman identity, the global covariances, both marginal variances, and the exact correlation-squared formula.

A second exact-rational loop checks the closed conditional means, the pairwise excedance probabilities, and the summed variance identities through \(n=1000\) without permutation enumeration.

The universal theorem is proved analytically above; finite enumeration is only a replay check.

## Relationship to prior work
Excedances are a classical Eulerian permutation statistic, and the literature develops their distributions, excedance sets, and interactions with other permutation statistics. Hultman's complete article explicitly defines excedance and weak excedance statistics in a broad character-theoretic study of permutation statistics, but it does not introduce Spearman rank displacement.

Jiang studies statistical dependence among permutation metrics and treats the Spearman family in detail, motivated in part by redundancy among ranking summaries. Searches of the complete article found no excedance statistic. Thus the two closest strands separately cover the Eulerian statistic and the Spearman metric, but not their finite joint covariance.

Modern work on multivariate Eulerian polynomials also places Eulerian permutation statistics in a probabilistic setting. The present result adds a position-resolved mixed-moment law: an excedance couples to every linear rank score through one centered weight, and the Spearman specialization exhibits an exact sign reversal across positions.

## Limitations
The formulas assume a uniform random permutation. They need not hold under pattern restrictions, Mallows-type laws, or other nonuniform permutation models.

The result concerns covariance and correlation, not the complete joint distribution of excedance count and Spearman's coefficient.

The local conditional argument is elementary, so an equivalent identity may exist in older Eulerian or rank-statistics literature under different notation. Targeted searches and the closest inspected full texts did not locate it.

## References
1. Y. Jiang, “Asymptotic correlations of metrics on the symmetric groups,” arXiv:1110.0807, first submitted 4 October 2011.
2. A. Hultman, “Permutation statistics of products of random permutations,” arXiv:1301.0430, first submitted 3 January 2013.
3. P. Brändén, M. Leander, and M. Visontai, “Multivariate Eulerian Polynomials and Exclusion Processes,” *Combinatorics, Probability and Computing* 25 (2016), 498–514. DOI: 10.1017/S0963548316000031.
4. R. Ehrenborg and E. Steingrímsson, “The excedance set of a permutation,” *Advances in Applied Mathematics* 24 (2000), 284–299.
