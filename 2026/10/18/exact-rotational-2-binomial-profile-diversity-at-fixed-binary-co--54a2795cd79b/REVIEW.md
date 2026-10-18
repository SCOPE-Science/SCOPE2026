# Review of the rotational binary \(2\)-binomial diversity theorem

## Correctness — PASS

Equality of full \(2\)-binomial signatures for words with equal numbers of ones and zeros is equivalent to equality of their weighted one-position sums. Cyclic rotation has the exact increment \(n w_i-k\), so all equality pairs have starting indices congruent modulo \(L=n/\gcd(n,k)\). Events that several of the \(g\) positions in one residue group have equal sums impose independent fixed-sum conditions on a partition of the circle into disjoint arcs. Each probability is a product of binomial coefficients divided by \(\binom{n}{k}\). Inclusion-exclusion by equality clusters gives the exact expectation. Equality in the lower bound \(C(w)\ge L\) is equivalent to period dividing \(L\), since subtracting consecutive length-\(L\) window counts forces every bit to repeat after \(L\). Fixed-gcd uniform Stirling estimates give the square-root correction, with all terms of subset size at least three bounded in total by a constant. The code independently checks all \(66\) pairs \((n,k)\) with \(2\le n\le12\), \(1\le k<n\), comprising \(8{,}166\) words. Finite checks support but do not prove the infinite theorem.

## Originality — PASS, subject to residual literature risk

The closest fully inspected authors' treatments, Lejeune–Rigo–Rosenfeld (arXiv:2001.11732) and Rigo–Stipulanti–Whiteland (arXiv:2201.04603), respectively address all-word equivalence class structure and factor complexities of infinite words, neither of which determines class diversity restricted to an individual cyclic orbit. Whiteland's binomial-monoid conjugacy equations allow auxiliary words and therefore do not directly establish equality of the particular cyclic rotations. Published-record searches compared adjacent multispectra, necklace orbits, and subsequence universality on their actual implications and found no prior equivalent full formula. The 2015 infinite-word binomial-complexity work was available at abstract level only, and equivalent results under alternative terminology remain possible.

## Mathematical value — PASS

The result determines a natural reconstruction invariant for every fixed binary composition, with an exact gcd-controlled arithmetic obstruction, full characterization of minimum diversity, and a sharp square-root loss beyond the trivial upper bound under random fixed-weight sampling. These features explain when unknown rotation starts are distinguishable using scattered pairs. It does not assert results for general alphabets, error channels, or growing gcd.

Self-review: passed. Independent audit: not yet performed.
