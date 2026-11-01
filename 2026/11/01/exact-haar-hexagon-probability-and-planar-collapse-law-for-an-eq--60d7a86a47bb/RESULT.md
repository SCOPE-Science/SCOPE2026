# Exact Haar hexagon probability and planar-collapse law for an equiangular affine octahedron

## Finding
For every \(t>0\), form the convex, centrally symmetric six-vertex polytope
\[
K_t=\operatorname{conv}\{\pm v_1,\pm v_2,\pm v_3\},\quad
v_1=(1,0,t),\quad v_2=(-\tfrac12,\tfrac{\sqrt3}{2},t),\quad v_3=(-\tfrac12,-\tfrac{\sqrt3}{2},t).
\]
Choose an unoriented plane uniformly by rotational Haar measure and let \(N_t\) be the number of vertices of the orthogonal projection of \(K_t\) onto that plane. Almost surely \(N_t\in\{4,6\}\). Put
\[
L=\sqrt{1+4t^2},\quad Y=3\sqrt3\,t,\quad X=L(16t^2-\tfrac12),\quad Z=\tfrac92L+3\sqrt3.
\]
With \(\operatorname{atan2}(Y,X)\) denoting the unique angle in \((0,\pi)\) having the indicated positive sine and the sign of \(X\) as cosine,
\[
\boxed{\Pr(N_t=6)=p(t)=\frac1\pi\left[\operatorname{atan2}(Y,X)+3\arctan\frac{Y}{Z}\right].}
\]
Its singular planar-collapse law is
\[
\boxed{p(t)=1-\frac{12(\sqrt3+3)}{\pi(3+2\sqrt3)}t+O(t^3),\qquad t\downarrow0.}
\]
At \(t=1/\sqrt2\), the polytope is a Euclidean regular octahedron, and its known hexagonal-shadow probability is \(4\arctan(\sqrt2/5)/\pi\). At the opposite endpoint \(p(t)\to1/2\) as \(t\to\infty\). Consequently this regular-octahedron value is neither the maximum nor the minimum among all affine octahedra: values near the planar-hexagon limit are almost one, whereas the present continuous family attains a global minimum at an interior parameter. The location and uniqueness of the minimum are not claimed.

## Assumptions and scope
The three generating vectors \(v_i\) are linearly independent whenever \(t>0\); thus \(K_t\) is a genuine affine image of a regular octahedron. The metric is Euclidean, and the random projection plane has normalized rotation-invariant measure. A generic shadow of any three-dimensional cross-polytope with six vertices is centrally symmetric and has either four or six vertices. Nongeneric collinearities have Haar measure zero. \(t=0\) is excluded, because then \(K_t\) is two-dimensional; the displayed limit is one-sided. In contrast to orthogonally stretched cross-polytopes, the generators here satisfy \(v_i\cdot v_j=t^2-1/2\) for \(i\ne j\).

## Proof
Let \(V\) have columns \(v_1,v_2,v_3\). For a unit normal \(u\), the three projected vectors \(q_i\) obey \(\sum_i g_i q_i=0\), where \(g=V^{-1}u\). Outside null sets, the antipodal pair \(\pm q_i\) fails to be exposed vertices precisely when \(|g_i|\ge |g_j|+|g_k|\). These three failure events are mutually exclusive. Hence all six projected vertices survive exactly when the positive triple \((|g_1|,|g_2|,|g_3|)\) satisfies all strict triangle inequalities.

