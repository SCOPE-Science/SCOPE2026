# Independent mathematical audit

## correctness

PASS

For positive integers, subtracting a²+b² gives a s(a)+b s(b)=2ab. If a=1, s(b)=2 contradicts s(1)=0, s(prime)=1 and s(composite)≥3. If a=p is prime, b(2p−s(b))=p, and neither b=1 nor b=p is possible. For powers of the same prime, unequal exponents give 1≡0 modulo p after division by the smaller power; equal exponents would require s(p^r)=p^r, whereas the geometric sum is strictly smaller. For powers a,b of different primes, coprimality forces a|s(b) and b|s(a), giving a<b and b<a. This proves the support bound also for equal coordinates. The known witness (4,6) gives 4·7+6·12=100 and support 1+2. See RESULT.md lines 18–53. The recorded finite scan in verification_output.txt and verify.py is corroboration only: its main pair scan uses a<b, although the prime-power grid includes the diagonal. Independently enumerating divisors by divisor pairs through 500 and scanning a≤b found no violations, including diagonal solutions (6,6), (28,28), (496,496). No bundled code was run.

## originality

PASS

The distinct claim is the universal obstruction for the exponent-one weighted-power equation, not the example establishing sharpness. The closest definition and tables, the exponent-two sequence, and the related harmonious-pair theorem do not cover it on the inspected evidence.

## value

PASS

The pair condition is an independently introduced divisor-sum relation with published examples. The two-prime-power exclusion gives an unbounded structural restriction on its solutions and a sharp minimum of total prime support; it eliminates an entire family from classification even though one composite prime power is possible. The contribution is modest and uses elementary divisibility, but is not a recomputation of the known witness or a change of normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
