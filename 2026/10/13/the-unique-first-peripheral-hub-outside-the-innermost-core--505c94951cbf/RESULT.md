# The unique first peripheral hub outside the innermost core
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph. For a vertex \(v\), let \(c(v)\) denote its core number: the largest integer \(k\) such that \(v\) survives in the \(k\)-core obtained by repeatedly deleting vertices whose current degree is less than \(k\).

Define the innermost-core vertex set by
\[
C(G)=\{v\in V:c(v)=\max_{u\in V}c(u)\}.
\]

Assume that \(G\) has a unique maximum-degree vertex \(h\).

If
\[
|V|\le 6,
\]
then
\[
h\in C(G).
\]

The bound is sharp. At order \(7\), exactly
\[
420
\]
of the
\[
1{,}866{,}256
\]
labeled connected simple graphs have their unique degree leader outside the innermost core. The exact labeled incidence is
\[
\frac{420}{1{,}866{,}256}=\frac{15}{66{,}652}.
\]

All \(420\) first failures form one isomorphism class. A representative on vertices \(0,\ldots,6\) has
\[
E=\{01,04,05,06,12,13,23\}.
\]
Its degree vector is
\[
(4,3,2,2,1,1,1),
\]
while its core-number vector is
\[
(1,2,2,2,1,1,1).
\]

Hence vertex \(0\) is the unique degree leader, but it is not in the innermost core. Vertices \(1,2,3\) form the innermost \(2\)-core.

