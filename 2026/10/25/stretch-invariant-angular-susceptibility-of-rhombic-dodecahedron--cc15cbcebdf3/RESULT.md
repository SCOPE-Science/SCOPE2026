# Stretch-invariant angular susceptibility of rhombic-dodecahedron central sections

## Finding
For positive real numbers \(a,b,c\), consider the orthogonally stretched rhombic dodecahedron
\[
Q_{a,b,c}=\operatorname{conv}\bigl(\{(\pm2a,0,0),(0,\pm2b,0),(0,0,\pm2c)\}\cup\{(\pm a,\pm b,\pm c)\}\bigr),
\]
where the latter eight signs are independent. Let \(U\) be a uniform unit vector on \(S^2\), and let \(N(U)\) be the number of sides of the central section \(Q_{a,b,c}\cap U^\perp\). Almost surely \(N(U)\) is either \(6\) or \(8\). Precisely,
\[
N(U)=8\quad\Longleftrightarrow\quad
2\max\{a|U_1|,b|U_2|,c|U_3|\}>a|U_1|+b|U_2|+c|U_3|.
\]
For an index \(i\in\{1,2,3\}\) write \((s_1,s_2,s_3)=(a,b,c)\), and let \(j,k\) be the other two indices. Then the exact octagon probability is
\[
\boxed{\displaystyle
p_8(a,b,c)=\frac4\pi\sum_{i=1}^3
\arctan\!\left(\frac{s_i^2}{
(\sqrt{s_i^2+s_j^2}+s_j)(\sqrt{s_i^2+s_k^2}+s_k)}\right).}
\]
In particular, for the unstretched regular member,
\[
p_8(1,1,1)=\frac{12}{\pi}\arccos\frac1{\sqrt3}-3
\approx0.649040687816356.
\]
The probability is not deformation-invariant: \(p_8(a,b,c)\to1\) as \(a\to\infty\) with \(b,c\) fixed.

Nevertheless, a sharper **angular-susceptibility invariant** survives every such orthogonal stretch. Conditional on \(U\), choose \(W\) uniformly on the unit circle in the tangent plane \(U^\perp\), independently of all other randomness, and put \(U_t=\cos(t)U+\sin(t)W\). As \(t\downarrow0\),
\[
\boxed{\Pr\{N(U_t)\ne N(U)\}=\frac4\pi t+O_{a,b,c}(t^2),}
\]
and the directed transitions satisfy
\[
\boxed{\Pr\{N(U)=6,N(U_t)=8\}
=\Pr\{N(U)=8,N(U_t)=6\}
=\frac2\pi t+O_{a,b,c}(t^2).}
\]
Thus the leading rate of changes of section type is **exactly independent of all three positive stretching factors**, although the proportions of hexagonal and octagonal sections generally vary.

## Assumptions and scope
All three parameters are strictly positive and fixed as \(t\to0\). A plane and its antipodal normal describe the same section; sampling uniformly on the full sphere gives the same probabilities as sampling uniformly on the unoriented projective plane. A section passing through a polyhedral vertex or containing a polyhedral edge is exceptional and has zero spherical measure. No statement about such exceptional sections is needed. Rotation is along a geodesic by exactly \(t\) radians with a uniformly random tangent direction, not an arbitrary ambient random rotation law.

## Proof
**1. Combinatorial section-type criterion.** The fourteen listed points are the vertices of the stretched rhombic dodecahedron. Its twenty-four edges connect each vertex of the form \((\pm2a,0,0)\), \((0,\pm2b,0)\), or \((0,0,\pm2c)\) to the four sign-corner vertices whose sign matches that of the nonzero coordinate. For a plane through the interior, in generic position, the number of section vertices equals the number of edges whose endpoints lie on opposite sides of the plane. Orthogonal changes of coordinate signs allow us to take \(aU_1=x>0\), \(bU_2=y>0\), \(cU_3=z>0\).

The antipodal corner pair \((a,b,c)\), \((-a,-b,-c)\) contributes no crossing edges. Each of the other three antipodal corner pairs, represented by sign pattern \((+,+,-)\), \((+,-,+)\), or \((-,+,+)\), contributes two crossing edges unless the magnitude of its singly signed coordinate exceeds the sum of the other two, in which case it contributes four. For example, the pair with representative \((a,b,-c)\) contributes four exactly when \(z>x+y\). At most one of \(x>y+z\), \(y>x+z\), \(z>x+y\) can hold. Therefore the total is \(6\) or \(8\), with the asserted strict dominance criterion. Replacing the positive variables by the absolute scaled normal coordinates completes the criterion.

**2. Exact probabilities.** On the unit sphere the octagon region consists of six disjoint open cones, one around each signed coordinate axis. Around \(+e_1\), the cone is
\[
C_1^+=\{u\in S^2:au_1>b|u_2|+c|u_3|\}.
\]
It is a spherical quadrilateral with corner rays \((b,\pm a,0)\) and \((c,0,\pm a)\). Connecting these corners to \(+e_1\) divides it into four congruent spherical triangles. For the positive-sign triangle take unit vertices
\[
p=e_1,\quad q=(b,a,0)/\sqrt{a^2+b^2},\quad r=(c,0,a)/\sqrt{a^2+c^2}.
\]
The standard spherical excess identity for three unit vectors, with positive orientation,
\[
\tan\frac{\Omega}{2}=\frac{|\det(p,q,r)|}{1+p\cdot q+q\cdot r+r\cdot p},
\]
gives
\[
\Omega=2\arctan\!\left(
\frac{a^2}{(\sqrt{a^2+b^2}+b)(\sqrt{a^2+c^2}+c)}\right).
\]
Each signed axis cone has four such triangles, and each coordinate axis has two antipodal cones. Dividing the resulting total spherical area by \(4\pi\) proves the stated formula for \(p_8\). When \(a=b=c\), the triangle has side lengths \(\pi/4,\pi/4,\pi/3\), angles \(\pi/2,\gamma,\gamma\) with \(\gamma=\arccos(1/\sqrt3)\), giving the equivalent expression \(12\gamma/\pi-3\). The dominance criterion also proves the claimed limit as one stretching factor tends to infinity: for almost every \(U\), the stretched coordinate eventually dominates.

