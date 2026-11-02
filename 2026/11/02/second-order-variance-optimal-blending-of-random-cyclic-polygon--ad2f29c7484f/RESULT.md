# Second-order variance-optimal blending of random cyclic polygon area and semiperimeter

## Finding

Let \(n\ge3\) independent uniform points on the Euclidean unit circle generate their convex hull. Denote its semiperimeter by \(S_n\) and its (ordinary unsigned) area by \(A_n\). For every real \(\lambda\), put
\[
T_n(\lambda)=(1+\lambda)S_n-\lambda A_n.
\]
There is exactly one finite-\(n\) minimizer of \(\operatorname{Var}(T_n(\lambda))\), namely
\[
\lambda_n^\star=\frac{\operatorname{Cov}(S_n,A_n-S_n)}{\operatorname{Var}(A_n-S_n)}.
\]
The following sharp asymptotic laws hold:
\[
\lim_{n\to\infty}n^2\left(\lambda_n^\star-\frac13\right)=\frac{16\pi^2}{3},
\qquad
\lim_{n\to\infty}n^9\operatorname{Var}\bigl(T_n(\lambda_n^\star)\bigr)=1056\pi^{10}.
\]
The explicit deterministic choice \(\widehat\lambda_n=1/3+16\pi^2/(3n^2)\) gives the same variance limit; the classical fixed coefficient \(1/3\) gives \(3616\pi^{10}\). Thus the leading variance is reduced by exactly \(80/113\) relative to the fixed classical blend, and its optimized-to-classical ratio is \(33/113\). Furthermore,
\[
\lim_{n\to\infty}n^4\left[1-\operatorname{Corr}(S_n,A_n)\right]=\frac{297}{10}\pi^4.
\]
The known fixed-weight \(3616\pi^{10}\) limit is included for comparison, not claimed as new. The new assertions concern finite-sample variance optimization, its sharp second-order scaling, the improved leading variance, and the quantified correlation defect.

## Assumptions and scope

The points are independent and uniform in Euclidean arclength on a circle of radius one, with no repeated points almost surely. Their cyclic angular spacings divided by \(2\pi\) are \((D_1,\dots,D_n)\sim\operatorname{Dirichlet}(1,\dots,1)\). Define \(U_{k,n}=\sum_{i=1}^nD_i^k\). For each \(n\ge3\),
\[
S_n=\sum_{i=1}^n\sin(\pi D_i),\qquad
A_n=\frac12\sum_{i=1}^n\sin(2\pi D_i).
\]
All variances and covariances are taken with respect to the joint law of the original \(n\) points. The coefficient \(\lambda_n^\star\) is a population optimum, not an empirically fitted estimator. Optimizing variance is distinct from minimizing bias or mean squared error; the explicit corrected coefficient contains the constant \(\pi\).

## Proof

**1. Exact gap covariances.** Write the rising factorial \((n)_k=n(n+1)\cdots(n+k-1)\). Standard beta-integral evaluation on the Dirichlet simplex gives, for integers \(k,l\ge1\),
\[
\mathbb EU_{k,n}=\frac{nk!}{(n)_k},\quad
\mathbb E[U_{k,n}U_{l,n}]=\frac{n(k+l)!+n(n-1)k!l!}{(n)_{k+l}}.
\]
Consequently
\[
\lim_{n\to\infty}n^{k+l-1}\operatorname{Cov}(U_{k,n},U_{l,n})
=\sigma_{kl}:=(k+l)!-(1+kl)k!l!.
\]
The three needed constants are \(\sigma_{33}=360\), \(\sigma_{35}=28800\), \(\sigma_{55}=3254400\), and the positive Schur complement is
\[
\sigma_{55}-\sigma_{35}^2/\sigma_{33}=950400.
\]
All identities are exact consequences of the displayed finite-\(n\) moments, not independence approximations for the gaps.

