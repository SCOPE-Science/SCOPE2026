# Circumvertex tangent sections govern extreme Haar central chords of convex polytopes

## Finding
Let \(d\ge2\), and let \(K=-K\subset\mathbb R^d\) be a full-dimensional convex polytope with the origin in its interior. Write
\[
R=\max_{x\in K}\|x\|_2,\qquad
\mathcal V_R=\{v\in\operatorname{vert}(K):\|v\|_2=R\},
\qquad u_v=v/R.
\]
For each \(v\in\mathcal V_R\), its polyhedral tangent cone is
\[
T_vK=\{z\in\mathbb R^d:\text{there exists }s>0\text{ with }v+sz\in K\}.
\]
Set
\[
S_v=\{w\in u_v^\perp:w-u_v\in T_vK\}.
\]
Every \(S_v\) is a compact \((d-1)\)-dimensional convex polytope with positive \((d-1)\)-volume. Let \(U\) be uniform on \(S^{d-1}\) and let \(L=\mathcal H^1(K\cap\mathbb RU)\) be the length of the center-passing chord. With \(\sigma_{d-1}=\mathcal H^{d-1}(S^{d-1})=2\pi^{d/2}/\Gamma(d/2)\),
\[
\boxed{
\mathbb P\{L>2R-\varepsilon\}
=C_K\varepsilon^{d-1}+O_K(\varepsilon^d),\qquad
C_K=\frac{\displaystyle\sum_{v\in\mathcal V_R}\operatorname{vol}_{d-1}(S_v)}{2^{d-1}R^{d-1}\sigma_{d-1}}>0.
}
\]
Thus **only the tangent cones at the farthest vertices determine the leading upper tail**; the exponent \(d-1\) is universal for origin-symmetric full-dimensional polytopes.

For the orthotope \(K=\prod_{i=1}^d[-a_i,a_i]\), with all \(a_i>0\) and \(R=(\sum_i a_i^2)^{1/2}\), the formula specializes in every dimension to
\[
\boxed{C_K=\frac{2R}{(d-1)!\,\sigma_{d-1}\prod_{i=1}^d a_i}.}
\]
For the Euclidean \(\ell_1\)-unit cross-polytope \(K=\{x:\sum_i|x_i|\le1\}\), it gives
\[
\boxed{C_K=\frac{2d}{(d-1)!\,\sigma_{d-1}}.}
\]
Both families have exactly the stated remainder order for each fixed dimension and set of parameters.

## Assumptions and scope
The Euclidean norm, ambient Euclidean \((d-1)\)-dimensional measures, and Haar-uniform direction on the unit sphere are fixed. Because \(K=-K\), \(K\cap\mathbb RU\) is an interval of length \(2\rho_K(U)\), where \(\rho_K(U)=\max\{r\ge0: rU\in K\}\). The chord is required to **pass through the origin**; no random offset is used. The finite vertex set \(\mathcal V_R\) includes each positive and negative circumvertex separately, so their spherical neighborhoods are counted separately before dividing by total sphere area. The implied constant in \(O_K\) can depend on the fixed polytope, dimension and vertex geometry.

If \(K=\{x:a_j\cdot x\le b_j,\;1\le j\le m\}\) is an irredundant facet representation (with \(b_j>0\)) and \(I_v=\{j:a_j\cdot v=b_j\}\), then \(S_v\) is explicitly computable by the finite linear inequalities
\[
S_v=\{w\in\mathbb R^d:w\cdot u_v=0,\ a_j\cdot w\le a_j\cdot u_v\ \text{for all }j\in I_v\}.
\]
No smoothness, simplicity of vertices, or generic position is assumed.

## Proof
**1. Isolated farthest directions.** By strict convexity of the Euclidean squared norm on every nontrivial segment, a maximum of \(\|x\|_2\) on a polytope is attained only at its vertices. Therefore the full set of points of \(K\) at Euclidean distance \(R\) from the origin is exactly \(\mathcal V_R\). In particular, \(\rho_K(U)=R\) holds only for the finitely many directions \(u_v\). Compactness and continuity show that, as \(\varepsilon\downarrow0\), the event \(\rho_K(U)>R-\varepsilon/2\) lies in disjoint fixed neighborhoods of these directions.

