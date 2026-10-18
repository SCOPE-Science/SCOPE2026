# Exact four-type random-shadow law for square antiprisms of every height

## Finding
For each height \(h>0\), let \(P_h\subset\mathbb R^3\) be the convex hull of two circumradius-one squares: the upper square has vertices
\[
(\cos(j\pi/2),\sin(j\pi/2),h),\qquad j=0,1,2,3,
\]
and the lower square has vertices
\[
(\cos(\pi/4+j\pi/2),\sin(\pi/4+j\pi/2),-h),\qquad j=0,1,2,3.
\]
For a Haar-uniform unit direction \(U\in S^2\), let \(N_h\) count the vertices of the orthogonal projection of \(P_h\) onto \(U^\perp\). Put
\[
\gamma=\frac{1-1/\sqrt2}{2h},\qquad
J_\gamma(t)=\arcsin\!\left(\frac{\sin t}{\sqrt{1+\gamma^2}}\right)
\quad(0\le t\le\pi/2),
\]
and abbreviate
\[
a=J_\gamma(\pi/8),\quad b=J_\gamma(\pi/4),\quad
c=J_\gamma(3\pi/8),\quad d=J_\gamma(\pi/2).
\]
Then the **complete** shadow-vertex law is
\[
\boxed{\begin{aligned}
\Pr(N_h=5)&=\frac8\pi(2c-b-d),\\
\Pr(N_h=7)&=\frac8\pi(2a-b),\\
\Pr(N_h=8)&=1-\frac8\pi a,\\
\Pr(N_h=6)&=1-\Pr(N_h=5)-\Pr(N_h=7)-\Pr(N_h=8).
\end{aligned}}
\]
All four probabilities are strictly positive for **every** \(h>0\); no other vertex count occurs except on a null set of nongeneric directions. Equivalently, by planar polarity, this is the full Haar law of central-section side counts of the polar square trapezohedra, in the corresponding Euclidean realization.

For the regular-faced square antiprism, \(h=2^{-3/4}\), the probabilities (in the order five, six, seven, eight vertices) are
\[
(0.356758138764\ldots,\ 0.600915394901\ldots,\
0.011795388796\ldots,\ 0.030531077539\ldots).
\]
The angular transition between the two integration patterns is always \(\pi/8\), independent of height.

## Assumptions and scope
The two squares have common vertical axis, equal circumradius one, relative twist exactly \(\pi/4\), and positive half-separation \(h\). The eight vertices form a convex antiprism with two square faces and eight triangular faces. A generic direction means no facet normal is perpendicular to the viewing direction, and no two projected polygon vertices collide or become collinear. These exceptional directions form a finite union of great circles, hence have spherical measure zero. Direction and its negative yield the same projected polygon. The law concerns the actual planar convex hull, not the transparent image of a nonconvex mesh.

## Proof
**1. Supporting facets and edge classes.** Write \(g=\gamma\) and \(\alpha=\sqrt2g=(\sqrt2-1)/(2h)\). Besides the cap normals \(\pm e_3\), the eight triangular facet normals, without unit normalization, are
\[
(\pm1,\pm1,\alpha),\quad
(\pm1,0,-g),\quad(0,\pm1,-g).
\]
The four upper-edge triangles lie in planes with support value \(1+\alpha h\), and the four lower-edge triangles have support value \(1-gh\). Direct substitution into the eight listed vertices shows in each case exactly three equality vertices and all remaining vertices strictly on the inner side. Together with the upper and lower quadrilateral caps these eight side triangles form the complete convex boundary; their face adjacency has four cap-to-upper edges, four cap-to-lower edges, and eight alternating lateral edges, for sixteen edges total.

**2. Reduction to one viewing wedge.** Negating the normal leaves the projection unchanged. The planar dihedral symmetries of the two rings restrict the calculation to
\[
z>0,\qquad x\ge y\ge0,\qquad U=(x,y,z)/\sqrt{x^2+y^2+z^2}.
\]
Define the four Boolean indicators
\[
A=\mathbf1\{x+y<\sqrt2gz\},\quad
B=\mathbf1\{x-y<\sqrt2gz\},\quad
C=\mathbf1\{x<gz\},\quad
D=\mathbf1\{y<gz\}.
\]
The upper side-normal signs, in cyclic order, contain two fixed positives and the two values \(A,B\). The lower side-normal signs contain two fixed negatives and two positives exactly when \(C,D\) respectively vanish. The upper-cap edge crossings count \(2-A-B\), and the lower-cap crossings count \(2-C-D\). From the eight triangle-to-triangle incidences the number of side-edge crossings is
\[
2+2A+B+2C+D-|B-D|.
\]
An edge of a convex polyhedron is on the apparent contour for a generic orthogonal viewing direction if and only if its two adjacent outward facet normals have opposite signs against that direction. Each such contour edge gives exactly one edge of the projected convex polygon. Summing the three classes therefore yields the exact directional identity
\[
\boxed{N_h=6+A+C-|B-D|.}
\]

