# Exact D-chromatic index of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\) and \(n_1\ge\cdots\ge n_r\ge1\). If \(H_D(G)\) denotes the edge-conflict graph whose vertices are the edges of \(G\) and whose adjacencies are exactly the pairs that must receive different colors in a D-coloring, then
\[H_D(G)\cong \bigvee_{1\le i<j\le r}L(K_{n_i,n_j}).\]
Consequently,
\[\chi'_D(G)=\sum_{1\le i<j\le r}\max\{n_i,n_j\}=\sum_{i=1}^{r-1}(r-i)n_i.\]
Equivalently, every color class in every D-coloring is a matching contained in the edges between one fixed unordered pair of multipartition classes. Private optimal palettes on the complete bipartite cuts attain the formula. Hence, with \(\Delta(G)=\sum_{i=1}^{r-1}n_i\), Wang's conjectured bound \(\chi'_D(G)\le \Delta(G)(\Delta(G)+1)/2\) holds for every complete multipartite graph, with equality if and only if \(G\) is complete.

## Assumptions and scope
All graphs are finite and simple. A D-coloring is a proper edge coloring in which every diamond subgraph is rainbow, using the definition introduced by Wang. Here a diamond is \(K_4\) with one edge deleted as a subgraph. Equivalently, for two nonincident edges \(uv\) and \(wx\), the D-condition forces different colors whenever at least three of the four connector edges \(uw,ux,vw,vx\) are present. The multipartition classes of \(G\) are \(V_1,\ldots,V_r\) with \(|V_i|=n_i\) and \(n_1\ge\cdots\ge n_r\ge1\).

## Proof
Partition \(E(G)\) by the unordered pair of multipartition classes containing the endpoints. Consider two distinct edges with the same color. Properness makes them disjoint. If their four endpoints meet at least three multipartition classes, then among the four possible connector edges joining the endpoints of one edge to the endpoints of the other, at most one connector lies inside a multipartition class. Hence at least three connectors are edges of \(G\), so the D-condition forces the original two edges to have different colors, a contradiction. Therefore any two same-colored edges use exactly the same unordered pair \(V_i,V_j\).

Conversely, two disjoint edges both joining \(V_i\) to \(V_j\) have exactly two connector edges: the other two connectors lie inside \(V_i\) and \(V_j\). Hence they are not in D-conflict. Within the block \(E(V_i,V_j)\), D-conflict is therefore exactly ordinary edge incidence, so the induced conflict graph is \(L(K_{n_i,n_j})\). Any edges belonging to two different unordered part-pairs are either incident or, if disjoint, have endpoints in at least three parts and hence are in D-conflict. Thus all vertices belonging to distinct blocks are mutually adjacent in the conflict graph. This proves
\[
H_D(G)\cong\bigvee_{i<j}L(K_{n_i,n_j}).
\]

The chromatic number of a graph join is the sum of the chromatic numbers of its factors. Also \(\chi(L(K_{a,b}))=\chi'(K_{a,b})=\max\{a,b\}\). For completeness, the upper bound in the latter equality has an explicit cyclic coloring: label the sides by \(0,\ldots,a-1\) and \(0,\ldots,b-1\), set \(q=\max\{a,b\}\), and give edge \(xy\) color \(x+y\pmod q\). The degree lower bound gives the reverse inequality. Therefore
\[
\chi'_D(G)=\sum_{i<j}\max\{n_i,n_j\}.
\]
Since the part sizes are nonincreasing, \(\max\{n_i,n_j\}=n_i\) for \(i<j\), which gives \(\sum_{i=1}^{r-1}(r-i)n_i\). The same argument shows directly that every color class is a matching supported on one fixed part-pair.

For the conjectured bound, put \(s=r-1\) and \(\Delta=\sum_{i=1}^{s}n_i\); this is the maximum degree because \(V_r\) is a smallest part. Since \(n_i\ge1\),
\[
\chi'_D(G)=\sum_{i=1}^{s}(s+1-i)n_i
\le s\Delta-\frac{s(s-1)}2.
\]
Consequently,
\[
\binom{\Delta+1}{2}-\chi'_D(G)
\ge\frac{(\Delta-s)(\Delta-s+1)}2\ge0.
\]
Equality in Wang's bound forces \(\Delta=s\), hence \(n_1=\cdots=n_s=1\), and then \(n_r=1\) as well. Thus equality holds exactly for complete graphs; conversely, the displayed formula gives equality when every part is a singleton.

## Verification
The standalone verifier reconstructs the edge-conflict graph directly from the D-coloring definition. For every complete multipartite isomorphism type of order at most \(7\), it computes the chromatic number of that conflict graph by exact backtracking and compares it with the formula. It also verifies the structural characterization of nonconflicting disjoint edge pairs, replays the explicit cyclic palette construction through order \(10\), and checks the conjectured inequality and equality characterization on a finite parameter box. Its recorded output is:

`ALL CHECKS PASSED; exact_types=37; exact_edges=388; structural_disjoint_pairs=1088; constructive_types=128; constructive_edges=2926; bound_cases=456`

These computations are stress tests only; the theorem for arbitrary part sizes is proved analytically above.

## Relationship to prior work
Wang introduced D-coloring and the D-chromatic index in arXiv:2606.06831v1, gave the equivalent two-edge connector condition used above, conjectured the universal bound \(\chi'_D(G)\le \Delta(G)(\Delta(G)+1)/2\), and noted that complete graphs attain equality. The same source also makes the bipartite endpoint of the present theorem immediate: triangle-free graphs are diamond-free, so for \(K_{a,b}\) the D-chromatic index is just the ordinary chromatic index \(\max\{a,b\}\). The inspected full preprint does not state an arbitrary complete-multipartite formula and contains no occurrence of “multipartite.”

Tian and Wang, arXiv:2609.01875v1, subsequently improved the asymptotic general upper bound for sufficiently large maximum degree. Its full text was inspected and likewise contains no occurrence of “multipartite”; its general estimate does not imply the exact join decomposition or the formula above. Thus the already-covered cases \(r=2\) and all-singleton parts are endpoints of a new arbitrary-part exact classification rather than the novelty claim by themselves.

## Limitations
The theorem concerns complete multipartite graphs only. It does not prove Wang's conjecture for arbitrary graphs, and it does not classify all optimal colorings beyond the forced support condition on each color class. Literature searches cannot exclude an unindexed or unpublished equivalent result. The finite computations are not an infinite proof.

## References
1. Runze Wang, “Proper edge coloring with rainbow diamonds,” arXiv:2606.06831v1, 5 June 2026. Primary MSC2020: 05C15.
2. Lin Tian and Runze Wang, “A stronger upper bound on the D-chromatic index,” arXiv:2609.01875v1, 1 September 2026.
