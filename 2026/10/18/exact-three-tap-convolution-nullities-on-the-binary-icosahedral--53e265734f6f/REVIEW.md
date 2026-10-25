# Independent mathematical audit

## correctness

PASS

Enumerate 120 matrices in SL(2,F5) and all 7021 unordered two-element normalized supports {1,x,y}. Simultaneous conjugation and reanchoring partitions them into precisely 62 nonoverlapping orbits, each left-translation invariant in rank. Integer regular-convolution matrices have exactly three unit entries in each row. For each orbit representative the four claimed independently primality-checked primes give coinciding modular ranks; product exceeds 3^60, the universal Hadamard bound on every 120x120 square minor. Hence any larger minor zero modulo all primes must vanish over Z, while a rank-size nonzero modular minor survives in characteristic zero. The 62 orbits yield 35 quotient-order triples and exactly {0:159240,4:38400,5:28800,10:28800,20:14400,22:7200,30:2400,40:1200,80:400} supports, 280840 total and 121600 singular. The 400 supports with 80-dimensional kernel are cosets of the ten order-3 subgroups (40 cosets each). Read complete check.cpp and its exact group, orbit, rank logic. An independently coded numba group algorithm exhaustively reproduced all 62 orbits, 35 signatures and four-prime ranks and histogram, not just an old log. The complete finite domain is proved by exhaustive exact certificate; no infinite-family claim.

## originality

PASS

PASS best-of-knowledge for SL(2,F5)'s complete 35-signature three-tap rank census and intrinsic order-signature rigidity. The published Cayley spectral factorization supplies a method but not these 62 orbit ranks; conjugacy-invariant normal-Cayley singularity results do not apply to arbitrary nonnormal supports. The A5 quotient and ternary-Heisenberg/dihedral three-tap results cannot determine faithful spinorial blocks of the double cover. Unindexed rank tables remain risk.

## value

PASS

The binary icosahedral group is the canonical nontrivial perfect central cover of A5, a natural group for finite noncommutative harmonic analysis. Exhaustively determining all unweighted 3-tap convolution kernels by intrinsic quotient orders, with a distinctive 22-nullity stratum and extremal cosets, supplies a reusable exact invariant in a natural nonabelian example; general group-wide theorem not required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
