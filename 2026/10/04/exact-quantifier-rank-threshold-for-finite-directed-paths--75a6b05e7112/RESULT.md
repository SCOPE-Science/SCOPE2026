# Exact quantifier-rank threshold for finite directed paths
## Finding
Let \(\vec P_n\) have vertex set \(\{0,1,\ldots,n-1\}\) and successor relation \(S(i,j)\) exactly when \(j=i+1\). For every \(q\ge0\),
\[
\vec P_n\equiv_q\vec P_m
\quad\Longleftrightarrow\quad
q\le1\;\text{ or }\;n=m\;\text{ or }\;(q\ge2\text{ and }n,m\ge2^q).
\]
Thus, for \(1\le n<m\), the least distinguishing quantifier rank is
\[
\max\{2,\lfloor\log_2 n\rfloor+1\}.
\]

## Assumptions and scope
The language contains equality and one binary relation \(S\), with no order predicate, endpoint constants, or unary labels. Quantifier rank is ordinary first-order quantifier nesting depth. The claim concerns finite nonempty directed paths only.

## Proof
For \(q\le1\), every nonempty \(\vec P_n\) has the same rank-\(q\) theory: one selected vertex cannot expose a successor edge. Isomorphic paths are trivially equivalent.

For the lower bound when \(q\ge2\), forget the orientation and interpret undirected adjacency by the quantifier-free formula \(E(x,y):=S(x,y)\vee S(y,x)\). Brown and Hoshino prove a complete \(q\)-round classification for undirected paths: their threshold is \(f(1)=1\), \(f(2)=4\), \(f(3)=7\), and \(f(q)=2^q\) for \(q\ge4\), and whenever the smaller path has size below \(f(q)\), unequal sizes are distinguishable in \(q\) rounds. Therefore the directed paths are distinguishable for every \(n<m\) with \(n<2^q\), except that this reduction leaves the single boundary \((q,n)=(3,7)\). That boundary is finite: an exhaustive minimax traversal of the complete three-round game tree gives Spoiler a win on \(\vec P_7,\vec P_8\); `verify.cpp` checks this without pruning assumptions. Once the upper bound below gives \(\vec P_8\equiv_3\vec P_m\) for every \(m\ge8\), transitivity handles all \(m>7\).

For the upper bound at \(q=2\), after the first move classify the chosen vertex as source, sink, or interior. In every path of size at least \(4\), each class has the same one-move response profile: a source has a successor and a non-neighbour but no predecessor, a sink has the reversed profile, and an interior vertex has both predecessor and successor and also a non-neighbour. Matching the class therefore wins the second round.

For \(q=3\), paths of size at least \(8\) admit a direct two-move pointed classification after the first response. If a chosen vertex is at left distance \(0,1,2\), match that exact left distance; if it is at right distance \(0,1,2\), match that exact right distance; otherwise choose a vertex with at least three vertices on each side. With two rounds left, these seven pointed cases are complete: on the next move, directed offsets \(-2,-1,+1,+2\) are copied exactly, while any more distant move is matched by a non-neighbour with the same endpoint-side availability. The final move can then only test equality or one-step successor adjacency to one of the two selected vertices, which is preserved. Hence all \(n,m\ge8\) are rank-three equivalent.

For \(q\ge4\), use the path strategy of Brown--Hoshino with one strengthening. Their Lemma 3.6 and Theorem 3.7 maintain protected endpoint gaps and exact short distances, proving that all undirected paths of sizes at least \(2^q\) are \(q\)-equivalent. Coordinate both paths from source to sink. Whenever their strategy copies a short displacement, choose the response with the same signed displacement rather than merely the same absolute displacement; whenever it matches an endpoint gap, match the corresponding left or right endpoint gap. In the long-gap cases, their response is placed at a prescribed protected distance on one side of an already selected point; choose that same side in the second path. The inequalities establishing available room are unchanged by this signed choice. Inductively, every selected pair at directed distance one has images at the same signed distance one, while all equality constraints are unchanged. Thus their complete response construction is orientation-preserving and is a winning strategy for the successor relation as well. Therefore all \(n,m\ge2^q\) are rank-\(q\) equivalent.

Combining lower and upper bounds gives the classification. For unequal \(n<m\), the least \(q\ge2\) with \(n<2^q\) is \(\max\{2,\lfloor\log_2 n\rfloor+1\}\).

## Verification
`verify.cpp` independently solves the exact finite Ehrenfeucht--Fraisse game by minimax on partial bijections. It checks every pair \(1\le n\le m\le17\) for \(1\le q\le4\), comparing the game result with the theorem, and separately records the finite boundary \(\vec P_7\not\equiv_3\vec P_8\). The replay returns `VERIFY_OK cases=612 states=814707 boundary_7_8=spoiler`.

## Relationship to prior work
Brown--Hoshino give the complete result for undirected paths, with the exceptional three-round threshold \(7\) and the threshold \(2^q\) from rank \(4\) onward. The directed successor signature is not a notational restatement: orientation removes reflection as a legal local match, changing the three-round threshold from \(7\) to \(8\). Weis--Immerman study quantifier depth on words with two variables in the stronger signature containing both linear order and successor; that framework does not state the unrestricted first-order, successor-only classification above.

## Limitations
The orientation-preserving upper-bound argument is specific to a single consistently oriented path. It does not classify arbitrary orientations, disjoint unions, rooted trees, or signatures containing order or endpoint constants. The literature search found no prior statement of this exact directed threshold, but an unindexed textbook or folklore treatment remains a priority risk.

## References
1. Jason I. Brown and Richard Hoshino, “The Ehrenfeucht-Fraisse Game for Paths and Cycles,” Ars Combinatoria 83 (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Philipp Weis and Neil Immerman, “Structure Theorem and Strict Alternation Hierarchy for FO2 on Words,” ECCC TR07-008 (2007). https://eccc.weizmann.ac.il/report/2007/008/download
