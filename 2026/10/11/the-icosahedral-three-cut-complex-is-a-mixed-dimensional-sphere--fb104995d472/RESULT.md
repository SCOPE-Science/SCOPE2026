# The icosahedral three-cut complex is a mixed-dimensional sphere wedge

## Finding
For the twelve-vertex icosahedral graph \(I\), its ordinary three-cut complex satisfies
\[
\Delta_3(I)\simeq S^7\vee\bigvee^6 S^8.
\]
Its face vector (in dimensions zero through eight) is \((12,66,220,495,792,924,792,465,140)\). In particular, this pure eight-dimensional complex is not shellable: it has nonzero reduced integral homology in degree seven.

## Assumptions and scope
The graph \(I\) is specified by the complete thirty-edge list in `verify.py`; it has twelve vertices of degree five, each vertex's induced link is a five-cycle, and its twenty triangular faces give the usual icosahedral triangulation. For each three-element vertex subset \(T\), declare \(T\) disconnected exactly when the induced graph \(I[T]\) is disconnected (equivalently, it has at most one edge). The facets of \(\Delta_3(I)\) are precisely \(V(I)\setminus T\) for the disconnected triples \(T\). This is the ordinary, not the total, cut complex.

## Proof
There are \(\binom{12}{3}=220\) triples, of which exactly \(140\) are disconnected. Taking all subsets of their nine-vertex complements gives exactly \(3906\) nonempty faces and the face vector stated above. The script enumerates every face and every one of the \(22800\) Hasse covers.

Order the vertices as \((7,9,5,1,2,4,3,11,10,0,6,8)\). At each stage, among faces not previously paired, pair every available face \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\), removing both from subsequent stages. This creates \(1949\) disjoint matching pairs and leaves eight critical faces: one vertex, one seven-dimensional face, and six eight-dimensional faces. Reverse matched arcs and orient all other nonempty Hasse covers upward. Exhaustive topological sorting visits all \(3906\) nodes; thus the matching is acyclic and produces a CW model with one cell in degrees zero and seven and six cells in degree eight.

It remains to identify the attaching maps. Define the simplicial complex \(K\) on these twelve vertices to consist of all subsets containing no disconnected triple. The ordinary cut complex is its combinatorial Alexander dual \(K^\vee\). Exhaustive enumeration of \(K\) gives face vector \((12,66,80,30)\). Its signed rational simplicial boundary ranks in degrees one, two, and three are, respectively, \((11,49,30)\). Therefore \(\dim_{\mathbb Q}\widetilde H^1(K;\mathbb Q)=66-11-49=6\). Combinatorial Alexander duality on twelve vertices yields \(\dim_{\mathbb Q}\widetilde H_8(\Delta_3(I);\mathbb Q)=6\).

The Morse CW model has six eight-cells and a single seven-cell, so the integer cellular differential from degree eight to seven must be identically zero: otherwise its rational top homology would have dimension at most five. Every attaching map \(S^7\to S^7\) therefore has degree zero, hence is null-homotopic. Attaching the six eight-cells gives exactly \(S^7\vee\bigvee^6 S^8\). This also proves that all stated integral reduced homology is free, and proves nonshellability because a pure shellable eight-complex is homotopy equivalent to a wedge of eight-spheres only.

## Verification
Execute `python3 verify.py` with the Python standard library. The verifier constructs the graph from its displayed edges, checks vertex links, generates all cut-complex and Alexander-dual faces, tests all Hasse covers and matching orientations for acyclicity, and computes the three small dual boundary ranks by exact rational elimination. Its successful result begins `VERIFY_OK`. No probabilistic or truncated search is used in the finite computation.

## Relationship to prior work
Bayer et al. [1] define ordinary cut complexes and classify several graph families (including trees, cycles, complete multipartite graphs, squared cycles, and prisms over cliques), but do not state the icosahedral three-cut homotopy type. Their triangle-free classification is for the two-cut complex, and their chordal criterion is a sufficient shellability condition for three-cuts; neither implies this computation. The sequel [2] treats disjoint unions, squared paths, and grids rather than the icosahedron. The total cut complex [3] uses independent triples instead of disconnected triples: those are distinct for a graph containing twenty triangles and many induced single-edge triples. This result provides a natural triangle-rich Platonic example with homology in two adjacent degrees, rather than a single-dimensional sphere wedge.

## Limitations
The assertion concerns only the ordinary three-cut complex of the specified icosahedral graph. It does not classify all Platonic graphs, all cut parameters, equivariant homology, or combinatorial manifold structure. Literature searches are evidence of noncoverage rather than a proof that no equivalent result exists. Independent validation has not been performed.

## References
[1] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26; SIAM Journal on Discrete Mathematics 38 (2024).

[2] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first posted 2024-07-11.

[3] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27.
