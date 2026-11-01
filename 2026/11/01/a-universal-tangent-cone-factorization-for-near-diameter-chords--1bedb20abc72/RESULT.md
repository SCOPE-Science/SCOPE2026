# A universal tangent-cone factorization for near-diameter chords of convex polytopes

## Finding
Let \(d\ge4\), let \(K\subset\mathbb R^d\) be any full-dimensional compact convex polytope, and let \(D=\operatorname{diam}(K)\). Select an unoriented affine line from Euclidean-motion-invariant line measure conditioned on intersecting \(K\), and let \(L\) be its Euclidean intersection-chord length. Write \(q=d-1\) and \(\kappa_q=\pi^{q/2}/\Gamma(1+q/2)\).

For every unordered diametral vertex pair \(\{a,b\}\), let \(e=(b-a)/D\), let \(C_a\) and \(C_b\) be the respective polyhedral tangent cones, and form the \(q\)-dimensional cone sections
\[
Q_{a\mid b}=\{y\in e^\perp:e+y\in C_a\},\qquad
Q_{b\mid a}=\{y\in e^\perp:-e+y\in C_b\}.
\]
Both are compact convex sets with positive \(q\)-volume. With \(S(K)=\mathcal H^{d-1}(\partial K)\) and \(\mathcal D\) the set of unordered diametral vertex pairs, the following asymptotic holds:
\[
\boxed{\Pr(L>D-\varepsilon)=C_K\varepsilon^{2d-2}+o(\varepsilon^{2d-2})},
\]
\[
\boxed{C_K=\frac{2(q!)^2}{(2q)!\,\kappa_q\,S(K)\,D^q}
\sum_{\{a,b\}\in\mathcal D}\operatorname{vol}_q(Q_{a\mid b})\operatorname{vol}_q(Q_{b\mid a}).}
\]
In particular, the exponent \(2d-2\) is universal for all full-dimensional convex polytopes in these dimensions, without general-position assumptions on the diametral pairs, and the positive leading coefficient factorizes into local tangent-cone sections and a global surface-area normalization.

For the regular unit-edge \(d\)-simplex this gives the explicit new all-dimensional benchmark
\[
\boxed{C_{\Delta_d}=\frac{d(d+1)2^{(3d-5)/2}(d-1)!}{\kappa_{d-1}\sqrt d\,(2d-2)!}.}
\]
For instance, \(C_{\Delta_4}\approx0.225079079039277\). The simplex specialization is included as an evaluation of the universal theorem, not a separate finding.

## Assumptions and scope
A line has direction \(u\in\mathbb S^{d-1}/\{\pm1\}\) and offset \(p\in u^\perp\), with measure \(d\sigma(u)\,dp\) under an arbitrary common scaling. Conditioning on intersection with \(K\) makes this a probability law. Tangent cones are \(C_a=\overline{\{t(x-a):t\ge0,\ x\in K\}}\), which for a polytope agree locally with the feasible displacement cones. Every diametral pair consists of vertices; distinct pairs determine distinct unoriented diameter lines. There is no need to assume that the diameter direction lies strictly inside either endpoint's tangent cone: a longest edge of a simplex is permitted.

## Proof
**1. Strict transverse geometry at every diameter vertex.** If \(v\in C_a\setminus\{0\}\), polyhedrality gives \(a+tv\in K\) for all sufficiently small \(t>0\). Since \(\|a+tv-b\|\le D\),
\[
2Dt\langle e,v\rangle\ge t^2\|v\|^2,
\]
so \(\langle e,v\rangle>0\). By compactness of the unit-direction section of the closed polyhedral cone, this inequality is uniform on unit vectors of \(C_a\). The analogous inequality \(\langle-e,v\rangle>0\) holds on \(C_b\setminus\{0\}\). Consequently the sections at positive axial level \(1\) are bounded, full-dimensional convex bodies in their respective affine hyperplanes, and orthogonal projection gives the stated positive finite volumes.

**2. Localization of almost-diametral lines.** The maximum of Euclidean distance on \(K\times K\) is realized only at finitely many vertex pairs, because squared distance is strictly convex in each variable. Every sequence of chords with length tending to \(D\) has endpoint subsequences converging to one such pair. Near \((a,b)\), write the endpoints \(x=a+v\) and \(y=b+w\). The expansion
\[
D-\|y-x\|=\langle e,v\rangle+\langle-e,w\rangle+O((\|v\|+\|w\|)^2)
\]
and the strict cone inequalities imply \(\|v\|+\|w\|=O(\varepsilon)\) whenever the chord is longer than \(D-\varepsilon\) and sufficiently close to this pair. Thus the diameter-line neighborhoods can be treated separately, and all relevant transverse coordinates are \(O(\varepsilon)\).

**3. Exact invariant-line Jacobian.** Fix one ordered representative \((a,b)\) of an unordered pair and use coordinates in the parallel hyperplanes perpendicular to \(e\) through \(a\) and \(b\). A line near their diameter intersects these hyperplanes at \(a+y_a\) and \(b+y_b\), where \(y_a,y_b\in e^\perp\). Its positive direction is proportional to \(e+s\), with \(s=(y_b-y_a)/D\). In these coordinates the motion-invariant unoriented line measure is exactly
\[
\frac{dy_a\,dy_b}{D^q(1+\|s\|^2)^{(d+1)/2}}.
\]
Indeed the sphere-direction Jacobian is \((1+\|s\|^2)^{-d/2}\,ds\), the orthogonal offset-projection Jacobian is \((1+\|s\|^2)^{-1/2}\), and \(ds=D^{-q}dy_b\) at fixed \(y_a\).

