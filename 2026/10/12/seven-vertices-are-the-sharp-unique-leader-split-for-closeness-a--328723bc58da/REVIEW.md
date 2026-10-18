# Independent mathematical audit

## correctness

PASS

For every connected simple undirected Graph Atlas representative on n=2..7 vertices, closeness maximizers minimize exact integer farness Σd, while harmonic maximizers maximize Σ(1/d). Independent BFS and Floyd–Warshall distances agree on inspected representatives, and a separate NetworkX graph_atlas_g census (which reconstructs connected unlabeled graphs rather than reproducing embedded data rows) independently yields connected class counts 1,2,6,21,112,853. Maximizer-set differences occur in 0,0,0,0,3,22 classes for n=2..7; distinct singleton-maximizer differences occur only in two n=7 classes. Both classes have closeness leader distances (1,1,2,2,2,3), farness 11, harmonic score 23/6, and harmonic leader distances (1,1,1,2,3,4), farness 12, harmonic 49/12. Exact all-permutation automorphism checks give size 2 and 7!/2=2520 labeled classes each, 5040 total; n=6 ties give 360+180+360=900 labeled. This is a genuinely exhaustive FINITE n≤7 classification conditional on standard Atlas completeness, not extrapolation to n>7.

## originality

PASS

Harmonic centrality and closeness are classical, and recent Madaras–Paralič 2026 work directly studies harmonic centers. Its accessible full text deals with harmonic-center geometry and realizability, not the exact first-order distinct unique maximizer comparison. The result is a natural sharp smallest-order obstruction with complete two-isomorphism-class census. A graph atlas annotation or thesis table could conceivably have recorded the same comparison, so originality is best of knowledge.

## value

PASS

Closeness and harmonic centrality are two canonical but inequivalent graph center notions. Their smallest order at which **both** make unambiguous conflicting choices is a natural cutoff; the two nonisomorphic optimal witnesses, identical contrasting distance profiles and exact first-layer frequency explain the mechanism, not just report a tiny graph. The computation is a complete meaningful boundary classification over all connected graphs up to n=7 rather than an arbitrary subset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
