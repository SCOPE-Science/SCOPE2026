# Exact Haar section-type probabilities of the regular dodecahedron

## Finding

Let \(D\subset\mathbb R^3\) be a regular dodecahedron centered at the origin, and let \(u\) be uniform on the unit sphere \(S^2\). For almost every \(u\), let \(N(u)\) be the number of vertices (equivalently, sides) of the planar polygon \(D\cap u^\perp\). Put
\[
 a=\arccos(1/3),\qquad b=\arccos(\sqrt5/3).
\]
Then \(N(u)\in\{6,8,10\}\) almost surely, with the **complete exact probability law**
\[
\begin{aligned}
\Pr(N=6)&=10-\frac{15}{\pi}(a+b)=0.638408811559341\ldots,\\
\Pr(N=8)&=\frac{15}{\pi}(2a+b-\pi)=0.238989468899770\ldots,\\
\Pr(N=10)&=6-\frac{15}{\pi}a=0.122601719540890\ldots.
\end{aligned}
\]
These probabilities also describe the numbers of vertices of a uniformly oriented planar orthogonal shadow of the polar regular icosahedron (by planar section–projection polarity), with the appropriate combinatorial duality.

## Assumptions and scope

The plane always passes through the center; its unoriented normal line is Haar-uniform in the space of lines through the origin. Concretely, \(u\) is uniformly sampled by normalized area on \(S^2\), and \(u\) and \(-u\) produce the same section. Boundary directions for which the plane contains a vertex have spherical measure zero. The result is independent of a uniform rescaling of \(D\); no affine-offset or width weighting is used.

For explicit computations, let \(\varphi=(1+\sqrt5)/2\) and take the convex hull of the twenty vectors
\[
 (\pm1,\pm1,\pm1),\quad
 (0,\pm\varphi^{-1},\pm\varphi),\quad
 (\pm\varphi^{-1},\pm\varphi,0),\quad
 (\pm\varphi,0,\pm\varphi^{-1}),
\]
where signs in each indicated family are independent. All these vectors lie on the sphere of radius \(\sqrt3\), and their convex hull is the regular dodecahedron.

## Proof

**1. Sign chambers and crossed edges.** Every dodecahedral vertex occurs in an antipodal pair, giving ten representative vectors \(v_1,\ldots,v_{10}\). Away from the ten great circles \(u\cdot v_i=0\), the signs of all twenty vertex dot products with \(u\) are locally constant. A dodecahedral edge crosses the central plane precisely when its endpoints have opposite signs. Thus the polygon vertex count is constant in every open great-circle chamber and equals the number of sign-discordant edges, because each transverse intersection with an edge is a distinct section vertex.

**2. Exhaustive exact chamber classification.** In the coordinate realization above, each coordinate lies in \(\mathbb Q(\varphi)\). The squared distance between the endpoints of any dodecahedral edge is \(4(2-\varphi)\); enumerating the closest vertex pairs gives the thirty edges. The ten great circles have no triple intersection: for any three representative vertices their exact determinant is nonzero. Each spherical chamber vertex is therefore one of the two normalized cross products of a pair of representative vertices: there are \(2\binom{10}{2}=90\) such intersection directions. Enumerating the \(2^{10}\) possible sign vectors, retaining only nonempty two-dimensional spherical chambers, and testing edge sign discordance yields exactly the following classification:

| Section vertices \(N\) | Spherical chambers | Edges per chamber | Multiset of chamber angles |
|:---:|:---:|:---:|:---|
| \(6\) | \(20\) | \(6\) | \(3\) of \(\pi-a\), \(3\) of \(\pi-b\) |
| \(8\) | \(60\) | \(3\) | \(2\) of \(a\), \(1\) of \(b\) |
| \(10\) | \(12\) | \(5\) | \(5\) of \(\pi-a\) |

Here **edges per chamber** means the number of sides of the spherical cell, not the number of edges of the planar section. This finite classification has an independently executable exact algebraic certificate in `check.py`. All combinatorial predicates are evaluated in the ordered field \(\mathbb Q(\sqrt5)\), not by floating-point tolerance. In particular, the certificate provides an exhaustive enumeration and checks that \(20+60+12=92\), as independently required by the generic arrangement of ten great circles, which has \(10^2-10+2=92\) regions. To obtain chamber angles, if \(\sigma_i v_i\) and \(\sigma_j v_j\) are the inward hemisphere normals for the two meeting boundary arcs, their spherical interior angle is \(\pi-\arccos(\sigma_i\sigma_j v_i\cdot v_j/3)\). The exact dot products in the certificate give the tabulated multisets.

**3. Exact area integration.** For a convex spherical \(k\)-gon on the unit sphere with internal angles \(\theta_1,\ldots,\theta_k\), Girard's formula gives area \(\sum_i\theta_i-(k-2)\pi\). Hence one chamber of the three types has respective areas
\[
 A_6=2\pi-3a-3b,\quad
 A_8=2a+b-\pi,\quad
 A_{10}=2\pi-5a.
\]
Multiplying by their chamber multiplicities \(20\), \(60\), \(12\), and dividing by the full sphere area \(4\pi\) proves the three displayed probabilities. Direct algebra gives \(20A_6+60A_8+12A_{10}=4\pi\), providing a normalization identity. All three areas are strictly positive.

## Verification

Run `python3 check.py` from the extracted file directory (Python 3 standard library only). The checker reconstructs all twenty vertices and thirty edges in \(\mathbb Z[\varphi]\), proves the absence of triple intersections, exhausts all 1024 sign codes and all 90 pair-intersection rays, checks strict chamber feasibility, tabulates the exact spherical-angle dot products, and checks the 92-cell total. Algebraic signs are compared using an explicitly proved rational enclosure for \(\varphi\). The spherical-area formulas are evaluated separately after these exact predicates; floating-point evaluation is **only** for the displayed decimals and the final numerical sum check. Successful output ends with `EXACT_ALGEBRAIC_ARRANGEMENT_CERTIFICATE_PASSED`.

## Relationship to prior work

Brandenburg, De Loera and Meroni (2023) develop slicing-chamber decompositions for general polytopes and illustrate volume-optimal dodecahedron sections. Their main chamber theorem provides the general framework, but their inspected article does not give Haar area weights or these complete sidedness probabilities. Classical descriptions of dodecahedral central hexagons and decagons concern special symmetry axes and do not determine the random-direction distribution. Published work on **central sections of the dual icosahedron** evaluates a different section problem; polarity relates the present law instead to **orthogonal projections of the icosahedron**. These geometric distinctions are essential for the comparison. The exact spherical-arrangement classification and its integrated probability law are the contribution here.

## Limitations

The claim is specific to central planar sections of the three-dimensional regular dodecahedron. It does not cover affine planes conditioned to hit the solid, nonuniform directions, deformed dodecahedra, or arbitrary polyhedra. Published specialized stereology and older projection tables may contain equivalent formulas not located in the bounded searches; therefore historical priority is not guaranteed. No independent mathematical audit has been performed.

## References

1. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, publicly posted April 27, 2023. Full article: https://arxiv.org/html/2304.14239v1.
2. E. W. Weisstein, *Regular Dodecahedron*, MathWorld, https://mathworld.wolfram.com/RegularDodecahedron.html (coordinates and classical special-axis sections).
3. *Exact Haar polygon-type law for central icosahedron sections*, publicly indexed mathematical result; compared solely as a different dual-polyhedron section problem. (Its title describes a central section, not a projection.)
