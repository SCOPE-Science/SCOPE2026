# Gaussian-pillow fluctuations and covariance spectrum of random discrete copulas

## Finding

Let \(k\ge2\), \(m=k!\), and let \((W_\pi)_{\pi\in S_k}\) have the uniform \(\mathrm{Dirichlet}(1,\ldots,1)\) distribution. For the checkerboard permutation copula \(\widehat C_\pi\), define
\[
\widehat Y_k(s,t)=\sum_{\pi\in S_k}W_\pi\widehat C_\pi(s,t),\qquad
G_k(s,t)=\sqrt{(k!+1)(k-1)}\,[\widehat Y_k(s,t)-st].
\]
Then \(G_k\) converges in distribution in \(C([0,1]^2)\), equipped with the uniform norm, to the centered continuous Gaussian field with covariance
\[
\operatorname{Cov}(G(s,t),G(u,v))=B(s,u)B(t,v),\qquad
B(x,y)=\min(x,y)-xy.
\]
This is the Brownian pillow. The mean \(\mathbb E\widehat Y_k(s,t)=st\) and the complete *finite-\(k\)* covariance kernel are exactly
\[
\operatorname{Cov}(\widehat Y_k(s,t),\widehat Y_k(u,v))
 =\frac{K_k(s,u)K_k(t,v)}{(k!+1)(k-1)},
\]
where, for \(1\le r\le k\),
\[
 A_{k,r}(x)=\max\{0,\min\{1,kx-r+1\}\},\quad
 K_k(x,y)=\frac1k\sum_{r=1}^k(A_{k,r}(x)-x)(A_{k,r}(y)-y).
\]
The uniform bound \(0\le B-K_k\le1/(4k)\) holds pointwise. At the interior grid points \((i/k,j/k)\), \(1\le i,j\le k-1\), the covariance matrix of \(G_k\) is \(M^{(k)}\otimes M^{(k)}\), with \(M^{(k)}_{ij}=B(i/k,j/k)\). Its exact eigenvectors are products of discrete sine vectors, and its eigenvalues are
\[
\Lambda_{r,q}^{(k)}=\frac{1}{16k^2\sin^2(\pi r/(2k))\sin^2(\pi q/(2k))},\qquad 1\le r,q\le k-1.
\]
**Mesh-area normalization is essential** when comparing this discrete covariance matrix to the limiting integral covariance operator: for fixed positive \(r,q\),
\[
\frac{\Lambda_{r,q}^{(k)}}{k^2}\longrightarrow\frac1{\pi^4r^2q^2},\qquad
\Lambda_{r,q}^{(k)}\sim\frac{k^2}{\pi^4r^2q^2}.
\]
Thus the raw eigenvalues do *not* approach finite limits; they diverge quadratically. The eigenvalues of the matrix representing the integral operator by a two-dimensional Riemann sum are \(\Lambda_{r,q}^{(k)}/k^2\). The unnormalized \(\widehat Y_k\) grid-covariance eigenvalues are \(\Lambda_{r,q}^{(k)}/[(k!+1)(k-1)]\). Finally,
\[\|\widehat Y_k-st\|_\infty\longrightarrow0\quad\text{almost surely}\]
for **every joint coupling** of the individual laws across mesh sizes, without independence between different \(k\).

## Assumptions and scope

The random law is the image of the *uniform simplex* on all \(k!\) permutations; it is neither one uniformly sampled permutation nor Lebesgue-uniform measure on the Birkhoff polytope. Permutation \(\pi\) places probability \(1/k\) uniformly in each square \(((r-1)/k,r/k]\times((\pi(r)-1)/k,\pi(r)/k]\), \(1\le r\le k\). Its checkerboard distribution function \(\widehat C_\pi\) is bilinear on cells, continuous, and a copula. The Gaussian convergence is weak convergence in the space of continuous fields, not an almost-sure Gaussian fluctuation coupling. The matrix eigenvalues concern *interior grid samples*, while the integral covariance operator uses two-dimensional Lebesgue measure; the corrected comparison therefore includes the \(k^{-2}\) mesh-area factor. All formulae apply for every integer \(k\ge2\).

## Proof

### 1. Exact centered covariance

