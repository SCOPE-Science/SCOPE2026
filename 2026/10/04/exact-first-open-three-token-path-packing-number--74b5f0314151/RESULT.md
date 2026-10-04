# Exact first open three-token path packing number
## Finding
Let \(F_3(P_{13})\) be the graph whose vertices are the three-element subsets of \(\{1,\ldots,13\}\), with one edge for moving a single token by one step along the path without collision. Then
\[
\rho(F_3(P_{13}))=52.
\]
Equivalently, a binary code of length \(13\) and constant weight \(3\) that corrects one adjacent transposition has at most \(52\) codewords, and this bound is attained.

## Assumptions and scope
A packing set in a graph has pairwise graph distance greater than \(2\). Under the standard support-set representation of a binary constant-weight word, swapping an adjacent unequal pair moves exactly one token across one path edge. Thus correcting at most one adjacent transposition is equivalent to choosing centers whose radius-one balls are disjoint. The statement is only for length \(13\) and weight \(3\); it does not assert a formula for other lengths or weights.

## Proof
Write a vertex as an increasing triple \(a=(a_1,a_2,a_3)\). For two vertices \(a\) and \(b\),
\[
d(a,b)=\sum_{i=1}^3 |a_i-b_i|.
\]
Each token move changes the right-hand side by at most one, so it is a lower bound on path length. Conversely, move the ordered tokens monotonically from their positions in \(a\) to the corresponding ordered positions in \(b\), choosing an outermost token whenever a desired move would otherwise collide; the order of tokens is preserved and exactly the displayed number of unit moves suffices. Hence a packing is exactly a family of triples with pairwise displayed distance at least \(3\).

There are \(\binom{13}{3}=286\) triples. Form the conflict graph by joining two triples when their displayed distance is at most \(2\). Direct enumeration gives \(2255\) conflict edges. The embedded verifier solves the exact 0-1 program
\[
\max \sum_v x_v,\qquad x_u+x_v\le 1\quad(uv\text{ a conflict edge}),\qquad x_v\in\{0,1\}.
\]
Exhaustive branch-and-bound in HiGHS returns an optimal objective of \(52\) with zero MIP gap. This is a finite exhaustive upper-bound computation, not an extrapolation. The verifier also checks the following explicit 52-triple feasible set:

\((1,2,3)\), \((1,2,7)\), \((1,2,10)\), \((1,2,13)\), \((1,4,11)\), \((1,5,6)\), \((1,5,9)\), \((1,5,13)\), \((1,7,8)\), \((1,7,11)\), \((1,9,10)\), \((1,9,13)\), \((1,11,12)\), \((2,3,4)\), \((2,3,9)\), \((2,3,12)\), \((2,6,7)\), \((2,6,10)\), \((2,7,13)\), \((2,8,9)\), \((2,10,11)\), \((2,12,13)\), \((3,4,5)\), \((3,4,10)\), \((3,4,13)\), \((3,5,8)\), \((3,6,12)\), \((3,8,11)\), \((3,10,13)\), \((4,5,6)\), \((4,5,11)\), \((4,7,9)\), \((4,8,13)\), \((4,9,10)\), \((4,11,12)\), \((5,6,7)\), \((5,6,10)\), \((5,6,13)\), \((5,9,12)\), \((5,12,13)\), \((6,7,8)\), \((6,7,11)\), \((6,10,13)\), \((7,8,9)\), \((7,8,12)\), \((7,11,12)\), \((8,9,10)\), \((8,9,13)\), \((8,12,13)\), \((9,10,11)\), \((10,11,12)\), \((11,12,13)\).

Every two displayed triples have distance at least \(3\), proving the matching lower bound.

## Verification
Run `python3 verify.py` with Python, NumPy, and SciPy available. The script reconstructs all triples and conflict edges from the definitions, verifies the explicit witness pairwise, solves the integer program for \(n=13\), and independently reconstructs the same model for each \(3\le n\le12\). The resulting values \(1,2,3,6,9,13,18,24,32,41\) match Table 1 of Ndjatchi et al. before the new \(n=13\) value \(52\). The computation concerns a finite graph, so successful optimal termination establishes the finite upper bound; it supplies no asymptotic statement.

## Relationship to prior work
Gómez Soto, Leaños, Ríos-Castro, and Rivera define \(T(n,k)\) as the largest length-\(n\), constant-weight-\(k\) binary code correcting one adjacent transposition and identify the packing formulation; their work solves the weight-two column. Its first public arXiv version is dated 2017-11-10 and lists MSC 94B05 first among its subject classifications.

Ndjatchi et al. study the weight-three case directly. They determine \(\rho(F_3(P_n))\) exactly only through \(n=12\), and for \(n=13\) report lower and upper bounds \(50\) and \(54\), respectively; their conclusion explicitly leaves exact values for \(n>12\) open. The present value \(52\) closes the first missing length and lies strictly between both published bounds. The current OEIS entry A085684 identifies the same triangle \(T(n,k)\) but does not list a value for \(T(13,3)\).

## Limitations
The exact upper bound is computational and depends on a complete mixed-integer branch-and-bound solve of a 286-variable, 2255-constraint 0-1 model. The verifier makes the model and witness explicit and checks published smaller cases, but no short human-only upper-bound certificate is supplied. No claim is made about uniqueness of optimal codes, \(n=14\), or a general formula. A differently phrased or unindexed prior computation could still contain the same finite value.

## References
1. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro, L. M. Rivera, *The packing number of the double vertex graph of the path graph*, arXiv:1711.03682, first submitted 2017-11-10; Discrete Applied Mathematics 247 (2018), 327–340.
2. C. Ndjatchi et al., *On the packing number of \(3\)-token graph of the path graph \(P_n\)*, AIMS Mathematics 9(5) (2024), 11644–11659, doi:10.3934/math.2024571.
3. OEIS A085684, triangle \(T(n,k)\) of maximal one-transposition-correcting constant-weight binary codes.
