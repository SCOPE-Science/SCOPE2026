# Independent mathematical audit

## correctness

PASS

An ordinary two-row n-column ladder perfect matching crosses each intercolumn cut in zero or two edges by prefix parity; it is uniquely tiled by vertical rungs and horizontal two-column dimers, hence F_{n+1} perfect matchings. Querying nonoverlapping dimer cuts realizes all 2^{floor(n/2)} answer patterns. For a shattered support, all-one horizontal queries occupy 2h columns and other queried rungs lie outside; assign opposite parity rung-zero patterns to inject each queried rung into a distinct unqueried neighbor column, giving 2v<=n-2h and VC=floor(n/2). For n=11, a full depth-7 mistake tree is in ladder11_tree.json; independent exact enumeration of all 144 dimer-tilings and recursive certificate traversal verified 127 internal nodes, 128 distinct compatible leaf matchings, and every split nonempty. Upper bound floor(log2 144)=7. Restrict full 11m ladder to matchings without block-boundary dimers and concatenate m trees to get Ldim >=7m; VC=floor(11m/2). For n>=2 the outer cycle guarantees 2-connectivity and every edge occurs in some matching. No exact general-n Ldim is claimed.

## originality

PASS

General resonance graphs encode transitions among perfect matchings, and their cubical/Clar polynomial data concern a different graph and invariant from fixed/adaptive original-edge incidence queries. General Littlestone closure and complexity bounds do not give the exact eleven-column depth or connected all-edges-allowed linear gap; classical Fibonacci tiling enumeration is credited.

## value

PASS

A natural matching-covered, planar, bipartite, two-connected max-degree-three infinite graph family with an explicit unbounded difference between static and online shattering of edge-incidence concepts; complete depth-7 finite core with rigorously transferable bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
