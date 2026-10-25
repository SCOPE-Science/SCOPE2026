# Sharp longest-segment law for homothetic orthotope shells

## Finding
Let \(d\ge2\), let \(s_1,\ldots,s_d>0\), and let \(0<a<1/2\). Define the outer orthotope and the centered open inner orthotope by
\[
 B=\prod_{i=1}^d[0,s_i],\qquad H_a=\prod_{i=1}^d(as_i,(1-a)s_i),\qquad A_a=B\setminus H_a.
\]
A segment is admissible when **every point** of the entire closed Euclidean segment lies in \(A_a\), not merely its two endpoints. Put \(r=a/(1-a)\), \(s_*=\min_i s_i\), and let \(L(A_a)\) be the maximum admissible segment length. Then
\[
 \boxed{L(A_a)^2=\sum_{i=1}^{d}s_i^2-(1-r^2)s_*^2.}
\]
All maximizing segments are obtained by choosing a shortest side index \(j\), independently reflecting any coordinate, and possibly reversing the segment with endpoints
\[
 p=(0,\ldots,0),\qquad q_i=s_i\ (i\ne j),\qquad q_j=r s_j.
\]
For equal shortest sides any one of them may be chosen. In particular the unit-cube value is \(\sqrt{d-1+r^2}\). The result treats an all-dimensional **connected chord** invariant, not the potentially disconnected total length of the intersection of a complete line with the annulus.

## Assumptions and scope
Dimension \(d\) is any integer at least two; side lengths are arbitrary positive real numbers, and the removed open orthotope is a homothetic copy of ratio \(1-2a\), with the same center and axes as \(B\). The retained shell is closed and includes the inner boundary. Euclidean length is used, not a lattice or intrinsic-path metric.

## Proof
**Two-coordinate displacement lemma.** Work first in the normalized square \([0,1]^2\setminus(a,1-a)^2\). Let a contained segment have absolute coordinate displacements \(p,q\in[0,1]\). By reflecting coordinates, its parametrization may be taken as \((u+pt,v+qt)\), \(0\le t\le1\), with \(0\le u\le1-p\), \(0\le v\le1-q\). We claim
\[
 pq\le a(p+q). \tag{1}
\]
If \(p\le a\) or \(q\le a\), this is immediate. Otherwise each coordinate belongs to the open interval \((a,1-a)\) for a nonempty interval of parameter values. The intervals are disjoint, since the segment avoids the open inner square. On interchanging coordinates if necessary, the first coordinate reaches \(1-a\) no later than the second reaches \(a\). Thus a separating parameter exists, and the earliest possible exit time for the first coordinate and latest possible entry time for the second satisfy
\[
 \frac{p-a}{p}\le\frac{1-a-u}{p}\le\frac{a-v}{q}\le\frac{a}{q}.
\]
Rearranging proves (1). This argument also covers tangency: the two parameter intervals may have a common endpoint but no common interior.

For arbitrary positive weights \(\alpha,\beta\), (1) implies the sharp weighted bound
\[
 \boxed{\alpha p^2+\beta q^2\le\max\{\alpha+r^2\beta,\beta+r^2\alpha\}.} \tag{2}
\]
Indeed, if \(p\le r\), then \(\alpha p^2+\beta q^2\le\alpha r^2+\beta\). If \(r\le p\le1\), then (1) gives \(q\le ap/(p-a)\). The upper envelope
\[
 f(p)=\alpha p^2+\beta\left(\frac{ap}{p-a}\right)^2
\]
is strictly convex on \([r,1]\): \(p\mapsto ap/(p-a)=a+a^2/(p-a)\) is positive with positive second derivative, so the square of that function has positive second derivative. A strictly convex function on this interval has maximum at an endpoint. The endpoint values are \(\alpha r^2+\beta\) and \(\alpha+\beta r^2\). Equality in (2) forces \((p,q)=(1,r)\) if \(\alpha>\beta\), \((p,q)=(r,1)\) if \(\beta>\alpha\), and one of these two pairs if the weights are equal. Both pairs can be realized by segments avoiding the inner square, so (2) is sharp.

