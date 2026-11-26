# Exact three-variable counting depth of finite paths

## Finding

Let \(P_n\) be the finite simple undirected path on \(n\ge 1\) vertices. Let \(D^3_{\#}(P_n)\) be the least quantifier depth of a counting first-order sentence using at most three variables and defining \(P_n\) up to isomorphism. Then
\[
D^3_{\#}(P_1)=1,\qquad
D^3_{\#}(P_n)=2+\left\lfloor\log_2\left(\frac{n+1}{3}\right)\right\rfloor\quad(n\ge2).
\]

More precisely, let \(H=P_m\mathbin{\dot\cup} C_{c_1}\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_{c_t}\) have the same order as \(P_n\), with \(m\ge2\), \(t\ge1\), and each \(c_i\ge3\). Put \(c=\min_i c_i\). The first round distinguishing their diagonal color multisets in ordered-pair 2-WL is
\[
r(P_n,H)=\min\{\lfloor\log_2(m+2)\rfloor,\ 1+\lfloor\log_2(c-1)\rfloor\}.
\]

## Assumptions and scope

All graphs are finite, simple, undirected, and uncolored. Ordered-pair 2-WL starts at round zero with equality, edge, and nonedge colors. At each subsequent round a pair retains its old color and records the multiset of ordered color pairs through every intermediate vertex of its graph. Colors are encoded consistently across the graphs being compared. A counting quantifier contributes one to depth regardless of its threshold.

## Proof

Write \(d_r=2^r\), \(a_r=d_r-1\), and take the distance between distinct components to be infinite. For \(s\ge1\) we show that the diagonal multisets of \(P_n,H\) agree in round \(s\) exactly when
\[
m\ge 2a_s=2^{s+1}-2,
\qquad c_i\ge 2d_{s-1}+1=2^s+1\quad(1\le i\le t).
\tag{1}
\]

**Sufficiency.** The type of a vertex at scale \(r\) is the unordered pair of its two distances along the path to its endpoints, each clipped at \(a_r\). A cycle vertex has type \((a_r,a_r)\). If (1) holds, the two graphs have the same vertex-type histogram at every scale \(r\le s\): each layer indexed by \(0\le j<a_r\) contributes two vertices of type \((j,a_r)\), and the other \(n-2a_r\) vertices have type \((a_r,a_r)\).

For \(0\le r\le s-1\), use the following pair descriptors. When the pair is farther apart than \(d_r\), store a far flag and the two unordered vertex types, in pair order. Otherwise store the distance and the two directed endpoint-distance pairs clipped at \(a_r\) in a common chart along the shortest path from the first vertex to the second. At a coincident pair either orientation can be used, with simultaneous reversal identified. For cycle vertices all directed endpoint distances are treated as infinite; the short arc is unique since each cycle has length at least \(2d_r+1\). These descriptors determine the round-\(r\) color in both graphs. At \(r=0\) this is just the atomic color.

For the induction, with \(d=d_{r-1}\), classify intermediate vertices according as they lie within distance \(d\) of the first vertex, the second, both or neither. A radius-\(d\) list about either anchor is a list of offsets on its chart, truncated at any endpoint. The directed clips at scale \(r\) suffice to give each listed vertex's directed clips at scale \(r-1\): shifting by at most \(d\) uses information only out to \(d+a_{r-1}=a_r\). If the anchors are farther than \(2d=d_r\), the two lists are disjoint and each can be generated using just its own type, with either choice of reflection. If the anchors are close, the charts are aligned by the stored distance. List overlap and distances in the overlap are determined by this alignment: on a cycle, an intersection using the other arc would give a second route between the anchors of length at most \(2d\), impossible since the cycle length is at least \(4d+1\) for \(r\le s-1\). For a coincident pair the lists are the same. Thus each offset in the union gives both old descriptors (a far descriptor uses just the two vertex types). Outside the union both descriptors are far, and the needed multiplicity of each intermediate type is its scale-\((r-1)\) histogram count minus the occurrences in the union. This determines the entire refinement multiset. The old color is also determined, since the scale-\(r\) data specialize to the old descriptor.

For the round-\(s\) diagonal step we need only coincident pairs. Exactly the same list computation now uses one radius-\(d_{s-1}\) chart, with distinct offsets on any cycle because its length exceeds \(2d_{s-1}\). Consequently the round-\(s\) diagonal color is a common function of the scale-\(s\) vertex type and the preceding histogram. Equality of the histograms proves the desired equality of color multisets.

**Necessity.** In any of these graphs a round-\(r\) pair color reveals the distance when it is at most \(d_r\), and otherwise reports that it is larger. Indeed, minimize the sum of the two recorded distances through an intermediate vertex, using only terms in which both distances were recorded at scale \(r-1\). A shortest path of length at most \(2d_{r-1}\) has a midpoint of this kind. From round one, a pair color also reveals the degree of each anchor by counting the initial edge occurrences. More generally it gives the distance of each anchor to the nearest degree-one vertex clipped at \(a_r\). For \(r=1\) this is exactly the degree-one test. At the next step minimize the distance to an intermediate vertex plus its recorded distance to the nearest degree-one vertex, using distances to the intermediate at most \(d_{r-1}\) and endpoint distances strictly below \(a_{r-1}\); cap the result at \(a_r\). Whenever the true endpoint distance is less than \(a_r=d_{r-1}+a_{r-1}\), a vertex on a shortest path to an endpoint realizes it in the allowed ranges. If none does, the clipped result is \(a_r\).

The number of diagonals with a recorded endpoint distance below \(a_s\) is \(\min(m,2a_s)\) in \(H\), versus \(\min(n,2a_s)\) in \(P_n\). These differ if \(m<2a_s\), since \(n>m\). If some cycle has length at most \(2d_{s-1}\), necessarily \(s\ge2\). The round-\(s\) diagonal at a vertex of that cycle counts at most \(2d_{s-1}\) vertices within distance \(d_{s-1}\) and none of degree one there, by the pair-color information at round \(s-1\). No path vertex has that combination: if its ball does not contain an endpoint, the ball has exactly \(2d_{s-1}+1\) vertices. This proves (1).

Since round zero agrees, the largest surviving round for this pair is the minimum of \(\lfloor\log_2(m+2)\rfloor-1\) and \(\lfloor\log_2(c-1)\rfloor\), and the first distinguishing round is one greater. This gives the stated pairwise formula.

For the defining depth, the Pikhurko–Verbitsky correspondence [1, Lemma 4.3] says that equality of the round-\(s\) diagonal multisets is equivalent to Duplicator surviving \(s+1\) rounds of the three-pebble counting game. Thus the minimum sentence depth for distinguishing a rival whose first diagonal difference is at round \(R\) is \(R+1\). Different orders are separated by a depth-one order sentence. Once the order is fixed, only finitely many rivals exist up to isomorphism, so conjoining their distinguishing sentences does not increase the maximum depth.

For \(n\ge2\), a same-order round-one survivor has exactly two degree-one vertices and all others of degree two. The classification of connected graphs of maximum degree two forces one path component and possibly cycles; nonisomorphism forces at least one cycle. By (1), such a rival survives round \(s\ge1\) only if \(n\ge3\cdot2^s-1\). Conversely the rival with one path on \(2^{s+1}-2\) vertices and one cycle on the remaining vertices works at every such \(n\). At \(s=0\) every same-order graph agrees, and at least one nonisomorphic same-order graph exists for \(n\ge2\). Hence the latest surviving round is \(\lfloor\log_2((n+1)/3)\rfloor\), and its first distinguishing round and the counting correspondence contribute one further round each. For \(P_1\), order alone defines the graph at depth one, whereas a quantifier-free sentence in the graph language cannot distinguish graph orders.

## Verification

The bundled `artifacts/verify.py` checks the pairwise formula on 390 path-plus-cycles decompositions for \(5\le n\le18\), then checks an extremal witness for each \(19\le n\le40\). The recorded output is `VERIFY_OK decompositions=390 exhaustive_n=5..18 extremal_n=19..40`. These are finite regression checks; the descriptor and census arguments prove the result uniformly.

## Relationship to prior work and limitations

Pikhurko and Verbitsky [1] record the counting-game correspondence and an upper bound of depth less than \(\log_2 n+3\) for ordinary three-variable first-order definitions of paths. They do not state the exact counting depth. Lichter, Ponomarenko, and Schweitzer [2] study general 2-WL iteration bounds. Neither an ordinary first-order upper bound nor single-graph stabilization yields the first round of diagonal distinction against the hardest nonisomorphic rival. The census argument relies on paths and cycles and is not a result for general trees. Targeted literature checks cannot exclude an unindexed occurrence of the exact threshold.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (2010).
2. M. Lichter, I. Ponomarenko, and P. Schweitzer, *Walk refinement, walk logic, and the iteration number of the Weisfeiler-Leman algorithm*, arXiv:1905.03008 (2019).