On each orthant of the \(g\)-coordinates, the triangle-inequality cone is simplicial: its generators in \(g\)-space have absolute coordinate vectors \((1,1,0)\), \((1,0,1)\), \((0,1,1)\), with the three orthant signs attached. Their images under \(V\) determine eight disjoint spherical triangles on the sphere of normals (up to null boundaries). Two sign patterns have all signs equal. Their ray generators are \(v_1+v_2\), \(v_1+v_3\), \(v_2+v_3\) or their common negatives. Each has norm \(L\), each pair has dot product \(4t^2-1/2\), and the absolute triple determinant is \(Y\). The spherical solid angle of each is
\[
\Omega_{\rm same}=2\operatorname{atan2}\bigl(Y,L^3+3(4t^2-1/2)L\bigr)=2\operatorname{atan2}(Y,X).
\]
The remaining six mixed-sign patterns are congruent under the triangular symmetry and overall sign reversal. One has ray generators \(v_1+v_2\), \(v_1-v_3\), \(v_2-v_3\). Their norms are \(L,\sqrt3,\sqrt3\); the three distinct dot products are all \(3/2\); and the absolute determinant remains \(Y\). Therefore
\[
\Omega_{\rm mixed}=2\arctan\left(\frac{Y}{(9/2)L+3\sqrt3}\right)=2\arctan(Y/Z).
\]
The used trihedral-angle formula is \(\Omega=2\operatorname{atan2}(|\det(a,b,c)|,|a||b||c|+(a\cdot b)|c|+(a\cdot c)|b|+(b\cdot c)|a|)\); it is valid here even when the denominator for the all-same class is negative, which is why the specified angle branch is essential. Dividing \(2\Omega_{\rm same}+6\Omega_{\rm mixed}\) by the sphere area \(4\pi\) yields the stated exact probability.

As \(t\downarrow0\), the all-same cone has \(\Omega_{\rm same}=2\pi-12\sqrt3\,t+O(t^3)\), while the mixed cone has \(\Omega_{\rm mixed}=6\sqrt3\,t/(9/2+3\sqrt3)+O(t^3)\). Combining them gives \(1-p(t)=[6\sqrt3-9\sqrt3/(9/2+3\sqrt3)]t/\pi+O(t^3)\), which simplifies to the coefficient displayed in the finding. As \(t\to\infty\), the all-same solid angle tends to zero, whereas the mixed one tends to \(2\arctan(1/\sqrt3)=\pi/3\); hence \(p(t)\to1/2\). At \(t=1/\sqrt2\), the mutually perpendicular, equal-length generators define the regular octahedron; substitution simplifies to the known value. The exact continuous expression has endpoint limits \(1\) and \(1/2\), each strictly above its value at \(t=1/\sqrt2\), so it necessarily has an interior global minimizer by compactness of a suitable closed subinterval; no uniqueness argument is needed.

## Verification
Run `python3 verify.py` with standard-library Python. It independently samples random Gaussian sphere normals, projects all six spatial vertices into the corresponding random orthonormal planes, counts projected convex-hull vertices by a monotone-chain hull algorithm, and compares the resulting proportions with the exact solid-angle expression at five positive parameters. It also checks the linear collapse coefficient numerically and the known regular-octahedron specialization. The finite Monte Carlo verification does not establish the exact law; the spherical-cone proof does.

## Relationship to prior work
Random planar shadows and regular cross-polytope probabilities were treated by Finch (2012), while Feldman–Klain (2008) explains solid angles as random projection probabilities. The published triaxial-octahedron result named below proves a sharp hexagonal-shadow bound for **pairwise orthogonal** generators, and explicitly excludes nonorthogonal affine octahedra. Its known regular-octahedron value is an input/check, not the novelty claim. Here the generators are oblique except at one parameter, and the contribution is the exact whole one-parameter oblique law with its planar-collapse coefficient and contrasting endpoint behavior. The full multi-parameter solid-angle method is classical; no claim of invention of that method is made. Historical coverage of the particular symmetric oblique family remains an uncertainty.

## Limitations
Only the displayed equiangular one-parameter affine family is classified, not all oblique octahedra. No claim of uniqueness of the interior minimizer, no non-Haar orientation law, and no extension to higher dimensions is made. The limiting degenerate hexagon at \(t=0\) itself is not a three-dimensional octahedron. The mathematical argument is analytical, but literature priority is based on sources actually checked and is not independently certified.

## References
1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (2012-03-12), https://arxiv.org/abs/1203.2464 .
2. D. V. Feldman and D. A. Klain, *Angles as Probabilities*, arXiv:0809.3459 (2008-09-19), https://arxiv.org/abs/0809.3459 .
3. *Sharp triaxial octahedron shadow bound and quadratic shape stability*, published geometric research finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-triaxial-octahedron-shadow-bound-and-quadratic-shape-stabi--c544249c351b .
