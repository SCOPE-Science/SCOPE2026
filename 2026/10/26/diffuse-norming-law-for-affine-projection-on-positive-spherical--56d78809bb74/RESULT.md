# Diffuse norming law for affine projection on positive spherical orthants

## Finding

Let \(S^{d-1}_+=\{x\in\mathbb R^d:\|x\|_2=1,\ x_i\ge0\}\) have normalized spherical surface measure \(\nu_d\), and let \(P_d\) be the \(L^2(\nu_d)\)-orthogonal projector onto restrictions of affine functions. Its evaluation-row \(L^\infty\)-norm at \(a\in S^{d-1}_+\) is \(\Lambda_d(a)=\int|K_d(a,x)|\,d\nu_d(x)\), where \(K_d\) is the reproducing kernel. Set
\[
\mu=\sqrt{2/\pi},\qquad c=1-3/\pi>0,\qquad
F(\theta)=\sqrt{\frac2\pi}\left(\frac{1-\theta^2}{1-2/\pi}+\frac{(\theta-\sqrt{2/\pi})^2}{1-3/\pi}\right)^{1/2}.
\]
For *every* sequence \(a^{(d)}\in S^{d-1}_+\) with \(\max_i a_i^{(d)}\to0\), set \(\theta_d=d^{-1/2}\sum_i a_i^{(d)}\in[0,1]\). Then the exact diffuse spatial asymptotic law is
\[
\frac{\Lambda_d(a^{(d)})}{\sqrt d}-F(\theta_d)\longrightarrow0.
\tag{1}
\]
The function \(F\) has its unique maximum on \([0,1]\) at \(\theta=0\), with value
\[
C_*=\sqrt{\frac2\pi}\left(\frac{1}{1-2/\pi}+\frac{2/\pi}{1-3/\pi}\right)^{1/2}=3.27783611857179\ldots .
\tag{2}
\]
Within the class of coordinate-delocalized sequences, asymptotically maximal amplification is characterized exactly by
\[
\frac{\Lambda_d(a^{(d)})}{\sqrt d}\to C_*
\quad\Longleftrightarrow\quad
\frac{\|a^{(d)}\|_1}{\sqrt d}\to0.
\tag{3}
\]
The value \(C_*\) is attained asymptotically, for example, by \(a^{(d)}\) equal to \(k_d^{-1/2}\) on \(k_d\) coordinates and zero elsewhere, when \(k_d\to\infty\) and \(k_d/d\to0\). In particular,
\[
\liminf_{d\to\infty}\frac{\|P_d\|_{L^\infty\to L^\infty}}{\sqrt d}\ge C_*.
\tag{4}
\]
The equality of this lower bound with the *global* asymptotic operator norm is not claimed.

## Assumptions and scope

Dimensions \(d\ge2\) are integers; \(\nu_d\) is normalized \((d-1)\)-dimensional spherical Hausdorff measure on the **positive orthant** of the unit Euclidean sphere, including its null-measure coordinate faces as evaluation points. Functions are real-valued and essentially bounded for \(\nu_d\). The approximation space consists exactly of restrictions of \(1,x_1,\dots,x_d\). A diffuse sequence has the explicitly quantified hypothesis \(\max_i a_i^{(d)}\to0\); this hypothesis does not cover coordinate vertices or vectors with fixed-size spikes. This is an asymptotic classification in the growing ambient dimension, not an exact norm computation at finite \(d\).

## Proof

