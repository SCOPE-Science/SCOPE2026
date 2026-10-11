# Sharp vertex-distance bound for reflection-symmetric equilateral pentagons

## Finding

For every nondegenerate, convex, reflection-symmetric equilateral Euclidean pentagon \(P\), let \(w(P)>0\) be its minimum Euclidean width and let \(S(P)\) be the sum of the distances over its ten unordered vertex pairs. Then

\[
\boxed{\frac{S(P)}{w(P)}\le 4+6\sqrt3.}
\]

Equality holds, among weakly convex five-vertex configurations, exactly for the isosceles trapezoid of two parallel edges in the ratio \(2:1\), with its shorter edge of length equal to both nonparallel edges and with a fifth marked vertex at the midpoint of the longer edge, up to Euclidean similarity. In particular, for **strictly convex** reflection-symmetric equilateral pentagons the bound is a sharp but unattained supremum; the limiting configuration has one straight interior angle. The result is for the reflection-symmetric subclass, not for arbitrary equilateral pentagons.

The bound resolves, within the symmetric five-vertex subclass, the extremal shape proposed for the full odd-sided problem in Audet–Ninin's numerical Conjecture 9 (later published version); the full problem remains outside this theorem.

## Assumptions and scope

A *five-vertex weakly convex equilateral configuration* is an ordered cyclic five-tuple of distinct planar points, consecutive distances equal to a positive number, and nonnegative signed turns, allowing a straight turn. The convex hull must have nonzero area. The total vertex-distance sum counts marked vertices, including a marked point lying in the relative interior of a hull edge. A reflection symmetry is a Euclidean reflection preserving this cyclic five-tuple as a labeled cyclic configuration (up to its dihedral action). By oddness, it fixes one vertex and exchanges two pairs. For a strictly convex pentagon the usual reflection of the geometric polygon is equivalent.

Both \(S(P)\) and \(w(P)\) scale linearly, so their ratio is invariant under similarity. We normalize every side to length \(1\). Place the reflection axis vertically, the opposite edge horizontally, and write the vertices cyclically as

\[
 p_0=(0,z),\quad p_1=(x,y),\quad p_2=(\tfrac12,0),\quad
 p_3=(-\tfrac12,0),\quad p_4=(-x,y).
\]

The side constraints and convexity give the exact one-parameter family

\[
 \frac14\le x\le1,\qquad
 y=\sqrt{1-(x-\tfrac12)^2},\qquad
 u=\sqrt{1-x^2},\qquad z=y+u.
\]

All square roots are the nonnegative ones. The endpoints of the parameter interval are allowed only in the weakly convex completion; \(\tfrac14<x<1\) corresponds to strictly convex pentagons. Distinctness and positive area hold throughout the closed interval.

## Proof

**1. Reduction and convexity.** Reflection across the vertical axis fixes one vertex and the midpoint of the opposite side. After scaling, that opposite side is the horizontal segment joining \((\pm\tfrac12,0)\). Convexity places the two adjacent vertices above this edge, and the fixed vertex above their common chord, fixing the positive signs of the two square roots displayed above. The only nonautomatic turn condition occurs at the adjacent vertices and is

\[
 xy\ge(\tfrac12-x)u\quad \text{when }x<\tfrac12.
\]

Squaring this inequality in the indicated range gives

\[
 x^2y^2-(\tfrac12-x)^2u^2=\frac{4x-1}{4}\ge0,
\]

hence \(x\ge\tfrac14\). For \(x\ge\tfrac12\) the turn condition is automatic. Every normalized configuration in the theorem occurs in this family, and conversely every parameter in the closed interval yields an allowable weakly convex configuration.

**2. Exact total distance and width.** Five of the ten unordered vertex distances equal the common side length \(1\). The remaining five are two copies of \(\sqrt{z^2+\tfrac14}\), one copy of \(2x\), and two copies of \(\sqrt{1+2x}\). Thus

\[
 S(x)=5+2\sqrt{z^2+\tfrac14}+2x+2\sqrt{1+2x}.
 \tag{1}
\]

