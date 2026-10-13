# Six vertices are the sharp unique-maximizer split for degree and betweenness centrality
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph.

For a vertex \(v\), use degree
\[
C_D(v)=\deg(v),
\]
closeness
\[
C_C(v)=\frac{|V|-1}{\sum_{u\ne v}d(u,v)},
\]
and unnormalized Freeman betweenness
\[
C_B(v)=
\sum_{\{s,t\}\subseteq V\setminus\{v\}}
\frac{\sigma_{st}(v)}{\sigma_{st}},
\]
where \(\sigma_{st}\) is the number of shortest \(s\)-\(t\) paths and \(\sigma_{st}(v)\) is the number of those paths containing \(v\) internally. Standard positive normalizations of degree or betweenness do not change their maximizers.

If \(G\) has at most \(5\) vertices and both \(C_D\) and \(C_B\) have unique maximizers, then those two maximizing vertices are the same.

This is sharp. Among the
\[
26704
\]
labeled connected simple graphs on \(6\) vertices, exactly
\[
720
\]
have a unique degree maximizer and a unique betweenness maximizer that are different. The exact labeled incidence is
\[
\frac{720}{26704}=\frac{45}{1669}.
\]

All \(720\) first-conflict graphs lie in one isomorphism class. Its orbit under all vertex relabelings has size
\[
720=6!,
\]
so the representative has trivial automorphism group.

Moreover, in every member of this class, closeness also has a unique maximizer and that maximizer is the degree maximizer, not the betweenness maximizer.

A representative on vertices \(0,1,2,3,4,5\) has edge set
\[
\{01,03,05,12,13,14,23,24\}.
\]
Its degree vector is
\[
(3,4,3,3,2,1),
\]
its closeness vector is
\[
\left(\frac57,\frac56,\frac58,\frac57,\frac59,\frac5{11}\right),
\]
and its unnormalized betweenness vector is
\[
\left(4,\frac72,\frac12,1,0,0\right).
\]
Thus vertex \(1\) is the unique degree and closeness maximizer, while vertex \(0\) is the unique betweenness maximizer.

There is a separate tie-level threshold one order earlier. Exactly
\[
150
\]
of the \(728\) labeled connected graphs on \(5\) vertices have different degree-maximizer and betweenness-maximizer sets, but none has both maximizers unique. Hence five vertices suffice for disagreement of maximizing sets, whereas six are necessary and sufficient for disagreement between two unambiguous leaders.

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and labeled when counts are stated.

The betweenness convention sums over unordered endpoint pairs and excludes the focal vertex from the endpoints. Dividing by the usual graph-order-dependent positive normalization leaves all maximizing sets unchanged.

Likewise, using normalized degree \(C_D(v)/(n-1)\) rather than raw degree leaves the degree maximizing set unchanged.

The result concerns the maximizing vertices of three classical centrality measures. It does not assert an ordering relation between their complete vertex rankings.

The exhaustive statement stops at six vertices. No frequency claim is made for larger graphs.

## Proof
Every simple graph on \(n\) labeled vertices is encoded by a bit vector on the \(\binom n2\) possible edges. The verifier enumerates all such vectors for \(1\le n\le6\), retains exactly the connected graphs, and obtains the known connected labeled counts
\[
1,\ 1,\ 4,\ 38,\ 728,\ 26704.
\]

For each connected graph, all-pairs shortest-path distances are computed independently by breadth-first search from every source and by Floyd--Warshall. The distance matrices agree exactly.

Degree centrality is read directly from adjacency.

Closeness is computed from each of the two independently obtained distance matrices and the resulting exact rational vectors agree.

Betweenness is computed in two independent exact forms. The first explicitly counts shortest paths between every unordered endpoint pair and allocates the fraction
\[
\frac{\sigma_{st}(v)}{\sigma_{st}}
\]
to each internal vertex. The second uses the exact Brandes dependency recurrence over every source and divides the ordered-source total by two. The two rational vectors agree for every connected graph through six vertices.

The numbers of connected labeled graphs whose degree-maximizer and betweenness-maximizer sets differ are
\[
0,\ 0,\ 0,\ 0,\ 150,\ 9150
\]
for orders \(1,\ldots,6\).

