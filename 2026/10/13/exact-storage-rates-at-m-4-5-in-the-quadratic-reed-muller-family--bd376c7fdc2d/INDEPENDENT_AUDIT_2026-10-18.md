# Independent mathematical audit

## correctness

PASS

Every rank≤1 symmetric matrix over F2 is xx^T for exactly one binary x, because its diagonal recovers x. Thus rows of M_m are indicators of translates of the complete 2^m support inside F2^D, D=m(m+1)/2, including x=0. A fresh independently written compiled C++ bit-Gaussian elimination reconstructed all 1024 rows for m=4 and all 32768 rows for m=5, using exact xor pivots; counted pivots respectively 448 and 13658. Also reproduced complete m=1..5 rank sequence 1,4,28,448,13658. Exhaustion is finite and complete for exactly these m, not a statistical sample. Computed rates/nullities and bicycle dims by cited identities; no general m recurrence claimed.

## originality

PASS

Zabokritskiy defines the same matrix and asks open rank asymptotics, providing only bounds, while Barg-Zemor leave the quadratic Reed-Muller rates open (their numeric table is different BCH family). Schmidt gives characteristic-zero association-scheme eigenvalues, which do not determine rank modulo 2. Resultary semantic and exact-value searches found no binary rank table at these two cutoff parameters; best-of-knowledge PASS with priority risk.

## value

PASS

These are first two instances m>=4 in the originally open and mathematically motivated storage-code parameter range; exact finite ranks give new calibrating benchmarks and a concrete meaningful cutoff, with no need to solve asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
