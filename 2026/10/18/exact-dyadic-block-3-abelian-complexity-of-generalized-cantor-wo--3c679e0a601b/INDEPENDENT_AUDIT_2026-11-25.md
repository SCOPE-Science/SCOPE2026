# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 29–66. A length-L window intersects at most one nonzero level-k block W, since these blocks are separated by at least two full zero blocks. All padded prefixes, padded suffixes, W itself and the all-zero word occur within the next iterate. Avoidance of 11 and 101 makes each one supply exactly one candidate instance of each of 001, 010 and 100, with the indicated boundary subtractions. Conversely subtracting the length-three extensions from each length-two count recovers the endpoint indicators. For K<R, cuts just after the K-th one and one place later have at least two leading pad zeros; cutting two places later is possible because one-positions differ by at least three. To have 00 at both ends, that last cut must leave two leading pad zeros. This holds automatically for K<=R−2, and for K=R−1 it leaves exactly q−3 pad zeros. To rule out extra mixed labels, note in particular that a one-symbol left pad requires the cut at L−1, where the last two included symbols of W are 00 by its terminal gap; reversal supplies the analogous one-symbol right pad. This proves the unique q=4 exception, including k=1. Projection onto one-letter endpoints gives the 2-Abelian count. Independent replay branches/6dace631-61f3-45d4-ad54-4faccaed72de/cantor_independent_small_enum.py directly compares all pattern counts through length three with labels for (q,k)=(4,1),(5,1),(4,3),(5,3), giving 6,7,36,37 classes. Frozen verifier and VERIFICATION.md inspected, not executed; the finite replay is not the all-depth argument.

## originality

PASS

Pass the explicit 3-Abelian label census and its sharp q=4 exception. Do not credit the definition, general endpoint reconstruction, ordinary factor complexity or a 2-Abelian regularity theorem as new. The two inaccessible same-family papers leave a residual access risk, not a determination of coverage.

## value

PASS

The natural substitution-aligned lengths and the next finer Abelian equivalence order refine a previously studied statistic. The full classification identifies exactly which boundaries split each intermediate class and the single short-gap obstruction at q=4; it supplies more than a regularity assertion or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
