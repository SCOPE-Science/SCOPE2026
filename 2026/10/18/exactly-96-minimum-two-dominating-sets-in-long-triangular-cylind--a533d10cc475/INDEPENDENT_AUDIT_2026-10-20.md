# Independent mathematical audit

## correctness

PASS

Examined column-based proof: empty interior column forces both neighbors full; maximal chains of empties at distance two incur excess at least three. Without empties, two disjoint endpoint pairs each require one extra selected vertex, hence n+2 lower bound. Equality forces one double column in each end pair and singleton remainder; each internal singleton needs both missing labels horizontally, imposing rainbow triples and period three. Six permutations times two choices at each double boundary give 24 per one of four placement cases, hence 96, with valid constructive solutions. Independently implemented 8-mask-column dynamic program for n=7..100, matching (n+2,96) in every test.

## originality

PASS

Garzón–Martínez–Moreno–Puertas 2022 establishes minimum size n+2 (at least n>=4), not optimizer multiplicity or four-family structural census in inspected full paper. Other cylinder studies address min-plus size bounds or rainbow 2-domination. The exact optimizer enumeration extends known numerical value rather than repackaging it.

## value

PASS

Complete description of all optimal labelled vertex sets of an infinite natural cylinder family, with unexpectedly constant count 96 and sharp period-three structure, is a motivated exact extremal classification. The count is not implied by the known size alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
