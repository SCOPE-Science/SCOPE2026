# Exact Hilbert distortion of quadratic \(\ell_1\)–\(\ell_\infty\) mixtures

## Finding
For each integer \(n\ge3\) and parameter \(t>0\), write
\[
N_t(x)=\bigl(\|x\|_\infty^2+t\|x\|_1^2\bigr)^{1/2},\qquad x\in\mathbb R^n.
\]
Define
\[
L_n(t)=\frac{1+nt+\sqrt{(1+nt)^2-4(n-1)t}}{2},\qquad
m_n(t)=\min_{1\le k\le n}\left(\frac1k+kt\right).
\]
Then the Banach--Mazur distance, with the infimum taken over **all** invertible real linear maps, is exactly
\[
\boxed{d_{\mathrm{BM}}((\mathbb R^n,N_t),\ell_2^n)^2=\frac{L_n(t)}{m_n(t)}.}
\]
The minimum on the Euclidean sphere is attained at an equal-amplitude, \(k\)-sparse point; the maximum is attained at a one-spike-plus-plateau point. The minimizing sparsity switches between \(k\) and \(k+1\) precisely when \(t=1/[k(k+1)]\).

Across **all positive parameters**, the best achievable Hilbert distortion obeys the sharp asymptotic law
\[
\boxed{\lim_{n\to\infty} n^{-1/4}\inf_{t>0}d_{\mathrm{BM}}((\mathbb R^n,N_t),\ell_2^n)=\frac1{\sqrt2}.}
\]
The explicit choice \(t=1/n\) attains the optimal asymptotic constant.

## Assumptions and scope
All scalars are real, \(n\) is an arbitrary integer at least \(3\), and \(t\) is any strictly positive real number. The norms \(\|\cdot\|_1\) and \(\|\cdot\|_\infty\) are the standard coordinate norms. The displayed \(N_t\) is a norm: its triangle inequality follows by applying the usual coordinatewise triangle inequalities and then the monotonicity and triangle inequality of the Euclidean norm on the nonnegative quadrant. The Banach--Mazur distance is \(\inf_T\|T\|\|T^{-1}\|\), with \(T\) running over all linear isomorphisms to Euclidean space. The result is **not** a claim about the complex case or about linear mixtures \((1-t)\|\cdot\|_\infty+t\|\cdot\|_1\).

## Proof
**Step 1 (global ellipsoid reduction).** Let \(G\) be the finite group of signed coordinate permutations. For every invertible \(T\), put \(Q=T^{\mathsf T}T\), and on the compact \(N_t\)-unit sphere write \(a=\min_{N_t(x)=1}x^{\mathsf T}Qx\), \(b=\max_{N_t(x)=1}x^{\mathsf T}Qx\). Since \(N_t(gx)=N_t(x)\) for all \(g\in G\), the inequalities \(a\le x^{\mathsf T}g^{\mathsf T}Qgx\le b\) hold simultaneously for every \(g\) and every unit vector \(x\). Averaging gives \(a\le c\|x\|_2^2\le b\), because the group average of \(g^{\mathsf T}Qg\) is \(cI\), where \(c>0\). Hence the distortion of \(T\), squared, is at least the ratio of the largest to smallest values of \(N_t(x)^2\) on the Euclidean unit sphere. Taking \(T=I\), with an immaterial scalar rescaling, attains that ratio. Therefore
\[
d_{\mathrm{BM}}^2=\frac{\max_{\|x\|_2=1}N_t(x)^2}{\min_{\|x\|_2=1}N_t(x)^2}.
\]
This optimizes over arbitrary ellipsoids, not just axis-aligned ones.

**Step 2 (spectral maximum).** For any \(x\),
\[
\|x\|_\infty^2+t\|x\|_1^2=
\max_{1\le i\le n,\;\varepsilon\in\{-1,1\}^n}
\left(x_i^2+t\left(\sum_{j=1}^n\varepsilon_jx_j\right)^2\right).
\]
The relevant matrices are \(e_ie_i^{\mathsf T}+t\varepsilon\varepsilon^{\mathsf T}\). They are all conjugate by signed permutations and have rank at most two, trace \(1+nt\), and product of nonzero eigenvalues \(t(n-1)\). Their largest eigenvalue is precisely \(L_n(t)\). Since the maxima range over a finite set of continuous Rayleigh quotients and the Euclidean sphere is compact,
\[
\max_{\|x\|_2=1}N_t(x)^2=L_n(t).
\]
For the representative matrix \(e_1e_1^{\mathsf T}+t\boldsymbol 1\boldsymbol 1^{\mathsf T}\), a positive maximizing eigenvector is proportional to \((L_n(t)/(L_n(t)-1),1,\dots,1)\), because \(L_n(t)>1\) and the eigenvalue equations imply \((L_n(t)-1)x_1=L_n(t)x_2\).

