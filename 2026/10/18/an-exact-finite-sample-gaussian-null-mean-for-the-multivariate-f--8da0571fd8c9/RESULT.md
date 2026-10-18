# An exact finite-sample Gaussian null mean for the multivariate Fourier–Stein normality statistic

## Finding
For every integer \(d\ge2\), every \(n\ge d+1\), and every \(a>0\), the Gaussian-null mean of the affine-invariant Fourier–Stein normality statistic introduced by Ebner, Henze, and Strieder has an explicit formula involving only confluent hypergeometric functions. In particular, no integration over random covariance matrices or simulation is required.

Put \(\alpha=d/2\), \(\beta=(n-1)/2\), and, for \(j\in\{0,1\}\) and \(u\ge0\), define
\[
M_j(u)=\frac{(\alpha)_j}{(\beta)_j}\,{}_1F_1(\alpha+j;\beta+j;-u),
\]
where \((q)_j\) is the rising factorial and \({}_1F_1\) is Kummer's confluent hypergeometric function. Then the exact identity is
\[
\begin{aligned}
\mathbb E_0 T_{n,a}
={}&\frac{nd}{2(a+1)}\left(\frac{\pi}{a+1}\right)^{d/2}\\
&-\frac{2n(n-1)}{2a+1}\left(\frac{2\pi}{2a+1}\right)^{d/2}
M_1\left(\frac{n-1}{4a+2}\right)\\
&+\left(\frac{\pi}{a}\right)^{d/2}\left[
 d+\frac{n-1}{2}\left\{
 dM_0\left(\frac{n}{2a}\right)
 -(n+1)M_1\left(\frac{n}{2a}\right)\right\}\right].
\end{aligned}
\]
Here \(\mathbb E_0\) denotes expectation under any nondegenerate multivariate Gaussian null distribution. At the minimal admissible sample size \(n=d+1\), the entire statistic, not just its expectation, is deterministic; the formula remains valid because \(M_0(u)=M_1(u)=e^{-u}\).

For instance, \(\mathbb E_0[T_{n,a}]\approx1.4582618412279\) for \(n=5\), \(d=2\), and \(a=1\). The corresponding established limiting-null mean is approximately \(1.7671458676443\); the finite-sample correction is therefore substantial at this sample size.

## Assumptions and scope
Let \(X_1,\ldots,X_n\) be independent with common distribution \(N_d(\mu,\Sigma)\), where \(\Sigma\) is positive definite. Set
\[
\overline X=n^{-1}\sum_{i=1}^n X_i,\qquad
S=n^{-1}\sum_{i=1}^n(X_i-\overline X)(X_i-\overline X)^\top,
\qquad Y_i=S^{-1/2}(X_i-\overline X).
\]
For \(t\in\mathbb R^d\), define
\[
\widehat\varphi_n(t)=\frac1n\sum_{i=1}^n e^{\mathrm i t^\top Y_i},
\qquad\varphi_0(t)=e^{-\|t\|^2/2},
\]
and use precisely the statistic
\[
T_{n,a}=n\int_{\mathbb R^d}
\big\|\nabla\widehat\varphi_n(t)+t\varphi_0(t)\big\|_{\mathbb C^d}^2
 e^{-a\|t\|^2}\,dt.
\]
The sample covariance has divisor \(n\), not \(n-1\), and the term multiplied by \(t\) is the **theoretical** characteristic function \(\varphi_0\), not the empirical one. These conventions are essential. No asymptotic limit, growing-dimension approximation, or exact quantile formula is asserted.

## Proof
**1. A single random projection.** Affine invariance reduces the Gaussian null to independent standard normal observations. Center their \(n\times d\) data matrix and take its polar decomposition. The centered-and-whitened matrix has Gram matrix \(nP\), where \(P\) is the orthogonal projection onto a Haar-uniform \(d\)-dimensional subspace of the \((n-1)\)-dimensional space \(\mathbf1^\perp\). This follows from orthogonal invariance of the centered Gaussian data matrix. In particular \(\sum_iY_i=0\), \(\sum_iY_iY_i^\top=nI_d\), and \(\sum_i\|Y_i\|^2=nd\).

For a fixed unit vector \(v\in\mathbf1^\perp\), \(Z=v^\top Pv\) has the \(\operatorname{Beta}(d/2,(n-d-1)/2)\) distribution when \(n>d+1\). Indeed \(Z\) is the ratio of independent chi-square variables with respectively \(d\) and \(n-1-d\) degrees of freedom. For \(n=d+1\) the projection is the identity on \(\mathbf1^\perp\), so \(Z=1\) surely. The displayed \(M_j(u)\) is \(\mathbb E[Z^j e^{-uZ}]\) in both cases: for a beta law, apply its Euler integral and Kummer's integral identity; for the point mass, use \({}_1F_1(q;q;-u)=e^{-u}\).

**2. Diagonal terms.** The centered coordinate vector \(e_i-\mathbf1/n\) has squared length \((n-1)/n\), so
\[
\|Y_i\|^2\stackrel{d}= (n-1)Z,
\quad
\mathbb E_0[\|Y_i\|^2 e^{-\|Y_i\|^2/(4a+2)}]
=(n-1)M_1((n-1)/(4a+2)).
\]

