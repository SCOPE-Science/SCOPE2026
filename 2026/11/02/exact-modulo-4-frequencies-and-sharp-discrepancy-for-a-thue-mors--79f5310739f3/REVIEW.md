# Scientific review

## Correctness
PASS. The signed-block transfer on \(2\times16\times4=128\) integer coordinates satisfies a four-level periodicity. An exact four-phase recurrence has characteristic polynomial \((X-16)(X-1)(X^2-X+16)\), and its primitive-state spectral projector yields the universal leading residue vector \((1,2,1,2)/6\). A binary-block decomposition proves the estimate for every initial interval, not merely powers of two. The four rational generating functions are certified from the recurrence plus exact initial coefficients; a noncancelled pole establishes the sharp exponent. Recomputing the certificate from the included standalone checker returns `VERIFY_OK`. A separate \(65{,}536\)-term recurrence enumeration agrees with the predicted count vector \((10922,21729,10924,21961)\). Finite enumeration alone would not prove the theorem; the exact transfer induction does.

## Originality
PASS within inspected sources. Lipka and Ulas, arXiv:2109.15243v1, Theorem 3.4 and Example 3.6, provide automaticity and a modulo-\(4\) automaton, but no natural-density vector, dyadic count fractions, or sharp global discrepancy estimate. The present statement is quantitatively stronger in these directions: automaticity does not itself ensure natural densities or their optimal error. Searches for this recurrence together with modulo-\(4\) frequency, the four constants, generating functions, square-root discrepancy and related formulations did not locate an equivalent statement; semantically related mathematical-record hits concern different objects. Search failure is not priority certification, and a later unindexed use of the published automaton remains a risk.

## Mathematical value
PASS. The published parity result explains why the sequence is not uniformly distributed modulo \(4\), but does not split the parity classes into exact asymptotic frequencies. Determining their precise imbalance, all four dyadic distributions, and an optimal discrepancy exponent resolves a natural arithmetic-statistical question for an automatic recurrence whose published modulo-\(4\) automaton has 80 states. The uniform eigenprojection for every primitive starting pair is the structural step allowing ordinary natural densities rather than only dyadic densities; the noncancelled complex poles explain the unavoidable oscillation. This is a substantive invariant rather than an arbitrary finite residue table.

## Limits and sources
Primary: E. Lipka and M. Ulas, arXiv:2109.15243v1 (2021-09-30), full preprint sections 1, 3, and concluding questions; published DOI:10.1080/10236198.2022.2065918. Independent priority certification and independent scientific audit have not been performed. The theorem is limited to modulus \(4\) and the specified initial values.

Self-review: passed. Independent audit: not yet performed.
