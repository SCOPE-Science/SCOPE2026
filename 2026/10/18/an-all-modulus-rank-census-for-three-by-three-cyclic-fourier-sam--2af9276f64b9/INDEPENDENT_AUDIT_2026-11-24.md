# Independent mathematical audit

## correctness

PASS

Dephasing any unimodular 3×3 matrix puts ones in the first row and column, with last square a,b;c,d. The zero-determinant equation is (a-1)(d-1)=(b-1)(c-1). If its product is zero, the chosen two factors equal to zero force an equal row or column in each of the four cases. Otherwise conjugation, using conj(z-1)=-(z-1)/z, gives ad=bc; expansion gives a+d=b+c, hence equality of the unordered pairs {a,d} and {b,c}. This again forces a proportional pair. For Fourier entries, a restricted row ratio is constant iff all its exponent differences vanish modulo N, equivalent by Bezout to N dividing (r-r')g_C; applying this to every row pair yields N|g_Rg_C. The equations for rank three and the residual rank two follow since all entries are nonzero. The term A_N(e,d) counts a chosen mod-e class, three distinct compatible mod-d classes, and one representative in each; their intersection sizes are N/lcm(e,d). Inverting e|g_R gives the exact strata T_N, so the two independent choices really multiply, with neither an ordering nor a stabilizer factor on an individual triple. For rank-one existence, N/g_R and N/g_C must each be at least three and have product dividing N; the stated progressions realize those gcds. The proof applies to all N≥3 over C and does not require squarefreeness or R=C.

## originality

PASS

Exact earlier finite and restricted-modulus overlaps and a later materially equivalent full census are verified. The latter has a later catalogue path, not evidence of earlier priority. On the evidence checked, the distinct contribution at the frozen record is the unrestricted cyclic-modulus census with an explicit per-pair criterion and divisor-stratum counts. None of the identified earlier principal, Hadamard or restricted-modulus results provides that full coverage.

## value

PASS

A complete rank census is a natural invariant of the cyclic Fourier sampling family, for which principal-minor or prime-specific facts are insufficient. The dephasing rigidity and gcd strata turn complex determinant enumeration into a reusable local decision test and exact divisor-only evaluation, including a sharp criterion for the existence of rank one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
