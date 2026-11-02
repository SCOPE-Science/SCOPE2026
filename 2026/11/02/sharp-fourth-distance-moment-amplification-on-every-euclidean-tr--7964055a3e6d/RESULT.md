# Sharp fourth-distance-moment amplification on every Euclidean triangle

## Finding
Let \(T\subset\mathbb R^2\) be any nondegenerate Euclidean triangle. Let \(X,Y\) be independent points uniform by area in \(T\), and \(U,V\) independent points uniform by arclength on \(\partial T\). Define \(I_4=\mathbb E\|X-Y\|^4\) and \(B_4=\mathbb E\|U-V\|^4\). Then
\[
2<\frac{B_4}{I_4}\le\frac{32}{9}.
\]
The upper equality holds exactly for equilateral triangles. The lower constant is an unattained sharp infimum, approached when two vertices coalesce and the remaining two side lengths become equal. The upper constant is also approached by flattened triangles with side-length proportions \(2:1:1\).

## Assumptions and scope
Sampling is independent within each pair, exactly area-uniform for \(X,Y\) and arclength-uniform for \(U,V\); both fourth moments are of **Euclidean point-pair distance**, not Crofton-random chord length. All side lengths are strictly positive and satisfy strict triangle inequalities. No upper bound on aspect ratio is imposed.

If the triangle's side lengths are \(a=u+v\), \(b=u+w\), \(c=v+w\), then \(u,v,w>0\) and the semiperimeter is \(s=u+v+w\). Set \(p=(uv+uw+vw)/s^2\) and \(q=uvw/s^3\). Here \(0<p\le1/3\) and \(q>0\).

## Proof
**Exact moments.** Uniform barycentric integration on a triangle gives
\[
I_4=\frac{a^4+b^4+c^4}{60}
=\frac{s^4}{30}\bigl((1-p)^2-4q\bigr).
\]
For boundary points, the three edges have sampling weights \(a/(2s), b/(2s), c/(2s)\), and the position on each chosen edge is affine-uniform. In the affine coordinates of a triangle with vertices \((0,0),(1,0),(0,1)\), squared Euclidean distance between points whose coordinate differences are \((h,k)\) is \(c^2h^2+b^2k^2+(b^2+c^2-a^2)hk\). Integrating its square over the nine ordered edge pairs, using their independent uniform edge parameters, yields
\[
B_4=s^4\left(\frac1{15}+\frac{p-8}{9}q\right).
\]
The finite polynomial expansions and their exact rational verification are reproduced in `check.py`. In particular, no approximation or sampling assumption enters either identity.

**Sharp lower bound.** Subtraction gives
\[
B_4-2I_4=\frac{s^4}{45}\{6p-3p^2+(5p-28)q\}.
\]
AM–GM gives \((u+v+w)(uv+uw+vw)\ge9uvw\), i.e. \(q\le p/9\). Since \(5p-28<0\),
\[
B_4-2I_4\ge\frac{s^4p}{405}(26-22p)>0.
\]
As \((u,v,w)\) tends to \((1,0,0)\), the ratio tends to \(2\).

**Sharp upper bound.** Set
\[
Q(p,q)=7-32p+16p^2+(56-15p)q.
\]
The exact identity is
\[
\frac{32}{9}I_4-B_4=\frac{s^4}{135}Q(p,q).
\]
For \(0<p\le1/4\), \(7-32p+16p^2=16(p-1/4)(p-7/4)\ge0\), and the strictly positive \(q\)-term makes \(Q>0\). For \(1/4<p\le1/3\), normalize \(s=1\). Fixing \(p\) fixes both the sum and the sum of squares of \(u,v,w\); all feasible triples form a compact circle inside the positive octant. A minimum of \(q=uvw\) on this circle has two equal coordinates by Lagrange multipliers. The smaller product occurs at the two larger equal coordinates:
\[
(u,v,w)=\left(\frac{1+t}{3},\frac{1+t}{3},\frac{1-2t}{3}\right),\quad t=\sqrt{1-3p}\in[0,1/2).
\]
The other stationary configuration has product larger by \(4t^3/27\). Since \(56-15p>0\), it follows that
\[
Q(p,q)\ge \frac{t^2(1-2t)(5t^2-14t+44)}{27}\ge0.
\]
The final factor is positive on \([0,1/2]\), and equality for an actual triangle requires \(t=0\), hence \(u=v=w\). This is exactly the equilateral family. Its ratio is \(32/9\). Finally, as \((u,v,w)\to(0,1/2,1/2)\), the ratio again tends to \(32/9\), showing the separate flattened upper extremizing sequence.

## Verification
`check.py` independently integrates the nine ordered edge pairs with exact symbolic polynomial arithmetic, compares the formulas for \(I_4\) and \(B_4\), factors both inequality identities, and verifies the fixed-\(p\) sharp factor. It additionally samples two independent uniform points in the interior and on the boundary of three nondegenerate triangles. All checks passed. Numerical tests corroborate formulas but do not replace the analytical positivity and extremal arguments.

## Relationship to prior work
Pure, Durrani, Tong and Pan (arXiv:1903.07757, first publicly posted 2019-03-18) develop a forward formula for two-point distance distributions in arbitrary polygonal regions. Bäsel (arXiv:2101.03815, first posted 2021-01-11) studies moments for regular polygons, including the equilateral case. Related published geometry work compares second moments between triangle boundary and interior sampling and fourth moments on parallelograms. Those statements do not imply this universal **fourth-moment** amplification interval with both sharp endpoints and its equality classification. A preprint by Lotnikov (arXiv:2608.14848, 2026) concerns boundary-versus-interior distance comparisons; its full manuscript was unavailable for definitive comparison, so historical priority remains provisional.

## Limitations
The result is specific to triangles in the Euclidean plane and two independently sampled points under the stated area/arclength measures. It says nothing about point-to-boundary distance, random-line chord measures, general convex bodies, or finite-sample estimation. No independent audit has been performed.

## References
- R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757 (2019), https://arxiv.org/abs/1903.07757.
- U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815 (2021), https://arxiv.org/abs/2101.03815.
- A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848 (2026), https://arxiv.org/abs/2608.14848 (comparison limited to available abstract).
