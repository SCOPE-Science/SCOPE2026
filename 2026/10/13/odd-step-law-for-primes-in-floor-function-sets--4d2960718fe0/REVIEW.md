# Independent mathematical audit

## correctness

PASS

For D_p(N)=floor(N/p)-floor(N/(p+1)), membership of p in the floor set is D_p>0 and D_p(N)-D_p(N-1)=1_{p|N}-1_{p+1|N}. Primes <=sqrt(N-1) persist by interval length; for p>=sqrt N D_p values are 0/1. At odd N>=5 the latter p is odd so p+1 cannot divide N. Hence exactly one new prime iff P+(N)>=sqrt N; at odd squares p=sqrt N is counted correctly. Direct independent prime-sieve window computation verified 24998 odd integers 5..49999.

## originality

PASS

Heyman (2021/22) explicitly conjectures the three-distinct-prime case and proves only prime/odd-semiprime cases. This proof establishes the stronger all-odd exact step law. Ma–Wu asymptotic prime counts and OEIS cardinality formulas do not imply exact increments.

## value

PASS

Resolves a specifically posed three-prime conjecture, with a natural sharp generalization in terms of largest prime factor for all odd arguments; distinguishes behavior from even steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
