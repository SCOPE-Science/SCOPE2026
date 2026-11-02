# Exact finite-sample dependence of squared Wilcoxon and Cramér–von Mises statistics

## Finding

Let two independent samples of sizes \(a,b\ge1\), with \(N=a+b\ge3\), have the same continuous null distribution. Pool and rank the observations, and let \(X_i\in\{0,1\}\) record membership in the first sample at pooled rank \(i\). Define the centered Wilcoxon rank sum
\[
W=\sum_{i=1}^{N}iX_i-\frac{a(N+1)}2
\]
and the following explicitly normalized two-sample Cramér–von Mises statistic:
\[
T=\frac1{abN^2}\sum_{t=1}^{N-1}(NA_t-at)^2,\qquad A_t=\sum_{i=1}^tX_i.
\]
Then the exact permutation-null covariance is
\[
\boxed{\operatorname{Cov}(W^2,T)=\frac{N+1}{180N}\bigl[ab(3N+4)-N(2N+1)\bigr]>0.}
\]
Its constituent variances are
\[
\operatorname{Var}(W^2)=\frac{ab(N+1)}{360}\bigl[ab(5N+8)-3N(N+1)\bigr],
\]
\[
\operatorname{Var}(T)=\frac{N+1}{180abN^2}\bigl[ab(4N+4)-3N^2\bigr].
\]
Consequently,
\[
\operatorname{Corr}(W^2,T)=\frac{\sqrt2\,[ab(3N+4)-N(2N+1)]}{\sqrt{[ab(5N+8)-3N(N+1)][ab(4N+4)-3N^2]}}.
\]
This correlation equals one exactly when one sample has size one; it is strictly between zero and one otherwise. If \(a/N\to\lambda\in(0,1)\), then
\[
\operatorname{Corr}(W^2,T)\longrightarrow\frac3{\sqrt{10}}.
\]
Thus the asymptotic dependence is universal across all nondegenerate sample-size ratios. The signed statistic \(W\), by contrast, has zero covariance with \(T\) by pooled-rank reversal symmetry; squaring reveals strong positive dependence of their two-sided testing magnitudes.

## Assumptions and scope

The null law is continuous, so pooled ranks are distinct almost surely; conditional on the pooled order, the binary membership vector is uniform over all \(\binom Na\) words with exactly \(a\) ones. No moment or density assumptions beyond continuity are needed. All claims are exact at each integer \(a,b\ge1\), \(N\ge3\); the limiting correlation requires both sample fractions bounded away from zero and one, with a convergent interior fraction. The normalization of \(T\) is part of the statement; rescaling an alternative convention rescales covariance and variance but leaves correlation unchanged.

## Proof

Write \(p=a/N\), \(Y_i=X_i-p\), \(\ell_i=i-(N+1)/2\), \(P=I-\mathbf1\mathbf1^\top/N\), and \(M_{ij}=N-\max(i,j)\). Let \(A=\ell\ell^\top\) and \(B=PMP\). Both are symmetric, have zero row sums, and satisfy
\[
W^2=Y^\top A Y,\qquad abT=Y^\top B Y.
\]
We first give a general quadratic-form covariance identity on fixed-composition binary words. For any symmetric zero-row-sum matrix \(D\), put \(d_i=D_{ii}-\operatorname{tr}(D)/N\); then \(\sum_i d_i=0\). Define \(R(d)\) to have diagonal entries \(d_i\) and off-diagonal entries \(-(d_i+d_j)/(N-2)\). There is an orthogonal decomposition
\[
D=\frac{\operatorname{tr}(D)}{N-1}P+R(d)+D_0,
\]
where \(D_0\) has zero diagonal and zero row sums. The first quadratic form is constant because \(Y^\top P Y=ab/N\). Using \(Y_i^2=p(1-p)+(1-2p)Y_i\) and \(\sum_iY_i=0\), the second is
\[
Y^\top R(d)Y=\frac{N(1-2p)}{N-2}\sum_i d_iY_i.
\]
The third is \(\sum_{i\ne j}(D_0)_{ij}X_iX_j\), orthogonal to every centered linear form under uniform fixed-composition sampling. For two matrices \(D,E\), classifying two ordered edges as equal, one-endpoint-overlapping, or disjoint and using \(\mathbb E\prod_{j\in J}X_j=(a)_{|J|}/(N)_{|J|}\) gives, for \(N\ge4\),
\[
\begin{split}
\operatorname{Cov}(Y^\top D Y,Y^\top E Y)
={}&\frac{abN(1-2p)^2}{(N-1)(N-2)^2}\sum_i d_i e_i\\
&+\frac{2(a)_2(b)_2}{(N)_4}\operatorname{tr}(D_0E_0).
\end{split}
\]
Here \((z)_k\) is the descending factorial. At \(N=3\), the zero-diagonal/zero-row-sum component vanishes identically, so only the first term is used.

