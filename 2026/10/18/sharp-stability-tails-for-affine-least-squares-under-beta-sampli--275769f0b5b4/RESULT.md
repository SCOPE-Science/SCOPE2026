# Sharp stability tails for affine least squares under Beta sampling

## Finding
For fixed integer \(n\ge2\), real \(\alpha,\beta>0\), and independent \(X_i\sim\operatorname{Beta}(\alpha,\beta)\), let \(K_n\) be the empirical-to-population stability norm of the affine least-squares space. The following three mutually exclusive large-\(t\) regimes give exact leading constants. Put
\[
\mu=\frac{\alpha}{\alpha+\beta},\qquad
\sigma^2=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)},\qquad
\nu=n-1,\quad a_*=\frac{n-1}{n},\quad
V_\nu=\frac{\pi^{\nu/2}}{\Gamma(1+\nu/2)}.
\]
Write \(B=B(\alpha,\beta)\), \(f(z)=z^{\alpha-1}(1-z)^{\beta-1}/B\), and \(a_0=\alpha,a_1=\beta\).

**Interior dominated:** when \(\alpha,\beta>a_*\),
\[
\Pr(K_n>t)\sim \frac{C_{\rm bulk}}{t^\nu},\qquad
C_{\rm bulk}=n^{n/2}V_\nu\int_0^1f(z)^n\bigl(\sigma^2+(z-\mu)^2\bigr)^{\nu/2}\,dz.
\]
**Critical:** when \(\alpha,\beta\ge a_*\) and at least one equals \(a_*\),
\[
\Pr(K_n>t)\sim C_{\rm crit}\,t^{-\nu}\log t,\qquad
C_{\rm crit}=\frac{n^{n/2}V_\nu}{B^n}
\sum_{\substack{e\in\{0,1\}\\a_e=a_*}}
\bigl(\sigma^2+(e-\mu)^2\bigr)^{\nu/2}.
\]
**Endpoint dominated:** when \(a=\min(\alpha,\beta)<a_*\),
\[
\Pr(K_n>t)\sim C_{\rm corner}\,t^{-na},\qquad
C_{\rm corner}=\frac1{B^n}
\sum_{\substack{e\in\{0,1\}\\a_e=a}}
J_n(a,R_e),\qquad
R_e=\sqrt{n\bigl(\sigma^2+(e-\mu)^2\bigr)},
\]
where
\[
J_n(a,R)=\int_{\substack{y_i>0\\\sum_i(y_i-\bar y)^2<R^2}}
\prod_{i=1}^ny_i^{a-1}\,dy_1\cdots dy_n
\]
is finite and positive precisely for \(0<a<a_*\). Thus every \(p>0\) satisfies
\[
\boxed{\ \mathbb E K_n^p<\infty\quad\Longleftrightarrow\quad
p<\min\{n-1,n\alpha,n\beta\}.\ }
\]
For uniform samples this gives \(\mathbb EK_n<\infty\) precisely from \(n=3\), and \(\mathbb EK_n^2<\infty\) precisely from \(n=4\). For three uniform samples the exact squared-tail coefficient is \(C_{\rm bulk}=\pi\sqrt3/2\).

## Assumptions and scope
All limits keep \(n\), \(\alpha\), and \(\beta\) fixed. The independent samples have beta density \(f\) on \((0,1)\). Population orthonormality is in \(L^2(f)\), with affine feature vector
\[
\phi(x)=\left(1,\frac{x-\mu}{\sigma}\right)^\mathsf T,\quad
G_n=\frac1n\sum_{i=1}^n\phi(X_i)\phi(X_i)^\mathsf T,\quad
K_n=\lambda_{\min}(G_n)^{-1/2}.
\]
The matrix is positive definite almost surely because the samples are not all equal. The condition number here is the operator norm of the empirical-to-population least-squares projection, not the spectral condition number \(\lambda_{\max}(G_n)/\lambda_{\min}(G_n)\). A linear change of domain identifies this degree-one model with Jacobi-weighted affine least squares on \([-1,1]\).

