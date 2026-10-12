# Exact support-size regression of bootstrap sample variance
## Finding
Fix real observations
\[
x_1,\ldots,x_n,
\qquad n\ge2,
\]
that are not all equal. Draw an ordinary nonparametric bootstrap sample
\[
X_1^*,\ldots,X_n^*
\]
of size \(n\) from the empirical distribution assigning mass \(1/n\) to each source observation.

Let
\[
K_n
\]
be the number of distinct source observations represented in the bootstrap sample. Write
\[
S^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2
\]
for the original unbiased sample variance and
\[
S_*^2=\frac1{n-1}\sum_{a=1}^n(X_a^*-\bar X^*)^2
\]
for the bootstrap unbiased sample variance.

For every
\[
1\le k\le n,
\]
let
\[
\left\{\begin{matrix}r\\s\end{matrix}\right\}
\]
denote a Stirling number of the second kind. Then
\[
\boxed{
\mathbb E[S_*^2\mid K_n=k]
=
\left(
1-
\frac{
\left\{\begin{matrix}n-1\\k\end{matrix}\right\}
}{
\left\{\begin{matrix}n\\k\end{matrix}\right\}
}
\right)S^2.
}
\]

Hence the conditional mean depends on the observed data only through the single scale \(S^2\). At the two extreme support sizes the formula gives
\[
\mathbb E[S_*^2\mid K_n=1]=0
\]
and
\[
\mathbb E[S_*^2\mid K_n=n]=S^2.
\]

There is also a closed unconditional covariance:
\[
\boxed{
\operatorname{Cov}(K_n,S_*^2)
=
\frac{(1-1/n)^n}{n-1}S^2.
}
\]
Equivalently,
\[
\boxed{
\operatorname{Cov}\!\left(K_n,\frac{S_*^2}{S^2}\right)
=
\frac{(1-1/n)^n}{n-1}.
}
\]
Thus this scale-free covariance is universal over all nonconstant data profiles and
\[
\operatorname{Cov}\!\left(K_n,\frac{S_*^2}{S^2}\right)
\sim
\frac{e^{-1}}n.
\]

## Assumptions and scope
The source observations are treated as fixed. Randomness comes only from an ordinary bootstrap resample of the same size \(n\), drawn independently with replacement from the \(n\) empirical atoms.

The statistic \(K_n\) counts distinct source labels, even if two source observations happen to have equal numerical values. The theorem therefore concerns the resampling support in the empirical measure, not the number of distinct numerical values in the resampled vector.

Both \(S^2\) and \(S_*^2\) use the usual divisor \(n-1\). The nonconstant assumption only avoids division by zero in the normalized covariance; the unnormalized identities remain valid when all observations are equal.

## Proof
Condition on the event \(K_n=k\). By symmetry, the occupied source set \(A\subseteq\{1,\ldots,n\}\) is uniform over all \(k\)-subsets. Conditional on a fixed occupied set \(A\), the ordered bootstrap labels are uniform over all surjections from the \(n\) draw positions onto \(A\).

Let \(Y_1,Y_2\) be the numerical values at two distinct bootstrap positions. For a uniform surjection onto \(k\) labels,
\[
q_{n,k}
:=
\Pr(Y_1\text{ and }Y_2\text{ use the same source label}\mid A,K_n=k)
=
\frac{
\left\{\begin{matrix}n-1\\k\end{matrix}\right\}
}{
\left\{\begin{matrix}n\\k\end{matrix}\right\}
}.
\]
Indeed, there are
\[
k!\left\{\begin{matrix}n\\k\end{matrix}\right\}
\]
onto labelings of the \(n\) positions, while identifying the first two positions leaves
\[
k!\left\{\begin{matrix}n-1\\k\end{matrix}\right\}
\]
onto labelings.

For the fixed set \(A\), put
\[
\bar x_A=\frac1k\sum_{i\in A}x_i,
\qquad
v_A=\frac1k\sum_{i\in A}(x_i-\bar x_A)^2.
\]
Each single draw is uniform on \(A\). Conditional on the two source labels being different, symmetry over ordered distinct pairs gives
\[
\mathbb E[(Y_1-\bar x_A)(Y_2-\bar x_A)\mid
A,K_n=k,\text{ different}]
=
-\frac{v_A}{k-1}.
\]
Conditional on equality the same product has mean \(v_A\). Therefore
\[
\operatorname{Cov}(Y_1,Y_2\mid A,K_n=k)
=
\frac{kq_{n,k}-1}{k-1}v_A.
\]

