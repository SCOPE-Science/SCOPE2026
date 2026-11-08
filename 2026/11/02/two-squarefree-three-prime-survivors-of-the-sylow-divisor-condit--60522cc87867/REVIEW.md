# Independent mathematical audit

## correctness

PASS

Let primes p<q<r. At r only pq can witness, so pq-1=kr with 1<=k<=p-1. At q, witness r would force q|k+1 while 2<=k+1<=p<q, so pr must witness and q|k+p; bounds p<k+p<2q force q=p+k. Mod p, qr=-1, q=1 mod p would give k=1 with q=p+1 composite for odd p; qr cannot witness for odd p, so r=1 mod p and k=p-1, yielding q=2p-1 and r=2p+1. If p>3 one candidate multiple of 3 and >3. Thus p=3 gives 3,5,7; p=2 gives k=1, 2,3,5. Explicit witnesses 30: (3,10,6), 105:(7,21,15). For one or two primes a witness for largest prime is too small. Independent direct divisor-condition enumeration over all triples of the first 46 primes (15180 cases) reproduced exactly the two; this finite check is not the global proof.

## originality

PASS

The two numbers 30 and 105 are recorded in OEIS A352287 and not their discovery. Eric Li 2026 proves asymptotic enumeration for all Sylow-condition integers, and the complete accessible mathematical source text of that paper was examined for a three-prime squarefree stratum, finding no such classification. Classical exclusion of simple groups of order pqr does not settle the arithmetic predicate (both 30 and 105 survive its numerical test). This is best-of-knowledge original as the complete infinite three-prime stratum, not the predicate itself.

## value

PASS

Classification of the first nonempty squarefree support layer of an established Erdős/Sylow divisor problem. Pinpoints exactly which squarefree pqr integers survive the necessary Sylow congruence test and require stronger group-theoretic obstructions. Although short elementary congruence chase, its unbounded complete boundary distinguishes it from arbitrary small casework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
