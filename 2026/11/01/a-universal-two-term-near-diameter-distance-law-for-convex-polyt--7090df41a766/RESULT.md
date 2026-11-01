# A universal two-term near-diameter distance law for convex polytopes, with sharp orthotope rigidity

## Finding

Let \(P\subset\mathbb R^d\) be any full-dimensional compact convex polytope, \(d\ge3\), of volume \(V>0\) and Euclidean diameter \(D>0\). Let \(X,Y\) be independent uniform points of \(P\). The complete first two nonzero coefficients of the probability that their distance approaches the diameter are determined by **only the tangent cones at the ordered diametral vertex pairs**:
\[
\mathbb P\{\|X-Y\|>D-t\}
=\frac{t^{2d}}{V^2}\sum_{(a,b)\in\mathcal E(P)}
B_{ab}\bigl(1+T_{ab}t+O_P(t^2)\bigr),\qquad t\downarrow0.
\tag{1}
\]
The definitions of \(B_{ab}\) and \(T_{ab}\) below involve only finite-volume cone sections and their elementary first two transverse moments. Each \(B_{ab}\) and \(T_{ab}\) is strictly positive. In particular, the universal endpoint exponent for a full-dimensional polytope is \(2d\), with a positive next-order coefficient.

For an orthotope with positive side lengths \(L_1,\ldots,L_d\), set \(D=(\sum_iL_i^2)^{1/2}\). Formula (1) specializes to
\[
\mathbb P\{\|X-Y\|>D-t\}
=\frac{2^dD^{2d}}{(2d)!\prod_iL_i^4}\,t^{2d}
\left(1+\frac{3D^2\sum_iL_i^{-2}-d(2d+1)}{D(2d+1)}\,t+O_P(t^2)\right).
\tag{2}
\]
Among orthotopes with a prescribed Euclidean diameter \(D\), the relative next-to-leading coefficient in parentheses is at least
\[
\boxed{\frac{d(d-1)}{D(2d+1)}}.
\tag{3}
\]
Equality holds **exactly for cubes**. This is an extremum of the *relative correction coefficient*, not a universal stochastic ordering of complete distance distributions.

## Assumptions and scope

The word polytope means a convex polytope of full affine dimension \(d\), with finitely many vertices and ordinary Euclidean metric and volume. The diameter \(D\) is attained at vertices. Its **ordered** diametral vertex-pair set is
\[
\mathcal E(P)=\{(a,b):a,b\in\operatorname{vert}(P),\ \|b-a\|=D\}.
\]
For each \((a,b)\in\mathcal E(P)\), put \(e=(b-a)/D\) and define inward tangent cones
\[
C_a=\operatorname{cone}(P-a),\qquad C_b=\operatorname{cone}(P-b).
\]
The linear height functions are \(h_a(y)=\langle e,y\rangle\) and \(h_b(z)=-\langle e,z\rangle\). They are strictly positive on nonzero points of the corresponding cones. Hence the height-one sections
\[
S_a=\{y\in C_a:h_a(y)=1\},\qquad
S_b=\{z\in C_b:h_b(z)=1\}
\]
are compact \((d-1)\)-dimensional convex polytopes. Define
\[
A_a=\operatorname{vol}_d\{y\in C_a:h_a(y)\le1\},\qquad
A_b=\operatorname{vol}_d\{z\in C_b:h_b(z)\le1\}.
\]
Let \(U_a,U_b\) be **independent** points, each uniform in \((d-1)\)-dimensional Hausdorff area on \(S_a,S_b\), respectively. With the orthogonal projection \(\Pi_e=I-ee^{\mathsf T}\), write
\[
\mu_a=\mathbb E[\Pi_e U_a],\quad \mu_b=\mathbb E[\Pi_e U_b],\qquad
M_a=\mathbb E\|\Pi_eU_a\|^2,\quad M_b=\mathbb E\|\Pi_eU_b\|^2.
\]
Finally,
\[
\boxed{B_{ab}=\frac{(d!)^2}{(2d)!}A_aA_b,\qquad
T_{ab}=\frac{d(d+1)(M_a+M_b)-2d^2\langle\mu_a,\mu_b\rangle}{2D(2d+1)}.}
\tag{4}
\]
All constants in (1)–(4) are dimensional in the usual units; for example \(T_{ab}\) has inverse-length units. No simpliciality, rationality, symmetry, or generic-position assumption is imposed. The main new scope is \(d\ge3\); the local expansion also works in dimension two, where full planar polygon-distance formulas already exist.

## Proof