For the specified matrices, straightforward polynomial sums give
\[
\begin{gathered}
\operatorname{tr}(A)=\frac{N(N^2-1)}{12},\quad
\operatorname{tr}(B)=\frac{N^2-1}{6},\quad
\operatorname{tr}(AB)=\frac{N(N^4-1)}{120},\\
\sum_i d_{A,i}^2=\frac{N(N^2-1)(N^2-4)}{180},\qquad
 d_{B,i}=\frac1N d_{A,i},\\
\operatorname{tr}(A_0B_0)=\frac{N(N-3)(N-1)(N+1)(3N+2)}{360}.
\end{gathered}
\]
For example, \(\ell^\top M\ell=\sum_{t=1}^{N-1}[t(N-t)/2]^2\), giving \(\operatorname{tr}(AB)\). The other traces follow by summing polynomials of degree at most four. Substitution into the general covariance identity and division by \(ab\) give the boxed covariance. Applying the same identity to \((A,A)\) and \((B,B)\) gives the displayed variances; the additional trace identities used are
\[
\operatorname{tr}(A_0^2)=\frac{N^2(N-3)(N-1)(N+1)(5N+6)}{720},\quad
\operatorname{tr}(B_0^2)=\frac{N(N-3)(N-1)(N+1)}{90}.
\]
The strictly positive covariance also follows directly: the expression in square brackets is minimized, for fixed \(N\), at \(ab=N-1\), where it equals \(N^2-4>0\).

For the correlation-equality classification, with \(h=ab\), put \(U=h(3N+4)-N(2N+1)\), \(V=h(5N+8)-3N(N+1)\), and \(Z=h(4N+4)-3N^2\). Polynomial expansion yields
\[
VZ-2U^2=N(2h-N)(N+2)(h+1-N).
\]
The first factors are strictly positive for \(N\ge3\). Since \(h\ge N-1\), equality holds exactly when \(\min(a,b)=1\). In the interior-ratio limit, retain the leading terms \(U\sim3hN\), \(V\sim5hN\), \(Z\sim4hN\), giving \(3/\sqrt{10}\). Finally, pooled-rank reversal sends \(W\) to \(-W\) while leaving \(T\) unchanged, explaining \(\operatorname{Cov}(W,T)=0\).

## Verification

The standalone Python 3 program `check_rank_energy.py` uses exact rational arithmetic to enumerate all fixed-composition rank words for \(3\le N\le11\), compares five independently enumerated moments/covariances with the displayed formulas for every allowed split, checks positivity and the perfect-correlation boundary, and exits on any disagreement. Execution returned `PASS` with 486 exact assertions. The general all-size claim rests on the preceding algebraic proof, not on the finite enumeration.

## Relationship to prior work

Anderson (1962) gave the classical two-sample Cramér–von Mises criterion, while Pettitt (1979) examined weighted Cramér–von Mises rank statistics and their relation to linear-rank scores including Wilcoxon. Ramdas, García Trillos, and Cuturi (2015) survey links between classical two-sample tests and Brownian-bridge norms. Alvarez-Andrade, Bouzebda, and Lachal (2015) develop integrated empirical-process approximations and two-sample applications. Curry, Dang, and Sang (2018) analyze a related rank-based Cramér–von Mises-type statistic, its separate moments and its relation to the classical criterion. The presently proved joint *finite-population fourth-order* covariance, strict positivity, singleton perfect-correlation characterization, and universal limiting correlation concern a different quantity than the separate marginal moments or asymptotic representations described in the accessible sources.

## Limitations

Historical priority is not established exhaustively. The full Pettitt (1979) text was inaccessible despite open-access retrieval attempts and an institutional access attempt requiring verification, so it remains a material overlap risk. The full Anderson (1962) paper was also not retrieved. Neither an absent search hit nor an abstract establishes novelty. The theorem is for a continuous common null distribution, exact fixed sample sizes, and the specified normalization; it does not give joint tail probabilities, optimal combined-test rejection regions, or power under alternatives.

## References

1. Anderson, T. W. (1962). *On the Distribution of the Two-Sample Cramér–von Mises Criterion.* Annals of Mathematical Statistics 33, 1148–1159. DOI: 10.1214/aoms/1177704477.
2. Pettitt, A. N. (1979). *Two-Sample Cramér–von Mises Type Rank Statistics.* JRSS B 41, 46–53. DOI: 10.1111/j.2517-6161.1979.tb01056.x.
3. Alvarez-Andrade, S., Bouzebda, S., and Lachal, A. (2015). *Some asymptotic results for the integrated empirical process with applications to statistical tests.* arXiv:1505.07345, first posted 2015-05-27.
4. Ramdas, A., García Trillos, N., and Cuturi, M. (2015). *On Wasserstein Two Sample Testing and Related Families of Nonparametric Tests.* arXiv:1509.02237, first posted 2015-09-08.
5. Curry, J., Dang, X., and Sang, H. (2018). *A rank-based Cramér-von-Mises-type test for two samples.* arXiv:1802.06332, first posted 2018-02-18.
