# Three symmetry-axis preference reversals for partial planks of a regular octagon

## Finding
Let \(P=\operatorname{conv}\{(\cos(j\pi/4),\sin(j\pi/4)):0\le j<8\}\), the regular octagon with circumradius one. For a plank of width \(W\) whose normal points along one of the eight reflection axes of \(P\), maximize the area of its intersection with \(P\) over translations of the plank and over these reflection axes. There are two dihedral orbits of axes: vertex-normal axes (V) and edge-normal axes (E). A centered plank attains the largest area for either orbit.

Define
\[
 a=\frac1{\sqrt2},\quad c=\cos(\pi/8),\quad d=\sin(\pi/8),\quad h=c+d,\quad m=2-\sqrt2.
\]
The three sharp critical half-widths are
\[
 s_1=\frac{2(1-c)}{\sqrt2-1},\qquad
 s_2=\frac{h-1+\sqrt{(h-1)^2-m^2/4}}{m},\qquad
 s_3=\frac12+d.
\]
They satisfy \(0<s_1<d<s_2<a<s_3<c\). For \(0<W<2c\), let \(s=W/2\). The E orbit gives strictly more covered area precisely when \(s_1<s<s_2\) or \(s_3<s<c\); the V orbit gives strictly more precisely when \(0<s<s_1\) or \(s_2<s<s_3\). At the three critical widths the two orbits tie. Thus, restricted to reflection-axis directions, **the preferred orientation reverses exactly three times** as the width increases. The critical full widths are approximately \(0.735084259941727\), \(1.35573629194945\), and \(1.76536686473018\).

For \(2c\le W<2\), E planks cover all of \(P\), while V planks do not; for \(W\ge2\), both orbits permit complete coverage. No claim is made that a reflection-axis plank is globally optimal among all unrestricted directions.

## Assumptions and scope
All planks are closed regions between parallel straight lines in the Euclidean plane. Plank width is Euclidean distance between those lines, not a normalized relative width. The optimization and three-reversal theorem concern **only** normals along the two dihedral orbits of symmetry axes of the stated regular octagon. Boundary lines have zero area. The octagon has area \(2\sqrt2\). Width \(W\) may be any nonnegative real number, but all three reversals occur for \(0<W<2c\).

## Proof
For a fixed unit normal \(u\), the section length \(\ell_u(t)=\mathcal H^1(P\cap\{x:\langle x,u\rangle=t\})\) is even by central symmetry. It is concave on its support by planar Brunn--Minkowski; hence it is nonincreasing for \(t\ge0\). For a given width, integrating \(\ell_u\) over an interval of that width is maximized by the interval centered at zero. Therefore it is enough to compare centered planks with the two axis-normal choices.

Write \(C_V(s)\) and \(C_E(s)\) for the areas in the single outer halfplane beyond distance \(s\) from the octagon center, with normal respectively toward a vertex and perpendicular to an edge. For \(0\le s\le1\), direct slicing of the octagon gives
\[
 C_V(s)=\begin{cases}
 \sqrt2-2s+(\sqrt2-1)s^2,&0\le s\le a,\\
 (1+\sqrt2)(1-s)^2,&a\le s\le1.
 \end{cases}
\]
It equals zero for \(s\ge1\). Indeed, for nonnegative horizontal coordinate \(x\), the vertical full-chord length is \(2[1-(\sqrt2-1)x]\) on \([0,a]\), and \(2(1+\sqrt2)(1-x)\) on \([a,1]\). Integrating each expression from \(s\) to the support point yields the displayed cap formulas.

For \(0\le s\le c\), the edge-normal chords have full length \(2c\) for \(0\le x\le d\), and \(2(c+d-x)\) for \(d\le x\le c\). Thus
\[
 C_E(s)=\begin{cases}
 \sqrt2-2cs,&0\le s\le d,\\
 (c-s)(c+2d-s),&d\le s\le c,
 \end{cases}
\]
and \(C_E(s)=0\) for \(s\ge c\). In either orbit the covered area of the centered strip of half-width \(s\) is \(2\sqrt2-2C_\bullet(s)\). Consequently V covers more exactly when \(C_E(s)-C_V(s)>0\).