For a farthest vertex \(v\), the functional \(x\mapsto u_v\cdot x\) attains its unique maximum \(R\) at \(v\). Indeed, \(u_v\cdot x\le\|x\|_2\le R\), with equality only if \(x=v\). As the polytope has finitely many vertices, \(u_v\) lies in the **interior** of the normal cone at \(v\). Equivalently, there exists \(c_v>0\) such that
\[
-u_v\cdot z\ge c_v\|z\|_2\quad\text{for all }z\in T_vK.
\]
This also shows that \(S_v\) is bounded: for \(w\in S_v\), apply the inequality to \(z=w-u_v\) to obtain \(1\ge c_v\|w-u_v\|_2\). It has nonempty relative interior because \(-u_v\in\operatorname{int}T_vK\), as the segment from \(v\) toward the interior point \(0\) enters the interior of \(K\). Closedness follows from the finite facet inequalities. Hence its \((d-1)\)-volume is finite and positive.

**2. Angular localization is linear in radial deficiency.** Put \(\delta=\varepsilon/2\) and \(x=\rho_K(U)U\in K\) for a direction with \(\rho_K(U)>R-\delta\). If \(U\) is near \(u_v\), set \(\alpha=\|U-u_v\|_2\). Because \(x-v\in T_vK\), the preceding strict support inequality yields
\[
c_v\|x-v\|_2\le R-u_v\cdot x\le\delta+\frac R2\alpha^2,
\qquad \|x-v\|_2\ge R\alpha-\delta.
\]
For sufficiently small fixed neighborhood radius \(\alpha\), the quadratic term can be absorbed, giving \(\alpha\le C_v\delta\). Thus only angular neighborhoods of size proportional to \(\delta\) contribute, with no assumption that vertices are simple.

**3. Tangent-cone blow-up.** On the sphere near \(u_v\), use the gnomonic coordinates
\[
U_\delta(w)=\frac{u_v+(\delta/R)w}{\sqrt{1+(\delta/R)^2\|w\|_2^2}},\qquad w\in u_v^\perp.
\]
Step 2 bounds the relevant \(w\) uniformly as \(\delta\to0\). By symmetry, the tail event is exactly
\[
\{(R-\delta)U\in K\},
\]
and uniformly on bounded \(w\)-sets,
\[
(R-\delta)U_\delta(w)
=v+\delta(w-u_v)+O_K(\delta^2).
\]
At \(v\), the inactive facet inequalities have positive slack and impose no restriction when \(\delta\) is small. Each active facet becomes
\[
a_j\cdot(w-u_v)\le O_K(\delta),\qquad j\in I_v.
\]
The unperturbed feasible set is precisely \(S_v\). On a common bounded \(w\)-domain, membership in the perturbed set can differ from membership in \(S_v\) only in finitely many thickness-\(O_K(\delta)\) slabs around its nontrivial facet hyperplanes. Such slabs have total \((d-1)\)-volume \(O_K(\delta)\). It follows that the permissible \(w\)-set has volume
\[
\operatorname{vol}_{d-1}(S_v)+O_K(\delta).
\]

**4. Spherical measure.** The spherical area element under this gnomonic chart is
\[
d\mathcal H^{d-1}(U_\delta(w))
=\left(\frac\delta R\right)^{d-1}
\left(1+(\delta/R)^2\|w\|_2^2\right)^{-d/2}
\,dw.
\]
The Jacobian factor in parentheses is \(1+O_K(\delta^2)\) on the bounded relevant domain. Hence the spherical measure contributed by the neighborhood of \(u_v\) is
\[
\left(\frac\delta R\right)^{d-1}
\operatorname{vol}_{d-1}(S_v)+O_K(\delta^d).
\]
Summing over all disjoint circumvertex neighborhoods, dividing by \(\sigma_{d-1}\), and substituting \(\delta=\varepsilon/2\) establishes the claimed coefficient and remainder. The boundary of the event has spherical area zero for every sufficiently small positive \(\varepsilon\), so strict versus non-strict inequalities do not change the probabilities.

