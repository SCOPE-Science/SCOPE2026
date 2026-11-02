# Fourth-order area–perimeter decorrelation in random cyclic polygons

## Finding
Let \(n\ge3\) independent points be uniform on the unit circle, and let \(S_n\) and \(A_n\) be the semiperimeter and area of their convex-hull polygon. Define \(\rho_n=\operatorname{Corr}(S_n,A_n)\) and the *exact finite-sample least-squares coefficient*
\[
\beta_n=\frac{\operatorname{Cov}(A_n,S_n)}{\operatorname{Var}(S_n)}.
\]
As \(n\to\infty\),
\[
\boxed{\beta_n=4-\frac{48\pi^2}{n^2}+o(n^{-2}),\qquad
\rho_n=1-\frac{297\pi^4}{10n^4}+o(n^{-4}).}
\]
Moreover, with \(\widetilde S_n=S_n-\mathbb E S_n\) and \(\widetilde A_n=A_n-\mathbb E A_n\),
\[
\boxed{n^{9/2}(\widetilde A_n-\beta_n\widetilde S_n)
\ \xrightarrow{\mathrm d}\ \mathcal N(0,9504\pi^{10}),\qquad
n^9\operatorname{Var}(\widetilde A_n-\beta_n\widetilde S_n)\to9504\pi^{10}.}
\]
The optimally projected residual has asymptotically \(33/113\) of the variance of the classical centered fixed-slope residual \(\widetilde A_n-4\widetilde S_n\), at their common \(n^{-9/2}\) fluctuation scale. This is a statement about predicting centered area from centered semiperimeter, *not* about knowing the circle constant from observed polygons.

## Assumptions and scope
The points are iid and arclength-uniform on the circumference of a Euclidean unit disk; all polygons use the *entire* sample, without maximizing over subsets. Their clockwise/counterclockwise ordering is immaterial. Put \(D_1,\ldots,D_n\) for the successive normalized circular gaps, after rooting at a randomly designated sampled vertex. Then \(D=(D_i)\sim\operatorname{Dirichlet}(1,\ldots,1)\), \(\sum_iD_i=1\), and
\[
S_n=\sum_{i=1}^n\sin(\pi D_i),\qquad A_n=\frac12\sum_{i=1}^n\sin(2\pi D_i).
\]
The variance in the definition of \(\beta_n\) is positive for \(n\ge3\). All asymptotics hold through integers \(n\ge3\). The same correlation holds for full perimeter \(2S_n\), while the corresponding regression coefficient for full perimeter is \(\beta_n/2\).

## Proof
**Exact Dirichlet moments.** For \(r\ge1\), set \(P_r=\sum_iD_i^r\), and write \(n^{\overline{k}}=n(n+1)\cdots(n+k-1)\). The Dirichlet moment formula yields, for integers \(r,s\ge1\),
\[
\mathbb EP_r=\frac{nr!}{n^{\overline r}},\qquad
\mathbb E[P_rP_s]=\frac{n\big((r+s)!+(n-1)r!s!\big)}{n^{\overline{r+s}}}.
\tag{1}
\]
Consequently,
\[
\operatorname{Cov}(P_r,P_s)
=\kappa_{rs}\,n^{1-r-s}+o(n^{1-r-s}),\quad
\kappa_{rs}=(r+s)!-(1+rs)r!s!.
\tag{2}
\]
In particular, \(\kappa_{33}=360\), \(\kappa_{35}=28800\), and \(\kappa_{55}=3254400\).

**Joint limit for gap power sums.** Write \(D_i=E_i/T_n\), where \(E_i\) are iid rate-one exponential random variables and \(T_n=\sum_iE_i\). Applying the multivariate central limit theorem and delta method to empirical means of \((E_i,E_i^3,E_i^5)\) gives
\[
\left(n^{5/2}(P_3-\mathbb EP_3),\ n^{9/2}(P_5-\mathbb EP_5)\right)
\xrightarrow{\mathrm d}\mathcal N\!\left(0,
\begin{pmatrix}360&28800\\28800&3254400\end{pmatrix}\right).
\tag{3}
\]
Indeed the influence function for power \(r\) is \(E^r-r!-rr!(E-1)\), whose cross-moment is \(\kappa_{rs}\). Equation (1) also gives convergence of the corresponding covariance matrices, so subsequent variance limits do not rely merely on weak convergence.

