# An added contact can sharply reduce worst-equilibrium protection cost

## Finding
Consider the spectral-threshold epidemic-containment game with one-unit protection cost, zero cost to unprotected agents in subthreshold components, two-unit cost to unprotected agents in superthreshold components, and fixed threshold \(0<T<1\). For every integer \(k\ge 2\), there is a connected tree \(G_k\) on \(2k+2\) agents and one missing contact \(e\) for which the augmented graph \(H_k=G_k+e\) has the exact equilibrium and social-optimal costs
\[
\begin{aligned}
\operatorname{Opt}(G_k)&=\operatorname{Opt}(H_k)=3,\\
\operatorname{BestNE}(G_k)&=\operatorname{BestNE}(H_k)=3,\\
\operatorname{WorstNE}(G_k)&=2k,\\
\operatorname{WorstNE}(H_k)&=k+1.
\end{aligned}
\]
Thus adding just one contact decreases the worst pure-Nash equilibrium protection cost by \(k-1\), arbitrarily much, while the social optimum and best equilibrium are unchanged. The price of anarchy drops from \(2k/3\) to \((k+1)/3\). Among connected simple graphs, six vertices are necessary and sufficient for any decrease of worst-equilibrium cost under one edge addition in this threshold regime.

## Assumptions and scope
Every graph is finite, simple, undirected, with one strategic agent per vertex. Each agent chooses to secure itself or remain unprotected. Let \(I\) be the unprotected set and let \(Q\) be the connected component of the induced graph \(G[I]\) containing an unprotected vertex. Its cost is zero when the adjacency spectral radius \(\lambda_1(Q)<T\), and two when \(\lambda_1(Q)>T\); a secured vertex pays one. Fix any \(0<T<1\), so equality is impossible: every edgeless component has spectral radius zero, while a component containing an edge has spectral radius at least one. Social cost is the sum of individual costs. \(\operatorname{BestNE}\) and \(\operatorname{WorstNE}\) range over pure Nash equilibria; \(\operatorname{Opt}\) ranges over all strategy profiles.

For each integer \(k\ge2\), construct \(G_k\) from distinct hubs \(u,v\), leaves \(a_1,\ldots,a_k\) adjacent only to \(u\), and leaves \(b_1,\ldots,b_k\) adjacent only to \(v\), together with one bridge \(a_1b_1\). In particular, the hubs are not adjacent in \(G_k\), and the bridge converts the two stars into a tree. Define \(H_k\) by adding the single hub edge \(uv\); it is unicyclic with one four-cycle. Edges and vertices carry no weights.

## Proof
**Step 1: equilibrium and optimum reduction.** A strategy profile is a pure Nash equilibrium precisely when its unprotected set \(I\) is a maximal independent set. Indeed, if \(G[I]\) has any edge, every unprotected agent in the corresponding component incurs cost two and can lower its own cost to one by securing. Conversely, if \(I\) is independent, every unprotected agent pays zero. A secured agent would strictly prefer to become unprotected exactly when it has no neighbor in \(I\). Thus precisely the maximal independent sets, which also dominate all vertices, are equilibria. Write \(i(G)\) for the minimum size of a maximal independent set and \(\alpha(G)\) for the maximum independent-set size. Every maximal independent set has protection cost \(|V(G)|-|I|\). Consequently,
\[
\operatorname{BestNE}(G)=|V(G)|-\alpha(G),\qquad
\operatorname{WorstNE}(G)=|V(G)|-i(G).
\]
In this cost regime, the social optimum also equals \(|V(G)|-\alpha(G)\). To see this without assuming equilibrium optimality, take a cost-minimizing profile. If any unprotected component contains an edge, an unprotected vertex in that component currently pays two; securing it changes its own cost to one and can only weakly reduce the costs of other agents, since the induced unprotected graph loses a vertex and spectral radii of its remaining components cannot increase. This strictly improves social cost, a contradiction. Hence any social optimum leaves an independent set unprotected, and a maximum independent set achieves the minimum protection cost.

**Step 2: unchanged optimum.** For \(k\ge2\), the three edges \(ua_2\), \(vb_2\), and \(a_1b_1\) are vertex-disjoint, in both \(G_k\) and \(H_k\). Any vertex cover therefore has at least three vertices. The set \(\{u,v,a_1\}\) covers all edges of either graph, including the added hub edge. Thus the minimum vertex-cover number is three in both graphs, and
\[
\alpha(G_k)=\alpha(H_k)=2k-1.
\]
Step 1 gives optimum and best equilibrium equal to three.

**Step 3: the tree's worst equilibrium.** Both hubs form an independent dominating set in \(G_k\), so \(i(G_k)\le2\). No vertex is universal when \(k\ge2\): every hub misses at least the opposite side's leaves, and each leaf misses other leaves. An independent dominating set of size one would require a universal vertex, hence \(i(G_k)=2\). Step 1 gives \(\operatorname{WorstNE}(G_k)=2k\).

**Step 4: the augmented graph's worst equilibrium.** Let \(I\) be an independent dominating set in \(H_k\). If \(u\in I\), the new edge excludes \(v\), and the hub's star edges exclude every \(a_j\). Each \(b_j\) must then belong to \(I\): for \(j\ge2\) its only neighbor \(v\) is absent, and for \(j=1\) both its neighbors \(v,a_1\) are absent. Therefore \(|I|\ge k+1\), with equality realized by \(\{u,b_1,\ldots,b_k\}\). The argument is symmetric if \(v\in I\). If neither hub belongs to \(I\), all \(2(k-1)\) private leaves \(a_2,\ldots,a_k,b_2,\ldots,b_k\) must belong to \(I\), and at least one of \(a_1,b_1\) must belong to \(I\); thus \(|I|\ge2k-1\ge k+1\). Consequently \(i(H_k)=k+1\), giving \(\operatorname{WorstNE}(H_k)=k+1\).