After restricting to graphs for which both measures have unique maximizers, the corresponding conflict counts are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 720.
\]
The same exact counts are obtained for unique closeness-versus-betweenness conflicts.

For every one of the \(720\) six-vertex degree-versus-betweenness conflicts, the closeness maximizer is checked to be unique and equal to the degree maximizer.

Canonicalization under all
\[
6!=720
\]
vertex permutations sends all \(720\) conflict graphs to one canonical edge mask. Conversely, the full relabeling orbit of that representative contains \(720\) distinct graphs and is exactly the complete conflict set. Hence there is one isomorphism class and its automorphism group is trivial.

For the displayed representative, direct exact evaluation gives the three vectors in the Finding, proving the claimed split of unique maximizers.

## Verification
The embedded `verify_centrality_unique_boundary.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every connected labeled simple graph through six vertices;
- the connected-graph counts \(1,1,4,38,728,26704\);
- two independent all-pairs distance computations;
- two independent closeness computations;
- two independent exact betweenness computations;
- exactly \(150\) five-vertex degree-versus-betweenness maximizing-set disagreements;
- no distinct unique degree and betweenness maximizers through five vertices;
- exactly \(720\) distinct-unique conflicts at six vertices;
- exactly \(720\) distinct-unique closeness-versus-betweenness conflicts at six vertices;
- unique closeness and degree maximizers coinciding in every first-conflict graph;
- one six-vertex conflict isomorphism class;
- orbit size \(720\);
- the exact representative edge set and all three displayed centrality vectors.

Run:

`python3 verify_centrality_unique_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Freeman's 1977 paper formalized betweenness as a social-network centrality based on the fraction of geodesics through a vertex, and his subsequent conceptual clarification placed degree, closeness, and betweenness among distinct classical notions of centrality.

The later literature repeatedly emphasizes that these measures capture different structural roles. In particular, degree is local, closeness is distance-based, and betweenness measures placement on shortest paths. Worked social-network examples are therefore expected to rank actors differently under different centralities.

Unnithan, Kannan, and Jathavedan give exact betweenness formulas for several graph families, including paths, stars, wheels, complete bipartite graphs, and trees. Those formulas provide useful structural benchmarks but do not compare the smallest graph order at which degree and betweenness choose different unique leaders.

The inspected literature therefore already owns the qualitative fact that centrality notions can differ. The contribution here is only the sharp finite obstruction statement: no connected graph through five vertices can have two different unique degree and betweenness leaders; at six vertices exactly one asymmetric isomorphism class does, with \(720\) labeled realizations, and closeness sides with degree throughout that entire first layer.

Targeted searches using degree-versus-betweenness terminology, unique-maximizer and smallest-graph formulations, the order-six restriction, the exact count \(720\), the connected-graph count \(26704\), and the representative structure did not locate this exact boundary or quotient census.

## Limitations
The theorem is restricted to connected simple undirected graphs.

The result concerns maximizers, not agreement of full centrality rankings.

At five vertices, maximizing sets can already differ through ties, so the six-vertex threshold applies specifically to distinct unique maximizers.

The exhaustive census stops at six vertices. It does not predict the density or isomorphism structure of conflicts for larger orders.

An unindexed small-graph database, thesis appendix, software corpus, or teaching enumeration could contain the same finite boundary.

## References
1. L. C. Freeman, “A Set of Measures of Centrality Based on Betweenness,” *Sociometry* 40(1), 35–41, 1977. DOI: 10.2307/3033543.
2. L. C. Freeman, “Centrality in social networks: Conceptual clarification,” *Social Networks* 1(3), 215–239. DOI: 10.1016/0378-8733(78)90021-7.
3. R. R. Unnithan, B. Kannan, and M. Jathavedan, “Betweenness Centrality in Some Classes of Graphs,” *International Journal of Combinatorics*, Article 241723, 2014. DOI: 10.1155/2014/241723.
4. S. Das, “On Local and Global Centrality in Large Scale Networks,” arXiv:1405.5512, 2014.