**Helly reduction.** Parametrize an admissible segment in \(A_a\) by \(x(t)\), \(0\le t\le1\), and normalize each coordinate by \(s_i\). For each coordinate form the interval
\[
 I_i=\{t\in[0,1]:a<x_i(t)/s_i<1-a\}.
\]
These are intervals (possibly empty), since the coordinates are affine in \(t\). Their total intersection is empty because the entire segment avoids \(H_a\). The elementary two-Helly property for intervals shows that there exist distinct coordinates \(i,j\) for which \(I_i\cap I_j=\varnothing\). If any \(I_i\) is empty, pair that coordinate with any other; otherwise take the largest interval lower endpoint and the smallest interval upper endpoint. Hence the projection to coordinates \(i,j\) is a contained segment of a two-dimensional centered rectangular annulus. Let \(w_k=|x_k(1)-x_k(0)|/s_k\in[0,1]\). Apply (2) with \(\alpha=s_i^2\), \(\beta=s_j^2\) to get
\[
 \begin{aligned}
 \|x(1)-x(0)\|_2^2
 &\le\sum_{k\ne i,j}s_k^2+\max\{s_i^2+r^2s_j^2,s_j^2+r^2s_i^2\}\\
 &=\sum_{k=1}^ds_k^2-(1-r^2)\min\{s_i^2,s_j^2\}\\
 &\le\sum_{k=1}^ds_k^2-(1-r^2)s_*^2.
 \end{aligned}
\]
This proves the upper bound in every dimension.

**Attainment.** Choose \(j\) with \(s_j=s_*\). Set \(x_i(t)=s_it\) for \(i\ne j\) and \(x_j(t)=rs_jt\). If \(a<t<1-a\), then \(rt<r(1-a)=a\), so the shortest-side coordinate is outside the inner interval. If \(t\) lies outside \((a,1-a)\), every other coordinate is outside its own inner interval. Therefore the segment is contained in \(A_a\). Its squared length is exactly the upper bound.

**Equality classification.** Since \(0<r<1\), equality in the last upper-bound line requires the shorter member of the Helly pair to have globally minimum side length. Equality in (2) and its strict-convexity argument forces that side's normalized displacement to be \(r\) and the other coordinate's displacement to be \(1\). Equality in the remaining coordinate estimates forces all remaining normalized displacements to be \(1\). After independent reflections, the full-displacement coordinates run as \(t\) from \(0\) to \(1\). The remaining coordinate is affine with displacement \(r\). To avoid \(H_a\) for all \(a<t<1-a\), that coordinate must lie entirely below its inner interval there or entirely above it there (a single affine function cannot cross the inner interval while those coordinates are interior). In the increasing orientation the first possibility requires its initial value \(0\), and the second requires initial value \(1-r\); the decreasing case is obtained by reflection. Independent reflections and reversal reduce these to the advertised endpoints. There are no other maximizing segments.

## Verification
The included standalone checker uses rational arithmetic on finite grids of endpoints. It tests complete segment avoidance by intersecting exact parameter intervals, checks the upper bound on all admissible grid segments, checks the two-coordinate necessary condition directly, and verifies exact attainment by the claimed optimizers for unequal side lengths. It covers \(17{,}658\) tested candidate segments in dimensions two through four and three shell thicknesses. The analytic proof above, not those finite samples, establishes the statement for all positive real side lengths, all admissible thicknesses and all dimensions.

Run with a Python 3 interpreter: `python3 checker.py`. Expected success prefix: `ORTHOTOPE_SHELL_OK`.

## Relationship to prior work
Ambrus, Corbo, Goto, Leitz and Mawhinney (2026), Claim 2.2, prove the sharp maximum of the **total one-dimensional intersection measure** of a line with a two-dimensional centered unit-square annulus, namely \(\sqrt{1+r^2}\). This recovers the unit-square, two-dimensional numerical special case here, and that case is **not** claimed as new. Their higher-dimensional results concern plank coverings and collar volume estimates rather than maximal fully contained straight segments of arbitrary rectangular orthotope shells. The weighted two-coordinate inequality, exact dimensional reduction, general side-length profile and complete equality classification supply the additional assertion. The formula does not imply a plank-covering theorem.

## Limitations
The hole must be axis-aligned, centered, and homothetic to the outer box; the theorem does not address displaced or rotated holes, non-Euclidean segment lengths, or the total disconnected length of a line's intersection with the shell. The numerical checker only corroborates finite instances. Historical priority outside searched and inspected material is not independently certified.

## References
Ambrus, G., Corbo, M., Goto, D. N., Leitz, D., Mawhinney, K., *On plank coverings of cube annuli*, arXiv:2610.18770v1, first submitted October 13, 2026. https://arxiv.org/html/2610.18770v1 ; https://arxiv.org/abs/2610.18770
