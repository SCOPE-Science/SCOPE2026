# Scientific review: early square defects in reciprocal-sum sequences

## Correctness

**PASS.** The claim concerns a definite rational recurrence and a fixed notion of integer square. The original source's recurrence and square criterion were checked against its complete Sections 2 and 4. Reconstructing the local reduction gives the two polynomials \(t^2+1\) and \(t^4+3t^2+1\); the latter has two quadratic factors of discriminant \(-5\) after adjoining \(i^2=-1\). Quadratic reciprocity establishes each mod-\(20\) case, including the ramified prime \(5\). Local events for consecutive numerators are disjoint, the Chinese remainder theorem proves the exact joint distribution and period, and an antecedent-discriminant obstruction rules out every later failure in the specified prime classes. The reverse implication uses an explicit initial value. Finite checks are independently reproducible but are not substituted for infinite arguments.

## Originality

**PASS with residual priority risk.** The source paper proves a universal per-sequence bound and poses the distribution of failures over starting values as an open question; it does not give the two-index product law or the sharp all-index no-later-failure criterion. Jones and Manes develop a general preimage-tree picture for the same rational map, including the first two levels; those structural facts do not explicitly give the joint starting-value law or all-index modulus classification. Searches for the exact polynomials, residue classes, and starting-value densities did not find an equivalent statement. The old general results make this a plausible elementary specialization, and an unlocated 2026 companion preprint is a genuine residual risk; independent priority checking remains advisable.

## Mathematical value

**PASS.** The exact joint probabilities answer a finite-depth form of the source paper's explicit quantitative question. More importantly, a sharp congruence criterion yields the *complete* count distribution across all indices for a natural infinite family of moduli. Products of arbitrarily many primes \(13\pmod{20}\) give an unbounded separation between the published bound and the true maximal number of failing indices. The phenomenon is explained by disappearance of second-level preimages when \(-5\) is a nonsquare, not by an arbitrary numerical cutoff.

## Literature and limitations

Primary sources: arXiv:2610.00765v1 (complete accessible text, Sections 2, 4, 7); Jones–Manes, *Galois theory of quadratic rational functions* (2014), especially introductory preimage-tree discussion, Figure 2 and the discriminant machinery. The cited 2026 companion *Arithmetic dynamics of z+k/z* could not be retrieved in full; an unindexed statement there might reduce priority. Nothing herein supplies the full distribution for arbitrary \(h\) with deep preimage trees.

Self-review: passed. Independent audit: not yet performed.