For a convex polygon, its least width occurs in a direction perpendicular to a supporting edge. To see this, between consecutive edge-normal directions the two extreme supporting points are fixed vertices, and width has the form \(a\cos\theta+b\sin\theta>0\). Any interior stationary point on such an interval is a local maximum (the second derivative is the negative of the positive width), so the minimum occurs at an edge normal. Evaluating the three edge orbits of this reflection-symmetric pentagon gives respectively

\[
 W_1=xz+\frac u2,\qquad
 W_2=\begin{cases}y,&x\le\tfrac12,\\2xy,&x\ge\tfrac12,\end{cases}
 \qquad W_3=z,
 \quad w(x)=\min\{W_1,W_2,W_3\}.
 \tag{2}
\]

For example, the normal to the upper-right edge may be taken as \((u,x)\); its supporting projection gap is \(xz+u/2\). The other two values are obtained from the oblique lower-right edge and the horizontal bottom edge. Formula (2) can also be checked directly by maximizing and minimizing the five scalar products for each normal.

**3. The interval \(\tfrac14\le x\le\tfrac12\).** Here \(w=y\). Indeed, \(z>y\) and

\[
 (x+\tfrac12)^2u^2-(1-x)^2y^2
 =\frac{(1-x)(2x+1)(4x-1)}2\ge0,
\]

so \((x+\tfrac12)u\ge(1-x)y\), equivalently \(W_1\ge y\). Also \(y\ge\sqrt{15}/4\) and \(z\le2\). Equation (1) therefore implies

\[
 S(x)\le6+\sqrt{17}+2\sqrt2<13,
 \qquad \frac{S(x)}{w(x)}<\frac{52}{\sqrt{15}}<14<4+6\sqrt3.
\]

The first strict comparison follows from \(\sqrt{17}+2\sqrt2<7\), whose square reduces to \(\sqrt2<10/7\); the second uses \(52^2<14^2\cdot15\).

**4. The interval \(\tfrac12\le x\le\tfrac{19}{20}\).** We prove \(w\ge1\) by checking every quantity in (2). Since \(x\ge\tfrac12\), the function \(x^2y^2=x^2(\tfrac34+x-x^2)\) is increasing, because its derivative is \(x(\tfrac32+3x-4x^2)>0\) on \([\tfrac12,1]\). Its value at \(x=\tfrac12\) is \(\tfrac14\), whence \(W_2=2xy\ge1\). Both \(y\) and \(u\) are nonincreasing here, giving

\[
 W_3=z\ge z(\tfrac{19}{20})
 =\frac{\sqrt{319}+\sqrt{39}}{20}>1.
\]

Finally \(W_1=xy+(x+\tfrac12)u\). For \(\tfrac12\le x\le\tfrac45\), use \(y>\tfrac9{10}\), \(u\ge\tfrac35\), and \(x+\tfrac12\ge1\) to obtain \(W_1>\tfrac{21}{20}\). For \(\tfrac45\le x\le\tfrac{19}{20}\), use \(y>\tfrac{17}{20}\), \(u>\tfrac3{10}\), and \(x+\tfrac12\ge\tfrac{13}{10}\) to obtain \(W_1>\tfrac{107}{100}\). Therefore \(w\ge1\).

Again \(y\le1\), \(u\le\sqrt3/2\), and \(x\le19/20\), so (1) gives

\[
 \frac{S(x)}{w(x)}\le S(x)
 \le\frac{69}{10}+2\sqrt{2+\sqrt3}
 +2\sqrt{\frac{29}{10}}
 <\frac{571}{40}<4+6\sqrt3.
\]

The penultimate inequality follows from \(\sqrt3<\tfrac74\), \(\sqrt{15}<\tfrac{31}{8}\), and \(\sqrt{29/10}<\tfrac74\); the last follows from \(\sqrt3>\tfrac{137}{80}\). Thus no maximizer lies in this interval.

**5. The interval \(\tfrac{19}{20}\le x\le1\).** In this interval \(w=z\). First \(u/(1-x)=\sqrt{(1+x)/(1-x)}\ge\sqrt{39}>4>2z\) for \(x<1\), because \(z<2\). Consequently \(W_1=xz+u/2\ge z\); the endpoint \(x=1\) follows by continuity. Secondly,

\[
 W_2-z=2xy-(y+u)=(2x-1)y-u.
\]

