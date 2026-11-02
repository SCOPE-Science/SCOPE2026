# Five three-round theories of planar rectangular grid graphs

## Finding

Let \(P_t\) be the ordinary undirected path on \(t\) vertices. For integers \(2\le m\le n\), let \(G_{m,n}=P_m\square P_n\), the uncoloured Cartesian grid graph. The language contains only equality and undirected adjacency. Write \(\equiv_r\) for agreement on all first-order sentences of quantifier rank at most \(r\).

**Theorem.** All the graphs \(G_{m,n}\) are equivalent at rank two. At rank three there are exactly five classes, represented by
\[
G_{2,2},\quad G_{2,3},\quad G_{2,4},\quad G_{3,3},\quad G_{2,5}.
\]
More explicitly, define \(c(m,n)\) to be I, II, III, or IV when \((m,n)\) is respectively \((2,2),(2,3),(2,4),(3,3)\), and V for every other \(2\le m\le n\). Then
\[
G_{m,n}\equiv_3 G_{p,q}\quad\Longleftrightarrow\quad c(m,n)=c(p,q),
\]
where both parameter pairs are sorted increasingly. In particular, \(G_{2,5}\equiv_3 G_{3,4}\), and indeed every grid of the fifth class is rank-three equivalent to both of these graphs. The smallest representative of the fifth class has ten vertices. Accordingly **ten is the sharp uniform representative bound within this two-dimensional grid family**.

## Assumptions and scope

The graphs are simple, undirected and loopless. Both path factors have at least two vertices, and the only relation in the language is ordinary (uncoloured) adjacency; no boundary, coordinate, order, distance or counting predicates are named. The theorem concerns quantifier rank rather than an unrestricted variable-width logic. It makes no claim about quantifier rank four or higher.

## Proof

### Exact three-round logical-profile recurrence

For an ordered pair \((u,v)\) of vertices of a finite simple graph, its **one-step pair profile** records (i) equality and adjacency of \(u,v\) and (ii), for each \((a,b)\in\{0,1\}^2\), whether a third vertex \(w\notin\{u,v\}\) exists with \(E(u,w)=a\) and \(E(v,w)=b\). When \(u=v\), the same definition uses the resulting restricted diagonal patterns. Two ordered pairs have identical profiles exactly when their equality/adjacency pattern is identical and Duplicator can match every possible final move in either graph.

Write \(\tau(u,v)\) for the profile, \(\sigma(u)=\{\tau(u,v):v\in V\}\), and \(\Theta(G)=\{\sigma(u):u\in V\}\). Back-and-forth induction shows
\[
G\equiv_3 H\quad\Longleftrightarrow\quad\Theta(G)=\Theta(H).
\]
Indeed, after the first move corresponding vertices must have the same possible one-step pair profiles for every response to the second move; this is necessary and sufficient for a matching third move. The sets rather than multisets are appropriate because ordinary first-order logic without counting does not demand multiple witnesses of the same profile. Equality cases are retained explicitly, so repeated choices are included.

### Exhaustive pair-profile geometry

Write coordinates as \((i,j)\), with \(0\le i<m\), \(0\le j<n\). The distance is Manhattan distance, \(d((i,j),(i',j'))=|i-i'|+|j-j'|\). Every vertex has degree between two and four. There are no triangles. Two distinct vertices have a common neighbour if and only if their distance is two. They then have exactly one common neighbour if their displacement is two steps along one axis, and two if their displacement is one step along each axis.

The following names exhaust all pair profiles across the family. In each displayed four-bit pattern the bits refer, in order, to existence of a third vertex adjacent to both, adjacent only to the first, adjacent only to the second, and adjacent to neither; previously chosen vertices are excluded.

