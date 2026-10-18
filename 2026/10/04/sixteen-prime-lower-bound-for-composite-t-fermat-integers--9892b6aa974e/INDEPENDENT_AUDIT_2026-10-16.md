# Independent mathematical audit

## correctness

PASS

PASS subject to the actual published structural lemmas. The source proves a composite T-Fermat n is an odd squarefree Carmichael number, p<d(n)=2^M for every p|n, ν₂(p−1) equal over p, and all mutual ord_{p−1}(q) odd. Therefore its M distinct prime divisors form an M-clique in the explicit FINITE graph of primes <2^M at common ν₂. Independently rebuilt graph without using the supplied order algorithm: odd order iff gcd(q,p−1)=1 and q^{oddpart(phi(p−1))}=1 mod(p−1). Reproduced all per-M vertex/edge data, no M-cliques for 3≤M≤14, exactly one 15-clique (331,631,751,991,2311,4951,7351,11251,11551,14851,17011,25411,26251,28351,30871), whose product N fails Korselt at (N−1) mod 330=90. M≤2 excluded for composite Carmichael. This is exhaustive finite exclusion due p<2^M, not an inference from sampling or a claim for M≥16.

## originality

PASS

PASS (best of knowledge). The full Hakobyan primary paper establishes pairwise prime restrictions and finite boundedness for each number of factors but does not give the explicit 16 factor cutoff in inspected theorems. The 2024 competition “almost prime” formulation uses same polynomial predicate but does not provide this compatibility-graph census in checked context. Distinct Deaconescu/Carmichael prime-factor lower bounds have different predicates and do not imply the T-Fermat bound. Residual risk is an unindexed stronger lower bound or publication after arXiv version.

## value

PASS

PASS. An explicit ≥16 prime obstruction for hypothetical composite T-Fermat integers is a natural arithmetic size invariant: it transforms structural theorems to a sharp-for-tested-range exact finite restriction rather than a routine tiny check. The 15-clique obstruction is a nontrivial reproducible finite certificate with a Korselt exclusion. It is not a proof composite examples exist or a complete classification for M≥16.

The dated certificate retains the supplied scientific assessment, sources and limitations.
