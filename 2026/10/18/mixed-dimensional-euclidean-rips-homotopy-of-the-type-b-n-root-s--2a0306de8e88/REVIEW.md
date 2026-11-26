# Independent mathematical audit

## correctness

PASS

Each long root is the sum of one edge of the short-root crosspolytope graph G; the two summands are its only short neighbors at distance 1 or at squared threshold 2. Distinct short roots are joined at squared distance 2 exactly when they have different supports. The distance-one graph is therefore the once-subdivided G, with rank |E|-|V|+1=2n(n-2)+1; nothing is joined below 1. For long roots, squared distance 2 means exactly one shared coordinate with matching sign. Pairwise-intersecting distinct two-element supports either form a star or the three edges of a triangle. In a star, antipodal choices of the other signed summand cannot be adjacent; the allowed faces form the stated crosspolytope base. The triangles on three supports have matching signs and give precisely 8 binom(n,3) exceptional long triangles. This leaves only the short crosspolytope boundary and the mixed bridge triangles in addition to the short-vertex cones. Each cone collapses relative to its radial edges by pairing nonvertex base faces with their cones, in descending dimension; separate cones meet only at untouched long vertices. Under this collapse, each side of an exceptional triangle retracts to the radial two-edge path in its cone, up to homotopy relative to endpoints. Thus the cones plus exceptional triangles form, up to homotopy, the short boundary's two-skeleton. It is simply connected and its Euler characteristic gives H_2 of rank 8 binom(n,3)-q, with q=2n(n-2)+1. Hurewicz and the simply connected homology Whitehead theorem give a wedge of that many 2-spheres. The bridge triangles give a mapping cylinder between the once-subdivided graph and the short graph, so the final gluing is the homotopy pushout over G. Both graph maps are null because the targets are simply connected, and the additional summand is the suspension of G, a wedge of q two-spheres. This proves the integral wedge with S^{n-1}, including the coincident dimensions giving nine 2-spheres at n=3. Coordinate integrality excludes squared pair distances strictly between 2 and 3, and the endpoints are inclusive as claimed.

## originality

PASS

Credit the established line-graph clique/two-skeleton mechanism and the exact B_3 overlap. The distinct supported statement is the uniform all-rank metric result and the short-sphere/bridge gluing that produces genuinely different homology dimensions for every n>=4; neither the known two-skeleton result nor the n=3 classification determines it.

## value

PASS

The two unequal Euclidean root shells form a canonical metric point cloud, and the first nontrivial thresholds are intrinsic rather than arbitrary. The mixed gluing yields a rank-uniform, torsion-free example with homology in both a fixed degree and a rank-dependent degree; knowing the long roots or a field Betti table would not explain the additional sphere or the integral attaching type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
