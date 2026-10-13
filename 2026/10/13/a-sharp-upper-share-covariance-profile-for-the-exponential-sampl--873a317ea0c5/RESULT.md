# A sharp upper-share covariance profile for the exponential sample Gini index

## Finding
Let \(n\ge2\), let \(X_1,\ldots,X_n\) be independent exponential random variables of a common rate \(\lambda>0\), and write \(X_{(1)}<\cdots<X_{(n)}\) for their order statistics. Put
\[
G_n=\frac{\sum_{1\le i<j\le n}|X_i-X_j|}{n\sum_{i=1}^n X_i},\qquad
T_{n,k}=\frac{\sum_{j=n-k+1}^{n}X_{(j)}}{\sum_{i=1}^n X_i},\qquad 1\le k\le n.
\]
Here \(G_n\) is the ordinary *uncorrected* finite-sample Gini coefficient, and \(T_{n,k}\) is the share held by the largest \(k\) observations. With \(H_m=\sum_{r=1}^m1/r\), their exact covariance for all these sample sizes and ranks is
\[
\boxed{\operatorname{Cov}(G_n,T_{n,k})=
\frac{k\bigl[(n+1)(H_n-H_k)-(n-k)\bigr]}{2n^2(n+1)}.}
\]
It is strictly positive when \(1\le k<n\), and zero for \(k=n\). Define
\[
\boxed{k_n=\min\bigl\{1\le k<n:(n+1)(H_n-H_k)\le2(n-k)\bigr\}.}
\]
The first maximum of \(k\mapsto\operatorname{Cov}(G_n,T_{n,k})\) occurs **exactly at** \(k_n\); this maximizer is unique unless equality holds in the defining threshold, in which case precisely \(k_n\) and \(k_n+1\) are tied. Furthermore,
\[
\boxed{\frac{k_n}{n}\longrightarrow\alpha_*=-\tfrac12W_0(-2e^{-2})=0.2031878699\ldots,}
\]
where \(W_0\) denotes the real principal Lambert-function branch. At the maximum,
\[
\boxed{\lim_{n\to\infty}n\max_{1\le k\le n}\operatorname{Cov}(G_n,T_{n,k})=
\frac{\alpha_*(1-\alpha_*)}{2}=0.0809512797\ldots.}
\]
This is an optimization of *covariance*, not of correlation or prediction error.

## Assumptions and scope
All observations are independent and identically distributed, strictly positive exponential variables with an arbitrary common rate. The event of a tie among observations has probability zero. The finite-sample Gini normalization is explicit above; multiplying it by \(n/(n-1)\), as in some goodness-of-fit tests, multiplies every covariance by that same positive factor but does not change \(k_n\). The conclusion is finite-sample exact for each integer \(n\ge2\) and each \(1\le k\le n\). No analogous universality for nonexponential parent laws is claimed.

## Proof
**Independent exponential spacings.** Set \(X_{(0)}=0\) and
\[
Y_j=(n-j+1)(X_{(j)}-X_{(j-1)}),\qquad 1\le j\le n.
\]
The \(Y_j\) are independent and identically exponentially distributed with rate \(\lambda\). This follows successively from the memoryless property: at each order-statistic arrival there are \(n-j+1\) residual exponential clocks. If \(S=\sum_{i=1}^nX_i\), telescoping gives \(S=\sum_jY_j\). Thus \(Z_j=Y_j/S\) together form a \(\operatorname{Dirichlet}(1,\ldots,1)\) vector, independent of \(S\), and
\[
\mathbb EZ_j=\frac1n,\qquad
\operatorname{Cov}(Z_i,Z_j)=\frac{n\mathbf1_{\{i=j\}}-1}{n^2(n+1)}.
\]