Structurally, the representative is a triangle together with a degree-\(4\) hub joined to one triangle vertex and to three leaves. Its automorphism group has order
\[
12,
\]
so the labeled orbit has size
\[
\frac{7!}{12}=420.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

The degree leader is required to be unique. Without that condition, a maximum-degree set can intersect the innermost core even when another tied maximum-degree vertex lies outside it.

The core number is the standard peeling index: \(c(v)\) is the largest \(k\) for which \(v\) belongs to the \(k\)-core. The innermost core is the set of vertices having maximum core number.

The theorem concerns only the first graph order at which local degree leadership and innermost-core membership can conflict. It does not assert that core number is a universally superior influence measure.

## Proof
Let
\[
k=\max_{v\in V}c(v)
\]
and let
\[
C=C(G).
\]
If \(h\notin C\), then \(k\ge 2\), since in a connected graph with maximum core number \(1\), every vertex has core number \(1\).

Every vertex of \(C\) has at least \(k\) neighbors inside \(C\), so
\[
|C|\ge k+1.
\]
Moreover, \(h\) has at most \(k-1\) neighbors in \(C\); otherwise \(h\) would itself survive in the \(k\)-core.

Put
\[
r=|V\setminus C|.
\]
Then
\[
\deg(h)\le (k-1)+(r-1)=k+r-2.
\]
Using \(|C|\ge k+1\), we obtain
\[
\deg(h)\le |V|-3.
\]

Suppose first that \(|V|\le 6\). Then \(\deg(h)\le 3\). Because every vertex of \(C\) has degree at least \(k\) in the whole graph and \(h\) is the unique maximum-degree vertex, one has
\[
k<\deg(h)\le 3.
\]
Hence
\[
k=2,\qquad \deg(h)=3.
\]
Every vertex of \(C\) has at least two neighbors in \(C\), but uniqueness of \(h\) forces every such vertex to have total degree at most \(2\). Thus every vertex of \(C\) already uses its full degree inside \(C\). Since \(h\notin C\) and the graph is connected, some edge must join \(V\setminus C\) to \(C\), raising the degree of its endpoint in \(C\) to at least \(3\), a contradiction.

Now let \(|V|=7\) and suppose \(h\notin C\). The same bound gives
\[
\deg(h)\le 4.
\]
If \(k=3\), then uniqueness forces \(\deg(h)=4\) and every vertex of \(C\) to have total degree exactly \(3\). Connectivity again requires an edge from outside \(C\) into \(C\), which would create a degree-\(4\) vertex in \(C\), contradicting uniqueness. Hence
\[
k=2.
\]

If \(|C|\ge 4\), then \(r\le 3\), so
\[
\deg(h)\le r\le 3.
\]
The same connectivity argument again contradicts uniqueness. Therefore
\[
|C|=3.
\]
A \(3\)-vertex \(2\)-core is a triangle.

Now \(r=4\). The vertex \(h\) can have at most one neighbor in the triangle, and uniqueness forces
\[
\deg(h)=4.
\]
Therefore \(h\) is adjacent to exactly one triangle vertex and to all three remaining outside vertices.

Those three outside vertices can have no additional edge. Any extra edge between two of them, or from one of them into the triangle, creates a cycle through \(h\). Every vertex on a cycle has core number at least \(2\), contradicting \(c(h)=1\). Thus the three outside vertices are leaves.

Consequently every order-\(7\) failure is isomorphic to the displayed graph, proving the structural classification.

Its automorphisms independently permute the three leaves and swap the two triangle vertices not adjacent to \(h\). Hence the automorphism-group order is
\[
3!\cdot 2=12.
\]
The labeled orbit therefore contains
\[
7!/12=420
\]
graphs.

## Verification
The embedded `verify_degree_coreness_boundary.py` uses only the Python standard library.

It exhausts every labeled simple graph on \(2\) through \(7\) vertices, retaining exactly the connected graphs. The connected labeled counts reproduced are
\[
1,\ 4,\ 38,\ 728,\ 26704,\ 1{,}866{,}256.
\]

Core numbers are computed by exact minimum-degree peeling on the complete enumeration. Every order-\(7\) failure is then independently rechecked by direct \(k\)-core pruning, and connectivity is independently rechecked by transitive closure.

The replay verifies:
- no failure through \(6\) vertices;
- exactly \(420\) failures at \(7\) vertices;
- degree sequence \((4,3,2,2,1,1,1)\) for every failure;
- core-number multiset \((2,2,2,1,1,1,1)\) for every failure;
- one isomorphism class;
- representative edges \(\{01,04,05,06,12,13,23\}\);
- orbit size \(420\);
- automorphism-group order \(12\).

Run:

`python3 verify_degree_coreness_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Seidman's classical work introduced minimum-degree cores as a way to identify cohesive regions of social networks. In the original formulation, a \(k\)-core is an induced subgraph whose minimum degree is at least \(k\), and the paper emphasizes the distinction between cohesive regions and the less cohesive remainder of a network.

Kitsak and collaborators later used \(k\)-shell decomposition explicitly as a node-position measure for spreading. Their analysis stresses that highly connected hubs can occur in peripheral low-coreness layers, while less connected vertices in the network core can be more effective spreaders.

Those results establish that degree and coreness encode genuinely different structural information. They do not, in the inspected material, state the smallest connected graph on which a unique degree leader lies outside the innermost core, nor the complete first-order classification.

Targeted searches using maximum-degree, hub, \(k\)-core, \(k\)-shell, coreness, peripheral-hub, smallest-graph, seven-vertex, and unique-leader formulations did not locate the exact order-\(7\) boundary or the \(420\)-graph one-orbit census.

## Limitations
The theorem is restricted to connected simple undirected graphs.

The unique-degree-leader condition is essential to the stated boundary.

The result concerns structural position under core decomposition, not actual spreading performance under a specified epidemic, rumor, or information-diffusion process.

The exact census stops at seven vertices.

An unindexed graph atlas annotation, teaching example, thesis appendix, or software corpus could contain the same finite boundary.

## References
1. S. B. Seidman, “Network structure and minimum degree,” *Social Networks* 5(3), 269–287, 1983. DOI: 10.1016/0378-8733(83)90028-X.
2. M. Kitsak, L. K. Gallos, S. Havlin, F. Liljeros, L. Muchnik, H. E. Stanley, and H. A. Makse, “Identification of influential spreaders in complex networks,” arXiv:1001.5285, first submitted 28 January 2010; *Nature Physics* 6, 888–893, 2010. DOI: 10.1038/nphys1746.
3. G. F. de Arruda, A. L. Barbieri, P. M. Rodriguez, Y. Moreno, L. da F. Costa, and F. A. Rodrigues, “The role of centrality for the identification of influential spreaders in complex networks,” arXiv:1404.4528, 2014.
