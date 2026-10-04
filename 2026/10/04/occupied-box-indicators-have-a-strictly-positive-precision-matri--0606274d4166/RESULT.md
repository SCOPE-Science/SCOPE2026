# Occupied-box indicators have a strictly positive precision matrix

## Finding

Fix
\[
m\ge2,
\qquad
p_1,\ldots,p_m>0,
\qquad
\sum_{i=1}^m p_i=1,
\]
and make \(n\ge1\) independent draws from these \(m\) categories. Let
\[
I_i=\mathbf 1\{\text{category }i\text{ appears at least once}\}
\]
and let
\[
C=\operatorname{Cov}(I_1,\ldots,I_m).
\]
Put
\[
q_i=(1-p_i)^n.
\]
Then
\[
C_{ii}=q_i(1-q_i)
\tag{1}
\]
and, for \(i\ne j\),
\[
\boxed{
C_{ij}
=
(1-p_i-p_j)^n-(1-p_i)^n(1-p_j)^n
<0.
}
\tag{2}
\]

There is an exact rank transition at sample size two.

For \(n=1\),
\[
\boxed{
\operatorname{rank}(C)=m-1,
\qquad
\ker C=\operatorname{span}\{\mathbf 1\}.
}
\tag{3}
\]

For every \(n\ge2\),
\[
\boxed{C\succ0}
\tag{4}
\]
and, more strongly,
\[
\boxed{
(C^{-1})_{ij}>0
\quad\text{for every }1\le i,j\le m.
}
\tag{5}
\]
Thus the covariance matrix is a positive-definite matrix with strictly negative off-diagonal entries, while its precision matrix is strictly positive entrywise.

In particular, if \(\Omega=C^{-1}\), the full-order linear partial correlation between distinct coordinates is
\[
\rho_{ij\,\cdot\,-\{i,j\}}
=
-\frac{\Omega_{ij}}{\sqrt{\Omega_{ii}\Omega_{jj}}}
<0.
\tag{6}
\]

The same covariance matrix occurs for the empty-box indicators
\[
E_i=1-I_i,
\]
so (3)--(6) apply to them as well.

## Assumptions and scope

The number of categories is finite, every category probability is strictly positive, and the draws are iid with one common category-probability vector.

The claim concerns the covariance and linear precision geometry of the vector of indicators recording whether each category has appeared at least once. It does not assert a sign for nonlinear conditional associations, and it does not extend the inverse-positivity statement to arbitrary non-identically distributed balls without further work.

The partial correlations in (6) are the ordinary linear partial correlations obtained after least-squares residualization on all remaining occupancy indicators.

## Proof

The probability that category \(i\) is empty after \(n\) draws is
\[
q_i=(1-p_i)^n.
\]
Hence \(I_i\) is Bernoulli with success probability \(1-q_i\), proving (1).

For distinct \(i,j\), inclusion--exclusion gives
\[
\Pr(I_i=I_j=1)
=
1-q_i-q_j+(1-p_i-p_j)^n.
\]
Subtracting
\[
\Pr(I_i=1)\Pr(I_j=1)
=(1-q_i)(1-q_j)
\]
gives (2). Its sign is strict because
\[
1-p_i-p_j
<
(1-p_i)(1-p_j)
\]
when \(p_ip_j>0\), and both sides lie in \([0,1]\).

For \(n=1\), exactly one occupancy indicator equals one, so
\[
C=\operatorname{diag}(p)-pp^{\mathsf T}.
\]
For any \(a\in\mathbb R^m\),
\[
a^{\mathsf T}Ca
=
\operatorname{Var}(a_X),
\]
where \(X\) is the single sampled category. This variance vanishes exactly when all \(a_i\) are equal. Therefore the nullspace consists precisely of the constant vectors, proving (3).

Now assume \(n\ge2\). Suppose
\[
a^{\mathsf T}Ca=0.
\]
Then the random variable
\[
\sum_i a_iI_i
\]
is almost surely constant on every occupancy pattern having positive probability.

For each category \(i\), the singleton occupancy pattern \(\{i\}\) occurs with probability \(p_i^n>0\). Therefore all singleton values \(a_i\) must be equal to one common constant \(c\).

For each pair \(i\ne j\), a pattern using exactly categories \(i,j\) has positive probability when \(n\ge2\); for example, the sequence consisting of one draw of \(i\) and \(n-1\) draws of \(j\) has positive probability. On such a pattern the same linear statistic equals
\[
a_i+a_j=2c.
\]
Since it must equal the singleton value \(c\), one has \(c=0\). Thus \(a=0\), proving (4).

