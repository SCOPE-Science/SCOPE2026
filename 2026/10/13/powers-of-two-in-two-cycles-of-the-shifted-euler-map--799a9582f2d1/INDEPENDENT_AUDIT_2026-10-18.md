# Independent mathematical audit

## correctness

PASS

A two-cycle 2^a<->y gives y+phi(y)=3*2^(a-1) on eliminating k. For odd y>1, parity of y+phi(y) excludes it (y=1 checked separately). Writing y=2^c m with c>=1 and m odd gives 2m+phi(m)=3*2^(a-c). If m>1 and v2(phi(m))>=2, LHS has valuation 1 but exceeds RHS 6; hence v2(phi(m))=1, forcing m=p^e for a single p=3 mod4. Then p^(e-1)(3p-1)=3*2^(a-c) and gcd(p,3p-1)=1 force p=3,e=2,a-c=3. Thus y=2^a or y=9*2^(a-3) (a>=4), with unique k=5*2^(a-3); direct totients verify converse. The otherwise omitted boundary x=2^0=1 is excluded directly: a nontrivial F_k(1)=y, F_k(y)=1 would force phi(y)+k=1, hence k=0, but F_0(1)=1. Independent exhaustive equation checks for all a=1..16 and the cycles agree; infinite result is from valuations, not enumeration.

## originality

PASS

Leonetti–Luca prove eventual periodicity and ask for sharper cycle structure, but not the exact prescribed-power-of-two period-two classification. The prior published Resultary extremal period-size theorem bounds maxima and characterizes a prime-progressions equality configuration; it neither forces nor excludes a two-cycle with prescribed 2^a and cannot supply k=5*2^(a-3). An explicit same-map and equation search found no covering all-a classification. Originality is best of knowledge with specific Diophantine-equation risk.

## value

PASS

Powers of two provide a canonical infinite test family for totient dynamics. The theorem resolves the exact period-two membership boundary for all exponents and gives unique parameters and partners, with an infinite explicit 2-cycle construction; this is a meaningful structural slice of the source’s periodicity problem rather than a small empirical catalogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
