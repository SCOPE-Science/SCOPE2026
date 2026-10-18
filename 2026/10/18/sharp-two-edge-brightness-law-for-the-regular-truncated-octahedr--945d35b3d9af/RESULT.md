# Sharp two-edge brightness law for the regular truncated octahedron

## Finding
Let \(T\subset\mathbb R^3\) be the Archimedean truncated octahedron with the 24 vertices obtained by permuting \((0,\pm1,\pm2)\), with all independent sign choices. Let \(U\) be uniform on \(S^2\) and let \(B(U)\) be the area of the orthogonal projection of \(T\) onto \(U^\perp\). Write \(F(t)=\mathbb P(B(U)\le t)\). Then
\[
B(u)=2\|u\|_1+6\max\{2\|u\|_\infty,\|u\|_1\},
\qquad
8\sqrt2\le B(u)\le2\sqrt{51}.
\]
Exactly 12 signed coordinate-face-diagonal directions attain the lower endpoint, and exactly 24 signed permutations of \((7,1,1)/\sqrt{51}\) attain the upper endpoint.

Put \(t_c=10\sqrt2\). The **complete upper brightness tail** is exactly
\[
F(t)=\frac{6t}{\sqrt{51}}-11,\qquad t_c\le t\le2\sqrt{51},
\]
so the brightness density is constant \(6/\sqrt{51}\) throughout this maximal terminal interval. A second exact branch extends it to \(14\le t\le t_c\):
\[
F(t)=\frac{6t}{\sqrt{51}}-11+\frac6\pi\,\mathcal L(t),
\]
where \(\mathcal L(t_c)=0\) and, for \(14\le t<t_c\),
\[
\mathcal L(t)=2\left[\pi-\arccos\left(\frac{196-t^2}{204-t^2}\right)\right]
-\frac{2t}{\sqrt{51}}\arccos\left(\frac{t}{\sqrt{50(204-t^2)}}\right).
\]
The linear upper-tail formula fails immediately below \(t_c\), with the sharp, nonanalytic correction
\[
F(t_c-\varepsilon)-\left(\frac{6(t_c-\varepsilon)}{\sqrt{51}}-11\right)
=\frac8\pi\sqrt{\frac2{t_c}}\,\varepsilon^{3/2}+o(\varepsilon^{3/2})
\qquad(\varepsilon\downarrow0).
\]
The opposite endpoint has a different universality exponent and an explicit coefficient:
\[
\mathbb P(B(U)\le8\sqrt2+\varepsilon)
=\frac{7\sqrt2}{64\pi}\,\varepsilon^2+o(\varepsilon^2)
\qquad(\varepsilon\downarrow0).
\]
The usual Cauchy projection identity also gives \(\mathbb EB(U)=3+6\sqrt3\); this mean is a classical consequence and is included for normalization, not claimed as new.

## Assumptions and scope
All Euclidean lengths and areas use the explicit coordinate normalization above; multiplying the entire polytope by \(a>0\) multiplies \(B\), both endpoints and both branch thresholds by \(a^2\). The probability is normalized spherical area on \(S^2\). The terminal CDF branches are asserted only on their specified closed intervals, and the endpoint expansions are one-sided. The result does not assert an elementary formula for the intervening CDF on \((8\sqrt2,14)\).

## Proof
**1. Surface geometry and support representation.** The six square facets of \(T\) are in the planes \(x_i=\pm2\) and each has area \(2\). The eight regular hexagon facets have unit normals \((\pm1,\pm1,\pm1)/\sqrt3\) and each has area \(3\sqrt3\). Cauchy's projected-area identity therefore gives
\[
B(u)=2\sum_{i=1}^3|u_i|+\frac32\sum_{\sigma\in\{\pm1\}^3}|\sigma\cdot u|.
\]
For \(x\ge y\ge z\ge0\), the eight-term sum is \(8x\) when \(x\ge y+z\), and \(4(x+y+z)\) otherwise. The first displayed formula follows in every orthant. Equivalently,
\[
B(u)=\max_{v\in\mathcal A\cup\mathcal D}v\cdot u,
\]
where \(\mathcal A\) consists of all 24 signed permutations of \((14,2,2)\), and \(\mathcal D\) consists of the eight signed vectors \((8,8,8)\).

