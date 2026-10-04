# Same-model review

## Correctness
PASS. The proof exhausts all possibilities according to whether a lower source point hits a target maximum, whether an upper source point hits a target minimum, or the map preserves the two ranks. In the rank-preserving case, the decisive crown fact is that for \(n\ge3\), a set of at least two target minima has a common upper neighbor only when it is exactly the two lower neighbors of one target maximum. The four disjoint counts are \(n(3^p-2^p)\), \(n(3^q-2^q)\), \(n2^q\), and \(n(2^p-2)\), whose sum is \(n(3^p+3^q-2)\). In each case the map is pointwise comparable with an explicit constant map, so finite-space homotopy follows from the standard pointwise-comparability criterion. The sharp \(n=2\) boundary follows from minimal-core rigidity.

The verifier independently enumerates all direct maps for \(27\) parameter triples with \(1\le p,q\le3\) and \(3\le n\le5\), verifies both the count and a comparable constant for every map, and checks the four-point boundary. This is a finite stress test rather than a substitute for the proof.

## Originality
PASS with a stated bibliographic residual risk. published-finding corpus searches for complete bipartite height-two sources, crowns, homotopy, and order-preserving maps returned no equivalent finding. The closest literature inspected in full is Farley's enumeration of maps whose sources and targets are fences or crowns; complete height-two spaces \(P_{p,q}\) are outside that source class except when \(p=q=2\). Barmak--Minian supply the finite-model framework, while May supplies the function-space and pointwise-homotopy criteria; neither source states or implies the count or the all-null direct-map conclusion. Searches for the exact expression \(n(3^p+3^q-2)\) produced no mathematical match.

Residual risk: the formula is elementary enough that it may exist as an unindexed exercise or observation in order-enumeration literature. No inspected source covers the same parameterized statement or its homotopy consequence.

## Value
PASS. The result gives a complete, closed-form direct-map census and a sharp representability obstruction between two natural families of finite models of graphs. The source order complex has first Betti number \((p-1)(q-1)\), while the target crown models a circle, so classical topology permits many nontrivial maps; nevertheless every direct finite-space map to any crown of length at least six is null-homotopic. The sharp failure at the four-point crown isolates exactly where direct finite representatives begin to exist. This is structural information about how model geometry constrains maps, not a routine recomputation of a known table.

## Closest literature and limitations
Barmak--Minian (arXiv:math/0611156v1) give the finite-space/order framework and minimal graph models. May's finite-space notes give the mapping-space pointwise order and the homotopy criterion for comparable maps. Farley, DOI 10.1007/BF01108588, enumerates maps among fences and crowns but does not cover general complete height-two sources. The finding does not address subdivided-source representatives or the full homotopy type of the mapping space.

Same-model review: passed. Independent audit: not yet performed.
