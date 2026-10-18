# Research review: a sharp eleven-vertex unicyclic turnover

## Correctness — PASS
The underlying invariant is precisely the external-neighbor characterization of \(P_3\)-convexity. The finite portion has a complete constructive exhaustiveness argument: every unicyclic graph is a tree plus one extra edge; the rooted multiset recursion spans all trees; center-canonical forms remove only genuine tree isomorphisms; and all subsets of every listed graph are tested. The exact table through ten gives a unique cycle-maximizing case at each order. The cycle transfer matrix, explicit four-cycle pendant-star classification and the induction from the verified \(\(486<532\)\) base establish nonoptimality at every larger order. `certify.py` executed successfully with no external dependencies. Limits: the finite enumeration is computationally certified, not hand-classified graph by graph; the all-order inequality is proved separately, not extrapolated.

## Originality — PASS with bibliographic limits
The motivating preprint arXiv:2603.04706v1 studies the invariant and proves that a unicyclic graph has fewer convex subsets than a spanning tree, but does not compare unicyclic graphs of equal order. Its tree algorithm and path recurrence do not imply a uniqueness census for unicyclic graphs nor the first-order threshold. The 2017 Helly-number work concerns a different statistic. Searches of published mathematical records for the exact invariant, two-neighbor closed sets, unicyclic extremality, cycle/pineapple formulas and aliases found no covering result. An unindexed equivalent theorem remains possible; older peripheral sources available only as abstracts cannot support whole-document exclusion claims.

## Value — PASS
This answers a canonical, sharply delimited next extremal question raised by the 2026 counting framework: are cycles extremizers when one restricts connected graphs to cycle rank one? The answer changes for the first time at exactly eleven vertices. The result includes a complete finite uniqueness certificate and an explicit infinite counterfamily with exponential leading term. This threshold is not an arbitrary graph slice, a mere coefficient recomputation, or a consequence of a global connected-graph maximum theorem.

## Boundaries
The exact maximum and its maximizers for order eleven and above are not determined. The witness family proves only that the pure cycle is not optimal, not that the witness is optimal. Published and private comparison is best-knowledge, not independent external validation.

Self-review: passed. Independent audit: not yet performed.
