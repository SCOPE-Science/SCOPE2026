# Exact quadrilateral enclosure of the midpoint-truncated affine-regular pentagon

## Finding

For the canonical convex hexagon \(H\) obtained by cutting one vertex off an affine-regular pentagon along the segment joining the midpoints of its two incident sides, the least area of any convex quadrilateral containing \(H\) is
\[
q(H)=2+\frac{3\sqrt5}{4}.
\]
Its area and normalized enclosure ratio are
\[
|H|=\frac94+\frac{\sqrt5}{2},\qquad
\frac{q(H)}{|H|}=\frac{42+11\sqrt5}{61}.
\]
The exact absolute area excess is \((\sqrt5-1)/4\). The normalized conclusion is affine invariant and therefore applies to every affine image of the canonical midpoint-truncation.

## Assumptions and scope

Put \(\varphi=(1+\sqrt5)/2\). In counterclockwise cyclic order, the vertices of \(H\) are
\[
(-\tfrac12,\tfrac12),\quad(-1,0),\quad(1-\varphi,-\varphi),\quad
(\varphi-1,-\varphi),\quad(1,0),\quad(\tfrac12,\tfrac12).
\]
The untruncated pentagon obtained by replacing the first and last vertices with \((0,1)\) is affine regular. Here \(q(K)\) means the infimum of ordinary Euclidean areas of convex quadrilaterals containing \(K\); allowing triangular degenerations does not affect the stated value.

Define the pentagonal core
\[
P=\operatorname{conv}\{(0,\tfrac12),(-1,0),(1-\varphi,-\varphi),
(\varphi-1,-\varphi),(1,0)\}.
\]
Because the new apex is the midpoint of the top horizontal side of \(H\), \(P\subset H\).

## Proof

**Upper bound.** Consider the intersection of the four halfplanes
\[
y\le \tfrac12,\quad y\ge-\varphi,\quad
-\varphi x+(\varphi-2)y\le\varphi,\quad
\varphi x+(\varphi-2)y\le\varphi.
\]
This is a bounded isosceles trapezoid \(Q\) containing all six vertices of \(H\). Its horizontal sections have endpoints on the two sloping lines. Direct evaluation gives
\[
|Q|=(\varphi+\tfrac12)\bigl(\varphi+\tfrac1{2\varphi^3}\bigr)
=2+\frac{3\sqrt5}{4}.
\]

**Lower bound.** It is enough to establish \(q(P)\ge |Q|\), since \(P\subset H\). We invoke DePano's classical extremal-side lemma, as reproduced and used in Hong–Ismailescu–Kwak–Park: a minimum-area enclosing quadrilateral of a convex pentagon can be selected so that at least three of its sides contain original pentagon edges, and the midpoint of each enclosing side belongs to the pentagon. The proper-quadrilateral case applies here; a triangle containing a strict convex pentagon cannot be optimal because a corner can be clipped.

Write the five supporting edge lines of \(P\) as \(n_i\cdot z\le h_i\), for \(i=0,\ldots,4\), in cyclic edge order. Their coefficients are
\[
\begin{array}{c|c|c}
i&n_i&h_i\\\hline
0&(-\tfrac12,1)&\tfrac12\\
1&(-\varphi,\varphi-2)&\varphi\\
2&(0,-1)&\varphi\\
3&(\varphi,\varphi-2)&\varphi\\
4&(\tfrac12,1)&\tfrac12
\end{array}
\]
Fix any three distinct original edge lines of the minimizing quadrilateral. If the fourth side contains a pentagon edge, it is one of the two omitted edge lines. Otherwise it supports a pentagon vertex \(v\), which must be the midpoint of the segment cut out by that fourth line. If the two neighboring fixed lines are \(n_i\cdot z=h_i\) and \(n_j\cdot z=h_j\), put \(\delta_i=h_i-n_i\cdot v\) and \(\delta_j=h_j-n_j\cdot v\). Solving for the two endpoints with midpoint \(v\) shows that the fourth supporting normal must be proportional to
\[
\pm(\delta_j n_i+\delta_i n_j).
\]
Indeed, if those endpoints are \(v+w\) and \(v-w\), then \(n_i\cdot w=\delta_i\), \(n_j\cdot w=-\delta_j\), and the displayed vector is perpendicular to \(w\). This enumerates all possible side configurations.

There are \(\binom53\bigl(2+\binom32\cdot5\cdot2\bigr)=320\) algebraic candidates: 20 edge-contact instances and 300 vertex-midpoint instances (repetition is intentional). The standalone program `verify_midpoint_truncation.py` constructs them in \(\mathbb Q(\sqrt5)\), discards zero/incorrectly oriented normals, non-supporting lines, unbounded or infeasible polygons, and compares all surviving exact shoelace areas to \(2+3\sqrt5/4\). Exactly 35 candidates are feasible, none has smaller area, and one enumerated candidate attains equality: fixed side indices \((1,2,3)\), supporting the apex vertex \((0,1/2)\) with the fourth side. This finishes the lower bound, and hence \(q(P)=q(H)=|Q|\).

Finally the shoelace formula gives \(|H|=9/4+\sqrt5/2\). Division and rationalization give the claimed ratio. All area ratios remain invariant under nonsingular affine maps.

## Verification

Run `python verify_midpoint_truncation.py` from the directory containing this manuscript and the supplied source file, with SymPy installed. The program reports `VERIFY_OK` and the candidate counts `total=320`, `valid=35`, `equal=1`, using exact algebraic-field computations for every acceptance and comparison predicate. Approximate floating point values are used solely to choose a cyclic ordering of four normal directions; exact cross-product and halfplane inequalities subsequently verify the chosen geometry. The script is a finite exhaustion justified by the cited three-edge/midpoint structural lemma, not a sampled approximation to an infinite configuration space.

## Relationship to prior work

Hong, Ismailescu, Kwak and Park establish the sharp universal \(3/\sqrt5\) quadrilateral enclosure factor for all pentagons and state DePano's extremal-side/midpoint lemma; they do not provide the above exact minimum for the canonical six-vertex truncation. Fodor and Grundbacher establish an improved universal factor below \(\sqrt2\) for general convex bodies. Neither universal upper estimate implies the present exact six-vertex enclosure, for which a lower bound is also necessary. The constants \(3/\sqrt5\) and the DePano structural lemma are prior results, not new claims here.

## Limitations

The theorem concerns one natural affine equivalence class: midpoint truncation of one vertex of an affine-regular pentagon. It does not give an all-parameter truncation profile, a new universal enclosure bound, or the resolution of Kuperberg's conjecture. The exhaustive certificate depends on the validity of DePano's structural lemma as stated in the cited source. An earlier unindexed exact calculation of this same benchmark remains a possible originality risk.

## References

1. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185 (first public version June 5, 2025). https://arxiv.org/abs/2506.05185
2. E. Hong, D. Ismailescu, A. Kwak, and G. Y. Park, *On the smallest area (n−1)-gon containing a convex n-gon*, arXiv:2108.00326 (2021), Lemma 2.1 and Section 3. https://arxiv.org/abs/2108.00326
3. J. DePano, extremal-side lemma for minimum circumscribed polygons, as stated and attributed in Reference 2, Lemma 2.1.
