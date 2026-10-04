# Exact logical depth of complete multipartite graphs via a threshold path
## Finding
Let \(G\) be a finite nonempty complete multipartite graph. Write its distinct part sizes as \(1\le d_1<\cdots<d_t\), with multiplicities \(m_i\), put \(d_0=0\), \(R_i=\sum_{h=i}^t m_h\), \(A_i=R_i+d_{i-1}+1\) for \(1\le i\le t\), \(A_{t+1}=0\), and \(B_i=d_i+m_i+1\). For an integer \(q\ge d_t+1\), form two directed paths on vertices \(1,\ldots,t+1\). In the upper path, vertex \(i\) is a source when \(A_i\le q\); an edge \(i\leftrightarrow i+1\) is bidirectional when \(B_i\le q\), and is directed \(i\to i+1\) when \(B_i=q+1\). In the lower path, vertex \(i\) is a source when \(A_i\le q+1\); the same edge is bidirectional when \(B_i\le q\), and is directed \(i+1\to i\) when \(B_i=q+1\). Edges with \(B_i\ge q+2\) are absent. Then the ordinary first-order logical depth \(D(G)\) is exactly the least \(q\ge d_t+1\) for which every vertex is reachable from a source in both paths. This criterion is linear-time in the number of distinct part sizes. In particular, \(D(K_{s,\ldots,s})=\max\{r,s\}+1\) for the complete \(r\)-partite graph with equal part size \(s\), and \(D(K_{a,b})=b+1\) for \(1\le a\le b\) except \(D(K_{1,1})=3\).

## Assumptions and scope
Graphs are finite, nonempty, simple, and undirected, in the first-order language with equality and adjacency. The logical depth \(D(G)\) is the minimum quantifier rank of a sentence defining \(G\) up to isomorphism among all finite graphs. A complete multipartite graph is specified by its multiset of nonempty independent-part sizes.

## Proof
Put \(F(x,y)\) for \(x=y\) or nonadjacency. On a complete multipartite graph, \(F\) is exactly the equivalence relation whose classes are the parts, and adjacency is quantifier-free definable back from \(F\). Hence quantifier-rank equivalence for complete multipartite graphs is the same as for finite equivalence relations with the same class-size multisets.

For a finite equivalence relation \(M\), let \(N_k(M)\) be the number of classes of size at least \(k\), and let \(C_k(M)\) be the number of classes of size exactly \(k\). A direct Ehrenfeucht--Fraisse argument gives the rank-\(q\) criterion
\[
\minigl(N_k(M),q-k+1igr)\quad(1\le k\le q),
\qquad
\minigl(C_k(M),q-kigr)\quad(1\le k<q),
\]
which must agree termwise for two structures, and these equalities are also sufficient. Necessity follows because rank \(q\) can demand \(r\) distinct classes of size at least \(k\) exactly up to \(r+k-1\le q\), and \(r\) distinct classes of size exactly \(k\) exactly up to \(r+k\le q\). For sufficiency, after \(j\) moves Duplicator pairs touched classes so that either their full sizes agree or each has at least \(q-j\) unused elements; the two triangular truncation families guarantee a fresh compatible class whenever Spoiler first enters a new one.

Now fix the target part multiset. Any defining rank must satisfy \(q\ge d_t+1\), since at rank at most \(d_t\) one may enlarge a largest part without changing the visible profile. For \(q\ge d_t+1\), every rank-\(q\)-equivalent competitor also has no class larger than \(d_t\).

Between consecutive distinct sizes, the cumulative class count is constant. Let \(x_i\) be the difference between the competitor's cumulative count and \(R_i\) on the plateau \(d_{i-1}<k\le d_i\), and put \(x_{t+1}=0\). The triangular profile reduces exactly to local constraints on this path. Plateau \(i\) is pinned to \(x_i=0\) when \(A_i\le q\); when \(A_i=q+1\) it gives the tight one-sided constraint \(x_i\ge0\); with \(A_i\ge q+2\) it has at least one unit of slack. Likewise the multiplicity jump at \(d_i\) gives \(x_i=x_{i+1}\) when \(B_i\le q\), the tight inequality \(x_i\ge x_{i+1}\) when \(B_i=q+1\), and at least one unit of slack when \(B_i\ge q+2\).

Thus the target is uniquely determined at rank \(q\) exactly when every \(x_i\) is forced both above and below by zero. Upper bounds propagate from pinned vertices through exact edges in both directions and through tight edges from left to right; this is precisely reachability in the upper path. Lower bounds propagate from pinned or tight plateau vertices through exact edges in both directions and through tight edges from right to left; this is precisely reachability in the lower path. If a vertex fails either reachability test, changing by one all vertices in the corresponding unpinned region respects every slack constraint and produces a different part multiset with the same rank-\(q\) profile. Conversely, if both tests reach every vertex, all \(x_i\) are zero, so no competitor exists. This proves the criterion.

For equal part size \(s\) and multiplicity \(r\), the path has one jump and the criterion reduces to \(q\ge s+1\) and \(q\ge r+1\), giving \(D=\max\{r,s\}+1\). For two parts of sizes \(a\le b\), the same criterion gives \(D=b+1\), except that the two-vertex complete graph requires rank \(3\).

## Verification
The accompanying `verify.py` performs two independent finite checks. First, a direct recursive Ehrenfeucht--Fraisse solver is compared with the triangular profile criterion for every pair of integer partitions of orders at most six and ranks at most three. Second, the threshold-path criterion is compared with exhaustive same-profile uniqueness over bounded canonical class-count vectors for targets of maximum class size at most four and ranks up to six. It also checks the uniform and two-part corollaries over small parameter ranges. The recorded output is `VERIFY_OK ef_cases=1305 criterion_cases=469 uniform=36 biclique=20`.

## Relationship to prior work
Pikhurko, Veith, and Verbitsky introduced and studied the graph logical-depth parameter and developed general upper bounds using similarity classes. Their 2003 preprint treats arbitrary graphs and binary structures, but a full-text search of the inspected version found no occurrence of “multipartite”; its similarity-class machinery gives broad bounds rather than the exact part-multiplicity criterion above. Tenney's 1975 paper uses Ehrenfeucht games for a single equivalence relation in a second-order decidability argument, providing historical context for class-size compression, but it does not state this graph logical-depth classification.

## Limitations
The theorem concerns ordinary first-order logic without counting quantifiers and only complete multipartite graphs (equivalently, complements of cluster graphs). The path rule is an exact combinatorial criterion rather than a single closed scalar formula for arbitrary heterogeneous part-size multisets. The literature search did not locate a prior statement of this criterion, but unindexed folklore or an exercise-level treatment of finite equivalence relations remains a priority risk.

## References
1. O. Pikhurko, H. Veith, and O. Verbitsky, “The First Order Definability of Graphs: Upper Bounds for Quantifier Rank,” arXiv:math/0311041, first submitted 4 November 2003.
2. R. L. Tenney, “Second-order Ehrenfeucht games and the decidability of the second-order theory of an equivalence relation,” Journal of the Australian Mathematical Society 20 (1975), 323–331, DOI 10.1017/S1446788700020681.