**Geometric expansions with controlled error.** Taylor's inequality uniformly on \([0,1]\) and (1) give \(\|P_7\|_2=O(n^{-6})\). Hence, with \(a=\pi^3/6\), \(b=\pi^5/120\), and centered random variables denoted by tildes,
\[
\widetilde S_n=-a\widetilde P_3+b\widetilde P_5+O_{L^2}(n^{-6}),\quad
\widetilde A_n=-4a\widetilde P_3+16b\widetilde P_5+O_{L^2}(n^{-6}).
\tag{4}
\]
It follows from (2)–(4) that
\[
\operatorname{Var}(S_n)\sim10\pi^6n^{-5},\qquad
\operatorname{Var}(A_n)\sim160\pi^6n^{-5},
\tag{5}
\]
and, using \(16b-4b=12b=\pi^5/10\),
\[
\beta_n-4=\frac{\operatorname{Cov}(\widetilde A_n-4\widetilde S_n,\widetilde S_n)}{\operatorname{Var}(S_n)}
=-\frac{48\pi^2}{n^2}+o(n^{-2}).
\tag{6}
\]
Because \(n^{9/2}\|\widetilde P_7\|_2\to0\) and the errors in (6) multiply a quantity of order \(n^{-5/2}\) in \(L^2\),
\[
\widetilde A_n-\beta_n\widetilde S_n
=\frac{\pi^5}{10}\left(\widetilde P_5-\frac{80}{n^2}\widetilde P_3\right)+o_{L^2}(n^{-9/2}).
\tag{7}
\]
The variance of the Gaussian limit in (7) is
\[
\left(\frac{\pi^5}{10}\right)^2
\left(\kappa_{55}-160\kappa_{35}+6400\kappa_{33}\right)
=9504\pi^{10}.
\tag{8}
\]
Equations (3), (7), and (8) prove both the residual central limit theorem and the variance limit. The exact regression identity
\[
1-\rho_n^2=
\frac{\operatorname{Var}(\widetilde A_n-\beta_n\widetilde S_n)}{\operatorname{Var}(A_n)}
\tag{9}
\]
with (5), (8) and \(\rho_n\to1\) yields \(n^4(1-\rho_n)\to9504\pi^4/320=297\pi^4/10\). With slope fixed at \(4\), the analogous limiting residual variance is \((\pi^{10}/100)\kappa_{55}=32544\pi^{10}\), proving the ratio \(9504/32544=33/113\).

## Verification
The standalone standard-library script `VERIFIER.py` checks the exact Dirichlet factorial moments, the three influence-function covariance constants, the orthogonal residual variance, regression/correlation asymptotic convergence from high-precision finite sums, and an independently evaluated two-dimensional simplex integral at three vertices. In its recorded execution it passed 76 deterministic assertions. The infinite-size results follow from (1)–(9), not the finite checks.

## Relationship to prior work
Bélisle (2011) studied individual area/perimeter asymptotics for random circular polygons. Xu, Meng and Li (2019) studied the fixed-slope extrapolation \((4S_n-A_n)/3\) and means. Wang, Xu and Liu (2021, Lemma 2.2 and Section 2) provide a fixed-slope Gaussian limit, for which \(n^9\operatorname{Var}(\widetilde A_n-4\widetilde S_n)\to32544\pi^{10}\), and univariate power-sum CLTs. The present claim instead identifies the *optimal \(n\)-dependent linear predictor*, the orthogonalized joint Gaussian residual, its smaller limiting variance, and the fourth-order correlation deficit. Koroleva and Nikitin (arXiv:1301.1360) address maximum-area/perimeter statistics over smaller vertex subsets, not the full-sample joint regression. These distinctions are comparisons of claims; they are not proofs of global priority.

## Limitations
The theorem concerns iid uniform points on one circle, not arbitrary smooth convex curves, nonuniform sampling, or point sets uniform in the disk. It gives leading asymptotics, not an elementary closed form for each finite \(\beta_n\), and linear prediction, not conditional expectation. Relevant older papers may contain equivalent implicit joint-moment statements; in particular, complete text for Bélisle (2011) could not be accessed for a conclusive priority comparison. The scientific checks reported here are not an independent audit.

## References
1. C. Bélisle, *On the polygon generated by n random points on a circle*, Statistics & Probability Letters 81 (2011), 236–242, doi:10.1016/j.spl.2010.11.012.
2. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first publicly posted 2013-01-07.
3. W.-Q. Xu, L. Meng and Y. Li, *Random Polygons and Estimations of π*, Open Mathematics 17 (2019), 575–581, doi:10.1515/math-2019-0049.
4. S. Wang, W.-Q. Xu and J. Liu, *Random Polygons and Optimal Extrapolation Estimates of π*, Statistics, Optimization & Information Computing 9 (2021), 241–249, doi:10.19139/soic-2310-5070-1193.
