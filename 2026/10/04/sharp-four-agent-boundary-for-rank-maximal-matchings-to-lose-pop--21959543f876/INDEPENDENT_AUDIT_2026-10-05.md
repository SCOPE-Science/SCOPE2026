# Independent mathematical audit

## correctness

PASS

The definitions of popularity and lexicographic rank maximality are applied to the same perfect-matching set. Independent exhaustive reconstruction in this audit reproduced the complete three-agent census: 138 profiles with equality of the rank-maximal and popular sets, 72 with the rank-maximal set a proper subset of the popular set, and 6 profiles with no popular matching, exactly the six identical-order profiles. The displayed four-agent witness was also checked from the actual package code: its best rank signature is \((2,1,1,0)\), it has four rank-maximal matchings and exactly two popular matchings, with the latter a proper subset. The package verifier additionally compares direct majority voting against the Abraham--Irving--Kavitha--Mehlhorn characterization and two independent rank-maximal encodings.

## originality

PASS

The foundational popular-matching paper explicitly notes that rank-maximal matchings need not be popular and supplies the strict-list characterization used by the verifier, but it does not identify the smallest balanced complete market where the conflict occurs or give the complete three-agent relation census. Later work studies popularity within the rank-maximal class and dynamic versions, again without the sharp four-agent boundary. Targeted Resultary and web searches found no prior exact small-market classification.

## value

PASS

Rank maximality and popularity are two standard, competing optimality notions in one-sided allocation. Locating their first possible conflict and completely resolving every smaller market gives a natural finite cutoff with a reproducible exact census, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
