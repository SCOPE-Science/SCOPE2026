# Exact depth-first back-edge congestion of wheel graphs

## Finding
Let \(n\ge4\) be an integer. Write \(W_{n+1}=K_1\vee C_n\) for the wheel with hub \(h\) and rim vertices \(v_0,\ldots,v_{n-1}\), indexed cyclically. In the terminology of Bourotte, Ducloz, Orponen, and Seki, \(\operatorname{KLX}(G)\) is the minimum, over ordered depth-first-search (DFS) trees, of the largest number of simultaneously open back edges. Let \(\operatorname{DTC}(G)\) denote their crossing-only DFS-tree congestion. Then
\[
\boxed{\operatorname{KLX}(W_{n+1})=\operatorname{DTC}(W_{n+1})=\left\lceil\frac n2\right\rceil+1.}
\]
An optimum is realized by the Hamiltonian DFS path
\[
v_0,v_1,\ldots,v_{a-1},h,v_a,\ldots,v_{n-1},\qquad a=\left\lfloor\frac n2\right\rfloor.
\]
In contrast, the ordinary spanning-tree congestion and treewidth satisfy
\[
\boxed{\operatorname{stc}(W_{n+1})=3,\qquad \operatorname{tw}(W_{n+1})=3.}
\]
Thus the DFS restriction incurs an unbounded additive and multiplicative congestion penalty on a family of planar, three-connected graphs of fixed treewidth. The four-vertex wheel \(W_4=K_4\), outside the new theorem's \(n\ge4\) domain, also has \(\operatorname{KLX}=3\), as follows from the previously known complete-graph formula.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected. For a rooted ordered DFS tree \(T\), a non-tree edge joins an ancestor and a descendant; its arc begins at the descendant's last appearance in the DFS contour and ends at the next appearance of its ancestor. The number of arcs spanning a reverse traversal of a tree edge is the open-back-edge count at that edge. \(\operatorname{KLX}(T)\) is the maximum of those counts, minimized over ordered DFS trees to obtain \(\operatorname{KLX}(G)\). \(\operatorname{DTC}(T)\) counts only non-tree edges whose tree paths traverse the edge. For a tree edge \(e\), removing \(e\) partitions the vertices into \(S_e\) and its complement; consequently
\[
\operatorname{dtc}_T(e)=|\delta_G(S_e)|-1.
\]
The inequality \(\operatorname{DTC}(G)\le\operatorname{KLX}(G)\) is from the initiating paper. Ordinary spanning-tree congestion \(\operatorname{stc}\) minimizes \(\max_e|\delta_G(S_e)|\) over all (not necessarily DFS) spanning trees. The theorem concerns wheels with a cycle of at least four rim vertices; no assertion is made for weighted, directed, or modified wheels.

## Proof
**Step 1 (the two hub-adjacent cuts in any DFS tree).** Consider an arbitrary ordered DFS tree \(T\) of \(W_{n+1}\). If \(h\) is the root, its first child subtree contains every rim vertex, since the rim cycle is connected. The cut of the first tree edge isolates \(h\); thus \(\operatorname{DTC}(T)\ge n-1\). If \(h\) is a DFS leaf, its incoming tree edge similarly isolates \(h\), giving the same bound. Since \(n\ge4\),
\[
n-1\ge\left\lceil\frac n2\right\rceil+1.
\]

Suppose instead that \(h\) is neither root nor leaf. Until \(h\) is first visited, the DFS path follows consecutive rim vertices: at each rim vertex, either it moves to \(h\), or it follows the only as-yet-unvisited next rim neighbour. Backtracking cannot occur beforehand, because \(h\) remains unvisited and is adjacent to the current rim vertex. Hence the strict ancestors of \(h\) form one contiguous rim path \(A\), with cardinality \(a\) satisfying \(1\le a\le n-1\). The remaining rim vertices form a connected path. Upon entering \(h\), DFS visits all of this remaining path inside its first child's subtree, so \(h\) has exactly one child \(c\).

For the entering edge \(e_-\) from the last vertex of \(A\) to \(h\), its child-side subtree is \(\{h\}\cup(V(C_n)\setminus A)\). The cut separates \(a\) hub spokes and exactly two rim edges, because \(A\) is a proper nonempty contiguous path in a cycle. One spoke is the tree edge. Therefore
\[
\operatorname{dtc}_T(e_-)=a+2-1=a+1.
\]
For the departing edge \(e_+=hc\), its child-side subtree is exactly the remaining \(n-a\) rim vertices. This cut consists of \(n-a\) spokes and the same two rim edges, with one spoke being the tree edge. Thus
\[
\operatorname{dtc}_T(e_+)=n-a+2-1=n-a+1.
\]
These edges alone give
\[
\operatorname{KLX}(T)\ge\operatorname{DTC}(T)
\ge\max\{a+1,n-a+1\}
\ge\left\lceil\frac n2\right\rceil+1.
\]
The argument covers branch vertices elsewhere in \(T\), since no shape assumption on the DFS subtree below \(c\) was used.

