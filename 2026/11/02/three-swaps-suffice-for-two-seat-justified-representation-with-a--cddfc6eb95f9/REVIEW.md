# Independent mathematical audit

## correctness

PASS

For two seats the JR obstruction is at least ceil(n/2) unrepresented supporters of a single candidate. Take a maximum-support candidate z. Below half no JR obstruction exists; above half all z-pairs are JR. At exactly half, a failed pair {z,a} requires a witness whose support is precisely the complement of z's support, and a has no supporters in that complement. Pairing z with the witness gives a valid hub pair. If both z-replacements of a JR pair failed, neither of its members would cover any complementary voter, contradicting JR by the same witness. Thus the valid z-pairs form a nonempty dominating clique whenever it is needed. Pairwise distances follow: overlaps give one swap, a disjoint pair has a two-step path exactly via a JR cross pair, and otherwise it is at distance three. With at most four candidates every neighbour of a disjoint endpoint is a cross pair, so connectivity rules out a distance-three pair. In the six-voter witness e is universal: each endpoint misses two e-supporters while each cross pair misses three, and the e-hub path has length three. For five candidates I independently exhausted unordered tuples of ballot masks, fixing any disjoint endpoints by relabelling and checking JR by the original quota-size voter-group intersection condition, not the package's per-candidate count/BFS. The n=1,…,5 profile counts were 32, 528, 5984, 52360, 376992, with zero detours in every layer. The same check confirmed the six-voter witness's endpoint and bridge statuses.

## originality

PASS

The closest published reconfiguration framework does not imply unrestricted exact-JR two-seat connectivity, the sharp three-swap diameter, or the extremal witness. It distinguishes non-isolation, approximate intermediate committees, and geodesic paths for a restricted domain. The closest indexed two-seat same-day result concerns a different representation rule and objective.

## value

PASS

The theorem closes the unrestricted two-seat case of the published exact reconfiguration problem and identifies precisely when the natural Johnson shortest path fails. The minimal-candidate witness shows a genuine obstruction despite connectivity and supplies a concrete sharp test instance. The conditional voter cutoff is a supporting extremal fact rather than a standalone brute-force claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
