# Gaussian-pillow fluctuations and exact covariance spectrum of random discrete copulas

## Finding

For the uniform-simplex mixture of **all permutation copulas** introduced in *Random discrete copulas*, the centered checkerboard extension has a nondegenerate functional Gaussian limit at the factorial fluctuation scale. Precisely, for every integer \(k\ge 2\), put \(m=k!\), let \(W=(W_\pi:\pi\in S_k)\) have the \(\mathrm{Dirichlet}(1,\ldots,1)\) law, and let \(\widehat C_\pi\) denote the checkerboard copula induced by the permutation \(\pi\). Define
\[
\widehat Y_k(s,t)=\sum_{\pi\in S_k}W_\pi\widehat C_\pi(s,t),\qquad
G_k(s,t)=\sqrt{(k!+1)(k-1)}\,\bigl(\widehat Y_k(s,t)-st\bigr).
\]
Then, as \(k\to\infty\),
\[
G_k\ \Longrightarrow\ G \quad\text{in }\bigl(C([0,1]^2),\|\cdot\|_\infty\bigr),
\]
where \(G\) is a continuous centered Gaussian field, zero on the boundary, with the **Brownian-pillow covariance**
\[
\operatorname{Cov}\bigl(G(s,t),G(u,v)\bigr)
=\bigl(\min(s,u)-su\bigr)\bigl(\min(t,v)-tv\bigr).
\]
The normalization is exact, not only asymptotic: the finite-mesh covariance separates as a product of explicit one-dimensional kernels. Its interior-grid covariance matrix has an explicit two-dimensional discrete-sine spectrum. Furthermore, the unscaled checkerboard fields converge uniformly to independence almost surely under every joint coupling of their individual laws.

## Assumptions and scope

All parameters and limits in this section concern **this particular uniform Dirichlet mixture**, not uniform Lebesgue measure on the Birkhoff polytope and not one randomly chosen permutation.

For every \(k\ge2\), each permutation \(\pi\) of \(\{1,\ldots,k\}\) places probability \(1/k\) uniformly in each square \(((r-1)/k,r/k]\times((\pi(r)-1)/k,\pi(r)/k]\), for \(1\le r\le k\). The resulting copula is \(\widehat C_\pi\). It is bilinear on mesh cells. The vector of \(k!\) mixture weights is uniform on the simplex, independently for any given \(k\); **no independence between different mesh sizes is needed** for the almost-sure conclusion.

Set
\[
A_{k,r}(x)=\max\{0,\min\{1,kx-r+1\}\},\qquad
K_k(x,y)=\frac1k\sum_{r=1}^k(A_{k,r}(x)-x)(A_{k,r}(y)-y).
\]
The exact identity for all \(s,t,u,v\in[0,1]\) is
\[
\operatorname{Cov}\bigl(\widehat Y_k(s,t),\widehat Y_k(u,v)\bigr)
=\frac{K_k(s,u)K_k(t,v)}{(k!+1)(k-1)},
\qquad \mathbb E\widehat Y_k(s,t)=st.
\]
Writing \(B(x,y)=\min(x,y)-xy\), the one-dimensional kernel satisfies the sharp uniform discrepancy bound
\[
0\le B(x,y)-K_k(x,y)\le\frac{1}{4k}.
\]
Consequently, the covariance of \(G_k\) converges uniformly to the stated Gaussian covariance.

At the interior grid points \(i/k\), \(1\le i\le k-1\), let \(M^{(k)}_{ij}=B(i/k,j/k)\). The covariance matrix of the vector of values of \(G_k\) on the interior grid is \(M^{(k)}\otimes M^{(k)}\). Its eigenvectors are the products of discrete sine vectors and its \((r,q)\)-eigenvalues, for \(1\le r,q\le k-1\), are exactly
\[
\Lambda_{r,q}^{(k)}=
\frac{1}{16k^2\sin^2(\pi r/(2k))\sin^2(\pi q/(2k))}.
\]
The unnormalized \(\widehat Y_k\) covariance eigenvalues are these values divided by \((k!+1)(k-1)\). For each fixed positive \(r,q\), \(\Lambda_{r,q}^{(k)}\to(\pi^4r^2q^2)^{-1}\), the eigenvalues of the limiting integral covariance operator on the square.

## Proof

**Step 1: exact covariance of the permutation checkerboards.** With \(a_r=A_{k,r}(s)\), and analogously for other arguments, the checkerboard copula is
\[
\widehat C_\pi(s,t)=\frac1k\sum_{r=1}^k A_{k,r}(s) A_{k,\pi(r)}(t),
\qquad \sum_{r=1}^k A_{k,r}(x)=kx.
\]
For a uniform random permutation \(\pi\), the finite-population covariance formula gives
\[
\operatorname{Cov}_\pi\!\left(\sum_ra_r b_{\pi(r)},\sum_ra'_r b'_{\pi(r)}\right)
=\frac{\sum_r(a_r-\overline a)(a'_r-\overline a')\,\sum_j(b_j-\overline b)(b'_j-\overline b')}{k-1}.
\]
Indeed, for the two permuted coordinates, the same-label covariance is the finite-population covariance with denominator \(k\), whereas distinct labels have its negative divided by \(k-1\); summing yields the display. Dividing by \(k^2\) proves
\[
\operatorname{Cov}_\pi\bigl(\widehat C_\pi(s,t),\widehat C_\pi(u,v)\bigr)
=\frac{K_k(s,u)K_k(t,v)}{k-1},\qquad
\mathbb E_\pi\widehat C_\pi(s,t)=st.
\]
For a Dirichlet vector of \(m\) unit parameters, \(\operatorname{Cov}(\sum W_i f_i,\sum W_i g_i)=(m+1)^{-1}\operatorname{Cov}_{I}(f_I,g_I)\), where \(I\) is uniform on its \(m\) indices. Applying this identity proves the exact covariance of \(\widehat Y_k\) and \(G_k\).

