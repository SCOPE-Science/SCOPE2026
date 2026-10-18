# Exact overlap and twelve-facet rigidity for body-diagonal twists of a cube

## Finding

Let \(C=[-1,1]^3\) be a cube of side length two. Let \(R_\theta\) denote a right-handed rotation around \(u=(1,1,1)/\sqrt3\) by angle \(\theta\), and set \(P_\theta=C\cap R_\theta C\). For \(0\le\theta\le\pi/3\), define
\[
q(\theta)=\frac{3-2\sqrt3\sin\theta}{1+2\cos\theta}.
\]
Then \(q\) decreases strictly from one to zero as \(\theta\) increases, and
\[
\operatorname{Vol}_3(P_\theta)=6+2q(\theta)^2,
\qquad
\operatorname{Area}(\partial P_\theta)=18+6q(\theta)^2.
\]
For every \(0<\theta\le\pi/3\), \(P_\theta\) has exactly eight vertices and twelve congruent nondegenerate triangular faces, each of area \((3+q^2)/2\). It is tangential to the unit ball, with circumradius \(\sqrt3\). The full rotation-volume function is even and periodic with period \(2\pi/3\); its unique maximal congruence class has volume eight at \(\theta\equiv0\pmod{2\pi/3}\), and its unique minimal congruence class has volume six at \(\theta\equiv\pi/3\pmod{2\pi/3}\).

In particular, at the half-symmetry angle \(\theta=\pi/6\), one has \(q=2\sqrt3-3\) and \(\operatorname{Vol}_3(P_{\pi/6})=48-24\sqrt3\). The minimum overlap is exactly three quarters of the original cube volume.

## Assumptions and scope

The cubes are centered, congruent and have the same fixed body diagonal as rotation axis. Both are closed solid cubes, not their boundaries. Volume is three-dimensional Lebesgue measure, and area is two-dimensional Hausdorff measure on the polyhedral boundary. Angles are in radians. The formula on the displayed fundamental interval extends to every real angle using the cube's threefold rotation symmetry and the evenness of intersection volume; the asserted eight-vertex/facet classification applies when the reduced angle is positive. The untwisted endpoint is the usual cube, not a triangular-faceted polyhedron.

## Proof

**1. Rotation and algebraic parameter.** Rodrigues' formula gives the cyclic matrix
\[
R_\theta=\begin{pmatrix}a&b&d\\d&a&b\\b&d&a\end{pmatrix},
\quad
 a=\frac{1+2\cos\theta}{3},\quad
 b=\frac{1-\cos\theta}{3}-\frac{\sin\theta}{\sqrt3},\quad
 d=\frac{1-\cos\theta}{3}+\frac{\sin\theta}{\sqrt3}.
\]
Here \(a+b+d=1\), \(R_\theta^TR_\theta=I\), and \(\det R_\theta=1\). Set \(q=1+2b/a\), which is exactly the displayed trigonometric expression. In the interval \(0\le\theta\le\pi/3\) it lies in \([0,1]\). Solving these relations together with orthogonality yields
\[
 a=\frac{2(q+1)}{q^2+3},\qquad
 b=\frac{q^2-1}{q^2+3},\qquad
 d=\frac{2(1-q)}{q^2+3}.
\]
These identities also follow by direct substitution into Rodrigues' matrix.

**2. Eight actual feasible vertices.** Write \(w=(1,1,1)\) and
\[
 p_1=(1,-1,q),\qquad
 p_2=(q,1,-1),\qquad
 p_3=(-1,q,1).
\]
Let \(H=\operatorname{conv}\{\pm w,\pm p_1,\pm p_2,\pm p_3\}\). Every displayed point lies in \(C\). Also, because \(R_\theta\) fixes \(w\) and commutes with cyclic coordinate permutations,
\[
 R_\theta^T p_1=(q,-1,1),\quad
 R_\theta^T p_2=(1,q,-1),\quad
 R_\theta^T p_3=(-1,1,q).
\]
Every transformed coordinate has absolute value at most one. Hence \(H\subseteq P_\theta\).

**3. All twelve supporting facets, proving equality of polytopes.** For \(0\le q<1\), each of the six inequalities \(\pm x_i\le1\) supports a distinct triangular face of \(H\). For example, the plane \(x_1=1\) contains exactly \(w,p_1,-p_3\), and their planar area is
\[
 \frac12\left|\det\begin{pmatrix}-2&-1-q\\q-1&-2\end{pmatrix}\right|
 =\frac{3+q^2}{2}>0.
\]
The other five cube faces follow by cyclic permutation and central inversion. For each of the six rotated-cube inequalities \(\pm(R_\theta^Tx)_i\le1\), the same computation works in rotated coordinates. For instance, on \((R_\theta^Tx)_1=1\) the three points are \(w,p_2,-p_3\), whose rotated coordinates are \((1,1,1),(1,q,-1),(1,-1,-q)\), with the same area. In both families of triangles the three squared edge lengths are \(4+(1-q)^2\), \(4+(1+q)^2\), and \(2+2q^2\), so equality of the full side-length multisets proves actual congruence (not merely equality of areas). The twelve supporting planes are pairwise distinct whenever \(0<\theta\le\pi/3\), including the endpoint \(q=0\). Thus \(H\) has at least twelve distinct triangular facets and at most eight vertices.

