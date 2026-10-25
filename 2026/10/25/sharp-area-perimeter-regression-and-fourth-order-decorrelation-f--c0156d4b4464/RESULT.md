# Sharp area–perimeter regression and fourth-order decorrelation for random cyclic polygons

## Finding

Choose \(n\ge3\) points independently with uniform arclength measure on the Euclidean unit circle, and let \(P_n\) and \(A_n\) be the perimeter and enclosed area of their convex hull. Set
\[
\beta_n=\frac{\operatorname{Cov}(A_n,P_n)}{\operatorname{Var}(P_n)},\qquad
\rho_n=\operatorname{Corr}(A_n,P_n).
\]
The denominator is strictly positive. As \(n\to\infty\),
\[
\boxed{\beta_n=2-\frac{24\pi^2}{n^2}+O(n^{-3})},
\qquad
\boxed{\operatorname{Var}(A_n-\beta_nP_n)\sim\frac{9504\pi^{10}}{n^9}},
\]
and
\[
\boxed{\rho_n=1-\frac{297\pi^4}{10n^4}+o(n^{-4})}.
\]
Moreover, the following *joint* limit holds:
\[
\left(n^{5/2}(P_n-\mathbb EP_n),\ n^{9/2}
\big[(A_n-\mathbb EA_n)-\beta_n(P_n-\mathbb EP_n)\big]\right)
\xrightarrow{\mathrm d}(Z_P,Z_R),
\]
where \(Z_P\) and \(Z_R\) are **independent** centered normal variables with variances \(40\pi^6\) and \(9504\pi^{10}\), respectively. Thus, the population least-squares prediction of area using perimeter has a strictly smaller leading residual variance than the natural fixed-slope prediction \(2P_n\):
\[
\operatorname{Var}(A_n-2P_n)\sim\frac{32544\pi^{10}}{n^9},\qquad
\frac{9504}{32544}=\frac{33}{113}.
\]
These expressions form a single sharp joint-fluctuation and optimal linear-prediction theorem; the earlier fixed-slope cancellation is not claimed as new.

## Assumptions and scope

All random samples are mutually independent and uniform in circular angle (equivalently, unit-circle arclength). Polygon vertices are put in counterclockwise order. Probability-zero coincidences do not matter. The full Euclidean perimeter (not semiperimeter) and ordinary unsigned enclosed area are used. The regression coefficient is the unique population least-squares slope for predicting area by a linear function of perimeter, with an unrestricted intercept. No conditional expectation or global nonlinear-optimality assertion is made.

## Proof

**1. Exact spacing geometry.** Let \(G_1,\dots,G_n>0\) be the circular angular gaps, with \(\sum_iG_i=2\pi\). Their normalized vector has the Dirichlet distribution with all parameters equal to one. Put \(S_k=\sum_iG_i^k\). The exact chord and shoelace formulas are
\[
P_n=2\sum_i\sin(G_i/2),\qquad A_n=\tfrac12\sum_i\sin G_i.
\]
Taylor's theorem, uniformly for \(0\le G_i\le2\pi\), gives
\[
P_n=2\pi-\frac{S_3}{24}+\frac{S_5}{1920}+R_P,
\qquad |R_P|\le\frac{S_7}{322560},
\]
\[
A_n=\pi-\frac{S_3}{12}+\frac{S_5}{240}+R_A,
\qquad |R_A|\le\frac{S_7}{10080}.
\]
In particular, \(A_n-2P_n+3\pi=S_5/320+O(S_7)\).

**2. Exact mixed spacing covariances.** Write \((n)_k=n(n+1)\cdots(n+k-1)\). Dirichlet integration yields, for integers \(k,\ell\ge1\),
\[
\begin{split}
\operatorname{Cov}(S_k,S_\ell)=(2\pi)^{k+\ell}\Bigg[
&\frac{n\big[(k+\ell)!+(n-1)k!\ell!\big]}{(n)_{k+\ell}}\\
&-\frac{n^2k!\ell!}{(n)_k(n)_\ell}\Bigg].
\end{split}
\]
Consequently,
\[
n^{k+\ell-1}\operatorname{Cov}(S_k,S_\ell)
\longrightarrow (2\pi)^{k+\ell}v_{k\ell},\qquad
v_{k\ell}=(k+\ell)!-(1+k\ell)k!\ell!.
\]
The critical numbers are \(v_{33}=360\), \(v_{35}=28800\), and \(v_{55}=3254400\). The same moment formula gives \(\mathbb E[S_7^2]=O(n^{-12})\). All remainder terms above are therefore \(O_{L^2}(n^{-6})\), small enough for the stated regression residual.

