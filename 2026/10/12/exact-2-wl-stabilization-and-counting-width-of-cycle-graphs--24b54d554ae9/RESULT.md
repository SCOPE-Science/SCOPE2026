# Exact 2-WL stabilization and counting width of cycle graphs

## Finding
Let \(C_n\) be the finite simple undirected cycle on \(n\ge3\) vertices. Start standard two-dimensional Weisfeiler--Leman refinement from the atomic coloring of ordered pairs into equality, adjacency, and nonadjacency, and let \(\operatorname{Stab}^2(C_n)\) be the least number of refinement rounds after which the pair-color partition is stable. Then
\[
\operatorname{Stab}^2(C_n)=
\begin{cases}
0,&3\le n\le5,\\
\left\lceil\log_2\!\left(\left\lfloor n/2\right\rfloor-1\right)\right\rceil,&n\ge6.
\end{cases}
\]

More precisely, put \(D=\lfloor n/2\rfloor\). After round \(r\), as long as refinement has not already stabilized, ordered-pair colors depend only on the undirected distance \(d\) in the cycle: the distance classes
\[
0,1,\ldots,\min(2^r,D)
\]
have pairwise distinct colors, while every remaining distance \(2^r+1,\ldots,D\), when there is more than one, has one common far color. Hence stabilization occurs exactly when \(D\le 2^r+1\).

