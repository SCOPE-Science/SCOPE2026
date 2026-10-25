# Exact Cheeger sets and a sharp flat-arc limit for regular disk triangles

## Finding
Fix a minimum Euclidean width \(w>0\). For each \(R\ge w\), let \(T_{w,R}\) denote the regular radius-\(R\) disk triangle of minimum width \(w\): the intersection of three congruent disks whose centers form an equilateral triangle. Write \(h(T)\) for the standard planar Cheeger constant \(\inf_{E\subseteq T,\ |E|>0}P(E)/|E|\), with finite-perimeter measurable competitors.

The exact Cheeger radius \(s_*(w,R)=1/h(T_{w,R})\) is the unique positive solution of an explicitly defined scalar equation. Its Cheeger set has three inherited circular arcs of radius \(R\) and three free circular arcs of radius \(s_*\), alternating. More precisely, set
\[
 v=\frac12\left[\sqrt{\frac{4R^2-(R-w)^2}{3}}-(R-w)\right],\qquad
 \rho=w-v,\qquad c=R-\rho .
\]
For \(0\le s\le\rho\) define
\[
 v_s=\frac{\sqrt{4(R-s)^2-3c^2}-c}{2},\quad
 \alpha_s=2\arcsin\left(\frac{\sqrt3\,v_s}{2(R-s)}\right),\quad
 G(s)=\frac{3\sqrt3}{4}v_s^2+\frac32(R-s)^2(\alpha_s-\sin\alpha_s).
\]
Then \(G(s_*)=\pi s_*^2\) has exactly one solution in \((0,\rho)\). The Cheeger set is \((T_{w,R})_{-s_*}+s_*B\), where \(B\) is the closed unit disk and the subscript denotes Euclidean erosion. Its three inherited arcs each subtend \(\alpha_{s_*}\) at radius \(R\); its three free arcs each subtend \(2\pi/3-\alpha_{s_*}\) at radius \(s_*\).

As \(R\to\infty\) with \(w\) fixed, put \(H=3+\sqrt{\pi\sqrt3}\). One has the **sharp first-order flat-arc limit**
\[
 s_*(w,R)=\frac wH+\frac{w^2(H^2+6H-9)}{6H^3R}+O\!\left(\frac{w^3}{R^2}\right),
\qquad
 h(T_{w,R})=\frac Hw-\frac{H^2+6H-9}{6H}\frac1R+O\!\left(\frac{w}{R^2}\right).
\]
In particular, the universal positive constant \(K=(H^2+6H-9)/(6H)\) is the exact limit of \(R(H/w-h(T_{w,R}))\) and cannot be reduced.

## Assumptions and scope
All constructions are two-dimensional and Euclidean. \(R\) and \(w\) are positive lengths, with \(R\ge w\); the limit means \(R/w\to\infty\). The family \(T_{w,R}\) is uniquely specified up to rigid motions. At \(R=w\), it is the regular Reuleaux triangle; as \(R\to\infty\), it approaches the equilateral triangle of altitude \(w\). The Cheeger constant uses ordinary Euclidean perimeter, not minimal width in place of perimeter. The notation \(T_{-s}=\{z:z+sB\subseteq T\}\) is the inner parallel body. Big-O constants are absolute after normalization by scaling, and do not claim uniformity in arbitrary unrelated shape families.

