# Distance-rigid power domination in dodecahedral–icosahedral duality

## Finding

Let \(D\) be the 20-vertex dodecahedral graph and let \(I\) be the 12-vertex icosahedral graph, the graph-theoretic planar dual of \(D\). For each of these graphs, every singleton fails power domination and some two-vertex sets succeed. The complete minimum-set classification is:

\[
\begin{aligned}
\gamma_P(D)&=2,&\quad\{u,v\}\text{ power dominates }D&\iff d_D(u,v)=3,\\
\gamma_P(I)&=2,&\quad\{u,v\}\text{ power dominates }I&\iff u\ne v.
\end{aligned}
\]

Thus \(D\) has exactly \(60\) minimum power dominating sets, while \(I\) has exactly \(66\). In the simultaneous rule with the closed neighborhood observed at time \(0\), the subsequent forcing-round count for every successful dodecahedral pair is exactly \(4\). On \(I\), every pair works, requiring \(2,1,0\) subsequent forcing rounds at pair-distances \(1,2,3\), respectively.

Join two *minimum* sets when they differ by one selected vertex. The resulting exchange graph for \(D\) is the line graph of the distance-three graph on \(V(D)\); it has \(60\) vertices, is \(10\)-regular with \(300\) edges, has diameter \(3\), and has unordered-pair distance frequencies \((300,870,600)\) at distances \(1,2,3\). The exchange graph for \(I\) is the triangular graph \(L(K_{12})\), with \(66\) vertices, degree \(20\), \(660\) edges, diameter \(2\), and frequencies \((660,1485)\).

## Assumptions and scope

Graphs are simple and undirected. Here is a complete labeled model, sufficient to remove ambiguities about drawings. For \(D\), use vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+2}\); the vertex numbers in the verifier are \(i\) for \(u_i\) and \(10+i\) for \(v_i\). This is the standard generalized Petersen representation \(GP(10,2)\) of the dodecahedral graph.

For \(I\), take poles \(N,S\), top vertices \(a_i\), bottom vertices \(b_i\), \(i\in\mathbb Z/5\mathbb Z\). Edges are \(Na_i\), \(Sb_i\), \(a_ia_{i+1}\), \(b_ib_{i+1}\), \(a_ib_i\), and \(a_ib_{i-1}\). The verifier labels these as \(N=0\), \(a_i=1+i\), \(b_i=6+i\), \(S=11\). This is the icosahedral graph.

For an initial set \(S\subseteq V(G)\), let \(O_0=N[S]\). Given \(O_t\), simultaneously observe every vertex that is the unique vertex of \(N(x)\setminus O_t\) for some \(x\in O_t\), defining \(O_{t+1}\). The set is power dominating exactly when \(O_t=V(G)\) for some finite \(t\). Our round count \(t\) excludes the initial closed-neighborhood observation; the convention of Ferrero--Hogben--Kenter--Young counts that observation as its first step and hence is larger by one.

## Proof

The graphs have respectively \((|V|,|E|,\deg)=(20,30,3)\) and \((12,30,5)\). Neither has a singleton power dominating set. For the dodecahedron, its girth is five: after observing the closed neighborhood of one vertex, every observed neighbor has two unobserved neighbors, and the seed has none. For the icosahedron, the neighbors of any vertex induce a five-cycle; each observed neighbor again has two unobserved neighbors. Thus no subsequent force is possible from a singleton in either graph.

For the upper bounds and complete equality classifications, it remains to check finitely many two-element sets. Because there are only \(\binom{20}{2}=190\) pairs in \(D\) and \(\binom{12}{2}=66\) in \(I\), the following complete distance-stratified table is an exact finite proof, not a sampled extrapolation. Each tuple lists the total number of observed vertices at time \(0\) and after each nonempty simultaneous forcing round, stopping at stabilization.

| Graph | Pair distance | Number of pairs | Stabilized observation-size sequence |
| --- | ---: | ---: | --- |
| \(D\) | \(1\) | \(30\) | \((6)\) |
| \(D\) | \(2\) | \(60\) | \((7,10)\) |
| \(D\) | \(3\) | \(60\) | \((8,10,14,18,20)\) |
| \(D\) | \(4\) | \(30\) | \((8)\) |
| \(D\) | \(5\) | \(10\) | \((8)\) |
| \(I\) | \(1\) | \(30\) | \((8,10,12)\) |
| \(I\) | \(2\) | \(30\) | \((10,12)\) |
| \(I\) | \(3\) | \(6\) | \((12)\) |