Here \((2x-1)y\ge\tfrac9{10}\cdot\tfrac{\sqrt3}{2}>\tfrac34\), while \(u\le\sqrt{39}/20<\tfrac13\). Thus \(W_2>z\), and (2) proves \(w=z\). The ratio becomes

\[
 F(x)=\frac{5+2x+2\sqrt{1+2x}}{z}
 +2\sqrt{1+\frac1{4z^2}}.
\]

On this interval the numerator of the first term is strictly increasing and positive, and \(z=y+u\) is strictly decreasing and positive; the second term also increases as \(z\) decreases. Hence \(F\) is strictly increasing. Its unique maximum occurs at \(x=1\), where \(u=0\), \(y=z=\sqrt3/2\), and \(S=9+2\sqrt3\). Therefore

\[
 F(1)=\frac{9+2\sqrt3}{\sqrt3/2}=4+6\sqrt3.
\]

The equality configuration is the stated marked trapezoid: its top edge consists of two unit segments meeting at the marked straight-angle vertex, its bottom edge has length \(1\), and the legs have length \(1\). The strict estimates in steps 3–4 and strict increase in step 5 prove uniqueness in the symmetric family. Taking \(x\uparrow1\) gives sharpness by strictly convex pentagons.

## Verification

The standalone `verify.py` evaluates both expressions (1)–(2) against direct five-vertex Euclidean computations on \(30{,}001\) evenly spaced parameters in \([1/4,1]\). It checks the endpoint geometry and the sharp constant, together with \(200\) exact rational instances of the identity used in step 1. Its output is `VERIFY_OK sampled_pentagons=30001 exact_rational_identities=200 sharp_ratio=14.392304845413`. These finite numerical and rational diagnostics are **not** the proof of the all-parameter inequality; steps 1–5 above are the proof. The result assumes the usual Euclidean norm, five marked vertices, nonzero area, and the reflection condition.

## Relationship to prior work

Audet and Ninin's June 8, 2010 working paper established sharp perimeter, diameter and area bounds for odd-sided equilateral unit-width convex polygons; that earlier version does not state the pairwise-distance conjecture. Their later publicly available journal-version text, Section 4, treats the sum over all vertex pairs, reports numerical branch-and-bound tests for \(n=5,7,9\), and poses a conjecture selecting the same trapezoidal extremizer for **all** odd \(n\). The present result proves that claimed extremal value and equality classification **only for reflection-symmetric equilateral pentagons**; numerical precision in the original work is not asserted to be an infinite analytic proof.

Dumitrescu, *Metric Inequalities for Polygons*, studies exact bounds on sums of intervertex distances for polygons under a **fixed perimeter** constraint, without equal-side plus minimum-width constraints. Those theorems do not imply the sharp width-normalized value here, and neither do the relevant published geometric/polygonal records inspected for other invariants.

## Limitations

The theorem does not establish the Audet–Ninin conjecture for arbitrary, asymmetric equilateral pentagons or for odd numbers of sides greater than five. It is a one-parameter symmetry-class extremal theorem. The extremizer is weakly rather than strictly convex; the strict class has only a supremum. Earlier equivalent work under other descriptions of the symmetry class remains a possible historical priority risk. No independent audit or external certification is claimed.

## References

1. C. Audet and J. Ninin, *Maximal Perimeter, Diameter and Area of Equilateral Unit-Width Convex Polygons*, dated June 8, 2010, GERAD working paper G-2010-37. Author-hosted preprint: https://www.gerad.ca/Charles.Audet/PUB/largeur_GERAD.pdf ; GERAD record: https://www.gerad.ca/en/papers/G-2010-37 .
2. C. Audet and J. Ninin, *Maximal perimeter, diameter and area of equilateral unit-width convex polygons*, *Journal of Global Optimization* **56** (2013), 1007–1016, DOI 10.1007/s10898-011-9780-4. Author-uploaded full journal-version text with Section 4 and Conjecture 9: https://www.researchgate.net/publication/241686886_Maximal_perimeter_diameter_and_area_of_equilateral_unit-width_convex_polygons .
3. A. Dumitrescu, *Metric inequalities for polygons*, *Journal of Computational Geometry* **4** (2013), 79–93. Full text: https://jocg.org/index.php/jocg/article/download/2940/2634/7316 .
