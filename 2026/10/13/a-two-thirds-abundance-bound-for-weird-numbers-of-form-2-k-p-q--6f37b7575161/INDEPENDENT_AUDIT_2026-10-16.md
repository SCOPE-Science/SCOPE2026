# Independent mathematical audit

## correctness

PASS

For k>=1, p<q distinct odd primes, M=2^(k+1)-1, x=p-M even, a=sigma(2^k p q)-2^(k+1)pq=M(M+1)-x(q-M). Iannucci gives M<a and M<p<2M. If a=r+sp+tq with 0<=r,s,t<=M then the binary proper-divisor blocks form a subset of proper divisors summing to a and hence a complement representing n, contradicting weirdness. First lemma: if q<=2M, write q=p+d even d and split M(d+1) by p. Quotient u obeys d/2<=u<=d, and the replacement of T copies p by q adjusts remainder to [0,M], giving a forbidden representation; hence q>2M. Second lemma: x residues (a-tq) mod p for t=0..x-1 must avoid [0,M], but at most x-1 residue classes lie outside, whenever a>=(x-1)q; contradiction; hence a<(x-1)q. If x>=M/3, q>2M yields a<(2/3)M^2+M; if x<M/3, the residue lemma gives q>M(p+1)/(2x-1) and a<.5 M(M+x+1)<(2/3)M^2+M. All inequalities strict. Independent exact finite no-representation classification matches first six weird-number counts 1,1,5,3,10,23; bounded test is corroboration only.

## originality

PASS

Iannucci proves the starting criteria and conjectures a much stronger one-third-scale bound; the closest published Resultary theorem establishes only the weaker three-quarter coefficient. This work is not merely a parameter renaming: q>2M and stronger residue packing are used to cross the two-thirds threshold. The prime-gap/intermediate statements and Iannucci base identity are not claimed as novel.

## value

PASS

A uniform improvement from 3/4 to 2/3 of the quadratic abundance coefficient across every exponent and prime pair closes a positive portion of the gap to a longstanding explicit one-third-scale conjecture. The proof supplies nontrivial exclusion and residue-packing lemmas; the quantitative gain is mathematically motivated, not an arbitrary small finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