**3. Paired terms.** For distinct \(i,j\), let
\[
v=\frac{e_i-e_j}{\sqrt2},\qquad
w=\frac{e_i+e_j-2\mathbf1/n}{\sqrt{2-4/n}}.
\]
These are orthonormal in \(\mathbf1^\perp\). Put \(Z=v^\top Pv\) and \(Q=w^\top Pw\). Orthogonal invariance of the Haar projection and its fixed trace \(d\) give
\[
\mathbb E[Q\mid Z]=\frac{d-Z}{n-2}.
\]
Moreover, \(\|Y_i-Y_j\|^2=2nZ\), and the parallelogram identity yields
\[
Y_i^\top Y_j=\frac{(n-2)Q-nZ}{2},
\quad
\mathbb E_0[Y_i^\top Y_j\mid Z]=\frac{d-(n+1)Z}{2}.
\]
(The conditional formula also holds at \(n=d+1\), where \(P\) is deterministic.) Therefore
\[
\mathbb E_0\left[Y_i^\top Y_j
 e^{-\|Y_i-Y_j\|^2/(4a)}\right]
=\frac{d M_0(n/(2a))-(n+1) M_1(n/(2a))}{2}.
\]
To justify the conditional trace identity explicitly: after fixing \(v^\top Pv=Z\), rotations of the orthogonal complement of \(v\) preserve the conditional law of \(P\). Every one of the \(n-2\) perpendicular coordinate directions must consequently have equal conditional projected squared length, and their sum is \(\operatorname{tr}P-Z=d-Z\).

**4. Combine the exact statistic.** The original statistic admits the algebraic representation
\[
\begin{aligned}
T_{n,a}={}&\frac{nd}{2(a+1)}\left(\frac\pi{a+1}\right)^{d/2}
-\frac2{2a+1}\left(\frac{2\pi}{2a+1}\right)^{d/2}
\sum_i\|Y_i\|^2 e^{-\|Y_i\|^2/(4a+2)}\\
&+\frac1n\left(\frac\pi a\right)^{d/2}
\sum_{i,j}Y_i^\top Y_j e^{-\|Y_i-Y_j\|^2/(4a)}.
\end{aligned}
\]
This identity follows by expanding the squared Fourier–Stein discrepancy, integrating Gaussian Fourier kernels, and using \(\nabla\varphi_0(t)=-t\varphi_0(t)\); it is also Theorem 2.1 in the cited primary paper. Take expectations, apply Step 2 to the \(n\) single-index terms, Step 3 to the \(n(n-1)\) distinct-index terms, and \(\sum_i\|Y_i\|^2=nd\) to the diagonal of the double sum. The resulting three terms are exactly those in the finding.

**5. Exact smallest-sample boundary.** If \(n=d+1\), the rank-\(d\) projection onto \(\mathbf1^\perp\) is unique, \(P=I-\mathbf1\mathbf1^\top/n\). Hence \(Y_i^\top Y_j=n\mathbf1_{i=j}-1\) deterministically. Every expression in Step 4 is a function of this Gram matrix; thus \(T_{n,a}\) is deterministic. This also proves the boundary statement, independently of special-function evaluation.

## Verification
The standalone `verify.py` directly implements the formula and the original finite-sample statistic. It compares the hypergeometric moments with independently integrated beta moments; tests the deterministic simplex boundary; and checks Gaussian Monte Carlo means for several higher-dimensional parameter triples. A run of the packaged script gave `PASS 101 independent beta-integral, exact-simplex and Monte Carlo comparisons`. For \(n=5\), \(d=2\), \(a=1\), the formula returned \(1.4582618412279\). Numerical finite-sample experiments corroborate, but do not replace, the preceding proof for all admissible parameters. Tests use ordinary double precision; extreme bandwidth and dimension regimes may require higher-precision special-function evaluation.

## Relationship to prior work
Ebner, Henze, and Strieder [1] introduced \(T_{n,a}\) and derived its finite-data representation, Gaussian limiting distribution, and the **mean of the limiting statistic**. Their Theorem 3.3, concerning \(\mathbb ET_{\infty,a}\), is distinct from an exact expression for \(\mathbb E_0T_{n,a}\) at finite \(n\). The paper describes Monte Carlo calibration of finite-sample critical values. The new formula gives an exact finite-sample **first-moment** calibration, not those critical values or the law of the statistic. Dörr, Ebner, and Henze [2] study a different harmonic-oscillator statistic; their null asymptotics do not directly give this first moment. The Haar-projection and beta-marginal inputs are standard facts about Gaussian sample covariance geometry, and the new calculation explicitly combines them with the statistic's pairwise Fourier representation. No unconditional historical-priority assertion is made.

## Limitations
The identity requires an independent Gaussian sample and the exact centering/studentization conventions above. It is a mean, not an exact full null distribution, variance, tail bound, quantile, or independently certified historical novelty result. The analytical formula remains valid for the smallest sample but the statistic there is deterministic and has no discriminatory power; computing stable small differences between its three terms in extreme parameter regimes can demand high precision. The finding does not resolve the spectral-eigenvalue or higher-cumulant questions posed in [1].

## References
[1] B. Ebner, N. Henze, D. Strieder, *Testing normality in any dimension by Fourier methods in a multivariate Stein equation*, arXiv:2007.02596 (first posted July 6, 2020); *Canadian Journal of Statistics* **50** (2022), 992–1033, DOI: 10.1002/cjs.11670. Primary MSC: 62H15.

[2] P. Dörr, B. Ebner, N. Henze, *Testing multivariate normality by zeros of the harmonic oscillator in characteristic function spaces*, *Scandinavian Journal of Statistics* (online June 23, 2020), DOI: 10.1111/sjos.12477.
