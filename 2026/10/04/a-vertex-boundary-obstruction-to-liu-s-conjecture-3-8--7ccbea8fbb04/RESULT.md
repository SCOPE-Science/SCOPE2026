# A vertex-boundary obstruction to Liu's Conjecture 3.8
## Finding
Liu's 2012 Conjecture 3.8 is false. Let \(ABC\) be a nondegenerate Euclidean triangle with \(a=BC\), \(b=CA\), and \(c=AB\). For an interior point \(P\), write \(R_1,R_2,R_3\) for the distances from \(P\) to \(A,B,C\), and \(w_1,w_2,w_3\) for the lengths of the internal angle bisectors of \(\angle BPC,\angle CPA,\angle APB\), respectively. Set
\[
\Delta(P)=R_1^2+2R_2R_3-\left[w_1^2+w_2^2+w_3^2+3(w_2w_3+w_3w_1+w_1w_2)\right].
\]
If
\[
(a-b)(a+b)^2>ac^2,
\]
then \(\Delta(P)<0\) for all interior points \(P\) sufficiently close to \(C\). Thus every triangle satisfying this strict side-length condition supplies an open boundary layer of counterexamples.

For the right triangle \(A=(0,0)\), \(B=(3,0)\), \(C=(0,4)\), one has \(a=5\), \(b=4\), \(c=3\) and the limiting defect at \(C\) is \(-16/9\). Hence Conjecture 3.8 fails already for a \(3\)-\(4\)-\(5\) triangle.

## Assumptions and scope
The triangle is nondegenerate and Euclidean. The point \(P\) is interior. The indexing is exactly that of Liu's paper: \(R_1,R_2,R_3\) are distances to \(A,B,C\), while \(w_1,w_2,w_3\) bisect \(\angle BPC,\angle CPA,\angle APB\). No statement is made about triangles that fail the displayed strict side-length condition; the result is a sufficient obstruction, not a classification of all counterexamples.

## Proof
For a triangle with two sides \(u,v\) adjacent to an angle and opposite side \(d\), the internal angle-bisector length \(\ell\) satisfies
\[
\ell^2=\frac{uv\bigl((u+v)^2-d^2\bigr)}{(u+v)^2}.
\]
Apply this to \(PBC\), \(PCA\), and \(PAB\). As \(P\) tends to \(C\) through interior points,
\[
R_1\to b,\qquad R_2\to a,\qquad R_3\to0.
\]
Consequently \(w_1\to0\) and \(w_2\to0\). The third bisector converges to the internal angle bisector from \(C\) in \(ABC\), whose squared length is
\[
w_c^2=\frac{ab\bigl((a+b)^2-c^2\bigr)}{(a+b)^2}.
\]
Therefore
\[
\lim_{P\to C}\Delta(P)=b^2-w_c^2
=\frac{b\left(ac^2-(a-b)(a+b)^2\right)}{(a+b)^2}.
\]
If \((a-b)(a+b)^2>ac^2\), this limit is strictly negative. The distance functions and the positive angle-bisector lengths are continuous on the interior and have the preceding limits at \(C\), so \(\Delta\) extends continuously there. Hence a sufficiently small interior neighborhood of \(C\) has \(\Delta(P)<0\).

For the \(3\)-\(4\)-\(5\) triangle, \(a=5\), \(b=4\), \(c=3\), and
\[
(a-b)(a+b)^2=81>45=ac^2.
\]
Moreover
\[
w_c^2=\frac{(5)(4)(81-9)}{81}=\frac{160}{9},
\qquad
\lim_{P\to C}\Delta(P)=16-\frac{160}{9}=-\frac{16}{9}.
\]
This proves the claim.

## Verification
The algebraic simplification of the boundary defect was checked from the angle-bisector formula. The bundled checker verifies the exact \(3\)-\(4\)-\(5\) arithmetic with rational numbers and, as a supplemental consistency test only, evaluates the original defect along the interior ray \(P_\varepsilon=(\varepsilon,4-2\varepsilon)\) for decreasing positive \(\varepsilon\). Those finite evaluations are not used to prove the quantified neighborhood statement; that statement follows from the exact negative boundary limit and continuity.

## Relationship to prior work
Liu's 2012 paper states Conjecture 3.8 exactly in the form refuted here and identifies \(w_1,w_2,w_3\) as the three internal angle-bisector lengths at \(P\). The same paper reports that its conjectures had been checked by computer. Liu's 2016 open-access follow-up develops new refinements involving the same \(R_i\) and \(w_i\), including the standard angle-bisector representation, but does not state a proof or disproof of the 2012 Conjecture 3.8. Liu's 2018 paper on new Erdős-Mordell refinements cites the 2012 and 2016 papers and studies other inequalities and open problems; inspection of its full text found no occurrence of the Conjecture 3.8 statement or the boundary obstruction proved here. Exact-formula and alias searches likewise found the 2012 source but no covering result.

## Limitations
The side-length inequality is sufficient, not necessary. The argument proves existence of an interior counterexample neighborhood by continuity and does not optimize its size. A differently phrased or unindexed prior counterexample could still exist; the literature checks described above did not find one.

## References
Jian Liu, "On a Geometric Inequality of Oppenheim," Journal of Science and Arts, 18(1), 5-12, 2012; published online 10 March 2012. https://www.josa.ro/docs/josa_2012_1/a_01_Liu.pdf

Jian Liu, "Refinements of the Erdös-Mordell inequality, Barrow's inequality, and Oppenheim's inequality," Journal of Inequalities and Applications 2016, Article 9. https://doi.org/10.1186/s13660-015-0947-2

Jian Liu, "New refinements of the Erdös-Mordell inequality," Journal of Mathematical Inequalities 12(1), 63-75, 2018. https://doi.org/10.7153/jmi-2018-12-05
