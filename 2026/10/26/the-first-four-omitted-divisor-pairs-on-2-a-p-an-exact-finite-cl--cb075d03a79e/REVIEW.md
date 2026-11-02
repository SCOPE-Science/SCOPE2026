# Independent mathematical audit

## correctness

PASS

The complete divisor-pair partition for n=2^a p (a>=1, p odd prime) consists of P_i=(2^i,p 2^(a-i)), 0<=i<=a, since n is nonsquare. Removing I gives a retained sum 2n iff p=(2^(a+1)-1-sum_{i in I}2^i)/(1+sum_{i in I}2^(a-i)). P_0 is too large to omit; P_a yields an even denominator and odd numerator, so I is a subset of 1..a-1. For n<=630194176, 3*2^a<=n forces a<=27, giving exactly 17,550 triples and 80,730 quadruples. Exhaustive exact-divisibility sieve yields 3 odd integral triple quotients (3531,4595,76083), none prime, and 8 integral quadruple quotients, exactly prime 601,2311,49123 with a=20,20,24. At n=2^20*601=630194176, unique four-pair indices (9,16,18,19) have omitted sum sigma(n)-2n=2096550, and independent checks rule out orders 1 or 2; order 3 is excluded for a<=27. The assertion is finite a<=27 except for the least-over-all-n order-4 example (proved via exponent bound); no statement about absence of larger-a 3-pair instances. Independently reran full sieve via separately written exact integer code and reproduced lists and counts.

## originality

PASS

Published Oct 4 Resultary note already gives the general pair-mask quotient and the first two-pair case n=11776; both are PRIOR and credited. A complete reading of its RESULT.md establishes no enumeration of three- and four-pair omissions for a<=27. Wang–Zelinsky 2026 introduces/studies strongly pseudoperfect integers, but accessible abstract and cited propositions do not establish the specific finite table. The new claim is the sharp least four-pair witness plus complete bounded 3/4-pair census, not the general sieve; priority is best-of-knowledge.

## value

PASS

The order of omitted complementary divisor pairs is a natural complexity parameter for strongly pseudoperfect representations of the natural two-prime-support family 2^a p. The least exact order-four witness with uniqueness, an unexpected no-order-three phenomenon through exponent 27, and the full finite three/four-pair census are independently useful reproducible arithmetic facts beyond a generic small-search table. The finite cutoff is explicitly meaningful because a<=27 suffices to prove global minimality of the claimed four-pair integer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
