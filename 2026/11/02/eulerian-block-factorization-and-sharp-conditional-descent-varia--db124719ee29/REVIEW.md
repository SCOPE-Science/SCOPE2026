# Review of the record-pattern conditional descent theorem

## Correctness

**PASS.** The exact factorization follows from a product of within-block permutation actions on each fixed record-position fiber, not from assuming unconditional independence. Boundary comparisons are forced descents before nonrecord blocks and forced ascents before new records; the only random comparisons are internal to the blocks. Standard Eulerian moments then yield an exact conditional variance. Optimization over all compositions into at most the number of records proves both finite sharp variance bounds and gives explicit achieving patterns. The extracted standard-library checker independently enumerates full permutations for lengths at most nine and checks the extremal bounds for every record count through length fifteen (1,151 checks). The proof addresses empty blocks, singleton blocks, and the smallest sample sizes. Enumerations alone are not used to infer all-size results.

## Originality

**PASS, with residual historical-priority risk.** The recorded comparisons cover alternative record orientations, classical insertion ranks, and joint Euler–Stirling enumerators. Gnedin supplies the independent insertion-rank and record framework. Dzhumadil'daev proves code equidistribution with prescribed right-maximal records and descent indices, but its identified results do not determine this left-to-right record-position conditional probability generating function or sharp extremal variance range. Jin studies jointly enumerated descent and record numbers rather than conditioning on the entire prescribed position set. A comparison of the implication directions is important: knowledge of counts by total records alone is insufficient to reconstruct conditional laws by the entire record-position set; equidistribution between two code statistics is not the claimed Eulerian block factorization. Literature beyond the inspected sources may have implicit equivalents; this review is not a definitive historical-priority certificate.

## Mathematical value

**PASS.** Records are a standard adaptive observation statistic, and the descent count measures local order fluctuations. Even when the number of records is fixed, distinct observed record-position configurations produce different conditional uncertainty in the descent count. The theorem gives the full conditional probability law and the exact, attained finite-sample variance envelope, instead of an isolated expectation or an unmotivated numerical example. The distinction matters for conditioning and stratification by record patterns, without claiming unproved testing improvements.

## Limitations

All conclusions require a uniform random permutation of distinct labels. The variance envelope concerns fixed-position fibers, not conditioning on record count alone. The finite checker does not establish the general proof by itself. Some older historical literature may encode a related identity indirectly. Independent scientific validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
