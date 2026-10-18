# Conditional projected-area moments of ten- and twelve-vertex regular-dodecahedron silhouettes

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(D\subset\mathbb R^3\) be the regular dodecahedron
\[
D=\{x: |x\cdot s_i|\le1\ (i=1,\ldots,6)\},
\]
where the six vectors are
\[
\begin{split}
s_1&=(0,-1,-\varphi),\quad s_2=(0,-1,\varphi),\\
s_3&=(-1,-\varphi,0),\quad s_4=(-1,\varphi,0),\\
s_5&=(-\varphi,0,-1),\quad s_6=(-\varphi,0,1).
\end{split}
\]
Every facet has the same area \(F>0\). For \(U\) uniform on the unit sphere, let \(N(U)\) be the number of vertices of the generic orthogonal projection of \(D\) onto \(U^\perp\), and let \(W(U)=\operatorname{area}(D\mid U^\perp)/F\). Almost surely \(N\in\{10,12\}\).

Put
\[
\theta=\arccos(1/\sqrt5),\quad p=\frac{15\theta}{\pi}-5,\quad
T=3\theta-\pi,\quad d=1-\frac1{\sqrt5},\quad c=\sqrt{4+\frac8{\sqrt5}}.
\]
The exact *type-weighted first two area moments* are
\[
\boxed{\begin{aligned}
\mathbb E[W\,\mathbf{1}_{\{N=12\}}]&=\frac3{\varphi+2},\\
\mathbb E[W\,\mathbf{1}_{\{N=10\}}]&=3-\frac3{\varphi+2},\\
\mathbb E[W^2\,\mathbf{1}_{\{N=12\}}]&=\frac5\pi\left[\left(2+\frac2{\sqrt5}\right)T+2dc\tan\frac\pi{10}\right],\\
\mathbb E[W^2\,\mathbf{1}_{\{N=10\}}]&=2+\frac{20(2+\arcsin(1/\sqrt5))}{\pi\sqrt5}-\mathbb E[W^2\,\mathbf{1}_{\{N=12\}}].
\end{aligned}}
\]
The weighted moments are approximately \(0.829179606750063\), \(2.170820393249937\), \(2.402328068330097\), and \(6.611800284734147\), respectively. The marginal \(p=\Pr(N=12)\approx0.286245735243501\) and the unconditional second area moment are prior-known ingredients, not new marginal probability or variance claims.

In particular, the projected area and the silhouette vertex count are strictly **negatively correlated**:
\[
\boxed{\operatorname{Cov}(N,W)=6\left(\frac1{\varphi+2}-p\right)<0.}
\]
Numerically, \(\operatorname{Cov}(N,W)\approx-0.059115197961\); conditional mean areas divided by \(F\) are about \(2.896740474\) for twelve-sided shadows and \(3.041411450\) for ten-sided shadows. Multiply each first (respectively second) normalized moment by \(F\) (respectively \(F^2\)) to obtain moments of ordinary projected area.

## Assumptions and scope

The twelve inequalities determine a bounded convex regular dodecahedron with twelve congruent pentagonal facets and twenty vertices. The normal \(U\) is Haar-uniform on the unit sphere; reversing its sign does not change the projection. Generic directions avoid finitely many great circles, a null set. Every probability, expectation, and covariance uses this model. The entire claim concerns this regular three-dimensional solid, with area normalized by the area \(F\) of one pentagonal facet. It does not concern perspective projections or nonuniform orientation distributions.

## Proof

