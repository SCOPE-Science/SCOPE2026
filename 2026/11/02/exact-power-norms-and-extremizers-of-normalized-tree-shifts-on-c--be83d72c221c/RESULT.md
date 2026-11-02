# Exact power norms and extremizers of normalized tree shifts on Cesàro spaces

## Finding

Let \(1<p<\infty\). On any locally finite, leafless, spherically homogeneous rooted tree, let \(M\) average the values over each vertex's children. For the level-mean Cesàro norm defined below, every integer \(k\ge1\) satisfies

\[
\boxed{\|M^k\|^p=\frac{\zeta(p)}{\zeta(p,k+1)}=\frac{\sum_{j=1}^{\infty}j^{-p}}{\sum_{j=k+1}^{\infty}j^{-p}}.}
\]

Here \(\zeta(p,k+1)\) is the Hurwitz-zeta tail. The nonzero norm-attaining functions are *exactly* those supported on level \(k\) whose nonzero entries have a common complex argument (for real scalar values, the same sign). In particular, branching numbers have no effect on the norm. Moreover,

\[
\|M^k\|\sim\big((p-1)\zeta(p)\big)^{1/p}k^{1-1/p},\qquad r(M)=1,
\]

so the averaging shift is not power bounded. For fixed \(k\), \(\lim_{p\to\infty}\|M^k\|=k+1\).

## Assumptions and scope

Take a rooted tree \(\mathcal T\) with root \(o\). Every vertex on level \(j\) has exactly \(b_{j+1}\in\{1,2,\ldots\}\) children, with no finite upper bound on the sequence of branching numbers required. Every individual number is finite. Let \(\mathcal T_j\) denote the finite level \(j\), of cardinality \(c_0=1\) and \(c_j=\prod_{i=1}^j b_i\). The scalar field is either \(\mathbb C\) or \(\mathbb R\).

For \(f:\mathcal T\to\mathbb C\), define the nonnegative level means and the norm by

\[
A_j(f)=\frac1{c_j}\sum_{v\in\mathcal T_j}|f(v)|,\qquad
\|f\|_{\operatorname{Ces}_p(\mathcal T)}^p=\sum_{n=0}^{\infty}\left(\frac1{n+1}\sum_{j=0}^n A_j(f)\right)^p.
\]

The space comprises exactly the functions of finite norm. Define \((Mf)(v)=b_{|v|+1}^{-1}\sum_{u\in\operatorname{Chi}(v)}f(u)\). The theorem includes the single-infinite-ray case \(b_j=1\). It concerns the *unweighted normalized child-mean* shift, not an arbitrary weighted sum shift. For \(\lambda\in\mathbb C\), \(\|(\lambda M)^k\|=|\lambda|^k\|M^k\|\). For \(\lambda=0\), every vector attains the trivial zero operator norm; the nonzero-extremizer characterization is asserted only for \(M^k\).

## Proof

**1. A sharp scalar tail-shift lemma.** Let \(S\) be the backward shift on the classical Cesàro sequence space, \((Sx)_j=x_{j+1}\), with norm \(\|x\|^p=\sum_{n\ge0}\big((n+1)^{-1}\sum_{j=0}^n|x_j|\big)^p\). Fix an integer \(k\ge1\) and a nonzero \(x\) with \(S^kx\ne0\). Removing the first \(k\) entries can only reduce the denominator \(\|x\|\), strictly if any of the removed entries was nonzero. For the remaining tail write \(y_j=|x_{j+k}|\) and \(u_n=\sum_{j=0}^n y_j\). Then \(u_n\) is nondecreasing and

\[
\|S^kx\|^p=\sum_{n\ge0}\frac{u_n^p}{(n+1)^p},\qquad
\|x\|^p\ge\sum_{n\ge0}\frac{u_n^p}{(n+k+1)^p}.
\]

For completeness, put \(a_n=(n+k+1)^{-p}\), \(h_n=((n+k+1)/(n+1))^p\), and \(d_n=u_n^p\). The weights \(a_n\) have finite positive sum, \(h_n\) is *strictly decreasing*, and \(d_n\) is nondecreasing. Normalizing \(a_n\) into a probability mass \(\mu_n=a_n/\sum_j a_j\), the identity

\[
\operatorname{Cov}_{\mu}(d,h)
=\frac12\sum_{i,j\ge0}\mu_i\mu_j(d_i-d_j)(h_i-h_j)\le0
\]

holds first for bounded truncations of \(d\) and then by monotone convergence of the separate nonnegative expectations. All needed expectations are finite because \(\sum_n a_nd_n\le\|x\|^p<\infty\) and \(h_n\le(k+1)^p\). Hence

\[
\frac{\sum_n a_n h_n d_n}{\sum_n a_n d_n}
\le\frac{\sum_n a_n h_n}{\sum_n a_n}
=\frac{\zeta(p)}{\zeta(p,k+1)}.
\]

