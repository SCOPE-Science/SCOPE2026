# The first information-bound failures for edge-conjunction Littlestone dimension

## Finding

For a finite simple graph \(G=(V,E)\) with at least one edge, consider the hypothesis class \(\mathcal H_G=\{h_e:e\in E\}\) on the domain of all vertex subsets \(U\subseteq V\), where \(h_e(U)=1\) precisely when both endpoints of \(e\) belong to \(U\). If \(|V|\le7\), then
\[
\operatorname{Ldim}(\mathcal H_G)=\lfloor\log_2|E|\rfloor
\]
with exactly two isomorphism-type exceptions: the graph obtained by attaching one leaf to \(K_6\), and the graph obtained by subdividing one edge of \(K_6\). Both have seven vertices and sixteen edges, and both have Littlestone dimension three rather than four. Among the \(2^{21}\) labeled simple graphs on seven fixed vertices, exactly 147 fail the information bound: 42 of the leaf-attachment type and 105 of the subdivision type. Thus seven is the smallest graph order with a failure, and sixteen is the only failing edge count at order at most seven.

## Assumptions and scope

Graphs are undirected, finite, simple, and may have isolated vertices. An edge hypothesis is a monotone two-variable conjunction, with other conjunctions excluded unless their corresponding edge is present. Every subset of vertices is a legal query, with a fixed edge returning its two-endpoint containment bit. No graph with more than seven vertices is classified here. A concept class with exactly one hypothesis has Littlestone dimension zero. The standard information upper bound is \(\operatorname{Ldim}(\mathcal H_G)\le\lfloor\log_2|E|\rfloor\), since distinct full branches require distinct hypotheses.

## Proof

**Exact finite recurrence.** Fix seven labeled vertices, with their 21 potential edges enumerated lexicographically. Encode every possible nonempty edge hypothesis set \(F\) as a nonzero 21-bit integer mask \(v\). For a query \(U\subseteq[7]\), let \(Q(U)\) be the 21-bit mask of all edges with both endpoints in \(U\). The positive version space is \(v\mathbin{\&}Q(U)\) and the negative version space is \(v\setminus Q(U)\). Put \(D(v)=0\) when \(|v|=1\); for larger nonempty \(v\), use
\[
D(v)=\max_{U:\,0<|v\cap Q(U)|<|v|}\bigl(1+\min\{D(v\cap Q(U)),D(v\setminus Q(U))\}\bigr),
\]
where an empty maximum is zero. This recurrence follows exactly from the definition of a shattered complete binary decision tree: to shatter depth \(t+1\), one root query must leave both labeled branches able to shatter depth \(t\). Both strict branch masks are smaller positive integers than \(v\), so evaluating \(D(v)\) in numerical mask order is an induction, not a heuristic search. The zero mask is never used as a child of a split.

**Complete finite exhaustion.** The companion `verify_all.cpp` constructs every one of the 128 possible vertex query masks, computes the above recurrence for every integer \(v\) from 1 through \(2^{21}-1\) in increasing order, and counts precisely those for which \(D(v)<\lfloor\log_2|v|\rfloor\). It includes every one of the 2,097,151 nonempty labeled graphs on seven vertices, without sampling, isomorphism-library reliance, or unexamined subcases. The recorded output reports exactly 147 failing masks, all of size sixteen and with \(D=3\). Since any graph on fewer vertices is obtained on the seven-vertex label set by adding isolated vertices, and since queries involving isolated vertices do not change hypotheses, this also establishes the lower-order part of the claim.

**Identification of both types.** Attaching a leaf to a six-vertex clique gives exactly \(7\cdot6=42\) distinct labeled graphs. Subdividing an edge of a six-vertex clique gives exactly \(7\binom62=105\) distinct labeled graphs. They are disjoint because the first has a degree-one vertex while the second has a degree-two vertex and no degree-one vertex. All 147 masks lack any eight-edge induced subgraph, as verified independently by enumerating all 128 vertex subsets in `check_types.py`. In a sixteen-hypothesis class, a shattered tree of depth four would require the root query to divide the sixteen hypotheses into precisely eight on each side. Thus every graph in either family has dimension at most three; both attain dimension three by the complete recurrence. Since there are 147 such explicit, pairwise distinct failed graphs and the exhaustive algorithm found only 147 failed graphs, they constitute all exceptions. The independent checker additionally confirms that the exact set of failing masks equals the union of the two constructed families.

## Verification

Compile with `g++ -O3 -std=c++17 verify_all.cpp -o verify_all`, run `./verify_all > verification_output.txt`, then run `python3 check_types.py` from the directory containing these files. `verify_all.cpp` performs the entire recurrence without nonstandard libraries; the second checker independently constructs the two exceptional families, checks their sizes and absence of eight-edge induced subgraphs, and compares them with the exhaustive list. The captured transcript begins with `states=2097152 labeled_nonempty=2097151 failures=147` and reports `edge_count=16 failed=147`. The independent checker prints `TWO_TYPES_CONFIRMED 42 105 147`.

## Relationship to prior work

The general definition of Littlestone dimension and its learning-theoretic motivation are standard. Ghazi, Golowich, Kumar and Manurangsi's 2020 preprint studies closure bounds for Littlestone and threshold dimensions, but its propositions concern bounds under aggregations of hypothesis classes rather than this exact first finite obstruction. A separate vertex-induced-edge range-system result concerns the **primal VC dimension** of sets \(E(G[U])\); that system is dual to the present edge-indexed query system, and its VC classification does not imply the exact adaptive dimension calculated here. The result here is therefore a finite exact classification of a different invariant, not a consequence of either cited theorem.

## Limitations

The complete classification is restricted to graphs on at most seven vertices. It supplies no formula for larger arbitrary graphs, no asymptotic theorem, and no independent formal proof assistant certification. The exhaustive finite proof depends on the correctness of the displayed recurrence, the small C++ implementation and its successful full execution; the separate Python checker tests the structural identification, not the entire dynamic program. Historical priority beyond the inspected publications is not guaranteed.

## References

1. Badih Ghazi, Noah Golowich, Ravi Kumar and Pasin Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, arXiv:2007.03668 (first public version 2020-07-07); PMLR 132 (2021), pp. 686–696. https://arxiv.org/abs/2007.03668 ; https://proceedings.mlr.press/v132/ghazi21a.html
2. Earlier vertex-induced-edge range-system classification (distinct primal VC-dimension problem); opaque reference ID `a4739d45-a19b-43c6-b908-bb2d6f583d10`. Its prior VC statement is not reproduced or certified here.
