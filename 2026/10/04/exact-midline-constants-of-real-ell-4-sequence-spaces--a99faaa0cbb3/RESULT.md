# Exact midline constants of real \(\ell_4\) sequence spaces
## Finding
Let \(I\) be any index set with at least two elements and let \(X=\ell_4(I)\) over the real scalars. For the constants introduced by Chen, Yang, Liu and Li,
\[
M_1(X)=\sup_{\|x\|=\|y\|=\|x-y\|=1}\frac{\|x+y\|+\|2x-y\|}2
\]
and
\[
M_2(X)=\sup_{\|x\|=\|y\|=\|x-y\|=1}\frac{\|x+y\|^2+\|2x-y\|^2}2,
\]
one has the exact values
\[
M_1(X)=(6\sqrt6-3)^{1/4},\qquad M_2(X)=(6\sqrt6-3)^{1/2}.
\]
Numerically these are \(M_1(X)\approx1.8493454844440614\) and \(M_2(X)\approx3.4200787208336402\).

## Assumptions and scope
The scalars are real, the norm is the standard \(\ell_4\) norm, and \(I\) has at least two coordinates. No finite-dimensionality assumption is used in the upper bound. The displayed values are for the two constants \(M_1\) and \(M_2\) as defined above; no claim is made for their generalized or subduplicate variants.

## Proof
Fix an admissible pair \(x,y\), and put \(v=y\), \(w=x-y\), and \(u=x=v+w\). Thus
\[
\|u\|_4=\|v\|_4=\|w\|_4=1.
\]
Write
\[
A=\|u+v\|_4=\|x+y\|_4,\qquad B=\|u+w\|_4=\|2x-y\|_4,
\]
and define
\[
R=\sum_i v_i^2w_i^2,\qquad T=\sum_i v_iw_i(v_i^2+w_i^2).
\]
All sums below converge absolutely by Cauchy--Schwarz because \(v^2,w^2\in\ell_2(I)\).

Expanding \(\|v+w\|_4^4=1\) gives
\[
1=2+4T+6R,
\]
so
\[
T=-\frac{1+6R}4.
\]
Cauchy--Schwarz gives
\[
T^2\le R\sum_i(v_i^2+w_i^2)^2=R(2+2R).
\]
Consequently
\[
(1+6R)^2\le32R(1+R),
\]
or equivalently
\[
4R^2-20R+1\le0.
\]
Hence
\[
R\ge R_0:=\frac52-\sqrt6.
\]

For real scalars the coordinate identity
\[
(a+b)^4+(a-b)^4=2a^4+12a^2b^2+2b^4
\]
implies
\[
A^4=3+12\sum_i u_i^2v_i^2,\qquad B^4=3+12\sum_i u_i^2w_i^2.
\]
Since \(u=v+w\),
\[
\sum_i u_i^2(v_i^2+w_i^2)=2+2R+2T=\frac32-R.
\]
Therefore
\[
A^4+B^4=24-12R\le24-12R_0=2(6\sqrt6-3).
\]
The power-mean inequality now yields
\[
\frac{A+B}2\le\left(\frac{A^4+B^4}2\right)^{1/4}\le(6\sqrt6-3)^{1/4},
\]
and Cauchy--Schwarz applied to \(A^2,B^2\) yields
\[
\frac{A^2+B^2}2\le\left(\frac{A^4+B^4}2\right)^{1/2}\le(6\sqrt6-3)^{1/2}.
\]
These are the desired upper bounds.

It remains to attain both bounds. Choose two coordinates and set
\[
a=2^{-1/4},\qquad P=\frac{\sqrt3-\sqrt2}2,
\]
\[
c=\sqrt{a^2+4P},\qquad r=\frac{c-a}2,\qquad d=\frac{c+a}2.
\]
Then \(d-r=a\), \(rd=P\), and a direct radical simplification gives
\[
r^4+d^4=1,\qquad 2r^2d^2=\frac52-\sqrt6=R_0.
\]
Take
\[
y=(-r,d,0,\ldots),\qquad x=(a,a,0,\ldots).
\]
Because \(d=a+r\), one has
\[
x-y=(d,-r,0,\ldots),
\]
so \(x,y,x-y\) are all unit vectors. Moreover, \(x+y\) and \(2x-y\) are obtained from one another by swapping the first two coordinates; hence \(A=B\). For this pair \(R=R_0\), so the identity above forces
\[
A^4=B^4=6\sqrt6-3.
\]
Thus equality holds simultaneously in the two upper bounds, proving both formulas.

## Verification
The proof is exact and does not depend on finite sampling. The accompanying script `artifacts/verify.py` reconstructs the explicit two-coordinate witness at high precision, checks the three unit-norm constraints, the value \(R=5/2-\sqrt6\), equality of the two midline lengths, and the two stated constants. Its numerical checks are corroborative; the infinite-dimensional upper bound is the analytic argument above.

## Relationship to prior work
Chen, Yang, Liu and Li introduced \(M_1\) and \(M_2\) in 2022, proved general bounds and geometric consequences, computed the Hilbert-space value of \(M_1\), and gave special examples for a different norm. Their paper motivates further study of these constants and does not state the exact \(\ell_4\) values above. Targeted searches for \(M_1(\ell_4)\), \(M_2(\ell_4)\), midline constants on \(\ell_4\), and the radical \(6\sqrt6-3\) did not locate a covering statement. A published result about equilateral perimeters in regular polygonal norms studies a different invariant and neither implies nor contains these formulas.

## Limitations
The proof exploits the exact quartic expansion, so it does not by itself give the corresponding constants for \(\ell_p\) when \(p\ne4\). The literature search cannot exclude every unindexed or differently phrased source; the originality assessment is therefore limited to the inspected primary article and the targeted literature searches described in the review materials.

## References
1. B. Chen, Z. Yang, Q. Liu, Y. Li, *Some Geometric Constants Related to the Midline of Equilateral Triangles in Banach Spaces*, Symmetry 14 (2022), 348. DOI 10.3390/sym14020348. Published 9 February 2022.
