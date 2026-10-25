# An exact polygonal shortcut law and sharp angular stability

## Finding

Let \(K\subset\mathbb R^2\) be a compact convex polygon with \(n\ge3\) genuine vertices, side lengths \(\ell_1,\ldots,\ell_n>0\), perimeter \(P\), and exterior turning angles \(\beta_i\in(0,\pi)\), so that \(\sum_i\beta_i=2\pi\). Choose two independent, arclength-uniform boundary points \(X,Y\). Write \(D_E=|X-Y|\) for their ambient Euclidean distance and \(D_B\) for the length of the shorter of the two boundary arcs joining them.

There is a polygon-dependent \(r_0>0\) such that, **exactly for every** \(0<r<r_0\),
\[
\boxed{\Pr(D_E\le r)-\Pr(D_B\le r)
=\frac{r^2}{P^2}\,\mathcal E(K),\qquad
\mathcal E(K)=\sum_{i=1}^{n}\left(\frac{\beta_i}{\sin\beta_i}-1\right).}
\tag{1}
\]
Here \(\Pr(D_B\le r)=2r/P\) for this range. In particular, \(\Pr(D_E\le r)=2r/P+r^2\mathcal E(K)/P^2\), with **no higher-order terms** at sufficiently small positive radii.

For every such \(K\), put \(\overline\beta=2\pi/n\). The shortcut coefficient obeys the **sharp, side-count-uniform angular rigidity inequality**
\[
\boxed{\mathcal E(K)\ge
n\left(\frac{2\pi/n}{\sin(2\pi/n)}-1\right)
+\frac16\sum_{i=1}^n(\beta_i-\overline\beta)^2.}
\tag{2}
\]
Equality holds exactly for equiangular polygons. The coefficient \(1/6\) is optimal among constants independent of \(n\); this does not assert fixed-\(n\) optimality of that coefficient. Equiangular does not necessarily mean regular when \(n\ge4\).

## Assumptions and scope

Angles are in radians. Adjacent sides are noncollinear, and each side is a nondegenerate closed segment. Vertices are cyclically indexed. When \(n=3\), the collection of nonadjacent side pairs is empty. An explicit admissible upper bound for \(r_0\) is the minimum of all side lengths, all quantities \(\min(\ell_{i-1},\ell_i)\sin\beta_i\), and distances between nonadjacent sides (if any). Any smaller positive \(r_0\) works. Since \(r_0\) is no greater than the shortest side, it is strictly less than \(P/2\).

Only Euclidean chord distance and the *boundary* intrinsic distance are compared; intrinsic geodesic distance through the filled convex region equals Euclidean distance and is not \(D_B\). The probability distribution is induced by normalized one-dimensional arclength, not two-dimensional uniform area measure or a motion-invariant random-line process.

## Proof

**1. The baseline boundary distance.** Parametrize the boundary by \(s\in[0,P)\), with uniform measure \(ds/P\). If \(S,T\) are independent uniform parameters, the circular difference \((S-T)\bmod P\) is uniform on \([0,P)\). Therefore \(D_B=\min\{(S-T)\bmod P,(T-S)\bmod P\}\) has cumulative distribution \(\Pr(D_B\le r)=2r/P\) for \(0\le r\le P/2\).

**2. A positive radius of exact locality.** Let \(E_i\) be the polygon's successive sides. Distinct nonadjacent sides are disjoint compact sets and have positive separation. For two sides meeting at vertex \(v_i\), let \(u,v\) be their outward-from-the-vertex unit directions; their angle is the interior angle \(\alpha_i=\pi-\beta_i\). A pair of points has form \(v_i+su,\,v_i+tv\) for \(s,t\ge0\), capped by the respective side lengths. If its distance is at most \(r\), its distance to either of the infinite supporting lines is also at most \(r\); consequently \(s\sin\alpha_i\le r\) and \(t\sin\alpha_i\le r\). Thus whenever \(r<\min(\ell_{i-1},\ell_i)\sin\alpha_i\), the side-length caps do not affect the adjacent-side pair integral. For \(r\) also below the smallest side length and all nonadjacent-side separations, only pairs on the same or on adjacent sides contribute to \(\Pr(D_E\le r)\), and the local integrals are exact.

**3. Same-side contributions.** On a side of length \(\ell_i\), the ordered parameter pairs \((s,t)\in[0,\ell_i]^2\) with \(|s-t|\le r\) have planar parameter area \(\ell_i^2-(\ell_i-r)^2=2\ell_i r-r^2\). Summing gives \(2Pr-nr^2\).

**4. Adjacent-side contributions.** The linear map \((s,t)\mapsto su-tv\) has determinant of absolute value \(\sin\alpha_i=\sin\beta_i\). It sends the positive quadrant bijectively to a planar cone whose opening is \(\pi-\alpha_i=\beta_i\). The sector of radius \(r\) has area \(\beta_i r^2/2\). The allowed \((s,t)\) area for one orientation of the two sides is therefore \(\beta_i r^2/(2\sin\beta_i)\). Counting both ordered orientations gives \(\beta_i r^2/\sin\beta_i\) for vertex \(i\). Adding this to the same-side total and dividing by \(P^2\) yields (1).

