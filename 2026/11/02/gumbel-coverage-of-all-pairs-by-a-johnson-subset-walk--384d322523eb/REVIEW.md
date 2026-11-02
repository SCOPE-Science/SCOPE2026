# Scientific review: Gumbel coverage of all pairs by a Johnson-subset walk

**Correctness (C): PASS.** The exact finite-state restriction to a fixed set of marked labels preserves avoidance probability. At zero arrival rate the killed kernel has simple eigenvalue 1 and a fixed spectral gap. Analytic perturbation of its quasi-stationary left eigenvector gives the coefficient \(2(r-1)|E(F)|\) without an assumption that forbidden pairs are disjoint. Factorial moments then yield the Poisson missing-pair count and Gumbel coverage time. A one-pair exponential tail gives the expectation. Exact enumeration and an independently implemented reduced-chain calculation passed 212 assertions. Remaining risk: the analytic argument is same-author reviewed; no external referee has checked it.

**Originality (O): PASS, subject to historical-priority uncertainty.** Athreya, Mukherjee and Mukherjee (arXiv:2304.01145, Conjecture 2.4) give a conjecture for dependent block updates and prove the \(s=r\) case; their Gumbel theorem is for independently resampled blocks. The present \(s=2\), \(r\ge3\) statement is not a special case of those proved results. Godbole and Janson (1996) treat independently selected blocks, so their coverage conclusions do not imply this Markovian law. Searches for other lower-shadow Johnson-walk cover laws did not identify a directly covering theorem. Specialized unindexed or unpublished work remains a priority risk; a failed search is not proof of uniqueness.

**Value (V): PASS.** The theorem resolves a natural, expressly formulated open subfamily of the Markovian super-coupon conjecture, including every fixed block size larger than two, and strengthens the expected-time prediction to a sharp extreme-value distribution. The universal graph-edge coefficient is a structural explanation of why overlapping target pairs do not change Poisson coverage at the terminal scale. This is not just a finite table or parameter substitution.

**Limits.** Only fixed \(r\) and pair targets are proved. No rates, no growing \(r\), and no claim of independent validation.

Self-review: passed. Independent audit: not yet performed.
