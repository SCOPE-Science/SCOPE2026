# Independent mathematical audit

## correctness

PASS

For a nontrivial word split uv the rotation vu ends in u, so a non-overlapping code contains at most one word from each rotation class, and a nonprimitive word is excluded by its self-border. For weight three, a nonprimitive word must be a triple repeat of a block with one 1, possible only at 3|n, with exactly n/3 labeled words. Division by n after excluding these gives floor((n−1)(n−2)/6). For t=floor(n/3), the construction uses gaps (a,b,c) in 0^a1 0^b1 0^c1 with a≥t>c. A matching one-1 prefix and suffix would require a≤C, impossible; a matching two-1 pair requires b=C and a≤B for suffix-word gaps (A,B,C). Equal total lengths then give c=A+B−a≥A≥t, also impossible. Other proper prefix lengths cannot match a suffix (all suffixes end in 1, and the third 1 ends the word). Independently, every primitive cyclic gap triple has both a gap ≥t and a gap <t: all gaps ≥t would sum too high, and all gaps <t sum to at most 3t−3, with equality only at the excluded periodic triple. There is exactly one low-to-high transition in a mixed cyclic triple, so the construction selects exactly one representative. This proves all lengths including n=4 and multiples of three. RESULT.md, VERIFICATION.md, verify.py and TABLE.csv read; the frozen script was not executed. Independent bounded_weight_three_check.py checked every ordered proper prefix–suffix pair at n=4,…,40 and separately enumerated weight-three primitive rotation classes through n=18. At n=6,9,12,15,18 it found 2,3,4,5,6 nonprimitive words and code sizes 3,9,18,30,45. These are bounded checks only. Scope is linear binary words of the same length n≥4, exactly three ones, with self-pairs included.

## originality

PASS

Credit the standard primitive-necklace bound, fixed-weight counts and the coprime positive-excursion regime. The supported distinct contribution relative to inspected earlier literature is all-length sharp attainment, in particular the divisible-length construction that selects the remaining primitive classes without overlaps. Multiple distinct indexed entries with later catalogue dates do cover the same capacity and transversal; they are positively identified as equivalent coverage, not described as search misses or assumed to establish earlier priority.

## value

PASS

The known rotation obstruction is only an upper bound until one can choose compatible linear representatives across classes. This explicit construction shows saturation even when the coprime excursion method fails to cover all classes, giving a complete answer in the first sparse three-gap regime with a possible equal-height return. That is a useful structural extremal fact beyond a small table or the routine necklace count; it is not a claim about weight four or greater.

The dated certificate retains the supplied scientific assessment, sources and limitations.
