# Exact isotropic covariance and a Gaussian radial law for equilateral Lipschitz-free balls

## Finding

For each integer \(n\ge2\), let \(M_n\) be an equilateral metric on \(n\) points, and realize its real Lipschitz-free unit ball canonically as the type-A root polytope
\[
H_n=\bigl\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\bigr\},\qquad P_n=\operatorname{conv}\{e_i-e_j:i\ne j\}\subset H_n.
\]
All volumes and Euclidean norms refer to the metric inherited from the ambient \(\mathbb R^n\). For a uniformly distributed random point \(X^{(n)}\) in \(P_n\), the covariance operator on \(H_n\) is exactly
\[
\operatorname{Cov}(X^{(n)})=\lambda_n I_{H_n},\qquad \lambda_n=\frac{4(2n-1)}{n(n+1)^2}.
\]
In particular, its affine-invariant isotropic constant, defined as \(L(P_n)=(\det_{H_n}\operatorname{Cov}X^{(n)})^{1/[2(n-1)]}/\operatorname{vol}_{H_n}(P_n)^{1/(n-1)}\), is
\[
L(P_n)=\frac{2\sqrt{(2n-1)/(n(n+1)^2)}}{\left[\sqrt n\binom{2n-2}{n-1}/(n-1)!\right]^{1/(n-1)}}\longrightarrow\frac1{\sqrt2\,e}.
\]
More strongly, these balls have a quantitative Gaussian thin-shell limit with an explicit sharp limiting variance:
\[
\boxed{\ \sqrt n\left(\frac n8\,\|X^{(n)}\|_2^2-1\right)\ \xrightarrow{\ d\ }\ N(0,1)\quad(n\to\infty).\ }
\]
The result includes the following exact constructive uniform sampler. Draw an integer \(K\in\{1,\dots,n-1\}\) with
\[
\Pr\{K=k\}=\frac{\binom nk\binom{n-2}{k-1}}{\binom{2n-2}{n-1}},
\]
choose independently a uniform \(k\)-subset \(S\subset[n]\), choose independent uniform Dirichlet simplex weights \((U_i)_{i\in S}\), \((V_i)_{i\notin S}\), and choose \(R\in[0,1]\) with \(\Pr(R\le r)=r^{n-1}\), all independent after conditioning on \(K\). Then \(X_i=RU_i\) on \(S\) and \(X_i=-RV_i\) off \(S\) is uniform on \(P_n\). In particular \(K-1\) is hypergeometric with population \(2n-2\), successful elements \(n-2\), and draws \(n-1\).

## Assumptions and scope

The metric on \(M_n\) has \(d(i,j)=1\) for distinct points. Its transportation norm on the zero-sum subspace is \(\|x\|_{\mathcal F(M_n)}=\frac12\sum_i|x_i|\), so \(P_n=\{x\in H_n:\sum_i|x_i|\le2\}\). All random variables are with respect to the intrinsic \((n-1)\)-dimensional Euclidean volume normalized to probability; the Gaussian convergence concerns **squared Euclidean radius**, not the Banach norm, which is the independent beta variable \(R\) in the sampler. At \(n=2\) the dimension is one and the formulas remain valid. The central limit theorem is an infinite-dimensional family asymptotic, not an exact normal law at finite \(n\).

## Proof

**1. Geometry, chamber volumes, and the uniform law.** In the relative interior of any sign chamber with \(k\) positive and \(n-k\) negative coordinates, the constraints \(\sum x_i=0\) and \(\sum_i|x_i|\le2\) mean the sum of the positive coordinates and the sum of the absolute negative coordinates both equal \(R\in(0,1)\). Thus the positive and negative coordinate vectors are \(R\) times independent points in their respective standard simplices. Directly computing the Jacobian in the hyperplane \(H_n\) gives the chamber-volume density
\[
\frac{\sqrt n}{(k-1)!(n-k-1)!}\,R^{n-2}\,dR
\]
for each specified sign set. Consequently, the intrinsic volume of one chamber is \(\sqrt n/[(n-1)(k-1)!(n-k-1)!]\). The total volume is
\[
V_n=\frac{\sqrt n}{(n-1)!}\sum_{k=1}^{n-1}\binom nk\binom{n-2}{k-1}
=\frac{\sqrt n}{(n-1)!}\binom{2n-2}{n-1},
\]
where the final equality is Vandermonde convolution. The normalized chamber volumes yield the asserted distribution of \(K\), while the radial density is \((n-1)r^{n-2}\,dr\), independently of \(K\), \(S\), and the two simplex components. This proves the uniform sampler, including its exact independence claims. The same binomial convolution identifies \(K-1\) as the stated hypergeometric variable. In particular \(\mathbb E K=n/2\) and \(\operatorname{Var}K=n(n-2)/[4(2n-3)]\), so \(K/n\to1/2\) in probability.

**2. Exact covariance and isotropic constant.** Each Dirichlet\((1,\ldots,1)\) vector of length \(k\) satisfies \(\mathbb E\sum U_i^2=2/(k+1)\). Also \(\mathbb E R^2=(n-1)/(n+1)\). The law is permutation-invariant and centrally symmetric, hence its covariance has to be scalar on the irreducible zero-sum permutation representation \(H_n\) (alternatively, constant diagonals and constant off-diagonals force this directly). Its trace is
\[
\mathbb E\|X^{(n)}\|_2^2
=\frac{n-1}{n+1}\,\mathbb E\left[\frac2{K+1}+\frac2{n-K+1}\right]
=\frac{4(n-1)}{n+1}\,\mathbb E\frac1{K+1}.
\]
Using \(\binom nk/(k+1)=\binom{n+1}{k+1}/(n+1)\) and a second Vandermonde identity,
\[
\mathbb E\frac1{K+1}
=\frac{1}{(n+1)\binom{2n-2}{n-1}}
  \sum_{k=1}^{n-1}\binom{n+1}{k+1}\binom{n-2}{k-1}
=\frac{2n-1}{n(n+1)}.
\]
It follows that \(\mathbb E\|X^{(n)}\|_2^2=4(n-1)(2n-1)/[n(n+1)^2]\). Dividing by \(\dim H_n=n-1\) proves \(\lambda_n\). Since the covariance determinant on \(H_n\) is \(\lambda_n^{n-1}\), the displayed formula for \(L(P_n)\) follows from \(V_n\). Stirling's formula gives \(V_n^{1/(n-1)}\sim4e/n\) and \(\sqrt{\lambda_n}\sim2\sqrt2/n\), yielding the stated limit.

