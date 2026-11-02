# Scientific review

## Correctness — PASS

The source condition is equivalent to excluding newly appended suffixes with period \(p\) and length \(\lceil9p/4\rceil\). Cubefreeness reduces the direct-prefix curling transform to the exact square-suffix test, while an overlap is exactly a periodic suffix of length \(2p+1\). Prefix heredity yields a complete finite recursion. `verify_full.cpp` exhausts all \(10{,}368\) labeled terminal words and directly checks the four joint counts; `verify.py` independently exhausts \(1728\) normalized representatives and verifies the factor-six orbit correspondence. Two exact fraction calculations identify critical exponents \(2\) and \(\frac{11}{5}\) only. Neither checker relies on random samples, floating-point thresholds, or heuristic search.

## Originality — PASS, with residual priority uncertainty

The full primary text of Caveney–Dong–Shallit, arXiv:2608.15670v1, Theorems 7 and 9 and Appendix B, establishes the maximum length and raw counts but not this joint transform/critical-exponent distribution. A previously recorded result for the stricter \(6048\)-word overlap-free subclass identifies two transforms but does not cover the additional \(4320\) sources admitted by \(\frac94\)-power-freeness. The new information includes the sharp \(\frac{11}{5}\) critical-exponent stratum and its exact fibres. Relevant exact-phrase literature comparisons located no broader statement. A supplementary or unindexed prior calculation could still contain an equivalent classification.

## Value — PASS

This is a natural, complete classification precisely at the source's sharp \(\frac94\)-power-free boundary, not an arbitrary sample of lengths. It reveals a gap in attainable source critical exponents and striking rigidity of the image under a highly nonlocal word transform: relaxing the source beyond overlap-freeness adds \(4320\) words without adding a single transform. It resolves the full joint critical-exponent/transform profile rather than re-enumerating the published \(10{,}368\) count.

## Scope and remaining limits

No theorem is claimed for longer words, weaker exponent constraints, or other alphabet sizes; source date is the original August 16, 2026 preprint. Verification is reproducible but does not constitute independent expert audit.

Self-review: passed. Independent audit: not yet performed.
