# Optimal finite-link tangent-polygon barriers for the disk

## Finding
Let \(B\) be the closed unit disk in the Euclidean plane. For every integer \(k\ge 2\), consider polygonal chains formed by retaining \(k\) consecutive sides of a **strictly convex \((k+1)\)-gon** each of whose supporting side lines is tangent to \(B\). The infimum of the lengths of these chains is attained, and its exact value \(L_k\) is
\[
L_k=2\tan a_k+2(k-1)\tan b_k,
\]
where \(b_k\in(0,\pi/2)\) is the unique solution of
\[
2\arctan\sqrt{1+2\tan^2 b_k}+(k-1)b_k=\pi,
\qquad
 a_k=\frac{\pi-(k-1)b_k}{2}.
\]
Every optimizer, up to plane isometry, has half-exterior angles \(a_k\) at the two ends of the omitted polygon side and \(b_k\) at the other \(k-1\) vertices; the optimizer is unique up to isometry. In particular,
\[
L_2=(1+\sqrt5)\sqrt{2+\sqrt5},\qquad L_3=4\sqrt2.
\]
The sequence is strictly decreasing, and for \(k\to\infty\) it approaches the optimum connected-disk-barrier length with the sharp excess
\[
L_k=\pi+2+\frac{\pi^3}{12(k-1)^2}+O\!\left((k-1)^{-4}\right).
\]
Every chain in this class is an opaque barrier for \(B\): every line meeting \(B\) also meets the chain.

## Assumptions and scope
The disk has radius one; by homothety all lengths scale linearly with its radius. The \(k\) links are the edges of a **convex, tangential, \((k+1)\)-vertex polygon with one side deleted**. Polygons are strictly convex and all normal gaps are less than \(\pi\); no polygon edge degenerates, all supporting lines are tangent to the same unit circle, and only **one** polygon side is deleted. Arbitrary \(k\)-link curves, non-tangential polygons, disconnected opaque sets, and unrestricted barriers are **not** optimized here. The indexed angles satisfy \(0<x_i<\pi/2\) and \(\sum_{i=1}^{k+1}x_i=\pi\); conversely such a tuple gives a strictly convex tangential polygon uniquely up to rotation via successive outward normals separated by \(2x_i\).

A connected compact planar set intersects each line that meets its convex hull: in every direction, its continuous orthogonal projection is an interval equal to the projection of its convex hull. Since the convex hull of the retained polygonal chain is the entire polygon and contains the unit disk, the chain is a disk barrier, including for tangent lines.

## Proof
**Step 1: exact geometric objective.** Index the polygon vertices in order so that the omitted side joins vertices \(1\) and \(k+1\). Let \(2x_i\) be the exterior angle at vertex \(i\); in a unit-inradius tangential polygon, the two tangency segments from that vertex have length \(\tan x_i\). Thus the side joining vertices \(i\) and \(i+1\) has length \(\tan x_i+\tan x_{i+1}\). Summing the retained \(k\) sides gives exactly
\[
F(x_1,\ldots,x_{k+1})=\tan x_1+\tan x_{k+1}
  +2\sum_{i=2}^{k}\tan x_i,\qquad
\sum_{i=1}^{k+1}x_i=\pi.
\]
The normal-turning and positive-gap hypotheses are precisely \(0<x_i<\pi/2\) together with the sum constraint. Conversely, taking the outward supporting normals in this order and intersecting consecutive tangent lines constructs the polygon. Every supporting line is an actual side because its point of tangency lies strictly inside every other tangent half-plane.

**Step 2: global optimization and rigidity.** The second derivative of \(\tan x\) equals \(2\sec^2x\tan x>0\) on \((0,\pi/2)\). Therefore \(F\) is strictly convex on the convex feasible domain. A stationary point must satisfy equality of the weighted marginal derivatives, so its two endpoint coordinates are equal to \(a\), its other \(k-1\) coordinates equal to \(b\), and
\[
\sec^2a=2\sec^2b,\qquad 2a+(k-1)b=\pi.
\]
Equivalently, \(\tan a=\sqrt{1+2\tan^2b}\), leading to the displayed scalar equation. Its left side is strictly increasing for \(b\in(0,\pi/2)\), starts at \(\pi/2\) and tends to a value strictly greater than \(\pi\); hence there is exactly one solution. This constructs an interior stationary point, which strict convexity makes the unique **global** minimizer, including against sequences approaching the omitted boundary of the feasible open simplex. Uniqueness of the normal gaps gives geometric uniqueness up to rotation/reflection. The formula for \(L_k\) follows.

