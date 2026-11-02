# Independent mathematical audit

## correctness

PASS

An uncolored vertex must see all r=m+n−2 labels on its exactly r neighbors, so no two uncolored vertices share a row/column. For a j-matching support, any two uncolored vertices share precisely the two off-diagonal colored cells (i,h),(h,i), and all other colored neighbors are unique to one support vertex. Therefore a valid assignment is equivalent to an edge-coloring of 2K_j using <=r colors, with residual labels freely assigned to unique neighbors. Exact factorization gives chi’(2K_j)=2j−2 for even j>=2 and 2j for odd j>=3; j<=1 is vacuous. Comparing r with the index yields the sole obstruction j=m odd, n=m or m+1, with the stated binomial-matching polynomial and optimum. Independent backtracking against direct shared-neighbor proper color constraints checked j<=4 and boards up to 5x7; exhaustive finite checks corroborate, not replace, the infinite factorization proof.

## originality

PASS

PASS, qualified. Lange 2026 defines exactly this singleton full-degree rainbow model, but his general independence bound and results for cycles, Möbius ladders and prisms do not include rectangular rook graph support enumeration. Mertens 2024 studies the ordinary domination polynomial on rook graphs, which is a different invariant. Žerovnik 2026 studies singleton 3-rainbow domination on path-cycle cylinders. The edge-coloring obstruction and exact parity exceptional coefficient remain distinctive in inspected coverage; unindexed equivalent line-graph formulations are a plausible residual risk.

## value

PASS

A full support-enumerator for the canonical Cartesian product of complete graphs is mathematically natural and stronger than its domination number. The doubled-clique obstruction yields a sharp odd near-square one-vertex transition and complete optimal support multiplicities, a genuine color-consistency phenomenon invisible to independence counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