**1. The exact arrangement and the projected-vertex count.** All \(s_i\) have length \(R=\sqrt{\varphi+2}\) and, for distinct indices, \(s_i\cdot s_j=\pm\varphi\). The polar face-normal configuration consists of \(\pm s_i/R\). By the silhouette-edge criterion, an original edge contributes a side of the generic projected silhouette exactly when its two incident face normals have opposite signs under \(U\). A generic planar convex shadow has equally many sides and vertices, so counting such silhouette edges counts \(N(U)\). For every unordered pair of the six antipodal face-normal axes, there are precisely two antipodal dodecahedral edges, and the adjacent signed face normals have positive inner product. Consequently, for \(\epsilon_i=\operatorname{sgn}(s_i\cdot U)\),
\[
N(U)=2\#\{\{i,j\}:i<j,\ \epsilon_i\epsilon_j\ne\operatorname{sgn}(s_i\cdot s_j)\}.
\]
The six great circles \(s_i\cdot U=0\) have no triple intersection. Their chamber vertices therefore occur only at the thirty oriented cross products \(\pm(s_i\times s_j)\). A sign chamber is exactly the positive intersection of its six oriented hemispheres; testing whether each such cross product meets all six non-strict inequalities is a complete finite chamber algorithm. Exact arithmetic in \(\mathbb Z[\varphi]\), as implemented in `verify_dodeca_shadow.py`, yields exactly 32 nonempty chambers: 20 spherical triangles with \(N=12\), and 12 pentagons with \(N=10\). Each triangular angle is \(\theta\), its spherical area is \(T=3\theta-\pi\), and each edge has length \(L=\pi/5\) (the spherical cosine rule). Thus the established marginal probability is
\[
\Pr(N=12)=\frac{20T}{4\pi}=p.
\]
This marginal law and the underlying icosahedral six-circle tessellation have appeared in prior work; the new calculations start with the area weight below.

**2. Directional area formula and first type-weighted moment.** Cauchy's projection-area formula, pairing opposite facets, gives the exact identity
\[
W(u)=\sum_{i=1}^6\frac{|s_i\cdot u|}{R}.
\]
On a given triangular chamber \(\Omega\), define \(q=\sum_i\epsilon_i s_i/R\). Then \(W(u)=q\cdot u\). The three active inward great-circle normals are \(m_j=\epsilon_{i_j}s_{i_j}/R\) for the three boundary sides. The exhaustive algebraic chamber test proves for each of the twenty triangular chambers that
\[
|q|^2=6+\frac6{\sqrt5},\qquad q\cdot m_j=d=1-\frac1{\sqrt5}=\frac2{\varphi+2}.
\]
On the sphere, \(\Delta_{S^2}(q\cdot u)=-2(q\cdot u)\). The outward unit conormal of the chamber along side \(j\) is \(-m_j\), so the divergence theorem gives
\[
\int_{\Omega} W(u)\,d\omega(u)=\frac12\sum_{j=1}^3 L(q\cdot m_j)=\frac{3\pi}{5(\varphi+2)}.
\]
All twenty triangles are congruent under the icosahedral symmetry; summing their integrals and dividing by \(4\pi\) gives the first boxed formula. Independently, \(\mathbb E|U\cdot s_i/R|=1/2\), so \(\mathbb EW=3\), and subtraction gives the second first-moment formula.

**3. Second type-weighted moment.** The spherical Laplace identity for \(h(u)=q\cdot u\) is \(\Delta_{S^2}h^2=2|q|^2-6h^2\). Along each of the three edges of a triangular chamber the endpoint values of \(h\) are the same positive number \(c\): exact cross-product calculations prove \(h(v)^2=4+8/\sqrt5\) at every triangle vertex. A geodesic arc of length \(L\) with equal endpoint values \(c\) satisfies
\[
\int_{\mathrm{arc}}h\,ds=2c\tan(L/2),
\]
by solving the restriction of the linear spherical harmonic to the great circle. Applying the divergence theorem to \(h^2\) yields
\[
\begin{split}
\int_{\Omega} h^2\,d\omega
&=\frac{|q|^2 T}{3}+\frac13\sum_{j=1}^3(q\cdot m_j)\int_{\mathrm{edge}_j}h\,ds\\
&=\left(2+\frac2{\sqrt5}\right)T+2dc\tan\frac\pi{10}.
\end{split}
\]
Multiplying by \(20/(4\pi)=5/\pi\) gives the third boxed formula.

For completeness, the unconditional squared moment follows by expanding the six-term brightness identity. For two unit vectors with absolute inner product \(r\), a Gaussian-polar integration gives
\[
\mathbb E(|U\cdot v|\,|U\cdot w|)=\frac2{3\pi}\bigl(\sqrt{1-r^2}+r\arcsin r\bigr).
\]
Here all fifteen off-diagonal pairs have \(r=1/\sqrt5\). The six diagonal terms contribute \(2\); the thirty ordered off-diagonal terms contribute \(20(2+\arcsin(1/\sqrt5))/(\pi\sqrt5)\). This reproduces the prior-known unconditional second moment and, by subtraction, gives the fourth boxed formula.

