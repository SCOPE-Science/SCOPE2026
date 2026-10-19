# Self-review

**Correctness — PASS.** On each fixed set of \(m\) labels, all full-support scattered palindromes have lengths \(2m\) or \(2m-1\). Counting the even palindromic restricted words and pairs of odd palindromic words with their single-insertion superwords yields the exact mean \(2m/(2m-1)!!\). Symmetry and linearity give the finite formula. The asymptotic uses an explicit sinh generating function, its computable first two moments, Chebyshev concentration at \(m\sim\sqrt{q/2}\), and a uniformly valid logarithmic product expansion. Direct enumeration verifies exact means through five labels.

**Originality — PASS, with residual risk.** The inspected double-occurrence insertion paper (arXiv:1811.11739), longest-palindromic-subsequence paper (arXiv:1901.07502), standard distinct-palindrome counting problem, targeted semantic published-record searches, and accessible earlier extremal claims do not supply the uniform double-occurrence expectation or its constant-factor stretched-exponential asymptotic. The earlier sharp maximum does not imply a first moment. An unindexed equivalent remains possible.

**Value — PASS.** The exact expectation and its nontrivial exponential-scale asymptotics quantify the typical distinct scattered-palindrome burden of random Gauss/double-occurrence words. The limiting factor \(e^{-1/4}\) comes from collisions caused by sampling without replacement; omitting it gives an incorrect leading asymptotic. This solves a natural infinite-family average-case counterpart to individual-word enumeration.

**Limits.** No higher moments, concentration of the palindrome count itself, or formulas for other multiplicity profiles are asserted. Finite enumeration corroborates rather than proves the theorem.

Self-review: passed. Independent audit: not yet performed.
