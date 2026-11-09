# Independent mathematical audit

## correctness

PASS

The overlining multiplicity is exactly 2^d for an ordinary support partition with d distinct sizes. Since m_odd-1 is even, d>=3 vanishes modulo 16. The single 1^n support contributes 4, the two-support {1,3} contribution is 0 mod 16, and other {1,m} contribute 8. Counting a+b*m=n reduces to sum floor((n-1)/m) and divisor parity reduces that sum to squares. For pbar modulo 8, Jacobi triple product gives P^-1=1+2 sum (-1)^k q^(k^2), so P=1-2S+4S^2 mod 8; in characteristic 2 S^2 has exponents 2k^2. Boundary n=1 and disjoint square/twice-square cases check. Independent ordinary-partition enumeration n<=21 passed both congruences.

## originality

PASS

The special odd support convention is mathematically different from the odd mex defined through nonoverlined parts in closely related literature; n=1 gives F(1)=6 mod4=2, whereas Veena-Fathima abstract gives its odd mex sum 0 mod4 at n=1. Its inaccessible full text is a material residual priority risk, but inspected sources do not imply the support-dependent mod-16 correction or complete mod-8 spectrum. The elementary input identities are old; the specific exact arithmetic statement remains a qualified best-of-knowledge novelty.

## value

PASS

Odd minimal excludant on complete support of an overpartition is an intrinsic, convention-sensitive partition statistic. Determining its full infinite modulo-8 spectrum, two-valued modulo-16 correction, and exact natural-density frequencies is a meaningful exact arithmetic classification not merely a finite table. It directly disambiguates conflicting mex conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