**Step 2 (an attaining ordered DFS path).** Put \(a=\lfloor n/2\rfloor\). The order
\[
v_0,\ldots,v_{a-1},h,v_a,\ldots,v_{n-1}
\]
is a Hamiltonian path of the wheel. Root and order DFS to traverse this path before backtracking. Every non-tree edge joins comparable path vertices, and the tree has no branching; hence there are no enveloping back edges. For a tree edge following a prefix \(S\), the open-edge count is exactly \(|\delta(S)|-1\).

Before visiting \(h\), a prefix consists of \(k\) consecutive rim vertices, where \(1\le k\le a\). Its cut has \(k\) spokes and two rim edges, hence the open count is \(k+1\le a+1\). After visiting \(h\), a proper prefix contains \(h\) and \(k\) consecutive rim vertices, where \(a\le k<n\); its cut has \(n-k\) spokes and two rim edges, hence the open count is \(n-k+1\le n-a+1\). Both displayed maxima are realized at edges incident with \(h\). Thus
\[
\operatorname{KLX}(T)=\operatorname{DTC}(T)
=\max\{a+1,n-a+1\}
=\left\lceil\frac n2\right\rceil+1.
\]
Combining Steps 1 and 2 establishes both exact DFS invariants.

**Step 3 (ordinary congestion and treewidth).** Each rim vertex has degree three. For any nonempty proper vertex set, its edge boundary has size at least three: if the hub is outside the set, either the set is the entire rim (at least four spokes cross), or a nonempty proper rim subset (at least one spoke and two rim edges cross); take complements if the hub is inside. Hence any spanning-tree cut has at least three graph edges. The hub-centered star is a spanning tree, and each of its edge cuts isolates a degree-three rim vertex. Therefore \(\operatorname{stc}(W_{n+1})=3\).

The bags \(\{h,v_0,v_i,v_{i+1}\}\) for \(1\le i\le n-2\), in their natural linear order, form a tree decomposition of width three. Conversely, contracting rim edges reduces any such wheel to \(K_4\) as a minor, so its treewidth is at least three. This proves \(\operatorname{tw}(W_{n+1})=3\).

## Verification
The standalone file `verify_wheel_klx.py` enumerates all ordered DFS traversals at rim sizes \(3\le n\le9\), reconstructs their full Euler contours, and counts open non-tree-edge arcs according to their endpoints. It checks that the minimum equals \(\lceil n/2\rceil+1\) even when DFS trees branch. In total, 2,380 ordered DFS traversals were checked, including 1,428 with branching. It also evaluates the explicit Hamiltonian path directly from arc intervals for every \(10\le n\le500\), and checks classical congestion of the hub star. These computations are finite consistency checks, not the proof of the unrestricted statement.

Run with Python 3: `python3 verify_wheel_klx.py` from the directory containing the file. No nonstandard packages are needed.

## Relationship to prior work
Bourotte, Ducloz, Orponen, and Seki introduced KLX, defined open/crossing/enveloping back edges, established \(\operatorname{DTC}\le\operatorname{KLX}\), characterized graphs with KLX at most two, and proved degree and treewidth bounds. Their accessible complete text does not give wheel evaluations. Its maximum-degree lower bound implies growth for wheel graphs but not the exact linear rate.

Previously published exact KLX results for complete graphs and complete bipartite graphs do not cover these wheels with \(n\ge4\). A separate published calculation for balanced complete multipartite graphs requires equal part sizes and is likewise inapplicable. Classical spanning-tree-congestion work optimizes over arbitrary spanning trees; the wheel's ordinary optimum is three, so it cannot imply the claimed DFS optimum by equality. The quantitative separation and the two-hub-cut proof distinguish the present assertion from these results.

## Limitations
The proof uses the hub joined to every vertex of an induced cycle, with exactly the wheel edges. It does not yield exact values for arbitrary apex graphs, wheel-like graphs with missing spokes or extra rim chords, or arbitrary DFS-order constraints. Bibliographic searches cannot exclude an equivalent unindexed theorem or an alternative formulation in older DFS-cut congestion literature. The evidence is a complete mathematical argument with finite checks, not an independent audit.

## References
1. C. Bourotte, G. Ducloz, P. Orponen, S. Seki, *A Congestion Parameter for Depth-First Graph Traversals*, arXiv:2606.24675v1, first posted 23 June 2026. https://arxiv.org/abs/2606.24675
2. *Exact KLX numbers of complete and complete bipartite graphs*, published mathematical record b27f97da8029 (19 September 2026).
3. *Exact KLX number of balanced complete multipartite graphs*, published mathematical record d7d7a1fe0f08 (4 October 2026).
