# Scientific review

## Correctness
**PASS.** For every prefix and suffix, the scattered \(01\) count splits into within-prefix pairs, within-suffix pairs, and the product of prefix-zero count and suffix-one count. This gives exact right quotients. Every parameter pair claimed reachable has an explicit prefix. The proof shows all zero, dead, one-one, and multi-one quotient identifications and uses explicit distinguishing suffixes to prevent false mergers; it separately verifies the \(k=0\) boundary. Therefore the Myhill–Nerode count is exact for all \(k\). The standalone script confirms the formula for \(k=0,\ldots,45\), but no finite test substitutes for the universal proof.

## Originality
**PASS, with literature risk.** The closest inspected primary works concern (i) whether at least one occurrence of a subsequence exists in a regular-language text, and (ii) the number of fixed-length binary words with exactly a given number of scattered occurrences. Neither statement entails the exact minimal number of states for the unbounded-length fixed-multiplicity language or the full quotient classification. The comparison includes the distinct notation of binary inversion count and Parikh-matrix entries. Database and published-result searches did not locate a matching stronger theorem, but incompleteness of such searches remains a real uncertainty and no claim of certified priority is made.

## Mathematical value
**PASS.** The counting condition is a natural exact-multiplicity refinement of binary subsequence matching, and state complexity is an intrinsic minimal memory requirement of its regular language. A naïve two-counter saturation automaton does not exhibit the exact quotient identifications. The proof identifies all equivalence classes and delivers a sharp closed form, explaining the quadratic dependence with precise parity correction; the result is neither a renaming of a sample enumeration nor a routine case of the published pattern-existence bound.

## Closest literature and limits
Brzozowski–Davies–Madan, arXiv:1806.04645, studies pattern existence and worst-case state-complexity operations. Menon–Singh, arXiv:2306.07870, studies length-restricted multiplicity enumerations. Publication search is not exhaustive, so a non-inspected theorem might cover the formula. The statement is only for the binary scattered \(01\) pattern and fixed \(k\).

Self-review: passed. Independent audit: not yet performed.