It remains to prove the strict positivity of the inverse. Let
\[
D=\operatorname{diag}(C_{11},\ldots,C_{mm})
\]
and normalize
\[
A=D^{-1/2}CD^{-1/2}.
\]
By (4), \(A\) is positive definite. By (2), it has unit diagonal and strictly negative off-diagonal entries, so
\[
A=I-B,
\]
where \(B\) is symmetric, has zero diagonal, and satisfies
\[
B_{ij}>0
\quad(i\ne j).
\]

Because \(A\succ0\), every eigenvalue of \(B\) is strictly smaller than one. Since \(B\) is entrywise nonnegative and symmetric, its spectral radius equals its largest eigenvalue. Hence
\[
\rho(B)<1.
\]
The Neumann series converges:
\[
A^{-1}
=
(I-B)^{-1}
=
\sum_{k=0}^{\infty}B^k.
\tag{7}
\]
Every term is entrywise nonnegative. The identity term makes all diagonal entries positive, while the \(B\) term itself makes every off-diagonal entry positive. Therefore
\[
A^{-1}>0
\]
entrywise, and so
\[
C^{-1}=D^{-1/2}A^{-1}D^{-1/2}>0
\]
entrywise as claimed in (5).

Formula (6) is the standard precision-matrix expression for full-order linear partial correlation. Finally,
\[
\operatorname{Cov}(1-I_i,1-I_j)=\operatorname{Cov}(I_i,I_j),
\]
so the empty-indicator statement follows immediately.

## Verification

The accompanying exact-rational checker independently constructs (1)--(2) for thousands of rational probability profiles. It verifies strict negative off-diagonal entries, the rank-one deficiency at \(n=1\), positive leading principal minors for \(n\ge2\), and strict positivity of every entry of the exact rational inverse.

For small instances it also enumerates every iid draw sequence exactly and reconstructs the occupancy-indicator covariance directly from the sample space, checking the closed formula without relying on it.

The finite replay is supplementary. The universal positive-definiteness proof is the occupancy-pattern argument above, and the universal inverse-positivity proof is the normalized Neumann-series argument (7).

## Relationship to prior work

Joag-Dev and Proschan introduced negative association and explicitly list the multinomial distribution among negatively associated families. This gives a broad dependence framework for multinomial counts but does not, in its accessible abstract, state the covariance-rank transition or a precision-matrix theorem for occupied-category indicators.

Dubhashi and Ranjan's full balls-and-bins treatment proves strong negative dependence for occupancy variables. In particular, their Theorem 46 states that empty-bin indicators are negatively associated and satisfy negative regression. Negative association implies the expected pairwise covariance sign, but it does not by itself imply that the covariance matrix is nonsingular or that its inverse is entrywise positive.

Bogachev, Gnedin, and Yakubovich write the number of occupied boxes as a sum of occupancy indicators and display the fixed-sample variance with the cross-term
\[
(1-p_i-p_j)^n-(1-p_i)^n(1-p_j)^n.
\]
Thus the pairwise covariance formula underlying (2) is present in aggregate form in the occupancy literature. Their objective is the asymptotic behavior of the variance of the number of occupied boxes, not the full covariance matrix, its exact rank transition, or its inverse sign pattern.

Targeted searches for occupancy-indicator precision matrices, inverse covariance, Stieltjes-matrix formulations, and multinomial empty-cell indicator inverses did not locate the combination (3)--(6).

## Limitations

The finite-category assumption is essential to the ordinary matrix inverse statement. Infinite-box models require an operator formulation and domain control.

The iid assumption is used for the closed covariance formula. Some positive-definiteness arguments survive for more general allocations, but inverse positivity is not claimed there.

The inverse sign statement is a linear second-order property. It should not be read as a theorem about all conditional probabilities or nonlinear conditional dependence.

The originality search was targeted. Because the inverse-positivity argument is short once the covariance matrix is recognized as a positive-definite matrix with negative off-diagonal entries, older matrix-analysis or occupancy literature may contain an equivalent observation under different terminology.

The full Joag-Dev--Proschan article was not available through the checked machine-readable route, so its abstract and bibliographic record were used only for broad negative-association scope and classification, not as a whole-document noncoverage certificate.

## References

1. K. Joag-Dev and F. Proschan, “Negative Association of Random Variables with Applications,” *The Annals of Statistics* 11 (1983), 286–295, DOI 10.1214/aos/1176346079.
2. D. P. Dubhashi and D. Ranjan, “Balls and Bins: A Study in Negative Dependence,” *BRICS Report Series* 3(25) (1996), DOI 10.7146/brics.v3i25.20006; later *Random Structures & Algorithms* 13 (1998), 99–124.
3. L. V. Bogachev, A. V. Gnedin, and Yu. V. Yakubovich, “On the variance of the number of occupied boxes,” arXiv:math/0609498, first submitted 2006-09-18; later *Advances in Applied Mathematics* 40 (2008), 401–432.
