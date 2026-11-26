# The seven rank-three theories of cycle-square graphs

## Finding
Let \(G_n=C_n^2\) for every integer \(n\ge3\): distinct residues modulo \(n\) are adjacent exactly when their cyclic distance is one or two. In first-order logic with equality and adjacency only,
\[
G_m\equiv_3G_n\quad\Longleftrightarrow\quad
(3\le m,n\le5)\;\lor\;(m=n\in\{6,7,8,9,10\})\;\lor\;(m,n\ge11).
\]
Here \(\equiv_3\) means agreement on all sentences of quantifier rank at most three. Thus there are exactly seven theories and the sharp stabilization threshold is eleven vertices.

## Assumptions and scope
The graphs are simple and undirected. There are no named vertices, order or counting predicates. Equality allows repeated choices in the Ehrenfeucht–Fraïssé game. We compare members of this family, not general graphs, and make no rank-four originality claim.

## Proof
For an ordered pair \((a,b)\), its one-round type is determined by the equality and adjacency of the pair and by the set of atomic diagrams obtained by appending one vertex. Appending a previously chosen vertex gives diagrams already determined by the pair. By the usual back-and-forth induction, two pointed graphs are equivalent for two more rounds exactly when their sets of one-round pair types agree. Since every \(G_n\) is vertex-transitive, two graphs are three-round equivalent exactly when these sets agree at a single choice of first vertex in each graph. This use of sets, not multiplicities, follows directly from the two-way requirement to match each possible move.

For a distinct pair write \(e=1\) when they are adjacent and \(e=0\) otherwise. Write \(C,X,N\) for the three Boolean flags indicating the existence of a third, distinct vertex adjacent to both, just to the first, or to neither, respectively. The condition “just to the second” has the same flag as “just to the first,” since the cyclic reflection \(x\mapsto a+b-x\) interchanges the pair. The pair type is therefore specified by \(e\) and the three bits \(CXN\). For \(n\ge6\), the repeated pair contributes a single additional type, the same for all these sizes: there are vertices adjacent and nonadjacent to the common vertex, as well as that vertex itself.

For \(n\ge6\), take the distinct pair to be \(0,d\), with \(1\le d\le\lfloor n/2\rfloor\). Put \(D=\{-2,-1,1,2\}\) and \(c_n(d)=|D\cap(d+D)|\), with the sets read modulo \(n\). The numbers of third vertices corresponding to the flags \(C,X,N\) are, respectively,
\[
c_n(d),\qquad 4-e-c_n(d),\qquad n-10+2e+c_n(d).
\]
Indeed, the sets of neighbours of the two vertices, restricted to the remaining vertices, each have size \(4-e\) and have intersection size \(c_n(d)\). The flags record positivity of these three numbers. To compute the intersection, count ordered differences of elements of \(D\) congruent to \(d\) modulo \(n\). The positive differences \(1,2,3,4\) have multiplicities \(2,1,2,1\), respectively; negative differences have the same multiplicities. The resulting sets of flag strings are:

| \(n\) | Adjacent pair, \(e=1\) | Nonadjacent distinct pair, \(e=0\) |
|---|---|---|
| 6 | 110 | 100 |
| 7 | 110, 111 | 110 |
| 8 | 111 | 110 |
| 9 | 111 | 110, 111 |
| 10 | 111 | 010, 111 |
| \(\ge11\) | 111 | 011, 111 |

For the last row, \(n-d\ge6\), so no negative difference is congruent to \(d\). The common-neighbour counts for \(d=1,2,3,4\) are then \(2,1,2,1\), and for every \(d\ge5\) the count is zero. All the nonadjacent entries claimed in that row exist: \(d=3\) gives 111 and \(d=5\) gives 011. The six rows have different ordered pairs of sets. Finally, the graphs on three through five vertices are complete. In three rounds a newly chosen vertex always has an unused match in any of these complete graphs, and a repeated choice is matched by the same repeat. None is equivalent to a member with \(n\ge6\), which has a distinct nonadjacent pair observable in two rounds. This proves the classification.

## Verification
The table is determined by the four difference multiplicities and the three displayed counts. In particular its unbounded row follows directly from the difference support, not from extrapolating a finite enumeration.

## Relationship to prior work and limitations
Brown and Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, study the ordinary cycle, not its square. As quoted in *Fifteen four-round theories of cycle-square graphs*, their ordinary-cycle theorem gives an upper bound of eleven for stabilization at rank three after interpreting squared adjacency by a formula of rank one. This does not give the distinctions among sizes below eleven or establish sharpness at rank three. The related [rank-four classification for \(n\ge5\)](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-fifteen-four-round-theories-of-cycle-square-graphs--13c2bba94a62) concerns a different rank; its statements of rank-four inequivalence do not determine rank-three inequivalence. The exact contribution here is the lower-rank partition, including its sharp boundary. No historical priority claim beyond the checked comparisons, nor any general formula for higher ranks or larger powers, is made.
