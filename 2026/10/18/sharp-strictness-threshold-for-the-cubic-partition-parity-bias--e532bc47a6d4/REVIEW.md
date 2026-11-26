# Independent mathematical audit

## correctness

PASS

The parity-adjusted signed unrestricted generating function is the product of (1+(-q)^(m^3))^(-1). On the factor family m=2^a u for a fixed positive odd u, the a=0 term is (1-z)^(-1) with z=q^(u^3), and the a>=1 terms divide out factors 1+z^(2^(3a)) from its binary product. Coefficientwise this cancellation is legal, and the surviving subset weights are distinct by their 2-adic valuations and odd cube roots. An independently written exact convolution of the signed multiplicity sums through degree 373 and a separate direct enumeration of the 1,024 subsets of the ten base weights (`python3 /workspace/branches/independent_checks.py 1`) produced all 23 listed zeros, no other zeros through 373, and verified every base sum from 124 through 373 (not 374 for those base weights). The certified interval adjoins its translate by 250, reaching 623, and overlaps its translate by the fresh weight 343, reaching 966. At that point 729<=966-123; each following overlap margin increases by 2v^3-(v+2)^3, positive for v>=9 since (1+2/v)^3<2. Each added odd cube is a fresh weight, and the accumulating right endpoints diverge. This gives every n>=124 without extrapolation. The empty partition is counted, and 123 is an actual zero, so the boundary is sharp.

## originality

PASS

Credit the signed product, sign pattern with possible equality and eventual strictness to earlier work. The novelty supported by the comparison is the exact all-n cubic zero classification and optimal effective threshold. Ciolan's printed strict statements cannot be a correct all-n comparator in the presence of explicit cubic zeros and the paper's own equality caveat. A finite coefficient table supplies existing individual zeros where it lists them, not an infinite tail proof.

## value

PASS

This is a sharp effective answer to a standard partition-parity question for a natural exponent, and it identifies the finite equalities that strict phrasing in the original literature misses. The value is not enumerating another table: the small interval is a succinct certificate that closes the infinite gap left by qualitative eventual positivity. The result gives the precise range in which strictness may be used without further caveats; it does not claim novelty for the known generating function or asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
