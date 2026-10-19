# Rank-two cross-covariance and shared modes of permutation and inverse comparisons

## Finding
Let \(\pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\), with \(n\ge3\). For \(1\le i<j\le n\) and \(1\le a<b\le n\), set
\[
X_{ij}=\mathbf1\{\pi(i)>\pi(j)\},\qquad
Y_{ab}=\mathbf1\{\pi^{-1}(a)>\pi^{-1}(b)\}.
\]
Then the entire position-by-value comparison covariance matrix has the explicit kernel
\[
\boxed{\operatorname{Cov}(X_{ij},Y_{ab})
=\frac{1}{2n(n-1)}+
\frac{(j-i-1)(b-a-1)}{n(n-1)(n-2)}.}
\]
In particular, every entry is strictly positive. If \(u_{ij}=1\) and \(v_{ij}=j-i-1\), then the square matrix indexed by pairs \(i<j\) is
\[
\Gamma=\frac{uu^\mathsf T}{2n(n-1)}+
\frac{vv^\mathsf T}{n(n-1)(n-2)}.
\]
Thus \(\Gamma\) is positive semidefinite and has rank exactly two.

Define \(\mathcal U\) and \(\mathcal V\) as the finite-dimensional subspaces of real \(L^2(S_n)\) spanned, respectively, by all centered \(X_{ij}\) and all centered \(Y_{ab}\). Define the inversion count and squared rank displacement
\[
I=\sum_{i<j}X_{ij},\qquad
D=\frac12\sum_{r=1}^n(\pi(r)-r)^2.
\]
Then, writing \(I^\circ=I-\mathbb EI\) and \(D^\circ=D-\mathbb ED\), the *entire common linear information* is
\[
\boxed{\mathcal U\cap\mathcal V
=\operatorname{span}\{I^\circ,D^\circ\},\qquad
(\mathcal U\ominus(\mathcal U\cap\mathcal V))
\perp(\mathcal V\ominus(\mathcal U\cap\mathcal V)).}
\]
Consequently the canonical correlations between the two complete centered comparison vectors are \(1,1,0,\ldots,0\), with precisely two ones. For \(n=2\), the unique covariance is \(1/4\) and the cross-matrix has rank one.

## Assumptions and scope
All permutations have equal probability \(1/n!\). Positions and values are each labeled \(1\) through \(n\) and are distinct; only ordered index pairs \(i<j\) and \(a<b\) are considered. The unconditioned comparison indicators are Bernoulli with mean \(1/2\). The matrix statement uses the same ordered list of unordered pairs for rows and columns. The geometric claim is about *linear second-order information*, not independence of the comparison-vector residuals as random variables.

## Proof
**1. Four one-position placements.** Write \(S_{ij}=2X_{ij}-1\) and \(T_{ab}=2Y_{ab}-1\); these are signed comparisons, so
\[
\operatorname{Cov}(X_{ij},Y_{ab})=\frac14\mathbb E[S_{ij}T_{ab}].
\]
If neither of the values \(a,b\) occurs at position \(i\) or \(j\), then conditional on their positions the two remaining values at \(i,j\) are exchangeable, so the conditional expectation of \(S_{ij}\) is zero.

If those two values occupy positions \(i,j\) in either order, the two signs are equal. This case contributes exactly \(2/[n(n-1)]\) to \(\mathbb E[S_{ij}T_{ab}]\).

For the four cases in which precisely one of the two chosen values lies in \(\{i,j\}\), write
\[
 h_a=\frac{2a-n}{n-2},\quad h_b=\frac{2b-n-2}{n-2},\qquad
 t_i=\frac{2i-n}{n-2},\quad t_j=\frac{2j-n-2}{n-2}.
\]
Conditional on \(\pi(i)=a\), with \(b\) outside \(\{i,j\}\), the expected signed value comparison is \(h_a\), while the expected signed inverse-position comparison is \(t_i\). The two signs depend on independent remaining assignments after conditioning on that placement; their product has conditional expectation \(h_at_i\). The other placements \((b,i)\), \((a,j)\), and \((b,j)\) yield respectively \(-h_bt_i\), \(-h_at_j\), and \(h_bt_j\). Each placement has probability \((n-2)/[n(n-1)]\). Their combined contribution is therefore
\[
\frac{n-2}{n(n-1)}(h_a-h_b)(t_i-t_j)
=\frac{4(b-a-1)(j-i-1)}{n(n-1)(n-2)}.
\]
Adding the two-value contribution and dividing by four establishes the claimed kernel, including all adjacent and endpoint cases.

**2. Rank.** The kernel gives the stated sum of two positive rank-one matrices. Both coefficients are positive, and for every \(n\ge3\) the vector \(v\) is not a multiple of \(u\): it is zero for \((1,2)\) and one for \((1,3)\). Hence \(\operatorname{rank}\Gamma=2\). The case \(n=2\) follows directly from its two equally likely permutations.