**5. Explicit examples.** For an orthotope, each circumvertex has coordinates \(v_i=\pm a_i\). In tangent coordinates the set \(S_v\) is a simplex, with its \(d\) vertices obtained by keeping all but one coordinate of \(w\) equal to the corresponding coordinate of \(u_v\). The edge Gram determinant equals \(R^{2d}/\prod_i a_i^2\), so
\[
\operatorname{vol}_{d-1}(S_v)
=\frac{R^d}{(d-1)!\prod_i a_i}.
\]
There are \(2^d\) such vertices. In the cross-polytope, \(R=1\), its \(2d\) circumvertices are \(\pm e_i\), and each \(S_v\) is the unit \((d-1)\)-dimensional \(\ell_1\) ball, with volume \(2^{d-1}/(d-1)!\). Substitution completes both calculations.

## Verification
The companion standard-library Python script `verify.py` tests exact circular-arc probabilities of planar rectangle chords, independently computes the three-dimensional cross-polytope spherical-tail probability by deterministic quadrature, checks the Gram determinants for orthotope tangent sections in dimensions two through seven, and compares the planar regular-even-polygon chord quantile with the general endpoint coefficient. Invoke `python verify.py` in the same folder. It terminates with `VERIFY_OK` if all assertions pass. These are finite consistency checks; the universal quantifiers and remainder estimates follow from the preceding proof.

The orthotope specialization in dimension three recovers the independently known box-endpoint coefficient \(R/(4\pi a_1a_2a_3)\). For the unit regular octahedron, the formula yields \(C_K=3/(4\pi)\), a second independent check of the normalization and counting of antipodal vertices.

## Relationship to prior work
Guédon, Litvak, Tatarko and Vritsiou (2026) analyze radii and diameters of Haar-random sections of arbitrary convex bodies via general bounds and high-dimensional problems. A Haar-random one-dimensional central section is included in their setting, but their investigated estimates do not state the polytope-specific exact upper-tail coefficient or the universal vertex-cone asymptotic above. The primary manuscript's introduction, theorems, and relevant section framework were inspected.

Published results for regular-polygon **central** chord laws give exact distributional formulas for one special planar class, but no arbitrary-polytope tangent-section identity. The exact central-chord distribution for three-dimensional orthotopes determines its special endpoint coefficient and is a covered corollary here, not a separately new assertion. Results concerning random hyperplane-section diameters of the cross-polytope sample a different Grassmannian and do not imply the one-dimensional chord tail. Bäsel (2012) and Harutyunyan–Ohanyan (2009) treat lines with randomized **offsets**, whose distributions do not determine the center-constrained conditional law. These distinctions are comparisons of mathematical statements, not merely of terminology.

## Limitations
The theorem requires an origin-symmetric, full-dimensional **polytope**, not a smooth convex body. It concerns the upper endpoint only; it does not provide the complete chord-length distribution for arbitrary polytopes. The geometry of the non-maximal vertices influences lower levels but not this coefficient. The remainder is for a fixed body and is not uniform over degenerating families of polytopes. The numerical script cannot establish infinite-dimensional, exhaustive, or historical priority statements. Older or unindexed integral-geometric treatments of spherical radial levels might contain equivalent general conclusions; no claim of exhaustive literature coverage is made. Independent validation has not been performed.

## References
1. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first publicly posted 21 September 2026, https://arxiv.org/abs/2609.24131. Primary MSC2020: 52A23.
2. Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (2012), https://arxiv.org/abs/1204.2707.
3. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability 41 (2009), 358–366, DOI: 10.1239/aap/1246886615.
4. *Parity-resolved central-chord laws for regular polygons*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-resolved-central-chord-laws-for-regular-polygons--de9bb055a653.
5. *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-diameter-law-and-exponential-endpoint-fluctuations-for-ran--72b090c504e9.
