# Independent mathematical audit

## correctness

PASS

Exact cross-bifix-free binary length-10 code of size 17 forces all encoded proper overlaps to be multiples of ten and preserves every overlap and greedy merge. Independently reconstructed 252 distinct length-eight source windows and the 17 codewords, checked each of 251 prescribed merges against the maximum over all live ordered pairs, all 63,252 ordered distinct source/binary input overlaps, the Eulerian 259-symbol optimal superstring, and output 519. Distinct length-80 inputs with max proper overlap 70 have starting positions at least ten apart in any superstring, proving OPT >=80+251*10=2590 and attainable. Greedy length=5190 so ratio 519/259>2. The finite certificate is exhaustive for this explicit instance; it is not a universal greedy approximation theorem.

## originality

PASS

The factor-two disproof, 252-word length-eight 17-symbol witness and binary alphabet-reduction principle are prior art, not new claims. Direct scientific contribution is the 10-bit cross-bifix-free 17-symbol code and resulting certified binary length-80 failure. Best-of-knowledge not found covered by the inspected 2026 length-eight source and Vassilevska general 2005 reduction, whose code has width 36 for 17 letters, yielding binary length 288. Exact short-code priority could overlap unpublished or unindexed constructions.

## value

PASS

The common-length binary shortest-superstring greedy ratio is a natural quantitative benchmark. The full 252-string exact instance cuts binary length from 288 under the cited general 17-letter alphabet reduction to 80, with exact OPT and a reproducible legal adversarial greedy trace. It neither proves that length 80 is minimal nor that all tie-breakings fail. This small but material 3.6-fold reduction in binary benchmark size is useful in algorithm testing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
