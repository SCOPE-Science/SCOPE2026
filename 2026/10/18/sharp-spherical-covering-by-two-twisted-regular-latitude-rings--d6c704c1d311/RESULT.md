# Sharp spherical covering by two twisted regular latitude rings

## Finding
Fix any integer \(n\ge3\). On the unit sphere \(S^2\), take the \(2n\) sites
\[
 v_k^+=(r\cos(2\pi k/n),r\sin(2\pi k/n),h),\qquad
 v_k^-=(r\cos(\delta+2\pi k/n),r\sin(\delta+2\pi k/n),-h),
\]
for \(k=0,\ldots,n-1\), where \(0<h<1\), \(r=\sqrt{1-h^2}\), and \(0\le\delta\le 2\pi/n\). Let \(\rho(n,h,\delta)\) be their geodesic covering radius: the greatest spherical distance of any direction from its nearest site. Put
\[
 c=\cos(\pi/n),\quad t=\cos(\delta-\pi/n),\quad
 D=\frac{hr(c+t)}{\sqrt{4h^2+r^2(t-c)^2}}.
\]
Then **the complete two-parameter covering-radius law** is
\[
 \boxed{\cos\rho(n,h,\delta)=\min\{h,D\}.}
\]
The active worst-hole type changes sharply at
\[
 \boxed{h^2=\frac{ct}{1+ct}:}
 \quad\begin{cases}
 \cos\rho=h,&h^2\le ct/(1+ct),\\
 \cos\rho=D,&h^2\ge ct/(1+ct).
 \end{cases}
\]
For any fixed twist \(\delta\), the **unique optimal positive latitude** is
\[
 \boxed{h^2=\frac{ct}{1+ct},\qquad
 \min_{0<h<1}\rho(n,h,\delta)=\arccos\sqrt{\frac{ct}{1+ct}}.}
\]
Optimizing both latitude and twist, the **unique optimum modulo relabeling and rigid motions preserving the two-ring presentation** occurs for the half-step stagger \(\delta=\pi/n\) and
\[
 \boxed{h^2=\frac{c}{1+c},\qquad
 \min_{h,\delta}\rho(n,h,\delta)=\arccos\sqrt{\frac{c}{1+c}}.}
\]
In particular, the minimum radius tends to \(\pi/4\), with the quantitative expansion
\[
 \min_{h,\delta}\rho(n,h,\delta)=\frac\pi4+\frac{\pi^2}{8n^2}+O(n^{-4})
 \quad(n\to\infty).
\]
For \(n=3\) the optimizer is the regular octahedron. For every \(n\ge4\), the optimum within this two-ring family is **not** the uniform (all-edges-equal) antiprism.

## Assumptions and scope
The sites are on the Euclidean unit sphere, measured by geodesic angle \(\arccos(u\cdot v)\). Both rings have the same Euclidean radius, opposite nonzero heights, and regular angular spacing. The twist interval is a complete fundamental period, with the two endpoints representing aligned prisms. This is optimization **within the stated two-ring family**; no assertion is made about the globally best unrestricted arrangement of \(2n\) spherical sites. The covering radius is the radius of equal spherical caps centered at the sites needed to cover the whole sphere, equivalently the radius of the largest empty spherical cap. The analytic formulas apply to all integers \(n\ge3\), all allowed twists, and every \(0<h<1\).

## Proof
**1. Covering radius from facet distances.** Let \(P\) be the Euclidean convex hull of the \(2n\) sites. Its centroid is the origin, which is strictly interior for \(0<h<1\). For a direction \(u\in S^2\), let \(H_P(u)=\max_{v\in P}u\cdot v\). By the definition of the angular nearest-site distance,
\[
 \rho=\max_{u\in S^2}\arccos H_P(u)
 =\arccos\left(\min_{u\in S^2}H_P(u)\right).
\]
For a polytope containing the origin, \(\min_{\|u\|=1}H_P(u)\) equals the minimum distance from the origin to a supporting facet plane: it is the radius of the largest **origin-centered** Euclidean ball inside \(P\). This is also the standard facet/empty-cap relation, but we derive the relevant facet distances directly.

