# Independent mathematical audit

## correctness

PASS

The left side is odd so y odd. If k even and an>=3 it is 7 modulo 8 whereas odd even powers are 1 mod8; remaining (a,n)=(1,1),(2,1),(1,2) give 1,3,7. If k>=3 odd, the cofactor T=(y^k+1)/(y+1) is odd and divides n, forcing T<=n; T>3*y^(k-1)/4 for odd y>=3 implies y^k<(4n/3)^(3/2). Cases n=1,2 contradict T>1 and T|n; for n>=3, n2^(an)-1>n2^(n-1)>=(4n/3)^(3/2), contradiction. Monotonic inequality at n=3, then growth ratio >1, proves all bounds.

## originality

PASS

No prior mathematical result located implying the all-parameter family-specific theorem; best-of-knowledge, with residual indexed/access limitations.

## value

PASS

Perfect powers in Woodall and generalized prime-search families are a natural exponential Diophantine predicate. The clean uniform all-a,n exclusion explains why odd factors of a potential perfect power have nowhere to reside for dyadic bases; substantially more than an isolated residue check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
