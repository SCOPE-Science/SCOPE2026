# A disconnected sharp termwise Erdős–Mordell regime for isosceles triangles

## Finding
Let \(A=(0,h)\), \(B=(1,0)\), \(C=(-1,0)\), with \(h>0\). For every \(P\) in the closed triangle, let \(R_i=|Pi|\) and let \(r_i\) be the perpendicular distance to the **supporting line** of the side opposite vertex \(i\). The following termwise inequality is indexed by each vertex \(i\), with \(i\) any one of \(A,B,C\), and \(j,k\) the other two:
\[
R_j+R_k\ge 2r_i+r_j+r_k.\tag{1}
\]
All three inequalities (1) hold for every \(P\) if and only if
\[
\boxed{0<h\le 1/\sqrt3\quad\text{or}\quad h=\sqrt3.}\tag{2}
\]
Equivalently the apex angle is at least \(120^\circ\), or is exactly \(60^\circ\). The flat branch includes its endpoint; the equilateral case is isolated from the flat branch. At \(h=1/\sqrt3\), (1) is sharp at the two trisection points of the base (for the relevant base vertices); for \(h=\sqrt3\), all three inequalities are sharp at the centroid.

Writing \(S=r_A+r_B+r_C\), the three inequalities imply the cyclic inequality
\[
\sum_{\{i,j,k\}=\{A,B,C\}}\frac{(S+r_i)^2}{R_j+R_k}\le\sum_i(S+r_i)=4S,\tag{3}
\]
where the summation is over the three distinct choices of \(i\), and \(j,k\) are its complementary pair. Equation (3) is Liu's 2015 Conjecture 1 on the shape families in (2). Failure of (1) outside these families is **not** a counterexample to (3).

## Assumptions and scope
All lengths are Euclidean. The normalization makes the base length \(2\), so \(h\) is the altitude divided by half the base; similarity does not affect the inequalities. The point \(P\) may be on the boundary for the classification. Failure found on a boundary persists for some strictly interior points by continuity. The source conjecture is stated for interior points; its consequence above is limited to the families in (2).

## Proof
Put \(L=\sqrt{1+h^2}\) and \(P=(x,y)\), where \(0\le y\le h\) and \(|x|\le1-y/h\). Direct distances to the three supporting lines give
\[
r_A=y,\qquad r_B=\frac{h+hx-y}{L},\qquad r_C=\frac{h-hx-y}{L}.\tag{4}
\]

**1. Apex inequality.** The two base-vertex distances, at fixed \(y\), sum to at least \(2\sqrt{1+y^2}\), with equality at \(x=0\) (symmetry and convexity). By (4), their required right-hand side is \(2y+2(h-y)/L\). Thus the apex inequality holds for all points precisely when
\[
F(y):=\sqrt{1+y^2}-\Big(1-\frac1L\Big)y-\frac hL\ge0\qquad(0\le y\le h).\tag{5}
\]
The global minimum of \(F\) over all real \(y\) is
\[
\min_{y\in\mathbb R} F(y)=\frac{\sqrt{2L-1}-h}{L},\qquad y_* =\frac{L-1}{\sqrt{2L-1}}.\tag{6}
\]
For \(L>1\), one has \(0<y_*<h\), by direct squaring. Therefore (5) holds if and only if \(2L-1\ge h^2=L^2-1\), or \(L\le2\), equivalently \(h\le\sqrt3\). If \(h>\sqrt3\), the interior point \((0,y_*)\) makes the apex inequality strictly false. At \(h=\sqrt3\), it is sharp only when \((x,y)=(0,h/3)\).

**2. Base-vertex inequality in the flat branch.** By symmetry it suffices to treat vertex \(B\). Its deficit is the convex function
\[
G_h(x,y)=\sqrt{x^2+(y-h)^2}+\sqrt{(x+1)^2+y^2}
-y-\frac{3(h-y)+hx}{L}.\tag{7}
\]
Define \(t=h/L\in(0,1)\) and
\[
x_*=-\frac{h(1-t)}{\sqrt{t(2-t)}}=-\sqrt{\frac{t(1-t)}{(1+t)(2-t)}}.\tag{8}
\]
As \(4t(1-t)\le1\), we have \(-1/3\le x_*<0\). On the line \(y=0\), \(\partial_xG_h(x_*,0)=0\), and
\[
G_h(x_*,0)=1-3t+\frac{t\sqrt{t(2-t)}}{\sqrt{1-t^2}},\tag{9}
\]
while the inward derivative is
\[
\partial_yG_h(x_*,0)=3\sqrt{1-t^2}-1-\sqrt{t(2-t)}.\tag{10}
\]
For \(t\le1/2\), expression (10) is at least \(3\sqrt3/2-2>0\). Hence the supporting-plane inequality for the convex function \(G_h\) shows that \(G_h(x,y)\ge G_h(x_*,0)\) for every \(y\ge0\).

