# Sharp upper-distance tails at the tip–rim transition of a finite flat cone

## Finding

Let \(C_{\ell,c}\) be the lateral surface of a right circular cone, including its tip and rim but **excluding the base disk**, with slant length \(\ell>0\) and base radius \(c\ell\), where \(0<c<1\). Equip this compact surface with its intrinsic shortest-path metric, and choose \(X,Y\) independently from normalized intrinsic area. Write \(D_c=d(X,Y)/\ell\). The developed cone has total angle \(2\pi c\). For the limiting value \(c=1\), let \(C_{\ell,1}\) mean the flat Euclidean disk of radius \(\ell\), sampled uniformly by area.

Put \(s_c=\sin(\pi c/2)\), \(b_c=\cos(\pi c/2)\), and \(M_c=\max\{1,2s_c\}\). The sharp near-diameter probability obeys

\[
\Pr(D_c>M_c-\varepsilon)\sim
\begin{cases}
\displaystyle\frac{4\tan(\pi c)}{3\pi c}\,\varepsilon^3,&0<c<1/3,\\[5pt]
\displaystyle\frac{28}{\pi\sqrt3}\,\varepsilon^3,&c=1/3,\\[5pt]
\displaystyle\frac{2}{3\pi c\,b_c\,s_c^2}\,\varepsilon^3,&1/3<c<1,\\[5pt]
\displaystyle\frac{32}{15\pi}\,\varepsilon^{5/2},&c=1.
\end{cases}
\]

All constants are positive and are limits of the probability divided by the displayed power. The first threshold is the developed total angle \(2\pi/3\), **not** a physical apex angle of \(2\pi/3\). The third regime describes strictly positive cone height; the last is a separate flat-disk limit. At the critical shape two geometrically disjoint kinds of maximizers contribute additively, producing the sum \(28/(\pi\sqrt3)\).

The geometric diameter formula \(\operatorname{diam}(C_{\ell,c})=\ell M_c\), the intrinsic point-pair second moment and its stochastic ordering with cone angle were previously obtained and **are not claimed here as new**. Their role is to locate the relevant upper endpoints. The new asserted result is the complete sharp upper-tail classification above, with exact coefficients including the critical case.

## Assumptions and scope

The surface is the lateral cone **only**. Distances are intrinsic geodesic lengths, not ambient Euclidean chord lengths or paths permitted through the base disk. Area sampling includes neither an atom at the tip nor one at the rim. In the main three cone regimes \(c\) is held fixed as \(\varepsilon\downarrow0\); the asymptotic is not asserted to be uniform as \(c\) approaches \(1/3\) or \(1\). Scaling by \(\ell\) is essential: the unnormalized tail is obtained by replacing \(\varepsilon\) with \(\varepsilon/\ell\).

The physical half-apex angle is \(\arcsin c\). Choose slant-polar coordinates \((r,\vartheta)\) with \(0\le r\le1\), \(\vartheta\in\mathbb R/(2\pi\mathbb Z)\) after normalizing \(\ell=1\). The intrinsic metric and area density are

\[
 ds^2=dr^2+c^2r^2d\vartheta^2,\qquad dA=c\,r\,dr\,d\vartheta.
\]

For independent normalized-area points, the slant radii \(R_1,R_2\) are independent, each with density \(2r\) on \([0,1]\). Their shorter azimuthal separation \(\Theta\) is independent and uniform on \([0,\pi]\). Unfolding the developed circular sector gives the exact distance formula

\[
 D_c=\sqrt{R_1^2+R_2^2-2R_1R_2\cos(c\Theta)}.
\]

This metric representation is standard background; only the **new tail consequences** are asserted as discoveries.

## Proof

**Step 1 — identify all diameter-producing pairs.** The displayed squared distance is a convex quadratic function of the two radii for each fixed angle. Its maximum on the radial unit square must occur at a corner. Since the distance is nondecreasing in \(\Theta\), the only possible maximal pair types are (i) tip–rim, of length \(1\), and (ii) two opposite rim points (azimuthal separation \(\pi\)), of length \(2\sin(\pi c/2)\). Consequently the known diameter is \(M_c\). For \(0<c<1/3\), only tip–rim pairs maximize; for \(1/3<c\le1\), only opposite rim pairs maximize; and for \(c=1/3\), **both types** maximize. Apart from their rotational orbits and the sample swap, these are all maxima. Compactness allows the near-diameter event to be localized to arbitrarily small neighborhoods of these sets.

**Step 2 — tip–rim contribution.** Fix \(0<c\le1/3\). In either of the two symmetric ordered configurations write \(R_1=u\), \(R_2=1-v\), with \(u,v\ge0\) small, and leave \(\Theta=\theta\in[0,\pi]\). Uniformly in \(\theta\),

\[
 D_c=1-v-u\cos(c\theta)+O(u^2+uv+v^2).
\]

The positivity \(\cos(c\theta)\ge\cos(\pi c)\ge1/2\) implies that for \(D_c>1-\varepsilon\) both \(u,v=O(\varepsilon)\), uniformly in angle. The normalized joint density, including the two swaps, is \(8u(1-v)\,du\,dv\,d\theta/\pi\). Rescale \(u=\varepsilon U\), \(v=\varepsilon V\), apply dominated convergence on uniformly bounded rescaled domains, and obtain

\[
 \lim_{\varepsilon\downarrow0}\varepsilon^{-3}\Pr(\text{tip--rim contribution})
 =\frac8\pi\int_0^\pi\int_{U,V\ge0,\ V+U\cos(c\theta)<1}U\,dU\,dV\,d\theta
 =\frac4{3\pi c}\tan(\pi c).
\]

