# Pointwise complementary sections of boxes and rhombic dodecahedra, with a sharp Haar law

## Finding
Let \(C=[-1,1]^3\), and let \(R\) be the rhombic dodecahedron
\[
R=\operatorname{conv}\bigl(\{\pm2e_1,\pm2e_2,\pm2e_3\}\cup\{(\pm1,\pm1,\pm1)\}\bigr).
\]
For any invertible linear map \(T:\mathbb R^3\to\mathbb R^3\), and for almost every unit vector \(u\), let \(N_C(u)\) and \(N_R(u)\) count the vertices of the central sections \(TC\cap u^\perp\) and \(TR\cap u^\perp\). There is a **pointwise combinatorial complementarity**:
\[
\boxed{N_C(u)+N_R(u)=12.}
\]
In particular, each generic rhombic-dodecahedron section is a hexagon or octagon, and the hexagon event is exactly the box-hexagon event **for the same normal**, not just an equality of averaged probabilities.

For every diagonal stretch \(T=\operatorname{diag}(a,b,c)\) with \(a,b,c>0\), put \(r=\sqrt{a^2+b^2+c^2}\). For Haar-uniform \(U\in S^2\), the entire section-polygon law is
\[
\boxed{\begin{aligned}
\Pr\{N_R(U)=6\}&=\frac4\pi\left(\arcsin\frac ar+\arcsin\frac br+\arcsin\frac cr\right)-2,\\
\Pr\{N_R(U)=8\}&=3-\frac4\pi\left(\arcsin\frac ar+\arcsin\frac br+\arcsin\frac cr\right).
\end{aligned}}
\]
Among all positive triples, the hexagon probability is **uniquely maximized, up to common scaling, at \(a=b=c\)**, where it equals
\[
\boxed{p_*=\frac{12}{\pi}\arcsin(1/\sqrt3)-2=0.350959312183644\ldots.}
\]
Its infimum is zero, not attained for positive side lengths, and approached at degenerating aspect ratios. Moreover, if \(a=e^{t_1},b=e^{t_2},c=e^{t_3}\) and \(\overline t=(t_1+t_2+t_3)/3\), then near equal sides
\[
\boxed{p_*-\Pr(N_R(U)=6)=\frac{1}{\pi\sqrt2}\sum_{i=1}^3(t_i-\overline t)^2+O(\|t-\overline t\mathbf1\|^3).}
\]
Thus the cubic optimum has a sharp quadratic angular/combinatorial stability law.

## Assumptions and scope
All planes pass through the origin, which is the center of the two convex bodies. Both are subjected to the *same* invertible linear transformation in the pointwise claim. The measure-zero excluded normals contain the finite set of great circles perpendicular to a polytope vertex; at these orientations a section plane may pass through vertices and the generic edge-crossing count does not apply. The probability, optimization, and second-order expansion require a positive diagonal stretch, rather than arbitrary shear. Section counts are unchanged by uniform rescaling.

## Proof
**1. A local edge-pair identity.** Label the eight cube vertices by signs \(\varepsilon\in\{-1,+1\}^3\). The cube has exactly twelve edges, one for each unordered pair \((\varepsilon^-,\varepsilon^+)\) differing at coordinate \(i\); call the endpoint with \(i\)-th coordinate negative the low endpoint. The polytope \(R\) has precisely the 24 edges joining each vertex \(\varepsilon\) to \(2\varepsilon_i e_i\), for \(i=1,2,3\); indeed, its twelve rhombic facets are the inequalities \(\pm x_i\pm x_j\le2\), for \(1\le i<j\le3\), each supporting precisely four displayed vertices; their 24 boundary edges are exactly these axial-to-corner pairs. Each cube edge has exactly two partner \(R\)-edges, one from each cube-edge endpoint to its corresponding axial vertex.

Fix a generic normal \(v\), and first take \(v_i>0\). Then the two endpoint scalar products satisfy \(\ell=v\cdot\varepsilon^-<h=v\cdot\varepsilon^+\). Exactly one of the following holds: both are negative, their signs differ, or both are positive. In the middle case the cube edge crosses \(v^\perp\), while neither partner edge of \(R\) crosses it. In either of the other two cases, exactly one partner edge of \(R\) crosses while the cube edge does not. Thus the total number of crossings among this cube edge and its two partners is **exactly one**. If \(v_i<0\), interchange the low and high designations and the same reasoning applies.

Summing this local identity over twelve cube edges counts every \(R\)-edge once, and proves \(N_C(v)+N_R(v)=12\): for generic normals, a transverse section of a convex polytope has exactly one section vertex on each crossing edge. For an invertible \(T\), replace \(v\) by \(T^\top u\); the same sign argument applies to \(TC\) and \(TR\). Every generic central section of a cube or parallelotope is a centrally symmetric polygon with either four or six vertices (at least four by central symmetry and at most six from the six faces). Consequently \(N_R\in\{6,8\}\) and the claimed same-normal event equivalence follows.

