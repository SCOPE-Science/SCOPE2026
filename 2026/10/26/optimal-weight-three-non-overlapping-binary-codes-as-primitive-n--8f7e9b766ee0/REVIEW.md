# Review: Optimal weight-three non-overlapping binary codes

## Correctness (PASS)
The upper bound follows from disjoint full-size cyclic rotation orbits; the constructed family's cross-bifix-free property is proved by a complete two-case prefix/suffix comparison. The exact number of words meets the bound in each residue class of the length modulo three. The primitive-necklace property follows by accounting separately for the single nonprimitive orbit when the length is divisible by three. The exhaustive Python checks agree through length sixteen, and the arithmetic identity is also tested on a large finite range. These computations supplement rather than replace the all-length proof.

## Originality (PASS, with priority risk)
Read the primary open-access papers by Chee, Kiah, Purkayastha, and Wang (2012 preprint; generalized-Fibonacci construction) and Blackburn (2013 preprint; unrestricted constructions and exact short-blocklength theorems), plus the open-access full text of Stanovnik, Moškon, and Mraz (2024; unrestricted global optimization). The former code constructions and latter unrestricted results do not establish the fixed-weight-three all-length equality or its perfect primitive-necklace transversal. Searches for cross-bifix-free codes, non-overlapping codes, constant-weight-three restrictions, the exact cardinality expression and necklace representatives found no directly covering statement. General cyclic rotation bounds give only the upper bound without construction; an unrestricted result can subsume some isolated small-length numerical cases. An older specialized equivalent result may remain unindexed; external historical priority is not certified.

## Value (PASS)
Exactly three active symbols is a natural energy/composition restriction in synchronization coding. The result determines the optimal code size for all blocklengths and supplies an efficiently enumerable construction that selects one representative per primitive weight-three orbit. Exact attainment at all lengths, including lengths with nonprimitive words, is a structural statement and not a finite-table recomputation.

## Scope and limitations
The theorem assumes binary length-\(n\) words of Hamming weight three for \(n\ge4\), with overlaps against the same word forbidden. No extra error-correction guarantee, arbitrary-weight optimum or independently audited status is implied. All primary literature comparisons were conducted against the inspected sections and mathematically stated hypotheses.

Self-review: passed. Independent audit: not yet performed.
