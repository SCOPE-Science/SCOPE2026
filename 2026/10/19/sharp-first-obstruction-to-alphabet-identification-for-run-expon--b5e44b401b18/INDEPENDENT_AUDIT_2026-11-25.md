# Independent mathematical audit

## correctness

PASS

I reimplemented the complete search by inserting positions into existing partition blocks or a new block, which represents every word up to renaming exactly once with no cap on the number of symbols beyond its length. The independent scorer enumerates every interval using vectorized lag-equality masks, takes the first matching period p<=length/2, tests both one-place extensions, and sums exact integer weights scaled by lcm(1,...,floor(n/2)); at n<=12 both masks and scores stay within their integer types. It discards an original word only if its score is zero or a merge has at least its original score, so short-circuiting cannot miss a witness. Counts for lengths 3–12 were 1, 7, 36, 171, 813, 4012, 20891, 115463, 677546 and 4211549; exactly one survivor at 12, 001101121122, and none earlier. Lengths below three cannot use three symbols. A separate literal slice-based scorer reproduced the four full run lists for each k=2–9. If all non-tail symbols are within positions 1 through T, each complete period block of a nonconstant run must have a non-tail symbol. The first two blocks give p<=T-1 and the final one gives an endpoint <=T+p-1<=2T-2. Here T<=10 in all four families. Thus the nonconstant runs stabilize in the common prefix ending at 18, without a maximality change beyond it; only the terminal constant run grows. This establishes the exact infinite-family scores and every strict inequality without extrapolation. Reversal was not used as an equivalence.

## originality

PASS

No checked claim gives the first strict failure of every single-pair alphabet identification to preserve the run-exponent sum, the unique length-12 pattern, or the family for each larger length. Global exponent bounds, binary fixed-composition scores and coarsening effects for a different observable are relevant adjacent results but do not supply this wordwise obstruction. The finding implies neither a separation nor equality of the global binary and unrestricted maxima.

## value

PASS

The binary and general run-exponent problems motivate a specific plausible proof strategy: reduce the alphabet by a score-preserving or score-increasing pairwise merge at each step. The robust counterexample shows that this step is not always available. The statement identifies the first failure over all alphabets, its unique pattern, and persistence at every larger length. This exact boundary is useful independently of whether any global maximizing word exhibits the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