**1. Strictly exposed diameter endpoints.** Fix \((a,b)\in\mathcal E(P)\) and \(e=(b-a)/D\). For a nonzero \(y\in C_a\), some \(\epsilon>0\) satisfies \(a+\epsilon y\in P\). If \(\langle e,y\rangle\le0\), then
\[
\|b-a-\epsilon y\|^2=D^2-2\epsilon D\langle e,y\rangle+\epsilon^2\|y\|^2>D^2,
\]
contradicting the diameter. Hence \(h_a(y)>0\) for \(y\ne0\); the same argument at \(b\) gives \(h_b(z)>0\). Compactness of the intersections of these pointed cones with the unit sphere implies a quantitative bound \(\|y\|\le C h_a(y)\), \(\|z\|\le C h_b(z)\). It also proves the height-one sections are compact and nondegenerate.

The Euclidean diameter is realized at vertices: fixing one coordinate and maximizing the strictly convex squared distance over a polytope can be reduced to vertices, and then repeating with the other coordinate. Every maximizing ordered pair must be vertices, since equality at a nontrivial convex combination would contradict strict convexity. Thus the global maximum set of the continuous distance function on \(P\times P\) consists of the finite set \(\mathcal E(P)\). By compactness, near-maximal pairs lie in small disjoint neighborhoods of these pairs. In each vertex neighborhood the polytope agrees exactly with its translated tangent cone.

