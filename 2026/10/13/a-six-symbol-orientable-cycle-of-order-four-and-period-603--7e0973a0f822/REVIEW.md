# Independent mathematical audit

## correctness

PASS

Fetched original witness.txt Git blob f098c294a2023a28f8a9a10425f04df07a0f82a6; independently constructed all 603 circular length-four windows. The word has exactly 603 symbols all in 0..5, 603 distinct forward windows, 603 distinct reversed windows, no forward/reverse overlap, zero palindromes and least period 603. Hence it realizes 603 of 630 possible nonpalindromic reversal pairs with 27 unused. The exact finite exhaustive verifier matches the definition and wraparound, not extrapolation; no assertion of optimality.

## originality

PASS

The revised 2026 primary paper Table 4 reports k=6, n=4 best prior period 552, upper bound 612. This certified 603 witness is not implied by an upper bound or earlier shorter examples. The search located no prior 603 witness, but later/unindexed constructions may still overlap.

## value

PASS

A rigorously checked explicit combinatorial construction raises the natural extremal period lower bound by 51 and leaves only nine to the known upper bound; it is a mathematically useful near-extremal finite certificate, not a trivial exhaustive rescan or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
