# Sharp minimum-angle area retention for inscribed isosceles triangles

## Finding

For a nondegenerate Euclidean triangle \(T\), let \(M(T)\) be the ratio of the largest area of an isosceles triangle contained in \(T\) to the area of \(T\). For \(0<\vartheta\le\pi/3\), let \(F(\vartheta)\) be the minimum of \(M(T)\) over all triangles whose smallest angle is at least \(\vartheta\).

Let \(u_*\) be the unique number in \((4/5,5/6)\) satisfying \(u_*^4+u_*^3=1\), and put \(\vartheta_* = \arccos(1/(2u_*^2))\). Then \(\vartheta_* = 41.83161869265986\ldots^\circ\), and the **sharp guarantee** is

\[
F(\vartheta)=\begin{cases}
(2\cos\vartheta)^{-1/2}, & 0<\vartheta\le\vartheta_*,\\
\text{the unique }z\in[u_*,1]\text{ solving }z^4-z^2+2z\cos\vartheta-1=0, & \vartheta_*\le\vartheta\le\pi/3.
\end{cases}
\]

For each \(0<\vartheta<\pi/3\), the minimizing triangle is unique up to similarity and relabeling. In normalized increasing side order its lengths are \((a_\vartheta,b_\vartheta,1)\), where \(b_\vartheta=F(\vartheta)\) and \(a_\vartheta=\sqrt{1+b_\vartheta^2-2b_\vartheta\cos\vartheta}\). Its smallest angle equals \(\vartheta\). At \(\vartheta=\pi/3\), equality holds exactly for equilateral triangles. The sharp unconstrained infimum is \(\inf_T M(T)=1/\sqrt2\), which is not attained by any nondegenerate triangle. The active optimal embedded-isosceles construction changes at \(\vartheta_*\), and \(F\) has a genuine first-derivative corner there.

## Assumptions and scope

All containment is Euclidean planar set inclusion, rotations and translations of the embedded isosceles triangle are permitted, and all triangles under consideration have strictly positive area. An isosceles triangle is permitted to be equilateral. Areas are ordinary Euclidean areas. The side order \(0<a\le b\le c\) refers to the host triangle; the angle opposite \(a\) is its minimum angle. A published maximum-area embedding theorem for isosceles triangles is used as an input, not claimed anew.

## Proof

**1. Exact pointwise formula.** Normalize the longest side to \(c=1\) and write \(0<a\le b\le1\). For strict inequalities, Theorem 1.2(ii) and Corollary 2.4 of Ambrus–Csikós–Kiss–Pach–Somlai [1] show that a largest inscribed isosceles triangle belongs to three explicit configurations. Their area ratios, computed from the elementary constructions in Section 2.1 of [1], are

\[
\frac ab,\qquad b,\qquad \frac{1}{1+b^2-a^2}.
\]

The first is obtained by taking a segment of length \(a\) along the host side of length \(b\), starting from their common vertex at the side \(a\); the second by truncating the longest side to length \(b\) from the opposite vertex; the third by intersecting the host side of length \(b\) with the perpendicular bisector of its side of length \(1\). In the third case, the law of cosines gives the segment ratio \(1/(2b\cos A)=1/(1+b^2-a^2)\), where \(A\) is the angle opposite \(a\). By continuity, including the case where the host itself is isosceles,

\[
M(T)=\max\left\{\frac ab,\ b,\ \frac{1}{1+b^2-a^2}\right\}.\tag{1}
\]

**2. Reduce the angular constraint to one scalar.** Put \(t=\cos\vartheta\), so \(1/2\le t<1\) for \(0<\vartheta\le\pi/3\). The smallest-angle constraint, by the law of cosines, is equivalent to

\[
a^2\ge 1+b^2-2bt.\tag{2}
\]

Since \(a\le b\), necessarily \(b\ge C:=1/(2t)\). Conversely, every \(C\le b\le1\) permits the triangle with \(a=a_0(b):=\sqrt{1+b^2-2bt}\). For positive \(\vartheta\) this triangle is nondegenerate; its smallest angle equals \(\vartheta\). At fixed \(b\), the first and third entries in (1) are strictly increasing functions of \(a\); hence the minimum is achieved at \(a=a_0(b)\). It follows that

\[
F(\vartheta)=\min_{C\le b\le1}\max\left\{b,\frac Cb,\frac{\sqrt{1+b^2-2bt}}b\right\}.\tag{3}
\]

The last two functions are strictly decreasing in \(b\) on \([C,1]\): for the last one, its square is \(1+b^{-2}-2tb^{-1}\) with derivative \(2(tb-1)/b^3<0\) on \(b<1\). The increasing function \(b\) and their decreasing maximum intersect exactly once in \([C,1]\). At \(b=C\) that maximum is \(1\), whereas at \(b=1\) it is at most \(1\); the intersection is interior if \(\vartheta<\pi/3\). Thus the unique minimizing \(b\) solves \(b=\max\{C/b,\sqrt{1+b^2-2bt}/b\}\).