## Proof
**Geometry and width.** Put \(u_j=(\cos(2\pi j/3),\sin(2\pi j/3))\) for \(j=0,1,2\) and let \(T=\bigcap_{j=0}^2B(cu_j,R)\). Its three vertices lie at \(vu_j\), and the symmetry-center inradius is \(\rho=R-c\). For each vertex, equilateral geometry gives \(R^2=c^2+cv+v^2\). The least width is attained from a vertex to the opposite circular arc midpoint, so \(w=v+\rho\) (the standard width characterization for regular disk triangles, recalled in Fodor–Robock–Sagmeister, Lemma 2.2, and in Bezdek's disk-triangle formulas). Solving these equations yields the displayed values of \(v,\rho,c\). The formula gives \(v>0\), \(\rho>0\), \(c>0\) for \(R\ge w>0\).

**The complete erosion area.** Erosion distributes across intersections and \(B(p,R)_{-s}=B(p,R-s)\) when \(0\le s\le\rho\). Thus \(T_{-s}=\bigcap_jB(cu_j,R-s)\). Its three vertices are \(v_su_j\), because \((R-s)^2=c^2+cv_s+v_s^2\), and the chord between adjacent vertices is \(\sqrt3v_s\). The intersection consists of the equilateral core triangle, of area \(3\sqrt3v_s^2/4\), and three circular segments of radius \(R-s\) and central angle \(\alpha_s\). Each segment has area \((R-s)^2(\alpha_s-\sin\alpha_s)/2\); hence its exact area is \(G(s)\). At \(s=\rho\) the erosion is a singleton, and \(G(\rho)=0\); at \(s=0\) it has positive area. Strict inclusion of the nested erosions for \(s\in[0,\rho)\) makes \(G\) strictly decreasing and continuous. Meanwhile \(\pi s^2\) strictly increases. The root \(s_*\in(0,\rho)\) therefore exists and is unique.

**Cheeger characterization and six arcs.** The planar convex Cheeger theorem states that the unique Cheeger set of a convex body \(T\) is \(T_{-s}+sB\), where \(|T_{-s}|=\pi s^2\) and \(s=h(T)^{-1}\). Applying this classical theorem proves \(h(T)=1/s_*\). The \(3\)-fold symmetric erosion has three circular side arcs, of radius \(R-s_*\), subtending \(\alpha_{s_*}\). Taking its outer parallel body by \(s_*\) changes these radii to \(R\) without changing their turning angles. Each of its three vertices is rounded by a radius-\(s_*\) arc of turn \(2\pi/3-\alpha_{s_*}\). The six arcs exhaust the boundary because their total turn is \(3\alpha_{s_*}+3(2\pi/3-\alpha_{s_*})=2\pi\). As a consistency check, \(P(C)=3(R-s_*)\alpha_{s_*}+2\pi s_*\) and, by Steiner's formula for the erosion body, \(|C|=G(s_*)+3s_*(R-s_*)\alpha_{s_*}+\pi s_*^2=s_*P(C)\).

**Sharp limit.** Normalize \(w\) by scaling if desired and set \(\varepsilon=1/R\). Direct binomial expansion of the vertex and eroded-vertex equations, locally uniformly for \(s\) near the limiting Cheeger radius, gives
\[
 v_s=\frac{2w}{3}-2s+\frac{-w^2/9+2ws-3s^2}{R}+O\!\left(\frac{w^3}{R^2}\right).
\]
A circular segment with chord length \(d\) and large supporting radius \(q\) has area \(d^3/(12q)+O(d^5/q^3)\), obtained by expanding \(\frac12q^2(2\arcsin(d/(2q))-\sin(2\arcsin(d/(2q))))\). Summing three segments and the equilateral core therefore yields
\[
 G(s)=\frac{(w-3s)^2}{\sqrt3}
 +\frac{\sqrt3\,(w-3s)(w^2+6ws-9s^2)}{9R}
 +O\!\left(\frac{w^4}{R^2}\right).
\]
For the limiting equilateral triangle the equation \((w-3s)^2/\sqrt3=\pi s^2\) has its unique admissible solution \(s_0=w/H\), since \(0<s<w/3\). At this root the derivative of the left side minus \(\pi s^2\) equals \(-2\sqrt3(w-3s_0)-2\pi s_0<0\). The analytic implicit-function theorem applies for \(1/R\) sufficiently small, and substitution of \(s=s_0+s_1/R+O(R^{-2})\) gives
\[
 s_1=\frac{w^2(H^2+6H-9)}{6H^3}.
\]
Expanding \(1/s\) produces the stated Cheeger law with coefficient \(K=(H^2+6H-9)/(6H)>0\). Because the normalized scaled difference converges to precisely \(K\), this coefficient is sharp.

## Verification
The standalone `verify.py` (Python 3.10 or later; optional SymPy) checks the geometric identities, eroded-area formula by independent angular ray integration for five nondegenerate members and several erosion depths, uniqueness-root consistency, Cheeger area/perimeter identity, and numerical convergence to the exact flat-arc coefficient. With SymPy installed it also checks exact symbolic expansions for the eroded vertices and first-order area coefficient. Run `python verify.py` in the extracted directory; successful output is `CHEEGER_DISK_TRIANGLE_CHECKS_OK`. Numerical quadrature is supplementary verification, not an infinite proof; the exact identities and implicit expansion above supply the all-parameter proof.

## Relationship to prior work
Fodor–Robock–Sagmeister (2026, arXiv:2602.19300), Theorem 1.1 and Lemma 2.2, motivate and characterize the fixed-radius minimal-width disk-triangle family; they establish area extremality, not this Cheeger shape-and-rate theorem. Bezdek (2009, arXiv:0903.5361), Remark 1.4, computes the corresponding disk-triangle inradius, width, area and perimeter under a center-distance parametrization, which determines the un-eroded shape but does not state the Cheeger-root formula or flat-arc coefficient. Bogosel (2025 online, DOI:10.5802/aif.3728) examines Cheeger constants for constant-width bodies and the Reuleaux triangle using inner-parallel geometry; the present theorem covers disk triangles of varying radius and width fixed, with an explicit first-order limit. Drach (2026) studies Cheeger inequalities for two-disk lenses and the general inner-parallel characterization; the source does not compute this three-disk coefficient. The published mathematical note *A sharp Steiner-area phase diagram for regular disk triangles* (2026) analyzes **outer** offsets \(T+tB\) and area/perimeter optimization as \(R\) varies, not the **inner** offset Cheeger equation or its flat-arc rate. The standard general Cheeger theorem itself is acknowledged rather than claimed new.

## Limitations
The all-parameter Cheeger radius is specified by a unique scalar equation rather than elementary closed form. No global monotonicity of the Cheeger constant in \(R\) is asserted, and no extremal statement over arbitrary convex bodies is made. Inner-parallel formulas can be derived from general disk-polygon techniques; the distinct quantitative content is the explicit complete variable-radius geometry and sharp first-order flat-arc Cheeger coefficient. An unindexed equivalent derivation may exist. Independent verification has not been performed.

## References
1. F. Fodor, N. Robock, Á. Sagmeister, *Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2602.19300, first posted 2026-02-22, https://arxiv.org/abs/2602.19300.
2. M. Bezdek, *On a generalization of the Blaschke–Lebesgue theorem for disk-polygons*, arXiv:0903.5361, first posted 2009-03-31, https://arxiv.org/abs/0903.5361.
3. B. Bogosel, *A geometric proof of the Blaschke–Lebesgue theorem for the Cheeger constant*, online 2025-08-01, DOI:10.5802/aif.3728, https://doi.org/10.5802/aif.3728.
4. K. Drach, *Stability of reverse isoperimetric inequalities in the plane: Area, Cheeger, and inradius*, Bulletin of the London Mathematical Society (2026).
5. *A sharp Steiner-area phase diagram for regular disk triangles*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-steiner-area-phase-diagram-for-regular-disk-triangles--3d6ed11c0577.
6. Classical characterization of the Cheeger set of a planar convex body by its inner parallel area equation, as discussed in references 3 and 4.