**Linear representations.** Write the Gini numerator as \(\sum_{j=1}^n(2j-n-1)X_{(j)}\). The coefficient of the spacing \(X_{(\ell)}-X_{(\ell-1)}\) is \((\ell-1)(n-\ell+1)\). Consequently,
\[
G_n=\sum_{j=1}^n a_jZ_j,\quad a_j=\frac{j-1}{n},\qquad
T_{n,k}=\sum_{j=1}^n b_jZ_j,\quad
b_j=\min\left\{1,\frac{k}{n-j+1}\right\}.
\]
The second identity counts how many of the \(k\) largest order statistics contain a given spacing.

**Exact covariance.** Let \(h=H_n-H_k\). Reversing the summation index gives the elementary finite sums
\[
\sum_j a_j=\frac{n-1}{2},\quad
\sum_j b_j=k(1+h),\quad
\sum_j a_jb_j=\frac{k(k-1)}{2n}+kh.
\]
The Dirichlet covariance identity then yields
\[
\operatorname{Cov}(G_n,T_{n,k})=
\frac{n\sum_j a_jb_j-(\sum_ja_j)(\sum_jb_j)}{n^2(n+1)}
=\frac{k[(n+1)h-(n-k)]}{2n^2(n+1)}.
\]
For \(k<n\), the coefficient sequence \((a_j)\) is strictly increasing and \((b_j)\) is nondecreasing and nonconstant. The strict rearrangement inequality makes the numerator \(n\sum a_jb_j-(\sum a_j)(\sum b_j)\) positive. For \(k=n\), \(T_{n,n}=1\) identically.

**Finite-sample maximizer.** Write \(C_{n,k}=\operatorname{Cov}(G_n,T_{n,k})\). Directly subtracting the preceding formula shows
\[
2n^2(n+1)(C_{n,k+1}-C_{n,k})
=\Delta_{n,k}:=(n+1)(H_n-H_k)-2(n-k),\quad1\le k<n.
\]
Furthermore,
\[
\Delta_{n,k+1}-\Delta_{n,k}=2-\frac{n+1}{k+1}.
\]
Thus \(\Delta_{n,k}\) decreases strictly while \(k<(n-1)/2\). On the remaining range,
\[
H_n-H_k=\sum_{r=k+1}^n\frac1r\le\frac{n-k}{k+1}
\quad\Longrightarrow\quad
\Delta_{n,k}\le(n-k)\left(\frac{n+1}{k+1}-2\right)\le0.
\]
The sequence of differences can therefore change sign at most once, from positive to nonpositive, and cannot revert to positive. Since \(\Delta_{n,n-1}<0\), the threshold set is nonempty. By its definition \(k_n\) is the first rank attaining the maximum; an equality at the threshold creates exactly one adjacent tie, and otherwise the maximum is unique. This includes the boundary case \(n=2\).

**Asymptotic optimum.** For each fixed \(s\in(0,1)\) and integers \(k/n\to s\), harmonic sums give
\[
\frac{\Delta_{n,k}}n\longrightarrow -\log s-2(1-s),\qquad
nC_{n,k}\longrightarrow \frac{s}{2}[-\log s-(1-s)].
\]
The first limiting function has exactly one zero in \((0,1)\), namely \(\alpha_*\in(0,1/2)\), besides the excluded endpoint \(s=1\). This follows because its derivative is \(2-1/s\), negative up to \(1/2\) and positive thereafter, while its values at \(0^+\) and \(1/2\) have opposite signs. Bracketing the first finite-sample sign-change between any two fixed fractions on opposite sides of \(\alpha_*\) proves \(k_n/n\to\alpha_*\). The equation \(-\log\alpha_*=2(1-\alpha_*)\) is equivalent to \((-2\alpha_*)e^{-2\alpha_*}=-2e^{-2}\), giving the principal-branch Lambert formula. Substituting it into the limiting covariance gives the asserted limit.