| Code | Pair condition | Four bits |
| --- | --- | --- |
| D | Equal endpoints; a different neighbour and nonneighbour exist | Diagonal case |
| E0 | Adjacent endpoints; no vertex nonadjacent to both | 0,1,1,0 |
| E1 | Adjacent endpoints; some vertex nonadjacent to both | 0,1,1,1 |
| K | Opposite vertices of the four-cycle \(G_{2,2}\) | 1,0,0,0 |
| F | Nonadjacent at distance two, each has an exclusive neighbour | 1,1,1,1 |
| G | Nonadjacent at distance two, the first has no exclusive neighbour | 1,0,1,1 |
| H | Nonadjacent at distance two, the second has no exclusive neighbour | 1,1,0,1 |
| I0 | Nonadjacent at distance at least three; no vertex nonadjacent to both | 0,1,1,0 |
| I1 | Nonadjacent at distance at least three; some vertex nonadjacent to both | 0,1,1,1 |

The equality/adjacency bit distinguishes E0 from I0 and E1 from I1. A pair of adjacent vertices has an exclusive neighbour on each side since every vertex has degree at least two and the grid is triangle-free.

For a distance-two pair, the number of common neighbours is one or two. Thus the first vertex lacks an exclusive neighbour exactly when its degree is two and the two common neighbours exhaust its neighbourhood. Degree two occurs exactly at corners, and the two-common-neighbour case is precisely diagonal opposition within a unit square. The same holds after reversing the pair. Both vertices can lack exclusive neighbours simultaneously only in \(G_{2,2}\), giving K. Every distance-two pair in a larger grid has a third vertex nonadjacent to both.

For completeness, here is an all-parameter check of the last nonadjacency assertion and its distance-at-least-three analogue. If \(mn\ge11\), at most eight vertices are in the union of the neighbourhoods of two distinct vertices, while \(mn-2\ge9\) vertices remain after deleting the endpoints; therefore a third vertex nonadjacent to both exists. The remaining grids with \(mn\ge8\) are \(G_{2,4},G_{3,3},G_{2,5}\). In \(G_{2,5}\), degree at most three makes the neighbour union at most six, below the eight other vertices. In \(G_{3,3}\), a nonadjacent pair cannot consist of a degree-four centre and a degree-three side vertex, since those are adjacent; all nonadjacent pairs have neighbour-union size at most six, below the seven other vertices. In \(G_{2,4}\), a nonadjacent pair of degree-three vertices is necessarily a diagonal pair in the two interior columns; its two common neighbours reduce the union to four, while all other nonadjacent pairs have total degree at most five, below the six other vertices. For adjacent pairs in all these grids, after excluding the endpoints each has at most three remaining neighbours, and in the only eight-vertex case each has at most two. The same nonneighbour conclusion follows.

The smaller grids can be checked directly from their coordinates: in \(G_{2,2}\), every edge has E0 and every opposite pair has K; in \(G_{2,3}\), the central rung has E0, the opposite-corner distance-three pairs have I0, and every other applicable pair has the ordinary codes above. For all remaining grids every adjacent pair has E1 and every distance-at-least-three pair has I1.

### Complete one-point profile table

Put
\[
A=\{D,E1,F,G,I1\},\quad
B=\{D,E1,F,H,I1\},\quad
C=\{D,E1,F,I1\}.
\]
Using the geometry just established, the complete rank-two pointed profiles, and hence the rank-three unpointed theories, are:

| Grid parameter range | The set \(\Theta(G_{m,n})\) |
| --- | --- |
| \((m,n)=(2,2)\) | \(\{\{D,E0,K\}\}\) |
| \((m,n)=(2,3)\) | \(\{\{D,E1,F,G,I0\},\{D,E0,E1,H\}\}\) |
| \((m,n)=(2,4)\) | \(\{A,B\}\) |
| \((m,n)=(3,3)\) | \(\{A,\{D,E1,H\},C\}\) |
| All other \(2\le m\le n\) | \(\{A,B,C\}\) |