**3. The four moving thresholds.** Parameterize the viewing wedge by polar angle \(0<\rho<\pi/2\) and azimuth \(0<\theta<\pi/4\):
\[
(x,y,z)=(\sin\rho\cos\theta,\sin\rho\sin\theta,\cos\rho).
\]
Writing \(r=\tan\rho\), the truth of \(A,B,C,D\) changes precisely when \(r\) crosses, respectively,
\[
r_A=\frac g{\cos(\theta-\pi/4)},\quad
r_B=\frac g{\cos(\theta+\pi/4)},\quad
r_C=\frac g{\cos\theta},\quad
r_D=\frac g{\sin\theta}.
\]
For \(0<\theta<\pi/8\), the strict order is \(r_C<r_A<r_B<r_D\); for \(\pi/8<\theta<\pi/4\), it is \(r_A<r_C<r_D<r_B\). In either case, as \(r\) increases through these thresholds, the exact identity above gives the five successive counts
\[
8,\ 7,\ 6,\ 5,\ 6.
\]
Every interval has positive length for azimuths in either open subwedge; every one of the four possible vertex counts therefore has strictly positive probability for every \(g>0\).

**4. Exact spherical integration.** Normalized spherical area in the wedge is \((4/\pi)\sin\rho\,d\rho\,d\theta\). The radial probability below \(r=R\) at fixed azimuth is
\[
F(R)=1-\frac1{\sqrt{1+R^2}}.
\]
The eight-, seven-, and five-vertex probabilities are thus, respectively,
\[
\frac4\pi\left(\int_0^{\pi/8}F(r_C)\,d\theta+
\int_{\pi/8}^{\pi/4}F(r_A)\,d\theta\right),
\]
\[
\frac4\pi\left(\int_0^{\pi/8}[F(r_A)-F(r_C)]\,d\theta+
\int_{\pi/8}^{\pi/4}[F(r_C)-F(r_A)]\,d\theta\right),
\]
and
\[
\frac4\pi\left(\int_0^{\pi/8}[F(r_D)-F(r_B)]\,d\theta+
\int_{\pi/8}^{\pi/4}[F(r_B)-F(r_D)]\,d\theta\right).
\]
The elementary antiderivative
\[
\int\frac{\cos t}{\sqrt{g^2+\cos^2t}}\,dt
=J_g(t)
\]
evaluates these integrals as \(1-8a/\pi\), \(8(2a-b)/\pi\), and \(8(2c-b-d)/\pi\), respectively. The remaining probability is their complement. This proves the displayed complete law and all quantifiers.

**5. Independent moment identity.** The upper-cap and lower-cap edge classes each have four edges with exterior normal angle \(\arccos(g/\sqrt{1+g^2})\). The eight lateral edges have exterior normal angle \(\arccos((1/\sqrt2-g^2)/(1+g^2))\). The classical edge-by-edge spherical formula for the expected silhouette size therefore supplies the separate exact identity
\[
\mathbb E N_h=\frac8\pi\left[
\arccos\frac g{\sqrt{1+g^2}}+
\arccos\frac{1/\sqrt2-g^2}{1+g^2}\right],
\]
which agrees algebraically with the four-point law. This is an independent consistency identity, not an additional novelty claim.

## Verification
Running `python3 verify.py` (Python standard library only) verifies the asserted supporting facet planes, all sixteen facet-adjacency edges, and the directional counting formula against **72,000 independently reconstructed planar convex hulls**, distributed over four positive heights. It also numerically integrates the spherical threshold regions independently at every tested height and checks the dihedral-angle expectation identity. The program prints `SQUARE_ANTIPRISM_SHADOW_OK` only after all assertions pass. Finite checks support the exact derivation but do not replace its all-height proof.

## Relationship to prior work
McGuire's study gives the classical mean silhouette-edge count through exterior dihedral angles; its one-dimensional expectation does not determine this four-point law. Glisse and Lazard analyze expected silhouette complexity for broad families of polyhedral surface approximations, not exact height-dependent probabilities for a fixed antiprism. Kettner and Welzl investigate contour edges and average complexity rather than the displayed four probabilities. The published X-ray-number result for uniform antiprisms concerns an entirely different invariant, the minimum number of penetrating line directions, and supplies no shadow count distribution. The polar reformulation was included in the originality searches: it is the central-section side-count law of the corresponding square trapezohedron, not a separate theorem. Searches for this formulation and for antiprism shadow aliases found no same-claim or stronger covering result in the inspected sources. Historical priority is not independently certified.

## Limitations
The result is for equal-radius, half-step-twisted squares and orthographic directions uniform on the sphere. It does not determine the silhouette law for unequal rings, other twists, perspective cameras, or nonuniform directional measures. Nongeneric images on finitely many great circles are not classified because they have probability zero. The full joint law with projected area or perimeter is not determined. No claim of a complete historical priority search or independent mathematical validation is made.

## References
1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087v1, first publicly submitted 14 February 2007, https://arxiv.org/abs/cs/0702087.
2. M. McGuire, *Observations on Silhouette Sizes*, Journal of Graphics Tools 9 (2004), 1–12, DOI: 10.1080/10867651.2004.10487594.
3. L. Kettner and E. Welzl, *Contour Edge Analysis for Polyhedron Projections*, ETH Zürich technical report 258 (December 1996), DOI: 10.3929/ethz-a-006651848.
4. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a Random Polytope*, Journal of Computational Geometry 7 (2016), 86–99, DOI: 10.20382/jocg.v7i1a5.
5. *Every uniform antiprism has X-ray number three*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-uniform-antiprism-has-x-ray-number-three--8163a250996c.
