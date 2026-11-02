# Exact Haar law of quadrilateral-section propensity for the regular tetrahedron

## Finding

Take the regular tetrahedron
\[
T=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}.
\]
For any generic unit normal \(u\), let the four vertex heights, in increasing order, be \(h_1(u)<h_2(u)<h_3(u)<h_4(u)\). Among the parallel planes \(u\cdot x=h\) meeting \(T\), choose the offset uniformly in \((h_1,h_4)\). The proportion producing a quadrilateral section is
\[
Q(u)=\frac{h_3(u)-h_2(u)}{h_4(u)-h_1(u)}.
\]
For Haar-uniform \(U\) on the sphere and every \(0\le q\le1\), the **entire orientation distribution** is
\[
\boxed{\Pr(Q(U)>q)=\frac{12}{\pi}\left(\arctan\sqrt{1+2\left(\frac{1-q}{1+q}\right)^2}-\frac\pi4\right).}
\]
In particular, the probability of a quadrilateral under the two-stage experiment *uniform orientation, then uniform admissible offset* is
\[
\boxed{p_{\mathrm{two}}=\mathbb E[Q(U)]=\frac{12}{\pi}\left(\operatorname{arsinh}\frac1{\sqrt2}-\frac{\log(1+\sqrt3)}{\sqrt3}\right)=0.298746285571077\ldots.}
\]
For comparison, sampling from the rigid-motion-invariant measure on affine planes and conditioning on intersection yields a different quadrilateral probability,
\[
p_{\mathrm{inv}}=\frac{2\pi}{\arccos(-1/3)}-3=0.288535543072004\ldots.
\]
This latter unconditional value is a **comparison**, not a claim of novelty; the substantive assertion is the complete law of the directional conditional probability \(Q(U)\).

## Assumptions and scope

The tetrahedron is nondegenerate and Euclidean, with the listed vertex coordinates. Haar-uniform means normalized surface-area measure on \(S^2\); the normal \(u\) and its negative describe the same unoriented directions and produce the same \(Q\). Genericity excludes the zero-area set on which vertex heights tie. The uniform offset conditional on \(u\) is Lebesgue-uniform on the full interval of offsets meeting the solid; it is not the measure induced by conditioning a motion-invariant random affine hyperplane to hit the solid. The latter instead weights the orientation by the directional width. Statements at \(q=0,1\) use strict survival probability, and both endpoints have probability zero for \(Q\).

## Proof

**1. Section combinatorics.** Fix a generic \(u\). For an offset in the first interval \((h_1,h_2)\), precisely one vertex lies below the plane and the section meets three tetrahedron edges, giving a triangle. For \(h\in(h_2,h_3)\), two vertices lie on each side and exactly the four cross-partition tetrahedron edges meet the plane, giving a quadrilateral. The third interval also gives a triangle. Thus the formula for \(Q(u)\) is exact for every generic \(u\), without a sampling approximation.

**2. Reduction to a spherical fundamental sector.** Let \(X\ge Y\ge Z\ge0\) denote the ordered values of \(|u_1|,|u_2|,|u_3|\). Permutations of coordinates preserve the tetrahedral vertex set. An odd number of coordinate sign changes sends that vertex set to its negative, reversing all heights; this also preserves the quotient of middle gap to full width. Hence all \(48\) open signed-order spherical sectors have the same statistic. On the representative sector with coordinates \((X,Y,Z)\), the four heights are
\[
X+Y+Z,\quad X-Y-Z,\quad -X+Y-Z,\quad -X-Y+Z,
\]
ordered as written from largest to smallest because \(X\ge Y\ge Z\ge0\). Their full width is \(2(X+Y)\), and their middle gap is \(2(X-Y)\). Therefore
\[
Q(u)=\frac{X-Y}{X+Y}.
\]

**3. Exact spherical law.** Write \(t=Y/X\), \(s=Z/X\). In this sector \(0<s<t<1\), and the unit normal is
\[
u(t,s)=\frac{(1,t,s)}{\sqrt{1+t^2+s^2}}.
\]
Its spherical area element is \((1+t^2+s^2)^{-3/2}\,dt\,ds\). One of the \(48\) sectors has area \(4\pi/48=\pi/12\). Hence the density of \(t\) for a uniformly sampled normal on the sphere is
\[
f_T(t)=\frac{12}{\pi}\int_0^t\frac{ds}{(1+t^2+s^2)^{3/2}}
=\frac{12t}{\pi(1+t^2)\sqrt{1+2t^2}},\qquad0<t<1.
\]
Integrating gives
\[
\Pr(T<t)=\frac{12}{\pi}\left(\arctan\sqrt{1+2t^2}-\frac\pi4\right).
\]
Because \(Q=(1-t)/(1+t)\), the claimed complete survival distribution follows upon substituting \(t=(1-q)/(1+q)\). At \(t=1\), the expression equals one, proving the normalization as well.

