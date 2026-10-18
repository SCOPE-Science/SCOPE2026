# Critical-window and fixed-parameter Hilbert–Schmidt laws for beta-Hausdorff matrices

## Finding

Let \(a,b>0\) and \(N\geq1\) be real shape parameters and an integer dimension. The finite beta-Hausdorff matrix is the lower-triangular real matrix
\[
H_N(a,b)_{nk}=\binom nk\frac{B(k+a,n-k+b)}{B(a,b)}\quad(0\leq k\leq n<N),
\]
with zero entries above the diagonal. Write \(E_N(a,b)=\|H_N(a,b)\|_{\mathrm{HS}}^2\), \(C(a,b)=1/B(a,b)\), \(m=\min\{a,b\}\), and \(r=2\) when \(a=b\), otherwise \(r=1\). Then, with all shape parameters fixed as \(N\to\infty\),
\[
E_N(a,b)\sim\begin{cases}
\displaystyle \frac{r C(a,b)^2\Gamma(m)^2\Gamma(1-2m)}{(1-2m)\Gamma(1-m)^2}N^{1-2m},&0<m<\tfrac12,\\[7pt]
\displaystyle \frac{r C(a,b)^2}{2}(\log N)^2,&m=\tfrac12,\\[7pt]
\displaystyle C(a,b)^2 B(2a-1,2b-1)\log N,&m>\tfrac12.
\end{cases}
\]
Here \(\sim\) means the ratio of the two positive expressions tends to one. The middle case covers one or two shapes equal to \(1/2\), with all other shapes at least \(1/2\).

The transition has an explicit **uniform two-parameter critical window**. Fix \(R>0\), and for \(|u|,|v|\leq R\), set \(L=\log N\), \(a_N=\tfrac12+u/L\), \(b_N=\tfrac12+v/L\); take \(N\) sufficiently large that both are positive. Define the continuous function
\[
\Phi(z)=\int_0^1\frac{1-e^{-2zs}}{2z}\,ds
=\begin{cases}\displaystyle\frac{2z-1+e^{-2z}}{4z^2},&z\ne0,\\[6pt]\tfrac12,&z=0.\end{cases}
\]
Then
\[
\boxed{\ E_N(a_N,b_N)=\frac{(\log N)^2}{\pi^2}\bigl(\Phi(u)+\Phi(v)\bigr)+O_R(\log N).\ }
\]
The constant in \(O_R\) depends only on \(R\), not on \(N,u,v\). In particular the symmetric arcsine matrix satisfies \(E_N(1/2,1/2)\sim (\log N)^2/\pi^2\), whereas \(H_N(1,1)\) is finite Cesàro averaging and satisfies the exact identity \(E_N(1,1)=\sum_{j=1}^N1/j\).

## Assumptions and scope

All matrices are finite, real, with rows and columns indexed from zero. The Hilbert–Schmidt norm is defined by the sum of squares of *all* matrix entries, not by the operator norm or a normalized trace. \(B\) and \(\Gamma\) are the beta and gamma functions with their usual positive-real normalizations. For the critical-window statement \(R\) is fixed *before* \(N\) varies; uniformity is not claimed if \(|u|\) or \(|v|\) grows with \(N\). The formulas concern the full finite matrix, and do not claim a Schatten-class property of the infinite Hausdorff operator.

## Proof

**Exact reduction.** For \(t>0\), let \(w_t(k)=[\Gamma(k+t)/\Gamma(k+1)]^2\), \(k\geq0\). The beta integral and the binomial identity give, exactly,
\[
H_N(a,b)_{nk}=C(a,b)\frac{\Gamma(n+1)}{\Gamma(n+a+b)}\frac{\Gamma(k+a)}{\Gamma(k+1)}\frac{\Gamma(n-k+b)}{\Gamma(n-k+1)}.
\]
Consequently each complete row has squared mass
\[
S_n(a,b)=C(a,b)^2\left[\frac{\Gamma(n+1)}{\Gamma(n+a+b)}\right]^2
\sum_{k=0}^n w_a(k)w_b(n-k),\qquad E_N=\sum_{n=0}^{N-1}S_n.
\]
Uniformly when \(t\) ranges over a fixed compact subset of \((0,\infty)\), the gamma-ratio estimate is
\(w_t(k)=k^{2t-2}(1+O(1/k))\) for \(k\geq1\), and the prefactor is \(n^{2-2a-2b}(1+O(1/n))\) for \(n\geq1\). These follow, for instance, by applying the standard uniform logarithmic Stirling expansion to both gamma differences.

