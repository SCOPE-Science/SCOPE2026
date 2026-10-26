# Review: parity-restricted Pascal-row least common multiples

## Correctness — PASS
For every integer \(N\ge1\), the proof distinguishes odd and even rows, then resolves each prime valuation. The full-row maximum is proved by prime-base borrow counts. The exceptional odd-index obstruction is precisely \(N+2=2p^r\); the necessity proof excludes odd maximizers and exhibits an index losing exactly one borrow. The doubling identity for the even-index 2-adic valuation follows from binary digit sums. Independent direct LCM evaluation passed 800 rows, with 11,475 additional 2-adic identity checks. Computations are finite corroboration, not the proof of the universal statement.

## Originality — PASS with stated risks
Farhi (arXiv:0906.2295) derives the full-row identity and an attaining index, but not the parity-restricted maximum. Hong (arXiv:0907.3401) proves an equivalent unrestricted identity. Huber (arXiv:2609.23024) studies optimal selected subsets, and his general exclusion framework is the most substantial nearby comparison; it does not state the closed parity-case quotient formulas. Targeted literature and published mathematical-record searches found no equivalent indexed result. Residual risks are an unindexed earlier derivation and the ease of representing fixed parity subsets in a more general framework.

## Mathematical value — PASS
The result answers a natural complete-row parity-dissection question for all indices; it classifies precise prime-power losses, rather than isolated test cases. The contrast between even and odd selections is structurally meaningful for divisibility of Pascal rows.

## Limits and integrity
No independent mathematical audit has occurred. The verifier's finite range does not bound the theorem. The claim concerns prescribed parity subsets only, not arbitrary periodic subsets. Further publication-priority review is warranted.

Self-review: passed. Independent audit: not yet performed.
