# Exact color-refinement depth of tadpole graphs

## Finding
Let \(T_{m,k}\) be the simple graph formed from a cycle \(C_m\), \(m\ge3\), by joining a distinguished cycle vertex \(q\) to the first vertex of a path \(p_1,\ldots,p_k\), where \(k\ge1\). There are \(m+k\) vertices. Start ordinary one-dimensional color refinement from the uniform vertex coloring, and let \(\operatorname{Stab}(G)\) be the least \(s\ge0\) such that rounds \(s\) and \(s+1\) induce the same partition. Then
\[
\boxed{\operatorname{Stab}(T_{m,k})=
\max\left\{\left\lfloor\frac m2\right\rfloor,
\left\lceil\frac k2\right\rceil,\min\{m,k\}\right\}.}
\]
The first term is the cycle-distance refinement scale, the second comes from the two endpoints of the tail, and the third records the delayed distinction between a cycle neighbor of \(q\) and \(p_1\). The latter pair first receives different colors at round \(\min(m,k)\).

For fixed order \(N=m+k\), the exact maximum over admissible \(m,k\) is
\[
\boxed{\max_{\substack{m+k=N\\m\ge3,k\ge1}}
\operatorname{Stab}(T_{m,k})=
\begin{cases}1,&N=4,\\\lfloor N/2\rfloor,&N\ge5.\end{cases}}
\]
For \(N=5\), the admissible graph \(T_{3,2}\) attains the maximum \(2\). For every \(N\ge6\), the admissible balanced choice \(m=\lfloor N/2\rfloor\), \(k=\lceil N/2\rceil\) attains \(\lfloor N/2\rfloor\). No balanced choice with \(m=\lfloor N/2\rfloor\) is admissible at \(N=5\), because a cycle has at least three vertices.

## Definitions, hypotheses, and scope
Every graph is finite, simple, undirected, and uncolored initially. Round zero is uniform; round \(r+1\) assigns to each vertex its previous color together with the multiset of previous colors of its neighbors. Stabilization means equality of color *partitions*, rather than numerical equality of arbitrary color labels. The parameter \(k\) is the number of path vertices **outside** the cycle; thus the bridge is the edge \(qp_1\). The statement concerns refinement of one graph, not distinguishing two graphs by a disjoint-union refinement or higher-dimensional Weisfeiler--Leman.

The eventual stable partition consists of the singleton attachment vertex \(q\), the \(k\) singleton tail vertices, and the reflection orbits of the cycle fixing \(q\). Thus two cycle vertices are equivalent precisely when their distances from \(q\) coincide.

## Proof
Use the standard universal-cover description of color refinement: the round-\(r\) color of a vertex is determined exactly by the isomorphism type of its depth-\(r\) rooted universal-cover tree. For the tadpole, the universal cover consists of a bi-infinite degree-two spine with degree-three vertices at consecutive distance \(m\), each such vertex bearing a pendant path of length \(k\) ending at a degree-one leaf. The two directions on the spine are exchanged by reflection. A finite-radius rooted neighborhood records the first appearance of a branch or leaf event in each direction, so comparisons below are comparisons of rooted tree types, not merely vertex degrees.

**Cycle positions.** The lift of a cycle vertex at distance \(d\) from \(q\), with \(1\le d\le\lfloor m/2\rfloor\), lies between its nearest two degree-three spine vertices at distances \(d\) and \(m-d\). Distinct \(d\)'s eventually give distinct rooted types; their successive distance waves separate them by round \(\lfloor m/2\rfloor\). The deepest pair of different distance classes (or the initial degree distinction for \(m=3\)) witnesses the corresponding lower bound. Reflection-equivalent vertices remain equivalent at every round.

**Tail positions.** Along the pendant path, its two ends are identifiable respectively by the degree-three attachment at \(q\) and the degree-one leaf \(p_k\). At round \(r\), these two distinguishing waves have advanced \(r\) levels. Positions not yet reached from either end have identical rooted truncations; each newly reached position becomes distinguishable from the remaining middle positions. All tail vertices separate within \(\lceil k/2\rceil\) rounds, and the central pair or initial endpoint distinction witnesses that this scale cannot generally be dropped from the maximum.

**Cycle versus tail.** The cycle neighbor \(c_1\) of \(q\) and \(p_1\) each have the same degree-two rooted arrangement near the same degree-three attachment vertex. In the direction away from \(q\), the cycle spine first displays the next branching vertex after the prescribed \(m\)-edge cycle interval, while the tail first displays a leaf at the end of its prescribed \(k\)-edge path. Before round \(\min(m,k)\), these two rooted truncations coincide; at that round one encounters the first distinguishing endpoint or branch (both events are different if simultaneous). Thus the pair first splits exactly at round \(\min(m,k)\).

Other cycle-tail pairs are separated no later. Indeed, differing distances from \(q\) are detected by the ordinary attachment-distance waves. For equal positive distance \(i\), the two roots compare the same local degree-two intervals as \(c_1,p_1\), but shortened by \(i-1\) along the directions leading back to the attachment; their remaining endpoint/branch discrepancy therefore occurs no later than \(\min(m,k)-i+1\), or earlier when a leaf or branch enters a truncated neighborhood. Together with the cycle and tail separation bounds, this gives the displayed upper bound. The three witness mechanisms give the matching lower bound. Once these rooted types are resolved, no subsequent round can further split a stable reflection orbit, so this is the precise stabilization time.

For the fixed-order assertion, put \(N=m+k\). For \(N\ge5\), each of \(\lfloor m/2\rfloor\), \(\lceil k/2\rceil\), and \(\min(m,k)\) is at most \(\lfloor N/2\rfloor\), using \(m\le N-1\) and \(k\le N-3\). At \(N=5\), \(T_{3,2}\) attains 2 by the formula. At \(N\ge6\), \(m=\lfloor N/2\rfloor\ge3\) and \(k=\lceil N/2\rceil\ge1\) are admissible and make the third term equal \(\lfloor N/2\rfloor\). Finally, \(N=4\) admits only \(T_{3,1}\), which stabilizes in one round.

## Verification and proof limitations
A direct standard-library implementation of partition-based color refinement independently checked every \(3\le m\le26\), \(1\le k\le38\), both the exact stabilization formula and the \(c_1,p_1\) separation time (912 parameter pairs). In particular \(T_{3,2}\) has depth 2, whereas the formally balanced pair \((2,3)\) is not an admissible tadpole. The repository's own checker reports a larger finite regression range. Finite tests are only corroboration: all-parameter assertions rely on the rooted universal-cover comparison above. No claim is made for arbitrary unicyclic graphs or nonuniform initial colors.

## Relationship to prior work
Krebs and Verbitsky identify color-refinement rounds with finite-depth universal-cover types and establish strong general depth bounds. Kiefer and McKay's analysis of iteration numbers gives extremal results for general graph families but does not imply the exact three-term formula for this bridged cycle-and-tail family from its inspected theorems. DeMaio and Jacobson study exact invariants of the same tadpole graphs, not refinement depths. The present result isolates the additional cycle-versus-tail scale and gives a complete natural family classification, not a general worst-case theorem. Equivalent earlier results under a different family name remain a bounded originality risk.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175; LICS 2015.
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI 10.4230/LIPIcs.ICALP.2020.73.
3. J. DeMaio and J. Jacobson, *Fibonacci number of the tadpole graph*, Electronic Journal of Graph Theory and Applications 2(2) (2014), 129--138, DOI 10.5614/ejgta.2014.2.2.5.
