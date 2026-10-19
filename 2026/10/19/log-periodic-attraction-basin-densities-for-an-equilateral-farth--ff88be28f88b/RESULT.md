# Log-periodic attraction-basin densities for an equilateral farthest-projection map

## Finding
Let three complete straight lines support a Euclidean equilateral triangle of side length one. On their union, apply the farthest-orthogonal-projection rule: from a point on one line, orthogonally project onto each of the other two lines, choose the *farther* projection, and leave the point fixed when their distances tie. Orient the three supporting lines cyclically around the triangle and use the side length as the unit of coordinate. Write a point as \((i,t)\), where \(i\in\mathbb Z/3\mathbb Z\) labels a line and \(t\in\mathbb R\) is its oriented coordinate, with the triangle side corresponding to \(0\le t\le1\).

The only periodic orbits are the three midpoint fixed points \((i,1/2)\) and the two attracting primitive three-cycles
\[
 C_- = \{(0,1/3),(1,1/3),(2,1/3)\},\qquad
 C_+ = \{(0,2/3),(1,2/3),(2,2/3)\}.
\]
Every other point either maps to a midpoint in finitely many steps or converges exponentially to exactly one of these two cycles. In every line coordinate, the exceptional set of points eventually fixed is exactly
\[
 E=\left\{\frac12\right\}\cup
 \bigcup_{k=0}^{\infty}\{4^k,\,2\cdot4^k,\,1-4^k,\,1-2\cdot4^k\}.
\]
It is precisely the boundary between the two open attracting basins (as viewed along each supporting line). It has no finite accumulation point, and among the three complete supporting lines the number of distinct exceptional physical points satisfying \(|t|\le R\) in at least one oriented chart is \(12\log_4 R+O(1)\) as \(R\to\infty\).

There is nevertheless **no limiting one-sided arclength fraction** of the two basins. On any oriented supporting ray \(0\le t\le R\), let \(B_-(R)\) denote the length, in side-length units, attracted to \(C_-\). For every \(R\ge1\), put \(m=\lfloor\log_4 R\rfloor\). Then the exact formula is
\[
 \boxed{B_-(R)=\frac{4^m}{3}+\frac16+\min\{R-4^m,4^m\}.}
\]
In particular, the **complete cluster interval** of \(B_-(R)/R\) as \(R\to\infty\) is \([1/3,2/3]\), so that
\[
 \boxed{\liminf_{R\to\infty}\frac{B_-(R)}R=\frac13,\qquad
 \limsup_{R\to\infty}\frac{B_-(R)}R=\frac23.}
\]
The complementary basin has the opposite one-sided fractions, since the exceptional set has zero length. These statements concern the unbounded three-line map, not a modified boundary-only map.

## Assumptions and scope
Take triangle vertices \(V_0,V_1,V_2\) in counterclockwise order with adjacent Euclidean distances all equal to one. Let \(\ell_i\) be the entire oriented line from \(V_i\) toward \(V_{i+1}\) (indices modulo three), and identify \((i,t)\) with \(V_i+t(V_{i+1}-V_i)\). The two representations of each vertex specify the same physical point and yield the same image. At a distance tie the physical point is fixed. Basin attraction means Euclidean distance to the stated three-cycle tends to zero, and a basin boundary is taken in the relative topology of each of the three complete lines. The length \(B_-(R)\) is one-dimensional Euclidean arclength along \(\ell_i\) over the directed segment \(t\in[0,R]\); the value is independent of \(i\).

## Proof
**1. Exact geometric reduction.** For a point with coordinate \(t\) on a side's supporting line, distances to the two other supporting lines are \((\sqrt3/2)|t|\) and \((\sqrt3/2)|1-t|\). The larger is the line incident to the *terminal* vertex if \(t<1/2\), and to the *initial* vertex if \(t>1/2\). Projection onto these lines is an affine contraction by the cosine of sixty degrees, giving the exact skew map
\[
 T(i,t)=
 \begin{cases}
 (i+1,(1-t)/2),&t<1/2,\\
 (i,t),&t=1/2,\\
 (i-1,1-t/2),&t>1/2,
 \end{cases}
 \qquad(i\bmod 3).
\]
These equations hold on the *entire* supporting lines, not only on their three side segments. In particular, the map is unambiguous at a vertex: the two incident-line descriptions both project to the opposite midpoint.

**2. Global entrance and recurrence.** Denote the scalar update by \(g\) off the midpoint. For \(t>1\), the first scalar update lies below \(1/2\), and for \(t<0\) it lies above \(1/2\). Consequently the following two-step identities hold with the line label returned to its original value:
\[
 T^2(i,t)=(i,t/4)\quad(t>1),\qquad
 T^2(i,t)=(i,(t+3)/4)\quad(t<0).
\]
Repeated application either reaches a marked endpoint or enters \((0,1)\) after finitely many steps: on the positive outer ray the coordinate is divided by four; on the negative outer ray the coordinate is transformed to \(1+(t-1)/4\) and moves toward one. Within \((0,1/2)\), the first branch is forward-invariant and contracts toward its unique scalar fixed point \(1/3\); within \((1/2,1)\), the second branch is forward-invariant and contracts toward \(2/3\). Every step in either invariant interval changes the line index by \(+1\) or \(-1\), respectively. Thus these two scalar fixed points yield exactly the stated two period-three cycles, with three-step transverse multiplier \(-1/8\). The three tie midpoints are fixed. No other periodic orbit is possible because all exterior orbits enter these sets or reach a tie.

