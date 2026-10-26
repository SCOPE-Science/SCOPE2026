# Review of exact paperfolding prefix subsequence universality

## Correctness

PASS. The claim specifies the fixed binary alphabet, zero-based paperfolding positions, and all positive prefix lengths. The complete arch argument proves that the scanner count equals subsequence universality. The odd-part definition yields the four exhaustive aligned eight-symbol templates. Both reachable scanner states and every partial offset are checked directly; telescoping yields the unrestricted floor-and-two-indicators formula. The checker separately verifies the arithmetic and folding constructions, complete transition cases, all prefix lengths through 262143, and exhaustive subsequence universality through length 28. The computations corroborate but are not the infinite proof.

## Originality

PASS against inspected evidence, with an unindexed-priority qualification. Madill--Rampersad (arXiv:1208.2856, sections 1--4) analyzes abelian factor complexity, not the length of the shortest *absent scattered subsequence* of each origin-anchored prefix. Barker et al. (arXiv:2003.04629, sections 1--4) establishes generic subsequence-universality and arch methods but not an explicit paperfolding prefix law. Kosche et al. (arXiv:2108.13968, sections 1--4) establishes general shortest absent subsequences and arch structure, without paperfolding-specific closed forms. Shallit (arXiv:2412.17930, sections 1--3) determines maximal constant-symbol run statistics, a different decomposition from greedy two-symbol arches. OEIS A014577 enumerates paperfolding symbols, not the derived prefix index. The closest available research-record summaries for binary universality distributions, paperfolding prefix-normal defect, and paperfolding string attractors likewise do not imply this all-prefix formula. Full records behind some research summaries were not accessible; hidden previous priority remains a risk.

## Mathematical value

PASS. This is a complete, origin-anchored evaluation of a standard language-theoretic completeness statistic in a canonical automatic word, rather than a finite table or arbitrary residue slice. The single formula determines the shortest missing subsequence length for every prefix and proves the sharp two-sided bounded discrepancy and asymptotic rate. The eight-symbol scanner explains the surprisingly bounded fluctuations, unlike a generic linear-time arch algorithm. The fact is specific to the regular paperfolding word and does not purport to solve arbitrary folding patterns or shifted factors.

## Scientific limitations

The literature search is not a proof of priority. The result counts only the minimum absent-subsequence *length*, not absent-subsequence multiplicities or positional occurrences. The proof is mathematical and self-review; it has not undergone an independent audit.

Self-review: passed. Independent audit: not yet performed.
