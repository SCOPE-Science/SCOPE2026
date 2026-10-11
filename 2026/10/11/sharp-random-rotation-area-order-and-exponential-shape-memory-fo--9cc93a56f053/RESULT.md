# Sharp random-rotation area order and exponential shape memory for tangential polygons

## Finding
Let \(n\ge3\), and let \(P\) be a nondegenerate convex \(n\)-gon tangent to the unit circle along all its sides. Independently rotate \(m\ge1\) copies of \(P\) by uniform angles and intersect them. The regular tangential \(n\)-gon uniquely minimizes the **expected intersection area** among all such \(P\). More precisely, its nonregular competitors have a strictly positive area excess which decays at a sharp exponential rate determined by their *shortest angular gap between adjacent tangent normals*. Despite this shape-dependent exponential correction, every such polygon has exactly the same complete expansion in inverse powers of the number of copies.

Write \(\Delta_1,\ldots,\Delta_n\in(0,\pi)\) for the cyclic angular separations between successive tangent normals, with \(\sum_i\Delta_i=2\pi\). For real \(t\ge0\) put
\[
p_P(t)=\frac{1}{2\pi}\sum_{i=1}^n (\Delta_i-2t)_+,
\qquad (z)_+=\max\{z,0\}.
\]
Let \(K_m(P)=\bigcap_{j=1}^mU_jP\), where \(U_j\) are independent uniform planar rotations, and \(A_m(P)=\operatorname{Area}(K_m(P))\). Then the following integral is exact for all \(m\ge1\):
\[
\mathbb E A_m(P)
=\pi+\pi\int_0^{\Delta_{\max}/2}
2\tan t\sec^2t\,p_P(t)^m\,dt.
\tag{1}
\]
For the regular tangential polygon \(P_n\), this reduces to
\[
\mathbb EA_m(P_n)=\pi+\pi\int_0^{\pi/n}
2\tan t\sec^2t\left(1-\frac{nt}{\pi}\right)^m dt.
\tag{2}
\]
For every polygon \(P\),
\[
\mathbb EA_m(P)\ge\mathbb EA_m(P_n),
\]
with equality for any finite integer \(m\ge1\) if and only if \(P\) is regular (up to rotation).

If \(P\) is not regular, let \(a=\Delta_{\min}/2\), let \(s\in\{1,\ldots,n-1\}\) be the number of minimal gaps, and set \(q=1-na/\pi\in(0,1)\). Then
\[
\boxed{\mathbb EA_m(P)-\mathbb EA_m(P_n)
\sim\frac{2\pi^2s}{n(n-s)}\tan a\sec^2a\,\frac{q^{m+1}}m}\quad(m\to\infty).
\tag{3}
\]
In particular the \(m\)-th root of the excess converges to \(q\). All such polygons share a complete inverse-power expansion; its first terms are
\[
\mathbb EA_m(P)=\pi+
\frac{2\pi^3}{n^2(m+1)(m+2)}+
\frac{16\pi^5}{n^4(m+1)(m+2)(m+3)(m+4)}+
O_{P,n}(m^{-6}).
\tag{4}
\]

## Assumptions and scope
All polygons are planar, bounded, strictly nondegenerate, and tangent along every side to the **same unit disk** centered at the origin. The number \(n\) of sides is fixed. The gap condition \(\Delta_i<\pi\) ensures the supporting half-planes form a bounded polygon, and each positive gap corresponds to a genuine corner. Each copy receives one shared rotation angle for all its sides; individual tangent lines **are not independently sampled**. The positive integer \(m\) is arbitrary; asymptotics hold for fixed \(n\) and fixed initial polygon as \(m\to\infty\). A common incircle radius \(r>0\) simply multiplies every area and every excess by \(r^2\).

## Proof
**Exact survival law.** For a direction \(\theta\), let \(D_m(\theta)\in[0,\Delta_{\max}/2)\) be its least circular angular distance to a tangent-side normal among the \(mn\) rotated copies. The radial extent of their intersection in that direction is exactly \(\sec D_m(\theta)\). Indeed, every support inequality is \(x\cdot u\le1\), and the closest normal gives the largest positive scalar product with the radial unit vector. All gap lengths are less than \(\pi\), so this scalar product is positive.

For a single uniformly rotated copy, an angular point remains farther than \(t\) from every tangent normal precisely when it lies in one of the residual interiors of the cyclic gaps, of combined angular measure \(\sum_i(\Delta_i-2t)_+\). Thus for every fixed \(\theta\), independence of the \(m\) rotations gives
\[
\mathbb P\{D_m(\theta)>t\}=p_P(t)^m.
\tag{5}
\]
Polar area and rotational stationarity give \(\mathbb EA_m=\pi\mathbb E[\sec^2D_m(0)]\). Applying the survival integral identity with \(f(t)=\sec^2t\) yields (1).

**Sharp area order.** The positive-part map \(z\mapsto(z-2t)_+\) is convex. Jensen's inequality and \(\sum_i\Delta_i=2\pi\) give
\[
p_P(t)\ge\left(1-\frac{nt}{\pi}\right)_+=p_{P_n}(t)
\quad\text{for every }t\ge0.
\tag{6}
\]
Since \(2\tan t\sec^2t>0\) whenever \(0<t<\pi/2\), (1) implies the asserted area order. If \(P\) is nonregular, then \(a<\pi/n\); on the nonempty interval \((a,\pi/n)\), at least one minimal gap is clipped in (5) while the regular expression remains positive. Hence (6) is strict there, implying strict expected-area inequality for every integer \(m\ge1\).

