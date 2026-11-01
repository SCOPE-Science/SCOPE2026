# Short-distance geodesic histograms recover edge-degree mixing in finite metric graphs

## Finding
Let \(G=(V,E)\) be a finite connected simple undirected graph with \(m=|E|\ge1\). Each edge is a geometric interval of length one, and the resulting one-dimensional length space carries its intrinsic shortest-path metric and normalized arclength measure. For independent arclength-uniform points \(X,Y\), set \(F(r)=\Pr(d_G(X,Y)\le r)\) and write \(d_v\) for vertex degree. Define the three graph statistics
\[
S=\sum_{v\in V}d_v(d_v-1),\qquad H=\sum_{uv\in E}d_ud_v,\qquad R=H-2S.
\]
For every real \(0\le r\le3/2\), the complete initial-distance profile is the universal quadratic spline
\[
\boxed{F(r)=\frac{2mr+(S/2-m)r^2+R\max\{r-1,0\}^2}{m^2}.}
\]
In particular, the local intrinsic-distance distribution determines all three invariants without knowing the graph:
\[
\boxed{m=\frac2{F'(0+)},\quad S=m^2F''(0+)+2m,\quad H=2S+\frac{m^2}{2}\big(F''(1+)-F''(1-)\big).}
\]
The second derivatives above are one-sided on the open polynomial chambers.

This invariant contains strictly more information than the degree sequence. For instance, take vertex set \(\{0,1,2,3,4\}\) and the two edge sets
\[
E_1=\{04,12,13,23,34\},\qquad E_2=\{01,13,14,23,24\},
\]
where \(ij\) denotes the undirected edge joining vertices \(i\) and \(j\). Both graphs have degree multiset \(\{1,2,2,2,3\}\), hence \(m=5\) and \(S=12\), but \(H_1=24\), \(H_2=23\). Therefore \(F_1(r)=F_2(r)\) for every \(0\le r\le1\), while
\[
\boxed{F_1(r)-F_2(r)=\frac{(r-1)^2}{25}>0\quad(1<r\le3/2).}
\]
Thus radius one is the sharp universal first point at which local arclength-distance histograms can detect edge-degree mixing not fixed by degrees alone.

## Assumptions and scope
Graphs are finite, connected and simple, have at least one edge, and have all edge lengths exactly one. Degree-two vertices are retained as vertices; this is a metric graph equipped with its specified unit-edge decomposition. The inverse statements recover graph statistics, not an arbitrary graph up to isomorphism. No formula beyond radius \(3/2\) is claimed. The CDF is continuous, and all derivatives are understood on open intervals or one-sided limits.

## Proof
We compute the area of pairs \((x,y)\) on each ordered pair of edges in their unit-square coordinates and divide by \(m^2\). For one edge paired with itself, the region \(|x-y|\le r\) has area \(2r-r^2\) for \(0\le r\le1\), and area one for \(r\ge1\).

For two distinct edges meeting at a vertex, the direct route through their common endpoint has length \(x+y\) with both coordinates measured outward from that vertex. Its region has area \(r^2/2\) for \(r\le1\), and \(1-(2-r)^2/2\) for \(1\le r\le3/2\). Every shortest route shorter than \(3/2\) between points on two edges must either be these direct same-edge/shared-vertex routes, or use exactly one distinct complete intervening edge. Indeed any route with two intervening complete edges costs at least two. The direct same-edge route is never beaten for \(r\le3/2\) by a detour, as a nontrivial alternate same-edge route requires at least two full edges in addition to endpoint distances.

For one intervening edge \(g=uv\), with original edges \(e\ne g\) incident to \(u\) and \(f\ne g\) incident to \(v\), the route using \(g\) has length \(1+x+y\), where \(x,y\) measure distances from \(u,v\) along \(e,f\). Its additional feasible area for \(1<r\le3/2\) is exactly \((r-1)^2/2\). These corner triangles are disjoint from one another and from the direct route on each edge-pair square: they occupy corners of side at most \(r-1\le1/2\), while any alternative direct route on two edges sharing a vertex lies in the opposite corner and would require \(r\ge3/2\) to overlap in positive area. Because the graph is simple, a fixed pair of endpoint corners has at most one intervening edge.

There are \(m\) same-edge ordered pairs and \(S=\sum_vd_v(d_v-1)\) ordered pairs of distinct edges with a common vertex. Counting the intervening-edge paths by their middle edge \(uv\) gives \(2Q\) ordered paths, where \(Q=\sum_{uv\in E}(d_u-1)(d_v-1)\). Their added area is therefore \(Q(r-1)^2\). For \(0\le r\le1\), direct regions contribute \(m(2r-r^2)+Sr^2/2\). For \(1\le r\le3/2\), they contribute \(m+S(1-(2-r)^2/2)\) plus the intervening contributions \(Q(r-1)^2\). The two expressions combine to
\[
m^2F(r)=2mr+(S/2-m)r^2+(m-S+Q)(r-1)^2
\]
for \(1\le r\le3/2\). Expanding \(Q=\sum_{uv}(d_ud_v-d_u-d_v+1)\) and using \(\sum_{uv\in E}(d_u+d_v)=\sum_vd_v^2=S+2m\) gives \(m-S+Q=H-2S=R\). This establishes the displayed spline on the entire claimed domain.

Differentiation yields the reconstruction identities. Finally, the displayed graph edge sets each give degree multiset \(\{1,2,2,2,3\}\), and their unique edges joining degree-one vertices to degree-three vertices differ: the first has no such edge, while the second has one. Direct summation gives \(H_1=24\), \(H_2=23\), so the exact CDF difference follows. Since the distributions agree throughout \([0,1]\), no smaller radius can detect an invariant not determined by the degree sequence; every larger radius through \(3/2\) does detect this example.

## Verification
The accompanying pure-Python `verify.py` enumerates small connected graphs, includes the two witnessing graphs, and independently computes the areas of all geodesic short-distance events using exact rational polygon clipping and inclusion-exclusion over four endpoint routes for every ordered pair of edges. It checks the claimed formula at rational radii \(1/3,1,6/5,3/2\). Each comparison is exact in \(\mathbb Q\), without Monte Carlo or floating-point tolerances. The universal result follows from the geometric edge-pair classification, not the finite checks.

## Relationship to prior work
Elenbogen and Fink (2007) analyze Wiener polynomials and graph-vertex distance distributions for network families; their distribution samples vertices, not continuously distributed edge points, and their statement does not imply recovery of edge-degree mixing from a short initial interval. Wei, Walteros and Batta (first public 27 November 2019), *On the distance between random events on a network*, Theorem 4 and Section 8, develop a substantially more general **forward** probability-density and distribution framework for arbitrary edge-weighted networks and sampling distributions, proving that the uniform-event PDF is piecewise linear. That powerful forward result necessarily specializes to our CDF after carrying out the endpoint geometry, so the piecewise-quadratic forward aspect is **not** asserted independent of their general theory. The distinct contribution claimed here is the universal explicit **inverse recovery of edge count, degree-square sum and edge-degree correlation solely from the short-distance law**, with a sharp first-separation example for graphs sharing the complete degree sequence. A bibliographic or conceptual formulation of the same inverse facts in other graph-reconstruction literature is possible and requires independent historical scrutiny.

## Limitations
The inverse theorem does not recover the entire graph or degree sequence. The claimed threshold is sharp for detection of edge-degree mixing for some fixed degree sequence, not an assertion that all same-degree graphs separate immediately. The sample law requires continuous uniform normalized arclength along every unit edge, not uniformly sampled graph vertices, unequal edge lengths or ambient Euclidean distances. The predecessor forward framework is stronger for calculating arbitrary full-network CDFs. The historical novelty of the inverse interpretation has not been independently certified.

## References
1. B. S. Elenbogen and J. F. Fink, *Distance distributions for graphs modeling computer networks*, Discrete Applied Mathematics 155 (2007), 2612–2624, DOI:10.1016/j.dam.2007.07.020; publication listing dated 1 November 2007.
2. N. Wei, J. L. Walteros and R. Batta, *On the distance between random events on a network*, Networks 75 (2020), 203–231, DOI:10.1002/net.21919, first online 27 November 2019; particularly Theorem 4 and Section 8.