For \(0\le s\le d\), the cap difference factors exactly as
\[
 C_E(s)-C_V(s)=s\bigl(2(1-c)-(\sqrt2-1)s\bigr),
\]
so the only positive crossing in this interval is \(s_1\). For \(d\le s\le a\), the difference is
\[
 m s^2-2(h-1)s+\frac m4.
\]
This quadratic has two real roots; its smaller root lies below \(d\), and its larger root \(s_2\) lies in \((d,a)\). For \(a\le s\le c\), the difference equals
\[
 (c-s)(c+2d-s)-(1+\sqrt2)(1-s)^2.
\]
This concave quadratic has a root at \(s=s_3=1/2+d\), with its other root below \(a\). This identifies precisely one crossing in \((a,c)\). For fully explicit verification of which roots belong to the admissible intervals, exact substitutions give
\[
 C_E(d)-C_V(d)=1+\sqrt{2-\sqrt2}-\frac{5\sqrt2}{4}<0,
\]
\[
 C_E(a)-C_V(a)>0,
 \qquad C_E(c)-C_V(c)=-(1+\sqrt2)(1-c)^2<0.
\]
The middle strict inequality follows by inserting \(a=\sqrt2/2\) into the displayed cap polynomials; the three values lie respectively in the rational intervals \((-0.00241,-0.00239)\), \((0.00579,0.00580)\), and \((-0.01400,-0.01398)\). For a direct rational certificate of the stated strict signs, use the enclosures \(1.4142135623<\sqrt2<1.4142135624\), \(0.9238795325<c<0.9238795326\), \(0.3826834323<d<0.3826834324\), and \(0.7071067811<a<0.7071067812\). The enclosures follow from squaring positive rational endpoints and, for \(c,d\), applying \(4c^2=2+\sqrt2\) and \(4d^2=2-\sqrt2\). Elementary rational interval substitution in the displayed cap polynomials proves the three stated sign intervals; no floating-point sign decision is needed. On \([d,a]\) the polynomial is convex, so opposite endpoint signs force exactly one crossing; on \([a,c]\) it is concave and the same conclusion holds. All inequalities are strict away from the stated crossing widths. For \(s\ge c\), the E cap vanishes and for \(s<1\) the V cap remains positive, completing the classification.

## Verification
The standalone script `check_octagon.py` performs symbolic algebra and endpoint checks using SymPy and compares both cap formulas against independent Euclidean polygon clipping over 2,001 half-widths. It additionally checks the proposed strict sign intervals at 1,599 sampled half-widths. The script produces `OCTAGON_SYMMETRY_PLANK_CHECK_OK 5601 ...`. These finite comparisons are diagnostic only; the exact geometric slicing, quadratic factorization, endpoint signs, and one-crossing arguments above prove the statements for every real width.

## Relationship to prior work
Bakaev and Polyanskii, *Optimal partial plank coverings* (first public arXiv version July 29, 2026, arXiv:2607.27483), prove that for a planar convex body and fixed total plank width, some single plank is globally optimal. Their Theorem 12 neither restricts normals to the reflection axes of a regular octagon nor determines their relative covered areas, the three explicit crossing thresholds, or a symmetry-axis preference phase diagram. The present result is a constrained, exact orientation comparison, **not** a claim of unrestricted global optimality and **not** a new proof of single-plank optimality.

## Limitations
This exact three-crossing law compares only the two natural orbits of reflection-axis normals. For intermediate widths, a non-symmetry-axis plank can cover more area than both orbit representatives; such directions are outside the theorem. No assertion is made about the unrestricted optimal direction as a function of width, or about arbitrary polygonal shapes, and independent historical priority verification remains outstanding.

## References
- E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483v1, first publicly submitted July 29, 2026. Preprint full text, especially Theorem 12. https://arxiv.org/abs/2607.27483
- W. Verreault, *Plank theorems and their applications: A survey*, Bulletin of the London Mathematical Society 58 (2026), article e70230, first online November 9, 2025. https://doi.org/10.1112/blms.70230
