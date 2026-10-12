# Scientific review

## Correctness — PASS

For arbitrary integer \(a\ne0\) and initial values with all positive-index terms nonzero, the exact expression \(x_n=(Cn+D)a^{n-1}\), with \(C=x_1-a x_0\) and \(D=a x_0\), reduces the integrality question to an affine sequence. In the two exceptional branches \(CD=0\) all generalized coefficients are integers and divisibility holds. Otherwise Dirichlet supplies infinitely many denominator primes with exactly \(\nu_p({2k\brack k}_x)=-1\). The same primes directly violate the required index divisibility. All negative, zero-initial, positive-root and unit-root boundaries under the stated hypotheses are covered. Exact rational finite checks in `verify_output.txt` support but cannot replace this proof.

## Originality — PASS relative to checked sources

Shapiro [1], especially Section 4.4 and Open Questions 29(1), explicitly asks which second-order recurrences are binomid and whether binomidness implies divisibility. His zero-initial Lucas-case implication is prior work, not claimed here. Granville [2] classifies recurrences already satisfying index divisibility; that does not determine whether other recurrences may nevertheless be binomid. Related indexed companion-Lucas binomid classifications and repeated-root quotient-set density results have different initial hypotheses or arithmetic invariants, hence do not imply this criterion. The checked literature does not state the infinite-prime denominator obstruction. There is residual risk from equivalently phrased classical generalized binomial literature outside the inspected sources; search absence is not proof of global novelty.

## Value — PASS

Repeated characteristic roots are a canonical structural branch of second-order integer recurrence theory. This theorem gives a complete natural branch of a published order-two binomid classification question, not a finite computation or isolated exceptional index. Its infinite family of explicit prime-denominator obstructions makes the boundary effective in the sense of providing a construction from arbitrarily large Dirichlet primes, though no least-prime bound is obtained.

## Scope and limitations

The statement requires integer nonzero repeated characteristic root and nonzero positive-index terms. It does not answer the full distinct-root classification nor the higher-level binomid question. It uses Dirichlet's theorem. Equivalent unindexed results remain a bibliographic risk. The exact verifier explores finite examples only.

Self-review: passed. Independent audit: not yet performed.

## References

[1] D. B. Shapiro, *Divisibility Properties for Integer Sequences*, INTEGERS 23 (2023), A57; arXiv:2302.02243v1.

[2] A. Granville, *Classifying linear division sequences*, arXiv:2206.11823v1 (2022).
