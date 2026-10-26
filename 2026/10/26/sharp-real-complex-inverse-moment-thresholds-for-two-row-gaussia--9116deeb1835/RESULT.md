# Sharp real–complex inverse-moment thresholds for two-row Gaussian Hankel matrices

## Finding

Fix an integer \(m\ge2\) and \(\mathbb F\in\{\mathbb R,\mathbb C\}\). Put \(\beta=1\) for \(\mathbb F=\mathbb R\), and \(\beta=2\) for \(\mathbb F=\mathbb C\). Let \(g_0,\ldots,g_m\) be independent standard real Gaussians or standard circular complex Gaussians, respectively. Define the overlapping input Hankel matrix
\[
H_m=\begin{pmatrix}g_0&g_1&\cdots&g_{m-1}\\g_1&g_2&\cdots&g_m\end{pmatrix},\qquad s_m=\sigma_{\min}(H_m),\qquad \kappa_m=\frac{\sigma_{\max}(H_m)}{s_m}.
\]
Then \(H_m\) has full row rank almost surely, and there exist positive constants \(c_{m,\beta},C_{m,\beta},t_{m,\beta}\) such that, for every \(0<t<t_{m,\beta}\),
\[
 c_{m,\beta}t^{\beta(m-1)}\le \Pr(s_m\le t)\le C_{m,\beta}t^{\beta(m-1)}.
\]
Consequently, for every real \(p>0\),
\[
 \mathbb E\|H_m^\dagger\|_2^p<\infty\quad\Longleftrightarrow\quad p<\beta(m-1),\qquad
 \mathbb E\kappa_m^p<\infty\quad\Longleftrightarrow\quad p<\beta(m-1).
\]
The upper and lower bounds imply the same power-law cutoff for both condition-number and pseudoinverse tails; no limiting tail constant is asserted. In particular, for real data the mean pseudoinverse norm is infinite at \(m=2\), finite at \(m\ge3\), and its second moment is finite exactly when \(m\ge4\). For complex data the corresponding mean is already finite at \(m=2\), while its second moment is finite exactly when \(m\ge3\).

## Assumptions and scope

All Gaussians in the generating sequence are independent, but adjacent entries and rows *within* the Hankel matrix overlap. The singular values and norms are spectral (Euclidean) ones, and \(H_m^\dagger\) is the Moore–Penrose pseudoinverse. Complex Gaussians have density \(\pi^{-1}\exp(-|z|^2)\) on \(\mathbb C\). Constants are allowed to depend on the fixed column count \(m\) and the field, but not on \(t\) or the moment order \(p\). No bound uniform as \(m\to\infty\) is claimed.

## Proof

**1. A uniform convolution singular-value bound.** For any unit vector \(\theta=(a,b)\in\mathbb F^2\), let \(L_\theta:\mathbb F^{m+1}\to\mathbb F^m\) be the linear map
\[
 (L_\theta u)_j=\overline a u_j+\overline b u_{j+1},\qquad 0\le j<m.
\]
This is precisely \(\theta^*H_m(u)\). The Hermitian \(m\)-by-\(m\) matrix \(L_\theta L_\theta^*\) has unit diagonal and the same off-diagonal coefficient \(\overline b a\) on every superdiagonal (and its conjugate on the subdiagonal). Its eigenvalues are
\[
 1+2|ab|\cos\frac{k\pi}{m+1},\qquad k=1,\ldots,m,
\]
up to reversing their order. Hence its least eigenvalue is bounded below uniformly by
\[
 c_m^2=1-\cos\frac{\pi}{m+1}>0,
\]
because \(2|ab|\le1\). In particular, \(L_\theta\) is surjective and has a one-dimensional kernel over \(\mathbb F\), and for every \(u\),
\[
 \|L_\theta u\|\ge c_m\operatorname{dist}(u,\ker L_\theta).
\]

**2. Spherical upper small-ball bound.** Regard \(\mathbb F^{m+1}\) as a real Euclidean space of dimension \(\beta(m+1)\). Write \(g=RU\), with \(U\) uniformly distributed on its unit sphere and independent of the Gaussian radius \(R>0\). For any fixed unit \(\theta\), spherical projection onto the real orthogonal complement of \(\ker L_\theta\) has dimension \(\beta m\). Its squared length has the \(\operatorname{Beta}(\beta m/2,\beta/2)\) distribution. The bound in step 1 therefore gives, for \(0<t<c_m/2\),
\[
 \Pr\{\|L_\theta U\|\le t\}\le C_{m,\beta}'t^{\beta m},
\]
uniformly in \(\theta\).

The projective space \(\mathbb F P^1\) of unit row coefficients modulo a scalar phase has real dimension \(\beta\): a circle when \(\beta=1\), a two-sphere when \(\beta=2\). It admits a projective \(t\)-net of at most \(C_\beta t^{-\beta}\) points, where the distance between representatives minimizes over unit phases. Also, for every unit \(u\), \(\|H_m(u)\|_2\le\|H_m(u)\|_F\le\sqrt2\). If \(\sigma_{\min}(H_m(U))\le t\), a minimizing row coefficient is within projective distance \(t\) of a net point, and that point satisfies \(\|L_\theta U\|\le(1+\sqrt2)t\). A union bound therefore gives
\[
 \Pr\{\sigma_{\min}(H_m(U))\le t\}\le C_{m,\beta}''t^{\beta m-\beta}=C_{m,\beta}''t^{\beta(m-1)}.
\]
The exponent uses the two-dimensional, not three-dimensional, projective net in the complex case; ignoring phase would lose a power of \(t\).