Equality requires \(d_n\) constant in \(n\), because \(\mu_n>0\) and \(h_n\) is strictly decreasing. Thus \(u_n\) is constant: \(y_j=0\) for \(j\ge1\). Together with the strictly improving effect of removing any nonzero first \(k\) coordinates, this shows that all nonzero scalar extremizers are precisely multiples of the coordinate vector at position \(k\). Such a coordinate vector attains the displayed ratio, so \(\|S^k\|^p=\zeta(p)/\zeta(p,k+1)\). When \(S^kx=0\), the strict positive optimal ratio cannot be attained.

**2. Tree contraction by level means.** For every \(v\in\mathcal T_j\), the descendants at distance \(k\) number \(c_{j+k}/c_j\); each vertex on level \(j+k\) descends from exactly one vertex on level \(j\). By the triangle inequality,

\[
A_j(M^kf)
\le\frac1{c_{j+k}}\sum_{u\in\mathcal T_{j+k}}|f(u)|
=A_{j+k}(f).
\]

Consequently, \(\|M^kf\|\le\|S^k(A_j(f))_{j\ge0}\|\le\big(\zeta(p)/\zeta(p,k+1)\big)^{1/p}\|f\|\). If \(f\) is supported only at level \(k\) and all its nonzero entries have the same complex phase, then \(M^kf\) is supported only at the root, with \(|(M^kf)(o)|=A_k(f)\); both inequalities are equalities. This proves exact norm attainment.

For necessity, equality in the scalar lemma forces \(A_j(f)=0\) for \(j\ne k\), so \(f\) vanishes off level \(k\). Equality in the triangle inequality at the root is now necessary; for a finite sum of nonzero complex terms, this holds exactly when all have one argument. This gives the complete nonzero extremizer set.

**3. Asymptotic consequences.** The integral-test estimate \(\zeta(p,k+1)\sim k^{1-p}/(p-1)\) gives the power-growth equivalent. Taking \(k\)-th roots gives the spectral radius \(\lim_{k\to\infty}\|M^k\|^{1/k}=1\), and the growth exponent is positive since \(p>1\). For fixed \(k\), \(\zeta(p)\to1\) as \(p\to\infty\), while \(\zeta(p,k+1)^{1/p}\to1/(k+1)\), giving the last limit.

## Verification

The standalone `check_power_norms.py` uses the closed value \(\zeta(2)=\pi^2/6\), exact infinite-tail summation for finite-support sequences up to floating-point precision, and three different finite spherically homogeneous tree profiles. Running `python check_power_norms.py` passed **2,118** finite checks, including spike extremizers, unequal-amplitude same-phase tree extremizers, and random complex perturbations. These calculations test definitions and constants; they do not prove the infinite theorem. The preceding scalar covariance and level-averaging arguments prove it for all admissible \(p\), \(k\), and trees.

## Relationship to prior work

Chen, Cheng, Zhang, and Zhou (2026), arXiv:2609.21752v1, introduce weighted backward shifts on Cesàro spaces of rooted trees and provide boundedness/dynamics criteria, including general bounds of a different form; they do not state the present exact power norms for normalized child means. Albanese and Asensio (published October 13, 2026), Section 4, Lemma 4.1 and Corollary 4.2, discuss the classical unweighted Cesàro shift and give a nonsharp norm bound by \(2\), without the exact zeta-tail formula, power profile or equality cases. Their space-and-operator results are prior and are not claimed anew. The proof here specializes the positive-shift estimates using a strictly monotone weighted-covariance identity and uses homogeneity to cancel tree branching exactly.

## Limitations

This is confined to normalized child averages on spherically homogeneous leafless rooted trees and \(1<p<\infty\). It does not cover arbitrary edge weights, nonhomogeneous branching, Cesàro endpoints \(p=1\) or \(p=\infty\), or dynamics beyond the displayed spectral-radius and power-growth conclusions. Publication priority remains subject to the possibility of an older unindexed exact classical Cesàro-shift norm formula or an implicit equivalent consequence of general positive-operator theory. No independent mathematical audit has been performed.

## References

1. Xiang Chen, Meng-Huan Cheng, Liang Zhang, Ze-Hua Zhou, *Dynamics of Weighted Backward Shifts on Cesàro Spaces of Rooted Trees*, arXiv:2609.21752v1 (first submitted September 18, 2026), https://arxiv.org/abs/2609.21752; full text https://arxiv.org/html/2609.21752.
2. Angela A. Albanese and Vicente Asensio, *On the linear dynamics of shift operators on (PLB)-spaces*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas, published online October 13, 2026, https://doi.org/10.1007/s13398-026-01935-0, especially Section 4.