The table is generated directly from the explicit edge sets by a short full enumeration, with two separately implemented observation recurrences (set-based and integer-bitmask). The program `power_dual_verify.py` checks agreement of the two recurrences for every pair, recomputes all-pairs breadth-first-search distances, asserts the exact table, and tests every singleton. In particular, exactly \(60\) dodecahedral pairs, those at distance \(3\), and all \(66\) icosahedral pairs succeed. Together with the singleton lower bounds, this establishes the claimed minima and round counts.

Define \(J\) on \(V(D)\) by \(xy\in E(J)\iff d_D(x,y)=3\). Since minimum sets are precisely the edges of \(J\), exchanging one vertex of a minimum set means replacing one edge of \(J\) by an incident edge. Thus the exchange graph is exactly \(L(J)\). Each vertex of \(J\) has degree \(6\), so \(|E(J)|=60\), and each vertex of \(L(J)\) has degree \(2(6-1)=10\). The edge number is \(60\cdot10/2=300\). Exact breadth-first-search enumeration on \(L(J)\) gives the full unordered-pair distance distribution \((300,870,600)\), summing to \(\binom{60}{2}=1770\); hence the exchange graph is connected with diameter \(3\). The same verifier checks these distances from each of its \(60\) vertices.

For \(I\), every unordered pair of distinct vertices is a minimum power dominating set, so the exchange graph is \(L(K_{12})\). Its vertices are the \(\binom{12}{2}=66\) edges of \(K_{12}\); it has degree \(2(12-2)=20\) and \(660\) edges. Two disjoint edges require and suffice for two exchanges, whereas intersecting edges are adjacent, proving diameter \(2\) and giving \(660\) pairs at distance one and \(\binom{66}{2}-660=1485\) at distance two.

## Verification

The self-contained Python 3 verifier `power_dual_verify.py` is included in this package and requires only the standard library. Execute `python3 power_dual_verify.py`. It constructs both labeled graphs from the edge rules above, independently runs set and bitmask simultaneous-observation algorithms on every unordered pair, checks all singletons, checks the distance-stratified tables, constructs all optimal-pair exchange graphs, and computes full shortest-path distance distributions. Successful output ends in `VERIFY_OK`.

## Relationship to prior work

Power domination originates with Haynes, Hedetniemi, Hedetniemi, and Henning. Barrera and Ferrero analyze power domination in generalized Petersen graphs and related product graphs; their stated general Petersen convention assumes a coprimality condition, and their relevant results determine upper bounds and some minimum *numbers*, not the present exhaustive locations and exchange metrics. Ferrero, Hogben, Kenter, and Young give the synchronous power-propagation framework and its timing convention. Xu and Kang, and Kang, Shan, and Zhao study generalized Petersen power-domination numbers, but their available abstracts do not establish the present complete distance characterization or its exchange-graph geometry. The latter two papers were not available for definitive full-text exclusion; this is a residual literature-comparison risk rather than evidence of priority.

## Limitations

The claim concerns exactly the two specified finite graphs; it does not extend to arbitrary dual planar graph pairs, generalized Petersen graphs, or larger polyhedra. The graph-distance classification and exchange diameter are exact finite results; they are not statements about electrical-network reliability or about a physical graph embedding. Some potentially relevant earlier generalized-Petersen papers could only be compared at abstract level; unindexed precedent cannot be ruled out. Independent review has not been performed.

## References

1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM Journal on Discrete Mathematics 15(4) (2002), 519–529. DOI: 10.1137/S0895480100375831.
2. R. Barrera and D. Ferrero, *Power Domination in Cylinders, Tori, and Generalized Petersen Graphs*, Networks 58(1) (2011), 43–49. DOI: 10.1002/net.20413. Author-hosted full text: https://cpb-us-e1.wpmucdn.com/wp.txstate.edu/dist/1/556/files/2015/03/BarreraFerrero.pdf.
3. D. Ferrero, L. Hogben, F. H. J. Kenter, and M. Young, *Note on power propagation time and lower bounds for the power domination number*, arXiv:1512.06413 (first public version 2015-12-20).
4. G. Xu and L. Kang, *On the power domination number of the generalized Petersen graphs*, Journal of Combinatorial Optimization 22 (2011), 282–291. DOI: 10.1007/s10878-010-9293-y.
5. L. Kang, E. Shan, and M. Zhao, *Power domination in the generalized Petersen graphs*, Discussiones Mathematicae Graph Theory 40(3) (2020), 695–712. DOI: 10.7151/dmgt.2137.
