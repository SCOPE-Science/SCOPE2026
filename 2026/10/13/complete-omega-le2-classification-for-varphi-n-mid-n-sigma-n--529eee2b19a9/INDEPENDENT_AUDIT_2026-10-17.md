# Independent mathematical audit

## correctness

PASS

For n prime, φ(p)|pσ(p) reduces p−1|2, giving p=2 or 3. For p² it reduces p−1|3, giving p=2 and n=4. For pq with p=2, q−1|12 yields q=3,5,7,13. For odd p<q, P=(p−1)/2 and Q=(q−1)/2; coprimality forces P|Q+1, Q|p(P+1). Writing Q+1=kP and Q|(k+1)(k+2), define h=(k+1)(k+2)/Q and t=(h+2)/k to obtain (kt−2)P=k+t+3. For P=1, (k−1)(t−1)=6 yields q=5,7,13; P>=2 implies 2kt−k−t<=7 with the listed finite possibilities, yielding remaining four prime pairs. Every implication is reversible via gcd(P,Q)=1; all fourteen numbers pass direct substitution. Independently exact computation over all n<=100000 with Ω(n)<=2 found precisely the listed 14, corroborating but not replacing the finite symbolic sieve.

## originality

PASS

OEIS A066994 describes precisely φ(n)|nσ(n) and lists early terms but gives no low-multiplicity classification or proof. Broughan–Zhou 2014 proves classification of φ(n)|σ(n) for few prime factors; that is strictly stronger condition and does not entail solutions made possible by multiplying by n, such as 26,39,155,203. The exact bound from (kt−2)P=k+t+3 is a new structural deduction relative to these checked sources; unindexed elementary notes remain a plausible originality risk.

## value

PASS

A complete finite characterization of the two-prime-factor edge of the naturally defined OEIS divisibility sequence supplies a clean first nontrivial structural layer. Beyond re-listing known terms, the prime-support restriction and bounded k,t parametrization prove no further solutions at arbitrarily large n, a fact finite sequence tables alone cannot establish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
