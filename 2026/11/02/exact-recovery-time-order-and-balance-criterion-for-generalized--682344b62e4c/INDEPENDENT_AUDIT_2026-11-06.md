# Independent mathematical audit

## correctness

PASS

From the actual theta-graph RESULT.md and verifying its finite subset checker: deleting target edge e leaves endpoint connectivity iff every other edge of its own terminal path AND every edge of at least one other full path has appeared. Poissonization gives independent edge states with x=1-exp(-t/N), so E_i=N integral_0^1 [1-x^(ell_i-1)(1-product_{j != i}(1-x^ell_j))] dx, yielding the given rational sum. Difference E_j-E_i=N integral (x^(ell_i-1)-x^(ell_j-1))(1-product_{k != i,j}(1-x^ell_k)) dx, strictly signed by lengths when r>=3. All equal yields rank r*ell-r+1. At r=2 the difference is zero: sharp boundary. Independently enumerated all subsets for (2,3,4), exact fractions E=(67/10,242/35,101/14) by paths, matching theory; finite tests are corroboration only.

## originality

PASS

Qualified PASS on infinite theta-family closed formula, strict length-order equivalence and if-and-only-if balance criterion; not on matroid recovery expectation as an invariant. Universal matroid counting formulas are prior art and do calculate any fixed finite instance in principle.

## value

PASS

A natural graph family with multiple internally disjoint paths gives a complete all-size structural classification of coordinate recovery efficiency, not a one-off calculation. The strict pairwise ordering survives changes to all other path lengths and exactly characterizes balance; the concise sign integral is a meaningful graph/matroid structural law beyond generic evaluation or mean rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
