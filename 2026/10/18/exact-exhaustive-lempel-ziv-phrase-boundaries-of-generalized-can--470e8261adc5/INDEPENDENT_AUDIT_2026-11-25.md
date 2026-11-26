# Independent mathematical audit

## correctness

PASS

The recurrence W_(m+1)=W_m 0^((q−2)q^m) W_m proves the digit criterion and longest internal gap. At L=q^m the first three nonzero L-blocks start at 0,(q−1)L,q(q−1)L; the two intervening zero gaps have lengths (q−2)L and q(q−2)L. At A_m=(q−1)L+1 the proper prefix ending in (q−2)L zeros is seen at 1, but an earlier full copy would require (q−2)L+1 zeros after an earlier 1. The last 1 in the suffix for m≥1 lies at the end of the second block, and no preceding 1 has that gap. At m=0 the phrase is the first 0^(q−1) and its shorter prefix is seen at 1. At B_m=2(q−1)L+1 the all-zero proper prefix of length R−1, R=(q−1)(q−2)L, is seen starting at qL; the next 1 is at q(q−1)L. An earlier full copy would end at an earlier 1 preceded by at least R−1 zeros, exceeding the maximum (q−2)L except at q=3,m=0 where 01 was indeed seen earlier. Exact end indices telescope from A_m to B_m to A_(m+1). The initial q≥4 base reaches A_0=q; the checked ternary prefix parses as 1|0|100|0101|0000|000001 with the last ending just before 19. In particular 010 occurs at 1 but 0101 does not occur before 5. Infinite starts restricted to indices <q^k count finite phrases, because only the last can truncate; counting scales gives 2k+2 or 2k+1 and the stated small-depth counts. Inspection of frozen verify_parsing.py confirms its truncated search window enforces j<i with overlap allowed. Its prediction helper seeds unfiltered initial indices and is only called at the selected long lengths, so the supplied test does not establish small-prefix cases. An independent Z-function reparse agreed on 294 prefixes including the small and truncated regimes; replay python3 /workspace/branches/independent_finite_checks.py (check 3). Neither finite test replaces the proof.

## originality

PASS

Credit the earlier exhaustive-history convention and general logarithmic complexity class. The inspected literature and closest exact analogue do not determine the two Cantor-family boundary progressions and their ternary exception or the exact depth counts. Novelty assessment is for those explicit sharp details under the precise parsing convention.

## value

PASS

These sparse uniform morphic fixed points provide a natural test of exhaustive compression history beyond size-order statements. Knowing every boundary reveals which marker-ended and zero-run innovations determine the parsing and identifies an exceptional base with different early phases and additive complexity. That information permits exact prefix counts and benchmarks parsers with overlap; it does not purport to give a new compression algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