Every three-dimensional polytope with \(v\) vertices has at most \(2v-4\) facets, by Euler's relation and triangulation of its boundary. Therefore \(H\) has at most twelve facets, all of which have just been exhibited. Since any convex polytope is the intersection of the supporting halfspaces of its facets, these twelve halfspaces determine \(H\) exactly. They are precisely the halfspaces defining \(P_\theta\); consequently \(H=P_\theta\). The eight points are distinct for \(q<1\); because the resulting polytope has twelve facets, none can be a redundant convex-hull point. Its edge count is eighteen by Euler's relation. All twelve facet areas equal \((3+q^2)/2\).

**4. Area and volume.** Every one of the twelve facet planes has outward unit normal and support distance one from the origin. Since the origin is in the interior, the decomposition into twelve pyramids with apex zero gives
\[
 \operatorname{Vol}_3(P_\theta)
 =\frac13\sum_{F}\operatorname{Area}(F)
 =\frac13\,12\frac{3+q^2}{2}=6+2q^2.
\]
The sum of the facet areas is \(18+6q^2\). The unit ball is inside each defining slab and tangent to every facet; moreover no ball of larger radius fits, as the pairs of opposite support planes are distance two apart. Thus the inradius is one. Both \(\pm w\) belong to the polytope and have norm \(\sqrt3\), while \(P_\theta\subseteq C\), so its circumradius is \(\sqrt3\). At \(q=1\) (the untwisted cube), volume and area are eight and twenty-four respectively, agreeing with the formulas by continuity; it has six square facets instead of twelve triangles.

**5. Strict monotonicity and every angle.** Eliminating the sine yields
\[
\cos\theta=\frac{-q^2+6q+3}{2(q^2+3)},\qquad
\frac{d\cos\theta}{dq}=\frac{3(1-q)(q+3)}{(q^2+3)^2}>0
\]
for \(0\le q<1\). Since cosine strictly decreases as \(\theta\) increases on \((0,\pi/3)\), \(q\), and hence \(6+2q^2\), strictly decrease there. The cube is invariant under rotation by \(2\pi/3\) about \(u\); therefore \(P_{\theta+2\pi/3}=P_\theta\). Replacing \(\theta\) by \(-\theta\) interchanges the two solids up to rotation, so \(\operatorname{Vol}(P_{-\theta})=\operatorname{Vol}(P_\theta)\). Every real angle reduces to \([0,\pi/3]\) under these symmetries, yielding all global equality classes and completing the proof.

## Verification

The included standalone program `check_cube_twist.py` checks the rational rotation identities and candidate vertex/facet conditions symbolically in the parameter \(q\), then verifies all twelve active supporting triples with exact rational arithmetic for 97 nontrivial rational parameters and both endpoints. An independently assembled halfspace-intersection/convex-hull calculation checks vertices, facet counts and volume at 231 angular samples. Run `python check_cube_twist.py` with Python 3 and SymPy; NumPy and SciPy enable the independent numerical checks. The general claim rests on the five proof steps above, not finite sampling.

## Relationship to prior work

General computational polyhedral-contact work motivates exact overlap observables but does not imply the one-parameter rotated-cube formula or its twelve-triangle rigidity. Nye, Kulchitsky and Johnson (2014) treat dilated polyhedral particles and collision/distance handling, explicitly working to avoid intersections of undilated polyhedral frames. A study of differentiable contact-volume estimation (2026) reports a different rotating-cube numerical benchmark about the coordinate \(z\)-axis, without the present body-diagonal analytic formula. Wolinski's account (2019) traces the volume **swept** by a cube rotated continuously around its long diagonal to a 2004 problem; a swept union across all angles is not the two-orientation intersection here. General translational cube covariograms differ because no relative rotation is permitted. These comparisons do not establish historical uniqueness.

## Limitations

Only two centered identically sized cubes with a common threefold body-diagonal axis are treated. Arbitrary three-dimensional relative rotations or translations, metric edge-type formulas, and multi-cube intersections are not classified. Historical priority remains subject to discovery of equivalent earlier formulas. No independent mathematical audit has been performed.

## References

1. B. Nye, A. V. Kulchitsky and J. B. Johnson, “Intersecting dilated convex polyhedra method for modeling complex particles in discrete element method,” *International Journal for Numerical and Analytical Methods in Geomechanics* (first published 15 May 2014), doi:10.1002/nag.2299. Full-text section on polyhedral distance and particle intersection methods inspected.
2. “Solving contact problems using Fiber Monte Carlo,” *Computational Mechanics* (2026), doi:10.1007/s00466-026-02822-6, especially the rotating-cube benchmark about the \(z\)-axis and contact-volume estimator.
3. F. Wolinski, “Le cube en rotation” (6 March 2019), discussing a distinct 2004 swept-volume problem for a cube rotated around its long diagonal: https://medium.com/@fran6w/le-cube-en-rotation-96b136175f5e.
4. G. Bianchi, “Matheron's conjecture for the covariogram problem” (2005), for the different setting of translation rather than relative rotation; bibliographic/abstract comparison only.
