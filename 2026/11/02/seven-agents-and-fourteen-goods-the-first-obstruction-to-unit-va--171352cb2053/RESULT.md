# Seven agents and fourteen goods: the first obstruction to unit-value equitable graph orientations

## Finding

For unit-valued indivisible goods represented by edges of a connected simple graph, every instance on at most six agents admits an orientation that is both equitable up to one good (EQ1) and envy-free up to one good (EF1). The same is true on seven agents with at most thirteen goods. Among connected seven-agent instances with fourteen goods, impossibility occurs **if and only if a vertex has degree one**. Precisely \(4410\) of the \(116175\) labeled connected graphs at this order and size fail, an exact proportion \(294/7745\).

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected undirected simple graph, with \(n=|V|\) and \(m=|E|\). Each edge is a separate indivisible good, worth one unit to each endpoint and zero to every nonendpoint. An *orientation* allocates each edge to exactly one endpoint. Agent \(v\)'s realized utility is its number of received edges, equivalently its indegree \(d^-(v)\) when directed toward the recipient.

EQ1 means that for any vertices \(u,v\), removing at most one good from the richer recipient's bundle eliminates their own-utility disparity: \(d^-(u)\ge d^-(v)-1\). Hence EQ1 is equivalent to \(\max_v d^-(v)-\min_v d^-(v)\le1\). EF1 means every agent \(u\) can remove at most one good from another recipient \(v\)'s bundle to eliminate \(u\)'s envy. Because the graph is simple, each other bundle contains at most one good that \(u\) values, so **every** orientation is EF1. These are unnormalized unit values; no varying weights, parallel edges, or disconnected graphs are claimed.

## Proof

Write \(q=\lfloor m/n\rfloor\). Since the indegrees sum to \(m\), EQ1 holds precisely when every indegree belongs to \(\{q,q+1\}\). For any set of vertices \(S\), let \(e(S)\) count edges with both endpoints in \(S\) and let \(i(S)\) count edges incident to at least one vertex of \(S\).

We use the following standard integral orientation criterion (Frank--Gyárfás; also follows by max flow): an orientation with every indegree between integers \(q\) and \(q+1\) exists if and only if, for every \(S\subseteq V\),
\[
 e(S)\le(q+1)|S|\quad\text{and}\quad i(S)\ge q|S|.
\]
The first condition counts edges forced to be received inside \(S\); the second counts the available incident edges for its lower demand. Sufficiency follows from the integral lower-/upper-capacity bipartite assignment of edge nodes to their endpoint nodes, by the circulation-cut criterion. It also covers cases in which all indegrees must equal \(q\).

If \(m<n\), connectedness forces \(m=n-1\), so \(G\) is a tree. Direct each edge away from one root: indegrees are zero at the root and one elsewhere. For \(n\le7\) and \(n\le m<2n\), we have \(q=1\). The lower condition \(i(S)\ge|S|\) holds for connected graphs with at least one cycle. Indeed, for a proper nonempty \(S\), if \(G[S]\) has \(c\) connected components, it has at least \(|S|-c\) internal edges and at least \(c\) edges to its complement. At \(S=V\), it holds because \(m\ge n\). The upper condition \(e(S)\le2|S|\) holds whenever \(|S|\le5\), since \(\binom{|S|}{2}\le2|S|\). For \(n\le6\), a six-vertex set, if present, is the entire graph with \(m<2n\le12\). For \(n=7,m\le13\), any six-vertex proper subset leaves at least one edge crossing to the omitted vertex by connectedness, hence \(e(S)\le m-1\le12\); the full set has \(m\le13<14\). This proves all the \(q=1\) cases.

For \(n=5,m=10\), the only possible graph is \(K_5\). A regular tournament orientation gives indegree two everywhere. For \(n=6\) and \(12\le m\le15\), we have \(q=2\). All sets satisfy \(e(S)\le3|S|\), since their cardinalities are at most six. For the lower inequality, \(i(S)=m-e(V\setminus S)\ge12-\binom{6-|S|}{2}\ge2|S|\) for each \(1\le |S|\le6\). These are all remaining cases with \(n\le6\). The cases of one through four vertices were already included in the tree and \(q=1\) arguments.

