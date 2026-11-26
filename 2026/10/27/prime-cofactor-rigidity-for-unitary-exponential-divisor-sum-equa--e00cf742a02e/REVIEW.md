# Independent mathematical audit

## correctness

PASS

The prime-power definitions give (q+1)U=qE with U=prod(p²+1) and E=prod(p(p+1)). For one squared prime, integrality of q=p+1+2/(p−1) gives exactly (2,5),(3,5), and the original sums agree. For at least two squared primes, every omitted factor of E/U exceeds 1, so q<p+1+2/(p−1) at each p. If the least p is at least 5, this and primality give q<p at the least p and even q+1<p there (p−1 is composite). Every repeated prime consequently divides U and is 1 modulo 4, since it divides a different factor t²+1. The 2-adic valuations of U and E are then equal, incompatible with consecutive q and q+1. If the least repeated prime is 3 (respectively 2), q is forced to be 2 (respectively 3), and every other repeated prime is again 1 modulo 4. At support size k the valuations of the two sides are respectively (k,k+2) and (k+1,k), excluding both cases. Independent divisor-pair enumeration matches 4,441 tests, 2,855 with multiple squared primes, and only 20 and 45 (common sums 30 and 60). The bounded replay corroborates, but is not the proof of, the unbounded exclusion.

## originality

PASS

The singleton classification is prior work. Credit is limited to the uniform exclusion when the squared support has cardinality at least two. The closest checked primary and published-result statements either give numerical examples, bound total prime multiplicity by four, or permit only one repeated prime. None establishes the multi-support exclusion.

## value

PASS

This isolates a natural next exponent pattern in an existing equality problem and rules out solutions at every squared-support size, not just in one more enumerated layer. The interaction between the prime cofactor inequality, quadratic-residue obstruction and 2-adic comparison gives a structural explanation; the already known positive examples are not the contribution. It makes no claim about composite cofactors, higher exponents or infinitude of general solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