**2. All facets.** Put \(\phi=\pi/n\), so \(c=\cos\phi\ge1/2\). If \(0<\delta<2\phi\), the convex hull consists of the top and bottom regular \(n\)-gonal facets, together with \(2n\) alternating triangles, each containing an edge from one ring and one vertex from the other. To see that no other facets occur, orthogonally project to the horizontal plane: the two regular polygons have alternating vertices around their common circumcircle, and each upper-edge midpoint has one nearest lower vertex in its angular wedge (and vice versa); the corresponding supporting planes described below put all remaining projected vertices on the interior side. These facets form a closed polyhedral surface, hence are exhaustive. For \(\delta=0\) or \(\delta=2\phi\), the alternating triangles merge in pairs into \(n\) rectangular side facets; the distance formula is their continuous limit and holds directly.

The top and bottom planes have distance \(h\). Rotate the coordinates to place a representative upper edge at horizontal angles \(-\phi,+\phi\), and its adjacent lower vertex at angle \(\beta=\delta-\phi\). The upper endpoints are
\[
 (rc,\pm r\sin\phi,h)
\]
and the lower vertex is \((r\cos\beta,r\sin\beta,-h)\). The facet plane is independent of the second horizontal coordinate. Up to normalization, its outward normal is
\[
 \left(1,0,\frac{r(t-c)}{2h}\right),\qquad t=\cos\beta.
\]
Its constant term is \(r(c+t)/2\). Its distance from the origin therefore is
\[
 \frac{r(c+t)/2}{\sqrt{1+r^2(t-c)^2/(4h^2)}}
 =\frac{hr(c+t)}{\sqrt{4h^2+r^2(t-c)^2}}=D.
\]
The lower-edge triangles have the same value because their relative angular offset is \(-\beta\). Thus all side-facet distances equal \(D\), proving \(\cos\rho=\min(h,D)\).

**3. Exact transition.** Since \(c>0\) and \(t\in[c,1]\), all quantities are positive. Squaring the comparison \(D\ge h\) and canceling positive factors gives
\[
 (1-h^2)\bigl[(c+t)^2-(t-c)^2\bigr]\ge 4h^2,
\]
which reduces to \((1-h^2)ct\ge h^2\), exactly \(h^2\le ct/(1+ct)\). This identifies the two active facet classes and the transition.

**4. Unique latitude optimum.** Put \(x=h^2\), \(q=t-c\ge0\), and \(x_*=ct/(1+ct)\). The first branch \(\min(h,D)=\sqrt x\) is strictly increasing on \(x\le x_*\). On the second branch,
\[
 D^2=(c+t)^2\frac{x(1-x)}{q^2+(4-q^2)x}.
\]
For \(q>0\), differentiation shows that this rational expression rises until \(x_0=q/(2+q)\) and decreases strictly thereafter. When \(q=0\), it equals \(c^2(1-x)\) and is strictly decreasing. In both cases \(x_* > x_0\), since, after multiplying positive denominators,
\[
 ct(2+t-c)-(t-c)(1+ct)=c+(2c-1)t>0
\]
for \(c\ge1/2\). Hence the second branch is strictly decreasing throughout \(x\ge x_*\). The two branches meet at \(x_*\), yielding the asserted unique optimum and its exact value.

**5. Unique twist optimum.** The optimal-in-height cosine \(\sqrt{ct/(1+ct)}\) is strictly increasing in \(t\). Since \(t=\cos(\delta-\phi)\le1\), with equality in the indicated fundamental interval only at \(\delta=\phi\), the unique global optimum follows. The limiting expansion follows by substituting \(\cos(\pi/n)=1-\pi^2/(2n^2)+O(n^{-4})\).

**6. Why uniform antiprisms are not optimal (except at six sites).** At half-step twist, equality between a same-ring polygon edge and a cross-ring side edge is equivalent to
\[
 h^2=\frac{(1-c)(1+2c)}{2+(1-c)(1+2c)}.
\]
The covering optimum instead has \(h^2=c/(1+c)\). They agree exactly when \(c=1/2\), i.e. \(n=3\), because equality reduces to \((2c-1)(c+1)=0\). For every \(n\ge4\), the covering-optimal antiprism is strictly taller than the corresponding edge-uniform antiprism.

