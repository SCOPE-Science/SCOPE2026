# Independent mathematical audit

## correctness

PASS

Rebuilt from the frozen GP(8,3) vertex/edge rule and independently ran a complete 16-bit exhaustive Python program (not a repository log): zero among C(16,5)=4,368 five-subsets is zero forcing, exactly 1,704 among C(16,6)=8,008 six-subsets force all vertices, so monotonicity proves Z=6. Constructed all legal 1-for-1 exchanges: exactly 16,560 undirected edges, degree histogram 16:240,17:96,18:336,19:192,20:288,21:192,22:240,24:120. Independently BFSed from all 1,704 vertices: every eccentricity is six; unordered distance counts at j=1..6 are 16,560,127,008,417,720,565,488,276,792,47,388, Wiener sum 5,453,976. Every one of 1,450,956 pairs checked against Johnson distance: excess 0/1/2 counts 1,441,284/9,648/24; the 24 excess-2 pairs have 48 distinct degree-16 endpoints. Finite enumeration IS complete proof for this finite object, not a sample. One sentence in RESULT.md says 'find zero forcing five-subsets', contrary to the next sentence and actual check: this is an evident missing-negation editorial error, not an unverified five-subset claim.

## originality

PASS

Qualified PASS for the exact all-pairs distance, eccentricity, degree and Johnson-excess classification, excluding the established ordinary zero-forcing rule, graph GP(8,3), and general reconfiguration graph definition. No identified primary result implies the 1,704-state metric. The inaccessible plausible 2026 Petersen correction and unindexed graph tables remain genuine risks.

## value

PASS

PASS: GP(8,3) is a canonical sixteen-vertex cubic symmetric graph; reconfiguring minimum forcing sets by a legal one-swap is a natural discrete optimization object. This complete exact 1,704-state metric distinguishes nonregularity from self-centeredness and isolates a small sharp Johnson-distance obstruction, a usable finite benchmark beyond recomputing a known Z-number. No general-family claim is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