Write \(a_r(x)=A_{k,r}(x)\). Then
\[
\widehat C_\pi(s,t)=k^{-1}\sum_{r=1}^k a_r(s)a_{\pi(r)}(t),\qquad
\sum_{r=1}^ka_r(x)=kx.
\]
For uniform \(\pi\), \(\mathbb E\widehat C_\pi(s,t)=st\). For deterministic sequences \(a,a',b,b'\), direct expansion of the diagonal and off-diagonal permutation indicators yields
\[
\operatorname{Cov}_{\pi}\left(\sum_ra_rb_{\pi(r)},\sum_ra'_rb'_{\pi(r)}\right)
=\frac{\left[\sum_r(a_r-\bar a)(a'_r-\bar a')\right]
\left[\sum_j(b_j-\bar b)(b'_j-\bar b')\right]}{k-1}.
\]
The factor \(k^{-2}\) for the two copula evaluations therefore gives \(\operatorname{Cov}_\pi(\widehat C_\pi(s,t),\widehat C_\pi(u,v))=K_k(s,u)K_k(t,v)/(k-1)\). A uniform \(m\)-component Dirichlet vector has \(\operatorname{Cov}(\sum_iW_if_i,\sum_iW_ig_i)=(m+1)^{-1}\operatorname{Cov}_{I}(f_I,g_I)\) for a uniform index \(I\). Applying this to the \(k!\) copulas proves both the exact formula and \(\operatorname{Cov}(G_k(s,t),G_k(u,v))=K_k(s,u)K_k(t,v)\).

### 2. Uniform kernel convergence

Let \(U\) be uniform on \([0,1]\) and let \(J\) label its one of \(k\) equal cells. Then \(a_J(x)=\mathbb P(U\le x\mid J)\). Total covariance of \(\mathbf1_{\{U\le x\}}\) and \(\mathbf1_{\{U\le y\}}\) gives \(B(x,y)=K_k(x,y)+\mathbb E[\operatorname{Cov}(\mathbf1_{\{U\le x\}},\mathbf1_{\{U\le y\}}\mid J)]\). The conditional covariance vanishes unless \(x,y\) belong to the same cell; when they do, writing their within-cell fractions as \(a,b\in[0,1]\), it is \(k^{-1}(\min(a,b)-ab)\). Hence \(0\le B-K_k\le1/(4k)\), uniformly, including cell boundaries.

### 3. Finite-dimensional Gaussian convergence

Enumerate permutations in a deterministic order and take independent standard exponential variables \(E_\pi\). Let \(S_m=\sum_\pi E_\pi\) and \(W_\pi=E_\pi/S_m\). Define deterministic centered functions
\[
h_{k,\pi}(s,t)=\sqrt{k-1}\,[\widehat C_\pi(s,t)-st],\qquad
T_k=m^{-1/2}\sum_\pi(E_\pi-1)h_{k,\pi}.
\]
Since \(\sum_\pi h_{k,\pi}=0\),
\[G_k=\frac{\sqrt{m(m+1)}}{S_m}T_k.\]
Chebyshev's inequality gives \(S_m/m\to1\) in probability. The empirical covariance of the deterministic \(h_{k,\pi}\) functions is exactly \(K_k\otimes K_k\), which converges uniformly to \(B\otimes B\) by Step 2. At any finite collection of evaluation points, every fixed linear combination of the triangular-array summands for \(T_k\) has variance tending to the asserted limit, and each \(|h_{k,\pi}|\le\sqrt{k-1}\). Exponential variables have a finite third absolute centered moment; Lyapunov's ratio is bounded by a constant times \(k^{3/2}/\sqrt{k!}\to0\). Cramér–Wold gives joint Gaussian finite-dimensional limits (a vanishing limiting variance is handled by the second moment).

### 4. Uniform functional tightness

For \(z=(s,t)\), \(w=(u,v)\), let \(D=|s-u|+|t-v|\). Every copula is 1-Lipschitz in each variable, so \(|h_{k,\pi}(z)-h_{k,\pi}(w)|\le2\sqrt kD\). Monotonicity of the cell CDF functions and \(0\le a_r\le1\) give
\[
K_k(s,s)+K_k(u,u)-2K_k(s,u)
=k^{-1}\sum_r[a_r(s)-a_r(u)-(s-u)]^2\le|s-u|.
\]
Combine the horizontal and vertical difference bounds with \(K_k(t,t)\le1/4\) and \((x+y)^2\le2(x^2+y^2)\). This yields \(m^{-1}\sum_\pi|h_{k,\pi}(z)-h_{k,\pi}(w)|^2\le D/2\). Rosenthal's eighth-moment bound for the independent centered \((E_\pi-1)h_{k,\pi}\) terms then yields, uniformly in \(k\ge2\),
\[
\mathbb E|T_k(z)-T_k(w)|^8
\le C\left[D^4+\frac{k^4}{(k!)^3}D^8\right]\le C'D^4,
\]
using \(D\le2\) and \(\sup_{k\ge2}k^4/(k!)^3<\infty\). As \(T_k(0,0)=0\) and the paths are continuous, the two-parameter Kolmogorov–Chentsov criterion, with exponent \(4>2\), proves tightness in \(C([0,1]^2)\). Finite-dimensional convergence identifies the Brownian pillow as the unique weak limit of \(T_k\); the scalar normalization in Step 3 converges to one, so Slutsky proves the asserted functional weak convergence of \(G_k\).