**Step 5: minimum order.** In every connected graph on at most five vertices, \(i(G)\le2\). If a vertex has degree at least \(|V|-2\), it alone, or together with its sole nonneighbor, is an independent dominating set. Otherwise, for a connected graph of order at most five the maximum degree is at most two, forcing a path or cycle; those orders have independent dominating sets of size at most two. If \(i(G)=1\), the graph has a universal vertex, retained after adding an edge, so \(i(G+e)=1\). Hence no edge addition can increase \(i(G)\) at such orders, and by Step 1 no such addition decreases worst-equilibrium protection cost. The case \(k=2\) supplies a connected six-vertex example: \(G_2\) is a six-vertex path, and \(H_2\) is the same path plus the chord between its two hubs. This proves the sharp cutoff.

## Verification
The accompanying standalone program `verify.py` enumerates *all vertex subsets* directly to compute the maximum independent-set size and the smallest maximal independent-set size. It checks both graphs for \(k=2,3,4,5,6\), including the predicted equal optimum and differing worst equilibria. It also exhaustively checks every connected labelled graph on two through five vertices and every possible one-edge addition; no decrease of worst-equilibrium cost is observed. The program uses only the Python standard library. Run `python verify.py` alongside this file. These finite checks are independent of, and not a replacement for, the quantified proof above.

## Relationship to prior work
Saha, Adiga and Vullikanti (2014) introduced this spectral-threshold epidemic-containment game, established the minimal securing-set characterization of pure Nash equilibria, and investigated general and random-network bounds. The present statement specializes the threshold to \(0<T<1\) and supplies an explicit sharp one-edge comparative static and its smallest connected witness, not a new epidemic process. Zhu, Ding, Tao, Wang and Yu (2021) analyzed minimum and maximum Nash protection costs on stars, complete graphs and paths and provided integer-programming formulations for small thresholds. Their formulations allow each finite instance to be solved, but do not themselves state the one-edge, unbounded-drop family with invariant social optimum or its sharp six-vertex threshold. Goddard and Henning (2013) surveyed independent domination, the graph parameter governing the worst equilibrium here. Xu (2013, Sec. 8.4) reviewed the independent *bondage number*, defined by deleting edges so that independent domination increases; this is a different operation from adding one edge to increase the parameter, and supplies no bound for the present construction. Kavitha and David (2015, Theorem 27) studied edge addition for *equitable* independent domination and identified the chord joining two supports of a path, including a special six-vertex case; their equitable adjacency restrictions differ from ordinary independent domination, and their result does not imply the quantified unbounded ordinary-parameter change. Aspnes, Chang and Yampolskiy (2004/2006) studied a different inoculation game whose risk cost depends on susceptible-component size rather than spectral-threshold status.

## Limitations
The result is exact for the specified discrete security game and all \(0<T<1\), not for realized epidemic counts, SIS transient distributions or arbitrary thresholds. It compares the worst *pure-equilibrium* protection costs, not the likely equilibrium under a specified learning or selection dynamic. The added edge never makes the protected contact network intrinsically safer; changed strategic responses account for the cost reduction. The social optimum refers to the game's stated costs, not empirical public-health welfare. A search of related mathematics cannot eliminate the possibility of earlier equivalent constructions; independent literature review and validation have not been performed.

## References
1. S. Saha, A. Adiga and A. K. S. Vullikanti, “Equilibria in Epidemic Containment Games,” *Proceedings of AAAI*, 28(1), pp. 777–783 (2014), DOI: 10.1609/aaai.v28i1.8819. Original article: https://ojs.aaai.org/index.php/AAAI/article/view/8819/8678 (publisher records public release 2014-06-21).
2. J. Zhu, H. Ding, Y. Tao, Z. Wang and L. Yu, “Secure the IoT Networks as Epidemic Containment Game,” *Symmetry* 13(2), 156 (2021), DOI: 10.3390/sym13020156.
3. W. Goddard and M. A. Henning, “Independent Domination in Graphs: A Survey and Recent Results,” *Discrete Mathematics* 313, 839–854 (2013), DOI: 10.1016/j.disc.2012.11.031.
4. J. Aspnes, K. Chang and A. Yampolskiy, “Inoculation Strategies for Victims of Viruses and the Sum-of-Squares Partition Problem,” Technical Report YALEU/DCS/TR-1295 (July 2004); *Journal of Computer and System Sciences* 72(6), 1077–1093 (2006). https://www.cs.yale.edu/publications/techreports/tr1295.pdf.
5. J.-M. Xu, “On Bondage Numbers of Graphs: A Survey with Some Comments,” *International Journal of Combinatorics* (2013), Article 595210, DOI: 10.1155/2013/595210. Sec. 8.4 discusses independence bondage under edge deletion.
6. K. Kavitha and N. G. David, “Equitable Total Domination Edge Addition Stable Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 92, 185–194 (2015). Theorem 27 concerns equitable independent domination after an edge is added. https://combinatorialpress.com/article/jcmcc/Volume%20092/vol-092-paper%2019.pdf.
