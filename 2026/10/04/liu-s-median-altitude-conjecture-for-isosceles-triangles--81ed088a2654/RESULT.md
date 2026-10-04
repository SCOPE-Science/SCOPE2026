# Liu's median-altitude conjecture for isosceles triangles
## Finding
For every nondegenerate Euclidean isosceles triangle \(ABC\), if \(m_a,m_b,m_c\) are the medians, \(h_a,h_b,h_c\) the altitudes, \(s\) the semiperimeter, and \(r\) the inradius, then \[m_a+m_b+m_c-(h_a+h_b+h_c)\ge s-3\sqrt{3}\,r.\] Equality holds if and only if the triangle is equilateral. Thus Liu's 2012 Conjecture 4 holds on the full isosceles subclass.

The statement is the isosceles specialization of Conjecture 4 in Jian Liu's 2012 paper. The source asks for the same inequality for every Euclidean triangle.

## Assumptions and scope
By similarity, write the equal sides as \(b=c=1\) and the base as \(a=x\), where \(0<x<2\). Put \(q=\sqrt{4-x^2}\). Then
\[
 m_a=\frac q2,\qquad m_b=m_c=\frac12\sqrt{1+2x^2},
\]
\[
 h_a=\frac q2,\qquad h_b=h_c=\frac{xq}{2},\qquad
 s=1+\frac x2,\qquad r=\frac{xq}{2(x+2)}.
\]
The result concerns all nondegenerate isosceles triangles; the degenerate limits \(x=0\) and \(x=2\) are not included.

## Proof
Substitution reduces the desired inequality to \(G(x)\ge0\), where
\[
G(x)=\sqrt{1+2x^2}-1-\frac x2-xq+\frac{3\sqrt3\,xq}{2(x+2)}.
\]
Rationalizing the first three terms gives
\[
\frac{G(x)}x=\frac{7x-4}{4D}-\frac{(2x+4-3\sqrt3)q}{2(x+2)},
\qquad
D=\sqrt{1+2x^2}+1+\frac x2.
\]
Set
\[
\alpha=\frac47,\qquad \beta=\frac{3\sqrt3-4}2.
\]
One has \(0<\alpha<\beta<2\). On \([\alpha,\beta]\), the first numerator is nonnegative and the second is nonpositive, so the inequality is immediate.

It remains to treat the two outer intervals. Let
\[
A=7x-4,\qquad B=2x+4-3\sqrt3,\qquad t=\sqrt{1+2x^2},
\]
and define
\[
U=A^2(x+2)^2-4B^2(4-x^2)\left(2+x+\frac94x^2\right),
\]
\[
V=4B^2(4-x^2)(x+2).
\]
After the first sign-preserving squaring, the comparison is governed by \(S=U-Vt\). A direct exact expansion gives
\[
U^2-V^2(1+2x^2)=784(x-1)^2\left(x-\frac47\right)^2(x+2)^2Q(x),
\]
where
\[
\begin{aligned}
Q(x)={}&x^6+(6-6\sqrt3)x^5+(52-24\sqrt3)x^4+(86-48\sqrt3)x^3\\
&+(-129+72\sqrt3)x^2+(-496+288\sqrt3)x-168+96\sqrt3.
\end{aligned}
\]

