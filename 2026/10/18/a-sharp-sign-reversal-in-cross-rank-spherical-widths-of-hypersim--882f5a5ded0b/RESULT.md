# A sharp sign reversal in cross-rank spherical widths of hypersimplices

## Finding

Let \(H_n=\{u\in\mathbb R^n:\sum_{i=1}^{n}u_i=0\}\), and let
\(\Delta_{n,k}=\operatorname{conv}\{\mathbf1_B:B\subseteq[n],\ |B|=k\}\)
be the rank-\(k\) hypersimplex in its canonical Euclidean realization. For a **single common** direction \(U_n\), uniform on the unit sphere in \(H_n\), write
\[
W_{n,k}=\max_{x\in\Delta_{n,k}}\langle U_n,x\rangle-\min_{x\in\Delta_{n,k}}\langle U_n,x\rangle.
\]
For \(0<\alpha\le\tfrac12\), set \(k_n(\alpha)=\lfloor n\alpha\rfloor\), \(t_\alpha=\Phi^{-1}(1-\alpha)\), \(\mu_\alpha=2\varphi(t_\alpha)\), and \(X_\alpha(z)=(|z|-t_\alpha)_+\), where \(\Phi,\varphi\) denote the standard normal distribution function and density.

**Joint angular-width theorem.** For every finite set \(\mathcal A\subset(0,\tfrac12]\), as \(n\to\infty\),
\[
\left(W_{n,k_n(\alpha)}-\sqrt n\,\mu_\alpha\right)_{\alpha\in\mathcal A}
\ \Longrightarrow\ \mathcal N(0,(K(\alpha,\beta))_{\alpha,\beta\in\mathcal A}),
\]
and the **actual covariances** converge to the same kernel. For \(0<\alpha\le\beta\le\tfrac12\), its closed formula is
\[
\begin{split}
K(\alpha,\beta)={}&2\bigl[(1+t_\alpha t_\beta)\alpha-t_\beta\varphi(t_\alpha)\bigr]\\
&-4\bigl[\varphi(t_\alpha)-t_\alpha\alpha\bigr]
 \bigl[\varphi(t_\beta)-t_\beta\beta\bigr]
-2\varphi(t_\alpha)\varphi(t_\beta).
\end{split}
\]
For reversed arguments interchange them. In particular, the final negative term is the correction from projecting to the Euclidean unit sphere; the leading unnormalized Gaussian trimmed-sum covariance is nonnegative because both influence functions are increasing in the same absolute Gaussian observation.

**Unique sign transition.** There is exactly one \(\alpha_*\in(0,\tfrac12)\), numerically
\[
\alpha_*=0.207998088885\ldots,
\]
such that
\[
\lim_{n\to\infty}\operatorname{Cov}\bigl(W_{n,\lfloor\alpha n\rfloor},W_{n,\lfloor n/2\rfloor}\bigr)
\begin{cases}<0,&0<\alpha<\alpha_*,\\=0,&\alpha=\alpha_*,\\>0,&\alpha_*<\alpha\le\tfrac12.\end{cases}
\]
More precisely, \(\alpha_*=1-\Phi(t_*)\), where \(t_*>0\) is the unique positive solution of
\[
2\bigl(1-\Phi(t)\bigr)+\frac{4t}{\sqrt{2\pi}}\bigl(1-\Phi(t)\bigr)
-\frac{6}{\sqrt{2\pi}}\varphi(t)=0,
\qquad t_*=0.813387056892\ldots.
\]
The covariance limits are, for example, \(K(0.05,0.5)=-0.015630673999\ldots\) and \(K(0.3,0.5)=0.018790937333\ldots\).

## Assumptions and scope

Each \(\Delta_{n,k}\) is considered in the hyperplane \(\sum_i x_i=k\), with the ambient induced Euclidean metric. The widths at different ranks are evaluated using the **same** direction, not independent directions. Every rank fraction is a fixed number strictly between zero and one half, with one half allowed; the statement makes no assertion when the rank fraction tends to zero with \(n\). The Gaussian limit may be degenerate in principle, as is standard for a covariance-kernel statement; the sign comparison above is nondegenerate away from the unique zero.

## Proof

