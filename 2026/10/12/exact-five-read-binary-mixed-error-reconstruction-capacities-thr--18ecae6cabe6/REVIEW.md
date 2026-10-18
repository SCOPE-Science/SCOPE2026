# Independent mathematical audit

## correctness

PASS

For each n=4,...,8, the complete binary channel ball B(x) is the union of outputs after one deletion and at most one substitution, counting distinct outputs only. Five-read decoding requires |B(x)∩B(y)|≤4 for distinct codewords, equivalently to cliques in the fully built compatibility graph. Supplied witnesses attain 5,5,6,8,12. Independent fresh standard-library reimplementation checked all 2^n vertices, found edge counts 38,115,552,2917,15194 and rigorously colored-backtrack clique numbers 5,5,6,8,12 with search-node counts 6,6,7,100,1146. The greedy coloring comprises independent classes so clique cardinality is bounded by colors; reverse-order candidate enumeration and neighborhood restriction preserve all feasible branches. Finite exhaustive search proves exactly those lengths, not n≥9.

## originality

PASS

The principal 2026 five-read construction (Li–Sun–Ge) yields an achievable redundancy rate, not exact unrestricted small-n maxima or finite converse bounds. Its 2025 precursor concerns seven or more reads; Song–Cai–Quek imposes longer-block hypotheses. Indexed Resultary single-read exact mixed-error code sizes, while superficially close, use a different disjoint-ball (one-read) requirement, not the five-distinct-read intersection threshold. No checked source implies this five-value unrestricted optimum profile; an unindexed small-codebook table remains possible.

## value

PASS

The code sizes give complete unrestricted optimal message counts for the first four nonvacuous short-block binary five-distinct-read instances n=5,...,8, plus a carefully delineated n=4 vacuous boundary. They are direct finite-length performance benchmarks for a natural fixed-read deletion/substitution reconstruction channel; no general asymptotic theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