**4. Haar-orientation mean.** Integrating the conditional fraction against the density yields
\[
\mathbb E Q=\frac{12}{\pi}\int_0^1
\frac{t(1-t)}{(1+t)(1+t^2)\sqrt{1+2t^2}}\,dt.
\]
The factor outside the square root decomposes as
\[
\frac{t(1-t)}{(1+t)(1+t^2)}=\frac1{1+t^2}-\frac1{1+t}.
\]
The first resulting integral is \(\operatorname{arsinh}(1/\sqrt2)\), by substituting \(t=\tan\theta\) and then \(y=\sin\theta\). The second is \(\log(1+\sqrt3)/\sqrt3\), by substituting \(t=\sinh v/\sqrt2\) and then \(z=e^v\) to integrate a rational quadratic denominator. This proves the exact displayed value.

**5. Motion-invariant comparison.** In the Euclidean-motion-invariant affine-plane model the element is proportional to \(d\sigma(u)\,dh\). Conditioning on hitting the tetrahedron weights a direction \(u\) by its width \(w(u)=h_4-h_1\), so its quadrilateral probability is \(\mathbb E[wQ]/\mathbb E[w]\), not \(\mathbb E Q\). For any four real heights in increasing order, the six pairwise absolute differences sum to \(3w+(h_3-h_2)\). Averaging the six tetrahedral edge projections on the sphere gives half the total edge length \(L\). Therefore \(\mathbb E[wQ]=L/2-3\mathbb E w\). The Cauchy–Steiner mean-width identity for a polyhedron is \(\mathbb E w=(4\pi)^{-1}\sum_e\ell_e\beta_e\), where \(\beta_e\) is the exterior dihedral angle. Here all six edges have length \(2\sqrt2\), and \(\beta_e=\arccos(-1/3)\), giving \(\mathbb E w=L\beta_e/(4\pi)\) and consequently \(p_{\mathrm{inv}}=2\pi/\beta_e-3\), as stated. This quantity is supplied solely to expose the sampling distinction.

## Verification

The standalone standard-library Python program `verify_tetra_sections.py` recomputes the exact constants, independently numerically integrates the normalized spherical density, tests the survival distribution at four thresholds by quadrature, checks the height-ratio identity against explicit tetrahedral vertex projections, and samples \(150000\) Haar normals. It also checks the four-versus-three-edge section count by testing all six tetrahedral edges against independently sampled offsets. Executing `python verify_tetra_sections.py` reports `ALL_CHECKS_PASSED`. Monte Carlo values have finite statistical error; the proof does not depend on them.

## Relationship to prior work

Brandenburg, De Loera and Meroni (arXiv:2304.14239v1, first public 2023-04-27) describe affine polytope slicing chambers, including parallel-translation chambers, and optimize certain section attributes; their investigated theorems and examples do not give the Haar distribution of the relative quadrilateral-offset interval of the tetrahedron. That geometric decomposition motivates the present orientation-resolved question. Prior simplex-section order-statistic methods already account for unconditional section-type probabilities under motion-invariant affine-plane sampling, so the displayed invariant-plane marginal is **not** claimed as a new finding. Projection/silhouette statistics are a different random-geometric experiment, as are regular-tetrahedron chord-length distributions. The complete angular distribution of the *conditional offset probability*, rather than those existing marginals, is the new contribution assessed here.

## Limitations

The exact closed law is proved only for Euclidean regular tetrahedra (and their similarities) and uniform orientation measure. It concerns the *fraction* of intersecting parallel plane offsets that give quadrilaterals, not the random geometry of section areas, angles or perimeters. Neither arbitrary tetrahedra nor nonuniform directional sampling is classified. Exhaustive priority against all historical stereological sources has not been established; the closest prior full text addresses a different invariant. Numerical tests are checks, not proof of originality or analytic correctness.

## References

1. M.-C. Brandenburg, J. A. De Loera and C. Meroni, “The Best Ways to Slice a Polytope,” arXiv:2304.14239v1 (2023-04-27), especially Theorem 1.1, §2.2, and the Platonic-solid examples. https://arxiv.org/abs/2304.14239
2. S. Ciccariello, “The intersect distribution of the regular tetrahedron,” *Journal of Applied Crystallography* **38** (2005), 97–106, DOI:10.1107/S0021889804028328 (a chord/intersect distribution, not the present plane-section propensity distribution).
3. D. Feldman and D. Klain, “Angles as Probabilities,” arXiv:0809.3459 (2008), concerning projection-angle probabilities, not uniform-offset affine sections. https://arxiv.org/abs/0809.3459
