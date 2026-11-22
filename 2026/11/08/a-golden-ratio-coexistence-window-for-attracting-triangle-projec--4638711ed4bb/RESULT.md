# Complete primitive four-cycle census for isosceles farthest projections

## Finding
For every real \(h>0\), let \(A=(0,h)\), \(B=(-1,0)\), \(C=(1,0)\), and let \(L_0=AB\), \(L_1=BC\), \(L_2=CA\) be the **complete infinite supporting lines**. On their union, apply Everett's farthest-orthogonal-projection map: at a nonvertex point on one line, project orthogonally to both other lines and move to the projection farther from that point; when the two distances tie, stay fixed. Count primitive nonvertex cycles once up to cyclic rotation.

Writing \(\varphi=(1+\sqrt5)/2\), the **complete least-period-four census** is
\[
\boxed{N_4(h)=\begin{cases}1,&0<h<\sqrt\varphi,\\0,&h\ge\sqrt\varphi.\end{cases}}
\]
When present, its four successive points are
\[
\left(\frac{h^2}{h^2+2},0\right),\quad
\left(-\frac{h^2}{h^2+2},\frac{2h}{h^2+2}\right),\quad
\left(-\frac{h^2}{h^2+2},0\right),\quad
\left(\frac{h^2}{h^2+2},\frac{2h}{h^2+2}\right).
\]
The cycle is locally attracting, with four-step multiplier \((1+h^2)^{-2}\). At \(h^2=\varphi\), the proposed side-to-side move becomes a fixed-point tie, not a periodic orbit. There are no other nonvertex primitive period-four cycles for **any** \(h>0\), including the obtuse-apex regime \(0<h\le1\).

**Prior coverage and precise new scope.** A November 2, 2026 result, *Sharp multistability windows for an isosceles farthest-projection map*, had already explicitly derived the above base-repeated four-cycle and its golden-ratio admissibility threshold for the acute range \(h>1\), and the coexistence of that cycle with two attracting three-cycles for \(1<h^2<\varphi\). Those results and that coexistence window are **not claimed to be new** here. The additional result proved here is a **complete census** of all primitive four-cycles over the full \(h>0\) family: uniqueness in the acute range, the valid extension through and below \(h=1\), and exclusion of every other four-step line itinerary. A previously published general three-cycle theorem already supplies the period-three count; it is not part of the new claim.

## Assumptions and boundaries
The three lines are complete, pairwise nonparallel and nonconcurrent. The triangle is nondegenerate since \(h>0\). Each counted cycle avoids the three intersection vertices; this qualification is necessary for an unambiguous incoming-line label. The equality convention is **tie-as-fixed**, so no equality endpoint can be taken as an orbit branch. Local attraction means contraction on a neighborhood on the union of lines, not global basin coverage. Only *least period four* is exhaustively classified; this theorem does not classify other periods or invariant measures. Distances and multipliers use the ordinary Euclidean metric and the original height normalization with half-base one.

## Proof
Let \(P_j\) denote Euclidean projection onto \(L_j\), and write \(d_j(x)=\lVert x-P_jx\rVert^2\). On any nonfixed orbit step the incoming and outgoing line labels differ. A nonvertex primitive period-four orbit therefore has a cyclic four-word over three symbols with adjacent labels distinct. Up to cyclic rotation it either alternates between two lines or visits three distinct lines with precisely one line repeated in the two opposite positions. There are three repeated-line choices, and vertical reflection interchanges the two sloping sides.

**Alternation on two lines.** A two-line alternating orthogonal-projection return is an affine strict contraction, with unique fixed point at the intersection of those two lines. This point is a vertex and cannot be a nonvertex primitive four-orbit. Thus an admissible four-cycle must use all three lines, repeating either the base or a sloping side.

