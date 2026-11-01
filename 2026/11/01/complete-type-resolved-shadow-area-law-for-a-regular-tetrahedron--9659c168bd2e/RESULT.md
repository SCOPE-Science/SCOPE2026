# Complete type-resolved shadow-area law for a regular tetrahedron

## Finding
Let \(T\subset\mathbb R^3\) be the regular tetrahedron with vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
\]
For a uniformly random direction \(U\in S^2\), let \(A\) be the Euclidean area of the orthogonal projection of \(T\) onto \(U^\perp\), and let \(N\) be the number of projected vertices. Almost surely \(N\in\{3,4\}\). This theorem determines the **full joint law** of \((A,N)\), not just the marginal area distribution.

Put
\[
 r_0=2\sqrt2,\qquad r_1=4\sqrt{2/3},\qquad
 r_2=2\sqrt3,\qquad r_3=4,
\]
\[
 p_3=1-\frac6\pi\arcsin(1/3),\qquad
 p_4=\frac6\pi\arcsin(1/3).
\]
For \(0<h<1\), define the elementary spherical-segment function, on the parameter range used below, by
\[
 G_h(t)=\begin{cases}
 2\left[\arccos\!\left(\dfrac{h}{\sqrt{1-t^2}}\right)
 -t\arccos\!\left(\dfrac{ht}{\sqrt{(1-h^2)(1-t^2)}}\right)\right],
 &0<t<\sqrt{1-h^2},\\[2mm]
 0,&\sqrt{1-h^2}\le t<1.
 \end{cases}
\]
The **two subdistribution functions**, \(F_j(r)=\mathbb P\{A\le r,\,N=j\}\), are exactly
\[
\boxed{
F_3(r)=\begin{cases}
0,&r\le r_0,\\
p_3-4\left(1-\dfrac r{2\sqrt3}\right)
 +\dfrac6\pi G_{1/3}\!\left(\dfrac r{2\sqrt3}\right),
 &r_0<r<r_2,\\
p_3,&r\ge r_2,
\end{cases}}
\]
and
\[
\boxed{
F_4(r)=\begin{cases}
0,&r\le r_0,\\
p_4-3\left(1-\dfrac r4\right)
 +\dfrac6\pi G_{1/\sqrt3}\!\left(\dfrac r4\right),
 &r_0<r<r_3,\\
p_4,&r\ge r_3.
\end{cases}}
\]
Consequently \(\mathbb P\{A\le r\}=F_3(r)+F_4(r)\), and the conditional distribution given \(N=j\) is \(F_j(r)/p_j\). Both types have the same attainable minimum \(r_0\); triangular shadows have maximum \(r_2\), whereas quadrilateral shadows have maximum \(r_3\). On the entire intervals \(r_1<r<r_2\) and \(r_1<r<r_3\), respectively, their subdistribution densities are exactly the constants
\[
\frac{dF_3}{dr}=\frac2{\sqrt3},\qquad \frac{dF_4}{dr}=\frac34.
\]
At their shared lower endpoint the two probabilities have the **same, sharp quadratic onset**:
\[
\boxed{F_3(r_0+\varepsilon)=F_4(r_0+\varepsilon)
 =\frac{3}{2\sqrt2\,\pi}\varepsilon^2+O(\varepsilon^3)
 \qquad(\varepsilon\downarrow0).}
\]
These formulas describe both silhouette classes for every area threshold. The marginal law, the unweighted silhouette probabilities, and the first two silhouette-conditional moments were previously known; their rediscovery is not asserted here.

## Assumptions and scope
The tetrahedron has edge length \(2\sqrt2\); its normalization matters: scaling edge lengths by \(c>0\) multiplies all area thresholds by \(c^2\). The direction is Haar-uniform on \(S^2\), and antipodal directions define the same projection plane. The exceptional viewing directions at which projected vertices coincide or the silhouette type is ambiguous have spherical measure zero. Every probability formula concerns orthogonal, not perspective, projection.

The function \(G_h\) is evaluated only with \(h\in\{1/3,1/\sqrt3\}\) and \(t\in(0,1)\), so its specified domain is sufficient. Its branch values agree continuously at the transition \(t=\sqrt{1-h^2}\). The formula for \(F_3\) applies for \(r\in(r_0,r_2)\), and the one for \(F_4\) for \(r\in(r_0,4)\), so no inverse trigonometric expression is used outside its real domain.