**1. Ordered-coordinate representation.** Let \(Z_1,\ldots,Z_n\) be independent standard Gaussians; put \(\bar Z=n^{-1}\sum_iZ_i\) and \(R_n=(\sum_i(Z_i-\bar Z)^2)^{1/2}\). Then \(U_n=(Z-\bar Z\mathbf1)/R_n\) is uniform on the sphere of \(H_n\) and independent of \(R_n\), which has the \(\chi_{n-1}\) distribution. If \(Z_{(1)}\le\cdots\le Z_{(n)}\) are ordered observations, maximization over the indicator vertices gives exactly
\[
W_{n,k}=T_{n,k}/R_n,
\qquad T_{n,k}=\sum_{i=n-k+1}^{n}Z_{(i)}-\sum_{i=1}^{k}Z_{(i)}.
\]
Subtracting \(\bar Z\) leaves both order and upper-minus-lower sums unchanged.

**2. A quantitative trimmed-sum linearization.** Fix \(\alpha\in(0,\tfrac12]\), set \(t=t_\alpha\) and \(k=\lfloor n\alpha\rfloor\). The upper sum is the minimum, over all real \(s\), of
\[
A_n(s)=ks+\sum_{i=1}^{n}(Z_i-s)_+.
\]
Its empirical minimizing threshold lies between the corresponding adjacent order statistics. The lower contribution is the same expression applied to \(-Z_i\). The Dvoretzky–Kiefer–Wolfowitz bound gives
\(\Pr(\sup_x|F_n(x)-\Phi(x)|>n^{-1/3})\le2e^{-2n^{1/3}}\).
On the complementary event, positivity and continuity of \(\varphi(t)\) imply every minimizing threshold differs from \(t\) by at most \(C_\alpha n^{-1/3}\). Throughout that interval the absolute derivative of \(A_n\), at its continuity points, is at most \(C_\alpha n^{2/3}\). Thus the improvement over \(A_n(t)\) is \(O_\alpha(n^{1/3})\). On the exponentially unlikely event, the error is bounded by a deterministic multiple of \(n(1+|t|+\max_i|Z_i|)\), which has polynomially bounded fourth moment. Consequently the error is \(o_{L^2}(\sqrt n)\), simultaneously for any finite collection of fixed fractions.

Combining upper and lower tails therefore yields
\[
T_{n,k}=2kt+\sum_{i=1}^{n}X_\alpha(Z_i)+o_{L^2}(\sqrt n)
=n\mu_\alpha+\sum_{i=1}^{n}\bigl(X_\alpha(Z_i)-m_\alpha\bigr)+o_{L^2}(\sqrt n),
\]
where \(m_\alpha=\mathbb EX_\alpha(Z)=2[\varphi(t_\alpha)-t_\alpha\alpha]\) and \(2\alpha t_\alpha+m_\alpha=\mu_\alpha\). The integer-floor error in the latter identity is bounded.

**3. Joint Gaussian limit with spherical correction.** The standard Gaussian central limit theorem applies jointly to the finite collection of \(X_\alpha(Z_i)-m_\alpha\) and \(Z_i^2-1\). Since \(n\bar Z^2=O_{\Pr}(1)\),
\[
R_n=\sqrt n+\frac{1}{2\sqrt n}\sum_{i=1}^n(Z_i^2-1)+o_{\Pr}(1).
\]
Dividing the result of Step 2 by this radius gives
\[
W_{n,k_n(\alpha)}-\sqrt n\mu_\alpha
=\frac1{\sqrt n}\sum_{i=1}^nY_\alpha(Z_i)+o_{\Pr}(1),
\quad
Y_\alpha(z)=X_\alpha(z)-m_\alpha-\frac{\mu_\alpha}{2}(z^2-1).
\]
Gaussian integration by parts gives \(\operatorname{Cov}(X_\alpha(Z),Z^2-1)=\mu_\alpha\), whereas \(\operatorname{Var}(Z^2-1)=2\). Thus
\[
K(\alpha,\beta)=\operatorname{Cov}(X_\alpha(Z),X_\beta(Z))
-\tfrac12\mu_\alpha\mu_\beta=\mathbb E[Y_\alpha(Z)Y_\beta(Z)].
\]
For \(\alpha\le\beta\), direct Gaussian-tail integration gives
\[
\mathbb E[X_\alpha(Z)X_\beta(Z)]
=2\int_{t_\alpha}^{\infty}(z-t_\alpha)(z-t_\beta)\varphi(z)\,dz
=2\bigl[(1+t_\alpha t_\beta)\alpha-t_\beta\varphi(t_\alpha)\bigr],
\]
proving the displayed kernel and the joint weak limit.

