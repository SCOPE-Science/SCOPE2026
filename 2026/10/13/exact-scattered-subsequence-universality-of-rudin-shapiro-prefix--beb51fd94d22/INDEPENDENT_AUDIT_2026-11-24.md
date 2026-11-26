# Independent mathematical audit

## correctness

PASS

The four morphism letters encode (parity of overlapping 11 pairs, last bit); their two children are exactly the append-0 and append-1 transitions in numerical order, including the leading-zero convention. Each full greedy arch embeds one prescribed letter, and requesting the successive arch-ending letters forces any embedding to reach at least the corresponding arch ends. Appending a letter missing from the tail proves the reverse bound. Recomputing from the one-letter scanner, at level 3 the exits for a,b,c,d are 1,2,1,2, with count triples (2,2,3),(2,2,3),(2,3,2),(2,3,2). Composition gives level-4 exits 2,1,2,1 and triples (4,4,5),(5,5,6),(5,6,5),(4,5,4). In a composition one adds the right count evaluated at the left exit; applying this to all four rows in both directions gives the stated parity tables with q replaced by 2q. The small-level maximum errors for all starting states are 11/16,10/16,12/16,8/16, so every aligned block costs at most one unit of error. Each block in the descending binary decomposition begins at a multiple of its own length; telescoping the counts through the actual scanner states proves the popcount bound, and its logarithmic upper bound gives the limit. The empty prefix and the four small dyadic values are consistent with the fixed two-symbol alphabet. The recorded scans and brute-force checks are consistent supporting evidence; the complete transfer induction is the all-level proof and the uploaded checker was not run.

## originality

PASS

Greedy arch factorization and compositional signatures are prior methods, not distinct contributions of this record. The supported contribution is their explicit evaluation for the standard Rudin–Shapiro fixed point, including the parity correction and the prefix-specific popcount bound. Two later dated records explicitly repeat results: their equivalent content is credited below, but they do not demonstrate earlier priority and neither gives the stated popcount bound. No earlier exact coverage was established by the checked sources.

## value

PASS

The exact density and parity effect measure a natural, nonadditive subsequence invariant of a standard automatic word. The explicit four-block profiles and popcount bound let a researcher predict universality thresholds with a certified error for all prefixes, not just compute a few dyadic examples or substitute parameters into a general formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