**2. Exact extrema.** The norms of vectors in \(\mathcal A\) and \(\mathcal D\) are \(2\sqrt{51}\) and \(8\sqrt3\), respectively. Thus the maximal brightness is \(2\sqrt{51}\) and its 24 distinct maximizing directions are \(v/(2\sqrt{51})\), for \(v\in\mathcal A\). To find the minimum, order absolute coordinates as \(x\ge y\ge z\ge0\) and put \(q=y+z\). If \(x\le q\), then \(B=8(x+y+z)\ge8\sqrt2\): for a fixed sum \(s=x+y+z\), the constraints \(x\le s/2\), \(y,z\le x\) give \(x^2+y^2+z^2\le s^2/2\), with equality exactly at permutations of \((s/2,s/2,0)\). If \(x\ge q\), then \(B=14x+2q\), with \(x^2+q^2\ge1\) and \(x\ge q\). Homogeneity reduces minimization to the unit-circle arc \(x=\cos\theta,q=\sin\theta\), \(0\le\theta\le\pi/4\). The concave function \(14\cos\theta+2\sin\theta\) is minimized at an endpoint, giving \(\min\{14,8\sqrt2\}=8\sqrt2\). Equality forces \(yz=0\) and \(x=q=1/\sqrt2\). Independent signs and permutations yield 12 minimizing directions.

**3. Exact terminal cap count.** For \(t>8\sqrt3\), the vectors in \(\mathcal D\) cannot satisfy \(v\cdot u>t\). Hence the event \(B(U)>t\) is a union of 24 spherical caps centered at \(v/(2\sqrt{51})\), all with angular radius \(\alpha(t)=\arccos(t/(2\sqrt{51}))\). Among distinct \(v,w\in\mathcal A\), the largest inner product is \(196\), occurring at exactly 24 unordered pairs (one minority-sign flip), and the next largest is \(188\), occurring at 12 unordered pairs. Two equal caps centered at \(v,w\) first overlap when \(t<\sqrt{(204+v\cdot w)/2}\). It follows that for \(t\ge10\sqrt2=\sqrt{(204+196)/2}\), all 24 caps are disjoint up to null boundaries. One spherical cap occupies probability \(\tfrac12(1-t/(2\sqrt{51}))\), so
\[
F(t)=1-24\cdot\frac12\left(1-\frac{t}{2\sqrt{51}}\right)
=\frac{6t}{\sqrt{51}}-11.
\]
For \(14<t<10\sqrt2\), exactly the 24 nearest cap pairs overlap, and all triple intersections have spherical area zero because every triple contains a pair of vectors with inner product at most \(188\). Inclusion-exclusion is then exact. The overlap of any nearest pair is a spherical lens with center separation \(\delta=\arccos(49/51)\) and equal angular radius \(\alpha(t)\). The spherical cosine rule gives half-arc angle
\[
\varphi=\arccos\left(\frac{t}{\sqrt{50(204-t^2)}}\right)
\]
and the angle between its inward circle radii at either boundary intersection is
\[
\gamma=\arccos\left(\frac{196-t^2}{204-t^2}\right).
\]
Gauss--Bonnet for the two small-circle arcs gives lens area \(2(\pi-\gamma)-4\cos\alpha\,\varphi=\mathcal L(t)\). Adding the 24 overlaps, each with spherical probability area divided by \(4\pi\), yields the claimed second branch. The same formula extends continuously to the stated endpoints.

**4. Sharp first overlap singularity.** For a nearest pair take \(v_\pm=(14,\pm2,2)\) and their tangency point \(u_0=(7,0,1)/\sqrt{50}\). Choose orthonormal tangent directions \(e_1=(0,1,0)\) and \(e_2=(-1,0,7)/\sqrt{50}\), and set \(u(a,b)=\sqrt{1-a^2-b^2}\,u_0+a e_1+b e_2\). The two cap inequalities at level \(t_c-\varepsilon\) become the single condition
\[
t_c\sqrt{1-a^2-b^2}-2|a|>t_c-\varepsilon.
\]
The overlap has \(a=O(\varepsilon)\), \(b=O(\sqrt\varepsilon)\). Its spherical area element is \((1-a^2-b^2)^{-1/2}da\,db\), and rescaling yields one-lens area
\[
\frac43\sqrt{\frac2{t_c}}\,\varepsilon^{3/2}+o(\varepsilon^{3/2}).
\]
There are exactly 24 such lenses. Multiplication by \(24/(4\pi)\) gives the stated cusp coefficient. In particular the linear CDF cannot extend below \(t_c\).

