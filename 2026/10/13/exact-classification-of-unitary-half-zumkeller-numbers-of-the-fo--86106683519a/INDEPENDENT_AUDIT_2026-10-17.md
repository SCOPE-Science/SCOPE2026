# Independent mathematical audit

## correctness

PASS

For n=4pq (p<q distinct odd primes), proper unitary divisors are exactly {1,4,p,q,4p,4q,pq}. Nonempty equal-sum partition exists iff signed sum=0; normalize sign of pq positive. Each independent sign pair gives an element of S={-5,-3,3,5}, reducing to q(p+u)=-(vp+w). For p>=11, p+u>=p-5>0 and q<=5(p+1)/(p-5)<p, contradiction; inequality p^2-10p-5>0 already holds at 11 and increases. Exhaustively evaluating all 64 (u,v,w) for p=3,5,7 gave candidate q sets respectively {5,6,7,9,10}, {6,9,10,11,14,15}, {8,9,10,12,13,15,16,19,20}; zero-denominator cases have no identities. Prime q leave (3,5),(3,7),(5,11),(7,13),(7,19), and explicitly checking both partition sums for 60,84,220,364,532 proves existence. Complete symbolic exclusion handles every larger prime and finite enumeration handles the residual set, not a bounded-only scan.

## originality

PASS

Das (2024) defines the unitary half-Zumkeller property and proves the subset-sum criterion and a two-prime-support theorem, with 60,84 known examples. OEIS A290467 already records all five numerical values; mere membership or listing of these numbers is not new. A published classification of even unitary *Zumkeller* numbers with three-prime support concerns a different property and does not imply this half-subset classification. The exact necessary-and-sufficient theorem for n=4pq and exclusion of all other primes is not found in inspected prior materials.

## value

PASS

This is the complete first three-prime-support dyadic-exponent-two slice where unitary differs from ordinary divisor partitions. The finite five-pair classification resolves a natural elementary number-theoretic divisibility/partition question; it proves global absence outside a short OEIS-visible list, which table membership alone cannot give. The prime-support and dyadic conditions are mathematically motivated, not arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
