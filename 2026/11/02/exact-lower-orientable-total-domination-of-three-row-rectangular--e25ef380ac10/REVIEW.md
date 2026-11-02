# Scientific review

## Correctness — PASS
The orientation criterion is proved in both directions. Every selected component must contain a cycle, and any cycle in a path-grid strip has vertical edges in two distinct columns. This forces at least two surplus selections per occupied column run. Empty interior gaps are at most two columns and empty endpoint gaps are at most one; a missing endpoint column forces the next column to have all three selected vertices, increasing the adjacent run's surplus. The resulting inequality \(|S|\ge n+2\) covers all runs, gaps and endpoint cases. The explicitly constructed middle-row set plus the two adjacent upper-row vertices has exactly \(n+2\) elements, dominates the grid and includes a square cycle. Exact exhaustive subset tests cover all widths \(2\le n\le9\) and direct orientation enumeration checks widths two and three. Finite checks are supporting evidence only.

## Originality — PASS, with limitations
The closest original paper, Anderson–Dravec–Johnston–Kuenzel (2023), proves only \(n\le\operatorname{dom}_t(P_3\square P_n)\le n+2\); its cycle requirement and upper bound are already known. The new lower argument establishes equality for every width. Goto–Kobayashi (2021) computes the connected domination number of the same grid, \(n\), but does not impose cycles and does not imply this formula. The searches considered open orientable domination, cyclic-component dominating sets, and generalized stronger grid results. No covering theorem was identified, but publication priority is not independently certified. The related earlier result on vertex-deletion monotonicity for orientable total domination concerns a different graph family and implication.

## Mathematical value — PASS
This result closes a published two-unit gap for a canonical infinite family and gives a structural explanation rather than a finite table. It distinguishes ordinary connected domination from orientation-feasible total domination and supplies a reusable column-run boundary accounting mechanism. It does not resolve wider grids or the upper orientable total domination invariant.

## Verification and limits
Compile the bundled `verify.cpp` as C++17 and run it. Exhaustive selected-subset minima for widths two through nine are four through eleven, respectively, and independent direct orientation enumeration agrees for widths two and three. The mathematical proof, not finite enumeration, establishes the formula for unbounded width.

Self-review: passed. Independent audit: not yet performed.
