# Optimal independent coordinate sketches: exact finite-support design and the \(\rho^\rho\) power-law loss

## Finding

Let \(\rho>1\), and let \(A_\rho:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\) be the diagonal Hilbert--Schmidt operator \(A_\rho e_j=j^{-\rho/2}e_j\). Among independent, identically distributed, **one-coordinate isotropic sketches** with \(L\ge2\) samples, the smallest expected squared Hilbert--Schmidt projection error is given exactly by a truncated power-law design. For its normalized infimum, the sharp large-budget inefficiency relative to an optimally chosen rank-\(L\) approximation is

\[
\lim_{L\to\infty}\frac{\inf_{\pi_j>0,\;\sum_j\pi_j=1}\mathbb E\|A_\rho-P_{\operatorname{ran}(A_\rho\Omega)}A_\rho\|_{\mathrm{HS}}^2}{\inf_{\operatorname{rank}B\le L}\|A_\rho-B\|_{\mathrm{HS}}^2}=\rho^\rho.
\]

In the class with positive probability at every coordinate, the finite-\(L\) infimum is **not attained**. Its unique optimizer in the larger closed simplex places positive mass on finitely many coordinates; isotropic full-support laws can approach its error arbitrarily closely.

## Assumptions and scope

The Hilbert space is real \(\mathcal H=\ell^2(\mathbb N)\); \(\rho>1\) is fixed. For a distribution \(\pi=(\pi_j)_{j\ge1}\) with all \(\pi_j>0\), \(\sum\pi_j=1\), let \(J\sim\pi\) and let \(\xi\in\{-1,1\}\) be an independent equiprobable sign. One sketch is \(\omega=\xi\pi_J^{-1/2}e_J\). For every \(u,v\in\mathcal H\), \(\mathbb E\langle u,\omega\rangle\langle\omega,v\rangle=\langle u,v\rangle\); no finite expectation of \(\|\omega\|^2\) is assumed. Draw \(L\ge2\) independent sketches and put \(Q=P_{\operatorname{span}\{A_\rho\omega_1,\ldots,A_\rho\omega_L\}}\). The error is the squared Hilbert--Schmidt norm of \(A_\rho-QA_\rho\), rather than an operator norm or a truncated sample-space rank-\(k\) SVD.

For any fixed integer \(L\ge2\), set \(\delta=\rho/(L-1)\). Let \(t=t_{\rho,L}>1\) be the unique solution of

\[
\sum_{1\le j<t}\bigl[1-(j/t)^\delta\bigr]=1.
\]

Write \(m=\lceil t\rceil-1\). The unique minimizing probability law in the *closed* simplex is

\[
\pi_j^*=\bigl[1-(j/t)^\delta\bigr]_+,
\qquad
\mathcal E_L^*=(m-1)t^{-\rho}+\sum_{j=m+1}^\infty j^{-\rho}.
\]

All infima over fully supported isotropic coordinate sketches in the finding equal \(\mathcal E_L^*\). More precisely, as \(L\to\infty\),

\[
t_{\rho,L}\sim m_{\rho,L}\sim L/\rho,\qquad
\mathcal E_L^*\sim\frac{\rho^\rho}{\rho-1}L^{1-\rho}.
\]

For two sketches, \(m=2\), \(\pi_1^*=2^\rho/(1+2^\rho)\), \(\pi_2^*=1/(1+2^\rho)\), and

\[
\mathcal E_2^*=\sum_{j\ge3}j^{-\rho}+\frac1{1+2^\rho}.
\]

## Proof

**Exact expected projection error.** A nonzero sketch image is a scalar multiple of the basis vector \(e_J\), because \(A_\rho e_J=J^{-\rho/2}e_J\). Thus \(Q\) retains exactly the sampled coordinates. The probability that coordinate \(j\) is absent from all \(L\) independent samples is \((1-\pi_j)^L\). By Tonelli's theorem,

\[
\mathcal E_L(\pi)=\sum_{j\ge1}j^{-\rho}(1-\pi_j)^L.
\]

**Optimality over all probability laws.** For \(L\ge2\), the summand \(f_j(p)=j^{-\rho}(1-p)^L\) is strictly convex on \([0,1)\). Define \(F(t)=\sum_{j<t}[1-(j/t)^\delta]\). It is continuous and strictly increasing for \(t>1\), with \(F(1)=0\) and \(F(t)\to\infty\). Its unique level-one root produces nonnegative \(\pi^*\) summing to one, supported on precisely \(1\le j\le m\). For the common multiplier \(\lambda=Lt^{-\rho}\), differentiation gives \(f_j'(\pi_j^*)=-\lambda\) on \(j\le m\), while \(f_j'(0)=-Lj^{-\rho}\ge-\lambda\) on \(j>m\). The supporting-hyperplane inequality for convex functions therefore implies, for any probability law \(\pi\),

\[
\mathcal E_L(\pi)-\mathcal E_L(\pi^*)
\ge\sum_j f_j'(\pi_j^*)(\pi_j-\pi_j^*)\ge0.
\]