For any exchangeable square-integrable sample,
\[
\mathbb E[S_*^2\mid A,K_n=k]
=
\operatorname{Var}(Y_1\mid A,K_n=k)
-
\operatorname{Cov}(Y_1,Y_2\mid A,K_n=k).
\]
Since \(\operatorname{Var}(Y_1\mid A,K_n=k)=v_A\),
\[
\mathbb E[S_*^2\mid A,K_n=k]
=
\frac{k}{k-1}(1-q_{n,k})v_A.
\]
A uniform \(k\)-subset has unbiased sample variance with expectation \(S^2\), so
\[
\mathbb E[v_A\mid K_n=k]
=
\frac{k-1}{k}S^2.
\]
Averaging the preceding display proves
\[
\mathbb E[S_*^2\mid K_n=k]=(1-q_{n,k})S^2.
\]
The case \(k=1\) follows directly and agrees with the same formula.

For the covariance, center the fixed data so that
\[
\sum_{i=1}^n x_i=0
\]
and set
\[
A_2=\sum_{i=1}^n x_i^2=(n-1)S^2.
\]
Let \(N_i\) be the bootstrap multiplicity of source \(i\), and put
\[
Z=\sum_{i=1}^nN_ix_i.
\]
Then
\[
S_*^2
=
\frac1{n-1}
\left(
\sum_iN_ix_i^2-\frac{Z^2}{n}
\right).
\]

By source-label symmetry,
\[
\operatorname{Cov}\!\left(K_n,\sum_iN_ix_i^2\right)=0.
\]
Let
\[
p_0=\Pr(N_i=0)=\left(1-\frac1n\right)^n.
\]
Unconditionally,
\[
\mathbb E Z^2=A_2.
\]
Conditional on one specified source \(i\) being omitted, the \(n\) draws are iid uniform on the remaining \(n-1\) source points; centering the full data gives
\[
\mathbb E[Z^2\mid N_i=0]
=
\frac{n}{n-1}A_2,
\]
independently of \(i\). Since
\[
K_n=\sum_i\mathbf 1\{N_i>0\},
\]
summing over omitted-label indicators yields
\[
\operatorname{Cov}(K_n,Z^2)
=
-\frac{n p_0}{n-1}A_2
=
-np_0S^2.
\]
Consequently
\[
\operatorname{Cov}(K_n,S_*^2)
=
-\frac1{n(n-1)}\operatorname{Cov}(K_n,Z^2)
=
\frac{p_0}{n-1}S^2,
\]
as claimed.

## Verification
The accompanying `checker.py` uses exact rational arithmetic. For each \(2\le n\le6\), it exhaustively enumerates all \(n^n\) ordered bootstrap resamples for several non-affinely-equivalent fixed data profiles. It recomputes \(K_n\), \(S_*^2\), every conditional mean by support size, and the unconditional covariance directly, and compares them with the stated formulas.

The checker also verifies the Stirling recurrences and the displayed conditional coefficient over a larger finite parameter range. These finite calculations are reproducibility checks only; the all-\(n\) statement is proved symbolically above.

## Relationship to prior work
Rao, Pathak, and Koltchinskii motivated sequential bootstrap resampling by observing that ordinary bootstrap replicates contain random numbers of distinct observations and therefore need not have equal information content. Their full technical-report text gives the mean and variance of the distinct-observation count and proposes sampling until a fixed number of distinct source observations is reached. A targeted inspection found no Stirling-number conditional regression for sample variance. The only occurrence of “sample variance” in the inspected technical argument refers to the variance of the initial sample inside an asymptotic bound.

Pauly likewise identifies randomness in the number of distinct observations as the motivation for fixed-support bootstrap variants and studies empirical-process consistency. The published record classifies the work under nonparametric resampling, MSC \(62G09\). The exact finite regression and covariance above concern the ordinary bootstrap itself and quantify one concrete variance statistic as a function of that random support size.

Targeted searches using “support size,” “number of distinct observations,” “sample variance,” “Stirling numbers,” “conditional,” and “covariance” did not locate an equivalent formula.

## Limitations
The theorem concerns the ordinary equal-weight nonparametric bootstrap with resample size equal to source sample size. Unequal empirical weights, \(m\)-out-of-\(n\) bootstrap, Bayesian bootstrap weights, and sequential stopping rules have different occupancy laws.

The result determines a conditional mean and a covariance. It does not give the full conditional distribution of \(S_*^2\) given \(K_n\), nor does positive covariance imply stochastic monotonicity.

Older survey-sampling or occupancy literature may encode the same mixed moment under different notation. This remains the main originality risk.

## References
1. M. Pauly, “Consistency of the Subsample Bootstrap empirical process,” *Statistics* 46 (2012), 621–626. DOI: 10.1080/02331888.2010.543469. Published online 18 April 2011.
2. C. R. Rao, P. K. Pathak, and V. I. Koltchinskii, “Bootstrap by sequential resampling,” *Journal of Statistical Planning and Inference* 64 (1997), 257–281. DOI: 10.1016/S0378-3758(97)00041-4. An earlier technical report is dated February 1996.