For \(0<x<\alpha\), both \(A\) and \(B\) are negative. Hence the original inequality is equivalent to \(S\le0\). The polynomial \(Q\) is strictly increasing on \([0,\alpha]\): the degree-five Bernstein coefficients of \(Q'(\alpha u)\), for \(0\le u\le1\), are
\[
\begin{gathered}
-496+288\sqrt3,\quad -\frac{18392}{35}+\frac{10656}{35}\sqrt3,\quad
-\frac{133904}{245}+\frac{77472}{245}\sqrt3,\\
-\frac{952344}{1715}+\frac{551328}{1715}\sqrt3,\quad
-\frac{1313904}{2401}+\frac{3815328}{12005}\sqrt3,\quad
-\frac{8686008}{16807}+\frac{725472}{2401}\sqrt3,
\end{gathered}
\]
and each is positive. Moreover
\[
Q(\alpha)=-\frac{55478520}{117649}+\frac{4574880}{16807}\sqrt3<0.
\]
Thus \(Q(x)<0\) on this interval, so \(U^2-V^2t^2<0\), which forces \(S<0\).

For \(x\ge\beta\), write \(x=\beta+y\), \(y\ge0\). The expansion of \(U(\beta+y)\) has all seven coefficients positive. For \(Q(\beta+y)\), the coefficients through degree three are positive, while the top three terms are
\[
y^4\left(y^2+(-6+3\sqrt3)y+\frac{73}4-9\sqrt3\right).
\]
The quadratic in parentheses has discriminant \(-10\), so it is positive. Hence \(Q(x)>0\) for \(x\ge\beta\). The positive-coefficient expansion also gives \(U>0\), and therefore \(S\ge0\), with equality only when \(x=1\). This proves the inequality on the final interval.

At \(x=1\) the triangle is equilateral and direct substitution gives equality. All other points in \(0<x<2\) are strict.

## Verification
The accompanying `verify.py` uses only Python's standard library and exact rational arithmetic in \(\mathbb Q(\sqrt3)\). It reconstructs \(U\), \(V\), and \(Q\), verifies the displayed factorization coefficient-by-coefficient, checks all Bernstein-sign certificates, verifies the shifted positive-coefficient certificates at \(\beta\), and checks the equality case exactly. Running `python3 verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Liu's 2012 article states Conjecture 4 for all triangles and gives the exact lower bound \(m_a+m_b+m_c-(h_a+h_b+h_c)\ge s-3\sqrt3\,r\). It does not provide the isosceles proof above. A later full-text paper by Liu from 2021 proves a different double inequality involving medians, angle bisectors, and exradii; its statement and proof do not contain this median-minus-altitude lower bound or an isosceles resolution. The 2017 American Mathematical Monthly problem “Sum of Medians of a Triangle” proves an upper bound for \(m_a+m_b+m_c\) alone and likewise does not imply the present difference inequality.

The closest checked later statement is Liu's 2023 Lemma 2, which gives a pointwise lower bound for each difference \(m_a-h_a\). Its summed consequence does not cover the present theorem. For the isosceles triangle with \(a=1/2\) and \(b=c=1\), summing that lemma gives only
\[
\frac{29}{32\sqrt{15}}=\frac{29\sqrt{15}}{480},
\]
whereas the right side required by Conjecture 4 is
\[
s-3\sqrt3\,r=\frac{25-9\sqrt5}{20}.
\]
Their difference is
\[
\frac{25-9\sqrt5}{20}-\frac{29\sqrt{15}}{480}>0.
\]
Thus the published 2023 lower bound is strictly insufficient even on this single isosceles member and cannot imply the full isosceles result.

## Limitations
The proof establishes Liu's conjecture only for the full isosceles subclass. It does not prove the conjecture for scalene triangles. Literature searching cannot exclude an unindexed or differently phrased earlier proof, so originality is limited to the checked sources and searches listed in the review materials.

## References
1. J. Liu, “On an inequality for the medians of a triangle,” *Journal of Science and Arts* 12(2)(19) (2012), 127–136. Published online 2012-06-15. Conjecture 4 is equation (4.7). https://josa.ro/docs/josa_2012_2/a_03_Liu_J.pdf
2. J. Liu, “Proof of a double inequality in triangles,” *Journal of Mathematical Inequalities* 15(4) (2021), 1361–1374. DOI: 10.7153/jmi-2021-15-92.
3. A. Alt and K. Knop, “Sum of Medians of a Triangle,” Problem 11790, solution by J. C. Smith, *American Mathematical Monthly* 124(2) (2017), 185. Stable item: 10.4169/amer.math.monthly.124.2.179.
4. J. Liu, “Two inequalities involving circumradius, inradius and medians of an acute triangle,” *Advances in Inequalities and Applications* 2023 (2023), Article 12. DOI: 10.28919/aia/8232.
