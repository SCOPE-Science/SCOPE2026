# Exact permutation-null correlation of Spearman footrule and rho
## Finding
Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). Define Spearman's footrule
\[
F_n=\sum_{i=1}^n|\Pi(i)-i|,
\]
the squared-displacement statistic
\[
D_n=\sum_{i=1}^n(\Pi(i)-i)^2,
\]
and the no-ties Spearman rank coefficient
\[
R_n=1-\frac{6D_n}{n(n^2-1)}.
\]
Then
\[
\mathbb EF_n=\frac{n^2-1}{3},
\qquad
\operatorname{Var}(F_n)=\frac{(n+1)(2n^2+7)}{45},
\]
and
\[
\boxed{\operatorname{Cov}(F_n,D_n)=\frac{n(n+1)(n^2+1)}{30}}.
\]
Consequently
\[
\boxed{\operatorname{Cov}(F_n,R_n)=-\frac{n^2+1}{5(n-1)}}
\]
and, because
\[
\operatorname{Var}(R_n)=\frac1{n-1},
\]
\[
\boxed{
\operatorname{Corr}(F_n,R_n)
=
-\frac{3(n^2+1)}
{\sqrt{5(n-1)(n+1)(2n^2+7)}}
}.
\]
Thus
\[
\operatorname{Corr}(F_n,R_n)\longrightarrow-\frac3{\sqrt{10}}.
\]
The two classical rank-disagreement summaries therefore remain strongly anticorrelated after standardization under the permutation null.

## Assumptions and scope
The probability law is uniform over all \(n!\) permutations, corresponding to the relative ordering of two complete rankings without ties. The result concerns the ordinary \(L^1\) footrule and the ordinary squared-rank-displacement form of Spearman's coefficient. It does not cover ties, partial rankings, weighted footrules, or nonuniform permutation laws.

## Proof
For an \(n\times n\) array \(A=(a_{ij})\), define
\[
X_A=\sum_{i=1}^n a_{i,\Pi(i)}.
\]
Let
\[
a_{i\bullet}=\frac1n\sum_j a_{ij},
\qquad
a_{\bullet j}=\frac1n\sum_i a_{ij},
\qquad
a_{\bullet\bullet}=\frac1{n^2}\sum_{i,j}a_{ij},
\]
and define the doubly centered array
\[
a^\circ_{ij}=a_{ij}-a_{i\bullet}-a_{\bullet j}+a_{\bullet\bullet}.
\]
For any two arrays \(A,B\), expansion under a uniform permutation gives
\[
\operatorname{Cov}(X_A,X_B)
=
\frac1{n-1}\sum_{i,j}a^\circ_{ij}b^\circ_{ij}.
\]
To verify this identity, first double-center so all row and column sums vanish. Same-row selection contributes
\[
\frac1n\sum_{i,j}a^\circ_{ij}b^\circ_{ij}.
\]
For different rows, summing over different columns and using the zero row and column sums converts the four-index sum to the same centered inner product with coefficient \(1/[n(n-1)]\). Adding the two contributions yields the displayed covariance formula.

Apply this with
\[
a_{ij}=(i-j)^2,
\qquad
b_{ij}=|i-j|.
\]
The elementary sums are
\[
\sum_{i,j}|i-j|=\frac{n(n^2-1)}3,
\]
\[
\sum_{i,j}(i-j)^2=\frac{n^2(n^2-1)}6,
\]
\[
\sum_{i,j}|i-j|^3
=
\frac{n(n^2-1)(3n^2-2)}{30}.
\]
The row sums are
\[
r_a(i)=
\frac n6\left(6i^2-6i(n+1)+2n^2+3n+1\right),
\]
\[
r_b(i)=
\frac12\left(2i^2-2i(n+1)+n^2+n\right),
\]
and
\[
\sum_i r_a(i)r_b(i)
=
\frac{n^2(n^2-1)(11n^2-14)}{180}.
\]
Because both arrays are symmetric,
\[
\sum_{i,j}a^\circ_{ij}b^\circ_{ij}
=
\sum_{i,j}a_{ij}b_{ij}
-\frac2n\sum_i r_a(i)r_b(i)
+\frac1{n^2}
\left(\sum_{i,j}a_{ij}\right)
\left(\sum_{i,j}b_{ij}\right).
\]
Substitution simplifies to
\[
\sum_{i,j}a^\circ_{ij}b^\circ_{ij}
=
\frac{n(n-1)(n+1)(n^2+1)}{30},
\]
so
\[
\operatorname{Cov}(F_n,D_n)
=
\frac{n(n+1)(n^2+1)}{30}.
\]

For the footrule variance, the same calculation with \(A=B=(|i-j|)\), together with
\[
\sum_i r_b(i)^2
=
\frac{n(n^2-1)(7n^2-8)}{60},
\]
gives
\[
\operatorname{Var}(F_n)
=
\frac{(n+1)(2n^2+7)}{45}.
\]
The analogous squared-displacement calculation gives
\[
\operatorname{Var}(D_n)
=
\frac{n^2(n-1)(n+1)^2}{36}.
\]
Since
\[
R_n=1-\frac{6D_n}{n(n^2-1)},
\]
the covariance, variance, correlation, and limiting correlation follow directly.

## Verification
The accompanying `checker.py` performs two exact checks. First, for every \(2\le n\le9\), it enumerates every permutation and verifies the displayed means, variances, covariance, and correlation-squared identity using rational arithmetic. Second, for every \(2\le n\le60\), it constructs the two distance arrays, double-centers them exactly, and verifies the covariance and variance formulas from the permutation-linear-statistic identity.

The analytic proof establishes every \(n\ge2\); the finite computations are supplementary.

## Relationship to prior work
Jiang studies joint asymptotic relationships among metrics on symmetric groups. In the complete article, the Spearman-family section explicitly defines the footrule \(L^1\) statistic and squared \(L^2\) displacement statistic and notes that correlations among the general family can be computed by splitting same-index and different-index terms. The inspected text does not state the exact finite covariance or correlation formula above.

Diaconis and Graham established the statistical theory of Spearman's footrule, including its mean, variance, asymptotic normality, and comparisons with other permutation metrics. A verified complete article text was not available in the retrieval paths used here.

Berry and Mielke later compare the footrule with Spearman's rank-order coefficient as agreement measures. Only abstract-level material was available during this comparison, so that article remains a specific residual coverage risk.

## Limitations
The result is an exact null relationship between two complete-ranking statistics; it is not a power comparison under structured alternatives. The covariance calculation is a specialization of the general double-centering identity for permutation linear statistics. Its contribution is the explicit all-\(n\) coefficient and the resulting null redundancy profile.

A complete inspection of the Berry-Mielke comparison article was unavailable, and an equivalent formula in that paper or older unindexed rank-statistics literature cannot be excluded.

## References
1. Y. Jiang, “Asymptotic correlations of metrics on the symmetric groups,” arXiv:1110.0807, first submitted 4 October 2011.
2. P. Diaconis and R. L. Graham, “Spearman's Footrule as a Measure of Disarray,” *Journal of the Royal Statistical Society, Series B* 39 (1977), 262–268. DOI: 10.1111/j.2517-6161.1977.tb01624.x.
3. K. J. Berry and P. W. Mielke, Jr., “Spearman's Footrule as a Measure of Agreement,” *Psychological Reports* 80 (1997), 839–846. DOI: 10.2466/pr0.1997.80.3.839.
