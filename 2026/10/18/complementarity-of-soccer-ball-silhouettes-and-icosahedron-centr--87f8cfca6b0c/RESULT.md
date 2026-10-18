# Complementarity of soccer-ball silhouettes and icosahedron central sections

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and let the regular icosahedron be
\[
I=\operatorname{conv}\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Truncate every edge at its one-third point to form the regular truncated icosahedron \(T\), a polyhedron with \(60\) vertices, \(90\) edges, \(12\) regular pentagons and \(20\) regular hexagons. For a generic normal \(u\in S^2\), let \(N_T(u)\) count the vertices of the orthogonal projection of \(T\) onto \(u^\perp\), and let \(S_I(u)\) count the vertices of the central plane section \(I\cap u^\perp\).

**The directional complementarity theorem** is
\[
\boxed{N_T(u)+S_I(u)=30.}
\]
It holds for every \(u\) outside the finitely many great circles orthogonal to vertices of \(I\) or face normals of \(T\). In particular \(N_T(u)\) is exactly \(18\) or \(20\) for almost every direction. In the six-icosahedral-axis spherical chamber decomposition, the \(20\) triangular chambers yield \((N_T,S_I)=(18,12)\), while the \(12\) pentagonal chambers yield \((20,10)\).

For uniform \(U\in S^2\), writing \(\theta=\arccos(1/\sqrt5)\), the complete projected-vertex distribution is
\[
\begin{aligned}
\mathbb P(N_T(U)=18)&=\frac{15\theta}{\pi}-5\approx0.286245735243501,\\
\mathbb P(N_T(U)=20)&=6-\frac{15\theta}{\pi}\approx0.713754264756499,\\
\mathbb E N_T(U)&=30-\frac{30\theta}{\pi}\approx19.427508529513.
\end{aligned}
\]
The central-icosahedron section distribution and the triangular/pentagonal spherical-area fractions used here were determined previously; novelty is proposed for the pointwise cross-body complementarity and the full generic truncated-icosahedron silhouette classification, not for those previously known ingredients.

## Assumptions and scope

A *viewing normal* is a unit vector \(u\). The orthogonal shadow is the convex polygon obtained by projecting all \(60\) vertices of \(T\) onto \(u^\perp\). A central section is the intrinsic polygon in \(u^\perp\). Exclude directions with \(\langle u,w\rangle=0\) for a face normal \(w\) of \(T\) or an original vertex of \(I\); these are a finite union of great circles and have Haar measure zero. Opposite viewing normals produce identical counts. All assertions are for equal-distance one-third truncations, orthographic projection, and planes through the center of \(I\).

## Proof

**1. Exact models and incidence.** Rescale all original icosahedron vertices by \(2\), keeping notation \(v_i\). Then their coordinates lie in \(\mathbb Z[\sqrt5]\). Two vertices are adjacent precisely when their scalar product is \(2+2\sqrt5\). There are exactly \(30\) edges and \(20\) equilateral triangular faces \(f=\{i,j,k\}\). The \(60\) truncated vertices are proportional to \(2v_i+v_j\) for oriented old edges \((i,j)\). Every old vertex \(v_i\) determines one pentagon whose outward normal is \(v_i\); every original triangle \(f\) determines one hexagon whose outward normal is \(w_f=v_i+v_j+v_k\). The truncated-polyhedron edges comprise \(60\) incidences \((i,f)\) between a vertex and an incident triangular face (pentagon--hexagon), and \(30\) incidences between the two triangular faces on an old edge (hexagon--hexagon), giving \(90\) in total. These assertions follow directly from third-point truncation and are also reconstructed exactly by `verify_soccer_icosahedron.py`.

**2. Shadow edges as sign changes.** At a generic viewing normal \(u\), a polyhedron edge belongs to the silhouette exactly when its two incident facets have outward normals with opposite signs of dot product with \(u\). Indeed, such an edge separates a locally front-facing from a locally back-facing facet; all other edges project into the interior of the shadow. The projected silhouette is a strictly convex polygon at generic directions, and every such silhouette edge corresponds to exactly one polygon vertex. Thus the number of silhouette vertices equals the number of sign-changing adjacent-facet pairs. Likewise, each vertex of the central icosahedron section comes from exactly one old edge with oppositely signed endpoint scalar products.

**3. Why hexagon-normal walls cannot change the count.** A hexagonal facet is a regular, centrally symmetric hexagon. Its six edge directions occur in three parallel pairs. For any viewing normal perpendicular to this facet normal but not simultaneously perpendicular to another facet normal, the tangential components of the six neighboring outward facet normals align with the six oriented outward normals of the hexagon edges, in three antipodal pairs. Consequently, exactly three neighbors have positive dot product with the viewing normal and exactly three have negative dot product. Crossing the great circle orthogonal to that hexagon's normal flips only the central hexagon's face sign, swapping \(3\) sign-changing boundary edges for the other \(3\); the total shadow-vertex number remains unchanged. Therefore \(N_T\) is constant inside each chamber formed by the *six* great circles orthogonal to the six antipodal axes of the original icosahedron, even though the signs of individual hexagon normals can change inside a chamber. The central section count \(S_I\) is also constant in each such chamber by the old-edge crossing criterion.

**4. Complete exact chamber test, rather than sampled directions.** Choose one vertex \(a_j\) from each of the six antipodal axes. Direct exact determinants in \(\mathbb Z[\sqrt5]\) establish that no three axes are coplanar, so their six great circles have exactly \(6^2-6+2=32\) chambers. An explicit test of the six strict signs \(\operatorname{sgn}\langle u,a_j\rangle\), at each of the twelve original vertex normals and twenty old-face normals, returns \(32\) distinct sign masks. Therefore these \(32\) normals represent *all* chambers. Applying the preceding sign-change counts to these representatives gives the exhaustive exact table:

| Representative normal | Number of chambers | Shadow vertices \(N_T\) | Section vertices \(S_I\) |
| --- | ---: | ---: | ---: |
| Original icosahedron vertex (pentagon normal) | 12 | 20 | 10 |
| Original triangular face sum (hexagon normal) | 20 | 18 | 12 |

No numerical tolerance enters this classification. The standalone certificate performs the scalar products, determinants, unique-mask assertions and count evaluations using pairs of integers representing elements of \(\mathbb Z[\sqrt5]\), with comparisons performed by exact integer squares. Since both counts are constant on every chamber, this proves \(N_T+S_I=30\) for the continuum of allowed viewing normals.

**5. Angular probabilities.** Every pair of distinct original antipodal axes has absolute normalized dot product \(1/\sqrt5\). The \(20\) triangular chambers have three interior angles \(\theta=\arccos(1/\sqrt5)\), hence unit-sphere area \(3\theta-\pi\). The \(12\) complementary pentagonal chambers have area \(2\pi-5\theta\), as follows from their angles and Girard's theorem. Dividing the respective total areas by \(4\pi\) gives \(20(3\theta-\pi)/(4\pi)=15\theta/\pi-5\) and its complement. Equivalently, the already-known central icosahedron section law and the newly proved count complementarity imply the same distribution and mean.

## Verification

Run `python3 verify_soccer_icosahedron.py` with Python's standard library. The checker reconstructs the complete icosahedral graph and its twenty faces; verifies the ninety truncated-polyhedron edges, all six axes' general position, thirty-two distinct and exhaustive chamber masks, and all sixty-four coordinate-field sign comparisons needed by the exact incidence formulas. It confirms \(12\) instances of \((20,10)\) and \(20\) instances of \((18,12)\), and checks central symmetry of all hexagonal facets. Separately, it projects the actual sixty truncated vertices for \(4000\) pseudorandom directions, recomputes planar convex hulls, and checks the complementarity numerically. The latter finite check is corroborative only; the exact chamber reduction establishes the continuum theorem.

## Relationship to prior work

Koca, Al Ajmi and Al-Shidhani (2010), arXiv:1006.2973, Section V.C, explicitly construct and count the \(60\) vertices, \(90\) edges, and \(32\) faces of the regular truncated icosahedron. Their treatment is of Coxeter/quaternionic polyhedral construction and molecular bond geometry, not of all-direction planar shadows or pointwise cross-body section identities. The QFBox truncated-icosahedron page (last updated 10 January 2023) lists an octadecagon in a face-centered view and an icosagon in a pentagon-centered view, as well as exceptional silhouettes; it does not assert that those are the *only generic* counts or supply a spherical probability law. A previously published record entitled *Exact Haar polygon-type law for central icosahedron sections* proves precisely the \(10\)-versus-\(12\) central-section classification and the same angular fraction \(15\theta/\pi-5\). That is a **used theorem**, not a new result here. Earlier descriptions of the six great circles and their triangle/pentagon area fractions (MathPages; Frederick) are also used, not claimed new. None of the inspected statements supplies a general implication from the existing icosahedron section law to the truncated-icosahedron silhouette law; the additional polyhedral sign-balancing and chamber transfer in steps 1--4 are essential to this new statement. Historical priority is provisional, particularly for non-indexed work on fullerene silhouette combinatorics.

## Limitations

The result is almost sure under Haar measure and pointwise outside finitely many exceptional great circles. Other special views may have \(10\) or \(16\) projected vertices, as already illustrated in older literature; the theorem deliberately does not classify the exceptional-direction strata. Only the regular one-third truncated icosahedron and central sections of its original regular icosahedron are studied. The numerical values of the angular probabilities are not themselves newly calculated; they are transported through the proved cross-body relation. The theorem does not cover perspective views, randomly translated cuts, nonregular fullerene deformations, or projected area distributions. No independent scientific audit has been performed.

## References

1. M. Koca, M. Al Ajmi and S. Al-Shidhani, *Quasi Regular Polyhedra and Their Duals with Coxeter Symmetries Represented by Quaternions II*, arXiv:1006.2973 (first public 15 June 2010), Section V.C, https://arxiv.org/pdf/1006.2973.
2. *The Truncated Icosahedron*, QFBox, https://www.qfbox.info/4d/buckyball (last updated 10 January 2023), section "Projections".
3. *Exact Haar polygon-type law for central icosahedron sections*, published mathematical record (11 October 2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f/RESULT.md.
4. *N Points On Sphere all in One Hemisphere*, MathPages, https://www.mathpages.com/home/kmath327/kmath327.htm, spherical icosahedral six-great-circle section.
5. G. Frederick, *Great Circle Bow-Ties of the Icosahedron*, 5 August 2023, https://geometryofthinking.com/2023/08/05/great-circle-bow-ties-of-the-icosahedron/.
