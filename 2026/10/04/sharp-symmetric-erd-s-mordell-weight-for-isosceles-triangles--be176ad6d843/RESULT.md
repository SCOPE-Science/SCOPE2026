# Sharp symmetric Erdős–Mordell weight for isosceles triangles
## Finding
Let \(ABC\) be an isosceles triangle normalized by \(A=(-1,0)\), \(B=(1,0)\), and \(C=(0,h)\), where \(h>0\). For an interior point \(P\), let \(r_a,r_b,r_c\) be its distances to \(BC,CA,AB\). The largest coefficient \(\Lambda(h)\) for which
\[
PA+PB+PC\ge \Lambda(h)(r_a+r_b)+2r_c
\]
holds for every interior \(P\) is
\[
\Lambda(h)=\begin{cases}
\dfrac{\sqrt{1+h^2}(h+2)}{2h},&0<h\le1,\\[4pt]
\dfrac{h^2+5}{2\sqrt{1+h^2}},&h\ge1.
\end{cases}
\]
For \(0<h\le1\) the sharp constant is approached at the base midpoint from the interior; for \(h>1\) equality occurs uniquely at \(P=(0,(h^2-1)/(2h))\). Consequently Jian Liu's 2015 Conjecture 2,
\[
R_1+R_2+R_3\ge2\left(\frac{m_a}{w_a}r_1+\frac{m_b}{w_b}r_2+\frac{m_c}{w_c}r_3\right),
\]
holds for every isosceles triangle and every interior point, with equality only for an equilateral triangle at its center.

The transition at \(h=1\) is exact: below it the extremal configuration escapes to the boundary, while above it the extremizer is an interior point on the symmetry axis.

## Assumptions and scope
The normalization fixes the base length at \(2\); this loses no generality because all quantities in the inequality are homogeneous of degree one. Put \(s=\sqrt{1+h^2}\), the common length of the two equal sides. For \(P=(x,y)\) in the interior, \(0<y<h\) and \(|x|<1-y/h\). The side distances satisfy
\[
r_a+r_b=\frac{2(h-y)}s,\qquad r_c=y.
\]
The sharp coefficient theorem concerns precisely the symmetric two-weight family \(\lambda(r_a+r_b)+2r_c\). The stated corollary concerns Liu's Conjecture 2 from 2015.

## Proof
For fixed \(y\), define
\[
S_y(x)=\sqrt{(x+1)^2+y^2}+\sqrt{(x-1)^2+y^2}+\sqrt{x^2+(h-y)^2}.
\]
Because \(0<y<h\), this function is even and strictly convex, so its unique minimum occurs at \(x=0\). Therefore
\[
PA+PB+PC\ge \lambda(r_a+r_b)+2r_c
\]
for every interior point if and only if its restriction to the symmetry axis holds for all \(0<y<h\). There it becomes
\[
2\sqrt{1+y^2}+h-y\ge \frac{2\lambda}s(h-y)+2y.
\]
Writing \(K=2\lambda/s\), this is equivalent to
\[
K\le B_h(y):=\frac{2\sqrt{1+y^2}+h-3y}{h-y}.
\]
A direct differentiation gives
\[
B_h'(y)=\frac{2\left(1-h(\sqrt{1+y^2}-y)\right)}{\sqrt{1+y^2}(h-y)^2}.
\]
Since \(\sqrt{1+y^2}-y=1/(\sqrt{1+y^2}+y)\), the minimum is at the boundary value \(y=0\) when \(0<h\le1\), giving \(K_*=1+2/h\). When \(h>1\), there is exactly one critical point, characterized by \(\sqrt{1+y^2}+y=h\), namely
\[
y_* = \frac{h^2-1}{2h},
\]
and it is the unique minimum; substitution gives
\[
K_*=\frac{h^2+5}{h^2+1}.
\]
Multiplying by \(s/2\) yields the stated piecewise \(\Lambda(h)\). Strict convexity in \(x\) supplies the equality classification. For \(0<h\le1\), the minimum over the open interval \(0<y<h\) is the limit at \(y=0\), so the constant is sharp but is not attained by an interior point.