The last equality uses \(\int_0^{1/q}U(1-qU)\,dU=1/(6q^2)\) for \(q>0\).

**Step 3 — opposite-rim contribution for \(1/3\le c<1\).** Write \(R_1=1-u\), \(R_2=1-v\), \(\Theta=\pi-\delta\) near the other maximizing orbit. With \(s_c=\sin(\pi c/2)>0\) and \(b_c=\cos(\pi c/2)>0\), Taylor expansion gives

\[
 D_c=2s_c-s_c(u+v)-c b_c\delta+O((u+v+\delta)^2).
\]

All three linear coefficients are strictly positive, so the near-maximal set has \(u,v,\delta=O(\varepsilon)\). Its joint density tends to \(4\,du\,dv\,d\delta/\pi\), since \(R_1,R_2\) each have density \(2r\) and \(\Theta\) density \(1/\pi\). Rescaling and integrating over a three-dimensional simplex yields

\[
 \lim_{\varepsilon\downarrow0}\varepsilon^{-3}\Pr(\text{opposite-rim contribution})
 =\frac4\pi\int_{u,v,\delta\ge0,\ s_c(u+v)+cb_c\delta<1}du\,dv\,d\delta
 =\frac{2}{3\pi c\,b_c\,s_c^2}.
\]

For \(c>1/3\) this is the entire tail. At \(c=1/3\), the two maximizing orbits are disjoint; by localization their contributions add. Step 2 yields \(4\sqrt3/\pi\), and Step 3 gives \(16/(\pi\sqrt3)\), totaling \(28/(\pi\sqrt3)\).

**Step 4 — flat disk.** At \(c=1\), the first angular derivative at opposite rim points vanishes; a linear \(\delta\) approximation is invalid. Instead,

\[
 D_1=2-(u+v)-\frac{\delta^2}{4}
 +O((u+v)^2+(u+v)\delta^2+\delta^4).
\]

Now \(u,v=O(\varepsilon)\) but \(\delta=O(\sqrt\varepsilon)\). Dominated convergence after the anisotropic rescaling gives

\[
 \begin{aligned}
 \lim_{\varepsilon\downarrow0}\varepsilon^{-5/2}\Pr(D_1>2-\varepsilon)
 &=\frac4\pi\int_{0}^{2}\frac12\left(1-\frac{w^2}{4}\right)^2dw\\
 &=\frac{32}{15\pi}.
 \end{aligned}
\]

No other near-maximal configurations contribute by Step 1. All four regimes follow.

## Verification

The supplied file `cone_verifier.py` uses only Python's standard library and computes independently normalized two-dimensional quadratures of the conditional radius integrals in localized maximizing neighborhoods. At cone parameters \(c=0.12,0.24,1/3,0.4,0.65,0.92,1\) and three decreasing positive thresholds, the measured probability ratios approach the claimed coefficients. The smallest tested threshold yields relative error below \(0.7\%\) in every tested regime. Independent tensor quadrature confirms the known exact second moment as a check of sampling normalization. Grid tests verify the two diameter candidates at representative angles. In total 67 numerical consistency comparisons pass. Execute with `python cone_verifier.py` (Python 3.9 or newer; no third-party packages).

The analytical proof above establishes the infinite family; numerical evaluations do not prove limiting equalities or historical originality.

## Relationship to prior work

The standard unfolded-sector cone-distance formula, the exact cone diameter \(\ell\max\{1,2\sin(\pi c/2)\}\), and the cone's two-point squared-distance moment and angle coupling are known and not claimed new. The previously established global-center law for finite cones also reports that diameter formula. This finding instead resolves the **distribution's extreme tail** for every fixed cone angle, identifies the second maximizing orbit exactly at the transition, and records its additive critical coefficient and the disk's different exponent.

For context, Gell-Redman studies harmonic maps with conic singularities; the results examined concern variational maps, not random distances. Bäsel derives random two-point Euclidean distance laws in planar triangles; the inspected equations concern planar domains, not intrinsic distances on identified cone sectors. A 2016 discussion explicitly derives the opposite-rim geodesic on a circular cone; that is partial geometric input and does not yield the four-regime random-pair tail. General published distance-distribution methods for Euclidean compact sets do not directly imply a law for intrinsic conical geodesics. These comparisons do **not** prove worldwide historical uniqueness.

## Limitations

The result assumes area-uniform independent sampling, an exact right circular lateral cone, and fixed shape as the distance deficit tends to zero. It excludes weighted sampling, cone bases, conical frusta, other surfaces of revolution, and simultaneous limits \(\varepsilon\to0\) with \(c\to1/3\) or \(c\to1\). No new claim is made about the standard cone metric, its diameter, its squared-distance moment, or its monotone angle coupling. The literature search did not exhaust every historical source, so the originality claim is conditional on the checked literature and accessible records.

## References

1. J. Gell-Redman, *Harmonic Maps of Conic Surfaces With Cone Angles Less Than \(2\pi\)*, arXiv:1010.4156, first posted 2010-10-20. https://arxiv.org/html/1010.4156v2
2. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle*, arXiv:1208.6228, first posted 2012-08-30. https://arxiv.org/abs/1208.6228
3. F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first posted 2013-11-29. https://arxiv.org/abs/1312.2498
4. B. Berentsen, J. D'Aurizio et al., *Geodesic on a right circular cone problem*, discussion first posted 2016-08-19; antipodal rim length explicitly obtained. https://math.stackexchange.com/questions/1897144/geodesic-on-a-right-circular-cone-problem/2061892