## Proof
**1. Exact area and silhouette partition.** Each face has area \(2\sqrt3\) and unit normal proportional to one of the four displayed vertex vectors. Cauchy's facet-projection formula therefore gives, for \(u\in S^2\),
\[
A(u)=\sum_{v\in\operatorname{vert}(T)}|v\cdot u|.
\]
Write \(a=|u_1|\), \(b=|u_2|\), \(c=|u_3|\), and \(s=a+b+c\). The four signed linear forms inside this sum are either two pairs of opposite signs, or one sign opposed to three. In each coordinate orthant, direct addition of the four absolute values shows that
\[
\boxed{A(u)=2\max\{s,2\max(a,b,c)\}.}\tag{1}
\]
In the first case a projected tetrahedral vertex lies in the projected opposite face, producing a triangular silhouette. Equivalently, direct convex-hull comparison of the four projected vertices gives, off the tie planes,
\[
N(u)=3\quad\Longleftrightarrow\quad s>2\max(a,b,c),
\qquad
N(u)=4\quad\Longleftrightarrow\quad s<2\max(a,b,c).
\tag{2}
\]
Thus the triangular directions are eight congruent spherical triangles, one centered on each signed diagonal \(d=(\pm1,\pm1,\pm1)/\sqrt3\). The quadrilateral directions are six congruent spherical diamonds, centered at the signed coordinate axes. These fourteen regions partition the viewing sphere up to great-circle boundaries. The triangular region centered at \((1,1,1)/\sqrt3\) is bounded by the three planes \(x=y+z\), \(y=x+z\), \(z=x+y\). Its three interior spherical angles are \(\arccos(1/3)\), so its area is \(3\arccos(1/3)-\pi\). The resulting probability is
\[
\frac8{4\pi}\bigl(3\arccos(1/3)-\pi\bigr)
=1-\frac6\pi\arcsin(1/3)=p_3.
\]
The remaining six diamonds have total probability \(p_4=1-p_3\). This also reproves the **prior-known** unweighted silhouette proportions.

**2. A spherical segment in closed form.** Let \(c,m\in S^2\) satisfy \(c\cdot m=-h\), with \(0<h<1\), and consider the part of the cap \(\{u:u\cdot c>t\}\) lying beyond the great circle \(u\cdot m=0\), namely \(\{u:u\cdot c>t,\ u\cdot m>0\}\). Choose \(c=e_3\), \(m=(\sqrt{1-h^2},0,-h)\). At height \(z=u_3\), the angular length of the permitted great-circle slice is
\[
2\arccos\left(\frac{hz}{\sqrt{(1-h^2)(1-z^2)}}\right)
\]
for \(0<z<\sqrt{1-h^2}\), and zero at larger positive heights. Hence its spherical area is
\[
2\int_t^{\sqrt{1-h^2}}
\arccos\left(\frac{hz}{\sqrt{(1-h^2)(1-z^2)}}\right)\,dz.
\tag{3}
\]
Differentiating the displayed closed expression for \(G_h(t)\) gives the negative integrand in (3), and both vanish at the upper endpoint; thus (3) equals \(G_h(t)\) exactly. This also proves positivity and continuity of the function without any numerical approximation.

**3. The triangular-shadow distribution.** Inside each of the eight spherical triangles, (1) reduces to
\[
A(u)=2\sqrt3\,(u\cdot d).
\]
The portion with \(A>r\) is the intersection of the spherical triangle with a cap of height \(t=r/(2\sqrt3)\) about \(d\). A full cap has area \(2\pi(1-t)\). Each side plane has outward spherical normal \(m\) satisfying \(d\cdot m=-1/3\), so the area protruding beyond that side is exactly \(G_{1/3}(t)\), by step 2. The cap does not include any triangular vertex for \(r>r_0\), because each vertex has projected area \(r_0\). Consequently its three side protrusions are pairwise disjoint for all \(r_0<r<r_1\). At \(r=r_1\), the cap first becomes contained in the spherical triangle; this is the identity \(r_1/(2\sqrt3)=\sqrt{1-1/9}\). Above \(r_1\) the segment function vanishes. Multiplication by eight and division by the sphere area \(4\pi\) gives
\[
\mathbb P(N=3,A>r)=4(1-t)-\frac6\pi G_{1/3}(t)
\qquad(r_0<r<r_2).
\]
Subtracting this from \(p_3\), and checking the endpoint values, proves \(F_3\). It also proves the maximal triangular-shadow area \(r_2\).

**4. The quadrilateral-shadow distribution.** The region centered at \(e_1\) is the spherical diamond \(u_1>|u_2|+|u_3|\), within which (1) reduces to \(A(u)=4u_1\). Each of its four side planes has outward normal \(m\) with \(e_1\cdot m=-1/\sqrt3\), so the protrusion of a height-\(t=r/4\) cap beyond one side has area \(G_{1/\sqrt3}(t)\). The four protrusions are pairwise disjoint for \(r>r_0\), since all four vertices of the diamond have area \(r_0\). They disappear at \(r=r_1\), equivalent to \(r_1/4=\sqrt{1-1/3}\). Summing the six diamond pieces and normalizing yields
\[
\mathbb P(N=4,A>r)=3(1-t)-\frac6\pi G_{1/\sqrt3}(t)
\qquad(r_0<r<4).
\]
Subtracting from \(p_4\) proves \(F_4\) and its maximal area \(4\). Differentiating the linear cap contributions once \(G_h=0\) gives both stated constant-density regimes.