If \(W_{\#}(G)\) denotes the minimum number of variables in first-order logic with counting quantifiers needed to define \(G\) up to isomorphism, then
\[
W_{\#}(C_n)=
\begin{cases}
2,&3\le n\le5,\\
3,&n\ge6.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and uncolored. The 2-WL convention is the classical ordered-pair refinement in which round zero is the atomic pair coloring and each subsequent color records the previous color together with the multiset of color pairs obtained by inserting a third vertex. Stabilization counts only refinement rounds after round zero. Counting width is the standard finite-model-theory variable-width parameter with arbitrary counting quantifiers.

## Proof
By the dihedral automorphism group of \(C_n\), the color of an ordered pair \((u,v)\) in every round depends only on the undirected distance \(d(u,v)\). At round zero, distances \(0\) and \(1\) are distinguished, and all distances at least \(2\) share the nonedge color.

We prove the stated distance profile by induction. Suppose after round \(r\) all distances at most \(R=2^r\) are individually colored and all larger distances share one far color. Consider a pair at distance \(d\). The next refinement records, over all intermediate vertices \(w\), the multiset of ordered pairs of old colors corresponding to \((u,w)\) and \((w,v)\).

If \(d\le2R\), a shortest \(u\)-\(v\) arc contains an intermediate vertex \(w\) with exact distances \(a=d(u,w)\le R\) and \(b=d(w,v)\le R\) satisfying \(a+b=d\). Thus the multiset contains an exact--exact color pair encoding a decomposition whose sum is \(d\). Distinct new distances in \(R+1,\ldots,2R\) therefore receive distinct colors, while previously separated distances remain separated because refinement never merges colors.

If \(d>2R\), no intermediate vertex can be within distance \(R\) of both endpoints, by the triangle inequality. For each exact distance \(a\le R\) from one endpoint, the corresponding vertices are still farther than \(R\) from the other endpoint; consequently the counts of exact--far and far--exact color pairs are independent of \(d\), and the far--far count is the remaining total. Hence all distances above \(2R\) remain in one color class. This proves the doubling profile.

Let \(D=\lfloor n/2\rfloor\). If \(D\ge R+2\), the current far class contains at least two distance classes, and the next round separates distance \(R+1\) from larger distances, so the coloring is not stable. If \(D\le R+1\), every distance class already has its own color: either there is no far class or it consists of the single distance \(D\). Since dihedral symmetry prevents any split inside a distance class, the coloring is stable. Thus the least stable round is the least \(r\) with \(D\le2^r+1\), giving the displayed formula, including round zero for \(D\le2\), that is \(3\le n\le5\).

For counting width, first suppose \(3\le n\le5\). A two-variable counting sentence can say that there are exactly \(n\) vertices and every vertex has exactly two neighbors. A finite simple 2-regular graph is a disjoint union of cycles, and with fewer than six vertices there is room for only one cycle, so this defines \(C_n\). One variable cannot inspect adjacency between two distinct vertices, so the width is exactly two.

Now let \(n\ge6\). The graph \(C_3\dot\cup C_{n-3}\) is nonisomorphic to \(C_n\), has the same order, and is also 2-regular. Starting from the uniform vertex color, one-dimensional WL therefore remains uniform forever on both graphs. By the standard equivalence between one-dimensional WL and two-variable counting logic, no two-variable counting sentence defines \(C_n\). Thus \(W_{\#}(C_n)>2\).

Three variables suffice. With counting one may state the exact order and degree two, while connectedness at this fixed order is expressible with three variables by the standard recursively composed bounded-distance formulas, requiring paths only up to length \(n-1\). A connected finite 2-regular graph is a cycle, so \(W_{\#}(C_n)\le3\). This proves the width formula.

## Verification
A standalone verifier implements the classical pair-color refinement directly, without using graph automorphisms in the update. For every \(3\le n\le60\) it checks the exact stabilization round and the complete distance-class profile at every round. It also checks the closed-form stopping criterion for every \(3\le n\le4096\). The script returns:

`VERIFY_OK full_2WL_cycles_3_60 formula_cycles_3_4096 width_witnesses_6_60`

The finite computation is supplementary. The proof above establishes the formulas for every \(n\ge3\).

## Relationship to prior work
Pikhurko and Verbitsky formalized stabilization numbers for Weisfeiler--Leman refinement and the counting-logic correspondences used in the width argument. Their survey gives general bounds and many exact logical-complexity examples, but the inspected cycle-related material does not state the exact pair-refinement stabilization formula above.

Kluge studied precisely the round complexity of 2-WL on circulant graphs, the class containing every cycle, and proved the general upper bound \(O(d(n)\log n)\), where \(d(n)\) is the divisor-counting function. For the degree-two circulants \(C_n\), the present calculation replaces that class-level asymptotic bound by the exact logarithmic expression and identifies the distance-doubling mechanism round by round. Kiefer and Neuen analyze stable 2-WL colorings on planar graphs and explicitly encounter cycle structures, but their inspected text is about expressive structure rather than the number of rounds needed by an isolated cycle.

Targeted published-finding corpus and literature searches using the cycle, circulant, stabilization-number, distance-color, and counting-width formulations did not locate the displayed exact formulas. The main residual priority risk is that this short distance-doubling calculation may occur in lecture notes, theses, or folklore under association-scheme terminology.

## Limitations
The stabilization theorem is for the standard classical 2-WL initialization and round convention; changing the initial coloring or counting the atomic coloring as round one shifts the reported integer. The width theorem concerns definability of each fixed finite cycle, not uniform first-order definability of the infinite class of all cycles. The originality assessment is based on targeted indexed searches and inspected primary sources, not a proof of absence from all unpublished or weakly indexed material.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 25 March 2010); Contemporary Mathematics 558 (2011), 129--180, DOI: 10.1090/conm/558/11050.
2. L. Kluge, *Combinatorial refinement on circulant graphs*, arXiv:2204.01054 (first posted 3 April 2022); *computational complexity* 33 (2024), article 9, DOI: 10.1007/s00037-024-00255-2.
3. S. Kiefer and D. Neuen, *A Study of Weisfeiler--Leman Colorings on Planar Graphs*, arXiv:2206.10557 (first posted 21 June 2022).
4. S. Döring and D. Neuen, *The Classical Weisfeiler-Leman Algorithm Stabilizes in \(O(n)\) Rounds*, arXiv:2609.17364 (first posted 15 September 2026).
