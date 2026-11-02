# Self-review

## Correctness — PASS

The objects and quantifiers are explicit: all even \(k\ge2\), all \(n\ge0\), and all prime powers at primes outside a five-element set. The recurrence identity gives \(D_k\mid E_k\). The exact Lucas norm invariant reduces a possible spurious cubic endpoint pair modulo an odd prime to nine cubic-root cases. Their Eisenstein norms, \(0,189,39,75,219\), restrict nontrivial possibilities to small primes; the case five is excluded by bijective cubing. Hensel lifting is direct because derivatives at the two true endpoint values are units for \(p\ne3\). A cubic telescoper then forces every window sum to vanish to the same prime-power precision. The infinite obstruction families use exact initial gcds and genuine Lucas modular periods. The order-four recurrence justifies using four windows for every exact gcd computation. The standalone verifier checks all nine algebraic norms and 300 separate even lengths. Computations are corroboration, not the infinite proof.

## Originality — PASS within inspected evidence

The motivating arXiv:2204.12626 paper proves first- and second-power analogues and poses cubic-window questions, but neither supplies a finite exceptional-prime classification nor an Eisenstein norm obstruction. The earlier arXiv:2104.12262 treats first powers. The closest accessible separate cubic-window finding treats Fibonacci values, not Lucas values, and does not imply the exceptional-prime claim. Specific research-record and literature searches about Lucas cubic windows, endpoint congruences, and the set \(\{7,13,73\}\) returned no covering theorem. Searches do not establish absolute novelty. Residual risk: an unindexed subsequent solution or a general theorem implying this local specialization.

## Mathematical value — PASS

The motivated question is when two endpoint cubic congruences correctly determine the GCD of **all** sliding cubic Lucas sums. The finding classifies the complete possible prime support of the discrepancy, for infinitely many block lengths, and proves that each of three exceptional odd primes genuinely produces an infinite obstruction family. It distinguishes a nontrivial cubic-root obstruction from the ordinary recurrence-period criterion, giving a useful local sieve for any future full cubic-GCD formula. It is more than a numerical counterexample, a normalization check, or a finite recomputation. It does not solve the complete cube-GCD problem.

## Literature and limitations

Inspected primary: Mbirika–Spilker, arXiv:2204.12626 (2022), introduction, GCD tables, Section 6.1 and references; Guyer–Mbirika, arXiv:2104.12262 (2021), abstract and original-GCD scope. The printed Lucas cube expression in the former includes a second endpoint subtracting \(9\), but the true difference of cubed values subtracts \(27\). The present theorem consistently studies the latter and makes no claim about the printed proposal. Unindexed higher-power extensions cannot be excluded. Independent mathematical audit not performed.

Self-review: passed. Independent audit: not yet performed.
