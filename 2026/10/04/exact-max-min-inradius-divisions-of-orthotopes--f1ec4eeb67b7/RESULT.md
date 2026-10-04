# Exact max-min inradius divisions of orthotopes

## Finding

Let
\[
R=\prod_{i=1}^d[0,L_i]\subset\mathbb R^d,
\qquad
L_1\ge\cdots\ge L_d=\ell>0,
\qquad d\ge2.
\]
For a two-division by one hyperplane, write \(\widetilde I_2(R)\) for the largest possible value of the smaller inradius of the two parts.

Put
\[
A=\sum_{i=1}^dL_i,
\qquad
B=\sum_{i=1}^dL_i^2,
\qquad
\Delta=\sum_{i=1}^d(L_i-\ell)^2-\ell^2.
\]
Then
\[
\boxed{
\widetilde I_2(R)=
\begin{cases}
\displaystyle
\frac{A-\sqrt{A^2-(d-1)B}}{2(d-1)},&\Delta<0,\\[3mm]
\displaystyle
\frac{\ell}{2},&\Delta\ge0.
\end{cases}}
\]

The formula comes with an optimizer classification in the unsaturated regime. If \(\Delta<0\), every optimal cut is, up to symmetries of the orthotope and interchange of the two pieces, the hyperplane through the center of \(R\) perpendicular to a space diagonal of the eroded orthotope
\[
R_{r_*}=\prod_{i=1}^d[r_*,L_i-r_*],
\qquad r_*=\widetilde I_2(R).
\]
At the transition \(\Delta=0\), the same diagonal description holds. When \(\Delta>0\), the optimum saturates at the full inradius \(\ell/2\), and optimal cuts are exactly those that separate two radius-\(\ell/2\) balls contained in \(R\).

A general structural identity underlies the computation: for every convex body \(C\),
\[
\widetilde I_2(C)=p_2(C),
\]
where \(p_2(C)\) denotes the largest radius of two equal Euclidean balls with disjoint interiors contained in \(C\).

For the unit cube this gives the particularly simple formula
\[
\boxed{
\widetilde I_2([0,1]^d)
=
\frac{\sqrt d}{2(\sqrt d+1)}
},
\]
and every optimal cut is a central hyperplane perpendicular to a body diagonal.

For a rectangle \([0,W]\times[0,H]\), with \(W\ge H\), one obtains
\[
\boxed{
\widetilde I_2=
\begin{cases}
\displaystyle\frac{W+H-\sqrt{2WH}}2,&H\le W\le2H,\\[2mm]
\displaystyle\frac H2,&W\ge2H.
\end{cases}}
\]
In particular the square value is \(1-1/\sqrt2\) after unit normalization.

## Assumptions and scope

A two-division is one hyperplane cut, exactly as in the division model of Cañete, Fernández, and Márquez. The two resulting subsets are the intersections of the orthotope with the two closed half-spaces.

The inradius is Euclidean. No affine invariance is claimed: changing side lengths changes the Euclidean problem.

The result concerns two-divisions. It does not give the max-min inradius for three or more successive cuts.

## Proof

First consider an arbitrary convex body \(C\). Suppose a hyperplane \(H\) divides \(C\) into \(C_1\) and \(C_2\), and both parts have inradius at least \(r\). Choose radius-\(r\) balls \(B(c_1,r)\subset C_1\) and \(B(c_2,r)\subset C_2\). Because the balls lie in opposite closed half-spaces bounded by \(H\), their centers have signed distances at least \(r\) from \(H\) on opposite sides. Hence
\[
\lVert c_1-c_2\rVert\ge2r,
\]
so their interiors are disjoint. Thus every two-division with minimum inradius \(r\) produces a two-ball packing of radius \(r\).

Conversely, suppose two radius-\(r\) balls \(B(c_1,r)\) and \(B(c_2,r)\) lie in \(C\) and have disjoint interiors. Since the radii are equal,
\[
\lVert c_1-c_2\rVert\ge2r.
\]
The perpendicular bisector of \(c_1c_2\) separates the two entire balls. Cutting \(C\) by that bisector therefore gives a two-division whose two parts each contain a radius-\(r\) ball. Taking suprema in the two directions proves
\[
\widetilde I_2(C)=p_2(C).
\]

Now specialize to the orthotope \(R\). A radius-\(r\) ball is contained in \(R\) exactly when its center lies in the eroded orthotope
\[
R_r=\prod_{i=1}^d[r,L_i-r].
\]
Necessarily
\[
0\le r\le\frac\ell2.
\]
Two radius-\(r\) balls fit if and only if \(R_r\) contains two points at distance at least \(2r\). Its diameter is
\[
D(R_r)=
\sqrt{\sum_{i=1}^d(L_i-2r)^2}.
\]
Hence the exact feasibility condition is
\[
q(r):=
\sum_{i=1}^d(L_i-2r)^2-4r^2
\ge0.
\]
Expanding,
\[
q(r)=B-4Ar+4(d-1)r^2.
\]
On \([0,\ell/2]\),
\[
q'(r)=-4A+8(d-1)r
\le -4A+4(d-1)\ell<0,
\]
because \(A\ge d\ell\). Therefore \(q\) is strictly decreasing throughout the feasible interval.

