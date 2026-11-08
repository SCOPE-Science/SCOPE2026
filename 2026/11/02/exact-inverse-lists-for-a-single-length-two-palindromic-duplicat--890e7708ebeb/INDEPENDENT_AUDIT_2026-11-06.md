# Independent mathematical audit

## correctness

PASS

For any alphabet q>=2 and received word length m>=4, legal inverse sites are occurrences of abba. If deleting two middle letters at different sites yields the same parent, direct word comparison forces period two between sites; legality of both palindromic windows forces the entire intervening interval constant. Consequently all constant 4-windows of a long run give a single parent, and every interior run of length two with equal-symbol flanks contributes exactly one distinct nonconstant window. Disjoint-run length budgets give max floor((m-2)/2), achieved by alternating runs of lengths 1,2,...,2,1. Counting nonconstant abba windows plus starts of runs >=4 gives sum_y d(y) = q^(m-4)*((m-3)q(q-1)+q+(m-4)(q-1)). An independent direct inverse enumeration checked q=2,m=4..11 and q=3,m=4..7; it is not an infinite proof.

## originality

PASS

Qualified best-of-knowledge originality: earlier palindromic-duplication coding papers study confusability, overlapping palindromic squares and multi-error-correcting codes, but do not in the inspected material give all received-word distinct single-step parent counts and aggregate incidence. This is a local inverse-list theorem, not a claim that palindromic overlaps are newly discovered.

## value

PASS

Inverse-list size controls ambiguity and decoder candidate enumeration for a natural finite-word mutation channel. The all-length run classifier, sharp peak and total incidence are exact enumerative invariants which may be used in coding channel analysis beyond known broad capacity estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