**2. Exact Haar probabilities.** For \(T=\operatorname{diag}(a,b,c)\) put \(r=\sqrt{a^2+b^2+c^2}\). Each of the eight \(R\)-edges incident to an axial vertex in direction \(i\) joins a vector parallel to \(e_i\) to a corner vector of length \(r\), with matching sign in coordinate \(i\). The acute angle between the two endpoint rays is \(\arccos(a_i/r)\). A uniformly oriented through-origin plane separates two non-antipodal rays with probability their angle divided by \(\pi\); this follows by restricting the normal to the great circle in their two-dimensional span. By linearity of expectation over the 24 edges,
\[
\mathbb E N_R(U)=\frac8\pi\sum_{i=1}^3\arccos(a_i/r).
\]
Writing \(p=\Pr(N_R=6)\), the two-valued support gives \(6p+8(1-p)=8-2p=\mathbb E N_R\). Substituting \(\arccos x=\pi/2-\arcsin x\) yields exactly the displayed probabilities.

**3. Global optimizer and local rigidity.** Scale to \(x_i=a_i/r>0\), so \(\sum x_i^2=1\). The function \(F=\sum\arcsin x_i\) extends continuously to the closed first-octant sphere. On its boundary, whenever one coordinate vanishes, the other two satisfy \(\arcsin x+\arcsin\sqrt{1-x^2}=\pi/2\), so \(F=\pi/2\). Every interior critical point satisfies, for a multiplier \(\lambda\), \(1/\sqrt{1-x_i^2}=2\lambda x_i\). Thus the three squared coordinates each solve \(y(1-y)=c\), and can take only the values \(y\) and \(1-y\). If both values occur, the requirement that three such positive numbers sum to one forces one of them to be zero or one, a contradiction. The only interior critical point is therefore \(x_1=x_2=x_3=1/\sqrt3\). There \(F=3\arcsin(1/\sqrt3)>\pi/2\). This proves unique global maximality, strict positivity of \(p\) for positive triples, and its unattained zero boundary infimum.

For the local expansion, write \(t_i=\log a_i\) and subtract their mean. On \(\sum t_i=0\), expand
\[
\frac{e^{t_i}}{\sqrt{\sum_j e^{2t_j}}}
=\frac1{\sqrt3}\left(1+t_i+\frac{t_i^2}{2}-\frac13\sum_jt_j^2\right)+O(\|t\|^3).
\]
Taylor expansion of \(\sum\arcsin(\cdot)\) at \(1/\sqrt3\) gives
\[
F=3\arcsin(1/\sqrt3)-\frac{1}{4\sqrt2}\sum_it_i^2+O(\|t\|^3).
\]
Multiplying by \(4/\pi\) proves the stated sharp quadratic coefficient.

## Verification
`python check.py` (Python with NumPy and SymPy) verifies the 8-vertex/12-edge cube and 14-vertex/24-edge rhombic dodecahedron, the exact three-case local crossing identity, hundreds of nondegenerate exact-integer normals across four rational stretch families, and the symbolic second derivative along a mean-zero logarithmic perturbation. It also compares the exact probabilities with 150,000 independently seeded sphere normals for each of four aspect ratios. The numerical experiment is **not** used as an infinite proof. The analytical incidence bijection and multiplier argument establish the asserted universal and extremal statements.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg, and Prün (arXiv:2609.16195, first public 2026-09-14) study combinatorial information in sections. Their accessible abstract does not present the pointwise cube–rhombic-dodecahedron identity; full text inspection remained unavailable.

A published research record titled *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes* already gives the single-body box hexagon probability and its cubical optimizer. **Those single-body box formulas and optimality are prior work, not novel claims.** The new result is the *same-normal, every-affine-map, edgewise* complementarity between the two distinct polytopes. It transfers the box distribution and cubic optimizer to the non-box rhombic dodecahedron, and supplies a direct independent edge-angle derivation together with a sharp quadratic stability coefficient. The box record's summary does not assert a pointwise incidence complement for a second polytope, so the implication requires the new twelve-edge correspondence proved above. Other indexed laws for octahedral shadows, four-cube sections, and icosahedral sections concern different objects and parameters.

An older MathPages discussion describes the four-great-circle arrangement of tetrahedral axes and gives its spherical triangle and quadrilateral area fractions. It does not state the generic section complement identity for parallelepipeds and affine rhombic dodecahedra. The exact six/eight event duality is stronger than independently tabulating spherical chamber areas.

## Limitations
No claim of historical priority is certified independently. Inaccessible highly relevant full texts, especially the full Birkemeyer et al. preprint and the exact-box-law record, remain potential sources of unobserved antecedents. The full affine pointwise statement does not imply that the displayed three-term arcsine formula remains valid under a general shear. The sharp quadratic expansion is local in logarithmic axis ratios; no global quantitative stability constant is asserted. Boundary/degenerate orientations are excluded from the combinatorial identity.

## References
- A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public 2026-09-14), https://arxiv.org/abs/2609.16195.
- *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, indexed mathematical research record `2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.
- *N Points On Sphere all in One Hemisphere*, MathPages, discussion of four tetrahedral axes, https://www.mathpages.com/home/kmath327/kmath327.htm (publication date not verified).
