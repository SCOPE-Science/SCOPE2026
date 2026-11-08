# Independent mathematical audit

## correctness

PASS

PASS. For every q>=2 the target words are exactly abab for all a,b in a labeled alphabet. In a cyclic list of distinct targets the suffix-prefix overlap between different targets has shifts 1,3 or 4 (never 2). A shift-1 transition uses one opposite ordered pair {abab,baba}; there can be at most binom(q,2) in the one connected tour. Contract chosen pairs; unmatched pairs and shift-4 transitions must connect all q symbol states, so 2s+z>=q. The cost bound then gives 2q(q+1). Grouped order aaaa,(abab,baba) for b>a achieves exact count of shift-1,3,4 transitions and a single cyclic witness. Independently implemented subset Held–Karp Hamiltonian-tour DP gave 12,24,40 at q=2,3,4. Finite DP corroborates, but arbitrary-q connectivity proof is the main certificate.

## originality

PASS

PASS, best of knowledge. Restricted-word universal cycles in Chen–Kitaev–Sun and Gardner–Godbole concern exact-once cycles or other motif sets; general cyclic-cover algorithms and shortest-superstring methods do not state the all-q tandem-square single-cycle length. An algorithm may compute individual q but does not imply the closed formula or the letter-connectivity lower bound without solving these instances. Unindexed tandem motif literature is a residual risk.

## value

PASS

PASS. A clean all-alphabet exact asymptotic/order-two covering invariant for a natural motif class, with a structural graph-connectivity obstruction rather than merely a computational small-case minimum. Clarifies why naive maximal-overlap matching underestimates one-cycle length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
