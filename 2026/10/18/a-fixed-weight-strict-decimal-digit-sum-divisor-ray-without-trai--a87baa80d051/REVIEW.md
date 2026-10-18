# Review: A fixed-weight strict decimal digit-sum divisor ray without trailing zeroes

## Correctness — PASS

For every \(k\ge12\), the verified integer identities \(a=448999\), \(a^2=201600102001\), \(2a^2=403200204002\), together with \(2a^2<10^{12}\le10^k\), imply the two exact nonoverlapping digit-block formulas. The individual sums are 43, 13, 17, so \(s_{10}(N_k)=86\) and \(s_{10}(N_k^2)=43\). Congruence modulo 10 fixes the last digit at 9; strict increase in k guarantees infinitely many distinct integers. A standalone integer checker verifies the seed and \(12\le k\le100\). The infinite proof relies on the block lemma, not on finite enumeration.

## Originality — PASS (qualified)

The exact claim fixes two *unequal* decimal digit sums at (86,43) for an unbounded non-trailing-zero family. OEIS A268135 asks about strict divisibility and lists finite examples, not this fixed-weight ray. Hare-Laishram-Stoll arXiv:1001.4170 proves infinite families with fixed *equal* digit weights; arXiv:1001.4169 proves arbitrarily small ratios but does not fix both weights. Its construction already yields the weaker plain infinitude with strict divisibility by suitable choices, so that weaker consequence is deliberately NOT asserted as new. The standard noninterfering-block lemma is also not claimed to be original. Targeted scientific-literature and mathematical-record searches for digit sums, proper divisors, fixed digital weights, and the specific seed found no encompassing record. Undiscovered explicit fixed unequal-weight families remain a risk.

## Value — PASS

The natural qualitative refinement of the March 2016 A268135 non-trailing-zero question is to hold both digit sums fixed instead of allowing the input digit weight to diverge. Such fixed-weight fibers are a recognized subject in Hare-Laishram-Stoll 2010; their displayed theorem treats equality, not proper divisibility. This establishes a fixed strict-divisor fiber with infinitely many members and constant quotient two, not a mere trailing-zero padding family. The numeric pair (86,43) is a witness to existence, not asserted to be an optimal invariant. The method is elementary and does not classify all possible weights.

## Closest literature and limitations

The comparison includes OEIS A268135 (March 2016 question), the 2010 paper arXiv:1001.4170 (fixed equal weights) and the 2010 paper arXiv:1001.4169 (small ratios). The separated-block identity and the weaker unconditional infinitude are not presented as new. The explicit fixed unequal-weight ray survives the statement-and-implication comparison, subject to possible earlier unindexed examples. No minimality or general classification is claimed. The computation checks exact seed arithmetic, not infinitely many individual instances.

Self-review: passed. Independent audit: not yet performed.
