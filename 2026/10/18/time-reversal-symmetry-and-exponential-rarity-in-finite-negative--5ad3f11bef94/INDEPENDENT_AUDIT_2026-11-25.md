# Independent mathematical audit

## correctness

PASS

On the fixed (n+1)-element algebra the Esakia dual has n points. The finite form of the published representation uses closed fibers (automatic), convex rows, and four upset-preserving tests in both row and column directions. Taking the empty and full input upsets makes each of the two complementary sets of empty and nonempty rows an upset; hence a nonempty relation has no empty row, and likewise no empty column. The tests against thresholds {t,…,n−1} are exactly that the minimum and maximum fiber entries are each nonincreasing. With such row endpoints, a column is a prefix (by its upper-endpoint condition) intersected with a suffix (by its lower-endpoint condition); if nonempty, its endpoints are also nonincreasing as the column index increases. Having no empty column is equivalent to the two extreme endpoints and the no-gap inequality ℓ_i≤u_(i+1)+1. Transpose swaps the two row/column pairs of operators; dual uniqueness on the fixed ordered chain gives the symmetry equivalence. If a missing cell lies below the row minimum, the minimum cell is present and its transpose provides an upper endpoint bound showing the transposed missing cell cannot be above its row maximum. Reversing the inequalities proves the corresponding property above the row maximum. Thus the two missing corners separately have transpose symmetry. The n possible odd distinct diagonal hook lengths give 2^n choices for either symmetric corner, hence Q_n≤1+4^n. Independently placing the endpoints on opposite sides of the antidiagonal yields two Catalan staircase choices and enforces the adjacent no-gap condition. This proves T_n≥1+C_n², also at n=1, and Stirling gives the stated O(n³/4^n) ratio. A fresh program counts symmetric shape pairs and counts all upper boundaries after fixing each lower boundary, reproducing all given counts through n=8; a binary-matrix sweep through n=4 independently cross-checked those counts.

## originality

PASS

Passes for the transpose-fixed corner criterion and exponential proportion bound, not for the published duality, the general endpoint model, or the numerical sequence. A distinct indexed inverse-fiber result gives exactly the same general endpoint classification. OEIS A026641 matches the nonempty time-symmetric counts in the tested range, not Q_n without the +1; an all-n equivalence was not established by the inspected sources.

## value

PASS

For a natural involution of a fixed finite operator class, the result both gives an explicit combinatorial description of its fixed subfamily and proves that time reversal is exponentially atypical. This is a qualitative asymptotic statement not supplied by the endpoint census alone, with an explanation via independence of the two unconstrained staircase choices versus the constraints on two self-conjugate boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
