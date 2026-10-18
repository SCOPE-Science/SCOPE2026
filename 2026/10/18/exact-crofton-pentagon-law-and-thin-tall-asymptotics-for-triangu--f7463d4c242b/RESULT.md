# Exact Crofton pentagon law and thin–tall asymptotics for triangular prisms

## Finding

Let \(T\subset\mathbb R^2\) be any nondegenerate triangle with vertices \(p_0,p_1,p_2\), perimeter \(P\), side lengths \(a_0,a_1,a_2\), and angles \(\alpha_0,\alpha_1,\alpha_2\). For \(h>0\), set \(K_h=T\times[0,h]\subset\mathbb R^3\). A random affine plane is chosen with Euclidean-motion-invariant measure, conditioned to meet \(K_h\). Write \(p_j(h)\) for the probability that the resulting polygon has \(j\) vertices.

For \(\theta\in[0,2\pi)\), sort the three numbers \(p_i\cdot(\cos\theta,\sin\theta)\) increasingly as \(b_1(\theta)\le b_2(\theta)\le b_3(\theta)\) and define
\[
X(\theta)=b_2(\theta)-b_1(\theta),\qquad
Y(\theta)=b_3(\theta)-b_2(\theta).
\]
Define the explicitly evaluable one-dimensional integral
\[
I_T(h)=\int_0^{2\pi}\left[
(X+Y)\arctan\frac{X+Y}{h}
-X\arctan\frac Xh-Y\arctan\frac Yh
\right]d\theta.
\]
The complete section-vertex-count distribution is
\[
\boxed{p_5(h)=\frac{I_T(h)}{\pi(P+2h)},\quad
p_3(h)=p_5(h)+\frac{2h}{P+2h},\quad
p_4(h)=\frac P{P+2h}-2p_5(h).}
\]
In particular, the pentagon probability is strictly positive for every \(h>0\), and the three probabilities are exact for all triangles, including scalene triangles. The formula is a one-dimensional quadrature, not a claim of an elementary antiderivative for arbitrary \(T\).

Two different geometric signatures occur in the thin and tall regimes. Let
\[
R(T)=\sum_{i=0}^2\frac1{a_i},\qquad
C(T)=\frac1\pi\sum_{j=0}^2
|p_i-p_j|\,|p_k-p_j|
\left(\sin\alpha_j-\alpha_j\cos\alpha_j\right),
\quad\{i,j,k\}=\{0,1,2\}.
\]
Then \(C(T)>0\), and for each fixed nondegenerate \(T\),
\[
\boxed{p_5(h)=\frac{2h-R(T)h^2+o_T(h^2)}{P+2h}
\quad(h\downarrow0),}
\]
while
\[
\boxed{p_5(h)=\frac{C(T)}{h^2}-\frac{P\,C(T)}{2h^3}
+O_T(h^{-4})\quad(h\to\infty).}
\]
The thin second-order correction detects the reciprocal side lengths; the tall leading constant detects the base's angles through a different explicit invariant.

## Assumptions and scope

The triangle has positive area and fixed finite side lengths. Its position in the horizontal plane does not matter. Its height \(h\) is positive, and only the one-sided limits at zero and infinity are taken. Almost every plane meeting the prism intersects it in a nondegenerate polygon with \(3\), \(4\), or \(5\) vertices. Tangencies and planes passing through polyhedron vertices have measure zero.

For definiteness, parameterize *oriented* planes by \(\{x:u\cdot x=t\}\), with \(u\in S^2\), \(t\in\mathbb R\), using \(d\sigma(u)\,dt\). Conditioning restricts \(t\) to the directional support interval of the prism; passing to unoriented planes divides both numerator and denominator by two, leaving all probabilities unchanged. The normal direction, after conditioning, is **not** uniformly distributed: it is weighted by directional width.

## Proof

**1. The offset length giving a pentagon.** Fix a normal with nonnegative vertical component \(w\) and planar magnitude \(r=\sqrt{1-w^2}\). Write the planar component as \(r(\cos\theta,\sin\theta)\), so that the three lower-base projected vertices, after translating their common minimum to zero, lie at \(0,x,x+y\) with \(x=rX(\theta)\), \(y=rY(\theta)\). The corresponding upper-base projected vertices lie at \(s,s+x,s+x+y\), where \(s=hw\).

