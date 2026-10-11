# Exact Dudley norms and mass-imbalance thresholds on equiradial stars

## Finding

For any nonempty finite or countable set \(I\), radius \(\rho>0\), and real absolutely summable coefficients \((a_i)_{i\in I}\), consider the star metric space
\[
S_{I,\rho}=\{o\}\cup\{v_i:i\in I\},\qquad
d(o,v_i)=\rho,\quad d(v_i,v_j)=2\rho\quad(i\ne j),
\]
and the zero-total-mass signed measure
\[
\mu=\sum_{i\in I}a_i(\delta_{v_i}-\delta_o).
\]
Write \(P=\sum_i(a_i)_+\) and \(Q=\sum_i(-a_i)_+\). With the *sum-normalized* real bounded-Lipschitz norm \(\|f\|_{\mathrm{BL}}=\|f\|_\infty+\mathrm{Lip}(f)\), its dual norm has the exact formula
\[
\boxed{\|\mu\|_{\mathrm{BL}}^*
 =\max\left\{\frac{\rho}{\rho+1}(P+Q),\frac{2\rho}{\rho+2}\max(P,Q)\right\}.}
\]
Equivalently, identifying \(\mu\) with its leaf coefficients,
\[
\|\mu\|_{\mathrm{BL}}^*
=\max\left\{\frac{\rho}{\rho+1}\sum_i|a_i|,
\frac{\rho}{\rho+2}\left(\sum_i|a_i|+\left|\sum_i a_i\right|\right)\right\}.
\]
The first branch is optimal precisely when \(P\le(1+2/\rho)Q\) and \(Q\le(1+2/\rho)P\); otherwise the one-sided branch corresponding to the larger signed mass is optimal. On either boundary the two indicated branches tie. All maxima are attained by explicit bounded-Lipschitz potentials, including for countably infinite stars.

## Assumptions and scope

The metric is the shortest-path metric of a star whose arms all have the same length \(\rho\); points on the edges other than the center and leaves are **not** included. The coefficient index set is nonempty, finite or countably infinite, and \(\sum_i|a_i|<\infty\). All measures and test functions are **real**. The normalization is a *sum* of supremum and Lipschitz norms, not the alternative maximum-normalized Fortet–Mourier norm. The zero-total-mass condition holds because the central atom has coefficient \(-\sum_i a_i\). The zero coefficient family gives zero on both sides.

## Proof

Let \(f:S_{I,\rho}\to\mathbb R\) be bounded Lipschitz and put \(y_i=f(v_i)-f(o)\). For \(R=\sup_i|y_i|\), the exact Lipschitz constant is \(R/\rho\): center–leaf pairs attain the supremum in the limiting sense, and leaf–leaf quotients are no larger, since \(|y_i-y_j|\le2R\). Since \(\mu(S_{I,\rho})=0\), adding a constant to \(f\) does not change \(\int f\,d\mu=\sum_i a_i y_i\).

Suppose \(R>0\), normalize \(R=1\) by homogeneity, and write
\[
U=\max\{0,-\inf_i y_i\},\qquad V=\max\{0,\sup_i y_i\}.
\]
Then \(0\le U,V\le1\) and \(\max(U,V)=1\). The range of the values of \(f\), including its central value, has diameter \(U+V\). Among all constant translates, the least possible supremum norm is \((U+V)/2\), obtained by centering the range. Also, coefficientwise,
\[
\sum_i a_i y_i\le PV+QU.
\]
Consequently every nonconstant potential satisfies
\[
\frac{\int f\,d\mu}{\|f\|_\infty+\mathrm{Lip}(f)}
\le \frac{PV+QU}{\rho^{-1}+(U+V)/2}.
\]
Constant potentials give zero because \(\mu\) has total mass zero. It therefore suffices to maximize the right-hand side over the two edges of the unit square on which \(\max(U,V)=1\).

On \(U=1\), the quotient is \((PV+Q)/(\rho^{-1}+(1+V)/2)\), whose derivative with respect to \(V\) has the constant sign of \((1+2/\rho)P-Q\). On \(V=1\), the derivative with respect to \(U\) has the constant sign of \((1+2/\rho)Q-P\). Thus the maximum occurs at one of the three corners \((U,V)=(1,1),(1,0),(0,1)\), giving exactly
\[
\frac{\rho}{1+\rho}(P+Q),\qquad
\frac{2\rho}{2+\rho}Q,\qquad
\frac{2\rho}{2+\rho}P.
\]
This proves the upper bound, with no finiteness assumption beyond absolute summability.