**Step 3 (sparse minimum).** Take nonzero \(x\) and divide it by \(\|x\|_\infty\), so its maximum coordinate magnitude becomes \(1\). Put \(s=\|x\|_1\), \(k=\lfloor s\rfloor\), and \(\theta=s-k\), using \(k=n\), \(\theta=0\) at \(s=n\). Thus \(1\le s\le n\) and all coordinate magnitudes lie in \([0,1]\). By moving mass from a smaller fractional coordinate to a larger one, preserving the sum, the sum of squares never decreases; repeating yields \(k\) ones, at most one coordinate \(\theta\), and zeros elsewhere. Therefore \(\|x\|_2^2\le k+\theta^2\). It follows that
\[
\frac{N_t(x)^2}{\|x\|_2^2}\ge
H_k(s):=\frac{1+ts^2}{k+(s-k)^2}.
\]
On \(k\le s\le k+1\), the derivative has the sign of
\[
g_k(\theta)=tk(k+\theta)(1-\theta)-\theta.
\]
Here \(g_k(0)=tk^2>0\), \(g_k(1)=-1<0\), and \(g_k'(\theta)=tk(1-k-2\theta)-1<0\). Thus \(H_k\) increases then decreases and its minimum over the interval occurs at an endpoint. Those endpoints give exactly \(1/k+tk\) and \(1/(k+1)+t(k+1)\). The endpoints are realized by vectors with exactly that many equal-magnitude nonzero coordinates. Therefore
\[
\min_{\|x\|_2=1}N_t(x)^2=m_n(t).
\]
Two consecutive support sizes \(k\) and \(k+1\) tie exactly when \(t=1/[k(k+1)]\); the lower envelope of the lines \(1/k+kt\) has no other transitions. Combining the two sphere extrema with Step 1 proves the distance formula and extremizer descriptions.

**Step 4 (sharp dimensional tuning).** Put \(k_n=\lfloor\sqrt n\rfloor\). The spectral formula implies \(L_n(t)\ge\max\{1,nt\}\), and the minimum formula implies \(m_n(t)\le1/k_n+k_nt\). Therefore, for every \(t>0\),
\[
d_{\mathrm{BM}}^2\ge
\frac{\max\{1,nt\}}{1/k_n+k_nt}
\ge\frac{k_nn}{n+k_n^2},
\]
where the last bound follows by elementary monotonicity on the two intervals separated by \(t=1/n\). Conversely, setting \(t=1/n\) gives the exact identity \(L_n(1/n)=1+1/\sqrt n\) and the arithmetic--geometric mean bound \(m_n(1/n)\ge2/\sqrt n\), whence
\[
\inf_{t>0}d_{\mathrm{BM}}^2\le
\frac{\sqrt n+1}{2}.
\]
After dividing by \(\sqrt n\), both bounds tend to \(1/2\). Taking positive square roots proves the claimed sharp \(n^{1/4}\) asymptotic with constant \(1/\sqrt2\) and the asymptotic optimality of \(t=1/n\).

## Verification
The derivation identifies both continuous extremizers explicitly; no computation is needed for infinite-dimensional or unbounded parameter ranges, and there is no claim about infinite-dimensional spaces. The standalone Python 3 checker in `artifacts/verify_quadratic.py` evaluates the analytic maximum and minimum, substitutes the explicit extremizers, and tests \(72{,}000\) deterministic Euclidean-sphere samples across six dimensions and eight parameters per dimension. It also prints the normalized tuned distortions for several larger dimensions. All checked cases passed. These finite sanity checks are **not** used as proof of the universal statements.

## Relationship to prior work
Zhang, Meng and Wu (arXiv:2207.05499v1, 2022, primary MSC 46B20) treat Banach--Mazur distances of finite-dimensional \(\ell_p\) spaces to the cube and motivate exact distortion questions. Their full text gives no result for the quadratic mixed norm or its distance to Euclidean space. Gotoh and Uryasev (2015) compare four **polyhedral** one-parameter norm families, including the linear convex combination of \(\ell_1\) and \(\ell_\infty\) norms, to \(\ell_p\) norms. The mixture here combines the *squares* of the endpoint norms under a square root, is nonpolyhedral in general, and is not a relabeling of their linear family. Their accessible abstract and indexed defining formula do not give the present rank-two maximum, sparse-minimum transition law, or sharp dimensional asymptotic; their full article was not readable in this comparison, leaving an explicit source-access risk. Deza, Hiriart-Urruty and Pournin (arXiv:2011.05607) study cube--cross-polytope *intersection* polytopes and their faces and volumes, whereas the present mixed quadratic unit balls are different.

A publicly indexed two-dimensional result on the Euclidean distortion of mixed \(\ell_p\)–\(\ell_q\) plane norms covers only exponents on the same side of \(2\); in particular it does not treat the exponent pair \((1,\infty)\), and it contains no higher-dimensional or sharp asymptotic statement. These comparisons are by precise object, hypotheses, and mathematical implications, not matching terminology alone.

## Limitations
The formula concerns real \(n\)-dimensional spaces for \(n\ge3\), positive weights, and comparison to Euclidean space only. No finite-dimensional minimizer \(t\) of the entire Banach--Mazur profile is explicitly classified: the asymptotic optimization statement does not assert that \(t=1/n\) is an exact finite-dimensional minimizer. The numerical checker cannot prove the quantified theorem. An equivalent formulation in unindexed mixed-norm literature remains possible, especially because one closely related 2015 paper was accessible only through its abstract and indexed excerpts. No independent external audit has been performed.

## References
1. L. Zhang, L. Meng and S. Wu, “Banach-Mazur Distance from \(\ell_p^3\) to \(\ell_\infty^3\),” arXiv:2207.05499v1, first posted 2022-07-12, primary MSC 46B20; https://arxiv.org/abs/2207.05499.
2. J.-Y. Gotoh and S. Uryasev, “Two pairs of families of polyhedral norms versus \(\ell_p\)-norms: proximity and applications in optimization,” Mathematical Programming 156 (2016), 391–431; DOI 10.1007/s10107-015-0899-9; publicly available by 2015.
3. A. Deza, J.-B. Hiriart-Urruty and L. Pournin, “Polytopal balls arising in optimization,” arXiv:2011.05607v1, first posted 2020-11-11, Contributions to Discrete Mathematics 16 (2021), 125–138; https://arxiv.org/abs/2011.05607.
4. H. Mizuguchi and K.-S. Saito, “Some geometric constants of absolute normalized norms on \(\mathbb R^2\),” Annals of Functional Analysis 2 (2011), 22–33, DOI 10.15352/afa/1399900191; foundational planar mixed-norm comparisons.