A generic section polygon has one vertex per polyhedron edge it crosses. To obtain five vertices, both triangular base faces must contribute two edges each; this requires the plane offset to lie in \([s,x+y]\). Exactly one vertical edge must then be crossed. The only eligible vertical edge has endpoints at offsets \(x\) and \(x+s\). Hence the total permitted offset length is
\[
\ell_5(s,x,y)
=\operatorname{length}\left([s,x+y]\cap[x,x+s]\right)
=\left(\min\{s,x,y,x+y-s\}\right)_+.
\]
Equivalently, writing \((z)_+=\max\{z,0\}\),
\[
\ell_5(s,x,y)=s-(s-x)_+-(s-y)_++(s-x-y)_+.
\]
This also covers non-overlap, and immediately proves that there are no six-vertex sections of a triangular prism. Reflection in a horizontal plane treats normals with negative vertical component identically.

**2. Integration and normalization.** On the upper hemisphere let \(q=hw/r\), so
\[
r=\frac h{\sqrt{h^2+q^2}},\qquad
 dw=\frac{h^2}{(h^2+q^2)^{3/2}}\,dq.
\]
Using homogeneity of \(\ell_5\), the sphere-and-offset measure of pentagonal sections is
\[
2\int_0^{2\pi}\int_0^\infty
\frac{h^3}{(h^2+q^2)^2}\,
\left[q-(q-X)_+-(q-Y)_++(q-X-Y)_+\right]dq\,d\theta.
\]
For every \(a\ge0\), direct integration gives
\[
\int_0^\infty\frac{h^3(q-a)_+}{(h^2+q^2)^2}\,dq
=\frac h2-\frac{\pi a}4+\frac a2\arctan\frac ah.
\]
Substituting the four terms, the constants and affine-linear terms cancel; the remaining integrand is exactly the definition of \(I_T(h)\). On the other hand, the total sphere-and-offset mass of intersecting planes is the integral of directional width. Cauchy's projection formula for planar perimeter gives
\[
\int_{S^2}\operatorname{width}_{K_h}(u)\,d\sigma(u)
=\pi(P+2h).
\]
Dividing establishes the expression for \(p_5(h)\).

**3. The other polygon probabilities.** Every generic section vertex lies on exactly one of the nine prism edges. For an edge \(e\), its total sphere-and-offset crossing mass is \(\int_{S^2}|u\cdot e|d\sigma(u)=2\pi|e|\). The edges have total length \(2P+3h\). Thus
\[
\mathbb E[N_h]=\frac{2(2P+3h)}{P+2h}.
\]
Since \(N_h\in\{3,4,5\}\), the identity \(\mathbb E[N_h]=4+p_5(h)-p_3(h)\) yields \(p_3-p_5=2h/(P+2h)\); normalization then gives \(p_4\). This edge-count expectation is a standard integral-geometric fact, not asserted as a new general theorem.

**4. Thin asymptotics and the reciprocal-side invariant.** Set
\[
f_h(X,Y)=(X+Y)\arctan((X+Y)/h)-X\arctan(X/h)-Y\arctan(Y/h).
\]
For fixed positive \(X,Y\), uniformly away from the zero sets of \(X\) and \(Y\), the large-argument expansion of arctangent gives \(f_h(X,Y)=h+O_T(h^3)\). Precisely six exceptional azimuths occur: for each triangle edge there are two perpendicular projection directions at which the projected endpoints coincide. Near a direction corresponding to an edge of length \(a\), the vanishing adjacent gap is \(a|\delta|+O_T(\delta^2)\), while the other remains bounded away from zero. With \(x=a|\delta|\), the local deficit relative to \(h\) has leading form
\[
h-f_h(X,Y)=h-x\arctan(h/x)+\text{an integrated }o_T(h^2)\text{ remainder}.
\]
The error statement follows by first fixing disjoint small angular neighborhoods, using smoothness of the nonvanishing gap, and applying the integrable bound of order \((1+t^2)^{-1}\) to the rescaled tail \(t=x/h\). The elementary identity
\[
\int_0^\infty\left(1-t\arctan(1/t)\right)dt=\frac\pi4
\]
shows that **each** of the two exceptional azimuths for a given edge contributes \(\pi h^2/(2a)+o_T(h^2)\) to the deficit \(\int(h-f_h)d\theta\). Summing gives
\[
I_T(h)=2\pi h-\pi R(T)h^2+o_T(h^2).
\]
The thin formula follows upon dividing by \(\pi(P+2h)\). The limits are for fixed \(T\), not uniformly over degenerating triangles.

