# Independent mathematical audit

## correctness

PASS

From r_{2i}=r_i and r_{2i+1}=r_i xor (i mod 2), state 2r_i+(i mod 2) follows the stated 4-symbol length-2 morphism. The exact eight adjacent state pairs E all occur in phi^4(0) and are closed under substitution; for n<=2^h every length-n factor lies in an aligned pair of length-2^h substituted blocks and every candidate pair actually occurs, proving exhaustive factor language (not just a sampled prefix). For a binary length-n word, all scattered length<=2 subsequence counts are equivalent to (W,T): #10=W(n-1)-T-C(W,2), #01=W(n-W)-#10, and #00/#11 depend only on W. Direct independent digit-rule C++ computed every (W,T) profile over the 65536-letter certified prefix for each n=1..4096; all 4096 spectrum rows and 620 dyadic weight rows match pinned Git CSV FNV64 fingerprints and exact length counts (spectrum 4097 lines/93566 bytes, FNV64 09b6fe847a6d626e; dyadic 621 lines/7277 bytes, FNV64 fe746b168315eeeb). At n=4096 count=24783, weight range 1953..2143. An independent shorter Python check verified E closure and equivalence on all binary words of length 1..8. These computations are exhaustive because of the proved substitution factor cover; they do not imply an unclaimed asymptotic.

## originality

PASS

Best-of-knowledge new technical specialization assessed after four statement/implication comparisons, primary-source reading and Resultary search. Published general background and covered special consequences are credited; no dominating prior theorem for the final stated result was found in material actually inspected.

## value

PASS

A complete exact 4096-length classification of the natural 2-binomial factor-complexity invariant for a classical automatic word, together with a reusable all-length eight-parent-block reduction and weight-resolved census, gives a reproducible finite reference and structural method. The cutoff has dyadic substitution motivation, not a random unmotivated slice. The result does not assert a closed formula beyond the cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
