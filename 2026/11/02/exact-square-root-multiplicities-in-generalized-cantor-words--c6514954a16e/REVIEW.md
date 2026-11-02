# Review: exact square-root multiplicities in generalized Cantor words

## Correctness — PASS

The zero/one positions admit an exact base-\(b\) digit representation. The successive gaps between nonzero level-\(k\) islands form a scaled binary ruler. Any square at the stated period with a one must pair two immediately adjacent islands across a minimum gap; the adjacent larger gaps force the possible start positions to the exact interval of length \(g+1\). Every start is realized and different. The circular zero-run certificate guarantees primitivity. Python 3 verification directly enumerated all observed square roots on finite prefixes for 23 base-level cases (bases 3–7), and rechecked the digit formula. The proof, not finite enumeration, handles all parameters.

## Originality — PASS (best knowledge)

Bell and Shallit, *Lie Complexity of Words* (arXiv:2102.03821), Example 7.3, count complete rotation classes for the classical Cantor word, not the rotations whose squares occur. Chen, Lü and Wu (arXiv:1703.04063) establish k-Abelian complexity, while Bulgakova, Frid and Scanvic (arXiv:2201.09556) examine prefix palindromic lengths of the same morphic family. These inspected claims do not imply the exact square-root family. Targeted published-literature and word-complexity searches did not identify an equivalent. The principal remaining risk is unindexed repetitions-specific work.

## Mathematical value — PASS

The classification is exact for all bases \(b\ge3\) and levels \(k\ge0\), resolves an infinite family of square-factor multiplicities, gives all roots explicitly and distinguishes occurrence of squares from occurrence of rotations. The structural boundary argument is reusable for nonprimitive morphic gap words.

## Scope and limitations

Only natural substitution periods and distinct nonzero roots are considered. No absence of squares at other lengths is asserted. Numerical enumeration is supplemental to the proof. This review does not substitute for an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
