# Sharp equality and basis counts for mixed-length spider resolving domination

## Finding
For all integers \(p\geq 0\) and \(q\geq2\), let \(T_{p,q}\) be the tree obtained by joining one central vertex to \(p\) leaves by edges and to another \(q\) leaves by two-edge paths. Then its dominant metric dimension and vertex-edge dominant edge metric dimension are
\[
\gamma_{md}(T_{p,q})=p+q,\qquad
\gamma_{emd}(T_{p,q})=\begin{cases}q,&p=0,\\ p+q-1,&p\geq1.\end{cases}
\]
In particular, equality holds precisely when \(p=0\), whereas adding any positive number of length-one arms produces an exact gap of one. The numbers of distinct minimum vertex sets are
\[
N_{md}(p,q)=\begin{cases}2^q-1,&p=0,\\(p+1)2^q,&p\geq1,\end{cases}
\]
\[
N_{emd}(p,q)=\begin{cases}(q+2)2^{q-1},&p=0,\\2^q-1,&p=1,\\p2^q,&p\geq2.\end{cases}
\]
These enumerations count labeled vertex subsets, not orderings of their elements.

## Assumptions and scope
All graphs are finite, simple, undirected, with ordinary unweighted shortest-path distances. Write the central vertex as \(r\), the short-arm leaves as \(x_1,\ldots,x_p\), and the vertices of the long arms as \(r-u_i-v_i\) for \(1\leq i\leq q\). An empty collection of short arms is permitted; there are always at least two long arms.

A dominant resolving set \(S\) dominates vertices by closed neighborhoods (every vertex outside \(S\) is adjacent to a member of \(S\)), and its distance vectors \((d(s,w):s\in S)\) distinguish all vertices \(w\). Its minimum size is \(\gamma_{md}\). For an edge \(e=ab\), set \(d(s,e)=\min\{d(s,a),d(s,b)\}\). A vertex-edge dominant edge-resolving set distinguishes all edges by the vectors \((d(s,e):s\in S)\), and satisfies \(d(s,e)\leq1\) for some selected vertex \(s\) for every edge \(e\). Its minimum size is \(\gamma_{emd}\). These are the two parameters compared in [1].

## Proof
**1. The dominant resolving sets.** For every \(i\), the leaf \(v_i\) is dominated only by itself and \(u_i\); therefore every vertex-dominating set intersects each pair \(\{u_i,v_i\}\). This requires at least \(q\) vertices. If \(p\geq1\) and \(r\notin S\), domination of all short leaves requires all \(p\) of them. If \(r\in S\), at most one short leaf may be omitted: two unselected short leaves are twins and have identical distance vectors to any selected vertices. Thus \(|S|\geq p+q\) (also when \(p=0\)).

The lower bound is attained by selecting one vertex in each long-arm pair and, if \(p\geq1\), either all short leaves or the root together with exactly \(p-1\) short leaves. For \(p=0\), choose one vertex per long arm, with at least one internal vertex \(u_i\), so that the root is dominated. These sets distinguish vertices: on a marked arm its own selected vertex gives its two nonroot vertices different distances; on distinct marked arms the selected marker of one arm distinguishes the two vertices, except for a possible short-leaf pair, which cannot both be unselected. More explicitly, the distance of a vertex outside arm \(i\) to a selected marker of arm \(i\) is its distance to the root plus the marker's depth; within arm \(i\) it is the absolute difference of depths. More directly, the two nonroot vertices of any marked long arm have distances zero and one to its selected vertex. A nonroot vertex in a marked arm is at distance at most one from its arm marker, whereas a vertex in another arm is at distance at least two from that marker. A selected short leaf distinguishes itself by distance zero. For the root versus a long-arm vertex, a marker on any *other* long arm has strictly smaller distance to the root than to that vertex (there is always such a marker since \(q\geq2\)); a selected short leaf similarly distinguishes the root from vertices in other arms. If the root is selected, its zero distance to itself also distinguishes it. Thus the displayed choices resolve all vertices. All admissible sets satisfy domination, including the root condition.

At the lower bound \(p+q\), exactly one vertex must occur in every long arm and the displayed minimum number of further vertices must be used. For \(p=0\) the root cannot be selected, and the all-terminal choice fails root domination, giving \(2^q-1\) minimum sets. For \(p\geq1\), there are \(2^q\) sets with all short leaves and no root, and \(p2^q\) sets with the root and all but one short leaf. This proves the first dimension and its basis count.

