# Scientific review: exact circular BWT of paperfolding prefixes

## Correctness — PASS

The arithmetic paperfolding definition implies a precise sixteen-symbol macroblock for each pair of parity and following paperfolding bit. All four macrotype populations are established by exact counts, and the sixty-four literal seven-letter tests give twenty-eight possible prefix classes. Only four classes have mixed predecessor letters. Two split by their eighth letter, one by its eighth and sixteenth letters, and the last is sorted by the recursive shorter-word rotations. The exceptional block has the proved recurrence \(B_j=A_jB_{j-1}\), with its explicitly sorted base case. Combining all classes gives the full eighteen-block transform and \(4k-4\) maximal equal-letter runs for every \(k\ge6\). The standalone checker tests independent literal sorting up to rank nine and the complete transform and symbolic macro enumeration through rank fourteen; these finite tests are corroboration, not a proof for unbounded ranks. The domain is deliberately sentinel-free and cyclic.

## Originality — PASS, subject to priority risk

The 1994 Burrows–Wheeler report defines rotation sorting but does not derive paperfolding instances. Allouche's 1992 primary article determines paperfolding factor complexity, including twenty-eight length-seven factors, but that number alone does not determine their ordering or predecessor-bit variation in circular BWT. Frosini and collaborators' 2022 preprint develops general logarithmic run bounds for purely morphic finite words, not this exact transform or the coefficient \(4\) for regular paperfolding. The full accessible primary texts were inspected, with comparisons by mathematical implication rather than names. Search for cyclic rotation, BWT runs, paperfolding, and automatic/morphic transform alternatives did not find an equal or stronger formula. Search incompleteness and alternative conventions remain real risks, particularly if an unlocated source has an exact circular paperfolding transform.

## Value — PASS

A full explicit infinite-family Burrows–Wheeler transform formula, with sharp run count \(4k-4\) and a finite factor-class mechanism, is a motivated compressibility/indexing invariant. The formula gives all transform letters without enumerating all rotations, and separates the lone recursively sorted local class from twenty-seven fixed or short-lookahead classes. It is meaningfully stronger than a generic logarithmic upper bound, not a renamed factor-complexity theorem or a few enumerated ranks.

## Evidence and limitations

The derivation appears in `RESULT.md`; the complete twenty-eight-class finite certificate is `SEVEN_GRAM_TABLE.md`, and independent finite replay is `checker.py`. Source comparisons use the original Burrows–Wheeler technical report, Allouche (1992), and the Frosini et al. (2022) freely accessible preprint. This is a self-review, not a publication-priority guarantee or an independently audited mathematical proof.

Self-review: passed. Independent audit: not yet performed.