**3. Regression slope.** Write \(U=P_n-\mathbb EP_n\), \(V=A_n-\mathbb EA_n\), and use \(\widetilde S_k=S_k-\mathbb ES_k\). By Step 1,
\[
V-2U=\frac{\widetilde S_5}{320}+O_{L^2}(n^{-6}),
\qquad U=-\frac{\widetilde S_3}{24}+O_{L^2}(n^{-9/2}).
\]
Let \(q_n=\operatorname{Cov}(S_3,S_5)/\operatorname{Var}(S_3)\). Step 2 gives \(q_n=320\pi^2n^{-2}+O(n^{-3})\). The identity \(\beta_n=2+\operatorname{Cov}(V-2U,U)/\operatorname{Var}(U)\) now gives
\[
\beta_n=2-\frac{3q_n}{40}+O(n^{-3})
=2-24\pi^2n^{-2}+O(n^{-3}).
\]
In particular, the centered least-squares residual satisfies
\[
V-\beta_nU=\frac1{320}(\widetilde S_5-q_n\widetilde S_3)
+o_{L^2}(n^{-9/2}).
\]
This is the nontrivial projection step: the fixed-slope combination retains the entire quintic fluctuation, whereas the least-squares slope projects out the part predictable from the cubic fluctuation.

**4. Limit theorem and sharp constants.** Let \(E_i\) be independent unit exponential random variables. The representation \(G_i=2\pi E_i/\sum_jE_j\) shows that \(n^{k-1}S_k=(2\pi)^k\overline{E^k}/\overline E^{\,k}\). The multivariate central limit theorem and delta method give a centered joint Gaussian limit for \(n^{5/2}\widetilde S_3\) and \(n^{9/2}\widetilde S_5\), with covariance matrix
\[
\begin{pmatrix}
360(2\pi)^6&28800(2\pi)^8\\
28800(2\pi)^8&3254400(2\pi)^{10}
\end{pmatrix}.
\]
Indeed, the influence function for power \(k\) is \(E^k-k!-kk!(E-1)\). In Step 3, the projected quintic variance is therefore
\[
\frac{(2\pi)^{10}}{320^2}\left(3254400-\frac{28800^2}{360}\right)
=9504\pi^{10}.
\]
The leading perimeter variance is \(360(2\pi)^6/24^2=40\pi^6\). The Gaussian limiting coordinates are uncorrelated by the explicit projection, hence independent. Uniform square-integrability for variance asymptotics follows from the exact Dirichlet moments and Taylor remainder bounds, not from convergence in law alone. The full fixed-slope variance is \(3254400(2\pi)^{10}/320^2=32544\pi^{10}\).

Finally, for the population correlation \(\rho_n\), exact least-squares algebra gives
\[
1-\rho_n^2=\frac{\operatorname{Var}(A_n-\beta_nP_n)}{\operatorname{Var}(A_n)}.
\]
Since \(\operatorname{Var}(A_n)\sim160\pi^6n^{-5}\) and \(\rho_n\to1\), this implies \(n^4(1-\rho_n)\to9504\pi^4/(2\cdot160)=297\pi^4/10\). All assertions follow.

## Verification

Run `python3 verify_area_perimeter.py` from a directory containing the two files. The program uses only Python's standard library. It (i) checks all factorial-moment constants exactly using rational arithmetic; (ii) compares independently reconstructed Cartesian polygon perimeters and shoelace areas with the gap formulas; (iii) confirms exact mixed Dirichlet covariances; and (iv) computes finite-sample regression quantities at large \(n\) with 85-digit Decimal arithmetic, using eleventh-degree sine truncations. The numerical asymptotic checks are corroboration, not a substitute for the preceding infinite-sample proof.

## Relationship to prior work

Bélisle (2011) proved univariate asymptotic laws for area and perimeter of the same random cyclic polygon model. Xu, Meng and Li (2019), and Wang, Xu and Liu (2021), studied extrapolation combinations; the latter proves a limit law for the fixed combination \(\frac43(P_n/2)-\frac13A_n\), whose variance corresponds to the \(32544\pi^{10}\) fixed-slope residual above. **That cancellation and its Gaussian limit are prior results.** The claim here is the different, population-optimal *regression coefficient*, its additional projected-variance reduction, the independent joint residual limit, and the sharp fourth-order area–perimeter correlation deficit. Those conclusions require the mixed cubic–quintic covariance, which is not among the statements located in the inspected literature. This does not establish exhaustive historical priority.

## Limitations

The theorem is restricted to independent uniform sampling on a circle and the population-optimal *linear* predictor. It does not assert optimality over all nonlinear functions of perimeter, nor cover nonuniform sampling, arbitrary ovals, or finite-sample closed forms for the regression slope. One historically plausible early paper was only available by abstract, so independent literature verification remains necessary.

## References

1. C. Bélisle, “On the polygon generated by n random points on a circle,” *Statistics & Probability Letters* 81 (2011), 236–242. DOI: `10.1016/j.spl.2010.11.012`.
2. W.-Q. Xu, L. Meng, and Y. Li, “Random Polygons and Estimations of π,” *Open Mathematics* 17 (2019), 575–581. DOI: `10.1515/math-2019-0049`.
3. S. Wang, W.-Q. Xu, and J. Liu, “Random Polygons and Optimal Extrapolation Estimates of π,” *Statistics, Optimization & Information Computing* 9 (2021), 241–249. DOI: `10.19139/soic-2310-5070-1193`.
4. D. A. Darling, “On a class of problems related to the random division of an interval,” *Annals of Mathematical Statistics* 24 (1953), 239–253. DOI: `10.1214/aoms/1177729030`.
