# Independent mathematical audit

## correctness

PASS

For a vertex cover \(S\), the zero coordinates of an edge-distance vector are exactly its selected endpoints. Two edges with the same intersection with \(S\) must therefore be \(sx\) and \(sy\) with distinct unselected neighbors of the same selected vertex. In a lollipop, a nonattachment clique vertex cannot have two such neighbors; at the attachment vertex the only possible pair is an omitted clique vertex versus \(p_1\), distinguished by selected \(p_2\); at a path vertex, two omitted path neighbors are distinguished by any selected nonattachment clique vertex. Thus every cover edge-resolves. The two cases \(c\in S\) and \(c\notin S\) give the exact minimum-cover size; standard path-cover structure gives the odd/even counts. An independent exhaustive reconstruction for \(3\le m\le5\), \(2\le\ell\le6\) verified every vertex cover and the basis formulas, as corroboration only.

## originality

PASS

The 2023 paper introducing dominant edge metric dimension treats complete graphs, complete bipartite graphs, paths, cycles, wheels, and several graph products; full-text inspection/search did not find lollipop graphs. Separate lollipop papers determine local or strong metric dimension, which are different vertex-resolving invariants and do not imply a vertex-cover-constrained edge metric parameter. Resultary likewise returned no earlier dominant-edge lollipop theorem. No stronger inspected theorem implies that every vertex cover of a lollipop edge-resolves.

## value

PASS

Lollipop graphs are a standard graph family and dominant edge metric dimension is a recently introduced natural hybrid invariant. The theorem identifies a family-specific mechanism making every vertex cover resolve edges and gives the complete minimum-basis census, not merely one scalar value. This is a natural exact family calculation with reusable structural content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