**Exponential shape memory.** For \(t\le a\), the expression (5) for a single copy is exactly \(1-nt/\pi\), so the two integrands agree up to \(a\). For \(t\ge a\), both survival functions are at most \(q=1-na/\pi<1\). Consequently
\[
0<B_m\le\pi\bigl(\sec^2(\Delta_{\max}/2)-\sec^2a\bigr)q^m.
\tag{7}
\]
Choose \(\varepsilon>0\) sufficiently small so that no other gap-closing threshold lies in \((a,a+\varepsilon)\), and \(a+\varepsilon<\pi/n\). Then, for \(0<y<\varepsilon\), the survival functions satisfy the **exact linear identities**
\[
p_P(a+y)=q-\frac{n-s}{\pi}y,
\qquad p_{P_n}(a+y)=q-\frac n\pi y.
\tag{8}
\]
For any continuous \(g\) at \(a\) with \(g(a)>0\) and any \(c>0\), a change of variables and dominated convergence, or direct integration of the linear factor followed by continuity of \(g\), gives
\[
\int_0^\varepsilon g(a+y)(q-cy)^m\,dy
\sim \frac{g(a)q^{m+1}}{cm}
\quad(m\to\infty),
\tag{9}
\]
where \(\varepsilon\) is chosen so the factor stays positive. The contribution from \(t\ge a+\varepsilon\) is exponentially smaller than \(q^{m+1}/m\): both decreasing functions are strictly below \(q\) there. Subtracting (9) for the two slopes in (8), with \(g(t)=2\pi\tan t\sec^2t\), gives (3). Since its coefficient is strictly positive, \(B_m^{1/m}\to q\).

**All-orders universality.** Formula (7) shows that nonregular and regular expected areas differ by at most a geometric factor. For the regular law (2), expand the analytic function \(2\tan t\sec^2t\) near zero. Each monomial \(t^{2j+1}\) integrates against \((1-nt/\pi)^m\) to the exact beta integral
\[
\int_0^{\pi/n}t^{2j+1}(1-nt/\pi)^m\,dt
=\left(\frac\pi n\right)^{2j+2}
\frac{(2j+1)!}{\prod_{k=1}^{2j+2}(m+k)}.
\tag{10}
\]
The first two Taylor coefficients \(2\) and \(8/3\) yield (4). For every fixed truncation order, Taylor's remainder integrated against the beta weight is of the next even inverse-power order, and the contribution away from zero is exponentially small. Equation (7) transfers every coefficient to all \(P\).

## Verification
The bundled standalone Python file `verify.py` executed successfully and printed `VERIFY_OK 6012 checks`. It verifies the \(m=1\) identity using an independent tangential-polygon side-angle area formula, compares direct random-rotation union-normal polygon area against the exact expectation for multiple \(m\) and shapes, samples the survival-function domination, and checks the leading exponential prefactor at high precision. The three measured ratios of exact excess to (3) at \(m=20,40,80\) were approximately \(1.14048\), \(1.06919\), and \(1.03432\), respectively. Monte Carlo checks are diagnostics, **not** substitutes for the all-parameter argument above.

## Relationship to prior work
Buck and Siddon study deterministic areas of polygons circumscribed about a circle; their tangency framework is relevant, but they do not study independent rotations of complete polygons. Fodor, Hug and Ziebarth study random *independent half-spaces* around general convex bodies and obtain expected-volume asymptotics and variance estimates. Their sampling independence occurs at the level of individual hyperplanes, not at the level of a complete rotated collection of strongly dependent facet normals. Brazitikos and Stavrakakis study intersections of random rotations of symmetric convex bodies, mainly through general-dimensional estimates; the available summary does not resolve whether their inaccessible full article contains a special planar formula. A 2015 question about rotating regular polygons studies the **number of sides** in intersections of two such polygons, rather than their exact expected areas and exponential shape-sensitive gaps.

The new conclusion is the combined exact survival-area identity, strict extremal order among *all tangential polygons with fixed side count*, and the sharp smallest-gap-dependent exponential correction for any number of independently rotated copies. It is not claimed that the classic underlying one-dimensional gap-counting principle itself is new.

## Limitations
The results concern common-center pure rotations only, fixed side count, equal incircle radii, and the expectation of area; they do not assert stochastic area domination, variance formulas, or conclusions for translations, individually independent tangent normals, or arbitrary convex bodies. The sharp exponential coefficient is for a fixed nonregular polygon, and does not give a uniform bound as the polygon approaches regularity. Some relevant historical full texts were unavailable for complete comparison, and unindexed prior results remain an originality risk. No independent scientific audit has been performed.

## References
1. Marshall W. Buck and Robert L. Siddon, *The Area of a Polygon with an Inscribed Circle*, arXiv:1203.3438v1 (first publicly posted March 15, 2012), https://arxiv.org/abs/1203.3438.
2. Ferenc Fodor, Daniel Hug, and Ines Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105v1 (first posted September 29, 2014), https://arxiv.org/abs/1409.8105.
3. Silouanos Brazitikos and Pantelis Stavrakakis, *On the intersection of random rotations of a symmetric convex body*, Math. Proc. Cambridge Philos. Soc. 157 (2014), 13–30, https://doi.org/10.1017/S0305004114000115.
4. Joseph O'Rourke and Gjergji Zaimi, *Intersection of rotating regular polygons*, MathOverflow discussion (October 17, 2015), https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons.