The value (9) is nonnegative for \(0<t\le1/2\): for \(t\le1/3\) this is immediate. For \(1/3<t\le1/2\), compare the positive radicals by squaring and use the identity
\[
(1-t^2)(3t-1)^2-t^3(2-t)=-(2t-1)(4t^3-4t+1).\tag{11}
\]
Both factors on the right after the leading minus sign are negative, because \(4t^3-4t+1\) decreases from \(-5/27\) on \([1/3,1/2]\). Therefore the radical in (9) is at least \(3t-1\). Thus the base inequality holds for all \(P\) whenever \(t\le1/2\), i.e. \(h\le1/\sqrt3\); symmetry proves the third inequality. At the endpoint \(t=1/2\), the minimizing boundary point is \((-1/3,0)\), and its reflected analogue is \((1/3,0)\).

**3. Exclusion of all intervening heights.** If \(1/\sqrt3<h\le1\), then \(1/2<t\le1/\sqrt2\). The cubic \(4t^3-4t+1\) is strictly convex on this interval and is negative at both endpoints (values \(-1/2\) and \(1-\sqrt2\)); hence it remains negative. Identity (11), now with \(2t-1>0\), gives that (9) is strictly negative. Thus the base point \((x_*,0)\) violates the \(B\)-inequality; nearby strictly interior points do likewise.

For \(1\le h<\sqrt3\), take the interior centroid \(P=(0,h/3)\). Its \(B\)-deficit equals
\[
G_h(0,h/3)=\sqrt{1+h^2/9}+h/3-2h/L.\tag{12}
\]
Here \(\sqrt2\le L<2\), so the positive quantity \(2h/L-h/3\) strictly exceeds the first radical if and only if
\[
3L^2\left[\left(\frac{2h}L-\frac h3\right)^2-
\left(1+\frac{h^2}9\right)\right]
=(2-L)(4L^2-L-6)>0.\tag{13}
\]
Indeed \(4L^2-L-6>0\) for \(L\ge\sqrt2\). Thus (12) is strictly negative. Combined with the apex obstruction for \(h>\sqrt3\), these witnesses exclude every height other than (2).

**4. Equilateral isolation and source conjecture.** At \(h=\sqrt3\), all three vertex inequalities follow from the apex case of step 1 by threefold rotational symmetry; they are sharp at the centroid. For all the accepted shapes, (1) reads \(R_j+R_k\ge S+r_i>0\) for interior \(P\). Therefore each rational summand in (3) is at most \(S+r_i\), which proves (3) upon summation.

## Verification
A standalone Python program `verification.py` checks the coordinate formulas on finite interior samples, the two explicit failure-witness regimes, and the exact polynomial identity (11) at rational sample inputs. The analytic argument above, especially the convex supporting-plane reduction and exact sign factorization, is the general proof; numerical sampling is not used to establish universal quantifiers. Run `python3 verification.py` with Python 3's standard library.

## Relationship to prior work
Jian Liu, *Sharpened versions of the Erdös-Mordell inequality* (2015), formulated the cyclic inequality (3) as Conjecture 1 in its Section 4, alongside other strengthened Erdős–Mordell inequalities. His proved theorems treat different cyclic rational expressions. The present result classifies when a **termwise domination** suffices throughout the full isosceles shape family, proving the original conjectured cyclic inequality on a natural extreme-angle range while showing that this particular proof mechanism fails elsewhere. Liu's follow-up 2016 article contains further global cyclic refinements, but the inspected relevant statements do not assert this sharp pairwise classification. The separate published finding *Sharp symmetric Erdős–Mordell weight for isosceles triangles* bounds a weighted three-vertex **sum**, concerning another Liu conjecture, and is not the pairwise-for-every-point statement (1).

## Limitations
This is not a proof of Liu's Conjecture 1 for all triangles, nor for all isosceles triangles. Outside (2), only the **stronger termwise** inequality is disproved, not the cyclic conjecture. Searches and comparisons cannot exclude all unindexed equivalent results; one relevant external record was inspectable only by indexed summary. The finite computational checks are supporting diagnostics and not a replacement for the proof.

## References
1. J. Liu, *Sharpened versions of the Erdös-Mordell inequality*, Journal of Inequalities and Applications **2015**, 206 (2015), first public online June 19, 2015. https://doi.org/10.1186/s13660-015-0716-2 .
2. J. Liu, *Refinements of the Erdös-Mordell inequality, Barrow's inequality, and Oppenheim's inequality*, Journal of Inequalities and Applications **2016**, 9 (2016). https://doi.org/10.1186/s13660-015-0947-2 .
3. *Sharp symmetric Erdős–Mordell weight for isosceles triangles*, indexed research result (2026), identifier `indexed scientific record be176ad6d843`, public abstract indexed by published-finding corpus.
