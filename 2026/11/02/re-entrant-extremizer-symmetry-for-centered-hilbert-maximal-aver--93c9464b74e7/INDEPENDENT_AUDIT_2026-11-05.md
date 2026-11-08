# Independent mathematical audit

## correctness

PASS

The nonlinear graph-ball maximal operator satisfies ||M_n x||_2²=max_rho ||A_rho |x|||_2². Since each A_rho^T A_rho has nonnegative entries, its top Rayleigh vector may be chosen nonnegative; taking max over the finite selections commutes with max over x, giving the exact spectral reduction. The total legal-radius profiles are respectively 18, 1200, 176400 for n=3,5,7. Independent Python exact integer fraction-free Sylvester elimination reconstructed all such profiles and found only (1,0,1), the reversed pair (1,0,1,2,3)/(3,2,1,0,1), and (3,2,1,0,1,2,3) above the rational separating thresholds 199/125, 823/500, 3387/2000. For these exceptions the given Gram characteristic-polynomial factorization and exact Rayleigh witnesses locate a unique top root above the threshold (trace <2T). The exact eigenvector ratios satisfy the displayed equations; nonnegative irreducible Gram matrices have unique Perron top vectors, and strict active-ball comparisons rule out other rays. The 3-vertex base is known, whereas P5 has two nonsymmetric reversed extremizers and P7 one symmetric centered extremizer. Finite enumeration is exhaustive over the explicit finite set, not an extrapolation to all odd paths.

## originality

PASS

Strong centered l2 maximal norms for complete/star graphs are known from González-Riquelme–Madrid 2020; P3 is a star and explicitly credited. Soria–Tradacete 2014 gives graph maximal constants and path weak-type behavior, not these two nonstar P5/P7 exact strong Hilbert norms. González-Riquelme–Kovač–Madrid 2026 concerns edge p-variation rather than l2 operator norm. A prior computational table covering small path orders cannot be ruled out, but no compared full theorem implies the exact P5/P7 algebraic constants together with extremizer symmetry switching.

## value

PASS

For natural unweighted centered graph maximal averaging, exact sharp p=2 operator norms and equality cases beyond stars are nontrivial global optimizations, not textbook local averaging. Exhaustive exact finite classification on the first nonstar odd paths reveals a rigorous symmetry break and restoration; it provides boundary-case benchmarks and points to nonmonotone extremizer structure without claiming an eventual law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
