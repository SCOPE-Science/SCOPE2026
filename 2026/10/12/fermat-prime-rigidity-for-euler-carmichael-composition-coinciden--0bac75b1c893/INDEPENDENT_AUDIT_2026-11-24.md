# Independent mathematical audit

## correctness

PASS

For p−1=2^t u with u odd, write c(j)=v₂(λ(2^j)), T=max(t,c(a)), S=a+t−1 and λ(u)=2^h K with K odd. The first iterates have the common odd part p^(b−1)u; p divides neither u nor λ(u) since λ(u)≤u<p. Thus the composed numerator is 2^L p^(b−2)uφ(u), L=T+t−1, and the denominator is 2^E p^(b−2)lcm(u,K), E=max(t,c(S),h). Cancellation works also at b=2. The lcm divides uφ(u). For u>1 its quotient into uφ(u) has valuation f=v₂(φ(u))≥1; h≤f and c(S)≤L (for a≤2 use c(S)≤S−1, for a≥3 use c(S)=a+t−3). Therefore L+f−E≥min(L,f)≥1. For u=1 the exponent is t−1 at a=1,2 and max(0,t−(a−2)) at a≥3. This proves the integer quotient, b-independence, parity obstruction and exact equality classification, including p=3 and the first qualifying a. The frozen verifier was inspected, not executed: lines 88–102 compare both compositions directly in the finite sweep, whereas the extra threshold assertions at lines 103–106 evaluate formula() only (the sweep itself reaches the 257 threshold). The proof does not depend on the script.

## originality

PASS

The exact local quotient and unbounded equality classification survive the statement-level comparisons. The best matches treat the same equation globally or enumerate bounded examples, or use Fermat primes in different equations; no inspected source supplies or implies the full local parity obstruction and threshold. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

The two-prime-power family isolates the 2-adic contribution to a studied composition equation while allowing arbitrarily large exponents on both primes. The result gives an exact obstruction for all odd parts u>1 and a least qualifying 2-adic exponent otherwise, connecting a natural arithmetic coincidence to Fermat primes. This is useful beyond reproducing finite entries or merely exhibiting another sufficient construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