**3. Limiting squared-radius fluctuations.** Take two independent infinite sequences of exponential random variables of mean one, independent of \(K\) and \(R\). The familiar exponential representation of a uniform Dirichlet simplex point shows that, conditionally on \(K=k\),
\[
\|X^{(n)}\|_2^2=R^2\left(\frac{Q_k}{k}+\frac{\widetilde Q_{n-k}}{n-k}\right),\qquad
Q_k=\frac{k^{-1}\sum_{j=1}^k E_j^2}{(k^{-1}\sum_{j=1}^k E_j)^2},
\]
where \(Q\) and \(\widetilde Q\) are built from independent exponential sequences. The bivariate ordinary central limit theorem and the delta method for \(f(a,b)=b/a^2\) at \((1,2)\) give
\[
\sqrt k(Q_k-2)\xrightarrow{\ d\ }N(0,4).
\]
Indeed the gradient is \((-4,1)\), and the covariance of \((E_j,E_j^2)\) is \(\begin{psmallmatrix}1&4\\4&20\end{psmallmatrix}\), yielding limiting variance \(4\). This proof also establishes the joint independent limits for \(Q\) and \(\widetilde Q\). Since \(K/n\to1/2\) in probability and the two exponential sequences are independent of \(K\), the same joint limits hold at the random sample sizes \(K\) and \(n-K\) (condition on \(K\), then use convergence uniformly for sample sizes exceeding any fixed threshold).

The radial factor satisfies \(R=U^{1/(n-1)}\) for an independent uniform \(U\in(0,1)\), so \(R^2=1+O_{\Pr}(n^{-1})\). Writing \(K=n/2+O_{\Pr}(\sqrt n)\), the deterministic conditional mean part obeys
\[
\frac n8\left(\frac2K+\frac2{n-K}\right)=1+O_{\Pr}(n^{-1}).
\]
Expanding the remaining centered terms gives independent limits
\[
\sqrt n\,\frac n8\frac{Q_K-2}{K}\xrightarrow{\ d\ }N(0,1/2),\qquad
\sqrt n\,\frac n8\frac{\widetilde Q_{n-K}-2}{n-K}\xrightarrow{\ d\ }N(0,1/2).
\]
The two centered terms converge jointly to independent Gaussians. The negligible radial and conditional-mean corrections vanish at \(\sqrt n\) scale. Slutsky's theorem gives the asserted \(N(0,1)\) limit. This argument proves the limit for all integer \(n\to\infty\) without any extrapolation from finite computation.

## Verification

The included standalone `verify.py` uses exact rational arithmetic for chamber-moment identities through \(n=23\). As a methodologically separate finite check, it independently constructs the convex hull in the first \(n-1\) zero-sum coordinates, triangulates its boundary, and integrates the squared intrinsic Euclidean radius exactly over each coned simplex for \(n=3,4,5,6\). The resulting intrinsic squared-radius means agree with the theorem after accounting for the zero-sum Gram matrix. It also performs optional seeded random-sampling diagnostics at \(n=40,160,400\). No finite check is claimed to establish the central limit theorem; that follows analytically from the exponential representation and delta method.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, Section 5.2) already evaluated the equilateral Lipschitz-free volume through sign-chamber integration. That volume and the decomposition on which it rests are therefore credited as known inputs, **not** as novel conclusions. Aliaga and Pernecká (arXiv:1810.11278) identified extreme molecules under strict metric triangles, supplying relevant finite Lipschitz-free geometry but not a uniform bulk distribution. Kipp (arXiv:2407.01353) studies isotropic constants and regular polytopes, without stating the present explicit covariance or radial distribution theorem for the type-A root family. Johnston and Prochno (arXiv:1911.00695) analyze Berry–Esseen bounds for random projections of \(\ell_p\) balls; projections do not have the fixed-hyperplane uniform-section distribution studied here. The specifically claimed contribution is the exact covariance/isotropic constant and Gaussian radial limit for the uniform type-A root-polytope law, together with its exact combinatorial-Dirichlet sampler, not the already published volume formula.

## Limitations

No rate of convergence, large-deviation bound, or analogue for arbitrary non-equilateral metric spaces is asserted. The limit concerns the Euclidean norm in the canonical zero-sum realization, which is not intrinsic to a Banach space up to arbitrary linear isometry. A literature search cannot rule out unindexed equivalent moment identities or general theorems that might imply the radial limit. The computation tests finitely many dimensions; its non-exhaustive random trials are diagnostics only.

## References

- R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278, publicly posted 2018-10-26, https://arxiv.org/abs/1810.11278.
- M. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first posted 2019-11-24, https://arxiv.org/abs/1911.10642. Especially Section 5.2.
- C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353, first posted 2024-07-01, https://arxiv.org/abs/2407.01353.
- S. Johnston and J. Prochno, *Berry–Esseen bounds for random projections of \(\ell_p^n\)-balls*, arXiv:1911.00695, first posted 2019-11-02, https://arxiv.org/abs/1911.00695.