**Base repeated.** By cyclic rotation take the word \(1\to0\to1\to2\to1\). Solving the affine return fixed-point equation gives exactly the four points in the Finding. The squared-distance margin (chosen target minus competing target) is the same at both base points:
\[
D_{\rm base}=\frac{4h^4}{(1+h^2)(h^2+2)}>0.
\]
At both sloping-side points it equals
\[
D_{\rm side}=\frac{-4h^2(h^4-h^2-1)}{(1+h^2)(h^2+2)^2}.
\]
Because every denominator is positive, the whole word is chosen by the farthest rule exactly when \(h^4-h^2-1<0\). Writing \(z=h^2>0\), this is \(z^2-z-1<0\), or \(0<h<\sqrt\varphi\). At equality the map fixes the tied point; above it the candidate's prescribed branch loses. All four displayed points are distinct and interior to their respective finite triangle edges for every \(h>0\), so the admissible orbit is genuinely primitive four. Multiplication of the four affine projection derivatives gives the return multiplier \((1+h^2)^{-2}\in(0,1)\). Strict margins persist locally, establishing local attraction.

**A sloping side repeated.** By reflection it suffices to consider \(0\to1\to0\to2\to0\). The affine return has a unique candidate. At the transition leaving the base, its base coordinate is exactly
\[
t=-\frac{(h^2-1)^2}{h^4+2h^2+5}\le0.
\]
If \(h\ne1\), then \(t<0\). At \((t,0)\), the distance squared to the right sloping line \(L_2\) is \(h^2(1-t)^2/(1+h^2)\), strictly greater than its distance squared to the left sloping line \(L_0\), namely \(h^2(1+t)^2/(1+h^2)\). Thus the candidate cannot follow the proposed step from the base to \(L_0\). For \(h=1\), one has \(t=0\) and the two candidate distances tie, forcing a fixed point rather than a four-cycle. Reflection excludes repetition of \(L_2\) as well.

These cases exhaust all nonvertex four-step cyclic line itineraries. Each admissible itinerary has at most one fixed point because its projection return contracts, so the base-repeated orbit is unique. This proves the complete census for all real \(h>0\). No finite sampling or unproved basin claim enters the argument.

## Verification and limitations
An independent exact-fraction implementation that enumerates all proper cyclic line words of lengths three and four and solves each affine return reproduced the predicted period-four counts and multipliers at heights \(1/10,1/2,4/5,1,11/10,5/4,13/10,2,3\). Symbolic projection-return calculations independently reproduced the positive base-repeated fixed-point coordinate, the multiplier, and the forbidden sloping-side candidate \(t\). These finite checks corroborate but do not prove the all-real theorem; the exhaustive word analysis and exact inequalities above supply that proof. The original repository's `verify.py` is a separate exact-rational diagnostic for 111 heights. No claim about periods other than four, global attractor basins, or behavior under edge-clipped projection is made.

## Comparison with prior work
1. S. Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* 18(2), 183–192; DOI `10.1080/1726037X.2020.1847765`, author preprint `arXiv:2408.16019v1` (August 2024). It defines the map and studies convergence and geometric bifurcations, but its available abstract and secondary mathematical exposition do not establish an exact complete four-cycle census; a direct full-paper comparison remains a residual priority limitation.
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map* (October 11, 2026), full RESULT at `https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/10/11/exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8/RESULT.md`. Its full proof exhausts least period three only and does not imply this four-cycle census.
3. *Sharp multistability windows for an isosceles farthest-projection map* (November 2, 2026), full RESULT at `https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/11/02/sharp-multistability-windows-for-an-isosceles-farthest-projectio--82fd9a413389/RESULT.md`. Its acute \(h>1\) four-cycle word, exact \(h^2<\varphi\) threshold, three-cycle coexistence, and four-cycle multiplier **precede and cover** the corresponding portions here. It does not claim to exclude other period-four itineraries or address the full \(0<h\le1\) family. The new mathematical conclusion is only the strengthened global completeness statement.
4. *Exact four-cycle basins and physical-measure selection for right-isosceles farthest projections* (November 8, 2026), full RESULT at `https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/11/08/exact-four-cycle-basins-and-physical-measure-selection-for-right--8ac7abb3f002/RESULT.md`. This independently treats the single \(h=1\) similarity class and goes further in its basin analysis, but does not establish the full height-dependent four-cycle census.

A complete priority determination against every possible outside publication is not asserted. The novel scope is deliberately narrower than the original coexistence-focused presentation, without altering the mathematical four-cycle proof or its hypotheses.