**Fixed-parameter convolution.** If \(a,b>1/2\), the endpoint-singularity-integrable Riemann-sum theorem, with endpoint bounds from \(w_t(k)=O((k+1)^{2t-2})\), gives
\[
\sum_{k=0}^n w_a(k)w_b(n-k)
\sim n^{2a+2b-3}B(2a-1,2b-1).
\]
Thus \(S_n\sim C(a,b)^2 B(2a-1,2b-1)/n\). If \(a=1/2<b\), the contribution from \(k\) near zero instead is \(n^{2b-2}\log n\), while the other endpoint and the bulk are smaller; hence \(S_n\sim C(a,b)^2\log n/n\). Interchanging parameters gives the other asymmetric case. If \(a=b=1/2\), both ends contribute, so \(S_n\sim2C(a,b)^2\log n/n\).

If \(a=m<1/2\) and \(a<b\), the summable endpoint dominates. Indeed the convergent series
\[
U_m=\sum_{k=0}^{\infty}w_m(k)=\Gamma(m)^2\,{}_2F_1(m,m;1;1)
=\frac{\Gamma(m)^2\Gamma(1-2m)}{\Gamma(1-m)^2}
\]
is evaluated by Gauss's hypergeometric summation, valid because \(1-2m>0\). Splitting the convolution into the two halves shows its leading term is \(U_m n^{2b-2}\): dominated convergence applies to the side with fixed small \(k\); the other half is \(o(n^{2b-2})\), by the regular-variation bounds above. It follows that \(S_n\sim C(a,b)^2U_m n^{-2m}\). If \(a=b=m<1/2\), the equal endpoint contributions double this value. Interchanging \(a,b\) handles the remaining cases. Finally, standard positive-series summation gives \(\sum_{n<N}n^{-2m}\sim N^{1-2m}/(1-2m)\), \(\sum_{n<N}(\log n)/n\sim(\log N)^2/2\), and \(\sum_{n<N}1/n\sim\log N\). The fixed-parameter formula follows, including the cases with equal minimal parameters.

