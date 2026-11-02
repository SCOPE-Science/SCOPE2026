# Independent mathematical audit

## correctness

PASS

For r>=2 cyclic binary words with r ones, gaps of one or two zeros, no cyclically adjacent short gaps and at least one double gap, the comparison words (01)^r and 0(10)^r establish r-universality and minimum missing subsequence length r+1. At each of D second-zero cuts, precisely 1^(r+1) is absent. The r first-zero cuts always lack 1^(r+1) and 1^r0 and have one additional absence iff the final internal zero gap is short. Earlier candidate absences cannot occur because any consecutive pair of zero gaps has at least one double gap. Reversal bijects the r cuts at ones with first-zero cuts and preserves absent counts. This yields exact marked-cut frequencies 1:D, 2:2D, 3:2S. Independent full direct subsequence membership checked 72 legal gap tuples and 1122 rotations for 2<=r<=7 and all binary patterns of lengths r and r+1. The proof, not finite checks, establishes all r.

## originality

PASS

General arch-factorization theory identifies shortest absent subsequences and universality index; circular universality and 2024 extremal cardinality bounds are prior results. The new precise claim is a rotation-by-rotation three-value histogram tied to D and S on a constrained family, not a new algorithm or general arch characterization. Main results in the inspected Kosche, Barker and Adamson texts address individual-string SAS characterizations, circular universality, and extremal counts, respectively; the specific marked-cut distribution is not directly stated or implied by an inspected general formula. Equivalent consequences of deeper word-combinatorics classifications are a residual risk.

## value

PASS

A sharp, all-length, three-point distribution of shortest absent scattered-subsequence cardinalities over every marked rotation is a natural exact refinement of circular subsequence universality. The answer depends only on gap statistics, not ordering, and fails outside a sharp no-neighboring-short-gap condition. This is an interpretable structural classification beyond generic shortest-absence algorithms, even though confined to a special family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
