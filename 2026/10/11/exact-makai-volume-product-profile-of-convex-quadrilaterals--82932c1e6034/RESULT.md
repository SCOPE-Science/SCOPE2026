# Exact Makai volume-product profile of convex quadrilaterals

## Finding

For every proper convex quadrilateral \(Q\) in the plane, the affine-invariant product
\[
\mu(Q)=\operatorname{area}(Q)\operatorname{area}((Q-Q)^\circ)
\]
is an explicit function of its two diagonal-division parameters. After the normalization specified below, its value is
\[
\boxed{\mu(Q)=2-\frac{(t+s-1)^2}{2\max\{ts,(1-t)(1-s)\}}
                 -\frac{(t-s)^2}{2\max\{t(1-s),(1-t)s\}}.}
\]
The **exact attainable range** is \((3/2,2]\). Equality at the upper endpoint occurs precisely for parallelograms; the lower endpoint is an unattained degeneration toward a triangle.

## Assumptions and scope

A *proper convex quadrilateral* is the convex hull of exactly four distinct planar extreme points, with nonempty interior. Write its vertices in counterclockwise order \(A,B,C,D\). Its two diagonal segments \(AC\) and \(BD\) meet at one interior point \(O\). There is an invertible affine map sending these diagonal vectors to the coordinate axes and placing the vertices at
\[
A=(t,0),\quad B=(0,s),\quad C=(t-1,0),\quad D=(0,s-1),\qquad 0<t,s<1.
\]
The parameters \(t,s\) are the two fractions in which \(O\) divides the oriented diagonals. Their order may change with vertex labels, but the displayed invariant formula does not.

For a convex body \(K\), set \(K-K=\{x-y:x,y\in K\}\) and
\[
(K-K)^\circ=\{u\in\mathbb R^2:\langle u,v\rangle\le1\text{ for all }v\in K-K\}.
\]
This is the polar of the **unscaled** difference body. The product \(\mu(K)\) is invariant under all invertible affine transformations, since the difference body is translation-invariant and polarity transforms under an inverse transpose. Throughout, areas refer to ordinary two-dimensional Lebesgue area.

## Proof

**1. The affine chart and area.** Each proper quadrilateral admits the specified chart: use the two nonparallel diagonals as basis vectors, after translating \(O\) to the origin. The shoelace formula gives
\[
2\operatorname{area}(Q)=ts+s(1-t)+(1-t)(1-s)+t(1-s)=1,
\]
so \(\operatorname{area}(Q)=1/2\) throughout the open parameter square.

**2. The exact polar constraints.** Since \(Q-Q\) is the convex hull of all vertex differences and their negatives, its polar is exactly the subset of the square \([-1,1]^2\) defined by
\[
\begin{aligned}
|tx-sy|&\le1, &|(1-t)x-(1-s)y|&\le1,\\
|tx+(1-s)y|&\le1, &|(1-t)x+sy|&\le1.
\end{aligned}
\]
The square bounds come from the two differences across diagonals, \((1,0)\) and \((0,1)\). There are no other independent inequalities: every unordered vertex pair is either a diagonal or one of the four side pairs, and the opposite orientation contributes only the corresponding absolute value.

**3. Only two opposite pairs of corners can be cut.** An inequality with a minus sign is automatically satisfied in both same-sign coordinate quadrants of the square. In the two opposite-sign quadrants, its largest possible absolute value is the sum of its positive coefficients. The coefficient sums of the two minus inequalities are \(t+s\) and \(2-t-s\), respectively. Unless \(t+s=1\), exactly one sum exceeds \(1\); the other inequality is redundant on the entire square. The active inequality cuts a triangle off each of the two square corners of opposite coordinate sign, with coefficient product
\[
M_-=\max\{ts,(1-t)(1-s)\},\qquad \delta_-=|t+s-1|.
\]
Similarly, each plus inequality is automatically satisfied in opposite-sign quadrants. In the same-sign quadrants, the relevant coefficient sums are \(1+t-s\) and \(1+s-t\), so at most one is active; it cuts the remaining opposite pair of square corners with
\[
M_+=\max\{t(1-s),(1-t)s\},\qquad \delta_+=|t-s|.
\]
The four corner triangles are pairwise interior-disjoint because the minus constraints can cut only the opposite-sign quadrants and the plus constraints only the same-sign quadrants. On the transition lines their respective cut areas are zero.

