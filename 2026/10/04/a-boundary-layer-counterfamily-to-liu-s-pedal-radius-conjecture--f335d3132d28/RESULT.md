# A boundary-layer counterfamily to Liu's pedal-radius Conjecture 1
## Finding
Jian Liu's 2011 pedal-triangle Conjecture 1 asserts that the circumradius \(R_p\) and inradius \(r_p\) of the pedal triangle of every interior point of a triangle satisfy
\[
R_p+\sqrt{2}\,r_p<R,
\]
where \(R\) is the circumradius of the reference triangle. The conjecture is false.

Take
\[
A=(-1,0),\qquad B=(1,0),\qquad C=(0,2),
\]
and, for \(0<y<2\), let \(P_y=(0,y)\). If \(D,E,F\) are the perpendicular feet from \(P_y\) to \(BC,CA,AB\), respectively, then
\[
R_p(y)=\frac{1+y^2}{1+2y},
\]
and
\[
r_p(y)=\frac{2(2-y)\bigl(\sqrt{5(1+y^2)}-2+y\bigr)}{5(1+2y)}.
\]
The reference triangle has \(R=5/4\). At the strictly interior point \(P_{1/100}\),
\[
R_p+\sqrt2\,r_p-R
=-\frac{2749}{10200}
+\frac{199\sqrt2\,(\sqrt{50005}-199)}{25500}>0.
\]
Thus the conjectured strict inequality is reversed at an interior point. Moreover, the displayed defect is a continuous function of \(y\) and has positive boundary limit
\[
\lim_{y\downarrow0}\bigl(R_p(y)+\sqrt2\,r_p(y)-R\bigr)
=-\frac14+\frac45\bigl(\sqrt{10}-2\sqrt2\bigr)>0,
\]
so the same triangle contains an entire interval of interior counterexamples near the midpoint of \(AB\).

## Assumptions and scope
The reference triangle is the nondegenerate isosceles triangle with vertices \(A=(-1,0)\), \(B=(1,0)\), and \(C=(0,2)\). For \(0<y<2\), the point \(P_y=(0,y)\) lies strictly inside the triangle. The pedal triangle is formed by perpendicular projection to the three side lines. Its inradius and circumradius are the ordinary Euclidean radii of that nondegenerate pedal triangle.

The claim disproves only Liu's linear conjecture \(R_p+\sqrt2\,r_p<R\). It does not assess the other pedal-triangle conjectures in the source.

## Proof
For \(P_y=(0,y)\), direct orthogonal projection gives
\[
D=\left(\frac{2(2-y)}5,\frac{2(1+2y)}5\right),\qquad
E=\left(-\frac{2(2-y)}5,\frac{2(1+2y)}5\right),\qquad
F=(0,0).
\]
Hence
\[
DE=\frac{4(2-y)}5,
\qquad
FD=FE=\frac{2\sqrt{1+y^2}}{\sqrt5},
\]
and the pedal-triangle area is
\[
S_p=\frac{4(2-y)(1+2y)}{25}.
\]
Its circumradius therefore equals
\[
R_p
=\frac{DE\,DF\,EF}{4S_p}
=\frac{1+y^2}{1+2y}.
\]
Its inradius is \(r_p=2S_p/(DE+DF+EF)\). Writing \(Q=\sqrt{5(1+y^2)}\), this becomes
\[
r_p=\frac{2(2-y)(1+2y)}{5(Q+2-y)}.
\]
Because
\[
Q^2-(2-y)^2=(1+2y)^2,
\]
rationalization yields
\[
r_p=\frac{2(2-y)(Q-2+y)}{5(1+2y)}.
\]

The reference triangle has side lengths \(2,\sqrt5,\sqrt5\) and area \(2\), so
\[
R=\frac{2\cdot\sqrt5\cdot\sqrt5}{4\cdot2}=\frac54.
\]
At \(y=1/100\),
\[
R_p=\frac{10001}{10200},
\qquad
r_p=\frac{199(\sqrt{50005}-199)}{25500}.
\]
Consequently the conjectured defect in the opposite direction is
\[
E:=R_p+\sqrt2\,r_p-R
=-\frac{2749}{10200}
+\frac{199\sqrt2\,(\sqrt{50005}-199)}{25500}.
\]
After multiplication by \(51000\), the assertion \(E>0\) is equivalent to
\[
398\sqrt2\,(\sqrt{50005}-199)>13745.
\]
Now
\[
\sqrt2>\frac{140}{99}
\]
because \(140^2<2\cdot99^2\), and
\[
\sqrt{50005}>\frac{1118}{5}
\]
because \(1118^2<50005\cdot25\). Therefore
\[
398\sqrt2\,(\sqrt{50005}-199)
>
398\cdot\frac{140}{99}\cdot\frac{123}{5}
=\frac{6853560}{495}
>13745.
\]
This proves \(E>0\) exactly.

For the boundary-layer statement, the explicit formulas for \(R_p(y)\) and \(r_p(y)\) are continuous at \(y=0\), where
\[
R_p(0)=1,
\qquad
r_p(0)=\frac{4(\sqrt5-2)}5.
\]
The resulting limiting excess is positive, so continuity gives \(R_p(y)+\sqrt2\,r_p(y)>R\) for every sufficiently small \(y>0\).

## Verification
The bundled script `verify_counterexample.py` checks the projection coordinates, squared side lengths, pedal area, the exact formulas for \(R_p\) and \(r_p\), the two rational lower bounds used for the radicals, and the final strict integer comparison. It also prints a high-precision numerical value of the interior excess for \(y=1/100\). The analytic proof above, not the numerical printout, establishes the claim.

## Relationship to prior work
Liu's public 2011 RGMIA preprint states Conjecture 1 as \(R_p+\sqrt2\,r_p<R\) for every interior point. The later journal version carries the same conjecture in the pedal-triangle paper. A 2018 full-text follow-up by Fangjian Huang explicitly identifies and proves Liu's conjectures corresponding to \(PO\ge |R-2R_p|\) and the product inequality \(R_1R_2R_3/(r_1r_2r_3)\ge 8R_p^2/r^2\); it does not prove or state the present linear conjecture as resolved.

Targeted searches for the exact linear inequality, its radical coefficient, and counterexamples did not locate a prior disproof. The remaining originality risk is unindexed or differently phrased literature.

## Limitations
The result disproves the universal conjecture and supplies a one-parameter boundary layer of counterexamples in one fixed isosceles triangle. It does not classify all triangles or all interior points for which \(R_p+\sqrt2\,r_p<R\) holds, nor does it determine a best universal replacement coefficient.

## References
1. J. Liu, *On the Inequality \(R_p<R\) of the Pedal Triangle*, RGMIA Research Report Collection 14 (2011), Article 46, public preprint received 13 June 2011. https://rgmia.org/papers/v14/v14a46.pdf
2. J. Liu, *On inequality \(R_p<R\) of the pedal triangle*, Mathematical Inequalities & Applications 16(3) (2013), 701–715. doi:10.7153/mia-16-53
3. F. Huang, *Two inequalities about the pedal triangle*, Journal of Inequalities and Applications 2018, Article 72. doi:10.1186/s13660-018-1661-7
