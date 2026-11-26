# Independent mathematical audit

## correctness

PASS

For n≥8 the full four-subset kernel has the Newton expansion of s↦q^((4−s)²) at s=0 into the PSD matrices M_j M_jᵀ, with the degree-four term F(q)I. The first four coefficients are positive for 0<q≤1/3; F changes sign between 1/4 and 1/3 and is decreasing up through 13/25 by the displayed derivative bound. At the root, the lower incidence column spaces nest in that of M₃, so rank reduces to rank M₃. The column-independence induction works because the exchange of x,y passes from (t,k,n) to (t−1,k−1,n−2) within t≤k≤n−t, forcing adjacent t-set coefficients equal and hence zero. On eight points the degree-four and degree-three pair differences are eigenvectors by flips and unpaired-coordinate symmetry. Counting flips gives F and G=1−2q+2q⁹−q¹⁶, respectively; G=(1−q)(1−q⁸)(1−sum_{i=1}^7 q^i), which is negative on [13/25,1) by even the first four terms of the sum. Thus between the first root and 13/25 the degree-four form is negative, and beyond it up to 1 the degree-three form is negative. The eight-point matrices are principal submatrices at every n≥8, and unit diagonal ensures a positive direction. The all-ones endpoint is separate. At 19/20 a bounded numerical check gives F≈0.00616653 and G≈−0.07962785, consistent with the rational signs; for general n the degree-three eigenvalue counts one choice preserving the unpaired point and n−7 choices adding one unit to the distance, hence equals F+(n−6)γ₃ and is negative there as well. Replay: RESULT.md lines 28–83; VERIFICATION.md and check.py were inspected, not run. The result uses d² for shortest-path d, not squared Euclidean distance of indicators.

## originality

PASS

The exact all-n first-loss polynomial, cutoff rank, and incidence method overlap substantially with the broader published Resultary frontier. Those parts cannot be treated as distinct from that catalogue result. The distinct contribution supported here is the full four-subset classification beyond the first frontier, proving no additional admissible interval all the way to the isolated all-ones endpoint despite top-sector reentry. The broader frontier explicitly leaves the relevant high-q region unclassified. Catalogue dates do not decide priority.

## value

PASS

A radial kernel usable on every ground-set size has an explicit, size-independent admissible set and an exact rank at loss of strict positivity. The same finite obstruction excludes every high-q interval; the top harmonic's sign reversal shows why recording only the first transition is insufficient in this natural distance family. This is a full classification rather than a numerical bandwidth or one small matrix computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