Now let \(n=7,m=14\). Any EQ1 orientation would have indegree exactly two at every vertex. Its existence is characterized by \(e(S)\le2|S|\) for every \(S\): since the total number of edges is \(2n\), assigning every edge to an endpoint with capacity two saturates every vertex, and the capacity-two Hall condition is precisely this collection of inequalities. For \(|S|\le5\), they hold automatically for a simple graph; for \(S=V\), there is equality. The only remaining case is \(|S|=6\), say \(S=V\setminus\{v\}\). Then \(e(S)=14-\deg(v)\le12\) if and only if \(\deg(v)\ge2\). Therefore EQ1 exists precisely when the graph has minimum degree at least two.

If a seven-vertex, fourteen-edge graph has a leaf \(v\), its other six vertices span thirteen edges and so form \(K_6\) with exactly two edges removed; they are automatically connected, with the leaf attached to one core vertex. Such a graph cannot have a second leaf, since two leaves would leave at most \(\binom52+2=12\) edges. Count the failures by choosing the unique leaf (seven choices), its neighbor (six choices), and the two missing core edges (\(\binom{15}{2}=105\) choices): \(7\cdot6\cdot105=4410\).

Of the \(\binom{21}{14}=116280\) labeled seven-vertex, fourteen-edge simple graphs, precisely \(7\binom{15}{14}=105\) are disconnected: a disconnected such graph must have exactly one isolated vertex, because any partition with both sides of size at least two has at most \(\binom52+\binom22=11\) edges. Thus the connected count is \(116280-105=116175\), and the fraction simplifies to \(294/7745\). The exhibited pendant-core graphs prove the cutoff sharp.

## Verification

The standalone script `verify.py` enumerates all labeled connected simple graphs on two through six vertices, checks the exact edge-to-endpoint orientation inequalities for every vertex subset, and reports zero failures. It independently enumerates all connected labeled seven-vertex graphs with exactly fourteen edges, checking the equivalence of failure and existence of a leaf. Its confirmed outputs include `n=6 connected=26704 nonEQ1=0` and `n7_m14 connected=116175 nonEQ1=4410 leaves=4410`. These finite enumerations corroborate the general proof; the cutoff and counting identities follow from the analytical argument above.

Reproduce with `python verify.py` using Python 3.10 or later; no nonstandard packages are required. In the checker, `feasible_cut` implements the two exact integral orientation inequalities, not a floating-point approximation.

## Relationship to prior work

Sun, Wang, and Li, *Fair Orientations: Proportionality and Equitability* (first public arXiv release February 20, 2026, arXiv:2602.18098), show that EQ1 graph orientations need not exist and study complexity for general weights. Their Section 4, Proposition 4.2 uses different edge values and does not state the uniform-unit connected-graph size threshold or the fourteen-edge seven-vertex classification. The Frank--Gyárfás orientation criterion already gives a general cut characterization; **that criterion is used, not claimed as new**. The new object is the sharp minimal uniform-unit obstruction and its complete labeled first-layer count, obtained through specific extremal graph analysis.

## Limitations

Only connected simple graphs with uniform unit value at their endpoints are treated. With disconnected graphs or heterogeneous edge values, counterexamples can occur earlier, and no extension to those models is claimed. The exact first-layer incidence is for labeled graphs, not unlabeled isomorphism types. This is a self-review, not an independent audit. Historical priority remains subject to unindexed specialized graph-orientation literature; the general orientation criterion is known.

## References

- A. Sun, R. Wang, B. Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098, first posted February 20, 2026, https://arxiv.org/abs/2602.18098 .
- A. Frank, A. Gyárfás, *How to orient the edges of a graph*, cited in Egres Open, *Orientation with degree bounds*, https://lemon.cs.elte.hu/egres/open/Orientation_with_degree_bounds .
- S. L. Hakimi, *On the degrees of the vertices of a directed graph*, J. Franklin Inst. 279 (1965), 290–308, https://doi.org/10.1016/0016-0032(65)90340-6 .