**3. Exact boundary length despite stretching.** Each signed axis cone has four great-circle edges. For a cone around the first axis, each such edge joins the normalized corner rays \((b,a,0)\) and \((c,0,a)\), or their signed counterparts, and therefore has geodesic length
\[
\delta_a=\arccos\!\left(\frac{bc}{\sqrt{(a^2+b^2)(a^2+c^2)}}\right).
\]
Define \(\delta_b,\delta_c\) by cycling the parameters and put \(H=\sqrt{a^2+b^2+c^2}\). All three angles belong to \((0,\pi/2)\), and elementary trigonometry gives
\[
\cot\delta_a=\frac{bc}{aH},\qquad
\cot\delta_b=\frac{ac}{bH},\qquad
\cot\delta_c=\frac{ab}{cH}.
\]
Consequently
\[
\cot\delta_a\cot\delta_b+\cot\delta_b\cot\delta_c+
\cot\delta_c\cot\delta_a=\frac{a^2+b^2+c^2}{H^2}=1.
\]
More explicitly, the cotangent addition identity gives
\[
\cot(\delta_a+\delta_b)=-\cot\delta_c.
\]
Since \(\delta_a+\delta_b\in(0,\pi)\) and \(\delta_c\in(0,\pi/2)\), this forces \(\delta_a+\delta_b+\delta_c=\pi\). Different cone boundaries intersect only at their finitely many corner points and do not share arcs. Each coordinate contributes two cones times four arcs, so the total spherical boundary length between the two section types is exactly
\[
\boxed{L=8(\delta_a+\delta_b+\delta_c)=8\pi.}
\]
It is this perimeter identity, rather than equality of type probabilities, that survives stretching.

**4. Geodesic crossing probability.** For any fixed partition of \(S^2\) whose separating boundary is a finite union of smooth geodesic arcs meeting at finitely many vertices, normal tubular coordinates show that a geodesic step of length \(t\), with uniformly random tangent direction, crosses the boundary with probability
\[
\frac{tL}{4\pi}\,\mathbb E|\cos\Phi|+O(t^2)
=\frac{tL}{2\pi^2}+O(t^2),
\]
where \(\Phi\) is uniform on \([0,2\pi]\) and \(\mathbb E|\cos\Phi|=2/\pi\). To justify the remainder, remove arc portions of length \(O(t)\) near each finite junction (the associated spherical bands have area \(O(t^2)\)); on remaining great-circle arcs, the exponential-map Jacobian and crossing displacement differ from their Euclidean tangent-plane forms by \(O(t^2)\). Here there are finitely many arcs and vertices for each fixed positive \((a,b,c)\), so the bound applies. Substituting \(L=8\pi\) gives the coefficient \(4/\pi\). The transition kernel \(U\mapsto U_t\) is reversible under spherical area measure, so the two directed type-change probabilities are exactly equal for every \(t\), and each has half the leading coefficient. This proves all claims.

## Verification
Run `python checks/check_sections.py` from the enclosing directory (NumPy and SciPy required). The program reconstructs all twenty-four edges independently of the dominance formula, evaluates the cone probabilities by a separate one-dimensional spherical polar integral, checks the trigonometric boundary-length identity, and samples Haar-uniform plane orientations and random geodesic perturbations. Its final marker is `ALL_RHOMBIC_DODECAHEDRON_SECTION_TESTS_OK`. These finite tests corroborate, but are not the proof of, the all-parameter and small-angle statements.

## Relationship to prior work
Hausel, Makai and Szűcs (1999) used the rhombic dodecahedron as a universal covering body in three-dimensional convex geometry, rather than studying the distribution of its random central-section types. Matteo (2014) classifies combinatorially two-orbit convex polytopes and discusses the rhombic-dodecahedral honeycomb, but its face-lattice sections are not random central Euclidean plane sections. Previously reported random-section calculations for rectangular boxes and the regular icosahedron concern different normal-chamber arrangements. Known Crofton-style boundary-crossing principles provide the general linear response once the boundary length is known; they do not themselves establish the stretch-independent identity \(L=8\pi\) for this family. The octagon probability and its simultaneous deformation-sensitive frequency versus deformation-invariant first-order transition rate are the claimed contribution.

## Limitations
The results apply to three positive **orthogonal** axis stretches of the regular rhombic dodecahedron, not arbitrary sheared affine images or all zonohedra. The \(O_{a,b,c}(t^2)\) constant may depend strongly on axis ratios; no uniform statement as a parameter degenerates is proved. Exact finite-angle transition probabilities are not determined. Priority with respect to inaccessible or unindexed historical geometric literature remains a residual risk; an absence of a retrieved matching result is not a proof of absolute novelty. Independent mathematical validation has not been performed.

## References
1. T. Hausel, E. Makai Jr., A. Szűcs, *Inscribing cubes and covering by rhombic dodecahedra via equivariant topology*, first publicly posted 1999-06-10, arXiv:math/9906066, https://arxiv.org/abs/math/9906066.
2. N. Matteo, *Combinatorially two-orbit convex polytopes*, first publicly posted 2014-11-06, arXiv:1411.1782, https://arxiv.org/abs/1411.1782.
3. *Exact Haar polygon-type law for central icosahedron sections*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
4. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.
