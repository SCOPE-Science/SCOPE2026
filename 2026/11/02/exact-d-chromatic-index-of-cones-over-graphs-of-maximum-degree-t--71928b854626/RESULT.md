# Exact D-chromatic index of cones over graphs of maximum degree two

## Finding

A \(D\)-coloring of a finite simple graph is a proper edge-coloring in which every subgraph isomorphic to a diamond (the graph \(K_4-e\)) has five pairwise different edge colors. Diamonds are not required to be induced. The \(D\)-chromatic index \(\chi'_D(G)\) is the minimum palette size admitting such a coloring.

**Theorem.** Let \(H\) be any simple graph on \(n\ge1\) vertices with \(\Delta(H)\le2\), and let \(G=K_1\vee H\) be the graph obtained by adjoining a universal vertex. Define three indicators:

\[
\begin{aligned}
e(H)&=\mathbf1\{E(H)\ne\varnothing\},\\
p(H)&=\mathbf1\{H\text{ contains a path on three vertices}\},\\
c(H)&=\mathbf1\{H\text{ has a component isomorphic to }C_3\text{ or }C_4\}.
\end{aligned}
\]

Then

\[
\boxed{\chi'_D(K_1\vee H)=\max\{n,3e(H),5p(H),6c(H)\}.}
\]

In particular, every such cone with \(n\ge6\) has \(D\)-chromatic index exactly \(n=\Delta(G)\), regardless of how many path and cycle components occur in \(H\). The exceptional small-link costs are: a rim edge requires three colors overall, a three-vertex rim path requires five, and a triangle or four-cycle rim component requires six.

## Assumptions and scope

All graphs are finite, simple and undirected. A path component can have one or two vertices; cycles have length at least three; disconnected \(H\) is allowed. A proper edge-coloring assigns distinct colors to any two edges with a common endpoint. A diamond is any five-edge subgraph on four vertices isomorphic to \(K_4\) with one edge deleted, not necessarily an induced subgraph. All colors come from one named finite palette, although distinct nonadjacent edges may reuse colors.

Because every component of \(H\) is a path or a cycle, the indicators and the prescribed coloring can be determined directly from its component sizes. The theorem includes stars, fans, wheel graphs, unions of several rim cycles, and combinations of path and cycle rims. It does not assert anything for links with maximum degree at least three.

## Proof

**1. Localization of diamonds.** Every diamond contains a vertex of degree three. Since \(\Delta(H)\le2\), every diamond in \(G\) contains the universal vertex \(h\). Its other three vertices must span at least two edges in \(H\). If they span exactly two edges they form a path \(a-b-c\) and the five edges of the diamond are the three spokes \(ha,hb,hc\) and the two rim edges \(ab,bc\). If they span three edges they form a triangle, and all six edges of the resulting \(K_4\) must be pairwise differently colored: each nonincident edge pair appears in one of its noninduced diamonds. Thus it is necessary and sufficient that the coloring be proper, every rim path on three vertices have its five associated edges pairwise different, and every rim triangle have six associated edges pairwise different.

**2. Four independent lower bounds.** All \(n\) spokes meet at \(h\), proving \(\chi'_D(G)\ge n\). Any rim edge together with its two spokes is a triangle, requiring three distinct colors, so \(\chi'_D(G)\ge3\) if \(e(H)=1\). A path \(a-b-c\) in \(H\) and the universal vertex form a diamond; its five edges require distinct colors, so \(\chi'_D(G)\ge5\) if \(p(H)=1\). If \(H\) has a triangle component, its three vertices and \(h\) induce \(K_4\), requiring six colors. If \(H\) has a four-cycle component with vertices \(a,b,c,d\) in order, each rim edge is part of the two diamond configurations on its consecutive triples and must therefore avoid all four spoke colors \(ha,hb,hc,hd\). Two adjacent rim edges must have different colors. Hence at least two further colors are needed, proving \(\chi'_D(G)\ge6\). These establish the stated maximum as a lower bound.

**3. A coloring attaining all bounds.** Let \(k=\max\{n,3e(H),5p(H),6c(H)\}\), with palette \(\{0,1,\ldots,k-1\}\). Give the \(n\) spokes distinct colors \(0,\ldots,n-1\). Arrange each path or cycle component as one consecutive block when choosing these spoke colors; the order within a path is the path order, and the order within a cycle is cyclic. Since each spoke has a different color, the spoke edges are properly colored.

For a path component with consecutive spoke colors \(i,i+1,\ldots,i+m-1\), if \(k\ge5\) color its rim edge joining the vertices with spoke colors \(j,j+1\) by \(j+3\pmod{k}\). Each path triple at spoke positions \(j,j+1,j+2\) then has its two rim edges colored \(j+3,j+4\pmod{k}\); all five residues are different because \(k\ge5\). If \(k<5\), the absence of any three-vertex rim path means every path component contains at most one edge, and \(k\ge3\) whenever such an edge exists. Color each isolated rim edge by any palette color outside its two endpoint-spoke colors. There are no path triples to check.

For a cycle component \(v_0v_1\cdots v_{m-1}v_0\) of length \(m\ge5\), let \(a_j\) be the spoke color at \(v_j\), and color rim edge \(v_jv_{j+1}\) by \(a_{j+3}\), with indices interpreted modulo \(m\). Every three consecutive vertices have spoke colors \(a_j,a_{j+1},a_{j+2}\) and the two rim edges have colors \(a_{j+3},a_{j+4}\). These five are distinct since \(m\ge5\). Consecutive rim edges also differ, so the coloring is proper on that component.

For a triangle component, \(k\ge6\); assign its three rim edges three distinct palette colors outside the three spoke colors of that component. For a four-cycle component, \(k\ge6\); choose two distinct palette colors outside its four spoke colors and alternate them along its rim. Both constructions satisfy every local diamond constraint and properness.

Finally, diamonds cannot use rim edges from two different components of \(H\): their three rim vertices must induce a connected two-edge path or triangle. Thus colors assigned independently to different rim components never create an additional conflict. All required diamonds are rainbow and the coloring is proper, using at most \(k\) colors. Coupled with the lower bound, this proves equality for every \(n\ge1\). \(\square\)

## Verification

The included self-contained Python 3 script `verify.py` reconstructs the \(D\)-conflict relation independently from four-vertex edge sets. For each graph it tests the constructive coloring directly on all conflicting edge pairs and determines the chromatic number of the conflict graph by exhaustive backtracking for the small instances. It checked all \(305\) labeled degree-at-most-two graphs on up to five vertices, and \(295\) path/cycle component profiles on up to ten vertices. For profiles on up to seven vertices it separately refuted a coloring with one fewer color.

Replay with `python3 verify.py` from the directory containing this file. The deterministic output is:

```
ALL_LABELED_DEGREE_TWO_GRAPHS_N_LE_5_OK 305
UNLABELED_COMPONENT_PROFILES_N_LE_10_OK 295
VERIFY_OK
```

This finite verification is independent support for the explicit construction; the proof above supplies the all-order guarantee. No assumption of exhaustive enumeration beyond the stated finite ranges is used.

## Relationship to prior work

Wang introduced rainbow-diamond \(D\)-coloring and its general degree-based bounds [1]. Hu, Kong and Wang proved upper bounds for planar graphs in several degree ranges and describe the edge-conflict graph [2]. Verma subsequently proved Wang's sharp general planar conjecture, including the \(2\Delta-1\) upper bound for maximum degree at least six, by discharging [3]. Those bounds do not give the exact \(n\)-color result for every cone with a maximum-degree-two link. The relevant paper [3] also treats the different graph \(K_2\vee P_m\) in a reducibility lemma; two universal vertices and a different prescribed edge palette are involved there.

The special family \(K_1\vee C_m\) for \(m\ge5\) had already been resolved in prior wheel work; its \(n\)-color minimum is not claimed as new. Similarly, special complete-multipartite cases such as \(K_4\) are already implied by general results on complete multipartite graphs. The contribution claimed here is the single exact criterion for **all** degree-at-most-two links, including arbitrary mixtures of disconnected paths, small cycles and longer cycles, with sharp exceptional thresholds and a uniform construction.

## Limitations

The result gives the minimum palette size, not the number of optimal colorings. It is restricted to a single universal vertex and rim graphs of maximum degree at most two; it does not classify graphs with links containing branching vertices, more general planar graphs, or joins with two universal vertices. Independent mathematical audit and exhaustive historical-priority verification have not been performed. Searches for alternate terminology do not certify priority.

## References

1. Runze Wang, *Proper edge coloring with rainbow diamonds*, arXiv:2606.06831 (first submitted 2026-06-05), https://arxiv.org/abs/2606.06831.
2. Xiaoxue Hu, Jiangxu Kong, and Yiqiang Wang, *D-coloring of planar graphs*, arXiv:2607.14837 (first submitted 2026-07-16), https://arxiv.org/abs/2607.14837.
3. Harshit Verma, *A proof of Wang's planar D-coloring conjecture*, arXiv:2610.33322v1 (first submitted 2026-10-23), https://arxiv.org/html/2610.33322v1.
