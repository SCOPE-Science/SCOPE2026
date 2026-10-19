# Sharp linear recovery of Spearman footrule from pairwise ranking disagreements

## Finding

Let \(n\ge2\), and let \(\pi\) be uniformly distributed on the permutations of \(\{1,\ldots,n\}\). Define the Spearman footrule distance from the identity and all pairwise inversion indicators by
\[
F_n=\sum_{i=1}^n |i-\pi(i)|,
\qquad I_{ab}={\bf1}\{\pi(a)>\pi(b)\},\quad 1\le a<b\le n.
\]
Set
\[
c_{ab}=\frac{1}{n(n-1)}\sum_{t=a}^{b-1}t(n-t).
\]
Then the exact individual comparison covariance is
\[
\boxed{\operatorname{Cov}(F_n,I_{ab})=c_{ab}>0.}
\tag{1}
\]
Among **all** affine linear predictors of \(F_n\) from the complete vector of \(\binom n2\) pairwise comparisons, the unique minimum-mean-square-error predictor is
\[
\boxed{\widehat F_n=\frac{n^2-1}{3}+\frac{12}{n+1}\sum_{a<b}c_{ab}\left(I_{ab}-\frac12\right).}
\tag{2}
\]
Its exact squared multiple correlation (the optimal fraction of footrule variance explained) is
\[
\boxed{R_n^2=\frac{3(17n^4+31n^2+24)}{28(n^2-1)(2n^2+7)}.}
\tag{3}
\]
Consequently, for every \(n\ge2\),
\[
\boxed{R_n^2\ge\frac{58}{65},}
\]
with equality **only for \(n=4\)**; \(R_2^2=1\), \(R_3^2=9/10\), and \(R_n^2\) increases strictly for integer \(n\ge4\). Furthermore,
\[
\boxed{\lim_{n\to\infty}R_n^2=\frac{51}{56},}
\qquad
\boxed{\operatorname{Var}(F_n-\widehat F_n)=\frac{(n-2)(n+2)(5n^2+67)}{1260(n-1)}.}
\tag{4}
\]
The residual variance vanishes exactly at \(n=2\). For every \(n\ge3\), a strictly positive nonlinear component remains even though the complete set of comparisons determines the permutation.

## Assumptions and scope

All \(n!\) permutations are equally likely. The predictor class consists of real affine linear combinations of the indicators \(I_{ab}\), not arbitrary functions of the entire inversion pattern. The minimum square error and variance-explained percentage are with respect to this uniform randomization law. The total comparison vector determines the ranking, so (4) is **not** a lower bound on unrestricted nonlinear prediction error. The same law applies to ranks of \(n\) independent draws from any continuous distribution.

## Proof

**1. Pairwise covariance.** Fix \(a<b\) and write \(X=\pi(a)\), \(Y=\pi(b)\). Conditional on an unordered pair of values \(\{x,y\}\), \(x<y\), the two assignments \((X,Y)=(x,y)\) and \((y,x)\) are equiprobable. All other footrule summands have identical conditional expectation under the two assignments. Their footrule difference (inversion minus noninversion) is
\[
|a-y|+|b-x|-|a-x|-|b-y|
=2\sum_{t=a}^{b-1}{\bf1}\{x\le t<y\}.
\]
Because \(\Pr(I_{ab}=1)=1/2\), the covariance is one quarter of the difference of these conditional means. Of the \(\binom n2\) possible unordered value pairs, exactly \(t(n-t)\) straddle the cut at \(t\). Hence
\[
\operatorname{Cov}(F_n,I_{ab})
=\frac12\sum_{t=a}^{b-1}\frac{t(n-t)}{\binom n2}
=c_{ab},
\]
proving (1). This identity includes every boundary position and \(n=2\).

**2. Comparison covariance and optimality.** Let \(m=\binom n2\), and let \(B\) be the \(n\times m\) oriented incidence matrix of the complete graph, with column \(e_a-e_b\) for \((a,b)\). For disjoint comparisons the centered indicators are independent; for incident comparisons the three-point ordering probabilities give covariance \(+1/12\) or \(-1/12\) according to the orientation. Each indicator has variance \(1/4\). Therefore their full covariance matrix is
\[
\Sigma=\frac1{12}(I_m+B^\top B).
\]
It is positive definite. Let \(h_a=\sum_{t=a}^{n-1}t(n-t)/[n(n-1)]\), so the vector \(c=(c_{ab})\) satisfies \(c=B^\top h\). The incidence identity
\[
BB^\top=nI_n-\mathbf1\mathbf1^\top
\]
implies \(B^\top Bc=nc\). Thus \(\Sigma c=(n+1)c/12\), so the normal equations \(\Sigma\beta=c\) have the **unique** solution \(\beta=12c/(n+1)\). Finally \(\mathbb E F_n=(n^2-1)/3\) and \(\mathbb E I_{ab}=1/2\), giving (2). The projection explains exactly \(12\sum_{a<b}c_{ab}^2/(n+1)\) units of variance.

