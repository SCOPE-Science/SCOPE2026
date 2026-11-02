# Scientific review: circular-palindrome spectrum of Zimin words

## Correctness (C) — PASS

The statement quantifies over every integer rank \(n\ge1\), distinct rank-marked alphabet letters, and circular factors of lengths at most \(N=2^n-1\). Its proof checks the ruler identity, all possible odd centers and the first forbidden offset, the unique possible even center at the seam, and the lengthwise count. The boundary ranks \(n=1\) and \(r=n\) are handled explicitly. The included checker independently enumerates all circular factors and tests exact sets through rank 8; the all-rank conclusion does not depend on extrapolating those examples. Remaining risk: ordinary possibility of an unnoticed error in a mathematical argument, pending independent review.

## Originality (O) — PASS, with a specified access risk

The checked older source Głowinski–Rytter (arXiv:1307.1560) concerns ranked variable matching and Zimin structure, not a proved exact circular-palindrome language. The checked richness treatment Glen–Justin–Widmer–Zamboni (arXiv:0801.1656) supplies general palindromic structure, not this explicit marked-ruler circular length distribution. Simpson (DOI:10.1016/j.tcs.2014.07.012) proves the stronger general numerical ceiling \(5N/3\) and near-extremal examples; that bound does not imply the Zimin formula or identify the listed palindromes. Simpson's complete text was inaccessible despite open-access and institutional retrieval attempts; this is a genuine historical-priority risk, not a claim that its uninspected sections do not cover the result. Actual published-record searches and available previously recorded claims did not identify an implication-equivalent theorem. Numeric coincidence alone is not considered originality. No general maximum or new classic integer sequence is claimed.

## Value (V) — PASS

Classifying the whole circular palindromic language of a canonical recursively self-similar word gives more information than the count: for every length, an explicit formula and unique even representative; for odd lengths, exactly determined rank-marked representatives. This connects the ruler valuation structure with cyclic palindromic complexity and gives a concrete infinite family reaching \((3N-1)/2\) palindromes below Simpson's general upper limit \(5N/3\). The result is structurally motivated and not an arbitrary finite table.

## Limitations and nearby literature

The theorem is restricted to distinct literal Zimin symbols and factors of length no more than one circle traversal. Full-text historical comparison with Simpson's 2014 paper is outstanding, along with independent checking. No extrapolation to larger circular languages, morphic images, or arbitrary words is asserted.

Self-review: passed. Independent audit: not yet performed.
