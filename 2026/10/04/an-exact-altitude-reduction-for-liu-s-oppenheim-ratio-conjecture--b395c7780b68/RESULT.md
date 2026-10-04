# An exact altitude reduction for Liu's Oppenheim-ratio conjecture on isosceles triangles

## Finding
For every nondegenerate Euclidean isosceles triangle \(ABC\) with \(AB=AC\), and every interior point \(P\), set \(R_1=PA\), \(R_2=PB\), \(R_3=PC\), and let \(r_1,r_2,r_3\) be the distances from \(P\) to \(BC,CA,AB\), respectively. Then
\[
\frac{R_2+R_3}{r_2+r_3}-\frac{2r_1}{R_1}\ge 1.
\]
Thus Liu's Conjecture 3.12 is valid for the full isosceles subclass singled out by its conjectured equality condition.

More precisely, after a similarity put \(A=(0,h)\), \(B=(-1,0)\), \(C=(1,0)\), with \(h>0\), and write \(P=(x,y)\). Every interior point satisfies \(0<y<h\) and \(|x|<(h-y)/h\). Then
\[
\frac{R_2+R_3}{r_2+r_3}-\frac{2r_1}{R_1}-1
\ge
\frac{(hy-1)^2}{(h-y)(\sqrt{1+h^2}\sqrt{1+y^2}+h+y)}.
\]
Equality in this stronger lower bound occurs exactly on the symmetry altitude \(x=0\). Equality in Liu's original inequality occurs exactly when \(h>1\), \(x=0\), and \(y=1/h\). In invariant terms, \(h>1\) is \(\angle A<\pi/2\), and the equality point has distance \((BC)^2/(4h_a)\) from \(BC\).

## Assumptions and scope
The triangle is nondegenerate, \(AB=AC\), and \(P\) is strictly interior. The notation follows Liu: \(R_i\) are point-to-vertex distances and \(r_i\) are point-to-opposite-side distances. The theorem proves only the isosceles subclass of the all-triangle conjecture; no assertion is made for scalene triangles.

## Proof
Let \(t=h-y>0\) and \(s=\sqrt{1+h^2}\). Directly from the two equal side equations,
\[
r_2+r_3=\frac{2t}{s},\qquad R_1=\sqrt{x^2+t^2},
\]
and
\[
R_2=\sqrt{(x+1)^2+y^2},\qquad R_3=\sqrt{(x-1)^2+y^2}.
\]
For fixed \(y\), the function \(R_2+R_3\) is even and strictly convex in \(x\), because
\[
\frac{d^2}{dx^2}(R_2+R_3)
=\frac{y^2}{R_2^3}+\frac{y^2}{R_3^3}>0.
\]
Hence it is strictly increasing for \(x>0\). Also \(-2y/\sqrt{x^2+t^2}\) is even and strictly increasing for \(x>0\). Therefore the full defect
\[
F(x,y)=\frac{R_2+R_3}{r_2+r_3}-\frac{2r_1}{R_1}-1
\]
is minimized, for each fixed \(y\), uniquely at \(x=0\).

At \(x=0\), \(R_2=R_3=\sqrt{1+y^2}\) and \(R_1=t\), so
\[
F(0,y)=\frac{s\sqrt{1+y^2}-h-y}{h-y}.
\]
Rationalizing the numerator gives the exact identity
\[
s\sqrt{1+y^2}-h-y
=\frac{(hy-1)^2}{s\sqrt{1+y^2}+h+y},
\]
because
\[
(1+h^2)(1+y^2)-(h+y)^2=(hy-1)^2.
\]
This proves the stated quantitative lower bound and the conjectured inequality.

For equality in Liu's inequality, strict horizontal minimization forces \(x=0\), while the rationalized defect vanishes exactly when \(hy=1\). Such a point is interior exactly when \(1/h<h\), i.e. \(h>1\). Undoing the normalization, if the half-base is \(q=BC/2\) and the altitude is \(h_a\), then the equality height above \(BC\) is \(q^2/h_a=(BC)^2/(4h_a)\). The condition \(h_a>q\) is equivalent to \(\angle A<\pi/2\).

## Verification
The argument is analytic and does not rely on finite enumeration. The bundled `verify.py` checks the algebraic rationalization identity exactly at the coefficient level and performs deterministic numerical stress tests over a broad range of isosceles aspect ratios and interior points. These numerical tests are supplementary; the proof above supplies the universal quantifiers.

## Relationship to prior work
Liu's 2012 paper states Conjecture 3.12 in exactly the ratio form proved here and explicitly predicts that equality should require \(b=c\) and a fixed point on the altitude from \(A\), while saying that the fixed point was unknown. The present theorem proves the whole \(b=c\) subclass and identifies that point when it lies in the interior. Liu's 2016 paper develops different refinements of Oppenheim's and Erdős--Mordell inequalities, but its stated theorems and open problems do not give this ratio inequality or the isosceles equality location.

Targeted searches for the exact ratio, the phrase describing the unknown altitude point, and equivalent isosceles formulations did not locate a published result covering this theorem. The closest indexed results found in the comparison search concern different triangle-shape or Oppenheim/Erdős--Mordell refinements and do not imply the claim.

## Limitations
The result does not settle Conjecture 3.12 for scalene triangles. The originality comparison is limited by indexing and terminology: an older or unindexed solution of this isosceles case could exist. The numerical checks in `verify.py` are not used as proof.

## References
1. J. Liu, “On a geometric inequality of Oppenheim,” *Journal of Science and Arts* 18(1), 5--12 (2012). Published online 10 March 2012. Public full text: https://www.josa.ro/docs/josa_2012_1/a_01_Liu.pdf
2. J. Liu, “Refinements of the Erdös-Mordell inequality, Barrow’s inequality, and Oppenheim’s inequality,” *Journal of Inequalities and Applications* 2016, Article 9 (2016), DOI 10.1186/s13660-015-0947-2.