**Step 2: uniform limit of the one-dimensional kernel.** Write \(x=(j-1+a)/k\) for a point in the \(j\)-th cell, with \(0\le a\le1\). The functions \(A_{k,r}(x)\) are the distribution functions of independent uniform locations conditional on membership in the corresponding cells. If \(U\) is uniform on \([0,1]\), let \(J\) be its cell label. The law-of-total-covariance identity for the indicators \(\mathbf1\{U\le x\}\) and \(\mathbf1\{U\le y\}\) gives
\[
B(x,y)=K_k(x,y)+\frac1k\mathbf1\{x,y\text{ lie in the same cell}\}\bigl(\min(a,b)-ab\bigr),
\]
where \(a,b\) are their within-cell fractions. The discrepancy is nonnegative and at most \(1/(4k)\), proving uniform kernel convergence.

**Step 3: exponential representation and finite-dimensional central limit theorem.** Enumerate permutations in any deterministic order and take independent unit-rate exponentials \(E_\pi\). Put \(S_m=\sum_\pi E_\pi\) and \(W_\pi=E_\pi/S_m\). Define the deterministic centered functions
\[
h_{k,\pi}(s,t)=\sqrt{k-1}\bigl(\widehat C_\pi(s,t)-st\bigr),
\quad
T_k=\frac1{\sqrt m}\sum_\pi(E_\pi-1)h_{k,\pi}.
\]
As \(\sum_\pi h_{k,\pi}=0\), the exact relation is
\[
G_k=\frac{\sqrt{m(m+1)}}{S_m}\,T_k.
\]
Since \(S_m/m\to1\) in probability, the scalar multiplier converges in probability to \(1\). For finitely many evaluation points and any fixed linear combination, the summands of \(T_k\) are independent, centered, and their variance converges by Step 1 to the corresponding linear combination of \(B\otimes B\). The absolute values of \(h_{k,\pi}\) are at most \(\sqrt{k-1}\); because exponentials have a finite third centered absolute moment, the Lyapunov third-moment bound is
\[
O\!\left(\frac{k^{3/2}}{\sqrt{k!}}\right)=o(1).
\]
Thus every finite-dimensional distribution of \(T_k\) converges to the centered Gaussian distribution with covariance \(B\otimes B\). A zero limiting variance is handled directly by convergence in second moment. Cramér–Wold covers joint distributions.

**Step 4: functional tightness, including the boundary.** Take two points \(z=(s,t)\), \(w=(u,v)\), and \(D=|s-u|+|t-v|\). Every copula and the product copula are 1-Lipschitz in each argument, so
\[
|h_{k,\pi}(z)-h_{k,\pi}(w)|\le 2\sqrt{k}\,D.
\]
Also, since \(A_{k,r}\) are monotone and each pointwise increment lies between zero and one,
\[
K_k(s,s)+K_k(u,u)-2K_k(s,u)
=\frac1k\sum_r\bigl(A_{k,r}(s)-A_{k,r}(u)-(s-u)\bigr)^2
\le |s-u|.
\]
Apply the Step 1 covariance formula to the horizontal difference at fixed \(t\), noting \(K_k(t,t)\le1/4\); do the same for the vertical difference and use \((a+b)^2\le2a^2+2b^2\). This yields the averaged squared increment bound
\[
\frac1m\sum_\pi |h_{k,\pi}(z)-h_{k,\pi}(w)|^2\le \tfrac12D.
\]
Rosenthal's inequality at exponent \(8\), with the independent centered exponentials, now implies
\[
\mathbb E|T_k(z)-T_k(w)|^8
\le c\left[D^4+\frac{k^4}{(k!)^3}D^8\right]
\le C D^4,
\]
for numerical constants independent of \(k,z,w\), because \(D\le2\) and \(\sup_{k\ge2} k^4/(k!)^3<\infty\). We also have \(T_k(0,0)=0\), and its trajectories are continuous. The two-parameter Kolmogorov–Chentsov tightness criterion, using \(4>2\), makes \((T_k)\) tight in \(C([0,1]^2)\). The Gaussian finite-dimensional limits identify its unique weak limit as the continuous Brownian pillow. Slutsky's theorem for a scalar multiplier gives the asserted **functional** weak convergence of \(G_k\).

