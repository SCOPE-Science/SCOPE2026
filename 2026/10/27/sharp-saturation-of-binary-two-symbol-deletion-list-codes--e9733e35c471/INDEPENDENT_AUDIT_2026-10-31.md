# Independent mathematical audit

## correctness

PASS

For every n>=3 and integer L>=1, each received word of length two is an ordered (not necessarily consecutive) subsequence, and codes use distinct source words. Each input has repeated 0 or 1, giving M<=2L. Exactly two constant words have signature size one and exactly four boundary-minority words have signature size two; all others have size >=3, so 3M-8 <= four receiver loads <=4L. Thus B(L)=min(2L,floor((4L+8)/3)). All three-output signatures are classified for n>=4 by missing pair: counts n-2,n-2,n-3,n-3; four-output words contribute at least one excess signature count. At equality B for L>=5, total excess q<=delta=4L+8-3B, forcing B <=4n-4+delta, and the three L mod 3 cases imply n>=max(4,ceil(L/3)+1); n=3 has only eight inputs and is strictly short. Explicit layer-based constructions with base six small-signature words, class multiplicities, and zero, one or two four-output words attain all four load ceilings for every n at/above threshold, and for L=1..4 attain 2L for every n>=3. Independent dynamic programming checks all n=3..6 and L=1..8, plus direct enumerations of signature class sizes. The proof is symbolic for all n,L; no claim of exact smaller-n M below saturation.

## originality

PASS

Statement/implication comparison of actually read primary theorems and direct published mathematical-finding search supports best-of-knowledge originality for the final narrow claim, with precisely documented broader prior formulas and residual historical risks. Neither a failed search nor literature inaccessibility is treated as a proof of novelty.

## value

PASS

The near-total deletion regime with exactly two ordered surviving symbols is a natural extremal list-decoding channel. The result gives a sharp universal capacity ceiling and the exact onset in source length when it becomes achievable, a genuine all-n,L phase transition rather than an arbitrary finite code table. It specifies a constructive family and sharp obstruction while honestly leaving below-saturation optima unclassified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
