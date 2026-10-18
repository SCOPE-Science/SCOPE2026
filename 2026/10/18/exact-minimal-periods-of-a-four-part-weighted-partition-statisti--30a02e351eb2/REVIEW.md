# Self-review

## Correctness — PASS

An explicit bijection with four independent nonnegative slack variables yields the weighted generating function. Clearing its denominators gives an exact integral identity with degree-16 numerator and degree-22 cyclotomic denominator, independently recomputed by `verify.py`. The numerator residues \(864\), \(32\), \(6\), and \(-12\) against the four cyclotomic factors establish coprimality modulo all primes at least five. A binomial expansion proves the candidate periods for every prime power; reduction modulo primes and evaluation at the sixth-order neighborhood of one prove that every period contains the full candidate factor. CRT proves the arbitrary-modulus claim. Brute-force partition enumeration through 74 and ten modular sample checks agree. This is an infinite algebraic proof, not an inference from those checks.

## Originality — PASS within inspected literature

Ballantine–Beck–Merca (arXiv:2408.13346v1, §1 and §3, published open-access article 2025) explicitly list the same statistic's minimal periods as conjectural except for their proved moduli two, three, and four. Their table records the anticipated values for five, seven, eleven, thirteen, and other primes; it does not give the all-prime-power formula or a numerator-coprimality minimality proof. Nijenhuis–Wilf and Kwong are cited there for unweighted partition counts, a different generating numerator. Targeted searches for aliases of the weighted statistic, periods, cyclotomic denominators, and prime powers did not locate a dominating statement in consulted records. A specialized result in unindexed literature or an unexamined corollary of a general rational-series period theorem remains possible; independent priority has not been certified.

## Mathematical value — PASS

The subject is an explicit conjectural table in a published investigation. The formula resolves an infinite modulus family rather than extending the table by a few entries, distinguishes a genuine five-adic exceptional regime, and settles all powers of every prime at least five. The period is proved *minimal* from the initial coefficient, not merely a valid eventual period. The result is a natural and reusable sharp arithmetic invariant.

## Limits

Moduli divisible by two or three are outside scope. Independent historical priority assessment remains open; the algebraic certificate is separately reproducible without any private archive.

Self-review: passed. Independent audit: not yet performed.