To establish **covariance convergence**, rather than infer it from weak convergence, use independence of \(R_n\) and the complete random-width vector:
\[
\operatorname{Cov}(T_{n,k_\alpha},T_{n,k_\beta})
=(n-1)\operatorname{Cov}(W_{n,k_\alpha},W_{n,k_\beta})
+\operatorname{Var}(R_n)\mathbb EW_{n,k_\alpha}\,\mathbb EW_{n,k_\beta}.
\]
The \(L^2\) linearization gives the left-hand side divided by \(n\) tending to \(\operatorname{Cov}(X_\alpha,X_\beta)\). Also \(\operatorname{Var}(R_n)\to\tfrac12\) by the chi-distribution mean formula, and \(\mathbb EW_{n,k_\alpha}/\sqrt n\to\mu_\alpha\). Rearrangement proves convergence of the actual covariances to \(K\).

**4. Existence and uniqueness of the sign reversal.** Fix \(\beta=\tfrac12\), put \(c=\varphi(0)=1/\sqrt{2\pi}\), and write \(t=t_\alpha\). The formula simplifies to
\[
G(t):=K(\alpha,\tfrac12)
=2\bar\Phi(t)+4ct\bar\Phi(t)-6c\varphi(t),
\qquad\bar\Phi(t)=1-\Phi(t).
\]
At the balanced rank, \(G(0)=1-3/\pi>0\). For large \(t\), Mills' ratio implies \(G(t)/\varphi(t)\to-2c<0\); in particular \(G(t)\to0\) from below. Its derivative is
\[
G'(t)=2B(t),\quad B(t)=2c\bar\Phi(t)+(ct-1)\varphi(t),\quad
B'(t)=\varphi(t)[t-c(1+t^2)].
\]
The quadratic bracket has precisely two positive zeros
\(t_\pm=[1\pm\sqrt{1-4c^2}]/(2c)\).
As \(B(0)=0\) and \(B'(0)<0\), \(B\) is negative just to the right of zero. It decreases until \(t_-\), increases until \(t_+\), and then decreases. Since \(B(t)/\varphi(t)=ct-1+2c\bar\Phi(t)/\varphi(t)>0\) eventually, \(B\) has exactly one positive zero, necessarily between \(t_-\) and \(t_+\). Therefore \(G\) strictly decreases and then strictly increases toward zero from below. Because \(G(0)>0\), it has exactly one positive zero \(t_*\). The monotonic correspondence \(\alpha=\bar\Phi(t)\) gives the claimed unique rank threshold and sign ordering. A bracketing computation yields the stated decimal values; uniqueness is analytical, not numerical.

## Verification

The accompanying `check_hypersimplex.py` checks the sorted-coordinate support-function identity against direct optimization over hypersimplex vertices in 250 cases, independently integrates six Gaussian mixed moments, brackets the unique critical zero, and simulates 20,000 independent spherical directions in dimension 768 to check the predicted opposite covariance signs for fractions 0.05 and 0.30 versus the half-rank width. The Gaussian integral and root checks have deterministic tolerances; the simulation has a fixed random seed and is a numerical sanity check only. The infinite-dimensional convergence and uniqueness are proved above, not established by simulation.

## Relationship to prior work

Pineda-Villavicencio and Schröter (2020), *Reconstructibility of matroid polytopes*, identify hypersimplices as canonical uniform-matroid base polytopes and study their combinatorial reconstructibility. This work supplies the geometric object and primary MSC ownership, but its results concern face reconstruction, not dependence between different ranks' random directional widths.

Kabluchko, Litvak, and Zaporozhets (2015), *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, establish Gaussian and spherical-width methods, including self-normalization for cube and other regular-polytope widths. Both radial normalization and normal central-limit tools are therefore **prior techniques**. The claimed contribution here is the explicit proportional-rank hypersimplex covariance kernel and the proved unique negative-to-positive cross-rank transition at a nontrivial rank fraction. Generic asymptotic theory for trimmed Gaussian order statistics is also prior methodology.

## Limitations

The result concerns canonical hypersimplices with a single shared uniform direction and ranks proportional to dimension. It neither treats shrinking ranks nor arbitrary affine realizations. The quoted decimal threshold is a numerical evaluation of a uniquely defined analytic zero. No claim of historical uniqueness can follow solely from unsuccessful searches; earlier results phrased in terms of jointly studentized Gaussian L-statistics could potentially imply part of the covariance kernel. Independent mathematical review has not been performed.

## References

1. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227 (first posted 2020-10-20), https://arxiv.org/abs/2010.10227. MSC2020 primary 52B11.
2. Z. Kabluchko, A. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (2015), https://arxiv.org/abs/1511.08479.