**4. Exact corner areas.** If \(a,b\in(0,1)\) with \(a+b>1\), the half-plane \(ax+by\le1\), restricted to the positive unit corner of \([-1,1]^2\), removes a right triangle of legs \((a+b-1)/a\) and \((a+b-1)/b\). Its area is \((a+b-1)^2/(2ab)\). A centrally opposite corner contributes an identical area. Consequently
\[
\operatorname{area}((Q-Q)^\circ)=4-\frac{\delta_-^2}{M_-}-\frac{\delta_+^2}{M_+}.
\]
Multiplication by \(\operatorname{area}(Q)=1/2\) proves the boxed formula, including all transition boundaries inside \((0,1)^2\).

**5. Sharp range and rigidity.** Both displayed subtractions in \(2-\mu(Q)\) are nonnegative, and they vanish simultaneously exactly when \(t+s=1\) and \(t=s\), namely \(t=s=1/2\). The diagonals then bisect each other, so \(Q\) is a parallelogram, and conversely every parallelogram has this property. For the strict lower bound, Eggleston's planar difference-body polar inequality [2,3] states that \(\mu(K)\ge3/2\) for every planar convex body, with equality only for triangles. Therefore \(\mu(Q)>3/2\) for every proper quadrilateral. The continuous family \(t=s=r\) with \(1/2\le r<1\) consists of proper trapezoids and has
\[
\mu(Q_{r,r})=2-\frac{(2r-1)^2}{2r^2}.
\]
As \(r\) increases from \(1/2\) toward \(1\), this expression decreases continuously and strictly from \(2\) toward \(3/2\). This family attains all values in \((3/2,2]\), completing the range assertion.

## Verification

The result is proved for the continuum of all proper convex quadrilaterals by the exact support-inequality and corner-area arguments above. As an independent finite arithmetic check, the accompanying standalone script `verification/check_quadrilateral.py` reconstructs the polar polygon from all ordered vertex-difference half-planes using exact rational arithmetic, computes its area by a rational shoelace formula, and compares it with the displayed profile at \(148\) prescribed rational parameter pairs. The script prints `EXACT_POLAR_INTERSECTIONS_OK 148`, together with the exact sample values \(2\) for the parallelogram and \(16/9\) for a non-parallelogram trapezoid. The finite test is **not** the proof of the continuum statement.

## Relationship to prior work

Haddad, Langharst, Livshyts and Putterman [1] prove the general polar-Schneider inequality, which for its one-difference-body specialization gives an ellipsoid-sharp upper bound on \(\mu(K)\). That theorem applies to all convex bodies, but does not determine the value of \(\mu\) for every quadrilateral or its sharp four-vertex range. Aliev's 2025 work [2] supplies a new proof of the Eggleston lower bound and equality classification, and does not supply the two-parameter quadrilateral profile. The older analysis of Böröczky, Makai, Meyer and Reisner [3] treats planar volume-product lower bounds and stability, including the scaled difference-body form; it does not state this exact moduli formula. The factor-of-four conversion from the scaled formulation is
\[
\operatorname{area}(Q)\operatorname{area}\left(\left(\frac{Q-Q}{2}\right)^\circ\right)=4\mu(Q).
\]
The contribution here is the complete **shape-dependent** formula, the sharp range and parallelogram rigidity for the first non-simplicial polygonal class; it is not a new proof of either universal inequality.

## Limitations

The theorem concerns proper convex quadrilaterals only. In particular, it does not give exact profiles for arbitrary pentagons or higher-dimensional polytopes. The lower endpoint is only a degeneration, not an equality quadrilateral. Source comparisons did not identify a published equivalent quadrilateral formula, but an older or unindexed equivalent calculation remains possible; no claim of universal literature novelty is certified. The exact-rational examples are supplementary evidence and do not stand in for the analytic proof. Independent validation has not been performed.

## References

[1] J. Haddad, D. Langharst, G. V. Livshyts and E. Putterman, *On the polar of Schneider's difference body*, arXiv:2503.06191 (first posted 2025-03-08; main result Theorem 1). https://arxiv.org/abs/2503.06191

[2] A. Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991 (first posted 2025-11-19; Theorem 1.1 and Section 2). https://arxiv.org/abs/2511.14991

[3] K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies — lower estimates with stability*, Studia Scientiarum Mathematicarum Hungarica 50 (2013), 159–198; arXiv:1507.01481. https://arxiv.org/abs/1507.01481