### 5. Exact grid spectrum, including the necessary mesh factor

At every interior grid point \(i/k\), \(a_r(i/k)=\mathbf1_{\{r\le i\}}\), hence \(K_k(i/k,j/k)=B(i/k,j/k)\). The inverse of \(M^{(k)}=[B(i/k,j/k)]_{i,j=1}^{k-1}\) is \(k\) times the tridiagonal Dirichlet Laplacian with diagonal 2 and super/subdiagonal \(-1\). Its eigenvectors are \((\sin(\pi r i/k))_{i=1}^{k-1}\), and its eigenvalues are \([4k\sin^2(\pi r/(2k))]^{-1}\). Tensoring the one-dimensional eigensystems establishes the exact two-dimensional formula for \(\Lambda_{r,q}^{(k)}\). For fixed \(r,q\), \(\sin(\pi r/(2k))\sim\pi r/(2k)\) implies \(\Lambda_{r,q}^{(k)}\sim k^2/(\pi^4r^2q^2)\). The limiting *integral* covariance operator is represented at grid spacing \(1/k\) by the matrix \(k^{-2}(M^{(k)}\otimes M^{(k)})\); consequently its eigenvalues approach \((\pi^4r^2q^2)^{-1}\) only **after** multiplying raw grid eigenvalues by \(k^{-2}\). This also directly shows why the unscaled fixed-mode convergence assertion would be false.

### 6. Almost-sure unscaled convergence for every coupling

Both \(\widehat Y_k\) and \(\Pi(s,t)=st\) are bilinear in each mesh cell, so the maximum of \(|\widehat Y_k-\Pi|\) occurs at grid vertices. At each interior grid vertex, the covariance identity gives \(\operatorname{Var}(\widehat Y_k-\Pi)\le1/[16(k!+1)(k-1)]\). A union bound and Chebyshev over the \((k-1)^2\) interior vertices therefore yield
\[
\mathbb P\{\|\widehat Y_k-\Pi\|_\infty>\varepsilon\}
\le\frac{k-1}{16(k!+1)\varepsilon^2}.
\]
These probabilities sum to a finite value over \(k\). The first Borel–Cantelli lemma proves almost-sure uniform convergence under *any* coupling of the prescribed \(k\)-wise laws, without independence between \(k\).

## Verification and limits

The unchanged standard-library script `checker.py` checks exact permutation covariance for \(k=2,\ldots,6\), bounded kernel discrepancy, discrete sine matrix eigenrelations through \(k=9\), and selected Dirichlet simulations. Independent rational calculations for \(k=3,4,5\) confirm grid covariance, while numerical fixed-mode values at \(k=4,8,16,32,64\) confirm \(\Lambda_{1,1}^{(k)}/k^2\to\pi^{-4}\) and \(\Lambda_{1,1}^{(k)}\to\infty\). These checks support exact identities and expose the scale correction; Steps 1–6, not experiments, prove the infinite-dimensional statements. No rate of convergence of the Gaussian law, off-grid matrix spectrum, or alternative distribution on the Birkhoff polytope is asserted.

## Relationship to prior literature

Kokol Bukovšek, Mojškerc and Stopar, *Random discrete copulas* (arXiv:2603.13953v3, 2026), define the simplex-weighted model and its bilinear extension. Their Lemma 4.2 supplies the compatible grid-point covariance reduction and Theorems 4.3 and 5.3 discuss finite pointwise quantities; these are credited rather than asserted as new. The full functional central limit theorem, uniform covariance kernel, explicit finite-mesh sine spectrum, and coupling-independent almost-sure uniform collapse are additional claims. General exchangeably weighted empirical-process and Dirichlet-Ferguson approximation results supply related background, but their exact applicability to this factorial triangular family and continuous two-parameter topology is not established here. Any older equivalent general triangular-array process theorem remains a potential originality antecedent.

## References

1. D. Kokol Bukovšek, B. Mojškerc and N. Stopar, *Random discrete copulas*, arXiv:2603.13953v3 (2026), https://arxiv.org/html/2603.13953v3.
2. G. L. Torrisi, *Quantitative Multidimensional Central Limit Theorems for Means of the Dirichlet-Ferguson Measure*, ALEA 20 (2023), https://alea.impa.br/articles/v20/20-30.pdf.
3. J. Præstgaard and J. A. Wellner, *Exchangeably Weighted Bootstraps of the General Empirical Process*, Annals of Probability 21 (1993), pp. 2053–2086.
4. S. Chatterjee, P. Diaconis and A. Sly, *Properties of Uniform Doubly Stochastic Matrices*, arXiv:1010.6136 (different probability law).
