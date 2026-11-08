# Independent mathematical audit

## correctness

PASS

PASS. Inspected exact channel definition, parent D_i(y)=y[:i+k]+y[i+2k:], and exact collision criterion D_i=D_j iff y_t=y_{t+k} for all i+k<=t<j+k. Two overlapping even palindromes at separation s impose period 2s in the overlap; s=1 forces constant overlap via central adjacency, and s>=2 with 2s|k forces the entire parent-comparison interval k-shift equal. Therefore distinct representative starts have spacing >=s_k in [0,m-2k], giving universal upper bound. For d=s_k the binary period-2d word with marked positions k-1,k has feasible palindrome starts every d; direct mismatch in the comparison interval between any consecutive distinguished starts makes all resulting parents pairwise distinct. Edge m=2k gives exactly one; k=1,2,3 give d=2, k=4 gives d=3, k=12 gives 4, k=24 gives 5. An independently implemented direct inverse enumeration verified binary short-word cases k=1..8 and hundreds of periodic witnesses; finite checks corroborate but never replace the all-parameter reflection proof.

## originality

PASS

PASS, best-of-knowledge. Lenz, Wachter-Zeh and Yaakobi 2017 give palindromic deletion-sphere sizes for small k and a general zero-column-run upper bound, including adjacency equivalences. These statements do not explicitly contain the sharp all-k worst-case inverse list or the arithmetic suppression at every offset 2s|k with a matching binary construction. Yohananov–Schwartz and Sun–Ge study capacity/code redundancy rather than this exact-one received-word list extremum; recent multiple-error studies address different quantifiers. The prior small-k special cases are acknowledged, and possible general zero-column theorem specialized to same result remains a risk.

## value

PASS

PASS. The maximum number of distinct parents of a received palindromic-duplication read is a canonical one-step list-decoding ambiguity invariant. An exact sharp formula for all k, q, m, with an explicit binary extremizer and nontrivial divisibility-sensitive spacing, provides a natural complete infinite-family result. It is not a code size or channel capacity claim and is not implied merely by known adjacent-position collisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
