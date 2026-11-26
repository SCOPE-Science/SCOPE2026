# Independent mathematical audit

## correctness

PASS

With the full ternary alphabet fixed, a binary squarefree factor has length at most 3, so the remainder has length at most 3 and a complete arch has length 3 or 4. A long arch must be abac. Of the six long starts for a second arch, starting with c gives cc, starting with a gives an identical block or acac, and starting with b followed by c gives cbcb. The only surviving second arch is babc. Repeating the rule gives the unique triple and forces a square for a fourth. Grouping arches in fours gives n <= 4m - floor(m/4) + 3, with m the universality index by the arch criterion; the right side is ceil(15m/4) + 3, so 15m/4 > n-4. In particular m <= 4 forces n <= 18. A separate exact enumeration confirmed the triple is squarefree, the specified length-18 witness factors as 0102 | 012 | 1012 | 0102 | 101 and lacks 22222, and each of the 1,830 length-19 squarefree words contains all 243 length-five subsequences. The supplied verifier selects a length-18 example from its census; the independent check tested the particular witness printed in the finding.

## originality

PASS

The known arch criterion and binary length limit are background. The reviewed distinct contribution is the forced transition and exclusion of four successive long arches for every ternary squarefree word, with its density bound and sharp five-universality threshold. The strongest inspected squarefree catalogue comparison is an exact calculation for prefixes of one particular infinite word; it does not imply the universal statement.

## value

PASS

The forced transition connects contiguous square avoidance with scattered-subsequence richness in the smallest alphabet supporting arbitrarily long squarefree words. It gives uniform quantitative control beyond the elementary four-position argument and resolves a natural first sharp forcing cutoff, without relying on a particular morphic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