Set \(\alpha=\beta(m-1)\). Since \(\mathbb E[R^{-\alpha}]<\infty\) for the chi radius in real dimension \(\beta(m+1)>\alpha\), integrating the preceding bound conditional on \(R\) yields
\[
 \Pr\{s_m\le t\}=\mathbb E\Pr\{\sigma_{\min}(H_m(U))\le t/R\mid R\}\le C t^\alpha\mathbb E[R^{-\alpha}],
\]
where the spherical inequality can be extended to all positive thresholds by increasing its constant. This proves the upper half of the small-ball assertion. It also shows that the rank-deficient event has probability zero.

**3. Sharp lower bound from geometric-sequence charts.** Restrict \(g_0\) to a small real or complex disk around \(1\), and \(g_1\) to a small disk around \(1/2\). Thus \(r=g_1/g_0\) is well defined and bounded and \(|g_0|\ge c_0>0\). Set
\[
 e_j=g_{j+1}-r g_j,\qquad j=1,\ldots,m-1.
\]
For fixed \((g_0,g_1)\), the triangular transformation between \((g_2,\ldots,g_m)\) and \((e_1,\ldots,e_{m-1})\) has real Jacobian determinant of absolute value one (also over \(\mathbb C\)). In a fixed bounded chart, the joint Gaussian density has a positive lower bound. Thus the event that \(|e_j|\le t/\sqrt{m-1}\) for every \(j\) has probability at least \(c t^{\beta(m-1)}\), for sufficiently small \(t\), while \(g_0,g_1\) remain in their disks.

Write \(v_0=(g_0,\ldots,g_{m-1})\) and \(v_1=(g_1,\ldots,g_m)\). By construction,
\[
 v_1-rv_0=(0,e_1,\ldots,e_{m-1}),
\]
so the unit row coefficient proportional to \((-\overline r,1)\) gives \(s_m\le\sqrt{\sum_j|e_j|^2}/\sqrt{1+|r|^2}\le t\). Moreover \(\sigma_{\max}(H_m)\ge\|v_0\|\ge c_0\). This proves the lower small-ball bound and supplies a corresponding lower \(t^{-\alpha}\) tail for \(\kappa_m\).

**4. Sharp moment criterion.** Almost surely \(\|H_m^\dagger\|_2=1/s_m\). The two-sided small-ball inequality and the layer-cake identity for nonnegative variables give \(\mathbb E[s_m^{-p}]<\infty\) precisely for \(p<\alpha\), with logarithmic divergence at equality. For the condition number, homogeneity gives \(\kappa_m=\kappa(H_m(U))\), and \(\sigma_{\max}(H_m(U))\le\sqrt2\). The spherical small-ball estimate thus bounds \(\Pr\{\kappa_m>z\}\le C z^{-\alpha}\), while the bounded chart in step 3 supplies \(\Pr\{\kappa_m>z\}\ge c z^{-\alpha}\) for large \(z\). The same layer-cake criterion proves the claim for every \(p>0\).

## Verification

A standalone standard-library Python checker, `verify.py`, uses exact rational arithmetic to verify the two-row Cauchy–Binet Gram determinant identity for all its seeded test cases, the geometric-sequence rank-one boundary and its triangular residual coordinates, and positivity of finite tridiagonal covariance pivots. Run with `python verify.py` in the package directory. It reports `VERIFY_OK` and the finite check count. These checks do not establish probability bounds for infinitely many Gaussian samples; the proof above does.

## Relationship to prior work

Schmitz, Schaller, Voigt and Worthmann [1] use Hankel matrices and explicitly discuss inherent poor conditioning in data-enabled predictive control; the present result concerns the fixed two-row random-input matrix's finite-sample *inverse moments*, not their fast solver or closed-loop properties. Lawrence et al. [2] analyze large-sample lower-singular-value growth under stochastic excitation; they do not provide the finite-column inverse-moment frontier above. Coulson, van Waarde and Dörfler [3] relate data-driven control robustness to quantitative persistent excitation without this Gaussian Hankel hard-edge law. Rudelson and Vershynin [4] prove small-singular-value bounds for **independent-entry** rectangular matrices; copying those conclusions to the overlapping Hankel ensemble would be unjustified. Onatski and Kargin [5] study an **increasing-row, proportional-aspect-ratio** Toeplitz regime and do not imply the fixed-two-row cutoff here.

## Limitations

Only the two-row Hankel input matrix generated by independent Gaussian samples, with spectral conditioning, is treated. The constants may deteriorate with the number of columns. This result neither gives a limiting probability coefficient nor establishes error bounds or stability for a particular closed-loop controller; additional state-output blocks, noisy measurements, or correlated/non-Gaussian inputs require new analysis. The similarity to the independent-entry Gaussian hard-edge exponent does not make the structured cases equivalent.

## References

[1] P. Schmitz, M. Schaller, M. Voigt, K. Worthmann, *Fast and memory-efficient optimization for large-scale data-driven predictive control*, arXiv:2402.13090v1, 2024-02-20, https://arxiv.org/abs/2402.13090.

[2] N. Lawrence, P. Loewen, S. Wang, M. Forbes, B. Gopaluni, *Stabilizing reinforcement learning control: A modular framework for optimizing over all stable behavior*, arXiv:2310.14098, https://arxiv.org/abs/2310.14098.

[3] J. Coulson, H. J. van Waarde, F. Dörfler, *Robust Fundamental Lemma for Data-driven Control*, arXiv:2205.06636, https://arxiv.org/abs/2205.06636.

[4] M. Rudelson, R. Vershynin, *The smallest singular value of a random rectangular matrix*, Communications on Pure and Applied Mathematics 62 (2009), https://arxiv.org/abs/0802.3956.

[5] A. Onatski, V. Kargin, *The smallest singular value of large random rectangular Toeplitz and circulant matrices*, arXiv:2412.17091, 2024-12-22, https://arxiv.org/abs/2412.17091.