As additional normalization checks, the same Dirichlet representation gives \(\mathbb E G_n=(n-1)/(2n)\), \(\mathbb E T_{n,k}=k(1+H_n-H_k)/n\), and \(\operatorname{Var}(G_n)=(n-1)/(12n^2)\).

## Verification
The accompanying standalone script `verify.py` requires only the Python standard library. It calculates the harmonic formula with exact rational arithmetic and independently computes the same covariance from two finite coefficient arrays and Dirichlet second moments. For all \(2\le n\le150\), it checks every admissible \(k\), strict positivity, the complete sign-change rule, and the maximizing set: **11,324 exact-rational identity checks**. Independent raw-order-statistic simulations cover five distinct sample-size/rank combinations, with 40,000 fixed-seed repetitions each, and separately check both statistics against their normalized-spacing forms. Additional larger-rank calculations check convergence towards the fractional optimum. The script prints `VERIFY_OK` only if all checks succeed. These finite verifications are not an exhaustive computational proof; the preceding analytic argument covers all \(n\) and \(k\).

## Relationship to prior work
Gail and Gastwirth (1978) develop a scale-free Gini test for exponentiality, and separately a sample-Lorenz-curve test, including marginal and asymptotic results. Drăgulescu and Yakovenko (2000) derive the population exponential Lorenz curve and population Gini coefficient. Martínez-Camblor and Corral (2009) treat the distribution of a Gini statistic under uniform observations. Alvaredo (2010) discusses deterministic relationships between top-income shares and the Gini coefficient. Chandra and Singpurwalla (1981) link Lorenz/Gini functionals to reliability total-time-on-test transforms. These connections establish the naturality of the two sampled quantities and nearby tools but do not, in the material inspected, state the all-rank finite-sample mixed covariance or classify the rank of its maximum. A published joint generating-function or Lorenz-process identity might still yield the result indirectly; a literature search is not proof of historical novelty.

## Limitations
No claim is made for arbitrary iid positive distributions, exchangeable dependent incomes, heavy-tailed models, or optimizers of correlation in place of covariance. The Gini convention and finite-sample ranking are integral to the numerical formula. The proof is self-contained apart from the elementary exponential-spacing and Dirichlet moment facts, both stated above. Some relevant original papers could be inspected only at abstract or landing-page level, so indirect prior coverage remains possible. No independent mathematical audit has been conducted.

## References
1. M. H. Gail and J. L. Gastwirth, “A Scale-Free Goodness-Of-Fit Test for the Exponential Distribution Based on the Gini Statistic,” *Journal of the Royal Statistical Society, Series B* 40 (1978), 350–357. DOI: `10.1111/j.2517-6161.1978.tb01048.x`.
2. M. H. Gail and J. L. Gastwirth, “A Scale-Free Goodness-of-Fit Test for the Exponential Distribution Based on the Lorenz Curve,” *Journal of the American Statistical Association* 73 (1978), 787–793. DOI: `10.1080/01621459.1978.10480100`.
3. A. Drăgulescu and V. M. Yakovenko, “Evidence for the exponential distribution of income in the USA,” arXiv:`cond-mat/0008305`, first posted 21 August 2000. DOI (journal): `10.1007/PL00011112`.
4. P. Martínez-Camblor and N. Corral, “About the exact and asymptotic distribution of the Gini coefficient,” *Revista de Matemática: Teoría y Aplicaciones* 16(2) (2009), 199–204. Open-access text: `https://dialnet.unirioja.es/descarga/articulo/7146156.pdf`.
5. F. Alvaredo, “A Note on the Relationship between Top Income Shares and the Gini Coefficient,” CEPR Discussion Paper DP8071, first published 23 October 2010. `https://cepr.org/publications/dp8071`.
6. M. Chandra and N. D. Singpurwalla, “Relationships Between Some Notions Which are Common to Reliability Theory and Economics,” *Mathematics of Operations Research* 6(1) (1981), 113–121. DOI: `10.1287/moor.6.1.113`.
