# Self-review

## Correctness
**PASS.** The two similarity formulas are evaluated exactly. The enumeration domain is complete because positive abundance implies \(2\le k\le N\); every positive composition is generated, every community pair is reduced only by genuine symmetries, and every unordered pair of comparison types with common \(N,k\) is tested. Strict-reversal counts are zero through \(N=7\) and exactly one at \(N=8\). Direct arithmetic gives \(B=5/8,H=13/22\) for the first comparison and \(B=1/2,H=3/5\) for the second. The packaged verifier returns `VERIFY_OK`.

Risk: allowing absent species or unequal totals changes the domain and can lower the boundary.

## Originality
**PASS.** Bray–Curtis and Morisita–Horn are classical abundance-based similarity measures, and published ecological work already documents their different weighting and empirical behavior. Chao et al. and Beck et al. are the closest inspected comparisons. Neither their full text nor targeted searches state the equal-total positive-integer cutoff, the four-species eight-individual witness, or uniqueness of the first layer. Exact-vector and smallest-boundary searches likewise did not locate a covering result.

Risk: a small worked example could exist in unindexed teaching material or software tests. The original Bray–Curtis full text was not available through the checked lawful route, so novelty does not rely on a whole-document noncoverage claim for that paper.

## Value
**PASS.** The literature explicitly distinguishes Bray–Curtis from Morisita–Horn by abundance weighting and sampling behavior, yet both are routinely used to rank community resemblance. Requiring equal totals and universal species presence removes sampling-size and turnover confounds. The resulting sharp minimum and unique first pair isolate the smallest abundance-only situation in which metric choice reverses an ecological comparison, providing a compact interpretive and software benchmark.

Self-review: passed. Independent audit: not yet performed.
