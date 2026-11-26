# Independent mathematical audit

## correctness

PASS

The completed transitions in the frozen statement agree with the later survey display, including the even/odd last-state conventions; in the v1 display the opposite-letter branch at the last state is indeed omitted for each parity. A shortest merge equals the shortest directed path to a diagonal in the unordered pair graph. Reversing arcs and starting at all diagonals gives exact unit distances. I inspected the frozen transition builder, triangular indexing, queue and inverse-image products, uniqueness scan, TSV, and supporting checks. For distinct successors a predecessor can be oriented to match x,y without losing the unordered pair; at x=y one orientation suffices. All packed indices and distances fit the integer types. Independently reconstructed the transitions by adjacent transpositions and two overwrites, generated every forward arc explicitly in sparse form, collapsed all diagonals to one terminal, transposed, and solved the unit-weight single-source shortest-path problem (/workspace/review_work/pairs.py). All additions/labels are integers exactly representable by the solver's numeric type. The run exhausted all k=1..1000 in ten 100-parameter chunks and checked reachability, the diameter and exactly one maximizer per k. The 1001-line /workspace/review_work/pair-census-independent.tsv matches the frozen output byte-for-byte, SHA-256 f88e9f5eb6626e581f2ffb6d19660280904394a77ad6bd590d8c8db8b81c2128. Verified counts: 1510524000 off-diagonal pairs (1512031500 states with all diagonals counted separately). Last case: 3006 states, distance 1258511, only {501,502}. This proves the finite interval, not arbitrary k. The cited extension relative to the other paper's proved endpoint is conditional on the frozen record's account of that paper; it is not independently confirmed by the census.

## originality

PASS

The assessed contribution is the exact exhaustive all-pair diameter extension through 1000 and the uniqueness census, not proposing the quadratic formula or solving the all-k conjecture. The accessible source establishes a different distinguished-state problem. The frozen attribution to the separate paper is credited as an attribution, without independently certifying its ranges or claiming priority over uninspected cases. No inspected statement dominates the bounded new census.

## value

PASS

This is not a small table of a generic algorithm: it exhaustively tests the conjectured sharp law across a thousand members of a named open-problem family and identifies the unique witnesses, using all pairs rather than just lower-bound examples. The significant range beyond the attributed prior computations and the uniform location of the hardest pair are usable evidence for an arbitrary-k approach, without claiming such a proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