The sums are justified because the derivatives are bounded in absolute value by \(L\) and the \(\ell^1\) distance between probability laws is at most two. Strict convexity on the coordinates where the designs can differ proves uniqueness: if \(\pi\ne\pi^*\), at least one coordinate has distinct probabilities and strictly positive curvature along its intervening segment, except possibly at the isolated endpoint \(1\), where strict convexity on \([0,1]\) still holds for \(L\ge2\). In particular no fully supported probability is an optimizer. Conversely \(\pi^{(\varepsilon)}=(1-\varepsilon)\pi^*+\varepsilon(2^{-j})_{j\ge1}\) is fully supported and isotropic; dominated convergence yields \(\mathcal E_L(\pi^{(\varepsilon)})\to\mathcal E_L^*\). Substitution into the exact error formula and \(\sum_{j\le m}(j/t)^\delta=m-1\) give the stated finite-\(L\) optimum.

**Sharp asymptotics.** Put \(\delta=\rho/(L-1)\to0\) and write \(\phi_t(x)=[1-(x/t)^\delta]_+\) for positive \(x\). For \(0<\delta\le1\), the tangent inequality to the concave function \(x^\delta\) at one gives \(1-(x/t)^\delta\ge\delta(1-x/t)\) for \(0<x\le t\). Because \(F(t)=1\), summing over integers \(j\le t/2\) shows \(t=O(\delta^{-1})\). Since \(F(t)\to0\) for every fixed \(t\) as \(\delta\to0\), necessarily \(t\to\infty\). The decreasing-function integral comparison yields

\[
0\le\int_0^t\phi_t(x)\,dx-F(t)
\le\int_0^1\phi_t(x)\,dx
\le\delta(1+\log t)=o(1),
\]

where the last inequality uses \(1-e^{-u}\le u\) and \(t=O(\delta^{-1})\). The integral equals \(t\delta/(1+\delta)\). Hence \(t\delta\to1\), so \(t\sim m\sim L/\rho\). By the ordinary integral test, \(\sum_{j>m}j^{-\rho}\sim m^{1-\rho}/(\rho-1)\). Also \((m-1)t^{-\rho}\sim t^{1-\rho}\). Therefore

\[
\mathcal E_L^*\sim\frac{\rho}{\rho-1}t^{1-\rho}
\sim\frac{\rho^\rho}{\rho-1}L^{1-\rho}.
\]

Finally, the compact diagonal operator has decreasing singular values \(j^{-\rho/2}\), and the Eckart--Young--Mirsky theorem gives optimal rank-\(L\) squared Hilbert--Schmidt error \(\sum_{j>L}j^{-\rho}\sim L^{1-\rho}/(\rho-1)\). Dividing proves the limit. For \(L=2\), inserting support \(\{1,2\}\) gives \(t^\rho=1+2^\rho\); the strict inequality \(1+2^\rho<3^\rho\) ensures \(2<t<3\), and direct substitution yields the special case.

## Verification

`coupon_checker.py` is a self-contained Python 3 checker. It independently enumerates finite independent-sampling spaces to compare with the missing-coordinate formula, verifies the root normalization and first-order optimality relations over many \((\rho,L)\) pairs, and tests finite-budget values against the predicted large-sample ratio. It also checks the exact two-draw case. An execution passed 90 test families. These computations supplement, but do not establish, the infinite-dimensional uniqueness or asymptotic proof; the preceding arguments establish those claims.

## Relationship to prior work

Lynch-Davies and Webb's 2026 work supplies the motivating infinite-dimensional isotropic sketch framework and explicitly constructs an almost-surely finite **one-coordinate isotropic sketch**, but does not derive the optimal distribution for a particular spectral profile. Saibaba and Międlar study non-Gaussian randomized low-rank approximation and discuss coordinate-sampling/coupon-collector issues; their performance bounds do not give this specific spectral-design optimum or sharp power-law loss. Halko, Martinsson and Tropp's randomized low-rank methodology and its coupon-collector examples are foundational rather than a derivation of this optimized law. General optimal weighted-coupon-allocation or caching literature may contain mathematically equivalent finite-budget first-order conditions; historical priority is not certified. The new mathematical target is the combination of full-support isotropy, the exact finite-support limiting design and its quantified \(\rho^\rho\) loss.

## Limitations

The result is for diagonal operators with pure power-law squared singular values, independent identically distributed one-coordinate sketches, and squared Hilbert--Schmidt error. It does not characterize arbitrary sparse/sub-Gaussian/Gaussian sketches or general non-diagonal targets, nor imply an information-theoretic lower bound for unrestricted randomized algorithms. The optimal closed-simplex design is not itself full-support isotropic; only its infimum is accessible in the required class. This is a proof for the stated model, not a general algorithm benchmark. A possible equivalent earlier weighted-coverage allocation calculation remains a historical-priority risk; there has been no independent audit.

## References

1. Morgan Lynch-Davies and Marcus Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1 (first public October 22, 2026), https://arxiv.org/abs/2610.31333, particularly Example 2.13 and the introductory algorithm and sampling discussion.
2. Arvind K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1 (2023), https://arxiv.org/abs/2308.05814, particularly their coordinate-sampling and coupon-collector discussion.
3. Nathan Halko, Per-Gunnar Martinsson and Joel A. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), https://arxiv.org/abs/0909.4061, particularly the randomized rangefinding paradigm and coupon-collector caveat.
4. Michael B. Cohen, Cameron Musco and Christopher Musco, *Input sparsity time low-rank approximation via ridge leverage score sampling*, arXiv:1511.07263 (2015), https://arxiv.org/abs/1511.07263. This reference concerns different low-rank sampling guarantees rather than the exact iid one-coordinate design.
