# Scientific review

## Correctness — PASS

The length-\((2^{k-1}-1)\) repeat classification is established by induction on substitution level. The base case \(P_3\) lists all possible windows, parity rules out cross-parity collisions, and the substitution recovers preceding-level factors from odd positions. The double-occurrence context lemma proves that every minimal absent word longer than \(2^{k-1}+1\) is impossible and exactly one exists at that length. The standalone checker verifies all levels \(3\) through \(9\) independently of the proof, without treating enumeration as infinite evidence.

## Originality — PASS, qualified

Barton et al. (2014) and Crochemore et al. (2015) supply general minimal-absent-word results; Schaeffer and Shallit (2015) investigate automatic-word properties. Banbara et al. (2026) explicitly give period-doubling parity and half-block structure while studying a different attractor invariant. Earlier work already exhibited the exact extremal *word* as a lower-bound witness, so mere discovery of that absent word is **not original**. The assessed additional result is its sharp *maximum length*, uniqueness, and the underlying complete longest-repeat classification. Searches and examined papers did not reveal those stronger statements. Possible alternate formulations remain a historical-priority risk.

## Value — PASS

A complete description of the deepest element of the anti-dictionary is a natural structural invariant: it settles sharp boundary depth and multiplicity at every dyadic level. The prior lower-bound example by itself neither proves a maximum nor rules out ties. The proof relates extremal forbidden patterns to exact repetition structure rather than reporting only a finite census.

## Limitations

Only finite linear dyadic period-doubling words, levels \(k\ge3\). The total minimal-absent-word count and arbitrary lengths are not claimed. Priority beyond the inspected primary sources is not guaranteed. A separate independent scientific audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