## Proof
**1. Exact instability event.** Define the sample mean \(Z=n^{-1}\sum_iX_i\), and quadratic spread \(Q=\sum_i(X_i-Z)^2\). In the orthonormal basis,
\[
G_n=\begin{pmatrix}
1&(Z-\mu)/\sigma\\
(Z-\mu)/\sigma&((Z-\mu)^2+Q/n)/\sigma^2
\end{pmatrix},\qquad
\det G_n=\frac{Q}{n\sigma^2}.
\]
Since \(\lambda_{\max}(G_n)\ge1\), for every \(t>1\) the inequality \(\lambda_{\min}(G_n)<t^{-2}\) is equivalent to \(\det(G_n-t^{-2}I)<0\). Completing the scalar inequality yields the *exact* event
\[
\boxed{\ Q<\frac n{t^2}\left[\sigma^2+\frac{(Z-\mu)^2}{1-t^{-2}}\right].\ }
\]
If \(R(z)=\sqrt{n(\sigma^2+(z-\mu)^2)}\), the exact event differs from \(Q<R(Z)^2/t^2\) by a uniform relative \(1+O(t^{-2})\) in the squared tube radius; the coefficient of this error depends on the fixed parameters, not the random sample. Thus a sharp continuous tube-volume asymptotic for the latter event carries over to \(K_n\).

**2. Tube coordinates.** Decompose \((X_1,\ldots,X_n)=Z\mathbf1+u\), with \(u\in H=\{u:\sum_i u_i=0\}\) and \(\lVert u\rVert^2=Q\). The Euclidean Jacobian is \(\sqrt n\,dZ\,du_H\), where \(H\) has dimension \(\nu=n-1\). The approximate event is the ball \(\lVert u\rVert<R(Z)/t\), restricted by \(0<Z+u_i<1\). Hence its probability is
\[
\sqrt n\int_0^1\int_{\substack{u\in H,\ \lVert u\rVert<R(z)/t\\0<z+u_i<1}}
\prod_i f(z+u_i)\,du_H\,dz.
\]
For each interior \(z\in(0,1)\), rescale \(u=w/t\). The rescaled cross-section tends to a Euclidean \(\nu\)-ball of radius \(R(z)\). Its volume is \(V_\nu R(z)^\nu\), giving density of the interior constant
\(\sqrt n V_\nu R(z)^\nu f(z)^n\).

**3. Uniform endpoint estimates.** The radius \(R(z)\) is bounded above and away from zero for \(z\in[0,1]\). For any fixed sufficiently large \(C\), the tube with \(z\in[C/t,\epsilon]\) has all its sample coordinates comparable with \(z\) as \(C\to\infty\), uniformly in \(t\), and contributes
\[
\frac{\sqrt n V_\nu}{t^\nu}
\int_{C/t}^{\epsilon}R(z)^\nu f(z)^n\,dz
\quad\text{up to a multiplicative }1+O(C^{-1})+o_t(1).
\]
Near zero the integrand equals
\[
\frac{\sqrt n V_\nu R(0)^\nu}{B^n}\,z^{n(\alpha-1)}(1+o(1)),
\]
and near one it has the analogous exponent \(n(\beta-1)\) and constant \(R(1)\). The small-\(z\) layer \(0\le z\le C/t\) is \(O_C(t^{-n\alpha})\), by the change \(X_i=y_i/t\) and integrability on bounded regions. Similarly the upper layer is \(O_C(t^{-n\beta})\). These estimates, first with fixed \(C\), then with \(C\to\infty\) and \(\epsilon\to0\), distinguish all three regimes without interchanging unbounded integrals illegitimately.

If both exponents exceed \(-1\), equivalently \(\alpha,\beta>a_*\), the interior integrand is integrable and the endpoint layers are \(o(t^{-\nu})\). Dominated localization yields \(C_{\rm bulk}\).

If an exponent equals \(-1\), equivalently \(\alpha=a_*\) or \(\beta=a_*\), the corresponding intermediate tube contributes \(\sqrt n V_\nu R(e)^\nu B^{-n}t^{-\nu}\log t\). Its corner layer is only \(O(t^{-\nu})\); noncritical endpoints contribute lower order. Since \(\sqrt n R(e)^\nu=n^{n/2}(\sigma^2+(e-\mu)^2)^{\nu/2}\), summing the critical endpoints yields \(C_{\rm crit}\).

