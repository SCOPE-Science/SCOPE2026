# Independent mathematical audit

## correctness

PASS

For odd B, multiplicativity forces each beta(p^e) to be a power of two. Even e gives an odd integer greater than one. For odd e=2t+1 the geometric factor in beta(p^e) has 2-adic valuation v2(t+1), by repeatedly halving its geometric length and using p^2=1 mod 8. If t>0 the factor exceeds t+1, so it is not a power of two. Thus B is a squarefree product of Fermat primes, with the indices forced by the set bits of a-1. For even a>=4, beta(2^a) is 11 mod 16 while the prescribed product is 3 or 15. For odd a>1, at the first omitted index j below the top digit, beta(2^a) is -1/3 modulo 2^(2^j+1); the forced product is the prefix without F_j, which differs from -1/3 by an odd multiple of 2^(2^j). This forces a=2^k-1. The product then is F_1 through F_(k-1); pairwise coprimality and composite F_5 exclude every k>=6, irrespective of later Fermat primes. Independently checked primality by trial division of each F_0 through F_4 up to its square root, the exact factorization F_5=641*6700417, and the two iterates for all asserted exponents, including 31. The frozen finite script, inspected but not executed, is corroboration rather than the exclusion proof.

## originality

PASS

The six examples and the theorem restricted to a=2^k-1 are prior. The distinct contribution supported by the inspected sources is the unrestricted converse for powers of two. A later-dated catalogue record explicitly subsumes it; this overlap is credited, without making a publication-priority claim from catalogue dates alone.

## value

PASS

The powers-of-two subfamily is the natural home of all the known examples. Excluding every other exponent is an exact infinite classification that is useful independently of the open general problem. The first-missing-bit obstruction explains why the known Fermat-prefix construction is forced, rather than simply extending a numerical search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
