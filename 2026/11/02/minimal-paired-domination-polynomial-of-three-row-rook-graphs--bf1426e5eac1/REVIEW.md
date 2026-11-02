# Mathematical review

## Correctness — PASS

The domination dichotomy is exact: an undominated cell exists precisely when both a row and a column are unrepresented. In the all-rows case any perfect matching contains at most three edges needed to cover all rows, reducing minimality to sizes four and six. The six-vertex classification uses the absence of cross-row matched edges and the ability to extract a dominating four-set whenever a column is shared. In the missing-row case the number of doubled columns has fixed parity, and at least two permit a two-vertex deletion preserving every column and yielding even occupancies. The surviving cases have explicit perfect matchings and are inclusion-minimal. Counting the disjoint configurations yields the polynomial with correct small-order coincidences. Direct independent graph-level enumeration through seven columns and arithmetic checks through one hundred corroborate the formula; finite computation is not the proof.

## Originality — PASS (provisional publication priority)

The 2021 paper by Alizadeh and Gözüpek studies upper paired-domination bounds and equality characterizations, not the present complete three-row rook-graph cardinality enumerator. The 2022 Jiang–Wu–Zhang–Rao work concerns algorithmic complexity. Burcroff's 2020 rook-graph discussion concerns ordinary upper domination and direct-product inequalities; the object and statements differ. The known polynomial for all paired-dominating sets of two-row complete prisms addresses a different dimension and does not imply minimality spectra in three rows. Direct statement-level comparisons and searches for equivalent rook-graph, line-graph-of-biclique, and upper-paired-domination formulations found no equivalent statement; this is not a proof of publication priority. Full texts of some older relevant papers remain uninspected.

## Mathematical value — PASS

Complete cardinality distributions of inclusion-minimal paired domination encode strictly more than the maximum size, which is studied in the complexity literature. A natural connected, claw-free graph family exhibits the unexpectedly sparse spectrum \(\{4,6,2\lceil n/2\rceil\}\), a parity-dependent upper parameter, and unbounded forbidden intervals of feasible even cardinalities. The exact counting formula resolves all multiplicities across an infinite family, rather than a finite or arbitrary parameter slice.

## Limitations and risks

The family has exactly three rows; broader dimensions are not covered. The independent program checks finite instances only. Older upper paired-domination full texts and potential alternative terminology constitute residual priority risks. No external or independent mathematical certification has been performed.

Self-review: passed. Independent audit: not yet performed.
