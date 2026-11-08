# Self-review

## Correctness — PASS

Euler's prime-power totient formula forces every prime factor of a preimage of \(8q\) into the candidate list \(2,3,5,2q+1,4q+1,8q+1\). Any larger mixed candidate is squarefree in the preimage; a doubled factor of \(3\) or \(5\) forces \(q=3\) or \(q=5\), respectively. Exactly one factor supplies the sole prime factor \(q\) of the target totient. Solving the remaining bounded \(2\)-power budget yields the three disjoint normal families; the two square-divisor branches yield exactly three further members each. Every displayed preimage is verified by multiplication of coprime prime-power totients, and the four-step exclusion is exhaustive. An independent exact-arithmetic verifier compares the formula with both a totient sieve and a prime-power inverse enumeration for 167 odd primes.

Scientific limits: the finite checks are not infinite proofs; the unrestricted claim is supported by the prime-factor classification and exhaustive exponent equations. The theorem does not address general exponents \(s\ge4\).

## Originality — PASS (qualified)

The strongest inspected primary source, He (arXiv:2610.34808v1), develops the family \(X_{2^s q}\) in its entirety, settles \(s=2\), and explicitly leaves \(s\ge3\) open in Open Problem 16. Its Table 2 reports six numerical fiber sizes for \(s=3\) rather than the uniform theorem. Shannon–Shiue–He–Saito (2025) proves the \(4q\) case and describes the general inverse-totient enumeration technique, but supplies neither the exact \(8q\) sets nor the exceptional branches and uniform cardinalities. Related mathematical-research searches and indexed web queries did not reveal a covering theorem. Matching the methods is not the same as proving the infinitely parameterized formula; explicit prime-factor cases and exceptions are necessary. Priority is not independently certified: an unindexed general treatment or an implicit special-case classification is a residual risk.

## Mathematical value — PASS

This is a complete classification of the **first open** exponent in an explicitly posed natural family, not a preset numerical extension. It resolves every odd prime parameter, exhibits a new two-branch coexistence giving fiber multiplicity six, classifies all generic cardinalities \(\{0,2,3,4,6\}\), includes the two previously tabulated exceptional primes, and gives a uniform exact description at \(s=3\). The no-singleton consequence was already available from Grosswald's criterion, and is not counted as a new stand-alone contribution. These exact sets and counts are mathematically motivated by Carmichael's totient-preimage question; their value does not depend on a downstream general theorem.

## Closest literature and residual risks

He (2026), §5.2, Proposition 15, and §5.3 Table 2 provide structural analogues and six overlapping finite counts. He (2026), §5.4 Open Problem 16 explicitly records the infinite-family gap. Shannon et al. (2025), §2.3, provides a generic prime-factor enumeration and a narrower result at \(4q\). Shannon et al. Table 1 already gives the finite exceptional fibers at \(24\) and \(40\); they are boundary conditions, not independent discoveries. Grosswald (1973) already implies no singleton at any target not divisible by \(32\), and therefore covers the no-singleton corollary of this theorem. The priority claim is restricted to the new uniform exact \(8q\) fiber formula and its cardinality classification. A general inversion algorithm is not a formula for all symbolic odd-prime parameters. Unindexed prior work could in principle contain an equivalent specialization. No claim of independent expert checking or of resolving the general Carmichael conjecture is made.

Self-review: passed. Independent audit: not yet performed.