**Step 5: exact interior-grid eigenvalues.** On the grid, \(A_{k,r}(i/k)=\mathbf1\{r\le i\}\), so \(K_k(i/k,j/k)=B(i/k,j/k)\). The inverse of the \((k-1)\times(k-1)\) matrix \(M^{(k)}\) is \(k\) times the tridiagonal Dirichlet matrix with diagonal \(2\) and off-diagonal \(-1\). Its eigenvectors are \(\bigl(\sin(\pi r i/k)\bigr)_{i=1}^{k-1}\), with inverse eigenvalues \(4k\sin^2(\pi r/(2k))\). Tensoring the two one-dimensional eigensystems proves the exact spectral formula and its fixed-mode limit.

**Step 6: uniform almost-sure collapse without inter-mesh independence.** Since \(\widehat Y_k-st\) is bilinear within each grid cell, its absolute maximum occurs at grid vertices. By the exact variance formula, Chebyshev's inequality, and a union bound over \((k-1)^2\) interior vertices,
\[
\mathbb P\!\left(\|\widehat Y_k-\Pi\|_\infty>\varepsilon\right)
\le \frac{k-1}{16(k!+1)\varepsilon^2},
\quad\Pi(s,t)=st.
\]
The upper bounds are summable, so the first Borel–Cantelli lemma implies \(\|\widehat Y_k-\Pi\|_\infty\to0\) almost surely under any joint coupling of the marginal laws.

## Verification

The accompanying standard-library script `checker.py` enumerates every permutation for mesh sizes \(2\le k\le6\), checks the cross-point covariance formula on 245 ordered point pairs to floating tolerance, and tests the \(1/(4k)\) kernel error bound. It separately checks 204 discrete-sine eigenvector/eigenvalue identities for \(2\le k\le9\). For \(k=4,5,6\), a reproducibly seeded Dirichlet simulation cross-checks the normalized variance and approximate fourth standardized moment. Run with `python checker.py` from a directory containing the embedded source file. All assertions passed in the recorded execution.

These finite calculations are **not** the infinite-dimensional proof; Steps 1–6 provide the analytic proof. No external numerical library, external data, or inaccessible auxiliary file is needed.

## Relationship to prior work

Kokol Bukovšek, Mojškerc, and Stopar (2026), *Random discrete copulas*, define the simplex-weighted mixture and its bilinear extension. Their Lemma 4.2 establishes covariance reduction to the uniformly selected permutation model **at grid points** and Theorem 4.3 establishes the pointwise grid variance. Their discussion of checkerboard extensions obtains pointwise quantities. Their concluding remarks identify convergence with increasing mesh size as a direction for future work. The exact full continuous covariance kernel, its finite sine eigenspectrum, the factorially rescaled functional Gaussian limit, and the almost-sure sup-norm convergence are not stated in the examined full text; the covariance reduction lemma is **used as compatible prior input** and is not claimed as new.

General quantitative Dirichlet-process central limit theorems, such as Torrisi (2023), supply related Gaussian approximation machinery for finite-dimensional Dirichlet-functionals. Exchangeably weighted empirical-process results provide broader methodological precedents, but their applicability to this triangular family with \(k!\) prescribed deterministic permutation-copula functions, its exact normalization, and the square-indexed functional topology requires additional verification; no exclusivity or blanket priority claim is made. The uniform-Lebesgue Birkhoff-polytope random-matrix model differs from the image of the uniform permutation-weight simplex.

## Limitations

The weak convergence concerns the Dirichlet\((1,\ldots,1)\) mixture over all \(k!\) permutations; it is not a theorem for arbitrary simplex-weight distributions, independently sampled permutations, or a uniform random point in the Birkhoff polytope. Functional convergence is in the topology of uniform convergence in distribution; it does **not** assert an almost-sure coupling of the normalized Gaussian fluctuations. The separate almost-sure statement is only for the unscaled fields and allows arbitrary inter-mesh dependence. The limiting covariance gives no nonasymptotic Gaussian approximation rate. The finite spectrum is for interior grid evaluations, not for all off-grid values. Priority remains subject to independent scholarly verification, particularly against general exchangeably weighted empirical-process theory.

## References

1. D. Kokol Bukovšek, B. Mojškerc and N. Stopar, *Random discrete copulas*, arXiv:2603.13953, first publicly submitted 14 March 2026; full HTML: https://arxiv.org/html/2603.13953v3 (Definitions 4.1 and 5.1, Lemma 4.2, Theorems 4.3 and 5.3, concluding remarks).
2. G. L. Torrisi, *Quantitative Multidimensional Central Limit Theorems for Means of the Dirichlet-Ferguson Measure*, ALEA 20 (2023), lawful open article: https://alea.impa.br/articles/v20/20-30.pdf.
3. J. Præstgaard and J. A. Wellner, *Exchangeably Weighted Bootstraps of the General Empirical Process*, Annals of Probability 21 (1993), pp. 2053–2086 (general empirical-process context; only abstract-level comparison here).
4. S. Chatterjee, P. Diaconis and A. Sly, *Properties of Uniform Doubly Stochastic Matrices*, arXiv:1010.6136 (different uniform-Birkhoff law).