**2. Mean-square Taylor control.** Let centered variables carry a superscript \(\circ\). Taylor's theorem on \([0,1]\), with bounded trigonometric derivatives, gives
\[
S_n=\pi-aU_{3,n}+bU_{5,n}+E_n,\quad
A_n=\pi-4aU_{3,n}+16bU_{5,n}+F_n,
\]
where \(a=\pi^3/6\), \(b=\pi^5/120\), and \(|E_n|+|F_n|\le C U_{7,n}\) for an absolute \(C\). Since
\[
\mathbb E[U_{7,n}^2]
=\frac{n14!+n(n-1)(7!)^2}{(n)_{14}}=O(n^{-12}),
\]
the remainders have \(L^2\)-norm \(O(n^{-6})\). Writing \(R_n=A_n-4S_n+3\pi\) and \(c=12b=\pi^5/10\) yields
\[
S_n^\circ=-aU_{3,n}^\circ+O_{L^2}(n^{-9/2}),\quad
R_n^\circ=cU_{5,n}^\circ+O_{L^2}(n^{-6}).
\]
Here \(\|U_{5,n}^\circ\|_2=O(n^{-9/2})\) and \(\|U_{3,n}^\circ\|_2=O(n^{-5/2})\). The exact asymptotic covariance constants and Cauchy–Schwarz therefore justify every limit below. Put \(B_n=A_n-S_n=3S_n+R_n-3\pi\). Thus
\[
\begin{aligned}
\operatorname{Var}(B_n)&\sim 9a^2\sigma_{33}n^{-5},\\
\operatorname{Cov}(R_n,B_n)&\sim -3ac\sigma_{35}n^{-7},\\
\operatorname{Var}(R_n)&\sim c^2\sigma_{55}n^{-9}.
\end{aligned}
\]
The first relation also follows from the nondegenerate variance of the third-power gap sum.

**3. The exact minimizer and its correction.** For each \(n\), \(B_n=A_n-S_n\) is not almost surely constant: it changes between configurations with nearly equal gaps and configurations with one gap near one, which occur in open regions of positive Dirichlet density. Therefore its variance is strictly positive and the quadratic \(\operatorname{Var}(S_n-\lambda B_n)\) has a unique minimizer. Because \(T_n(1/3)=\pi-R_n/3\), set \(\delta=\lambda-1/3\), obtaining \(T_n(\lambda)=\pi-R_n/3-\delta B_n\). Completing the square gives
\[
\lambda_n^\star-\frac13=-\frac{\operatorname{Cov}(R_n,B_n)}{3\operatorname{Var}(B_n)}
\sim\frac{c}{9a}\frac{\sigma_{35}}{\sigma_{33}}n^{-2}
=\frac{16\pi^2}{3n^2}.
\]
The exact minimum variance is
\[
\frac19\left[\operatorname{Var}(R_n)-\frac{\operatorname{Cov}(R_n,B_n)^2}{\operatorname{Var}(B_n)}\right].
\]
By the three joint asymptotics its \(n^9\)-scaled limit equals
\[
\frac{c^2}{9}\left(\sigma_{55}-\frac{\sigma_{35}^2}{\sigma_{33}}\right)
=\frac{\pi^{10}}{900}\cdot950400=1056\pi^{10}.
\]
The fixed coefficient \(1/3\) instead produces \(c^2\sigma_{55}/9=3616\pi^{10}\), consistent with the earlier published central limit theorem. Since \(\widehat\lambda_n-\lambda_n^\star=o(n^{-2})\) and \(\operatorname{Var}(B_n)=O(n^{-5})\), the exact quadratic completion shows that the explicit choice has the same \(n^{-9}\) variance constant.