If \(\alpha=a<a_*\), take \(X_i=y_i/t\) near the zero endpoint. The event becomes \(\sum_i(y_i-\bar y)^2<R(0)^2+o(1)\), and the density-volume factor becomes \(t^{-na}B^{-n}\prod_i y_i^{a-1}\,dy\). The resulting integral \(J_n(a,R(0))\) is finite: near each coordinate face, \(a>0\) gives local integrability; along the large-diagonal direction, all \(y_i\) are within \(O(R)\) of a common \(s\), and the integral behaves like \(\int_1^\infty s^{n(a-1)}ds\), which converges exactly when \(na<n-1\). A truncation at large \(\lVert y\rVert\), followed by dominated convergence on compact sets, proves convergence to the corner integral. Its tail outside a truncation contributes at most a constant times \(t^{-na}\) times a vanishing diagonal integral. The upper endpoint is analogous. Any endpoint with larger exponent is lower order. When the two exponents tie below threshold, their disjoint corner contributions add. This proves \(C_{\rm corner}\).

**4. Moment threshold.** The three asymptotics have a strictly positive coefficient and tail index \(q=\min(n-1,n\alpha,n\beta)\), with a possible logarithm at equality. The layer-cake identity \(\mathbb E K_n^p=p\int_0^\infty t^{p-1}\Pr(K_n>t)\,dt\) gives finite moments precisely for \(0<p<q\) and divergence at \(p=q\), proving the assertion.

## Verification
The independent numerical checker in `verify.py` compares the empirical Gram determinant, trace and the exact tube event across 5,000 randomized beta datasets and 20,000 threshold cases, checks the uniform two-point tail by a direct one-dimensional quadrature, verifies the three-point uniform coefficient, tests the explicit two-point corner integral \(J_2(a,R)=B(a,1-2a)(\sqrt2R)^{2a}/a\) for \(0<a<1/2\), and compares two million direct three-point uniform draws to the predicted leading constant. Its deterministic seed and numerical tolerances are specified in source. The infinite-parameter theorem and integrability are proved analytically above; simulations are not a substitute for asymptotic proof.

## Relationship to prior work
Xu and Zhang (arXiv:2407.10221, first public 2024-07-14), Lemma 2.3, give the exact identification of the least-squares stability constant with \(\lambda_{\min}(G_n)^{-1/2}\). Their Theorems 1.1 and 1.4 concern degree/sample-size high-probability stability, rather than the fixed-degree large-condition-number tail and sharp leading constants derived here. The affine change from \([-1,1]\) to \([0,1]\) respects the Jacobi/Beta setting.

Royen (arXiv:0810.1572), Theorem 3, establishes the \(\min(na,n-1)/2\) lower-tail exponent and threshold logarithm for the *unweighted* sample spread \(Q\) under a one-sided power-law parent. Those exponents and singularity mechanisms are prior art, not claimed as new. Unlike \(Q\), the least-squares stability norm corresponds exactly to a sample-mean-dependent threshold \(Q<R(Z)^2/t^2\); Royen's marginal \(Q\) distribution does not specify the sharp coefficients for this event.

The previously published three-sample Beta sample-variance phase theorem supplies the analogous unweighted \(n=3\) competing-endpoint classification and is acknowledged as closest overlapping work. It does not give \(K_n\)'s mean-dependent constants or the all-\(n\) affine stability classification. Cohen, Davenport and Leviatan (arXiv:1111.4422) provide high-probability discrete least-squares Gram control, not exact catastrophic tails. A broader joint small-ball theorem not located in these checks could subsume the coefficients; that priority risk is explicitly retained.

## Limitations
Only degree-one polynomial least squares, independent fixed-parameter beta samples, and the rare-event limit \(t\to\infty\) are considered. The constants are positive convergent integrals, not asserted to be elementary in general. No uniform-in-\(n\) remainder bound, confidence interval, error bound for noisy data, or extension to higher polynomial degrees is proven. The finding does not assert novelty for the classical sample-variance small-ball exponent, and possible stronger theorems on joint mean-and-variance small-ball asymptotics remain an originality risk.

## References
1. Z. Xu and X. Zhang, *Stability of Least Squares Approximation under Random Sampling*, arXiv:2407.10221 (first public 2024-07-14), especially Lemma 2.3 and Theorems 1.1, 1.4.
2. T. Royen, *The exact distribution of the sample variance from bounded continuous random variables*, arXiv:0810.1572 (2008), especially Theorem 3.
3. A. Cohen, M. Davenport and D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422 (2011).
4. *Exact lower-tail phase diagram for the three-sample Beta variance*, publicly available research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-lower-tail-phase-diagram-for-the-three-sample-beta-varianc--f275509045a1.
5. S. Jebalia and A. Karoui, *A Stable Jacobi polynomials based least squares regression estimator associated with an ANOVA decomposition model*, arXiv:2208.02891 (2022).
