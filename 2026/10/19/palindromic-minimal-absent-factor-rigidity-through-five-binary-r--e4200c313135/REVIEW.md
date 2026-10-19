# Mathematical review

## Correctness — PASS

The source word's complete factor occurrence criteria are determined by traversal of its five maximal constant-symbol runs. They imply the five disjoint minimal-absence families after considering every candidate run count from one through six; larger counts cannot satisfy the present-prefix/present-suffix requirement. The resulting exact cardinality is an algebraic sum of the five family sizes. The three- and one-run reductions complete the at-most-five-run rigidity theorem, while `0010110100` supplies an explicit sharp seven-run counterexample. The standalone checker computes *whole minimal-absent-factor sets* for 1728 five-run choices and 342 shorter palindrome cases and verifies the two nonpalindromic factors in the counterexample. These finite checks support, but do not replace, the universal proof.

## Originality — PASS with residual risk

The closest primary work, Akagi et al., *Minimal Absent Words on Run-Length Encoded Strings* (arXiv:2202.13591), supplies general run-length enumeration and a five-category decomposition, rather than the closed symmetric five-run factor classification and sharp palindromicity threshold here. Mieno et al., *Palindromic Trees for a Sliding Window and Its Applications* (arXiv:2006.02134), treat minimal absent *palindromic* words defined by an inner-factor condition, not all ordinary minimal absent factors and their forced palindromicity. Accessible research-record and keyword searches did not identify equivalent parameter-uniform coverage, but search failure is not proof of novelty. A specialized example or equivalent theorem in an unindexed source remains possible.

## Mathematical value — PASS

The full three-parameter classification makes the antidual factor language of low-run palindromes explicit without expanding long runs; the exact count depends on two simple run comparisons. More significantly, **palindromicity of every minimal absent factor** holds for *all* binary palindromes with at most five runs, with a certified sharp failure at seven. This is a natural structural threshold for compressed palindromic strings and absent-factor algorithms, not a numerical table extension or a change of terminology.

## Scientific limitations

The classification is binary and for symmetrically patterned five-run words. It is not a general formula for all five-run nonpalindromes; the sharp counterexample does not classify seven-run cases. Finite computer checks cannot establish the universal statements, which rest on the given factor-incidence proof. Search coverage cannot exclude all unindexed literature.

Self-review: passed. Independent audit: not yet performed.