**3. Complete basin boundary.** The only points in \([0,1]\) with a forward iterate equal to a midpoint are \(0\), \(1/2\), and \(1\). For a positive exterior coordinate, successive two-step renormalizations divide by four, so an orbit meets \(1\) or \(1/2\) exactly when its starting coordinate belongs to \(\{4^k,2\cdot4^k:k\ge0\}\). For a negative coordinate, the two-step iterate is \(1+(t-1)/4^j\) until entrance; solving for an eventual zero or midpoint gives precisely \(\{1-4^k,1-2\cdot4^k:k\ge0\}\) in the nonpositive range. Together with the midpoint, these are all and only the eventual fixed-point preimages, giving \(E\). In each connected interval of the complement of \(E\) the eventual scalar branch is constant, whereas immediately across each point of \(E\) the eventual branch differs. Thus \(E\) is exactly the common relative boundary of the two basins. The four geometric progressions have two branches in each unbounded direction on each supporting line, hence \(4\log_4 R+O(1)\) exceptional parameter values per line; accounting for three lines and only finitely many shared vertices gives \(12\log_4 R+O(1)\) physical points.

**4. Exact basin length and its oscillation.** On the positive oriented ray the \(C_-\) basin is exactly the disjoint union
\[
 (0,1/2)\ \cup\ \bigcup_{k\ge0}(4^k,2\cdot4^k).
\]
Indeed for \(t>1\), two-step renormalization \(t\mapsto t/4\) is repeated until the coordinate first reaches \((0,1)\); it reaches \((0,1/2)\) precisely in the displayed intervals, and \((1/2,1)\) in their complementary interstices. The length up to \(4^m\) is \(1/2+\sum_{k=0}^{m-1}4^k=4^m/3+1/6\). Adding the occupied part of the next interval gives the boxed exact formula. Writing \(R=4^m s\), \(1\le s<4\), yields
\[
 \frac{B_-(R)}R=
 \frac{1/3+\min\{s-1,1\}}s+\frac{1}{6R}.
\]
The continuous phase function increases from \(1/3\) at \(s=1\) to \(2/3\) at \(s=2\), then decreases to \(1/3\) as \(s\uparrow4\). Every phase can be sampled along \(R=4^m s\), proving the complete cluster interval and both sharp limits.

## Verification
Run `python3 verify_equilateral.py` with a standard Python 3 interpreter. Its exact rational geometry uses the embedded representation \((p,q)\leftrightarrow(p,\sqrt3q)\), so all squared distances, projections, and branch comparisons are computed with `fractions.Fraction` without floating-point comparisons. The checker compares \(46{,}839\) geometric transitions with the scalar formula, classifies \(15{,}613\) rational parameter states by two independent methods, checks the cycles and exceptional sequences, and compares \(4{,}788\) exact rational basin-length evaluations by independent interval summation. The checks passed. Infinite statements follow from the analytic four-step argument above, not from finite testing.

## Relationship to prior work
Everett introduced this farthest-orthogonal-projection triangle map and established qualitative asymptotic periodicity, including odd-period orientations. Its public full text does not give the exact global basin boundary for the equilateral three-line case or the sharp one-sided arclength oscillation. An accessible published mathematical result, *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map* (2026), gives sharp existence conditions for period-three cycles in arbitrary triangles. That result **already covers the existence and count** of the two equilateral period-three orbits here; it explicitly does not classify other periods, global basins, or their size distributions. The new assertion is the complete equilateral global basin decomposition and exact log-periodic density law, neither implied by the three-cycle existence inequalities. General theorems on piecewise contractions restrict periodic-orbit counts but do not evaluate this unbounded geometric model's basin fractions.

## Limitations
The formula concerns the original map on **three complete supporting lines** and exactly equilateral geometry; varying the triangle angles or clipping projections to finite edges changes the system. The nonconvergent density is for a *one-sided directed ray*: a symmetric cutoff about a side midpoint has basin fraction \(1/2\) by reflection symmetry, so no universal cutoff-independent density is claimed. The count of exceptional points uses side-length-normalized coordinates on each supporting line. Numerical checks are finite demonstrations, not substitutes for the proof. Historical originality cannot be certified from the examined literature alone.

## References
1. S. Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18** (2020), 183–192, DOI `10.1080/1726037X.2020.1847765`, first published online 2021-01-07. Public author preprint arXiv `2408.16019v1` (2024-08-26).
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published published-finding corpus record, 2026-10-11, identifier `2944d54e59d8` (the full theorem treats arbitrary triangles but not global attraction basins).
3. A. Nogueira and B. Pires, *Dynamics of piecewise contractions of the interval*, *Ergodic Theory and Dynamical Systems* **35** (2015), 2012 preprint arXiv `1206.5676v1`.
4. J. Wang and Y. Zhang, *A geometric iterated function system on triangles*, arXiv `1605.01794v1` (2016); its phase space is triangle moduli rather than the three supporting lines.