Here is a direct coordinate derivation of the infinite last row, avoiding extrapolation. For \(m=2,n\ge5\), the corners have A, the noncorner vertices in columns \(1\) and \(n-2\) have B, and those in columns \(2,\ldots,n-3\) have C. The latter range is nonempty, including column \(2\) when \(n=5\). All these vertices have a distance-two straight counterpart (code F), and a vertex at distance at least three (code I1); the corner-diagonal asymmetry gives G or H exactly as indicated.

For \(m\ge3,n\ge4\), the four corners have A; vertices diagonally opposite at least one corner across a unit square have B; all remaining vertices have C. Every vertex has a distance-two straight counterpart because \(n\ge4\), and eccentricity is at least \(\lceil(m-1)/2\rceil+\lceil(n-1)/2\rceil\ge3\), giving I1. Corner-diagonal asymmetry is the only source of G or H. All three types occur: a corner, \((1,1)\), and \((0,1)\) are representatives of A, B, and C respectively. For \(G_{3,3}\), the centre is the only corner-diagonal vertex, but it has eccentricity two and no straight distance-two counterpart, yielding \(\{D,E1,H\}\); the corners give A and the four side-centres give C. The two small ladder cases follow by examining their columns as recorded in the table.

The five sets in the table are pairwise distinct. By the exact recurrence, this proves the asserted five classes and the equivalence \(G_{2,5}\equiv_3G_{3,4}\). Their smallest graph orders are respectively \(4,6,8,9,10\), so ten is the sharp ceiling. Finally, every vertex in every grid has both a neighbour and a distinct nonneighbour, and both adjacent and distinct nonadjacent pairs exist. The same two-round back-and-forth profile therefore holds throughout the family, proving universal rank-two equivalence.

## Verification

Two standalone scripts reproduce the result using different representations. `verify_profiles.py` directly enumerates the existence pattern of all third vertices for each ordered pair and compares the resulting pointed-profile sets with the entire five-class table. It checks all \(66\) unordered parameter pairs \(2\le m\le n\le12\). `verify_recursive.py` computes complete atomic-diagram types by an unreduced quantifier-rank recursion, without using the geometric pair-code table; it checks \(27\) rectangular grids including the five minimal representatives and the \(8\)-by-\(8\) grid. Both independently return PASS. Invoke each with Python 3 from a directory containing the corresponding file. Their complete checked outputs are included as text files. These computations support the boundary cases; the infinite theorem is proved by the preceding coordinate argument.

## Relationship to prior work

Pikhurko, Veith and Verbitsky (2003, arXiv:math/0311041) develop the finite-graph quantifier-rank and game machinery, including general graph-definability bounds, but not the present exact five-class planar-grid calculation in the inspected abstract, contents, and relevant game section. Verbitsky (2004, arXiv:math/0401361) proves asymptotic definability bounds for graph families with separators, rather than bounded-depth equivalence classes of Cartesian grids. Brown and Hoshino (2007) classify Ehrenfeucht–Fraïssé games on single paths and cycles, not Cartesian products of two paths. The distinction matters: the thin grid \(G_{2,5}\) and the thicker grid \(G_{3,4}\) agree at rank three although they have different vertex degrees and numbers of squares.

The formula's non-counting extension signatures do not claim independence from the general Ehrenfeucht–Fraïssé equivalence theorem; the contribution is the exact parameter classification and its sharp minimal representative bound for the natural two-factor grid family. Earlier logical classifications of products of at least three paths do not imply this two-factor result: they exclude dimension two and have different extension profiles. Exact historical priority beyond the inspected material remains open.

## Limitations

This is a statement about pure adjacency in two-dimensional finite rectangular grids with both side lengths at least two. It is not a classification of arbitrarily many Cartesian path factors, one-dimensional paths, rectangular order posets, graph signatures with named coordinates, counting logic, or rank-four theories. No claim of independent mathematical verification or exhaustive historical-priority search is made.

## References

1. O. Pikhurko, H. Veith, O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041, first posted 2003-11-04. https://arxiv.org/abs/math/0311041
2. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361, first posted 2004-01-26. https://arxiv.org/abs/math/0401361
3. J. Brown and R. Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/
