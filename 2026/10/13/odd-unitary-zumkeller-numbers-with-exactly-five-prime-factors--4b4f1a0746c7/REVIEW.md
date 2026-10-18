# Independent mathematical audit

## correctness

PASS

The necessary sigma*(n)>=2n makes the five smallest primes 3,5,7 obligatory, and gives s<=32(r+1)/(3r-32) with r in {11,13,17,19}. The resulting squarefree supports number 87. Exact monotone abundancy bounds exclude exponent repetition except s^2 for r=11 and s=13,17,19. Independent full certificate check from witnesses.json confirmed all 90 distinct candidates and each exact proper-unitary-divisor subset sums to sigma*/2-n. Independently rederived all 90 cases and used integer bitset subset sums, obtaining 90 successes and least n=15015. Four-or-fewer-prime odd numbers have sigma*/n<=768/385<2.

## originality

PASS

Das (2024) establishes necessary unitary abundancy and subset-sum criteria but does not classify odd numbers with exactly five distinct prime factors. OEIS A290466 catalogs numbers without this structural family. Published even three-prime support classification has disjoint parity/support.

## value

PASS

A complete naturally bounded support stratum with precise 90-count, explicit rational prime/exponent pruning, and independently checkable finite witnesses; 15015 is a sharp least odd value rather than a tiny arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
