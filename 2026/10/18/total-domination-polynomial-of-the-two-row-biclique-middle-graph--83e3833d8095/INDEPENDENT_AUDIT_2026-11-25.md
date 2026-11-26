# Independent mathematical audit

## correctness

PASS

First choose a nonempty edge-vertex subset in every column, with both rows represented, and allow all original vertices. This baseline has enumerator ((2z+z²)^n−2z^n)(1+z)^(n+2). It dominates all original and all unselected edge-vertices. A failure occurs only if a selected edge-vertex has no selected partner in its row or column; then it is an unpaired singleton row, and its original hub and original column endpoint must both be missing for the baseline choice to fail. For n≥3 at most one row can be singleton under column coverage. There are 2n unpaired singleton profiles, each of weight z^n, with n other free original vertices, so subtract 2nz^n(1+z)^n. This proves the entire polynomial. At degree n, the configurations use no originals and one edge-vertex per column; each row must have at least two. The constant in the bracket is 2^n−2n−2, positive from n=4. At n=3 it is zero, and the linear term is 24. Bernoulli substitution at q=1−p gives (1−q²)^n less 2(pq)^n(1+nq²), with a continuous extension at q=0. The correction is uniformly bounded by 2(n+1)4^(−n); the main term gives all three claimed limits, including the endpoints. A new exhaustive program built the middle graph by original endpoint intersections and tested domination by the union of selected open neighborhoods. All coefficients, including zeros, agreed for n=3–6 over 1,198,080 subsets. The positive totals reproduced 752, 4928, 30528 and 185344.

## originality

PASS

The scalar minimum is known. The distinct claim is the evaluated compact all-size enumerator for this two-row family and its exact Bernoulli consequence. The inspected primary works do not give that evaluated family law. A later indexed general expansion is substantial broader coverage: it enumerates the same polynomial by edge covers but leaves the family-specific evaluation and probability window unstated. It is not earlier priority evidence.

## value

PASS

A full exact size distribution for a standard family is more informative than the known minimum; it gives the number and shape of optimal sets and quantifies the probability of total domination over every density. The scaling law isolates the missing-column obstruction from the uniformly exponentially small row/endpoint obstructions, which explains the transition rather than only giving a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
