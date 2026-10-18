# Independent mathematical audit

## correctness

PASS

For prime powers, H(p^a)=sum_{j=0}^{a-1}p^{2j}-p^{a-1}, yielding 0 for prime, p²-p+1 for square and 1+p⁴ for cubes, with exponents >=4 bounded >=57. The exact expansion H(p^a q^b)=q^{2b}h_{p,a}+p^{2a}h_{q,b}+S_{p,a}S_{q,b}+R_{p,a}R_{q,b} yields H(pq)=2 and sharp >=34 when the smaller-prime block is repeated; other repeated block placement >=41. Adjoining a coprime prime-power increases H(mp^a)>p^{2a}H(m), so >=three distinct primes forces >50. Equality reduces uniquely to 2²*3=12. Independent sieve n=2..40000 reproduced the four low non-semiprime examples and sole H=34 at12. Infinite claim is symbolic, sieve corroborative.

## originality

PASS

OEIS A072780 is exactly the sequence H and already records H=0 at primes and H=2 at distinct semiprimes; those facts are not claimed as new. Inspected sequence and A072779 do not state the all-n >=34 mixed-repeated support barrier with unique equality or complete intermediate fiber list. A broad phi*sigma paper treats multiplicative square values rather than this additive sigma2 gap. Best-of-knowledge original exact threshold, with risk an old OEIS comment or short note has essentially same elementary deduction.

## value

PASS

The first value after known 0/2 fibers forced by a repeated prime factor in mixed support is a natural arithmetic phase threshold of a specific classical OEIS sequence. Determining the complete low spectrum and sharp equality (n=12) gives a complete useful initial invariant classification, not an arbitrarily selected interval unsupported by object motivation. Value is bounded, explicitly not a global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
