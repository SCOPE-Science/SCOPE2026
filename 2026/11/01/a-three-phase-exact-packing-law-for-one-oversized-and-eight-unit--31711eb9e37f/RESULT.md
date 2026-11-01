# A three-phase exact packing law for one oversized and eight unit squares

## Finding
For every real \(a\ge1\), the optimal container side for one square of side \(a\) and eight unit squares, all axis-parallel, is
\[
L(a)=\max\{a+1,\min\{a+2,5\}\}=
\begin{cases}
a+2,&1\le a\le3,\\
5,&3\le a\le4,\\
a+1,&a\ge4.
\end{cases}
\]
The constant middle phase is a genuine packing threshold, rather than an area comparison.

## Assumptions and scope
All nine squares are closed, have pairwise disjoint interiors, and must lie in a closed axis-parallel square container; rotations are forbidden. The unit squares have side exactly \(1\), and the distinguished square has side \(a\ge1\). Boundary contacts are permitted. Scaling gives the general case of one square of side \(a\) and eight congruent squares of side \(b>0\) by multiplying the displayed function of \(a/b\) by \(b\), provided \(a\ge b\).

## Proof
**The geometric obstruction.** Let a square of side \(a\) and eight unit squares be packed in a container of side \(L\). We claim that
\[
L\ge \min\{a+2,5\}.
\]
Assume the contrary: \(L<a+2\) and \(L<5\). Then \(L-a<2\). Reflect each coordinate if needed so that the gap on the left and the gap below the \(a\)-square are each less than \(1\). This is possible because the two horizontal gaps sum to \(L-a<2\), and similarly vertically. Thus each unit square, being interior-disjoint from the large square, lies either entirely to its right or entirely above it (or both). Assign every unit square to one such strip.

Both the right strip and the top strip have width less than \(2\). In a strip of width less than \(2\), any two unit squares' projections across the short direction overlap in their interiors, so the projections along the long direction must have disjoint interiors. Because \(L<5\), each strip holds at most four unit squares. The total is eight, so exactly four are assigned to each strip.

Let \(T\) be the top-strip square with greatest left coordinate and \(R\) the right-strip square with greatest bottom coordinate. The four assigned top-strip squares have disjoint horizontal unit projections, so the left coordinate of \(T\) is at least \(3\); also it is at most \(L-1\). Likewise, the bottom coordinate of \(R\) lies in \([3,L-1]\).

Write \(x_R\) for the left coordinate of \(R\), \(x_T\) for the left coordinate of \(T\), and similarly \(y_R,y_T\). The right-strip condition and containment give
\[
a\le x_R\le L-1<4\le x_T+1,
\qquad x_R+1\ge a+1>L-1\ge x_T.
\]
Thus the horizontal projections of \(R\) and \(T\) overlap in their interiors. By the identical vertical argument,
\[
a\le y_T\le L-1<4\le y_R+1,
\qquad y_T+1\ge a+1>L-1\ge y_R,
\]
so their vertical projections also overlap. Their interiors intersect, a contradiction. This proves the claimed obstruction.

**A separate span obstruction.** If \(L<a+1\), the gaps around the large square total \(L-a<1\) on each coordinate, so no unit square can be disjoint from the large square. Therefore \(L\ge a+1\). Combining both arguments yields
\[
L\ge\max\{a+1,\min\{a+2,5\}\}.
\]

**Sharp constructions.** Put the \(a\)-square at \([0,a]^2\). For \(1\le a\le3\), use a container of side \(a+2\): place six unit squares in two rows of three with lower-left corners \((j,a+i)\), \(j=0,1,2\), \(i=0,1\), and two more with lower-left corners \((a,0)\) and \((a+1,0)\). For \(3\le a\le4\), use the side-\(5\) container: place five unit squares at \((j,4)\), \(j=0,1,2,3,4\), and three at \((4,j)\), \(j=0,1,2\). For \(a\ge4\), use side \(a+1\), five unit squares at \((j,a)\), \(j=0,1,2,3,4\), and three at \((a,j)\), \(j=0,1,2\). All listed interiors are disjoint, all squares lie in their containers, and their container sides equal the lower bound. This proves the result for every real \(a\ge1\), including both transition points.

## Verification
The lower bound is a continuous geometric argument and needs no finite enumeration. The standalone `verify_packings.py` constructs and checks the three stated layouts at rational sample points on both sides of the two transitions and exactly at the transition points. Its finite checks corroborate the constructions only, not the universal lower bound.

## Relationship to prior work
Badger, *Axis-parallel square packing with an exact formula for optimal packing of seven squares* (arXiv:2610.22622, first public 15 October 2026), gives the general optimal-packing function for up to seven squares and observes that the complete nine-square formula is unknown. Badger's companion paper *An exact formula for optimal axis-parallel packing of eight squares* (arXiv:2610.28504, first public 20 October 2026) solves all eight-square side vectors. The present one-parameter **nine**-square formula is not a corollary of either seven- or eight-square theorem. The general finite-strategy framework and standard axis-parallel nonoverlap condition are prior work; the two-strip obstruction and the three-branch nine-square determination are the asserted contribution.

## Limitations
The theorem concerns only one distinguished square plus eight equal unit squares with a common orientation. It does not determine the arbitrary nine-square problem, placements under free rotation, or uniqueness of optimizers. Historical priority among unindexed packing constructions has not been independently established.

## References
1. M. Badger, *Axis-parallel square packing with an exact formula for optimal packing of seven squares*, arXiv:2610.22622v1 (15 October 2026), https://arxiv.org/html/2610.22622v1.
2. M. Badger, *An exact formula for optimal axis-parallel packing of eight squares*, arXiv:2610.28504v1 (20 October 2026), https://arxiv.org/html/2610.28504v1.
3. K. G. Murata, K. Fujiyoshi, S. Nakatake and Y. Kajitani, *Rectangle-packing algorithms based on sequence-pair*, IEEE Transactions on Computer-Aided Design (1996), as cited in [1] and [2].
