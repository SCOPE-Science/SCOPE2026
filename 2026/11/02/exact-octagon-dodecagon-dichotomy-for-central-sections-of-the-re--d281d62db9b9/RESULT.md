# Exact octagon–dodecagon dichotomy for central sections of the regular rhombicuboctahedron

## Finding
Let \(a=1+\sqrt2\), and let \(P\subset\mathbb R^3\) be the convex hull of all \(24\) signed coordinate permutations of \((a,1,1)\), the regular small rhombicuboctahedron. For a generic unit normal \(u\), write \(N(u)\) for the number of sides of the central planar section \(P\cap u^\perp\). Sort the absolute coordinates of \(u\) as \(x>y>z>0\). Then the exact pointwise classification is
\[
N(u)=\begin{cases}8,&x>ay+z,\\12,&x<ay+z.\end{cases}
\]
In particular, generic central decagons never occur. Under a uniform direction on the unit sphere, put \(\theta=\arccos(1/\sqrt{5+2\sqrt2})\). The complete law is
\[
\Pr(N=8)=\frac{24\theta}{\pi}-9\approx0.207863937034156,\qquad
\Pr(N=12)=10-\frac{24\theta}{\pi}\approx0.792136062965844.
\]
Thus \(\mathbb E N=48-96\theta/\pi\approx11.168544251863377\) and \(\operatorname{Var}(N)=16\Pr(N=8)\Pr(N=12)\approx2.634504331437062\).

## Assumptions and scope
The polyhedron is the regular small rhombicuboctahedron, with edge length \(2\), \(24\) vertices, \(48\) edges, \(8\) triangular faces and \(18\) square faces. A normal is generic when the plane \(u^\perp\) avoids every vertex and none of the absolute coordinate equalities used to choose a symmetry chamber hold. These exclusions have spherical measure zero. Each nonexceptional section is a convex polygon, and the number of its vertices equals the number of polyhedral edges with endpoints of opposite signs under \(v\mapsto u\cdot v\). Directions are sampled with rotation-invariant spherical surface measure; antipodal normals represent the same unoriented plane.

## Proof
**1. Edge structure.** Every vertex is a signed coordinate permutation of \((a,1,1)\). Its four edge-neighbors arise either by flipping the sign of one small coordinate, or by exchanging the location of the large coordinate with one of the two small coordinates while retaining the coordinate signs. Each of these segments has Euclidean length \(2\), since \(\sqrt2(a-1)=2\). Counting gives \(24\) sign-flip edges and \(24\) exchange edges, forming the standard edge graph of the regular rhombicuboctahedron. The accompanying exact checker reconstructs all \(48\) edge pairs directly in \(\mathbb Q(\sqrt2)\) and verifies degree four at every vertex.

**2. Reduction to one fundamental direction sector.** Signed coordinate permutations preserve \(P\), so it suffices to take the normal proportional to \((1,v,w)\) with \(0<w<v<1\). In the triangular parameter domain \(0\le w\le v\le1\), the only possible nonconstant vertex-sign boundaries, up to multiplication by \(-1\), are
\[
L_1=av-w-1,\quad L_2=av+w-1,\quad
L_3=aw-v-1,\quad L_4=aw+v-1.
\]
The lines cut the parameter triangle into exactly six open polygons. The exact vertex-sign calculation gives the following exhaustive sign table, where signs are ordered as \((L_1,L_2,L_3,L_4)\):

| Boundary-sign pattern | Number of section sides |
| --- | ---: |
| \((-,-,-,-)\) | \(8\) |
| \((-,+,-,-)\) | \(12\) |
| \((-,+,-,+)\) | \(12\) |
| \((+,+,-,-)\) | \(12\) |
| \((+,+,-,+)\) | \(12\) |
| \((+,+,+,+)\) | \(12\) |

This is an exact finite sign enumeration, not a sample of directions. In each polygon, the checker clips against the four lines using rational arithmetic in \(\mathbb Q(\sqrt2)\), tests that the sign of each of the original \(24\) vertex linear forms is constant on that whole polygon by checking all its corners, and counts exactly the sign-changing edges. Since a linear form cannot change sign over a convex polygon whose vertices all have the same weak sign, this proves the table on every open chamber. The only octagonal chamber is \(L_2<0\), equivalent to \(x>ay+z\); the remaining chambers are dodecagonal.

**3. Spherical area.** The fundamental signed-permutation sector occupies \(1/48\) of the unit sphere. Inside it, the octagonal normals form the spherical triangle defined by
\[
z\ge0,\qquad y-z\ge0,\qquad x-ay-z\ge0.
\]
Its three inward boundary normals are \((0,0,1)\), \((0,1,-1)\), and \((1,-a,-1)\). Their exact scalar products show that the spherical triangle has interior angles \(\pi/4,\theta,\theta\), where \(\cos\theta=1/\sqrt{5+2\sqrt2}\). Girard's theorem therefore gives area \(\Omega=2\theta-3\pi/4>0\). There are \(48\) congruent copies disjoint up to measure zero, so \(\Pr(N=8)=48\Omega/(4\pi)=24\theta/\pi-9\). The complementary probability and moment identities follow immediately.

## Verification
Run `python3 verify_rhombicuboctahedron.py` with Python 3. The standalone checker uses exact fractions in \(\mathbb Q(\sqrt2)\) for all vertex, edge, clipping, chamber, sign and spherical-angle algebraic identities. It verifies all \(16\) candidate sign patterns, six positive-area sectors, the exact eight-or-twelve classification, and the three bounding normals. An independent Gaussian-direction diagnostic evaluates \(80{,}000\) normals against the original \(48\)-edge graph and the derived threshold, with no discrepancies; that diagnostic is corroboration, not the proof of the all-direction statement. All numerical probabilities are evaluations of the proved closed formula.

## Relationship to prior work
Berlow, Brandenburg, Meroni and Shankar study semialgebraic intersection bodies of polytopes, a different geometric observable. Brandenburg, De Loera and Meroni develop general chamber decompositions for polytope sections, including the fact that the crossed-edge set is fixed in each chamber. These general methods are antecedents, but the exact \(8/12\) dichotomy, missing-decagon phenomenon, sharp coordinate criterion, and explicit spherical probability for this regular Archimedean solid are not stated in the relevant inspected portions of those works. The classical vertex and face structure of the rhombicuboctahedron is not claimed as new. Earlier or unindexed literature could contain an equivalent special case; historical priority is not independently certified.

## Limitations
The result is for the regular small rhombicuboctahedron, not the great rhombicuboctahedron (truncated cuboctahedron), and for planes through its center only. Directions whose planes contain vertices are excluded from the side-count dichotomy; their possible degenerate polygons are not classified. The result does not determine areas, perimeters, off-center sections, or a continuous family of deformations. Its historical originality assessment is provisional, and independent validation has not been performed.

## References
1. K. Berlow, M.-C. Brandenburg, C. Meroni, I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, first public version 2021-10-12. https://arxiv.org/abs/2110.05996
2. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first public version 2023-04-27. https://arxiv.org/abs/2304.14239