**2. The edge-resolving lower bound.** The \(p+q\) radial edges \(rx_j\) and \(ru_i\) have equal distances from \(r\) and from every vertex outside their two respective arms. If two distinct arms contain no selected vertex, their radial edges have identical distance vectors. Consequently, at least \(p+q-1\) distinct arms must be marked by nonroot selected vertices. If the root is selected this costs at least \(p+q\) vertices in total. If it is not selected, every outer edge \(u_iv_i\) must be dominated by a vertex of its own long arm: any vertex of another arm has distance at least two from \(u_iv_i\). Thus at least one of \(u_i,v_i\) must be chosen in every long arm, implying \(|S|\geq q\). Combined, the lower bounds are \(q\) when \(p=0\) and \(p+q-1\) when \(p\geq1\).

**3. Attainment and complete edge-basis classification.** If \(p=0\), either choose one vertex of each long arm and omit the root, or choose the root and one vertex of every long arm except one. Their sizes are \(q\); their counts are respectively \(2^q\) and \(q2^{q-1}\).

If \(p=1\), choose one vertex of every long arm, omit the root and the short leaf, and require at least one internal marker \(u_i\). The last condition is necessary and sufficient to dominate the short radial edge. These give \(2^q-1\) sets of size \(q\).

If \(p\geq2\), choose one vertex of every long arm and exactly \(p-1\) short leaves, omitting the root. The one omitted short radial edge is dominated by any chosen short leaf, and these sets total \(p2^q\).

Here is a direct check that every displayed set resolves edges. With respect to a selected marker of a long arm, the radial and outer edges of its own arm have distances \((0,0)\) if the marker is internal, or \((1,0)\) if it is terminal; all radial and outer edges of other arms have respectively distances \((1,2)\) or \((2,3)\). A chosen short leaf has distance \(0\) to its own radial edge, distance \(1\) to radial edges of other arms and distance \(2\) to outer edges. The root, when selected, has distance \(0\) to all radial edges and distance \(1\) to all outer edges. These signatures show that two different radial edges are distinguished as long as at most one arm is unmarked; two distinct outer edges are distinguished by a selected vertex on at least one of their arms; and a radial edge and an outer edge on different arms are distinguished by a marker of the latter long arm, or by a marker of the former arm if the latter is unmarked. A radial and outer edge of the same long arm are distinguished by a selected marker in any other arm or by the root. Such an auxiliary marker exists because \(q\geq2\), except possibly for the one unmarked arm in the root-selected family, when the root supplies the distinction. Outer edges are dominated by their own arm markers when present, and the outer edge in the unique unmarked long arm of the root-selected family is dominated by the root at distance one. Radial edges are dominated by a selected marker on that arm, by the root, or by an internal/short marker in another arm at distance one from the root. The three displayed families meet this condition. No other minimum sets are possible: equality in the preceding lower-bound argument forces one nonroot marker per marked arm, zero root unless \(p=0\), and permits the unmarked arm only as specified. This proves the second formula and the exact basis counts.

## Verification
An independent, finite direct-enumeration program is included as `verification/check_spiders.py`. It constructs adjacency, calculates all shortest paths by breadth-first search, tests vertex and edge codes from their definitions, checks domination, and enumerates every vertex subset for \(0\leq p\leq5\) and \(2\leq q\leq5\). It verified all four formulas on 24 graphs, examining 171360 subsets. The exhaustive finite diagnostic does not replace the proof for arbitrary parameters.

## Relationship to prior work
Ikhlaq, Hayat, and Siddiqui [1] introduced the vertex-edge dominant edge metric dimension, derived general tree bounds and comparisons, and explicitly asked in Problem 2 which trees have \(\gamma_{md}=\gamma_{emd}\). Their inspected results do not give the present radius-two mixed-arm equality classification or any of these complete minimum-basis enumerations. Brigham et al. [2] introduced resolving domination; Kelenc, Tratnik, and Yero [3] studied edge metric dimension without the additional edge-domination requirement. The present theorem settles the equality question only for the stated natural family, not all trees.

## Limitations
The result assumes an unweighted tree, at least two long arms, and no arm longer than two edges. It does not characterize equality for arbitrary trees, or enumerate nonminimum feasible sets. Priority cannot be conclusively established by indexed searches alone; an equivalent unindexed characterization may exist. 

## References
[1] H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327v1 (17 Nov 2022), especially Sections 2, 5–7 and Problem 2.
[2] R. C. Brigham, G. Chartrand, R. D. Dutton, P. Zhang, *Resolving domination in graphs*, Mathematica Bohemica 128 (2003), 25–36.
[3] A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: The edge metric dimension*, arXiv:1602.00291 (2016); Discrete Applied Mathematics 251 (2018), 204–220.
