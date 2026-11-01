# Sharp section–shadow coupling and asymptotically independent fluctuations of regular simplices

## Finding

For every integer \(N\ge3\), let \(S_N=\operatorname{conv}\{e_1,\ldots,e_N\}\) be the regular Euclidean \((N-1)\)-simplex in the affine hyperplane \(\sum_i x_i=1\). Put \(L_N=\{u\in\mathbb R^N:\sum_i u_i=0\}\), and choose a unit vector \(U\) Haar-uniformly on the sphere of \(L_N\). Let \(H_U\) be the affine hyperplane through the centroid with normal \(U\). The same normal determines a central **section** \(S_N\cap H_U\) and an orthogonal **shadow** \(\operatorname{proj}_{U^\perp}S_N\), viewed in their affine spans. Define
\[
C_N=f_0(S_N\cap H_U),\quad A_N=\operatorname{Vol}_{N-2}(\operatorname{proj}_{U^\perp}S_N),\quad F_N=\frac{\sqrt{N-1}}{(N-2)!},\quad Y_N=\frac{2A_N}{F_N}.
\]
Here \(U^\perp\) is taken inside \(L_N\), the ambient linear space parallel to the simplex, so the projection has dimension \(N-2\). With probability one no coordinate of \(U\) vanishes. For every such direction, write \(p=\#\{i:U_i>0\}\), \(q=N-p\). Then
\[
\boxed{C_N=pq,\qquad Y_N=\sqrt{\frac N{N-1}}\sum_{i=1}^N|U_i|.}
\tag{1}
\]
The **complete feasible simultaneous section–shadow range for a prescribed sign split** is
\[
\boxed{\sqrt{\frac{2N}{N-1}}<Y_N\le 2\sqrt{\frac{pq}{N-1}}\quad (p,q\ge1,\ p+q=N).}
\tag{2}
\]
Every value in this half-open interval occurs for some generic direction with exactly \(p\) positive coordinates. The upper endpoint is attained precisely by two-level normals, whose coordinates are constant on the positive and negative groups; the lower endpoint is a sharp but unattained infimum for \(N\ge3\). In geometric units, \(A_N^2\le F_N^2 C_N/(N-1)\), with the same exact equality class. Thus (2), as \(p\) ranges from \(1\) to \(N-1\), classifies all possible ordered pairs \((C_N,A_N)\) for generic central sections and their perpendicular shadows.

The **exact finite-dimensional shadow moments**, valid for every \(N\ge3\), are
\[
\boxed{\mathbb EY_N=\frac{N\Gamma((N-1)/2)}{\sqrt\pi\,\Gamma(N/2)},}
\tag{3}
\]
\[
\boxed{\mathbb EY_N^2=\frac N{N-1}+\frac{2N}{\pi}\left(\sqrt{1-\frac1{(N-1)^2}}+\frac{\arcsin(1/(N-1))}{N-1}\right).}
\tag{4}
\]
In particular \(\operatorname{Var}(Y_N)=\mathbb EY_N^2-(\mathbb EY_N)^2\to1-3/\pi\). Writing \(\mu=\sqrt{2/\pi}\), \(\tau^2=1-3/\pi\), and \(s^2=1/4-1/(2\pi)\), we have the following **joint limit from the same randomly oriented hyperplane**:
\[
\boxed{\left(Y_N-\mu\sqrt N,\frac{N^2/4-C_N}{N}\right)\ \Longrightarrow\ (\tau Z_1,s^2 Z_2^2),}
\tag{5}
\]
where \(Z_1,Z_2\) are independent standard normals. Consequently, centered shadow brightness is asymptotically Gaussian, the section-vertex deficit is asymptotically chi-square, and these geometrically linked fluctuations become **independent** despite the exact finite-dimensional constraint (2). The normalized deficit in (5) uses the real number \(N^2/4\); for odd \(N\) this differs by \(1/4\) from the greatest feasible integer vertex count, which is negligible after division by \(N\).

## Assumptions and scope

The simplex has the canonical side length \(\sqrt2\); scaling it changes shadow volumes but not the dimensionless variable \(Y_N\) or the section count. All sections are central, all projections are orthogonal, and both use one and the same Haar-uniform direction. The word generic means every normal coordinate is nonzero, an event of probability one. The finite-dimensional envelope is deterministic, and its equality classes refer to directions rather than positive-probability events. The weak convergence in (5) holds as the number of vertices \(N\to\infty\), not for a fixed simplex. No claim is made about nonregular simplices, noncentral sections, or projection onto a lower-dimensional subspace of arbitrary codimension.

## Proof

**1. Exact geometric coupling.** The simplex facet opposite \(e_i\) has \((N-2)\)-volume \(F_N=\sqrt{N-1}/(N-2)!\) and outward unit normal \(w_i=-\sqrt{N/(N-1)}(e_i-N^{-1}\mathbf1)\), in \(L_N\). Cauchy's projection formula for a polytope gives
\[
A_N=\frac12\sum_i F_N|\langle U,w_i\rangle|=\frac{F_N}2\sqrt{\frac N{N-1}}\sum_i|U_i|.
\]
An edge \([e_i,e_j]\) meets \(H_U\) in its relative interior if and only if \(U_iU_j<0\). Such crossings are precisely the vertices of the central section (their barycentric supports have exactly two elements). Thus \(C_N=p(N-p)\), proving (1) without any probabilistic approximation.

**2. Complete sharp range.** Put \(a=\sum_{U_i>0}U_i=-\sum_{U_j<0}U_j>0\). Since \(\|U\|_2=1\), Cauchy–Schwarz within each sign group yields
\[
1\ge a^2\left(\frac1p+\frac1q\right)=\frac{Na^2}{pq},
\]
with equality precisely when the entries within each sign group are all equal. Conversely, \(\sum_{U_i>0}U_i^2\le a^2\) and \(\sum_{U_j<0}U_j^2\le a^2\), so \(1\le2a^2\). The latter inequality is strict for \(N\ge3\) with all coordinates nonzero, since at least one sign class contains at least two entries. Because \(Y_N=2\sqrt{N/(N-1)}a\), these are the sharp upper and strict lower bounds in (2). A two-level vector attains the upper bound. To approach the lower bound with any prescribed split, assign one positive and one negative coordinate tending to \(+1/\sqrt2\) and \(-1/\sqrt2\), respectively, and let all other coordinates tend to zero while preserving their assigned signs and the zero-sum condition. The sign-constrained unit-sphere chamber is path connected: linearly interpolate any two vectors in its open convex cone, then renormalize. Continuity of \(Y_N\) shows that every intermediate value occurs. This also establishes the claimed equality class and the complete joint range.

**3. Exact moment calculation.** In the \(d=N-1\)-dimensional space \(L_N\), the unit facet normals satisfy \(\langle w_i,w_j\rangle=-1/d\) for \(i\ne j\). For a Haar-uniform unit direction in dimension \(d\),
\[
\mathbb E|\langle U,w_i\rangle|=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d+1)/2)},\qquad \mathbb E\langle U,w_i\rangle^2=\frac1d.
\]
For distinct unit vectors with inner product \(\rho\), writing a standard Gaussian as its independent radius and uniform direction gives
\[
\mathbb E\{|\langle U,v\rangle\langle U,w\rangle|\}=\frac2{\pi d}\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right).
\]
This last identity follows by integrating the absolute product of a correlated standard Gaussian pair. Substituting \(\rho=-1/d\), summing the \(N\) diagonal and \(N(N-1)\) off-diagonal terms of \(Y_N^2=(\sum_i|\langle U,w_i\rangle|)^2\), gives (3)–(4). Stirling's gamma-ratio expansion yields \(\operatorname{Var}(Y_N)\to1-3/\pi\), also recovered by the limit proof below.