**4. Strict sign.** Since \(\theta=\pi/2-\arctan(1/2)\), the alternating arctangent series gives \(\arctan(1/2)<1/2-1/24+1/160=223/480\). Together with \(\pi>157/50\), this shows \(p>7/25\). On the other hand \(1/(\varphi+2)=(5-\sqrt5)/10<7/25\), since \(\sqrt5>11/5\). Therefore \(p>1/(\varphi+2)\). Finally, \(N=10+2\mathbf{1}_{\{N=12\}}\) almost surely, and
\[
\operatorname{Cov}(N,W)=2\bigl(\mathbb E[W\mathbf{1}_{\{N=12\}}]-p\mathbb EW\bigr)=6\bigl((\varphi+2)^{-1}-p\bigr)<0.
\]
The conditional means follow by division by \(p\) and \(1-p\).

## Verification

Run `python3 verify_dodeca_shadow.py` from the supplied standalone package. Only the Python standard library is needed. The checker constructs the six face-normal axes in exact \(\mathbb Z[\varphi]\) arithmetic, tests all 64 possible sign patterns against all thirty oriented pairwise great-circle crossings, certifies all 32 feasible chambers and their ten/twelve silhouette counts, checks each triangular chamber's normal and corner identities, and evaluates the exact analytic formulas. It separately reconstructs all twenty dodecahedral vertices from their dual icosahedral faces and compares 400 projected planar convex hulls with the independently obtained facet-normal brightness. A 240,000-direction deterministic spherical quadrature corroborates the type-weighted first two moments numerically.

The full continuum of orientations is covered by the proved finite sign-chamber decomposition and the spherical integral identities. A finite experiment alone would not prove these claims; the numerical convex-hull and quadrature portions are supplemental checks.

## Relationship to prior work

Glisse and Lazard give the general silhouette-edge criterion and expected silhouette-count theory for convex and nonconvex polyhedra. Classical Cauchy projection geometry yields the unconditional mean area. An existing exact Haar central-section calculation for the regular icosahedron gives the same marginal ten/twelve type probability through polar duality. That result is **prior coverage** of the unweighted type law, not an originality claim here. A prior complete exact variance computation for the five Platonic solids similarly covers the unconditional dodecahedral second moment and does not give the present type-conditioned moments.

The current contribution consists specifically of the four type-weighted area moments, their two conditional means and variances, and the proven negative area–complexity covariance for the regular dodecahedron. Earlier area-weighted silhouette calculations for arbitrary tetrahedra already employ spherical boundary-flux integrals; the flux technique itself is therefore not claimed to be novel. The tetrahedral and cuboctahedral formulas treat different facet-normal configurations and do not imply the dodecahedral identities. The calculations depend essentially on the icosahedral triangular chamber normals and their common boundary values.

## Limitations

The result covers only orthographic, uniformly oriented shadows of the regular Euclidean dodecahedron. Exceptional viewing normals have probability zero and are not individually classified. It does not determine the full conditional area density, perspective projections, or arbitrary deformations. Independent external validation and a definitive historical priority determination have not been performed. Older stereological work could contain an equivalent type-conditioned dodecahedral formula that was not located in the inspected accessible sources.

## References

1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087v1 (first publicly posted 14 February 2007), https://arxiv.org/pdf/cs/0702087.
2. *Exact Haar polygon-type law for central icosahedron sections*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f .
3. *Exact orientation-variance spectrum of Platonic shadow areas*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859 .
4. G. Frederick, *Great Circle Bow-Ties of the Icosahedron* (5 August 2023), https://geometryofthinking.com/2023/08/05/great-circle-bow-ties-of-the-icosahedron/ .
5. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-area-weighted-silhouette-probabilities-of-arbitrary-tetrahedra--ddfd7f3eeb66 .
6. *N Points On Sphere all in One Hemisphere*, MathPages, https://www.mathpages.com/home/kmath327/kmath327.htm (original publication date not established).
