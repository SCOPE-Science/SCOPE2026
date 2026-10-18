# Exact John–Löwner ellipsoid profile of twisted regular polygonal prismatoids

## Finding
Let \(n\ge3\), \(R,h>0\), and \(\phi\in\mathbb R\). Let \(P_n\) be the regular \(n\)-gon of circumradius \(R\), centered at the origin, and define
\[
K=\operatorname{conv}\bigl((P_n\times\{0\})\cup (R_\phi P_n\times\{h\})\bigr),
\quad \beta=\frac\pi n,\quad
\delta=\operatorname{dist}(\phi,(2\pi/n)\mathbb Z)\in[0,\beta],
\quad A=\cos\beta,\quad B=\cos(\beta-\delta).
\]
Here \(R_\phi\) denotes planar rotation. The **unique** maximum-volume inscribed John ellipsoid and minimum-volume enclosing Löwner ellipsoid of \(K\) are, respectively,
\[
J(K)=\left\{(x,z):\frac{\|x\|^2}{R^2AB}+\frac{(z-h/2)^2}{(h/2)^2}\le1\right\},
\qquad
L(K)=\left\{(x,z):\frac{\|x\|^2}{(3R^2/2)}+\frac{(z-h/2)^2}{3h^2/4}\le1\right\}.
\]
In particular, \(L(K)\) is independent of the twist, but \(J(K)\) is not. More precisely,
\[
\operatorname{Vol}_3(K)=\frac{nhR^2\sin\beta}{3}(2A+B),\qquad
\frac{\operatorname{Vol}_3(J(K))}{\operatorname{Vol}_3(K)}
=\frac{2\pi AB}{n\sin\beta(2A+B)},
\qquad
\frac{\operatorname{Vol}_3(J(K))}{\operatorname{Vol}_3(L(K))}
=\frac{2AB}{3\sqrt3}.
\]
For each fixed \(n,R,h\), both ratios above, as well as \(\operatorname{Vol}_3(J(K))\), increase **strictly** with \(\delta\in[0,\beta]\). Therefore the right prism \(\delta=0\) is the unique minimizing twist class, while the half-step antiprism \(\delta=\beta\) is the unique maximizing twist class. The sharp multiplicative improvement in the John volume fraction is
\[
\boxed{\frac{\left(\operatorname{Vol}_3 J/\operatorname{Vol}_3 K\right)_{\delta=\beta}}
{\left(\operatorname{Vol}_3 J/\operatorname{Vol}_3 K\right)_{\delta=0}}
=\frac{3}{1+2\cos(\pi/n)}}.
\]

## Assumptions and scope
The polygons are congruent, regular, concentric in orthogonal projection, and lie in distinct parallel Euclidean planes. No equality of side lengths and lateral edges is imposed; thus the half-step antiprism need not be uniform. No regularity other than \(n\ge3\), \(R,h>0\) is required. All optimizations are over **arbitrary ellipsoids**, with unrestricted centers, tilts, and principal axes. \(\operatorname{dist}(\phi,(2\pi/n)\mathbb Z)\) is ordinary absolute angular distance to integer multiples of \(2\pi/n\). The formula uses the representative \(0\le\delta\le\beta\) afforded by reflection and rotation symmetry.

## Proof
**1. Symmetry reduces unrestricted ellipsoids.** Existence and uniqueness of maximum-volume inscribed and minimum-volume circumscribed ellipsoids hold for each full-dimensional convex body. Rotating about the vertical axis by \(2\pi/n\) preserves \(K\). Reflection in a vertical plane at azimuth \(\phi/2\), combined with \(z\mapsto h-z\), interchanges its two polygonal bases and also preserves \(K\): a bottom vertex at angle \(\theta\) is taken to the upper vertex at angle \(\phi-\theta\). By uniqueness, both extremal ellipsoids must be invariant under these symmetries. The planar quadratic block therefore is scalar, its vertical cross-terms vanish, and its center is \((0,h/2)\). Thus both have unrestricted-in-parameters form \(\|x\|^2/a^2+(z-h/2)^2/b^2\le1\) with \(a,b>0\).

**2. Complete facet description.** It suffices to work with \(0\le\phi=\delta\le\beta\). Rotate the horizontal coordinate system so that a bottom polygon edge has outward unit normal \(u\), with its endpoints at angular offsets \(\pm\beta\). Then the edge has equation \(u\cdot x=RA\); the largest upper vertex projection on \(u\) is \(RB\). The plane through that edge and that upper vertex is a supporting plane. Its centered form is
\[
u\cdot x-\frac{R(B-A)}{h}(z-h/2)\le \frac{R(A+B)}2.
\]
Similarly the upper-polygon edges and their closest bottom vertices supply \(n\) inequalities with the positive vertical coefficient, the same right side and the horizontally rotated unit normal. Together with \(0\le z\le h\), these are all facets: every nonhorizontal face meets each polygonal base in an exposed vertex or edge, and for \(0<\phi<\beta\) it has one edge from one base and one vertex from the other. The endpoint cases follow by continuity (coincident side triangles merge into quadrilaterals at \(\phi=0\)). In particular the two lateral facet orbits have the same horizontal-normal length \(1\), vertical-normal magnitude \(R(B-A)/h\), and centered support value \(R(A+B)/2\).