At the full inradius,
\[
q(\ell/2)
=
\sum_{i=1}^d(L_i-\ell)^2-\ell^2
=
\Delta.
\]
If \(\Delta\ge0\), then two radius-\(\ell/2\) balls fit, and no part of \(R\) can have inradius exceeding \(\ell/2\). This proves
\[
\widetilde I_2(R)=\frac\ell2.
\]

If \(\Delta<0\), strict decrease gives one root \(r_*\in(0,\ell/2)\). Solving \(q(r_*)=0\) gives
\[
r_*
=
\frac{A-\sqrt{A^2-(d-1)B}}{2(d-1)}.
\]
The larger quadratic root lies beyond the first crossing and is irrelevant. This proves the value formula.

For the optimizer classification when \(\Delta<0\), any optimal cut supplies two radius-\(r_*\) inballs. Their centers lie in \(R_{r_*}\) and are separated by the cut, hence have distance at least \(2r_*\). But
\[
D(R_{r_*})=2r_*.
\]
Thus their centers must be a diameter pair of the orthotope \(R_{r_*}\), namely opposite vertices. The two balls are tangent. A separating hyperplane between two tangent equal balls is uniquely their common middle tangent hyperplane: it passes through their tangency point, equivalently through the center of \(R\), and is perpendicular to the segment joining the centers. This is precisely the claimed diagonal cut. The same argument applies at \(\Delta=0\), because the diameter of \(R_{\ell/2}\) is then exactly \(\ell\).

For the cube, substituting \(L_i=1\) gives
\[
r_*
=
\frac{d-\sqrt d}{2(d-1)}
=
\frac{\sqrt d}{2(\sqrt d+1)}.
\]
For a rectangle, the transition condition is
\[
(W-H)^2\ge H^2,
\]
which is equivalent to \(W\ge2H\), and the smaller quadratic root reduces to the displayed planar formula.

## Verification

The standalone checker reconstructs
\[
q(r)=\sum_i(L_i-2r)^2-4r^2
\]
and verifies its strict monotonicity on the admissible radius interval for exact rational test families. It checks the branch transition, the cube tangent-diagonal identity through dimension \(100\), the rectangle formula including the threshold \(W=2H\), and compares the closed form against direct bisection of the packing inequality on hundreds of deterministic orthotopes.

The replay output is:

`VERIFY_OK orthotope max-min inradius profile`

The computations are consistency checks only. The all-dimensional formula and optimizer classification are proved analytically above.

## Relationship to prior work

Cañete, Fernández, and Márquez formulate the max-min problem for the inradius for successive hyperplane divisions, prove existence of balanced optima, and give the general lower bound
\[
\widetilde I_n(C)\ge\frac{I(C)}n.
\]
For two pieces they give an implicit characterization through a rounded body and a max-min width value. Their discussion explicitly says that refining the optimal-value bounds remains open. The full text treats orthotopes elsewhere for diameter and width estimates, but it does not state an orthotope formula in the max-min inradius subsection and does not use the two-equal-ball packing equivalence.

The elementary problem of fitting two equal circles or balls in boxes is classical and is not claimed as new here. In particular, the square value \(1-1/\sqrt2\) is a familiar two-circle packing calculation. The new claim is the exact identification of the two-division max-min inradius invariant with two-ball packing, followed by the all-dimensional orthotope profile and the resulting classification of every optimal cut in the unsaturated regime.

Targeted searches for max-min inradius divisions of rectangles, boxes, orthotopes and hypercubes; for two-ball packing formulations of the division invariant; and for the displayed radical profile did not locate an equivalent division theorem.

## Limitations

The two-ball packing identity is specific to two hyperplane pieces. For three or more successive cuts, a packing of several equal balls need not encode the required cut tree, so no multi-piece extension is claimed.

In the saturated regime \(\Delta>0\), the value is explicit but there is generally a continuum of optimal cuts; the result characterizes them through separation of two full-inradius balls rather than listing a finite normal-form family.

Because the orthotope packing calculation is elementary, an equivalent division observation could exist under different terminology or in unindexed material. The inspected primary source and targeted searches did not reveal one.

## References

A. Cañete, I. Fernández, and A. Márquez, “Optimal divisions of a convex body,” Mathematical Inequalities & Applications 26 (2023), 315–342, DOI 10.7153/mia-2023-26-21; arXiv:2311.13882.

A. Cañete, “Optimal divisions of a convex body,” abstract in Congreso Bienal de la Real Sociedad Matemática Española, Ciudad Real, 17–21 January 2022, describing the joint work with I. Fernández and A. Márquez and citing a 2021 preprint.