It remains to compare Liu's coefficient. In the present isosceles triangle,
\[
m_a=m_b=\frac12\sqrt{s^2+8},\qquad
w_a=w_b=\frac{\sqrt{8s(s+1)}}{s+2},\qquad
m_c=w_c=h.
\]
Hence Liu's right-hand side is \(\lambda_L(r_a+r_b)+2r_c\), where
\[
\lambda_L=\frac{(s+2)\sqrt{s^2+8}}{\sqrt{8s(s+1)}}.
\]
Set \(H(s)=(s^2+4)/(2s)\). Squaring positive quantities and simplifying gives the exact factorization
\[
H(s)^2-\lambda_L^2=
\frac{(s-2)^2(s^3+2s^2+8s+8)}{8s^2(s+1)}\ge0.
\]
For \(h\ge1\), \(\Lambda(h)=H(s)\). For \(0<h\le1\),
\[
\Lambda(h)-H(s)=\frac{(h-1)^2}{hs}\ge0.
\]
Thus \(\lambda_L\le\Lambda(h)\) for every \(h>0\), proving Liu's Conjecture 2 on the entire isosceles class. Equality in this corollary requires \(s=2\), hence \(h=\sqrt3\), and then the sharp equality point is the common center of the equilateral triangle.

## Verification
The bundled `verify.py` checks the polynomial factorization with exact integer arithmetic, checks the two closed-form comparisons over deterministic parameter grids, and performs deterministic randomized coordinate tests of both the sharp inequality and Liu's specialized inequality. These computations are supplementary; the quantified theorem is established by the convexity and one-variable derivative argument above.

## Relationship to prior work
Liu's 2015 paper states the median-to-angle-bisector inequality above as Conjecture 2 and explicitly presents it as an open problem. Liu's 2016 refinement involving medians has a different weighted form: it weights \(r_i+R_i\) by linear combinations of the three medians and contains no ratio \(m_i/w_i\). Later weighted Erdős–Mordell papers found in the literature use other weighting schemes; exact searches for the ratio formulation and for an isosceles solution did not locate this sharp two-weight classification.

The present result is stronger than merely verifying the 2015 conjecture on isosceles triangles: it identifies the exact largest symmetric coefficient and all extremal behavior in that subclass.

## Limitations
No claim is made here for scalene triangles, so Liu's full 2015 Conjecture 2 remains unresolved by this result. Full text of the closely related 2018 paper *Two New Weighted Erdős–Mordell Type Inequalities* and of Tran's 2021 weighted-family paper was not available through the sources inspected here; their abstracts and accessible previews do not state the present isosceles sharp coefficient, but they remain residual literature risks. Numerical tests are not used as proof.

## References
1. J. Liu, “Sharpened versions of the Erdös-Mordell inequality,” *Journal of Inequalities and Applications* 2015, 206 (2015), doi:10.1186/s13660-015-0716-2. Published 19 June 2015.
2. J. Liu, “Refinements of the Erdös-Mordell inequality, Barrow’s inequality, and Oppenheim’s inequality,” *Journal of Inequalities and Applications* 2016, 9 (2016), doi:10.1186/s13660-015-0947-2.
3. J. Liu, “Two New Weighted Erdős–Mordell Type Inequalities,” *Discrete & Computational Geometry* 59, 707–724 (2018), doi:10.1007/s00454-017-9917-4.
4. J. Liu, “New Refinements of the Erdös–Mordell Inequality and Barrow’s Inequality,” *Mathematics* 7, 726 (2019), doi:10.3390/math7080726.
5. Q. H. Tran, “A family of weighted Erdös–Mordell inequality and applications,” *Journal of Geometry* 112, 33 (2021), doi:10.1007/s00022-021-00597-0.