**Uniform crossover estimate.** Fix \(R\), set \(L=\log N\), and write \(\delta_a=2u/L\), \(\delta_b=2v/L\), \(a=(1+\delta_a)/2\), \(b=(1+\delta_b)/2\). For sufficiently large \(N\), both parameters are in a compact subinterval of \((0,\infty)\). Uniformly for \(2\leq n<N\), the gamma ratios obey
\[
w_a(k)=k^{-1+\delta_a}(1+O_R(1/k)),\quad k\geq1,
\qquad\left[\frac{\Gamma(n+1)}{\Gamma(n+a+b)}\right]^2
=n^{-\delta_a-\delta_b}(1+O_R(1/n)).
\]
On \(0\leq k\leq n/2\), the factor involving \(n-k\) differs from \(n^{-1+\delta_b}\) by a relative \(O_R((k+1)/n)\). The corresponding weighted sum of errors is bounded because \(\sum_{k\leq n/2}(k+1)w_a(k)=O_R(n^{1+\delta_a})\). Also, uniformly for \(|\delta_a|\leq2R/L\) and \(n\leq N\),
\[
\sum_{k\leq n/2} w_a(k)=\frac{(n/2)^{\delta_a}-1}{\delta_a}+O_R(1),
\]
where the quotient is interpreted as \(\log(n/2)\) when \(\delta_a=0\). This follows by the integral test and the summable gamma-ratio remainder \(O_R(k^{-2+\delta_a})\). Apply the symmetric argument to the other half (assign the central summand to one half only). Since \(n^{\pm\delta_a}\), \(n^{\pm\delta_b}\) stay within constants depending on \(R\), the replacement of \(n/2\) with \(n\) changes the result by \(O_R(1)\). After multiplying by the prefactor, one obtains the **uniform row estimate**
\[
S_n(a,b)=\frac{C(a,b)^2}{n}
\left(\frac{1-n^{-\delta_a}}{\delta_a}+\frac{1-n^{-\delta_b}}{\delta_b}\right)+O_R(1/n),
\qquad 2\leq n<N.
\]
The error constant is independent of \(u,v,n,N\) in the prescribed range; the rows \(n=0,1\) contribute \(O_R(1)\). Define \(g_z(s)=(1-e^{-2zs})/(2z)\), continuously extended to \(g_0(s)=s\). Then the bracket equals \(L[g_u(\log n/L)+g_v(\log n/L)]\). The functions \(g_z\) and their first derivatives are uniformly bounded for \(|z|\leq R\), \(0\leq s\leq1\). Comparing the logarithmic harmonic sum with its integral yields, uniformly,
\[
L\sum_{n=2}^{N-1}\frac{g_z(\log n/L)}n
=L^2\int_0^1g_z(s)\,ds+O_R(L)=L^2\Phi(z)+O_R(L).
\]
Lastly \(C(a_N,b_N)^2=\pi^{-2}+O_R(1/L)\) by smoothness of the beta function. Summing the row error \(O_R(1/n)\) gives \(O_R(L)\), proving the claimed uniform crossover with the stated remainder.

## Verification

The included standard-library-only `check_beta_hausdorff.py` checks exact rational beta-binomial row normalization, positivity, reflection, endpoint entries, and finite Cesàro row energy; it compares a logarithmic-gamma recurrence to exact fractions and inspects several critical-window instances. Run with `python3 check_beta_hausdorff.py`. The key infinite-dimensional and parameter-uniform estimates above are proved analytically; finite checks are not used as an extrapolation argument.

## Relationship to prior work

Goldstein and Reinert (arXiv:1207.1460) study the Pólya–Eggenberger urn and its beta-binomial distribution, obtaining Wasserstein approximation bounds; their distribution is the row probability used here, but their analysis does not state a finite-matrix Hilbert–Schmidt transition or two-shape logarithmic window. Bellavita, Chalmoukis, Daskalogiannis and Stylogiannis (arXiv:2307.15334) give the general measure-induced Hausdorff matrix and study associated *generalized Hilbert matrices* on Hardy spaces. Their operator and conclusions differ from the squared Frobenius mass of finite beta-Hausdorff sections. Talebi's generalized Hausdorff-matrix study (DOI below) gives norm inequalities, not the displayed energy asymptotics. General convolution and hypergeometric formulas underpin the fixed-parameter arguments; the uniform two-parameter \((\log N)^{-1}\) critical-window estimate is the distinct additional conclusion.

## Limitations

The error constant \(O_R\) is proved to exist but not optimized. Fixed-parameter limits do not give a uniform approximation for arbitrary parameter sequences away from the stipulated critical window. A non-exhaustive literature search cannot establish absolute priority; potentially differently phrased sequence-space or urn collision results may overlap. No independent mathematical or bibliographic assessment is asserted.

## References

1. L. Goldstein and G. Reinert, *Stein's method for the Beta distribution and the Pólya-Eggenberger Urn*, arXiv:1207.1460, first submitted 2012-07-05. https://arxiv.org/html/1207.1460v2
2. C. Bellavita, N. Chalmoukis, V. Daskalogiannis and G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, arXiv:2307.15334. https://arxiv.org/html/2307.15334v2
3. G. Talebi, *New results for generalized Hausdorff matrices*, *Journal of Inequalities and Applications* (2025), doi:10.1186/s13660-025-03354-y. https://link.springer.com/article/10.1186/s13660-025-03354-y