**4. The sharp area–perimeter correlation defect.** Since \(A_n=4S_n+R_n-3\pi\), the determinant identity
\[
\det\operatorname{Cov}(S_n,A_n)=\det\operatorname{Cov}(S_n,R_n)
\]
is exact. Using the same three moment limits,
\[
\begin{aligned}
\operatorname{Var}(S_n)&\sim a^2\sigma_{33}n^{-5},\\
\operatorname{Var}(A_n)&\sim16a^2\sigma_{33}n^{-5},\\
\det\operatorname{Cov}(S_n,A_n)&\sim a^2c^2(\sigma_{33}\sigma_{55}-\sigma_{35}^2)n^{-14}.
\end{aligned}
\]
The correlation is positive for all sufficiently large \(n\), and \(1-\rho_n^2=(\det\operatorname{Cov})/[\operatorname{Var}(S_n)\operatorname{Var}(A_n)]\). Hence
\[
\lim_{n\to\infty}n^4(1-\rho_n)=
\frac{c^2}{32a^2}\frac{\sigma_{33}\sigma_{55}-\sigma_{35}^2}{\sigma_{33}^2}
=\frac{297}{10}\pi^4.
\]
This completes the theorem.

## Verification

The self-contained standard-library script `verify.py` checks the exact finite Dirichlet covariance formula against rational arithmetic, the three factorial covariance limits, the variance constants, the optimal second-order coefficient, and the correlation coefficient. Run `python3 verify.py` for deterministic exact checks; `python3 verify.py --simulation` additionally checks area and semiperimeter from independent Dirichlet gap samples, an equivalent representation of uniform circle endpoints. Representative independently calculated finite-\(n\) values of \(n^2(\lambda_n^\star-1/3)\) are approximately \(45.259\) at \(n=80\), \(48.705\) at \(n=160\), and \(51.609\) at \(n=640\), approaching \(16\pi^2/3\approx52.638\). Finite simulations are corroboration only; the proof above establishes all infinite statements.

## Relationship to prior work

Xu, Meng and Li (2019), Wang, Xu and Liu (2021), and Wang, Li and Xu (2023) study random cyclic polygon estimates and extrapolation of \(\pi\). The leading cancellation at fixed coefficient \(1/3\), including the \(3616\pi^{10}\) variance constant, is established in this literature and is **not** new here. The 2023 paper develops nonlinear extrapolations and a general covariance/central-limit framework involving third and fifth powers of normalized spacings. These existing moment tools contain much of the raw analytical input to the present calculation. What is resolved here is a different and narrower optimization: for the two-observable, inscribed-only blend, optimize its *actual variance for each \(n\)* and then extract the second-order optimal weight, the exact reduced limiting variance \(1056\pi^{10}\), and the first nonzero area–semiperimeter correlation deficit. The fixed-weight convergence and higher-order bias-optimized estimators in earlier papers address different criteria. Historical priority of these exact refined constants has not been independently certified.

## Limitations

The optimum minimizes variance, **not** bias, root mean squared error, or total approximation error. Its exact finite-\(n\) formula uses population covariances; the explicit asymptotically optimal coefficient contains \(\pi\) and is not a standalone procedure for estimating that unknown constant. Only iid uniform boundary points on the circle are considered; no affine, nonuniform, or interior sampling generalization is asserted. The correlation expansion concerns \(n\to\infty\), not an exact formula for each finite \(n\). Earlier general extrapolation theorems provide substantial ingredients, so historical-priority assessment should be treated cautiously.

## References

1. W.-Q. Xu, L. Meng, and Y. Li, “Random Polygons and Estimations of Pi,” *Open Mathematics* 17 (2019), 575–581. DOI: 10.1515/math-2019-0049.
2. S. Wang, W.-Q. Xu, and J. Liu, “Random Polygons and Optimal Extrapolation Estimates of Pi,” *Statistics, Optimization & Information Computing* 9 (2021), 241–249. DOI: 10.19139/soic-2310-5070-1193.
3. S. Wang, Z. Li, and W.-Q. Xu, “Nonlinear Random Extrapolation Estimates of Pi under Dirichlet Distributions,” *Journal of Numerical Analysis and Approximation Theory* 52 (2023), 273–294. DOI: 10.33993/jnaat522-1360.
4. W.-Q. Xu and S. Wang, “Random Cyclic Polygons from Dirichlet Distributions and Approximations of Pi,” *Statistics & Probability Letters* 140 (2018). DOI: 10.1016/j.spl.2018.05.007 (full text not inspected).