For the first value, define the potential by \(f(o)=0\) and \(f(v_i)=\rho\operatorname{sgn}(a_i)/(1+\rho)\), using \(\operatorname{sgn}(0)=0\). Unless all coefficients vanish, it has \(\|f\|_\infty=\rho/(1+\rho)\), \(\mathrm{Lip}(f)=1/(1+\rho)\), and integral \(\rho(P+Q)/(1+\rho)\). For the positive one-sided value (when \(P>0\)), set \(f(o)=-\rho/(2+\rho)\), let \(f(v_i)=\rho/(2+\rho)\) if \(a_i>0\), and otherwise set \(f(v_i)=f(o)\). Its supremum and Lipschitz seminorm sum to one, and its integral is \(2\rho P/(2+\rho)\). Reversing signs gives the negative one-sided value when \(Q>0\). These witnesses establish the reverse inequality and attainment. They are bounded even when \(I\) is infinite.

Comparing the first candidate with each one-sided candidate gives the stated sharp inequalities: the positive one-sided value strictly dominates if \(P>(1+2/\rho)Q\), while the negative one strictly dominates if \(Q>(1+2/\rho)P\). Equality gives a tie, and both strict inequalities cannot hold simultaneously. The equivalent coefficient formula follows from \(P+Q=\sum_i|a_i|\) and \(2\max(P,Q)=P+Q+|P-Q|\).

## Verification

The proof is analytic and requires no finite enumeration. As an independent numerical check of its finite-dimensional specialization, a direct linear program was run with variables for every potential value, its supremum-norm bound, and its Lipschitz bound. For \(|I|\in\{1,2,3,5,8\}\), \(\rho\in\{0.1,0.3,1,2,7,20\}\), and 50 deterministically sampled coefficient vectors at each pair, all 1,500 linear-program optima agreed with the formula within \(10^{-7}\). The complete optional reproduction script is `checks/test_star_lp.py`, with its dependencies in `checks/requirements.txt`. These tests cannot certify the infinite case, which is proved above.

Useful exact boundary checks: at \(\rho=1\), coefficients \((1,-1)\) give norm \(1\); coefficients \((4,-1)\) give norm \(8/3\); and at \(\rho=2\), coefficients \((2,-1)\) lie exactly on the phase boundary and give norm \(2\).

## Relationship to prior work

Hille and Theewis (2022), Section 6 and Lemma 6.1, describe a general linear-programming method for evaluating the Dudley norm of *finite* molecular measures on arbitrary metric spaces. Their result supplies an algorithmic representation, not the displayed closed form, its sharp mass-imbalance boundary, or the countably infinite case. Hille and Theewis (2023), especially Sections 2, 5 and 6, establish extremal/norming function descriptions on general metric spaces and examine finite spaces; their statements likewise do not evaluate this equiradial-star family. The classical two-point instance is prior background, not an originality claim. Sriperumbudur and coauthors (2012) provide a general empirical-measure computation method, discussed in the 2022 paper; it does not supply a known exact symbolic star formula in the inspected evidence. The claimed distinction is therefore an explicit all-size, all-radius norm identity and its sharp optimizer transition, **not** the existence of a general numerical algorithm.

## Limitations

The result concerns real test functions, equal-length star arms, and zero-total-mass measures. It gives neither a formula for unequal arm lengths nor one for arbitrary nonzero-total-mass measures. The explicit solution of a general finite linear program is not claimed to be new, and a symbolically equivalent special formula in unindexed literature cannot be excluded. The finite numerical checks do not establish completeness or uniqueness of any general algorithm and are not a substitute for the proof.

## References

1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1, first publicly submitted 15 May 2023, https://arxiv.org/abs/2305.08500.
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet-Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234v2, Section 6, https://arxiv.org/abs/2206.12234.
3. B. K. Sriperumbudur, K. Fukumizu, A. Gretton, B. Schölkopf, and G. R. G. Lanckriet, *On the empirical estimation of integral probability metrics*, Electronic Journal of Statistics 6 (2012), 1550–1599, DOI:10.1214/12-EJS722 (method cited as related prior art; full text not independently inspected).