**3. Two common statistics.** Inversion count is invariant under inversion, as each inverted position pair corresponds bijectively to an inverted value pair. For each deterministic permutation, with \(A_r\) the number of earlier values larger than \(\pi(r)\) and \(B_r\) the number of later values smaller than \(\pi(r)\), one has \(A_r-B_r=r-\pi(r)\). Thus
\[
\sum_{i<j}(j-i)X_{ij}
=\sum_{r=1}^n r(A_r-B_r)
=\sum_{r=1}^n r(r-\pi(r))
=\frac12\sum_{r=1}^n(r-\pi(r))^2=D.
\]
The last equality uses \(\sum_r\pi(r)^2=\sum_rr^2\). The same weighted-inversion identity applied to \(\pi^{-1}\) shows that \(D\) also belongs to the span of inverse-comparison indicators, since it is invariant under inversion. Both \(I^\circ\) and \(D^\circ\) are therefore in \(\mathcal U\cap\mathcal V\).

**4. Exactly two shared dimensions.** The centered comparison indicators within either family are linearly independent. Indeed, their covariance matrix is \(\Sigma=(\mathrm I+B^\mathsf TB)/12\), where \(B\) is the signed incidence matrix of the complete graph with edges oriented from their first to second index. This follows by enumerating the six relative orders of three distinct values; disjoint comparisons are independent, while incident comparisons have covariance \(\pm1/12\) according to incidence signs. Since \(\Sigma\succeq\mathrm I/12\), both within-family Gram matrices are nonsingular.

Consequently, the rank of the orthogonal-projection map from \(\mathcal U\) to \(\mathcal V\) equals the cross-Gram rank \(\operatorname{rank}\Gamma=2\). The two shared centered statistics are linearly independent: their coefficient vectors \(u\) and \(u+v\) are independent, and \(\Sigma\) is positive definite. Since the projection already fixes these two independent vectors, its image is exactly their common span. Every vector of \(\mathcal U\) orthogonal to this span is therefore orthogonal to all of \(\mathcal V\). Symmetry gives the corresponding statement for \(\mathcal V\), proving the exact intersection and residual orthogonality. As a result, precisely two canonical correlations are one and all others are zero.

## Verification
Run `python3 verify.py` using only the Python standard library. The program exhaustively enumerates all \(n!\) permutations for each integer \(2\le n\le7\), checks the weighted inversion/displacement identity for every permutation, tests each of the \(\binom{n}{2}^{2}\) cross-covariance entries using exact rational arithmetic, and checks the exact rank at the smallest sizes. It also checks positive rank-two kernel structure for every integer \(3\le n\le64\). On the tested ranges it reports 812 exact covariance-entry comparisons and 372 exact structural checks. These finite computations are corroboration and are not asserted to prove the all-size theorem.

## Relationship to prior work
Petersen's *Two-sided Eulerian numbers via balls in boxes* (arXiv:1209.6273; first posted 2012-09-27), and Visontai's *Some remarks on the joint distribution of descents and inverse descents* (arXiv:1210.3799; first posted 2012-10-14), study aggregates of adjacent position comparisons and adjacent inverse-value comparisons. Their bivariate generating functions do not retain all arbitrary pair indices, so those stated identities alone do not determine this rank-two full comparison kernel. The classical identity that inversion count agrees with its inverse is acknowledged rather than claimed as new.

The published result *Incidence precision law for all inversion indicators of a random permutation* supplies a within-permutation incidence covariance/precision description. Its original mathematical statement and proof were read; they do not provide the *cross* covariance with the inverse-comparison vector. The incidence covariance identity in Step 4 is therefore background, not an asserted new contribution.

Durbin and Stuart's 1951 *Inversions and Rank Correlation Coefficients* develops classical relationships involving Spearman and Kendall statistics. The weighted-inversion/displacement identity is not offered here as independently original. Its full text could not be inspected, so any broader implicit coverage by that work is a priority risk; see the limitations.

## Limitations
The theorem concerns uniform permutations and second-order linear dependence, not all joint moments or probabilistic independence of the residual comparison coordinates. No analogous rank statement is claimed for nonuniform Mallows measures. Although directly relevant prior work on two-sided Eulerian polynomials was materially read and a search of related public mathematical findings was performed, an earlier implicit formula may exist, particularly in historical rank-correlation literature. The 1951 article was accessible only in bibliographic summary; this leaves a named residual originality risk. Neither priority nor scientific correctness has been independently audited.

## References
1. T. Kyle Petersen, *Two-sided Eulerian numbers via balls in boxes*, 2012 preprint, https://arxiv.org/abs/1209.6273 .
2. M. Visontai, *Some remarks on the joint distribution of descents and inverse descents*, Electronic Journal of Combinatorics 20(1), P52 (2013), https://arxiv.org/abs/1210.3799 ; open article https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p52/pdf/ .
3. J. Durbin and A. Stuart, *Inversions and Rank Correlation Coefficients*, Journal of the Royal Statistical Society B 13(2), 303–309 (1951), https://doi.org/10.1111/j.2517-6161.1951.tb00095.x .
4. *Incidence precision law for all inversion indicators of a random permutation*, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805 .
