# Independent mathematical audit

## correctness

PASS

With old state x_v and s_v active neighbors outside v, the closed-count rule is exactly s_v≥x_v+1. To check the order reduction independently, orient each edge by its endpoint order. Schedules for one orientation are linear extensions and differ by adjacent swaps of incomparable, nonadjacent vertices, whose local updates commute. A source-to-sink flip cyclically shifts an update at the start to the end; writing the two global maps as BA and AB, A intertwines them and is bijective on their periodic states (injectivity from BA being a permutation there, surjectivity via AB on its periodic states and the intertwiner B). All orientations of a tree are connected by such flips and their inverses: delete a leaf, realize the flips on the smaller tree, flipping the leaf first if it blocks its parent's scheduled source flip, and then adjust the final leaf edge. Thus lengths and cycle multiplicities are schedule-independent, not necessarily transient graphs. A fresh exhaustive implementation generates rooted trees by multisets of smaller rooted types and deduplicates free trees by the least complete rooted code over all roots; this covers every class because each free tree has a rooting. It evaluates all 2^n states for each representative and counts each cycle once by marking completed traces. It reproduced 1,1,1,2,3,6,11,23,47,106 free trees; maxima 1,1,1,1,2,3,6,10,14,22; and maximizing-class counts 1,1,1,2,1,1,2,1,1,1. It found exactly two period-22 cycles in the unique extremal class, checked that the displayed labelled tree belongs to that class, and verified all 22 pairwise-distinct witness states and transitions, including 267→2. These maxima are ≤2n for every n<10 and 22>20. Replay: python3 /workspace/branches/fb7bca10-bc85-48da-84d2-b7125e18a1e7/independent_census.py, which printed INDEPENDENT_CENSUS_OK. The frozen verify.py was inspected, not run; contrary to the prose, it prints but does not assert all maximizing-tree counts, and checks its computed cycle rather than explicitly reading the printed tuple in RESULT.md. The fresh calculation checks both directly.

## originality

PASS

The earlier literature supplies both the order-equivalence reduction and long-cycle constructions, but the inspected results neither classify all trees of these sizes nor settle the first violation of 2n. The later-dated 9e5a9ef7f73d is a genuine stronger exact overlap: its certificate repeats every stated maximum and maximizer count, and the ten-vertex witness and multiplicity agree. It is not evidence that the census was already known when the frozen record was dated; no claim of priority over every possible source or of novelty relative to that later census is made. The inaccessible 2014 lead is a residual risk, not a ground for either scientific rejection or a finding of noncoverage.

## value

PASS

The order range is motivated by the first strict period-versus-size crossing, not chosen as an arbitrary census cap. The exact maximum 22 on ten vertices and upper bounds for every smaller tree establish a minimal-order witness that long-cycle existence theorems and selected examples do not give. Uniqueness of the witnessing class and the two-cycle multiplicity are useful exact checks for subsequent structural or enumeration work. A later extension corroborates the finite result without making the earlier mathematical gap arbitrary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