For \(k=2\), put \(t=\tan a\), so \(b=\pi-2a\) and \(\tan b=2t/(t^2-1)\). The stationarity relation yields \((t^2-1)^3=8t^2\), factoring as \((t^2+1)(t^4-4t^2-1)=0\). The positive solution has \(t^2=2+\sqrt5\), giving the stated \(L_2\). For \(k=3\), \(a+b=\pi/2\), \(\tan a=\sqrt2\), and \(L_3=4\sqrt2\).

**Step 3: strict link-count improvement.** For an optimal \(k\)-link polygon, split any non-endpoint half-exterior angle \(b_k\) into two equal positive half-angles while keeping the remaining ones unchanged. The resulting normal list is a valid \((k+2)\)-sided tangential polygon and its chain has \(k+1\) links. In the objective, the single interior contribution \(2\tan b_k\) becomes \(4\tan(b_k/2)<2\tan b_k\), so \(L_{k+1}<L_k\).

**Step 4: sharp convergence.** Write \(q=k-1\), \(b=b_k\), \(a=a_k\). Since \(2a+qb=\pi\) and \(\tan a=\sqrt{1+2\tan^2b}\), the root has \(b=O(q^{-1})\), \(a\to\pi/4\), and Taylor expansion gives
\[
a=\frac\pi4+\frac{b^2}{2}+O(b^4),\qquad
qb=\frac\pi2-b^2+O(b^4),\qquad
b=\frac\pi{2q}+O(q^{-3}).
\]
Consequently, using \(\tan b=b+b^3/3+O(b^5)\),
\[
2\tan a+2q\tan b
=2+2b^2+O(b^4)+2qb+\frac{2q}{3}b^3+O(qb^5)
=2+\pi+\frac{2q}{3}b^3+O(b^4+qb^5)
=2+\pi+\frac{\pi^3}{12q^2}+O(q^{-4}).
\]
The positive coefficient proves the exact leading rate; a finite numerical table alone would not establish this asymptotic.

## Verification
Run the included, self-contained Python 3 program `verify.py` in the same directory as this document: `python verify.py`. It solves the monotone scalar equation by bisection, independently constructs the intersections of the tangent lines, sums the actual retained side lengths, checks the first-order equation and angle normalization, verifies the closed formulas for \(k=2,3\), and compares finite samples to the sharp asymptotic coefficient. These numerical checks are **illustrative**: the infinite family, strict global optimality and asymptotic remainder are proven analytically above.

## Relationship to prior work
Nikonorov's 2021 paper, *Properties of a curve whose convex hull covers a given convex body* (arXiv:2109.12830v1; primary MSC2020 52A10), treats lower bounds for curves covering convex figures, including a perimeter-minus-diameter inequality and its higher-dimensional generalization; its full text does not give this finite-link circumscribed-polygon minimizer, endpoint-angle rigidity, or rate. Dumitrescu, Jiang and Pach's *Opaque sets* (arXiv:1005.2218v5) discusses connected and single-arc barriers, proves a minimum Hamiltonian path theorem for the **vertices of a fixed convex polygon** (Theorem 6), and quotes the classic optimal length \(\pi+2\) for a connected unit-disk barrier. Those results give the natural background and benchmark but do not determine the optimum when the tangent polygon itself varies with the prescribed number of sides. Faber, Mycielski and Pedersen (1984) is the classical connected-disk reference; its full text was inaccessible during this comparison, so the possibility of an earlier finite-link formulation there remains an explicitly unexcluded priority risk.

## Limitations
The optimization is **only** for the defined tangential-polygon-minus-one-edge class. Neither uniqueness nor length optimality is claimed among arbitrary connected \(k\)-segment barriers, and there is no claim about disconnected opaque forests. The independent scholarly audit has not been performed. A targeted novelty search and material comparison of two accessible primary texts found no implication to this finite-link result, but absence from the searched texts is not proof of absolute priority; the inaccessible 1984 full text is a residual risk.

## References
1. Yu. G. Nikonorov, *Properties of a curve whose convex hull covers a given convex body*, arXiv:2109.12830v1 (first public version, 2021-09-27), https://arxiv.org/html/2109.12830v1.
2. A. Dumitrescu, M. Jiang and J. Pach, *Opaque sets*, arXiv:1005.2218v5, https://arxiv.org/html/1005.2218v5, especially §§4 and 6, Theorem 6.
3. V. Faber, J. Mycielski and P. Pedersen, *On the shortest curve which meets all the lines which meet a circle*, Annales Polonici Mathematici 44 (1984), 249–266, doi:10.4064/ap-44-3-249-266 (full text not obtained in this run).
