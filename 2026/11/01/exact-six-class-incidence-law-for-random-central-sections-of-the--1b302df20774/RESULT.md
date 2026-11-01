# Exact six-class incidence law for random central sections of the regular truncated tetrahedron

## Finding
Let \(T\) be the regular truncated tetrahedron, obtained by one-third truncation of each vertex of a regular tetrahedron, centered at the origin. Let \(U\) be uniformly distributed on the unit sphere in \(\mathbb R^3\), and cut \(T\) by the plane \(U^\perp\). Write \(J\) and \(H\) for the numbers of its four triangular and four hexagonal faces intersected in positive-length segments. Almost surely the joint type \((J,H)\) lies in exactly six classes. Put
\[
 \alpha=\arccos(1/11),\quad \beta=\arccos(5/11),\quad
 \gamma=\arccos(7/11),\quad \delta=\arccos(9/11).
\]
The *exact* joint probabilities are
\[
\begin{aligned}
\mathbb P(J=0,H=4)&=3-6(\gamma+\delta)/\pi,\\
\mathbb P(J=1,H=3)&=6(2\alpha+\beta-\gamma-\pi)/\pi,\\
\mathbb P(J=1,H=4)&=12(-\alpha+\gamma+\delta)/\pi,\\
\mathbb P(J=2,H=3)&=6(2\pi-2\alpha-2\beta-\gamma)/\pi,\\
\mathbb P(J=2,H=4)&=6(2\alpha+\gamma-\delta-\pi)/\pi,\\
\mathbb P(J=3,H=3)&=6\beta/\pi-2.
\end{aligned}
\]
All six probabilities are strictly positive. The generic section therefore has precisely \(J+H\in\{4,5,6\}\) sides, with probabilities respectively \(0.21593608531264\), \(0.52024746523894\), and \(0.26381644944842\) (rounded). The full joint law separates geometrically distinct sections with the same side number.

## Assumptions and scope
Take four vertices \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), \(v_3=(-1,-1,1)\). Its truncation is the convex hull of twelve points \(b_{ij}=2v_i+v_j\), for ordered distinct indices \(i,j\in\{0,1,2,3\}\). This is a uniform scaling of the standard one-third truncation, with centroid the origin. Its four triangular faces have vertex sets \(\{b_{ij}:j\ne i\}\), and its four hexagonal faces have vertex sets \(\{b_{jk}:j,k\ne i,\ j\ne k\}\), one for each \(i\). All vertices have squared Euclidean norm \(11\). Degenerate orientations with \(U\cdot b_{ij}=0\) form a finite union of great circles, hence have spherical measure zero. The theorem concerns central planes, not randomly translated planes or orthogonal projections.

## Proof
**Step 1 (finite sign cells).** Away from the degeneracy great circles, a central section meets the relative interior of a face if and only if its vertex dot products with \(U\) have both signs. The set of directions realizing any fixed strict sign vector \(\sigma\in\{-1,+1\}^{12}\) is a convex spherical polygon, if nonempty. It is the spherical intersection with the pointed polyhedral cone \(C_\sigma=\{x:\sigma_{ij}b_{ij}\cdot x\ge0\text{ for all }i\ne j\}\). Every extreme ray of a full-dimensional such cone is a (positive or negative) primitive cross product of two of the twelve vertex vectors. Computing these integer cross products yields exactly \(132\) candidate oriented rays.

For each of all \(2^{12}=4096\) sign vectors, retain the candidate rays satisfying all twelve inequalities. There is a full-dimensional cone precisely when the sum of its retained generating rays has strict positive dot product with every signed constraint normal. Indeed these cones are pointed, all their extreme rays occur among the retained candidates, and positivity of the sum is equivalent to every inequality being nonidentical on the cone. The provided standalone exact-integer program exhausts this test, identifying exactly \(134\) nonempty open spherical chambers.