**1. Exact Gram spectrum.** Let \(X\sim\nu_d\). Independent standard normal coordinates \(Z_i\) give the representation
\[
X_i=\frac{|Z_i|}{(\sum_{j=1}^d Z_j^2)^{1/2}}.
\]
A direct spherical moment calculation yields, for \(i\ne j\),
\[
m_d=\mathbb E X_i=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\quad
\mathbb E X_i^2=\frac1d,\quad
\mathbb E X_iX_j=\frac{2}{\pi d}.
\]
Writing \(u=d^{-1/2}(1,\ldots,1)\) and \(q=2/\pi\), the covariance matrix \(\Sigma_d=\operatorname{Cov}(X)\) has eigenvalue
\[
\lambda_{\perp,d}=\frac{1-q}{d}
\]
on \(u^\perp\), and eigenvalue
\[
\lambda_{\parallel,d}=\frac{1+(d-1)q-d^2m_d^2}{d}
\]
on \(\mathbb Ru\). Both are strictly positive: a nonconstant affine function cannot be constant almost everywhere on the positive spherical patch. The gamma-ratio expansion is
\[
m_d=\frac\mu{\sqrt d}\left(1+\frac1{4d}+O(d^{-2})\right),\qquad
d\lambda_{\parallel,d}\to 1-\frac{3}{\pi}=c>0.
\tag{5}
\]
The affine reproducing kernel, and hence the exact projection kernel, is
\[
K_d(a,x)=1+(a-m_d\mathbf1)^\top\Sigma_d^{-1}(x-m_d\mathbf1).
\tag{6}
\]
For \(\theta=d^{-1/2}\sum_i a_i\) and \(b=a-\theta u\), \(\sum b_i=0\), \(\|b\|_2^2=1-\theta^2\), this becomes
\[
K_d(a,X)=1+\frac{b\cdot X}{\lambda_{\perp,d}}+
\frac{\theta-\sqrt d\,m_d}{\lambda_{\parallel,d}}
\left(\frac1{\sqrt d}\sum_i(X_i-m_d)\right).
\tag{7}
\]
Because the kernel is continuous and \(\nu_d\) has full support on the orthant, \(\Lambda_d(a)\) is exactly the norm of evaluation of \(P_df\) at \(a\): choose \(f(x)=\operatorname{sgn}K_d(a,x)\). Also,
\[
\mathbb E K_d(a,X)^2=K_d(a,a)
=1+\frac{1-\theta^2}{\lambda_{\perp,d}}
+\frac{(\theta-\sqrt d\,m_d)^2}{\lambda_{\parallel,d}}.
\tag{8}
\]

**2. Joint limit law for diffuse evaluation points.** Put \(H_i=|Z_i|\), \(R_d=(\sum Z_i^2)^{1/2}\), and define
\[
B_d=\sum_i b_i(H_i-\mu),\qquad
T_d=\frac1{\sqrt d}\sum_i\left(H_i-\mu-\frac\mu2(Z_i^2-1)\right).
\]
The elementary Gaussian moment identities \(\operatorname{Var}(H_i)=1-\mu^2\), \(\operatorname{Var}(Z_i^2)=2\), and \(\operatorname{Cov}(H_i,Z_i^2)=\mu\) show
\[
\operatorname{Var}(B_d)=(1-q)(1-\theta_d^2),\quad
\operatorname{Var}(T_d)=c,\quad
\operatorname{Cov}(B_d,T_d)=c\sum_i b_i/\sqrt d=0.
\tag{9}
\]
Along every subsequence with \(\theta_d\to\theta\in[0,1]\), the assumption \(\max_i a_i^{(d)}\to0\) implies \(\max_i|b_i|\to0\), while \(\sum_i b_i^2\le1\). The two-dimensional triangular-array Lindeberg theorem, applied to the independent pairs \((b_i(H_i-\mu),\ d^{-1/2}[H_i-\mu-(\mu/2)(Z_i^2-1)])\), gives
\[
(B_d,T_d)\ \Rightarrow\ (B,T),
\]
where \(B,T\) are independent centered normal variables of variances \((1-q)(1-\theta^2)\) and \(c\), respectively. This includes the degenerate case \(\theta=1\).

