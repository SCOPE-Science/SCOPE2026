# Independent mathematical audit

## correctness

PASS

For p prime and p<B<=p^2 write p^2=aB+b (1<=a<p, 0<=b<B). If the prime quotient p^2/(a+b) is prime it must equal p, so a+b=p and p(p-1)=a(B-1). Coprimality gcd(a,p)=1 forces a|p-1 and B=pd+1 for d=(p-1)/a; conversely every such d gives valid digits (a,b)=((p-1)/d,p-(p-1)/d) and quotient p. Therefore there are tau(p-1) Moran bases. For Harshad digit sum divides p^2, so it is 1,p or p^2; the last impossible by a(B-1)>0; sum1 forces (a,b)=(1,0), B=p^2, adding exactly one Harshad-only base. Bound p<B<=p^2 is strictly two digits. Exhaustive independent enumeration of all bases for primes 2..79 selected verified both exact sets; proof works every prime without finite extrapolation.

## originality

PASS

Witno's accessible complete 2010 original 'Numbers Which Factor as Their Digital Sum Times a Prime' develops DECIMAL Moran/Niven numbers. A 2012 arbitrary-radix Moran implementation and OEIS A001101 establish that the base-dependent notion is prior. The inspected primary full text and databases do not supply the complete variable-base, fixed-prime-square spectrum B=pd+1 and counts tau(p-1), tau(p-1)+1. This is best-of-knowledge; simple equivalent divisor arithmetic in unindexed recreational literature is a substantial residual risk.

## value

PASS

For a fixed integer n, counting the bases in which n is Harshad or Moran is a natural arithmetic invariant, rather than a slice selected only after seeing numerical data. Prime squares are the first composite class with a unique prime divisor; restricting to their two-digit representations makes the prime-quotient condition sharp while still ranging over an unbounded set of radices. The exact variable-base spectrum tau(p-1) and one additional Harshad base provide a complete non-tabular benchmark for future base-dependent digital-sum problems. Its short elementary proof and narrow scope limit, but do not erase, this independently usable exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