**Step 2 (their spherical areas).** Each chamber boundary edge lies on one of the great circles \(b_{ij}\cdot U=0\). The enumeration verifies that the boundary rays and great-circle arcs form a single cycle, so it reconstructs each polygon without numerical approximation. If consecutive inward edge normals are \(\sigma_{ij}b_{ij}\) and \(\sigma_{k\ell}b_{k\ell}\), their inner product is an integer \(q\) and both have squared norm \(11\). The corresponding polygon interior angle is \(\pi-\arccos(q/11)\). Thus Girard's theorem gives each chamber the exact area
\[
 2\pi-\sum_{\text{chamber corners}}\arccos(q/11).
\]
The complete grouping of the \(134\) chambers is recorded in `incidence_certificate.json` as counts of the exact angular coefficients, not just floating-point approximations.

**Step 3 (face-type grouping).** The full enumeration produces the following \((J,H)\)-classes, number of chambers, and multiplicities of terms \(\arccos(q/11)\) in the total angular sum:

| \((J,H)\) | Chambers | Multiplicities \((q:\text{count})\) |
| --- | ---: | --- |
| \((0,4)\) | 6 | \(7:24,\ 9:24\) |
| \((1,3)\) | 24 | \(-5:24,\ -1:48,\ 7:24\) |
| \((1,4)\) | 48 | \(-9:48,\ -7:48,\ 1:48\) |
| \((2,3)\) | 24 | \(1:48,\ 5:48,\ 7:24\) |
| \((2,4)\) | 24 | \(-7:24,\ -1:48,\ 9:24\) |
| \((3,3)\) | 8 | \(-5:24\) |

Consequently each class probability is its aggregated spherical area divided by \(4\pi\). Reducing all negative arguments using \(\arccos(-z)=\pi-\arccos(z)\) gives exactly the six displayed formulas. For a generic central section every polygon vertex lies in the relative interior of one polyhedron edge, and every polygon side is supported by one polyhedron face. The code separately enumerates all \(18\) polyhedron edges and verifies for each of the \(134\) chambers that the count of sign-crossing polyhedron edges equals \(J+H\). This completes the joint and marginal classifications. All orientation cells have positive area; hence all six classes genuinely occur.

## Verification
Run `python incidence_certificate.py` with Python 3 and NumPy. It uses integer coordinates and exact integer inequalities, dot products and cross products to exhaust \(4096\) sign patterns, reconstructs the complete boundary cycle for every realized chamber and evaluates the angular multiplicities. Numerical calls to \(\arccos\) occur only when printing approximate spherical areas, and are not used to decide any incidence type, combinatorial cell, or angular coefficient. The checker asserts the exact six-class chamber counts and the area normalization within floating-point rounding error. The resulting `incidence_certificate.json` provides the expected chamber and angle frequency table for cross-checking. A proof of the finite enumeration's completeness is given in the extreme-ray argument above; the executable enumerates every sign vector, not sampled orientations.

## Relationship to prior work
Zefiro's geometric treatment of Archimedean truncated tetrahedra describes their geometry and the triangle/hexagon face structure, but not a Haar central-section face-incidence probability distribution. Chen, Jiao and Torquato (2014) investigate equilibrium packing phases of congruent truncated tetrahedra, not the central plane-section law. A search for equivalent stochastic-geometric formulations and relevant existing exact central-section laws on different solids found no theorem implying this six-class law. This is a best-knowledge originality assessment, not a guarantee of historical priority; older stereological tables may require further independent examination.

## Limitations
The theorem applies to a regular truncated tetrahedron, invariantly oriented central planes, and generic sections. It does not determine random translated-section frequencies, areas or perimeters, or other truncation ratios. The exact formulas rely on the fully enumerated small great-circle arrangement. Independent scientific audit and comprehensive historical-priority verification have not been performed.

## References
1. L. Zefiro, *Vertex- and edge-truncation of the Platonic and Archimedean solids leading to vertex-transitive polyhedra*, VisMath archive, https://www.mi.sanu.ac.rs/vismath/zefirosept2011/_truncation_Archimedean_polyhedra.htm (geometric source; publicly dated exact day not verified).
2. D. Chen, Y. Jiao and S. Torquato, *Equilibrium Phase Behavior and Maximally Random Jammed State of Truncated Tetrahedra*, arXiv:1406.1535, first publicly submitted 2014-06-05, https://arxiv.org/abs/1406.1535 (packing context, not a proof of this theorem).
