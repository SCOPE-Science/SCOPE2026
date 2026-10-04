# Exact boundary obstruction profile for Liu's Erdős–Mordell exponent conjecture
## Finding
Liu's Conjecture 6 asks whether, for every interior point \(P\) of a Euclidean triangle and every \(0<k\le 1.73\),
\[
R_1^k+R_2^k+R_3^k\ge (r_2+r_3)^k+(r_3+r_1)^k+(r_1+r_2)^k,
\]
where \(R_i\) are the distances from \(P\) to the vertices and \(r_i\) are the perpendicular distances from \(P\) to the opposite sides. On the complete axial boundary family of isosceles triangles described below, the limiting defect has an exact one-variable minimum:
\[
m(k)=2-\left((2+2^k)^{2/(k+2)}-1\right)^{(k+2)/2}.
\]
Thus every \(k>0\) with \(m(k)<0\) produces genuine interior counterexamples arbitrarily close to the midpoint of the base. In particular, \(m(7/4)<0\) rigorously, so a universal extension of Conjecture 6 to \(k=7/4\) is impossible. A numerical solve gives a nearby zero \(k\approx1.7337000816624983\), explaining the scale of the conjectured endpoint \(1.73\), but no claim is made that this is the globally sharp exponent.

## Assumptions and scope
Let
\[
A=(-1,0),\qquad B=(1,0),\qquad C=(0,h),\qquad h>0,
\]
and take the axial interior point \(P_y=(0,y)\) with \(0<y<h\). The side opposite \(A\) is \(BC\), and cyclically. Define \(\Phi_k(h,y)\) to be the left side minus the right side in Liu's Conjecture 6. The theorem concerns the boundary limit \(y\downarrow0\) and its exact minimization over all isosceles aspect ratios \(h>0\). A strict negative boundary limit is then promoted to actual interior counterexamples by continuity.

## Proof
Direct distance calculation gives
\[
R_1=R_2=\sqrt{1+y^2},\qquad R_3=h-y,
\]
and
\[
r_1=r_2=\frac{h-y}{\sqrt{1+h^2}},\qquad r_3=y.
\]
Therefore
\[
\Phi_k(h,y)=2(1+y^2)^{k/2}+(h-y)^k
-2\left(y+\frac{h-y}{\sqrt{1+h^2}}\right)^k
-\left(\frac{2(h-y)}{\sqrt{1+h^2}}\right)^k.
\]
Letting \(y\downarrow0\) yields
\[
F_k(h)=2+h^k-(2+2^k)\left(\frac{h}{\sqrt{1+h^2}}\right)^k.
\]
Put \(t=h^2/(1+h^2)\in(0,1)\), \(p=k/2\), and \(C=2+2^k\). Then
\[
F_k=2+\left(\frac{t}{1-t}\right)^p-Ct^p,
\]
so
\[
\frac{dF_k}{dt}=p t^{p-1}\left((1-t)^{-p-1}-C\right).
\]
The bracket is strictly increasing from \(1-C<0\) to \(+\infty\), hence there is a unique critical point and it is the global minimum. It satisfies
\[
1-t_*=C^{-1/(p+1)}=C^{-2/(k+2)},
\]
equivalently
\[
h_*^2=C^{2/(k+2)}-1.
\]
Substitution gives
\[
m(k)=F_k(h_*)=2-\left(C^{2/(k+2)}-1\right)^{(k+2)/2}.
\]
If \(m(k)<0\), then \(\Phi_k(h_*,y)\to m(k)<0\) as \(y\downarrow0\), so continuity provides an \(\varepsilon>0\) for which every \(0<y<\varepsilon\) is an interior counterexample.

For the exact certificate at \(k=7/4\), write \(x=2^{1/60}\). The inequality \(m(7/4)<0\) is equivalent to
\[
(2+x^{105})^8>(1+x^{32})^{15}.
\]
Reducing the difference modulo \(x^{60}-2\) gives an explicit degree-\(56\) integer polynomial. The bundled verifier proves \(1011/1000<x<253/250\) and evaluates that reduced polynomial by exact rational interval Horner arithmetic, obtaining a strictly positive interval. Hence \(m(7/4)<0\) without relying on floating-point arithmetic.

## Verification
Running `python verify_boundary.py` reconstructs the reduced polynomial directly from the two binomial expansions, checks its reduction under \(x^{60}=2\), proves the rational enclosure for \(x=2^{1/60}\), and certifies positivity of the polynomial throughout that enclosure. It also reports the numerical values of \(m(1.73)\), \(m(1.7337)\), \(m(1.734)\), and the nearby numerical zero only as diagnostics. The analytic minimization above is independent of those numerical diagnostics.

## Relationship to prior work
Liu's source states Conjecture 6 with the range \(0<k\le1.73\) and notes that \(k=1\) recovers the Erdős–Mordell inequality. The source does not provide a sharpness mechanism for the decimal endpoint. The exact boundary profile above isolates a natural obstruction already inside the simplest symmetric triangle family and shows that failure is forced by an open interior boundary layer whenever \(m(k)<0\).

A later paper by Liu on refinements of the Erdős–Mordell and Barrow inequalities was inspected because it is a natural follow-up in the same line of work. It develops different refinements and conjectures; targeted searches of that text for the exponent \(1.73\) and the powered-distance form did not produce this boundary minimization or a covering theorem. published-finding corpus searches for the exact powered inequality, exponent endpoint, and isosceles boundary formulation likewise returned no covering result.

## Limitations
This result does not prove Liu's conjecture at \(k=1.73\), and it does not determine the globally sharp exponent over all triangles and all interior points. The exact function \(m(k)\) is the optimum only for this isosceles boundary family. Positivity of \(m(k)\) at a given exponent therefore gives no global validity result. The quoted zero near \(1.7337000816624983\) is a numerical localization, not a certified uniqueness or global-threshold theorem. Unindexed or differently phrased prior literature remains an originality risk.

## References
1. Jian Liu, “A New Proof of the Erdös-Mordell Inequality,” RGMIA Research Report Collection 14 (2011), Article 12, source PDF carrying a received stamp of 2 February 2011 and primary classification 51M16. https://rgmia.org/papers/v14/v14a12.pdf
2. Jian Liu, “A New Proof of the Erdös-Mordell Inequality,” International Electronic Journal of Geometry 4(2) (2011), 114–119. https://dergipark.org.tr/en/pub/iejg/article/599495
3. Jian Liu, “New Refinements of the Erdös–Mordell Inequality and Barrow’s Inequality,” Mathematics 7 (2019), 726. https://doi.org/10.3390/math7080726
