# Independent mathematical audit

## correctness

PASS

For 2 beta(n)=n multiplicative beta(p^a)=(p^{a+1}+(-1)^a)/(p+1), n must be even. Under omega<=2 either n=2^a (only a=1) or 2^a p^b. The exact ratio beta(p^b)/p^b=3/(4+(-1)^a 2^{1-a})<=4/5 for a>=2 and >=(p-1)/p excludes p>=7. p=5 forces a=3,b=1, n=40. For p=3 even b the left valuation forces a=1 (excluded); odd b requires even a and yields 3^{b+1}=2^{a+1}+1, hence (3^{(b+1)/2}-1)(3^{(b+1)/2}+1)=2^{a+1}, forcing factors 2 and 4: a=2,b=1, n=12. n=2 also works, and n=252 shows omega=3 possible. Independent exact enumeration n<=100000 confirmed all support<=2 hits.

## originality

PASS

Best-of-knowledge PASS for an all-integers rigidity theorem. Iannucci, Zhou--Zhu, Toth, and OEIS have definitions, finite enumerations, and partial necessary conditions, but not the all-exponent two-prime exclusion in inspected relevant portions. An unindexed elementary argument remains possible.

## value

PASS

The least number of distinct prime factors beyond 2,12,40 is exactly three. This is a complete natural support layer of a classical imperfect-number analogue, with a sharp 252 boundary and an unbounded exponent proof. It is a useful structural constraint rather than just a known-prefix recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
