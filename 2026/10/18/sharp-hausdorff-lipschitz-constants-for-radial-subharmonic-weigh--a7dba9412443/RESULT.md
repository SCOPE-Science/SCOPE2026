# Sharp Hausdorff Lipschitz constants for radial-subharmonic weighted perimeters

## Finding
Fix an integer \(n\ge2\). Let \(\phi:[0,\infty)\to[0,\infty)\) be continuous, nondecreasing, and twice continuously differentiable on \((0,\infty)\), with \(\lim_{r\downarrow0}r^{n-1}\phi'(r)=0\) and with \(r\mapsto r^{n-1}\phi'(r)\) nondecreasing. Equivalently the radial function \(f(x)=\phi(|x|)\) has nonnegative distributional Laplacian and no point mass at the origin. Write \(B\) for the Euclidean unit ball, \(\omega_n=\operatorname{vol}_n(B)\), and
\[
\mathcal P_\phi(K)=\eta_K\int_{\partial K}\phi(|x|)\,d\mathcal H^{n-1}(x),\qquad
\eta_K=\begin{cases}1,&\dim K=n,\\2,&\dim K<n.\end{cases}
\]
The factor two is the usual boundary-multiplicity convention for degenerate convex bodies. Let \(G(R)=n\omega_n R^{n-1}\phi(R)\).

**Sharp outer-parallel increment.** Every nonempty compact convex \(K\) satisfying \(0\in K\subseteq RB\), every \(R>0\), and every \(t\ge0\) satisfy
\[
0\le \mathcal P_\phi(K+tB)-\mathcal P_\phi(K)
\le G(R+t)-G(R). \tag{1}
\]
Furthermore, writing \(f(x)=\phi(|x|)\), the deficit obeys the explicit nonnegative bound
\[
\begin{split}
&G(R+t)-G(R)-\bigl(\mathcal P_\phi(K+tB)-\mathcal P_\phi(K)\bigr)\\
&\hspace{1cm}\ge \int_0^t\int_{(R+s)B\setminus(K+sB)}\Delta f(x)\,dx\,ds. \tag{2}
\end{split}
\]
If \(\Delta f>0\) almost everywhere away from the origin, inequality (1) is strict for every \(t>0\) unless \(K=RB\).

