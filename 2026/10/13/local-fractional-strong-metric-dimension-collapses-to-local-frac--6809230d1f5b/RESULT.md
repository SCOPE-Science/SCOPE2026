# Local fractional strong metric dimension collapses to local fractional metric dimension

## Finding

For every finite connected simple graph \(G\) and every edge \(uv\), the local strong resolving neighborhood \(L_S(u,v)\) equals the ordinary local resolving neighborhood \(L(u,v)\). Thus the fractional linear programs have the same feasible functions, the same optimum, and the same set of minimizers:
\[
\operatorname{lsdim}_f(G)=\operatorname{ldim}_f(G).
\]
For a connected graph with at least one edge, the common value is \(1\) if and only if the graph is bipartite. For \(K_1\), the common value is \(0\). In particular, \(C_4\) is a counterexample to the claim that only paths have local fractional strong metric dimension \(1\).

## Assumptions and scope

Distances are ordinary unweighted graph distances. For an edge \(uv\), set
\[
L(u,v)=\{w\in V(G):d(w,u)\ne d(w,v)\}.
\]
The set \(L_S(u,v)\) consists of the vertices \(w\) for which \(u\) lies on a \(w\)-to-\(v\) geodesic or \(v\) lies on a \(w\)-to-\(u\) geodesic, allowing endpoints. A local resolving function is a function \(f:V(G)\to[0,1]\) with \(\sum_{w\in L(u,v)} f(w)\ge1\) for every edge. A local strong resolving function instead uses the sets \(L_S(u,v)\). The dimensions are the minima of \(\sum_{w\in V(G)} f(w)\) over the respective feasible sets.

## Proof

For an edge \(uv\), \(|d(w,u)-d(w,v)|\le1\) by the triangle inequality. If the distances are unequal, exchange \(u,v\) if necessary so that \(d(w,u)=d(w,v)+1\). A shortest path from \(w\) to \(v\) followed by \(vu\) has length \(d(w,u)\), so it is a geodesic containing \(v\). Conversely, if \(v\) lies on such a geodesic, then \(d(w,u)=d(w,v)+d(v,u)=d(w,v)+1\); the other geodesic condition likewise gives a difference of one. Hence the two neighborhoods are equal for every edge, so the constraints, objective, and minimizers are identical.

If \(G\) has at least one edge, each feasible function has total weight at least \(1\), because the constraint on any one edge requires weight at least \(1\) on a subset of vertices. If \(G\) is bipartite, distances from any \(w\) to adjacent vertices have opposite parity, so every neighborhood is \(V(G)\) and weight \(1\) concentrated at any vertex is feasible.

Conversely, suppose the minimum is \(1\). It is attained, since the feasible region is a nonempty compact polytope. For an optimal function of total weight \(1\), each edge constraint forces all vertices of positive weight to be in that edge's neighborhood. Fix one such vertex \(w\). Across every edge the distances from \(w\) differ by exactly one. The parity of distance from \(w\) is therefore a bipartition of \(G\). In \(K_1\) there are no edge constraints and the zero function is optimal. In \(C_4\) the common value is \(1\) by the bipartite case, although \(C_4\) is not a path.

## Verification

The shortest-path argument proves the neighborhood identities for every graph in scope. The included checker enumerates connected labeled simple graphs of orders \(2\) through \(6\), compares the two neighborhood predicates for every edge and vertex, and tests \(C_4\) explicitly. The checker is corroborative; the value for \(K_1\) follows directly from the unconstrained linear program.

## Relationship to prior work

Benish, Murtaza, and Javaid [1] define the ordinary local fractional program and state the value-one characterization for graphs of order at least two (Lemma 2.1 in the preprint). Jamil et al. [2] define local strong resolution on adjacent pairs using the geodesic condition. They state \(\operatorname{ldim}_f(G)\le\operatorname{lsdim}_f(G)\), and their Lemma 4 states a path-only characterization at value one for graphs of order at least two. The definitions imply equality edge by edge, which identifies the entire programs and corrects that characterization. The ordinary local fractional characterization is not claimed as a new result.

## Limitations

Adjacency is essential. The argument makes no identification of the ordinary and strong programs that constrain all pairs of vertices, or of versions using a different locality condition.

## References

1. H. Benish, M. Murtaza, and I. Javaid, “The Fractional Local Metric Dimension of Graphs,” arXiv:1810.02882v1 (2018); *Contributions to Discrete Mathematics* 19(3) (2024), 163–177, DOI 10.55016/ojs/cdm.v19i3.62807.
2. F. Jamil, A. Kashif, S. Zafar, Z. Bassfar, and A. M. Alanazi, “Local Fractional Strong Metric Dimension of Certain Rotationally Symmetric Planer Networks,” *IEEE Access* 9 (2021), 159326–159333, DOI 10.1109/ACCESS.2021.3131311.