**5. Lower-edge asymptotic.** At a minimizer \(u_0=(1,1,0)/\sqrt2\), take tangent basis \(e_1=(1,-1,0)/\sqrt2\), \(e_2=(0,0,1)\). For sufficiently small \(a,b\) the exact formula is
\[
B(u(a,b))=8\sqrt2\sqrt{1-a^2-b^2}+8|b|
+6\max\{0,\sqrt2|a|-|b|\}.
\]
The positively homogeneous first-order increment is \(L(a,b)=8|b|+6\max\{0,\sqrt2|a|-|b|\}\). Its unit sublevel set has planar area \(7\sqrt2/192\): in the first quadrant, split at \(b=\sqrt2 a\), giving the two triangles with areas \(\sqrt2/256\) and \(\sqrt2/192\), then multiply their sum by four. The difference between the true increment and \(L(a,b)\) is \(O(a^2+b^2)\), while the spherical area element tends to \(da\,db\). Rescaling by \(\varepsilon\), all 12 isolated minimizers therefore contribute
\[
\frac{12}{4\pi}\cdot\frac{7\sqrt2}{192}\varepsilon^2+o(\varepsilon^2)
=\frac{7\sqrt2}{64\pi}\varepsilon^2+o(\varepsilon^2).
\]
No other directions contribute to this endpoint asymptotic by continuity and the complete minimizer classification.

## Verification
The accompanying standalone Python program `check_brightness.py` requires only the standard library. It independently constructs all 24 vertices, projects them orthogonally, builds their planar convex hull and compares its area with the exact support formula for 800 deterministic seeded spherical directions. It exhaustively checks the 24 candidate upper normals, their 24 nearest pairs, 12 second-nearest pairs, and all endpoint orbits. It also compares both exact terminal CDF branches with 300,000 reproducibly sampled Haar directions and independently checks the first-overlap asymptotic at four scales. The analytic argument, not sampling, establishes the exact CDF and the endpoint limits. Cauchy's formula yields \(\mathbb EB=(12+24\sqrt3)/4\), independently checking facet normalization.

## Relationship to prior work
The 2026 work of Abas on random width and brightness establishes a general polyhedral density framework, an exact width law for the regular truncated octahedron and a brightness law for the regular tetrahedron. The present calculation concerns instead **the projected-area distribution of the truncated octahedron**. It supplies the explicit finite cap arrangement, the exact thresholds \(14\) and \(10\sqrt2\), the maximal linear terminal law, the three-halves overlap cusp and the quadratic opposite-edge constant. The general framework motivates the question but its retrieved abstract does not give these quantities. Because its full text was not accessible in this study, an equivalent uninspected calculation remains a specific priority risk. The 2026 isoperimetric characterization of the Archimedean truncated octahedron by Hales and Song provides independent motivation for this distinguished polytope but addresses surface-area optimization, not projection distributions. Earlier exact octahedral width and Platonic shadow-variance results concern different statistics or different solids; marginal width or variance statements do not determine the present distribution.

## Limitations
The theorem gives the full upper CDF only from \(t=14\) to the global maximum and a sharp lower-end asymptotic, not an elementary global CDF on \((8\sqrt2,14)\). The numerical checks do not constitute a general proof. The highly relevant, 92-page 2026 polyhedral-density manuscript could not be read in full; its appendices might contain a stronger or equivalent specialization, so formal publication priority should be independently checked. None of the results assert geometric uniqueness from the brightness distribution or stability under arbitrary polytope perturbations.

## References
1. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (public bibliographic record dated 2026-08-10; inspected abstract and metadata). https://arxiv.org/abs/2609.26202
2. Thomas Hales and Lark Song, *The Truncated Octahedral Conjecture*, arXiv:2609.00997 (2026-09-01; inspected abstract). https://arxiv.org/abs/2609.00997
3. Standard Cauchy projection-area formula for convex bodies, via the surface-area measure; see R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded edition, Cambridge University Press (2014), chapter on projections and surface-area measures.