**3. John optimization.** An axial ellipsoid with semiaxes \(a,b\) lies in every horizontal cap precisely when \(b\le h/2\), and lies in all lateral halfspaces precisely when
\[
a^2+\frac{R^2(B-A)^2}{h^2}b^2\le\frac{R^2(A+B)^2}{4}.
\]
The optimal \(a\) saturates the latter inequality. Its volume is \((4\pi/3)a^2b\), so for \(0<b\le h/2\) the objective, apart from a positive factor, is
\[
f(b)=b\left(\frac{(A+B)^2}{4}-\frac{(B-A)^2}{h^2}b^2\right).
\]
Since \(1/2\le A\le B\le1\), we have \(B/A\le2\), and hence \((A+B)^2>3(B-A)^2\). Therefore \(f'(b)>0\) on \(0<b\le h/2\). The maximizing cap value is \(b=h/2\), at which
\[
a^2=R^2\frac{(A+B)^2-(B-A)^2}{4}=R^2 AB.
\]
This proves the displayed unrestricted John ellipsoid, with tangencies to both horizontal caps and to every lateral facet (when \(0<\delta\le\beta\)).

**4. Löwner optimization.** The \(2n\) vertices all have horizontal norm \(R\) and axial displacement \(h/2\). An axial ellipsoid contains \(K\) if and only if it contains those vertices, namely
\[
\frac{R^2}{a^2}+\frac{h^2}{4b^2}\le1.
\]
At the minimum of \(a^2b\), equality holds. Setting \(p=R^2/a^2\) and \(q=h^2/(4b^2)\), the problem minimizes \(1/(p\sqrt q)\) subject to \(p,q>0\), \(p+q=1\). Strict optimization gives \(p=2/3\) and \(q=1/3\), whence \(a^2=3R^2/2\), \(b^2=3h^2/4\). Every polytope vertex is a contact.

**5. Polytope volume and sharp strict ordering.** The horizontal section of \(K\) at height \(th\) is \((1-t)P_n+tR_\delta P_n\). Its area equals \(((1-t)^2+t^2)S+2t(1-t)V\), where \(S=nR^2\sin\beta A\) is the polygon area and \(V\) is its mixed area with its rotated copy. The support-function edge formula gives \(V=(n/2)(2R\sin\beta)(RB)=nR^2\sin\beta B\). Integration over \(0\le t\le1\) gives \(\operatorname{Vol}_3 K=h(2S+V)/3\), as claimed. The John and Löwner volumes are \(2\pi R^2hAB/3\) and \(\pi\sqrt3 R^2h\), respectively. Since \(B=\cos(\beta-\delta)\) increases strictly on \([0,\beta]\), so do \(AB\) and \(AB/(2A+B)\); the latter derivative with respect to \(B\) is \(2A^2/(2A+B)^2>0\). Evaluating at \(B=A\) and \(B=1\) establishes the sharp factor. \(\square\)

## Verification
The accompanying standalone `verify.py` independently enumerates supporting facets using a three-dimensional convex hull for \(3\le n\le17\), verifies the analytic John ellipsoid's support-function containment and facet tangencies at five nondegenerate twists for each \(n\), and checks all 75 independent hull-volume calculations at the same parameter set including prism and antiprism endpoints. Symbolic identities and the sign of the derivative above prove the full infinite and continuous parameter ranges; finite tests serve only to catch normalization or facet-incidence errors.

## Relationship to prior work
Gruber and Schuster (2012) prove John's general ellipsoid characterization and uniqueness, while Henk (2012) surveys the classical inscribed and circumscribed extremal ellipsoids and applications. Those general tools establish symmetry reduction but do not supply the present angular formula or the strict John-fraction twist inequality. Kovič (2013) classifies centrally symmetric polyhedra with regular polygonal faces, including antiprism families, but the accessible abstract does not assert an ellipsoid formula. The maximum-contained-tetrahedron problem for rotated regular polygonal prismatoids concerns a different extremal object and do not imply the John/Löwner pair or the volume-fraction ordering. Likewise, published exact ellipsoid calculations for unrelated polytope families do not determine the facets or optimized semiaxes here. The specific contribution is the simultaneous complete all-\(n\) angular profile, the unchanged outer ellipsoid, and the sharp improvement of the *relative* inner-ellipsoid volume under twist.

## Limitations
The theorem is confined to two equal-radius regular polygonal bases whose projected centers coincide; different radii, translations, irregular polygons and higher-dimensional analogues are not claimed. The exact formulas are proved for Euclidean volume and ellipsoids, not general affine-invariant approximation functionals. The uniqueness step relies on the established classical extremal-ellipsoid theorem. Historical-priority uncertainty remains for potentially unindexed special-polyhedron formulas; the 2013 Kovič PDF was unavailable for complete inspection, so its abstract alone is not used as evidence of full-text noncoverage. No independent review has been performed.

## References
1. P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246v1, 31 July 2012.
2. M. Henk, *Löwner–John Ellipsoids*, *Documenta Mathematica*, Extra Volume ISMP (2012), 95–106, DOI 10.4171/DMS/6/15.
3. J. Kovič, *Centrally symmetric convex polyhedra with regular polygonal faces*, *Mathematical Communications* **18** (2013), 429–440; https://hrcak.srce.hr/110844.
