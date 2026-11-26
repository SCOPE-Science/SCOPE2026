# Independent mathematical audit

## correctness

PASS

At level k, the aligned blocks are W and 0^L. The base-q digit condition forbids adjacent nonzero blocks for q>=3 and permits 101 on the upper sequence exactly at q=3. A proper suffix of W misses its first 1 and a proper prefix misses its last 1. This proves uniqueness at length L. At length 2L, an unaligned start of offset r sees precisely a suffix of length L-r, a whole block, and a prefix of length r. The occurring upper triples 000, 010, 100, 001 and (only at q=3) 101 realize exactly the stated families; aligned starts are the zero or end-padded cases. The two single proper-piece families have smaller weight and are distinguished from each other by the half containing their ones. Within those families, the first one or the terminal zero run identifies the offset. The padded family has weight T and is distinguished internally by the first one. The split family has weight T because the prefix and suffix partition W, and its unique internal zero run of length L identifies its offset and separates it from padding. This gives total 4L-1 or 3L and extremal size 2L or L+1 respectively, also at L=1 where all proper-piece families are empty. The fractions tend to 1/2 and 1/3. An independent digit-predicate window check (check_record2_independent.py) used prefixes of length 12L for q=3 through 7 and k=0 through 3 and matched the full sets and extrema; finite prefix observations alone do not establish exhaustion. Frozen verify.py was inspected, not executed.

## originality

PASS

Pass applies to the complete word-level extremal fiber at both scales across q, principally the split-family transition and the resulting exact multiplicities. It does not credit the total factor counts, the ordinary-Cantor maximum value, or the ordinary length-3^k uniqueness already implied by the indexed morphology. A strong match for padded words comes from square roots, but the square condition excludes the complementary split words and does not classify the entire weight fiber.

## value

PASS

Substitution scales are natural recurring lengths, and the extremal Parikh fiber is a sharper and reusable invariant than peak weight or total factor complexity. The full classification isolates exactly when two distinct nonzero blocks contribute without losing weight and explains the different limiting fractions. This gives an exact comparison for distinct factors rather than occurrence frequencies or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
