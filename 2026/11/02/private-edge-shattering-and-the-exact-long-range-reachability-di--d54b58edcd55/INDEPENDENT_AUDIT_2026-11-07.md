# Independent mathematical audit

## correctness

PASS

PASS. In a fixed undirected tree, an oriented reachability query equals conjunction of prescribed edge signs on its unique path. For a shattered set, all-one realizability forces orientation compatibility; one-negative/all-other-positive labeling forces a private edge of that query. Conversely, orient all positive paths consistently and reverse a distinct private edge of each negative query; other query paths cannot be affected, realizing every labeling. On a path, intervals each having private points form a strict two-sided antichain. A middle interval must contain a private point outside its predecessor and successor, forcing L_{i+2}>=R_i+2 and hence R_{i+2}>=R_i+d+1. Initial R1>=d,R2>=d+1 yield k<=2q+1_{r=d}; two overlapping length-d intervals per disjoint length-(d+1) block with last d-edge tail when r=d achieve equality. Independently brute-force maximized private-point interval systems for all 2<=d<=m<=8. This establishes the exact domain for all finite tree supports and for path m>=d>=1; finite brute force only corroborates.

## originality

PASS

PASS best-of-knowledge: known hidden-directed-graph path-query reconstruction complexity studies and Kozma–Moran orientation/VC connectivity duality are related but study different hypothesis/query domains. They do not state or directly imply the private-edge iff criterion for the concept class of all orientations with ordered-pair reachability coordinates nor its sharp distance-cutoff path VC dimension.

## value

PASS

PASS. Exact shattering characterization for an arbitrary tree and closed VC dimension for a natural restricted query domain on a path quantify the sample/query capacity of orientation reachability, distinct from graph reconstruction. The threshold d and extremal interval construction are intrinsic and may guide learning-theoretic analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
