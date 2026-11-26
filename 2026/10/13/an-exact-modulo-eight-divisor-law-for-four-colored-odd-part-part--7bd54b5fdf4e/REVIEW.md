# Independent mathematical audit

## correctness

PASS

The unrestricted colors give F4=E(q²)P². Jacobi's identity gives P=1+2B with B modulo 2 equal to the positive-square series. Modulo 8, P²=1+4(B+B²), where B² modulo 2 has only even degrees. As E(q²) is even, at odd n Euler's pentagonal expansion leaves only four times the number of n=j(3j−1)+s² with integer j and s>0. Completing the square gives x=6j−1,y=2s and N=12n+1≡13 mod 24. Modulo 8 forces y even (y odd would require x²≡2), then y≡2 mod 4; modulo 3 forces 3∤x. Both coordinates are nonzero and each four-sign orbit has exactly one such (j,s), since just one sign of x is −1 mod 6. In the Euclidean Eisenstein ring, norm-N ideals number H(N) by splitting; their six generators reduce twice over each of the three nonzero classes modulo 2 (N odd). Exactly two are in the suborder Z[√−3], so 4 times the pentagonal-square count equals 2H(N). Since N is nonsquare, the inert-prime test and product of e+1 over split primes give precisely the stated 0/4 residues. For a fixed finite set of split primes, the exact-exponent-one indicators are asymptotically independent on N≡13 mod 24 by CRT, each with mean (p−1)/p². The sum of means diverges as the set grows and the variance is at most the mean. Chebyshev bounds the proportion with fewer than two occurrences by a quantity tending to zero; two factors of 2 suffice for mod 8. Dirichlet primes 13 mod 24 give infinitely many residue-4 exceptions. Independent replay: the logarithmic-derivative recurrence n·a4(n)=Σ_{k=1}^n a4(n−k)Σ_{d|k}d·color(d) matched the divisor expression at 201 positive odd indices through 401 (independent_checks.py 3); the written proof, not the finite check, covers all odd indices and density. No even-index law, higher modulus, or quantitative density claim.

## originality

PASS

Credit the identical family and product to published work, and the quadratic representation count and character sum to classical arithmetic. The supported distinct claim is the complete odd-index modulo-eight bridge from this product to the divisor sum, including its factor criterion and density consequence. The closest inspected same-family progressions have different moduli.

## value

PASS

This natural partition family already motivates congruence questions. The mod-8 law resolves every odd coefficient, replaces coefficient expansion by a prime-factor test, and distinguishes density-one vanishing from infinitely many explicit exceptions. The odd restriction comes from even support in the theta calculation rather than a chosen cutoff or isolated progression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