**Exact global Hausdorff modulus.** For any two such sets \(K,L\subseteq RB\) containing the origin,
\[
\boxed{\ \bigl|\mathcal P_\phi(K)-\mathcal P_\phi(L)\bigr|
\le n\omega_n\bigl((n-1)R^{n-2}\phi(R)+R^{n-1}\phi'(R)\bigr)d_H(K,L).\ }\tag{3}
\]
The coefficient in (3) is the **smallest possible** constant valid for all such pairs: balls of radii \(R\) and \(R-\varepsilon\) approach equality as \(\varepsilon\downarrow0\). In particular, for every \(p>0\), the radial power weight \(\phi(r)=r^p\) has the exact coefficient
\[
\boxed{\ n\omega_n(n-1+p)R^{n-2+p}.\ }\tag{4}
\]
This includes \(0<p<1\), where the weight gradient is singular at the origin, as well as smooth radial moments. The constant weight \(\phi\equiv1\) recovers the classical sharp surface-area coefficient \(n(n-1)\omega_nR^{n-2}\).

## Assumptions and scope
The ambient Euclidean distance determines \(d_H\), and the containing ball and the radial weight share the fixed origin. Full-dimensional and degenerate convex bodies are both allowed. For a set of dimension below \(n-1\), its weighted perimeter is zero. The derivative \(\phi'(R)\) exists for every \(R>0\) by the regularity assumption. Distributional subharmonicity is exactly \((r^{n-1}\phi'(r))'\ge0\) away from the origin, together with the stated vanishing flux at zero; it guarantees \(\Delta f\in L^1_{\mathrm{loc}}\). No homogeneity of the weight is assumed. The sign and monotonicity conditions permit comparison of origin-containing convex bodies by inclusion.

## Proof
**1. Smooth parallel variation.** Initially let \(K\) be smooth, strictly convex and contain the origin in its interior, and set \(K_s=K+sB\). Write \(H_s\) for the sum of its \(n-1\) principal curvatures and \(\nu\) for its exterior normal. The normal-speed-one first variation is
\[
\frac{d}{ds}\mathcal P_\phi(K_s)
=\int_{\partial K_s}\!H_s\phi(|x|)\,dS
+\int_{\partial K_s}\!\nabla f(x)\cdot\nu(x)\,dS
=\int_{\partial K_s}\!H_s\phi(|x|)\,dS
+\int_{K_s}\!\Delta f(x)\,dx. \tag{5}
\]
The last equality is the divergence theorem. For possibly nonsmooth \(f\) at the origin, apply it on the body with a small central ball deleted and let its radius vanish: the inner boundary flux is \(n\omega_n r^{n-1}\phi'(r)\to0\). The subharmonicity assumption makes both integrals well-defined and nonnegative.

**2. The sharp ball domination.** If \(K_s\subseteq (R+s)B\), then \(\Delta f\ge0\) and the divergence theorem on a ball give
\[
\int_{K_s}\Delta f\,dx\le\int_{(R+s)B}\Delta f\,dx
=n\omega_n(R+s)^{n-1}\phi'(R+s).\tag{6}
\]
Curvature is nonnegative on a smooth convex hypersurface, and the standard Steiner/coefficient identity and monotonicity of the second quermassintegral give
\[
\int_{\partial K_s}H_s\phi(|x|)\,dS
\le \phi(R+s)\,n(n-1)W_2(K_s)
\le \phi(R+s)\,n(n-1)\omega_n(R+s)^{n-2}.\tag{7}
\]
Combining (5)--(7) bounds the derivative by \(G'(R+s)\), the derivative of the weighted perimeter of the radius-\(R+s\) ball. Integration proves the upper inequality in (1). Retaining the nonnegative difference between the two sides of (6), rather than discarding it, and then integrating proves (2). The lower inequality in (1) follows from the established inclusion monotonicity of nonnegative nondecreasing radial weighted perimeters when the smaller body contains the origin.

**3. General compact convex sets and strictness.** Approximate \(K\) by smooth strictly convex bodies \(K_j\), with \(0\in\operatorname{int} K_j\), \(K_j\to K\) in Hausdorff distance, and \(K_j\subseteq(R+o(1))B\). Such approximants follow from support-function regularization plus addition of a vanishing Euclidean ball. Qualitative continuity of the multiplicity-corrected weighted perimeter supplies convergence both at \(K_j\) and at \(K_j+tB\). Since \(\Delta f\) is locally integrable, characteristic functions of the parallel bodies converge almost everywhere and the deficit integrals converge by dominated convergence. Hence (1)--(2) hold also for segments, flats and points. If \(K\ne RB\), then \(K+sB\) is a proper subset of \((R+s)B\) with a positive-volume difference for every \(s\ge0\). Positivity of \(\Delta f\) almost everywhere makes the right side of (2) strictly positive for \(t>0\).

**4. Global Hausdorff estimate by infinitesimal chaining.** Let \(\delta=d_H(K,L)\) and let \(K_u=(1-u)K+uL\), \(0\le u\le1\). Every \(K_u\) contains the origin and lies in \(RB\). Support functions give \(d_H(K_u,K_v)=|u-v|\delta\). Inclusion, the radial-weight monotonicity theorem, and (1) show for \(v>u\), with \(h=(v-u)\delta\),
\[
|\mathcal P_\phi(K_v)-\mathcal P_\phi(K_u)|\le G(R+h)-G(R).\tag{8}
\]
Partition \([0,1]\) into \(N\) equal subintervals. Sum (8) and let \(N\to\infty\):
\[
|\mathcal P_\phi(L)-\mathcal P_\phi(K)|\le
\lim_{N\to\infty}N\bigl(G(R+\delta/N)-G(R)\bigr)=G'(R)\delta.
\]
For concentric balls \(K=RB\) and \(L=(R-\varepsilon)B\), the ratio of the perimeter difference to \(d_H(K,L)=\varepsilon\) tends to \(G'(R)\). Thus the optimal constant is exactly that displayed in (3).

**5. Power case.** With \(\phi(r)=r^p\) and \(p>0\), one has \(\Delta f(x)=p(n+p-2)|x|^{p-2}>0\) for \(x\ne0\), and \(r^{n-1}\phi'(r)=pr^{n+p-2}\to0\). Substitution into (3) proves (4) and the strict parallel-increment assertion, including the potentially singular-gradient interval \(0<p<1\).

## Verification
A standalone standard-library program `CHECKS.py` exercises the exact disk/ball derivatives, confirms the factor-two boundary normalization as a planar rectangle shrinks to a segment, and independently integrates the squared-radius perimeter of Euclidean rectangles and their outer parallel bodies. It checks the exact rectangle formula against the inequality and verifies that the ball comparison is strict for proper rectangles. The computation is auxiliary: all-dimensional statements and the treatment of singular derivatives are proved by (5)--(8), not inferred from finite tests. Run with `python3 CHECKS.py`.

## Relationship to prior work
Csató, Giovagnoli and Roy (arXiv:2608.19851v1) introduced the recent weighted-perimeter variational questions and the multiplicity-two convention and stated qualitative continuity and origin-anchored inclusion monotonicity. Csató and Giovagnoli (arXiv:2610.11677v1) proved those properties in full generality, but did not give a sharp Hausdorff coefficient or outer-parallel increment inequality. A published 2026 planar note, *Sharp Hausdorff regularity exponents of planar radial weighted perimeters*, gives a dimension-two Lipschitz bound for positive powers with coefficients \(2\pi(1+\max\{1,p\})R^p\), explicitly not asserting their optimality. Its coefficient already matches (4) in dimension two for \(p\ge1\), and this covered part is **not independently claimed**. The new claims are the sharp general radial-subharmonic formulation, its all-dimensional and strict parallel-body comparison, and notably the missing optimal positive-power coefficient for \(0<p<1\). Hug and Schneider (arXiv:1310.1514v1) treat bounded-Lipschitz control of support measures, rather than this weighted sharp global inequality. Classical Steiner and quermassintegral facts are used as established inputs.

## Limitations
The common origin constraint and radial subharmonicity are substantive; dropping them may invalidate (1)--(3). The coefficient is sharp as a global supremum approached by close concentric balls, not generally attained for two distinct bodies at positive Hausdorff separation. The theorem does not concern arbitrary nonradial or nonmonotone weights, negative radial powers, or nonconvex sets. The existing 2026 planar positive-power exponent result is not claimed to be new, nor is the classical unweighted case. An unindexed equivalent formulation in curvature-measure literature is a remaining bibliographic risk. No independent scientific audit has been performed.

## References
1. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, first public 2026-08-20, https://arxiv.org/abs/2608.19851 .
2. G. Csató, D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, first public 2026-10-08, https://arxiv.org/abs/2610.11677 .
3. *Sharp Hausdorff regularity exponents of planar radial weighted perimeters*, published mathematical note, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-hausdorff-regularity-exponents-of-planar-radial-weighted-p--840cdd1da1ee/RESULT.md .
4. D. Hug, R. Schneider, *Hölder continuity of normal cycles and of support measures of convex bodies*, arXiv:1310.1514v1, 2013-10-05, https://arxiv.org/abs/1310.1514 .
5. G. Saracco, G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770v1, https://arxiv.org/abs/2306.07770 .
