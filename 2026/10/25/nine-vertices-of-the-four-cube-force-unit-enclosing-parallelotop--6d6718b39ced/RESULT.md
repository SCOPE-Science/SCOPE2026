# Nine vertices of the four-cube force unit enclosing parallelotope volume

## Finding
Let \(Q=[0,1]^4\). Every full-dimensional four-dimensional parallelotope \(P\subset\mathbb R^4\) containing at least nine distinct vertices of \(Q\) satisfies
\[
\operatorname{vol}_4(P)\ge 1.
\]
Both the volume constant and the vertex-count threshold are sharp. The unit cube attains volume one while containing sixteen vertices. With only eight vertices the volume can be arbitrarily small: the parallelotope \([0,1]^3\times[0,\varepsilon]\) contains the eight vertices of \([0,1]^3\times\{0\}\) and has volume \(\varepsilon>0\).

Equivalently, for each nine-element subset \(S\subset\{0,1\}^4\), put
\[
W_S=\{y\in\mathbb R^4:\langle y,s-t\rangle\le 1\text{ for all }s,t\in S\}.
\]
Then the sharp determinant bound is
\[
\max_{y_1,\ldots,y_4\in W_S}\left|\det\begin{pmatrix}y_1^{\mathsf T}\\y_2^{\mathsf T}\\y_3^{\mathsf T}\\y_4^{\mathsf T}\end{pmatrix}\right|=1.
\]

## Assumptions and scope
A parallelotope means a translate of \(A[0,1]^4\) for an arbitrary invertible real \(4\times4\) matrix \(A\); no integrality, orthogonality, or containment inside \(Q\) is assumed. Volume is ordinary four-dimensional Euclidean measure. The vertices are exactly the sixteen points in \(\{0,1\}^4\); nine may be chosen in any configuration. The assertion is a volume lower bound only, not an integer-lattice covering theorem.

## Proof
**1. Compact width polars.** Fix any nine-element \(S\). In each of the four coordinate directions, the sixteen cube vertices form eight disjoint pairs differing by a standard basis vector. Since \(|S|=9\), some complete pair belongs to \(S\) in each direction. Thus both \(e_i\) and \(-e_i\) belong to \(S-S\), giving \(|y_i|\le1\) for every \(y\in W_S\). Hence \(W_S\) is a compact full-dimensional convex polytope (the origin strictly satisfies all defining inequalities).

**2. From enclosure to determinants.** Write \(P=c+A[0,1]^4\) with \(A\) invertible and let \(B=A^{-1}\). If \(S\subseteq P\), every row \(b_i\) of \(B\) varies by at most one on \(S\), because \(B(P-c)=[0,1]^4\). Thus \(b_i\in W_S\). The identity \(\operatorname{vol}_4(P)=|\det A|=1/|\det B|\) reduces the desired bound to \(|\det(b_1,b_2,b_3,b_4)|\le1\) for four arbitrary rows in \(W_S\).

**3. Reduction to finitely many vertices.** The determinant is linear in each row, so its maximum absolute value over the compact polytope \(W_S\) in each argument is attained at vertices. Repeating for all four arguments shows that it suffices to check four-tuples of vertices of \(W_S\). Repeated vertices give determinant zero, so only distinct four-tuples matter.

**4. Exact finite lemma.** The attached plain-Python checker and rational table prove the following finite assertion, with no floating-point computations:

> Under the \(2^4\cdot4!=384\) signed coordinate-permutation symmetries of the four-cube, the \(\binom{16}{9}=11440\) nine-element subsets form exactly 56 orbits. For every representative \(S\), its rational width polytope \(W_S\) is exactly the convex hull of the vertices listed in `cube9_width_polars.json`; and every determinant of four listed vertices has absolute value at most one, with equality achieved.

The verification of the purported vertex sets does **not** assume that a polytope-enumeration routine found every vertex. It checks each listed rational vertex against every defining width inequality, verifies full affine dimension, and examines all affinely independent quadruples of listed vertices that support the listed convex hull. Every supporting facet equation coincides with one of the original width inequalities. Consequently the listed hull contains the intersection of *all* original width halfspaces, while feasibility supplies the reverse inclusion; the hull is exactly \(W_S\). The checker then exhausts all four-row determinants by exact integer operations after clearing denominators. No numerical approximation or sampling enters the final certificate: every checked predicate is an integer equality or inequality. The exact test totals are stated below.

Cube symmetries preserve both determinants up to sign and the nine-vertex incidence problem. Therefore the finite lemma gives the determinant bound for every nine-element subset, proving the volume inequality. A parallelotope containing more than nine vertices contains some nine-element subset, so the same conclusion applies.

**5. Sharpness.** The unit cube has volume one. The thin-facet example in the Finding establishes that eight vertices cannot force any positive universal volume bound.

## Verification
From a directory containing the two accompanying artifacts, run `python verify_cube9.py` with Python 3's standard library. It exhaustively regenerates the 56 orbit representatives and accounts for all 11440 nine-vertex subsets; it confirms the exact inequality representation of 1066 candidate vertices; checks 11812 supporting-quadruple incidences; and verifies 290663 determinant quadruples. Its final line starts with `FOUR_CUBE_NINE_VERTEX_VOLUME_OK` and reports `max_det=1`. The maximum number of width-polar vertices in one orbit is 28, and every certificate denominator divides 6.

The enumeration is finite and exhaustive, not an inference from a sample. The mathematical reduction to this exact finite assertion is proved above, independently of the implementation. All integer determinants fit in the checker language's arbitrary-precision integer arithmetic.

## Relationship to prior work
Grozev and Nikolov, *Lattice coverings by parallelotopes containing cube vertices* (first posted 15 October 2026), show that five cube vertices suffice for covering in dimension three, and in all dimensions obtain covering when a parallelotope contains an entire cube facet together with one vertex from the opposite facet. They pose the unrestricted majority-of-vertices covering question. Their covering theorem yields a volume lower bound for the particular facet-plus-vertex configurations, but it does not cover arbitrary nine-element subsets of the four-cube. For example, the eight even-Hamming-weight corners together with \((1,0,0,0)\) contain no entire three-dimensional cube facet. The present finite theorem provides the universal **necessary volume bound** in the first dimension outside their complete low-dimensional covering result; it does not resolve their covering question.

The determinant-width reformulation is an elementary tool used here, not claimed as a novel method. Exact minimal-enclosing-parallelotope computations exist for other configurations; the specific all-nine-subset statement was not found in the inspected accessible literature or research records. This search does not establish global historical priority.

## Limitations
The theorem does not assert \(P+\mathbb Z^4=\mathbb R^4\), does not address ambient dimensions five or higher, and does not classify the equality parallelotopes. The finite certificate is specifically four-dimensional. Priority relative to unpublished or unindexed results remains uncertain. This is exact computer-assisted finite verification supported by a mathematical reduction, not an independently audited result.

## References
Grozev, D., and Nikolov, N. (2026), *Lattice coverings by parallelotopes containing cube vertices*, arXiv:2610.21572v1, https://arxiv.org/abs/2610.21572 (initial submission 15 October 2026).