**5. Sharp lower onset.** The global minimum \(r_0\) occurs at the twelve signed coordinate permutations of \((1,1,0)/\sqrt2\). Around \(u_0=(1,1,0)/\sqrt2\), use local coordinates \(p=u_1-u_2\), \(z=u_3\), and \(s=u_1+u_2=\sqrt{2(1-z^2)-p^2}\). For sufficiently small \(p,z\), (1)--(2) become
\[
 A(u)=2\left(s+\max\{|p|,|z|\}\right),\qquad
 N(u)=3\ \Longleftrightarrow\ |z|>|p|.
\]
The spherical area element is \((1/\sqrt2+O(p^2+z^2))\,dp\,dz\). For \(\varepsilon\downarrow0\), the set \(A\le r_0+\varepsilon\) in this chart is, to first order, the square \(|p|,|z|\le\varepsilon/2\); its area is \(\varepsilon^2/\sqrt2+O(\varepsilon^3)\). The two types occupy equal halves of this square, with an \(O(\varepsilon^3)\) area error. Multiplying by twelve disjoint charts and dividing by \(4\pi\) proves the common coefficient \(3/(2\sqrt2\pi)\), with a strictly positive leading term. No finite simulation is used in this proof.

## Verification
Run `python3 verify.py` with the Python standard library. The program performs 5,444 deterministic checks and independently generates 400,000 Haar-uniform orientations. It compares the type-resolved CDF at eleven thresholds, independently projects the tetrahedron's four vertices and computes convex hulls for 700 directions, numerically integrates the cap/hemisphere segment area using a second parametrization, checks both endpoint expansions, and independently integrates the subdistributions to recover **previously published** conditional first and second moments. The verifier prints `PASS` when all assertions hold. Finite tests corroborate, but do not certify, universal geometric assertions; steps 1--5 are their proof.

## Relationship to prior work
Jakimiuk and Pandis (first public 16 October 2026) develop global stability for extremal simplex projection volume, rather than the joint type-and-area law. Their explicit projection formula is related to (1), and its underlying classical versions are credited.

Vickers and Brown (2001, Sections 3 and Appendix B) **already determine the entire marginal distribution** of the projected area of a regular tetrahedron (at unit edge length), including its density transitions. This article also observes that the projected silhouette may be triangular or quadrilateral. Accordingly, neither \(F_3+F_4\), the marginal support, nor the general spherical-cap method is claimed as new. The new assertion is the separate, complete, all-threshold pair \((F_3,F_4)\), including which shape realizes each part of the area distribution, distinct constant-density upper regimes, and equal sharp quadratic lower onsets. Summing the two formulas recovers the earlier marginal; conversely the sum cannot determine its two summands.

Finch (2012) computes regular-tetrahedral shadow moments and the unweighted silhouette probabilities. A published geometric-moment calculation for arbitrary tetrahedra gives the first two moments **conditioned on shadow type**, but explicitly stops short of the full conditional distribution; integrating the formulas above reproduces its regular-tetrahedron special case. Other published calculations of area--perimeter covariance and Platonic-shadow variance concern different observables and do not imply either subdistribution. The geometric segment decomposition is therefore a separate conditional calculation, not a re-expression of known marginal data.

## Limitations
This theorem is for Haar-uniform viewing directions of the regular tetrahedron in three Euclidean dimensions, not arbitrary tetrahedra, higher-dimensional simplices, perspective projections or biased orientations. No general inference or universal extremal inequality is asserted. The complete marginal distribution and the low conditional moments belong to the cited earlier work; the novelty claim is confined to the **full type-resolved law**. Older stereological calculations may contain a synonymous result not located by the inspected literature; historical priority is consequently provisional. No independent mathematical audit has been performed.

## References
1. J. Jakimiuk and C. Pandis, *Stability of Hyperplane Projections of the Regular Simplex and \(L_p\)-Projection Bodies of Balls in \(\ell_q^n(\mathbb R)\)*, arXiv:2610.23489v1 (first publicly submitted 2026-10-16), https://arxiv.org/abs/2610.23489.
2. G. T. Vickers and D. J. Brown, *The Distribution of Projected Area and Perimeter of Convex, Solid Particles*, Proceedings of the Royal Society A 457 (2001), 283--306, doi:10.1098/rspa.2000.0667, especially Section 3 and Appendix B.
3. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (2012), especially Sections 2.1 and 5, https://arxiv.org/abs/1203.2464.
4. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-area-weighted-silhouette-probabilities-of-arbitrary-tetrahedra--ddfd7f3eeb66 (its conditional moment results are prior work).