**4. Local deficit and product-cone volume.** For each cone section \(Q\), define its extended gauge \(g_Q(y)=\inf\{t\ge0:y\in tQ\}\), with value \(+\infty\) when no such \(t\) exists. The cone boundary is locally an axial graph with entrance level \(g_{Q_{a\mid b}}(y)\), and likewise at \(b\). Because the polytope equals its tangent cone in a sufficiently small vertex neighborhood, rescaling \(y_a=\varepsilon z_a\) and \(y_b=\varepsilon z_b\) gives for almost every pair \((z_a,z_b)\)
\[
\frac{D-L}{\varepsilon}\longrightarrow g_{Q_{a\mid b}}(z_a)+g_{Q_{b\mid a}}(z_b).
\]
The possible gauge discontinuities on boundary rays affect a set of Lebesgue measure zero. Step 2 confines the integration to one fixed bounded region after rescaling; the Jacobian from Step 3 tends uniformly there to \(D^{-q}\). The threshold boundary has zero \(2q\)-dimensional measure, so dominated convergence applies.

Finally, since \(\operatorname{vol}_q\{g_Q<t\}=t^q\operatorname{vol}_q(Q)\), direct beta integration yields
\[
\operatorname{vol}_{2q}\{(x,y):g_{Q_a}(x)+g_{Q_b}(y)<1\}
=\frac{(q!)^2}{(2q)!}\operatorname{vol}_q(Q_a)\operatorname{vol}_q(Q_b).
\]
Summing over all diameter lines therefore gives the unnormalized leading coefficient \(D^{-q}(q!)^2/(2q)!\) times the stated sum.

**5. Crofton normalization.** Cauchy's projection formula gives the total invariant unoriented-line measure intersecting \(K\):
\[
\frac12\int_{\mathbb S^{d-1}}\operatorname{vol}_q(K\mid u^\perp)\,d\sigma(u)=\frac{\kappa_q}{2}S(K).
\]
Dividing the numerator in Step 4 by this quantity proves the boxed coefficient.

**6. Regular simplex evaluation.** For a regular simplex with edge length \(1\), a diameter direction is any edge. Each cone section has \(q+1\) vertices, whose \(q\) nonzero transverse edge generators have Gram matrix \(2I_q+\mathbf 1\mathbf 1^\top\); its determinant is \(2^{q-1}(q+2)\). Thus
\[
\operatorname{vol}_q(Q)=\frac{2^{(q-1)/2}\sqrt{q+2}}{q!},\quad
S(\Delta_d)=\frac{(d+1)\sqrt d}{q!2^{q/2}},
\]
and there are \(\binom{d+1}{2}\) diameter pairs. Substitution proves the simplex formula.

## Verification
The standalone `verify_cone_endpoint.py` is executable with Python, NumPy and SymPy. It checks the exact Gram determinant through dimension \(8\), independently reduces the cone coefficient for several nonsymmetric orthotopes to their known direct formula, and uses facet clipping of \(400000\) sampled near-diametral lines of a regular four-simplex. The estimated coefficients converge from \(0.302264485\) at deficit \(0.15\) to \(0.228696137\) at deficit \(0.006\), against the proved constant \(0.225079079\). The latter comparison is numerical corroboration, not an infinite proof. The proof's limiting step is the local gauge convergence and dominated-convergence argument above.

## Relationship to prior work
Bäsel's 2012 chord-distribution formula treats regular planar polygons under motion-invariant line measure and records the standard line normalization. Ciccariello's 2019 general polyhedron result gives a structural closed-expression theorem for the full three-dimensional chord-length distribution. Neither result asserts an arbitrary-dimension \(d\ge4\) tangent-cone product coefficient. An orthotope-specific near-diameter asymptotic in dimensions at least four is a strict special case: for \(K=\prod_{i=1}^d[-a_i,a_i]\), the cone sections have volumes \(A^d/((d-1)!\prod_i a_i)\), where \(A=(\sum_i a_i^2)^{1/2}\), and the boxed law reduces exactly to that specialized expression. The present theorem does not claim those earlier cases as independently new.

## Limitations
This is a first-order endpoint asymptotic for the Euclidean-motion-invariant **line** measure only; other chord-sampling conventions need not have this coefficient. The theorem does not provide a full length distribution or a rate in its little-oh term. Its positivity uses full-dimensional polytopes; smooth convex bodies have different local contact geometry and need not share this exponent. Existing three-dimensional full-distribution work and some exact families predate this result. Historical-priority risk remains for general high-dimensional endpoint asymptotics in less-indexed integral-geometry literature. No independent scientific audit has been performed.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public preprint 2012-04-12, https://arxiv.org/abs/1204.2707.
- S. Ciccariello, *The chord-length distribution of a polyhedron*, arXiv:1911.02532, first public preprint 2019-11-06, https://arxiv.org/abs/1911.02532; Acta Crystallographica A (2020).
- L. A. Santaló, *Integral Geometry and Geometric Probability*, 1976, Cauchy projection formula and invariant line measure (standard normalization).