**5. Sharp angular stability.** Put \(f(z)=z/\sin z\) for \(0<z<\pi\). Euler's sine product gives
\[
f(z)=\prod_{m=1}^{\infty}\left(1-\frac{z^2}{m^2\pi^2}\right)^{-1}
=1+\frac{z^2}{6}+\sum_{k\ge2}a_kz^{2k},\qquad a_k>0,
\tag{3}
\]
where positivity follows by multiplying convergent power series with nonnegative coefficients. Hence \(f''(z)>1/3\) on \((0,\pi)\), and \(h(z)=f(z)-z^2/6\) is strictly convex. Jensen's inequality, \(\sum_i\beta_i=2\pi\), and \(\sum_i\beta_i^2=n\overline\beta^2+\sum_i(\beta_i-\overline\beta)^2\) give
\[
\sum_i f(\beta_i)\ge nf(\overline\beta)+\frac16\sum_i(\beta_i-\overline\beta)^2.
\]
Subtracting \(n\) proves (2). Strict convexity forces equality precisely when all turning angles are equal. Conversely, equiangular polygons exist for every \(n\).

**6. Sharpness across side counts.** Let \(n\) run through multiples of four, let \(b=2\pi/n\) and \(\varepsilon=n^{-2}\), and choose consecutive positive turning angles \(\beta_i=b+(-1)^i\varepsilon\). They sum to \(2\pi\) and remain less than \(\pi\). Taking the intersections of consecutive supporting lines tangent to the unit circle with these successive outward-normal gaps constructs convex tangential \(n\)-gons realizing those angles; their side lengths are positive since each is a sum of positive half-angle tangents. By Taylor's theorem,
\[
\frac{\sum_i f(\beta_i)-nf(b)}{\sum_i(\beta_i-b)^2}
=\frac{f(b+\varepsilon)+f(b-\varepsilon)-2f(b)}{2\varepsilon^2}
=\frac12f''(b)+o(1)\longrightarrow\frac16.
\]
Therefore the coefficient \(1/6\) cannot be increased uniformly in \(n\), completing the proof.

## Verification

The independent standard-library script `verify.py` numerically integrates the actual positive-quadrant adjacent-side inequality for six angles and compares it with the sector formula \(\beta/(2\sin\beta)\). It also checks inequality (2) on explicit alternating exterior-angle sequences and confirms the approach of the sharpness ratio toward \(1/6\). Run `python3 verify.py`; the observed output is `VERIFY_OK`. These tests detect normalization or trigonometric mistakes but do not substitute for the all-polygon proof.

For the unit square, (1) specializes, exactly at sufficiently small \(r>0\), to
\[
\Pr(D_E\le r)=\frac r2+\left(\frac\pi8-\frac14\right)r^2,
\qquad \Pr(D_B\le r)=\frac r2.
\]
As the number of sides of a regular polygon grows, the dimensionless shortcut coefficient in (1) satisfies \(\mathcal E(K)=2\pi^2/(3n)+O(n^{-3})\), consistent with the disappearance of the polygonal corner term in the circular limit.

## Relationship to prior work

Bäsel [1] determines motion-invariant random-line chord laws and area-uniform random-point distances **inside** regular polygons. Those measures are not the present arclength-pair model, so the published formulas do not imply (1) or the angular rigidity statement (2). Tong and Pan [2] provide an algorithmic calculation of distances of points uniformly distributed **within** arbitrary polygons, again with a different measure. A published convex-polygon result [3] gives a sharp angle-variance bound for the **fourth-order coefficient of an area-pair distance distribution**. Its full proof concerns the planar covariogram; it does not supply the boundary-arc baseline, the boundary-pair quadratic coefficient, or its sharp \(1/6\) rigidity bound. Tokmachev [4] studies the **mean** distance for uniform points on a convex boundary, which alone does not determine the small-radius law or the angle-energy bound; only its abstract was inspected here.

The novelty claimed is the exact local **difference between two metrics on the same polygonal boundary** and the globally sharp angular-stability inequality for that coefficient. It is not a claim of the first general procedure for computing polygon distance distributions, of a full-radius stochastic comparison, or of a new Euler sine product.

## Limitations

The identity is local in radius, with no geometry-independent positive radius guaranteed over all polygons. The theorem does not recover individual angles from one measured coefficient, and equiangular nonregular polygons share the minimum at fixed side count. The stability coefficient is globally optimal across side counts; fixed-side-count best coefficients may be larger. The proof assumes a genuine convex polygon with positive side lengths and no adjacent collinear sides; neither self-intersecting boundaries nor higher-dimensional polyhedra are covered. Earlier specialized perimeter-pair distance calculations could conceal an equivalent local formula; novelty is provisional pending an independent literature audit.

## References

1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707v1 (public 12 April 2012), https://arxiv.org/abs/1204.2707.
2. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (2016), https://arxiv.org/abs/1602.03407.
3. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b.
4. A. S. Tokmachev, *The Mean Distance Between Random Points on the Boundary of a Convex Figure*, Journal of Mathematical Sciences 286 (2024), 798–806, https://doi.org/10.1007/s10958-024-07543-w.