**4. One Gaussian sample generates both observations.** Let \(G_1,\ldots,G_N\) be independent standard normal variables, put \(\bar G=N^{-1}\sum_iG_i\), and let \(S=(\sum_i(G_i-\bar G)^2)^{1/2}\). Then the vector \(U=((G_i-\bar G)/S)_i\) is Haar-uniform on the unit sphere of \(L_N\). Consequently, with \(K_N=\#\{i:G_i>\bar G\}\),
\[
C_N=K_N(N-K_N),\qquad Y_N=\sqrt{\frac N{N-1}}\frac{\sum_i|G_i-\bar G|}{S}.
\tag{6}
\]
These equalities hold jointly, not merely in their separate marginal distributions.

**5. The sign-count linearization.** Let \(\phi_0=1/\sqrt{2\pi}\), \(\mu=\sqrt{2/\pi}\), and define the odd function \(\psi(g)=\mathbf1_{\{g>0\}}-1/2-\phi_0g\). Then
\[
T_N:=\frac{K_N-N/2}{\sqrt N}=\frac1{\sqrt N}\sum_i\psi(G_i)+o_p(1).
\tag{7}
\]
One proof of the moving-threshold remainder uses \(\bar G=O_p(N^{-1/2})\). On \(|\bar G|\le M/\sqrt N\), place a deterministic grid of mesh \(N^{-3/4}\) on \([-M/\sqrt N,M/\sqrt N]\). A count between any grid point and zero has variance \(O_M(\sqrt N)\), while the number of grid points is \(O_M(N^{1/4})\). Chebyshev plus a union bound shows that the maximum centered count is \(o_p(\sqrt N)\). Monotonicity bounds the gaps between grid points by counts with expected size \(O(N^{1/4})\). The Gaussian cdf expansion \(\Phi(t)=1/2+\phi_0t+O(t^3)\) yields (7). Moreover
\[
\mathbb E\psi(G)=0,\qquad \operatorname{Var}(\psi(G))=\frac14-\frac1{2\pi}=s^2.
\]

**6. The shadow linearization and independence.** Let the even function \(\eta(g)=|g|-\mu-(\mu/2)(g^2-1)\). The elementary inequality
\[
\big||g-h|-|g|+h\operatorname{sgn}(g)\big|\le2|h|\mathbf1_{\{|g|\le|h|\}}
\]
with \(h=\bar G\), together with \(\#\{i:|G_i|\le|\bar G|\}=O_p(\sqrt N)\), shows \(\sum_i|G_i-\bar G|=\sum_i|G_i|+O_p(1)\). Similarly \(S^2=\sum_iG_i^2-N\bar G^2\), where \(N\bar G^2=O_p(1)\). First-order expansion of the quotient in (6) gives
\[
Y_N-\mu\sqrt N=\frac1{\sqrt N}\sum_i\eta(G_i)+o_p(1).
\tag{8}
\]
The Gaussian absolute moments \(\mathbb E|G|=\mu\), \(\mathbb E|G|^3=2\mu\), and \(\mathbb EG^4=3\) yield
\[
\operatorname{Var}(\eta(G))=1-3/\pi=\tau^2>0.
\]
Crucially, \(\psi\) is odd while \(\eta\) is even, so \(\mathbb E[\psi(G)\eta(G)]=0\). The ordinary bivariate iid central limit theorem applied to (7)–(8) gives independent centered Gaussian limits, with variances \(s^2,\tau^2\). Finally
\[
\frac{N^2/4-C_N}{N}=T_N^2
\]
identically. The continuous mapping theorem proves (5). Notice that the zero covariance used in this argument is for the **linearized Gaussian influence functions**; it is not a claim of finite-dimensional independence of the two geometric observables.

## Verification

The standalone checker `verify.py` requires Python with NumPy and SciPy, as listed in `requirements.txt`, and runs by `python verify.py`. Independent convex-hull reconstruction compares orthogonal shadow volumes against Cauchy's formula for 480 generic directions in dimensions \(N=3,4,5,6\); it also explicitly constructs every crossed-edge intersection and verifies its section-vertex count. For all \(3\le N\le19\) and every sign split, it constructs the exact two-level upper extremizer and positive/negative near-degenerate directions approaching the lower infimum. Additional random directions test the deterministic envelope. Independent one-dimensional numerical integration checks the correlated-Gaussian absolute-product formula for five correlations. For \(N=3,4,8,20,100\), independent random samples of 40,000 Haar directions each check the exact first and second moments. Samples of 50,000 directions each at \(N=300,1000\) diagnose the two limiting variances and the vanishing correlation. A successful reproduction prints `ALL_SIMPLEX_SECTION_SHADOW_CHECKS_PASSED`. Finite experiments do not prove a weak limit; Steps 4–6 do.

## Relationship to prior work

The brightness function and its relationship to a convex hull function are studied by Horváth and Lángi [1]; their Lemma 1 covers arbitrary convex bodies but does not connect the brightness of a regular simplex to the vertices of its simultaneous central section. Kabluchko, Litvak, and Zaporozhets [2] give the Gaussian limit for a **one-dimensional** random shadow of a high-dimensional cube, alongside separate random-width results for simplices. That established Gaussian variance coincides with \(\tau^2\) here, but it is a different geometric observable and neither provides the complete feasible section–shadow domain (2) nor the same-hyperplane independent joint limit (5). König [3] treats extremal hyperplane-section volumes, not the joint section vertex count and perpendicular shadow volume. Affentranger and Schneider [4] establish expected face counts of random **projections** of regular simplices, not the present coupled section–shadow statistic; the complete text was not accessible for inspection.

Two previously published geometric notes [5,6] already establish the signed-Gaussian reduction, expected vertex count, and chi-square limits for the central section's face vector. Those components are credited, not asserted as new. The result here is instead the complete sharp **simultaneous** feasibility interval for vertex complexity and perpendicular brightness, the exact shadow moments, and the joint asymptotic independence under a *single common normal*. Neither the published section-only statements nor the cited brightness-only statements assert those combined claims. Known Cauchy–Schwarz and central limit principles are tools, not independent claims of novelty. Historical priority remains provisional, particularly for older stereological literature involving simultaneous sections and projections.

## Limitations

The result applies only to regular simplices and uniform centroidal orientations. The lower endpoint is an infimum approached by nongeneric limiting normals, not an attainable generic shadow. The chi-square/Gaussian independence is asymptotic, not a finite-dimensional factorization. No local limit theorem, quantitative convergence rate, conditional density formula, or extension to nonregular polytopes is claimed. Some older projection literature could only be checked from abstracts; no conclusion of total literature uniqueness follows from database searches alone. Independent mathematical audit has not been performed.

## References

[1] Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, arXiv:2012.08955, first posted 2020-12-16; https://arxiv.org/abs/2012.08955 ; full open-access journal text https://doi.org/10.1007/s10711-022-00673-y .

[2] Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first posted 2015-11-26; https://arxiv.org/abs/1511.08479 .

[3] H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743, first posted 2020-02-25; https://arxiv.org/abs/2002.10743 .

[4] F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete Comput. Geom. 7 (1992), 219–226; https://doi.org/10.1007/BF02187839 .

[5] *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, public mathematical research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90 .

[6] *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, public mathematical research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e .
