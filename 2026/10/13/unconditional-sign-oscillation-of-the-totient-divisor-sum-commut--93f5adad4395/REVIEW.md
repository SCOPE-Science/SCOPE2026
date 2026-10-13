# Scientific review of the sign-oscillation theorem

## Correctness — PASS
The identity \(C(2^{k-1})=(2^k-2)/2-\varphi(2^k-1)\) holds for every \(k\ge2\), including \(k=2\). For odd prime \(k\), each prime factor of \(2^k-1\) is \(1\bmod 2k\); fewer than \(k\) distinct prime factors can occur, forcing the totient ratio strictly above \(1/2\). For \(12\mid k\), divisibility by \(4095\) fixes a totient ratio below \(1/2\). Five exact composite-index checks, together with the prime-index theorem, establish the first positive case. The reproducible finite checker evaluates both compositions directly; the unrestricted result rests on a full proof, not enumeration.

## Originality — PASS
Golomb (1993), §§4, treated both signs over all integers and described a powers-of-two negative-sign construction under an infinitude assumption for Mersenne primes. Here every prime **index** works regardless of Mersenne primality, and the positive-sign family is also contained in powers of two. De Koninck–Luca (2007) provides general extreme-order and density results but does not restrict to this geometric subsequence. OEIS A065395 and A116083 define the commutator and an exact difference-one subproblem, not the two index-class theorem. Searches of the published published-finding corpus corpus for aliases, the Mersenne-totient inequalities, and the first sign change found no equivalent or dominating statement. These searches cannot exclude unindexed elementary prior observations.

## Value — PASS
The old unrestricted sign theorem and global density results do not determine behavior on a zero-density subsequence. This result establishes sign oscillation on that subsequence with explicit infinite sets of exponent indices and an exact first positive boundary, replacing a conditional Mersenne-prime route to the negative sign by an unconditional statement. The problem and subfamilies are defined intrinsically rather than by an arbitrary finite search.

## Scientific boundaries
The theorem does not classify all composite exponent indices, infer the distribution of signs over unrestricted integers, or address infinitely many Mersenne primes. Direct source comparison still leaves some risk of earlier unindexed work.

Self-review: passed. Independent audit: not yet performed.