**5. Tall asymptotics and the angular invariant.** Boundedness of all three projected gaps allows uniform Taylor expansion as \(h\to\infty\):
\[
f_h(X,Y)=\frac{2XY}{h}+O_T(h^{-3}).
\]
In the azimuthal sectors where vertex \(p_j\) is the middle projected vertex, the projections of the two incident edge vectors have opposite signs. Integrating their negative product over the two corresponding arcs gives
\[
\int_{\text{middle at }p_j}XY\,d\theta
=|p_i-p_j|\,|p_k-p_j|
\bigl(\sin\alpha_j-\alpha_j\cos\alpha_j\bigr).
\]
Consequently \(I_T(h)=2\pi C(T)/h+O_T(h^{-3})\). Division by \(\pi(P+2h)\) yields the stated two-term tall expansion, with error \(O_T(h^{-4})\). Finally \(\sin\alpha-\alpha\cos\alpha>0\) for \(0<\alpha<\pi\), since its derivative is \(\alpha\sin\alpha>0\) and its value at zero is zero. Hence \(C(T)>0\).

## Verification

A standalone NumPy checker (`check_prism.py`) evaluates the azimuthal quadrature and **independently counts actual crossings of all nine prism edges** over spherical Gauss–Legendre directions. Three base triangles and four heights per base supply twelve independent geometry comparisons; six additional numerical comparisons test the thin and tall coefficients. Run with `python check_prism.py` in an environment containing NumPy. The expected success marker is `PRISM_CROFTON_CHECK_OK independent_edge_counts= 12 thin_tall_checks= 6`. All tests passed on the stated finite grids. The analytical proof—not these finite tests—establishes the results for every allowed triangle and height.

The quadrature's shape inputs are given directly as triangle vertices; it is not necessary to fit parameters to the samples. The code uses deterministic integration, not an unreported random seed.

## Relationship to prior work

The general edge-count and mean section-complexity identity is classical and also appears in related form in Bárány–Domokos, *Same average in every direction* (arXiv:2310.18960). The present claim concerns the **complete motion-invariant law of polygon types for every triangular prism**, not just its mean. De Loera–Lopez-Campos–Torres (arXiv:2412.12419) and Brandenburg–De Loera–Meroni (arXiv:2304.14239) study feasible or optimal polytope sections, not this exact Crofton distribution. Birkemeyer–Brose–Brandenburg–Prün (arXiv:2609.16195) studies combinatorial reconstruction from sections and motivates a distributional refinement.

An existing exact Crofton polygon-type law for *equilateral-base* triangular prisms supplies an already-known special case. Its unique pentagon-height optimizer is not asserted as new here. An anisotropic affine transformation from an equilateral triangle to a scalene triangle does not preserve Euclidean-motion-invariant measure on planes, so the arbitrary-scalene distribution and both shape-dependent asymptotic coefficients do not follow by affine substitution.

Important earlier stereological antecedents must be distinguished: Voss (1982) derives exact frequencies of polygon types for *some* classes of polyhedra; Ohser–Mücklich (1995) studies sectional profiles and regular prisms; Konstantinova's later work investigates numerical angular distributions for polyhedron sections including a regular triangular prism. Their accessible abstracts or descriptions do not specify this complete arbitrary-triangle formula and both asymptotic invariants; however, the complete older papers were not available for full comparison, so an equivalent prior theorem cannot be excluded. The priority determination is therefore provisional.

## Limitations

The result assumes a right triangular prism with a fixed nondegenerate planar base. It does not cover sheared prisms or other polytopes. The sampling law is conditioned Euclidean-motion-invariant affine-plane measure, *not* a uniformly oriented central plane and not unweighted orientation averaging. Only the pentagon probability requires the explicit integral; the other two are algebraic consequences. The small/large height asymptotics are shape-wise, not uniform in a triangle degenerating to a segment. No complete classification of height maximizers is claimed. Historical priority remains subject to checking inaccessible older stereological results, especially Voss (1982).

## References

1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first public 2026-09-14. https://arxiv.org/abs/2609.16195
2. I. Bárány, G. Domokos, *Same average in every direction*, arXiv:2310.18960. https://discovery.ucl.ac.uk/10193049/1/SameAveFeb01.pdf
3. J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419. https://arxiv.org/pdf/2412.12419
4. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239. https://arxiv.org/pdf/2304.14239
5. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy **128** (1982), 111–120, doi:10.1111/j.1365-2818.1982.tb00443.x.
6. J. Ohser, F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability **27** (1995), 384–396, doi:10.2307/1427832.
7. E. P. Konstantinova, *On the density of angle distributions in random plane sections of a polyhedron* (Russian-language conference abstract), https://publications.hse.ru/chapters/876255268.