**2. Uniform localization on the \(t\) scale.** In an \((a,b)\) neighborhood write \(x=a+y\), \(y'=b+z\), where \(y\in C_a\), \(z\in C_b\). Then
\[
\|y'-x\|=\|De+(z-y)\|,\quad
\langle e,z-y\rangle=-h_a(y)-h_b(z).
\]
The strict positivity just proved forces \(\|y\|+\|z\|=O(t)\) when the distance exceeds \(D-t\): apply the uniform first-order expansion of \(\|De+z-y\|\) and shrink the local neighborhoods to dominate its quadratic error by half the linear height deficit. Hence for sufficiently small \(t\), the contribution at this pair is exactly the corresponding tangent-cone integral, after scaling \(y=tY\), \(z=tZ\), over a uniformly bounded region.

**3. Radial threshold and the cone-product beta integral.** Define
\[
s=h_a(Y)+h_b(Z),\qquad
q=\|\Pi_e(Z-Y)\|^2.
\]
Uniform Taylor expansion on this bounded region gives
\[
\frac{D-\|De+t(Z-Y)\|}{t}
=s-\frac{t}{2D}q+O_P(t^2).
\tag{5}
\]
The product cone \(C_a\times C_b\) is a \(2d\)-dimensional cone. On a ray with \(s=1\), let \(q_0\) be its squared transverse difference. By (5), the radial admissibility threshold is
\[
r_t=1+\frac{t}{2D}q_0+O_P(t^2),
\tag{6}
\]
where the remainder is uniform in the normalized cone section. The radius-zero and boundary sets have zero Lebesgue measure, so termwise integration is valid. With radial Jacobian \(r^{2d-1}\), this yields the local integral
\[
t^{2d}B_{ab}\left(1+\frac dD\,\mathbb E_{s=1}q_0\,t+O_P(t^2)\right).
\tag{7}
\]
At \(t=0\), cone-section volume at height \(u\) is \(A_au^d\). Thus the measure at heights \(u,v\ge0\) has density \(d^2A_aA_bu^{d-1}v^{d-1}\,du\,dv\). Integrating over \(u+v\le1\) gives
\[
B_{ab}=d^2A_aA_b\frac{\Gamma(d)^2}{\Gamma(2d+1)}
=\frac{(d!)^2}{(2d)!}A_aA_b.
\]

**4. The explicit second coefficient.** Under uniform volume on \(\{(Y,Z)\in C_a\times C_b:s\le1\}\), the heights \((u,v,1-u-v)\) have the \(\mathrm{Dirichlet}(d,d,1)\) law. Independently, the directions are uniform on \(S_a\) and \(S_b\), hence \(Y=uU_a\), \(Z=vU_b\). Their moments are
\[
\mathbb E[u^2]=\mathbb E[v^2]=\frac{d(d+1)}{(2d+1)(2d+2)},\qquad
\mathbb E[uv]=\frac{d^2}{(2d+1)(2d+2)}.
\]
Also \(q\) is homogeneous of degree two under cone-product dilation, so \(\mathbb E_{s=1}q_0=(d+1)\mathbb E_{s\le1}q/d\). Substituting this and expanding \(q=\|v\Pi_eU_b-u\Pi_eU_a\|^2\) in (7) gives \(T_{ab}\) in (4). The bracket in (4) is strictly positive, since it is a positive multiple of the expectation of a nonnegative transverse squared distance that is positive on a set of positive measure, as both sections have dimension \(d-1\ge2\). Finally, sum (7) over the disjoint ordered diametral neighborhoods and divide by \(V^2\), proving (1).

**5. Orthotopes and sharp isotropic rigidity.** For \(P=\prod_i[0,L_i]\), the ordered diametral pairs are its \(2^d\) opposite-vertex pairs. The height-one section at the all-zero corner has vertices \((D/L_i)e_i\), and the opposite inward section is its negative. Its uniform barycentric coordinates have \(\mathrm{Dirichlet}(1,\ldots,1)\) moments. Writing \(S=\sum_iL_i^{-2}\), direct evaluation gives
\[
A_a=A_b=\frac{D^d}{d!\prod_iL_i},\quad
\|\mu_a\|^2=\frac{D^2S}{d^2}-1,\quad
\mu_b=-\mu_a,\quad
M_a=M_b=\frac{2D^2S}{d(d+1)}-1.
\]
Substitution into (4), followed by division by \(V^2=(\prod_iL_i)^2\), gives (2) exactly. Independently, the coordinate differences \(X_i-Y_i\) have triangular densities; substituting their deficits from the \(2^d\) farthest corners yields the same beta/Dirichlet integrals, providing a different derivation. Finally, Cauchy--Schwarz yields
\[
D^2S=(\sum_iL_i^2)(\sum_iL_i^{-2})\ge d^2,
\]
with equality if and only if all side lengths coincide. Inserting this inequality into the relative coefficient proves (3) and its unique equality class.

## Verification

The standalone Python 3 file `verify_tail.py` uses only the standard library. Running `python3 verify_tail.py` performs exact rational comparisons of the orthotope formula and its independent cone-section moment derivation in 1,818 box instances, and checks the sharp equality criterion for each. It additionally verifies the regular-simplex cone specialization in dimensions two through seventeen and checks the exact leading and linear coefficients against an independent direct two-dimensional square integral at four shrinking distances. The executed verifier returned `PASS` with **1,838 total instances**. These are reproducible finite diagnostics; the proof above establishes the universal theorem.

## Relationship to prior work

Sinan Wang's 2026 study develops Brunn--Minkowski structure for the complete random-pair distance distribution in convex bodies, including covariogram formulations, but does not state the polytope-specific local two-term diameter-tail expansion or the orthotope coefficient rigidity proved here. Pure and collaborators derive the distance distribution for arbitrary **planar polygons**; the main theorem is intentionally restricted to \(d\ge3\), and the planar special case is not claimed as a standalone new contribution. Lellouche and Souris (2019) present a general convolution method and special rectangle and hypersphere calculations; their open-access full text does not state the all-polytope local cone-moment correction or fixed-diameter box rigidity. Existing literature on mean random-point distances and covariogram transforms supplies related general integral methods, but the cited statements do not imply (1)--(4) with their explicit local coefficients and anisotropy equality case. Schrempp's 2017 smooth-pole extreme-distance analysis and the earlier sample-diameter laws it surveys identify a different extreme-value regime (many sampled points, often smooth poles), with possible overlap at leading-order cube behavior; neither gives the present fixed-two-point full-polytopal second cone coefficient or its sharp box anisotropy. Earlier formulas for regular simplices are consistent special cases of (1) and are not claimed independently as new.

## Limitations

This is an asymptotic expansion as \(t\downarrow0\), not an exact full-distance distribution or a uniform estimate as the polytope degenerates. The constants and hidden remainder may depend on the entire polytope, including its angular separation between diameter pairs. The stated sharp box inequality concerns only the first relative correction at a fixed diameter; it is not a monotonicity theorem for arbitrary distances. Historical priority cannot be ruled out for an unindexed local-cone endpoint expansion, and no independent mathematical validation has been performed.

## References

1. Sinan Wang, *A Brunn--Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916, first posted 2026-10-01. https://arxiv.org/abs/2610.01916
2. Ross Pure and collaborators, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757, 2019. https://arxiv.org/abs/1903.07757
3. Gilles Bonnet, Anna Gusakova, Christoph Thäle and Dmitry Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, *Advances in Mathematics* 386 (2021), article 107813; preprint arXiv:2010.03351. https://arxiv.org/abs/2010.03351
4. Solal Lellouche and Marc Souris, *Distribution of Distances between Elements in a Compact Set*, *Stats* 3 (2020), 1–15 (first published 2019-12-26). https://doi.org/10.3390/stats3010001
5. Michael Schrempp, *Limit laws for the diameter of a set of random points from a distribution supported by a smoothly bounded set*, 2017, arXiv:1709.03706. https://arxiv.org/abs/1709.03706
6. G. Ohanyan and H. Khalatyan, *Relation between Covariogram and Distribution Function of the Distance Between Two Uniform and Independent Points*, 2022. See bibliographic abstract and related distance-transform formulas in journal databases.