Next the law of large numbers and the first-order delta method give
\[
\frac{R_d}{\sqrt d}\to1\quad\text{in probability},\qquad
\sum_i(X_i-m_d)=T_d+o_{\mathbb P}(1),\qquad
\sqrt d\,b\cdot X=B_d+o_{\mathbb P}(1).
\tag{10}
\]
For the middle identity, explicitly expand \(R_d=\sqrt d[1+(2d)^{-1}\sum_i(Z_i^2-1)+O_{\mathbb P}(d^{-1})]\); the \(\mu/2\) correction is exactly the fluctuation induced by normalizing the Gaussian radius. Substituting (5) and (10) into (7) yields
\[
\frac{K_d(a^{(d)},X)}{\sqrt d}
=\frac{B_d}{1-q}+\frac{\theta_d-\mu}{c}T_d+o_{\mathbb P}(1).
\tag{11}
\]
Along a subsequence with \(\theta_d\to\theta\), the right-hand side tends to a centered normal distribution of variance
\[
V(\theta)=\frac{1-\theta^2}{1-q}+\frac{(\theta-\mu)^2}{c}.
\tag{12}
\]
Equation (8) supplies a uniform \(L^2\) bound on \(K_d(a,X)/\sqrt d\), independently of the diffuse sequence (indeed uniformly over all \(a\in S^{d-1}_+\)), because \(d\lambda_{\parallel,d}\to c>0\). Therefore the absolute values are uniformly integrable, and their expectations converge to \(\sqrt{2/\pi}\sqrt{V(\theta)}=F(\theta)\). Every subsequence of \(\theta_d\in[0,1]\) has a convergent subsubsequence, proving the moving-parameter assertion (1).

**3. Sharp diffuse envelope and rigidity.** The squared profile \(V(\theta)\) is a strictly convex quadratic, since its \(\theta^2\)-coefficient is \(c^{-1}-(1-q)^{-1}>0\). Its endpoint gap is
\[
V(0)-V(1)=\frac{1}{1-q}+\frac{2\mu-1}{c}>0.
\]
Thus \(V\), and hence \(F\), has unique maximum on \([0,1]\) at \(0\). Formula (1), compactness of \([0,1]\), and strictness prove (3). For the \(k_d\)-supported equal-coordinate vector, \(\max_i a_i=k_d^{-1/2}\to0\) and \(\theta_d=\sqrt{k_d/d}\to0\); hence its normalized row norm tends to (2). Because \(\|P_d\|\ge\Lambda_d(a)\) at every evaluation point, (4) follows. No step takes a supremum over *nondiffuse* evaluation sequences. \(\square\)

## Verification

The accompanying `checks/verify.py` (Python 3 with NumPy) checks the exact two-eigenvalue Gram decomposition and covariance inversion for seven dimensions, the folded-normal/chi-square covariance identity, strict endpoint comparison, and independently sampled positive-orthant reproducing-kernel rows for four dimensions and distinct support sizes. It checks the **moving-parameter** asymptotic \(F(\sqrt{k/d})\), not a false finite-dimensional equality with \(C_*\). All sample tests passed upon execution from the delivered record. The analytic Lindeberg and delta-method argument, not these finite computations, proves (1)–(4).

## Relationship to prior work

Hangelbroek–Narcowich–Sun–Ward (2010) establish operator-norm stability of \(L^2\) projections onto well-localized kernel approximation spaces on smooth manifolds under quasiuniformity and basis hypotheses. Their Theorem 5.1 addresses a distinct projection space/parameter regime and does not give the present orthant-moment spectrum or sparse/diffuse asymptotics. The 2015 Savas–Karliga–Yakut work concerns geometric orthogonal projection onto spherical geodesic subspaces, not least-squares function projection. Defant and collaborators analyze minimal projections onto polynomial spaces on the **full** Euclidean sphere, with different symmetries and norming questions; the positive orthant destroys their full-sphere rotational symmetry. Related previously recorded affine projection results on Euclidean balls, hemispheres, and cones similarly do not determine the positive-orthant, coordinate-delocalized law (1). Equivalent unindexed older work is a residual possibility, not ruled out merely by search.

## Limitations

The sharp constant \(C_*\) is proved for delocalized evaluation sequences, and as a **global lower bound** only. The full global asymptotic \(L^\infty\)-operator norm, the behavior of fixed coordinate spikes, exact finite-dimensional extremizers, and other spherical sectors are not determined. The result concerns degree-one real affine approximation with normalized spherical surface measure and does not extend here to higher polynomial degrees or solid-orthant volume measure.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector* (first public 2010-05-13), arXiv:1005.2424, https://arxiv.org/abs/1005.2424.
2. M. Savas, B. Karliga, A. T. Yakut, *Orthogonal Projections Based on Hyperbolic and Spherical \(n\)-Simplex*, *Advances in Mathematical Physics* 2015, article 808250, https://doi.org/10.1155/2015/808250.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres* (2026), https://doi.org/10.1112/jlms.70429.