**3. Exact total variance and sums.** Put \(d_{ij}=|i-j|\), \(r_i=n^{-1}\sum_jd_{ij}\), and \(g=n^{-2}\sum_{i,j}d_{ij}\). The standard random-assignment variance identity, obtained by evaluating pairs of distinct permutation columns, reads
\[
\operatorname{Var}\!\left(\sum_i d_{i,\pi(i)}\right)
=\frac1{n-1}\sum_{i,j}(d_{ij}-r_i-r_j+g)^2.
\]
Here
\[
r_i=\frac{i(i-1)+(n-i)(n-i+1)}{2n},\quad
 g=\frac{n^2-1}{3n}.
\]
Expanding the squares and using the finite sums of powers gives
\[
\boxed{\operatorname{Var}(F_n)=\frac{(n+1)(2n^2+7)}{45}.}\tag{5}
\]
For checking the other finite summation, the cut covariance has the explicit polynomial form
\[
c_{ab}=\frac{(b-a)\big[3(n+1)(a+b)-2(a^2+ab+b^2)-3n-1\big]}{6n(n-1)}.
\]
Expanding its square and applying \(\sum_{k=1}^N k^j\) for \(0\le j\le6\) yields the exact finite identity
\[
\boxed{\sum_{a<b}c_{ab}^2=\frac{(n+1)(17n^4+31n^2+24)}{5040(n-1)}.}\tag{6}
\]
Equations (5)–(6) give (3), and subtracting the projection variance gives the residual in (4).

**4. Uniform sharp bound and limit.** A direct difference of the rational functions in (3) has the sign of
\[
P(n)=23n^4+46n^3-311n^2-334n-504,
\]
since every other factor is positive for integer \(n\ge2\). The differences at \(n=2,3\) are negative. For \(n\ge4\), setting \(z=n-4\ge0\) gives
\[
P(n)=23z^4+414z^3+2449z^2+5274z+2016>0.
\]
Thus (3) decreases through \(n=4\) and then increases strictly, proving the unique global minimum \(R_4^2=58/65\). Dividing the leading terms of (3) gives \(51/56\).

## Verification

Run `python verify_footrule_projection.py` using Python 3 and the standard library only. The verifier exhaustively enumerates permutations for \(2\le n\le7\), recomputes every cross-covariance and comparison covariance entry from integer counts, checks the exact affine normal equations and projection identities, and directly checks the closed finite-sum identities for \(2\le n\le100\). It reports 1,004 enumeration assertions and 396 additional rational checks, all passed. The polynomial identities in the proof are exact symbolic finite sums; checking a finite set of sizes alone would not establish them for all \(n\).

## Relationship to prior work

Spearman footrule and Kendall inversion distance are classical ranking metrics. Diaconis–Graham established foundational relationships and asymptotic properties of the footrule. Chen–Li–Feng (arXiv:1207.2541, first public version 2012-07-11) study weighted footrule approximations to weighted Kendall distances rather than uniform-null least-squares recovery from *all individual comparison indicators*. Xia–Guan–Xu (2025, DOI:10.3934/era.2025220) obtain asymptotic representations of the footrule and state its exact marginal variance; their independent-input Hájek projection is not the finite-dimensional projection onto the vector of comparison indicators considered here.

The published study *Incidence precision law for all inversion indicators of a random permutation* provides the comparison covariance and precision formula used in proof step 2. It does not evaluate the footrule–indicator covariance vector, optimal footrule coefficients, the sharp uniform \(58/65\) bound or the limiting \(51/56\) fraction. Accordingly, the claim of contribution concerns **the exact cross-covariance, optimizer and explained-variance theorem**, not the already established marginal footrule moments or indicator precision. The literature comparison does not establish historical priority beyond the inspected materials.

## Limitations

The result is for the uniform permutation law and linear prediction; it makes no optimality assertion among nonlinear predictors or under a nonuniform ranking model. The original Diaconis–Graham paper and the complete Chen–Li–Feng preprint were not accessible in full in this search, so implicit historical coverage cannot be ruled out. The 2025 article and the published comparison-indicator precision result were inspected in their relevant substantive sections. The exact finite checker is corroborative, not a substitute for the all-size algebra and covariance proof.

## References

1. P. Diaconis and R. L. Graham, “Spearman's Footrule as a Measure of Disarray,” *Journal of the Royal Statistical Society, Series B*, 39 (1977), 262–268; DOI:10.1111/j.2517-6161.1977.tb01624.x.
2. J. Chen, Y. Li, and L. Feng, “A New Weighted Spearman's Footrule as A Measure of Distance between Rankings,” arXiv:1207.2541 (first public version 2012-07-11).
3. L. Xia, L. Guan, and W. Xu, “Asymptotic representations for Spearman's footrule correlation coefficient,” *Electronic Research Archive* 33 (2025), 4893–4916, DOI:10.3934/era.2025220.
4. “Incidence precision law for all inversion indicators of a random permutation,” publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805 .
