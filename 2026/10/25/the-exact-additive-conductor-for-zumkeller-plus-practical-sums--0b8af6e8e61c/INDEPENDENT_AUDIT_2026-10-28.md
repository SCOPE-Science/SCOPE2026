# Independent mathematical audit

## correctness

PASS

The 945 divisor witness has half divisor sum 960 and gcd(945,1+105t)=1, giving the infinite progression 945+99225t of Zumkeller numbers. A complete practical representative in each residue modulo 99225 with max 41235272 implies every n>=41236217 is in the sumset. The finite bridge 19069<=n<41236217 is explicitly certified by a whole-bitset convolution of 1989 odd Zumkeller witnesses with even practical numbers, plus the separate 20177=20176+1 case and the previously proved even-number coverage. Independent exact Python divisor-subset and practical tests recomputed 720 exceptions, last gap 19067 and the 38 odd Zumkeller integers below 19068. Crucially, a separately written C++ implementation independently performed the full 42,000,000-number practical sieve: it found all 99,225 residue classes, the exact maximum first representative 41,235,272 in residue 56,897, independently enumerated exactly 1,989 odd Zumkeller integers through one million, and checked the entire odd finite bridge: exactly one apparent gap at 20,177, itself covered by 20,176+1; the independent divisor test confirmed 20,176 is Zumkeller. This complete finite computation, rather than a saved log, supports the finite part; the arithmetic progression/residue argument proves the infinite tail.

## originality

PASS

Somu–Kukla–Tran prove qualitative eventual representation by Z+P and separately an exact maximal gap for Z+Z; neither statement gives the Z+P conductor or its 720-exception list. Our exact conductor is a meaningful quantitative specialization of the established qualitative theorem, not a claim to discover eventual additive coverage.

## value

PASS

The least eventual-additive threshold for a natural divisor-structural sumset answers the finite obstruction problem left by a published cofinite-sum theorem. The 19067 sharp witness and full exception census can be reused as exact boundary data rather than merely repackaging a density bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
