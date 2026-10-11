# Independent mathematical audit

## correctness

PASS

Every geodesic in a connected complete multipartite graph has at most two edges. A two-edge geodesic has endpoints in one part and its middle vertex in one other part, so both edges lie in a single complete bipartite block \(E(X_i,X_j)\). Therefore block \((i,j)\) needs at least \(\lceil n_i n_j/2\rceil\) geodesics. This bound is attained blockwise: if one side has even order, pair its incident edges at vertices of the other side; if both sides are odd, pair all but one edge per vertex and pair the remaining even number at a chosen opposite vertex, leaving one single edge. Thus cover and partition numbers equal the sum of the block ceilings. Exactly the odd-odd blocks contribute the parity excess, giving \((|E|+\binom{o}{2})/2\). Since no geodesic contains three edges, the whole edge set is edge-general-position, so \(\operatorname{gp}_e=|E|\) and dual equality holds exactly when \(o\le1\).

## originality

PASS

The complete 2025 primary article defines the edge-geodesic cover/partition framework and its dual inequalities, but its exact families are torus graphs, hypercubes, and Beneš networks; its conclusion contains no complete-multipartite result. The earlier path-cover survey concerns vertex isometric-path covers, a different optimization object. Targeted Resultary and exact literature searches found no complete-bipartite or complete-multipartite edge-geodesic formula or parity correction.

## value

PASS

Complete multipartite graphs are a canonical family for a recently developed edge-geodesic duality. The theorem simultaneously gives exact cover and partition numbers, an explicit parity defect, and the precise condition for tightness of the edge-general-position dual bound. The classification is natural rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
