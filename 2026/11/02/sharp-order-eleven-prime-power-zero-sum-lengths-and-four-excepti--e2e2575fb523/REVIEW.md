# Scientific review: order-eleven prime-power zero-sum classification

## Correctness — PASS

For each proposed shorter sum the integer polynomial \(g\) has positive coefficient mass below eleven, so it is not divisible by the cyclotomic polynomial \(\Phi_{11}\). Its resultant is a nonzero integer of absolute value at most \(10^{10}\); a standard integral resultant identity forces divisibility by the candidate \(p^k\). Hence the proof excludes every prime above \(100000\) independently of computation. The standalone checker exhaustively lists all \(352715\) allowed exponent-multiplicity vectors for each of the \(945\) eligible smaller primes at square level and for all six needed higher levels, using exact arithmetic and direct order checks. Monotonicity and the length-eleven geometric sum then settle every larger exponent. Boundary conditions (exact order eleven, \(k\ge2\), repeated powers allowed) are explicit. No use is made of finite extrapolation.

## Originality — PASS within inspected literature

The 2022 motivating paper already establishes general finiteness and exhibits the prime-square exceptions at \(23,67,89\) and a few nonexceptions, so these instances are not independently presented as novel. The new contribution is the **complete** order-eleven classification including the missing square exception \(683\), with a uniform effective prime cutoff and a proven sharp global stabilization level. The 2019 foundational treatment and relevant mathematical records were inspected for stronger implications; none of the examined statements subsumes the full result. Other unindexed or implicitly equivalent prior work remains a residual risk, not an absolute novelty guarantee.

## Mathematical value — PASS

An explicitly studied minimum-length invariant is determined for a whole natural prime-power family at the first order left without a complete treatment after five and seven. The exact exceptional support, new prime \(683\), and smallest uniform stabilization exponent answer a concrete structural question, not a routine table slice. Although the proof invokes a finite census, the resultant theorem makes the search globally exhaustive, and the classification holds for infinitely many primes and arbitrarily high powers.

## Closest literature, checks, and limitations

- L. Jacob and B. Külshammer, arXiv:2204.09403v1, Propositions 10–15 and Example 16(i): foundational definitions, sharp selected rows and an open request for effective bounds; **does not give** this complete order-eleven table.
- Breuer, Héthelyi, Horváth, Külshammer, arXiv:1912.03065v1: foundational minimum-length results, not the eleven-order exceptional-prime list.
- All new finite identities are checkable from `verify.cpp`. An unindexed exact specialization remains the main priority uncertainty. The work is proof-backed but has no independent audit.

Self-review: passed. Independent audit: not yet performed.