## Verification
The standalone executable `check_antiprism.py` computes independent three-dimensional convex hulls using `scipy.spatial.ConvexHull`, obtains every actual facet distance, and compares their minimum against the closed formula. It tests \(n\in\{3,4,5,6,8,12,21\}\), seven twist values (including aligned endpoints and interior staggerings), and five heights: 245 distinct facet comparisons. It also samples 300,000 uniform spherical directions for selected configurations and checks the geometric bound, and performs 25 separate finite-difference checks at the analytically asserted unique latitude maxima. The script output was:

```text
ANTIPRISM_SPHERICAL_COVERING_OK facet_comparisons 245 samplings 300000 optimal_profiles 25
```

These numerical checks are corroborative, not a proof for all parameters. The quantified theorem follows from the complete supporting-facet classification and the exact one-variable inequality in the proof. To reproduce: `python check_antiprism.py` with Python, NumPy, and SciPy installed.

## Relationship to prior work
Fowler, Tarnai and Gáspár (2002) study optimized sphere coverage by antipodal cap-center configurations, including a pentagonal antiprism as a packing-stage configuration and its subsequent symmetry-breaking deformation. Their numerical and geometric study concerns unrestricted antipodally paired centers (for selected small sizes) and a continuous range of cap radii; it does not give the stated all-integer, all-twist two-ring exact mesh-norm law or its restricted unique global optimizer. Indeed, the pentagonal antiprism is not asserted there to be the globally covering-optimal ten-site configuration.

Brauchart, Dick, Saff, Sloan, Wang and Womersley (2014) relate generic spherical covering radii to numerical integration and design discrepancy, not to the exact finite-ring optimization. Brauchart, Reznikov, Saff, Sloan, Wang and Womersley (2015) analyze random spherical sets and the distribution of facet-induced hole radii, rather than a fixed, doubly cyclic configuration. Their facet-to-cap interpretation is a general antecedent of Step 1 and is not claimed as original.

A separately published theorem that every uniform antiprism has X-ray number three concerns illumination by three unoriented Euclidean line directions, not geodesic coverage by the antiprism's vertices, and does not imply this result. Its restrictions to edge-uniform antiprisms do not include most optimizers found above.

The standard six-point octahedral spherical-covering extremum is established classical knowledge and is **not** claimed as new. The claimed addition is the full two-parameter formula, phase switch, every-twist unique latitude optimum, and all-\(n\) optimality/metric contrast for the two-ring family. Historical mathematical priority remains provisional.

## Limitations
The global optimum is solely within equal-radius, equal-cardinality rings symmetrically located at two latitudes. It need not solve the unrestricted spherical covering problem with \(2n\) centers; even for ten sites, unrestricted configurations can improve over the two-ring optimum. The formula does not cover unequal ring populations, different latitudes, nonregular angular gaps, or non-Euclidean angular metrics. Numerical hull tests cannot prove exhaustive global optimality, which is supplied only within the specified family by the analytical argument. Prior work under an unsearched classical polyhedral-inradius formulation remains a residual historical-priority risk. No independent validation has been performed.

## References
1. P. W. Fowler, T. Tarnai and Zs. Gáspár, *From circle packing to covering on a sphere with antipodal constraints*, Proceedings of the Royal Society A **458** (2002), 2275–2287, first published online 24 July 2002. DOI: https://doi.org/10.1098/rspa.2002.0990.
2. J. S. Brauchart, J. Dick, E. B. Saff, I. H. Sloan, Y. G. Wang and R. S. Womersley, *Covering of spheres by spherical caps and worst-case error for equal weight cubature in Sobolev spaces*, arXiv:1407.8311, first submitted 31 July 2014. https://arxiv.org/abs/1407.8311.
3. J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang and R. S. Womersley, *Random Point Sets on the Sphere—Hole Radii, Covering, and Separation*, arXiv:1512.07470, first submitted 23 December 2015. https://arxiv.org/abs/1512.07470.
