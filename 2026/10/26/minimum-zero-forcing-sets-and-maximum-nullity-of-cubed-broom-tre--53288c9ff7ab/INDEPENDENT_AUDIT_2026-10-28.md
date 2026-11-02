# Independent mathematical audit

## correctness

PASS

Let B_{t,ell} have t>=2 brush leaves a_i at v_0 and path v_0...v_ell with ell>=2; cube adjacency means tree-distance at most 3. Brush leaves become a true-twin clique adjacent to v0,v1,v2. Reconstructed the Gram representation: assign identical interval vectors w0 to brushes and consecutive interval vectors w_{j+1} to v_j in R^{ell−1}, each supported on coordinate indices max(0,i−3)..min(i,ell−2). Two vectors overlap precisely at cube distance<=3 and these vectors span ell−1 dimensions, hence a real symmetric matrix with exact off-diagonal support and nullity t+2. The standard inequality M<=Z gives the lower bound Z>=t+2. Explicit forcing schedules of size t+2 reach all vertices using forward path forces v_{j−3}->v_j or reverse forces v_{j+3}->v_j, with omitted brush forced when the first three path vertices are black. Necessity: at most one brush is initially white because distinct true twins cannot be uniquely forced while both white. With t black brushes and two path vertices the only possible first force is from a brush, requiring two of v0,v1,v2; with t−1 brushes and three path vertices, the first force must come from brush or right endpoint, leaving exactly four path triples. This exhausts cases and yields 3+4t minimum sets for ell>=3. For ell=2 the cube is K_{t+3}, so t+3 minimum sets and Z=M=t+2. Independently built broom distance cubes and exhaustive zero-forcing simulations for 18 pairs 2<=t<=4,2<=ell<=7; all exact counts match, with no forcing sets of size t+1. Finite work corroborates but Gram rank/first-move argument proves the full infinite family.

## originality

PASS

Abiad–Flagg–Ghasemi Nezhad–Zeijlemaker (2026) study graph-power zero forcing and give exact path-power values and an upper bound for equal-arm spiders S_m(ell)^k; their Proposition 9 assumes all legs equal and does not enumerate minimum sets of a broom cube with many unit arms and one arbitrary handle. DeAlba et al. (2012) treat minimum ranks of path powers and strict powers/squares of trees; they do not classify min zero forcing sets of the usual cubic broom. A broader upper bound could overlap with the t+2 cardinality, and common true-twin forcing rules are standard; the assessed contribution survives as the exact uniform complete labeled minimum-set enumeration and simultaneous maximum-nullity equality. An unindexed combinatorial formula for broom powers remains a residual risk.

## value

PASS

Zero forcing number and maximum nullity are natural extremal graph invariants connected to inverse eigenvalue problems. For a sparse tree family whose cubes have large true-twin cliques, the exact stable count 4t+3 for all handle lengths ell>=3, the Gram witness establishing matching maximum nullity, and the complete first-move classification offer a precise infinite-family result. It is not merely a small computation or an arbitrary new graph power; it supplies a reusable twin/clique/path forcing template, while clearly limiting its scope to cubes of brooms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
