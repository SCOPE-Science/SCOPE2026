# Independent mathematical audit

## correctness

PASS

For K_n square K_2 with OPEN locating-total domination of ALL vertices, same-layer outside signatures are distinct iff at most one matching column is empty; top/bottom cross signatures separate when either layer has at least two selected. Total domination forces two occupied vertices in each nonempty layer except full opposite layer and the one-vertex matched-pair cases. Counting empty columns and column states with weighted inclusion–exclusion yields n>=4 polynomial t^n(t+2)^n+n*t^(n-1)(t+2)^(n-1)-2*n*t^n-2*n^2*t^(n-1), +6*t^2 at n=3, and 4*t^2+4*t^3+t^4 at n=2. It implies min n for 2<=n<=4 and n-1 for n>=5, counts 4,14,56,n(2^(n-1)-2n). Independent from source checker: enumerate all 2^(2n) labeled vertex subsets for each n=2..7 using direct adjacency and open-neighborhood signatures and compare EVERY coefficient, including boundaries. Proof unbounded, finite tests corroborative.

## originality

PASS

Relevant prior results give general bounds for twin-free cobipartite graphs, general line-graph location domination, and ordinary C_n prism graphs, not the all-cardinality open-neighborhood LTD polynomial of K_n square K_2. The same-graph Roman 3 domination record has distinct labeled functions. Best-of-knowledge original with historical indexing limitations.

## value

PASS

The size enumerator is a natural strengthening of a locating-total domination number on a canonical infinite cobipartite/line-graph family. It recovers the minimum and all equality configurations and detects the sharp change at n=5; the exact coefficient sequence is mathematically usable beyond a single small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
