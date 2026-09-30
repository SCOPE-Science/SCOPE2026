# Exact first-order saturation for a triangle plus two disjoint edges
## Finding
Let \(H=K_3\cup 2K_2\), and let \(\operatorname{sat}(n,H)\) denote the minimum number of edges in an \(n\)-vertex finite simple graph that is \(H\)-free but becomes \(H\)-containing after every single missing edge is added. Then
\[
\operatorname{sat}(7,H)=9,\qquad \operatorname{sat}(8,H)=10.
\]
Up to isomorphism, the \(7\)-vertex extremal graph is unique: it is obtained from \(K_4\) by subdividing exactly the three edges incident to one fixed vertex once each.

Up to isomorphism, there are exactly two \(8\)-vertex extremal graphs. Type A is \(K_4\) with one pendant leaf attached to each of its four vertices. Type B starts from \(K_4-e\); attach one pendant leaf to each of its two degree-three vertices, and join its two nonadjacent degree-two vertices by an internally vertex-disjoint path of length three.

There are exactly \(840\) labeled \(7\)-vertex extremal graphs and \(11760\) labeled \(8\)-vertex extremal graphs. The two \(8\)-vertex isomorphism classes have labeled orbit sizes \(1680\) and \(10080\), respectively.

## Assumptions and scope
All graphs are finite, simple, and undirected. Containment means ordinary subgraph containment, not induced containment. Saturation means that every nonedge, when added individually, creates at least one copy of \(H\). The result is exact only for orders \(7\) and \(8\); no claim is made here for \(n\ge 9\).

## Proof
The proof is a complete finite enumeration.

For \(n=7\), there are \(\binom{7}{2}=21\) possible edges. Every copy of \(H\) is spanning. Such a copy is specified by choosing its triangle and then one of the three perfect matchings on the remaining four vertices, giving
\[
\binom{7}{3}\cdot 3=105
\]
distinct labeled edge sets for \(H\). The verifier enumerates every graph with at most \(9\) edges, rejects graphs containing one of these \(105\) copies, and for every remaining nonedge checks that adding it completes at least one copy of \(H\). It finds no saturated graph with at most \(8\) edges and exactly \(840\) saturated graphs with \(9\) edges.

A representative of the claimed \(7\)-vertex type has automorphism group of order \(6\), hence labeled orbit size
\[
\frac{7!}{6}=840.
\]
Because the exhaustive enumeration also finds exactly \(840\) labeled extremal graphs, every extremal graph lies in that single orbit.

For \(n=8\), a copy of \(H\) uses exactly seven vertices. It is therefore specified by choosing the omitted vertex, the triangle on the remaining seven vertices, and one of the three perfect matchings on the remaining four vertices. Thus the verifier constructs exactly
\[
8\binom{7}{3}\cdot 3=840
\]
labeled \(H\)-copies. It exhaustively enumerates every graph with at most \(10\) edges, finds no saturated graph with at most \(9\) edges, and finds exactly \(11760\) saturated graphs with \(10\) edges.

For Type A, the automorphism group has order \(24\), so its labeled orbit has size
\[
\frac{8!}{24}=1680.
\]
For Type B, the automorphism group has order \(4\), so its labeled orbit has size
\[
\frac{8!}{4}=10080.
\]
Their degree sequences are different:
\[
(1,1,1,1,4,4,4,4)
\]
for Type A and
\[
(1,1,2,2,3,3,4,4)
\]
for Type B, so the two graphs are not isomorphic. Since
\[
1680+10080=11760,
\]
their two orbits account for every labeled \(8\)-vertex extremal graph.

The primary verifier, `verify.cpp`, uses explicit \(H\)-copy masks and completion witnesses. A second implementation, `crosscheck.cpp`, independently detects whether a newly added edge can play either the triangle-edge role or one of the two isolated-edge roles in \(H\); it reproduces the same extremal counts.

## Verification
Compile and run the two supplied C++17 programs. The primary program verifies the lower bounds, labeled counts, automorphism orders, orbit sizes, and degree-sequence separation. The cross-check program independently re-enumerates all candidate edge counts up to the claimed minima using a different containment test.

A successful primary run ends with `VERIFY_OK`. A successful cross-check run ends with `CROSSCHECK_OK`.

## Relationship to prior work
Lin, He, and Xu study saturation for unions of three cliques and prove exact saturation numbers and unique extremal graphs for \(K_p\cup K_q\cup K_r\) in the regime \(2\le p\le q<r<p+q\) when \(n\) is sufficiently large. Their parameter choice \(p=q=2\), \(r=3\) is exactly \(H=K_3\cup 2K_2\). The present result addresses the first two admissible graph orders and gives complete extremal classifications there; it does not modify the sufficiently-large-\(n\) theorem.

## Limitations
The proof is computational rather than a human structural proof. It is exhaustive for the stated orders, but it gives no direct formula or classification for \(n\ge 9\). The originality claim is best-of-knowledge and depends on targeted literature and published-finding corpus searches rather than a formally complete bibliography of all unpublished or inaccessible work.

## References
Hanlai Lin, Zhen He, and Yiduo Xu, “A note on the saturation number for unions of three cliques,” arXiv:2608.00459v1, first submitted 2026-08-01, primary MSC2020 \(05C35\).
