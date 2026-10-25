# Two extremal eleven-tile animals in the \(\{4,5\}\) tessellation

## Finding

In the regular hyperbolic square tessellation \(\{4,5\}\), the minimum boundary-edge perimeter among connected animals made of exactly \(11\) tiles is \(18\). Exactly two extremal animals occur up to tessellation isometry. Each is the union of all tiles incident to three interior vertices forming a path of two edges; in one type the path endpoints are opposite corners of a square, while in the other they share no tile.

## Assumptions and scope

A \(\{4,5\}\)-tessellation is the regular hyperbolic tiling by squares with five squares incident to every vertex. An animal is a finite connected set of tiles with connected interior. Its perimeter is the number of boundary edges, not a metric length. Two animals are equivalent when a symmetry of the tessellation maps one tile set to the other. A vertex is interior when all five tiles incident to it belong to the animal.

The statement concerns exactly \(11\) tiles in this one tessellation. It does not claim an enumeration for other tile counts or for other \(\{p,q\}\)-tessellations.

## Proof

For a vertex \(v\), write \(T(v)\) for its five incident tiles. In this tessellation, two distinct vertices share two tiles if they are adjacent, one tile if they are opposite corners of a square, and no tile otherwise. The vertex graph is bipartite, has no triangles, and the five neighbors of any vertex form a cyclic link of length five. Every four-cycle in this graph is a square face: if a four-cycle enclosed \(F\ge2\) square faces, Euler's formula for the enclosed disk would give \(F-1\) interior vertices and \(2F-2\) edges not on the boundary. The total degree available to the interior vertices would then be at most \(4F-4\), less than \(5(F-1)\), impossible because each interior vertex has degree five.

First, at most three vertices can be interior in an animal of \(11\) tiles. Suppose instead that four distinct vertices are interior, and let \(X\) be their set. The union \(U=\bigcup_{v\in X}T(v)\) is contained in the animal and so has at most \(11\) tiles. Let \(P\) be the sum of \(|T(u)\cap T(v)|\) over the six pairs in \(X\). Since each \(T(v)\) has five tiles, the elementary union bound gives \(|U|\ge 20-P\).

Let \(e\) be the number of adjacent pairs in the induced vertex graph on \(X\). If \(e\le2\), then \(P\le 2e+(6-e)\le8\). If \(e=3\), triangle-freeness makes that graph either a four-vertex path or a three-leaf star. For a path, the pair at graph distance three cannot share a square; for a star, among three leaves in a five-cycle link, at most two pairs are consecutive. Thus at most two nonadjacent pairs share a tile, again giving \(P\le8\). In either case \(|U|\ge12\), a contradiction. If \(e=4\), the induced graph is a four-cycle and hence the boundary of one square. The union of the incident-tile sets of its four corners consists of the central square, four squares across its edges, and eight further squares incident to one corner each, for a total of \(13\) tiles. This is also impossible. Therefore an 11-tile animal has at most three interior vertices.

Next, classify triples \(X=\{a,b,c\}\) whose incident-tile union has at most \(11\) tiles. There are \(15\) vertex-tile incidences. If no pair of centers is adjacent, at most three pairwise intersections are nonempty, so the union has at least \(12\) tiles. If exactly one pair is adjacent, the other two pairs cannot both be opposite corners of squares: those two requirements would force \(c\) to have the same bipartition class as both endpoints of an edge. Thus at most three pairwise intersections contribute, and the union again has at least \(12\) tiles. Three pairwise adjacent centers are impossible because the vertex graph has no triangles.

The only remaining possibility is that exactly two pairs are adjacent, so the centers form a two-edge path. The adjacent pairs each share two tiles. Its endpoints either share one tile, in which case they are opposite corners of the same square and that square is common to all three centers, or share no tile. Inclusion-exclusion gives \(15-(2+2+1)+1=11\) tiles in the first case and \(15-(2+2)=11\) in the second. In the five-cycle link around the middle center, unordered pairs of neighbors have exactly two orbits under tessellation symmetries: cyclic separation one and cyclic separation two. These give precisely the two endpoint types just described.

For each type, the union of the three incident-tile sets is connected and has no hole: the incident-tile patches of adjacent centers overlap in the two tiles around their common edge, so their union is a disk-like neighborhood of the path. It has exactly \(11\) tiles and three interior vertices. It has no fourth interior vertex by the four-center bound. Thus both types are extremal candidates, and no other triple of interior vertices fits in \(11\) tiles.

For a hole-free animal with \(n\) tiles, let \(e_2\) be its number of shared edges, \(e_1\) its boundary-edge perimeter, and \(h\) its number of interior vertices. The dual Euler relation is \(h=1+e_2-n\), while edge counting gives \(e_1=4n-2e_2\). Consequently

\[
 e_1=2n+2-2h.
\]

Malen, Roldán, and Toalá-Enríquez prove that any minimum-perimeter animal has no holes and that the spiral construction attains the minimum for each fixed tile count. For \(n=11\), the four-center bound gives \(h\le3\), so every minimum-perimeter animal has perimeter at least \(24-2\cdot3=18\). The two constructions above attain \(18\). Equality forces \(h=3\), and the triple classification shows that the two listed types are the only extremal animals up to isometry.

## Verification

The incidence count uses only the local facts that five squares meet at each vertex, adjacent vertices share exactly two incident squares, opposite corners share one, and the vertex link is a five-cycle. The four-center exclusion is by pair-intersection bounds and the unique four-cycle face property. The three-center classification is exhaustive by the number of adjacent pairs and the five-cycle link orbits. Euler's relation and edge counting then give the exact perimeter. No finite computation is used as a substitute for the proof.

## Relationship to prior work

Malen, Roldán, and Toalá-Enríquez prove that spiral \(\{p,q\}\)-animals minimize perimeter and that minimum-perimeter animals have no holes. Their enumeration section gives five extremal \(\{4,5\}\)-animals at \(9\) tiles and proves uniqueness for certain special sequences, but does not state the isometry-class count at \(11\) tiles. Roldán and Toalá-Enríquez later give closed perimeter formulas for hyperbolic animals, including \(\{4,5\}\), but do not enumerate extremal isometry classes. The present claim adds the exact equality-case classification at this tile count; the perimeter-minimization theorem itself is prior work.

## Limitations

The classification is restricted to \(11\)-tile animals in the regular \(\{4,5\}\) tessellation. It does not enumerate all animals of that size, count labeled embeddings, or classify extremal animals for other tile counts. The literature comparison cannot rule out an unindexed source that already records this exact small case; no independent audit has been performed.

## References

1. G. Malen, É. Roldán, and R. Toalá-Enríquez, “Extremal \(\{p,q\}\)-Animals,” arXiv:2109.05331v1 (first public 2021-09-11); *Annals of Combinatorics* 27 (2023), 169–209, DOI: 10.1007/s00026-022-00631-1. Relevant results: Theorem 1.8, Corollary 5.6, Theorems 6.3–6.4, and the \(9\)-tile example in Section 6.
2. É. Roldán and R. Toalá-Enríquez, “Isoperimetric Formulas for Hyperbolic Animals,” arXiv:2206.14910v1 (first public 2022-06-29); *Graphs and Combinatorics* 41 (2025), article 38, DOI: 10.1007/s00373-025-02900-1. Relevant results: the minimum-perimeter formula and the table of small \(\{4,5\}\)-perimeters.