**3. Solve the two competing branches.** The crossing of \(b\) with \(C/b\) is \(b_0=\sqrt C=(2t)^{-1/2}\). At this point, the third entry in (3) does not exceed \(b_0\) exactly when

\[
b_0^5-b_0^3-b_0+1=(b_0-1)(b_0^4+b_0^3-1)\ge0.\tag{4}
\]

Since \(b_0\le1\), (4) is equivalent to \(b_0\le u_*\). The polynomial \(u^4+u^3-1\) is strictly increasing for positive \(u\), with opposite signs at \(4/5\) and \(5/6\), so \(u_*\) exists uniquely. Since \(b_0\) increases with \(\vartheta\), this condition is precisely \(\vartheta\le\vartheta_*\), yielding the first branch. For \(\vartheta>\vartheta_*\), the third entry in (3) exceeds \(b_0\) at \(b_0\), and the optimal intersection is instead \(b=\sqrt{1+b^2-2bt}/b\). Squaring gives \(b^4-b^2+2tb-1=0\), which has exactly one solution beyond \(b_0\) and below \(1\) by the monotonic intersection established above. At the endpoint \(\vartheta=\pi/3\) only \(b=1\) is feasible. This proves the piecewise formula.

**4. Equality and the transition.** Strict decrease of the last two entries in (3) and strict increase of its first entry make the minimizing \(b\) unique. At that \(b\), an active first or third term in (1) is strictly increasing in \(a\), forcing equality in (2), and hence a unique similarity class with sides given in the finding. The two one-sided derivatives at \(\vartheta_*\) are

\[
F'_-(\vartheta_*)=\frac{u_*}{2}\tan\vartheta_*,\qquad
F'_+(\vartheta_*)=\frac{2u_*\sin\vartheta_*}{4u_*^3-2u_*+2\cos\vartheta_*}.
\]

They are distinct: the assertion \(F'_+>F'_-\) reduces, using \(2\cos\vartheta_*=u_*^{-2}\), to \(4u_*^5-2u_*^3<1\), which follows from \(4/5<u_*<5/6\) via \(4(5/6)^5-2(4/5)^3<1\). Finally, \(F(\vartheta)\to1/\sqrt2\) as \(\vartheta\downarrow0\), while every positive-angle triangle satisfies a strict stronger bound corresponding to its own minimum angle. Its unique limiting extremal side ratio is \((1-1/\sqrt2,1/\sqrt2,1)\), which is degenerate and hence not an equality case.

## Verification

The standalone `CHECK.py` evaluates both analytical branches by independent bisection, checks the equality-side formula against the exact three-candidate expression (1), tests the angular constraint and verifies the branch inequality on a deterministic finite test grid. It also checks strict one-sided derivative inequality at the phase point. This code is a reproducibility aid; the inequalities and uniqueness statements for every angle follow from the preceding analytic proof, not from the finite tests.

## Relationship to prior work

Ambrus et al. [1], first publicly posted on 2022-05-23, prove that all maximum-area embedded isosceles triangles share a side and an adjacent angle with the host. They enumerate the three candidate types used in Step 1. The present result does not re-prove or replace that classification: it solves a different sharp outer minimax problem over all host triangles satisfying an arbitrary minimum-angle quality constraint, obtaining the previously unstated explicit two-branch profile, the precise regime switch, equality shapes, and its non-differentiability. Earlier work on minimal-area isosceles containers [2] concerns enclosing rather than embedded triangles, and does not determine this normalized inner-area guarantee.

## Limitations

The result relies on the published pointwise optimal-embedding theorem [1]; the new arguments prove the constrained minimax and phase transition, not the underlying full classification from scratch. The profile is for Euclidean triangles, isosceles inner triangles, and a lower bound on *every* host angle; it does not extend to general convex polygons, equilateral-only inner triangles, or other angle-quality constraints. The universal endpoint is an infimum attained only in a degenerate limit. Bibliographic searches cannot certify absolute priority; a closely related unindexed inequality might exist.

## References

[1] Á. Ambrus, M. Csikós, G. Kiss, J. Pach, and G. Somlai, *Optimal embedded and enclosing isosceles triangles*, arXiv:2205.11637v1 (2022-05-23), Section 2.1, Corollary 2.4, Theorem 1.2(ii), and proof in Section 3. Full text: https://arxiv.org/html/2205.11637v1 . Subsequently published in *International Journal of Foundations of Computer Science* 34 (2023), 737–760.

[2] G. Kiss, J. Pach, and G. Somlai, *Minimum area isosceles containers*, Journal of Information Processing 28 (2020), 759–765, as referenced in [1].
