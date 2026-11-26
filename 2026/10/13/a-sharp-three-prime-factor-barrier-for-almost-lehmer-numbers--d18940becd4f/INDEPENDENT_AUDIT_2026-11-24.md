# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 21–71. Because ℓ divides n−1, the right-hand side is coprime to n; hence gcd(n,φ(n))=1. A repeated prime factor would divide φ(n), and an even composite would share the factor 2 with φ(n); thus only odd squarefree composites need consideration. For n=pq with distinct primes, an independent valuation argument confirms the exclusion: choose a prime r at which p−1 and q−1 have unequal valuations s<t. Then v_r(pq−1)=s, by expanding (p−1)+(q−1)+(p−1)(q−1), whereas v_r(φ(pq))=s+t. Divisibility requires v_r(ℓ)≥t. If s=0 this is impossible because ℓ divides pq−1; if s≥1 it requires valuation at least 2, impossible since ℓ is squarefree. This also confirms the logic of the frozen gcd argument: the coprime quotients a,b must divide ℓ, while gcd(ab,hab+a+b)=1 forces ab to divide h and then the complementary factor of ℓ, contradicting squarefreeness unless p=q. Directly, 1729=7·13·19, φ(1729)=1296, and 3·1728=4·1296 with 3 a squarefree divisor of 1728. The reduced-denominator test d is valid by canceling gcd(φ(n),n−1): admissibility is exactly d squarefree and d|n−1. Read VERIFICATION.md, verify.py and verification_output.txt; the reported finite regression was not rerun and is not needed for the unbounded proof.

## originality

PASS

The definition, odd squarefree reduction and witness 1729 are prior work, and the classical Lehmer bound concerns a proper subclass. The distinct claim is the unbounded semiprime exclusion under the exact almost-Lehmer constraint, making the known witness sharp in the number of distinct prime factors.

## value

PASS

The minimum distinct support is a natural exact invariant of an established Lehmer class. Unlike the known odd squarefree reduction, this result rules out the entire lowest remaining composite support, with a local obstruction showing why the squarefree multiplier constraint excludes two primes even though the adjacent power class admits them. The known example supplies sharpness, not the contribution by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
