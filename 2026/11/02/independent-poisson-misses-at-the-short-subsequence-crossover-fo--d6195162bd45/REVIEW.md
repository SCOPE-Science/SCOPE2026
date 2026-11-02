# Scientific review

## Correctness
**PASS.** A random-word greedy subsequence matcher advances with independent Bernoulli probability \(1/2\); therefore one-pattern avoidance is exactly a binomial lower tail. The critical nonstandard lemma shows that avoiding two distinct length-\(r\) patterns has \(O_r(n^{r-2})\) possible source words, by bounding the number of loop-capable states in a joint greedy automaton. This gives asymptotically disjoint rare misses per sampled word, the multivariate Poisson generating-function limit, and the LCS sandwich by lengths \(r-1\) and \(r+1\). Exact finite-state checks corroborate the combinatorial counts, including direct brute-force comparisons for small inputs. Fixed positive \(r\), all binary patterns, and all \(\lambda\in(0,\infty)\) are covered.

## Originality
**PASS, subject to residual priority risk.** The closest full primary paper (Li–Ren–Wen, arXiv:2504.10425) establishes estimates for a length-normalized LCS constant using a distinct order of limits. The full-text comparison of Heineman et al. (arXiv:2407.10925) also concerns those constants, not an exponentially growing sample with fixed subsequence length. Related exact single-word subsequence-universality and shortest-absent-subsequence results do not imply the joint multiword Poisson law. Explicit searches for the proposed Poisson scaling, aliases, equivalent pattern-intersection formulations, and stronger all-parameter results did not identify covering results. A prior formulation in occupancy or random-language terminology is a residual possibility.

## Value
**PASS.** The 2025 primary paper underscores interest in LCS across many independent words. The new theorem describes a distinct natural finite-size regime that cannot be characterized by normalized fixed-sample constants: it gives the sharp threshold \(d\asymp2^n/n^{r-1}\), the complete distribution of the number of shared length-\(r\) patterns, and the two-point fluctuation of LCS length. A joint limit for all \(2^r\) patterns is structurally stronger than a union bound or a single expectation. The exact scaling avoids integer-length lattice ambiguity.

## Sources and limits
Li, Ren and Wen (arXiv:2504.10425, Cambridge HTML full research text); Heineman et al. (arXiv:2407.10925v1, arXiv HTML); publicly accessible binary subsequence-universality and shortest-absent-subsequence results. Neither independent mathematical refereeing nor exhaustive verification of the entire historical literature has been performed. Extensions to growing pattern lengths, nonbinary alphabets, and nonuniform sources remain outside scope.

Self-review: passed. Independent audit: not yet performed.
