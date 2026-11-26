# Independent mathematical audit

## correctness

PASS

With n>5 the congruence is exactly remainder five; write sigma(n)=kn+5. A prime power must have prime p dividing 4; the remainder for a power of two greater than five is n−1, never five. With at least two prime divisors the proper divisors 1,p,q make k≥2. The strict divisor-ratio product excludes two odd primes. With support {2,p}, the ratio is less than 3 and parity forces an even exponent b of p, hence k=2 and (2^(a+1)−p)(1+p+...+p^(b−1))=6. The positive sum is at least 4, so it must be 6; the only possibility p=5,b=2 requires 2^(a+1)=6. For three odd primes the ratio is less than 3 and parity again gives all even exponents. The upper ratio bounds force 3,5 and a third prime below 16 (the comparison is exactly 2 at 16). For 7 or 13 the two non-5 primes have order 4 mod 5, so their odd-length geometric sums cannot vanish; for 11 the full divisor sum is 1 mod 3 instead of 2. Finally for any even n in scope, oddness of sigma(n) forces even exponents for every odd prime. The exact inequalities and modular constants independently checked by python3 -B /workspace/branches/frozen_math_replay.py (divisor section). Frozen verify.py was inspected, not executed; its bounded scan cannot imply the infinite claim. No existence or nonexistence conclusion for the remaining support classes.

## originality

PASS

The standard parity fact about odd divisor sums is not credited as independently original. The substantive statement is the exclusion of every two-prime case and every odd three-prime case for the actual remainder five. The closest primary sources study exactly the general congruence, but give small known examples, regular-family criteria, sparsity or finiteness results, not these unrestricted local exclusions. The decision is limited to the structural bounds, not the conjectural absence of any remainder-five integer.

## value

PASS

The target remainder is a documented unresolved entry, not an arbitrary numerical test. The proof removes whole unbounded families rather than pushing a search limit: the least possible support must be even with exactly two distinct odd primes both to even powers, while the odd branch needs at least four primes. The useful part is the exclusion with arbitrary exponents and primes, not the textbook parity lemma or the scan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
