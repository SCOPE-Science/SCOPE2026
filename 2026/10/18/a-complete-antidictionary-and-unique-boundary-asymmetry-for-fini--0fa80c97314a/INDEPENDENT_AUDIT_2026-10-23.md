# Independent mathematical audit

## correctness

PASS

For binary Fibonacci prefixes F_0=0,F_1=01,F_k=F_(k-1) F_(k-2), k>=5, the length-q block B=F_(k-2) occurs only at offsets 0,q,p, making shortest unique suffix K=q+1. Standard finite Sturmian/trapezoidal complexity gives c(t)=min(t+1,q+2,N-t+1); only central palindromes U_1,...,U_(k-2) are bispecial in the finite word. The counting identity m(t)=b(t-2)+2c(t-1)-c(t-2)-c(t), derived by two-sided extension grouping, gives one absent word at each asserted k length, with no others. Explicit y_j U_j y_j, xUx and d F_(k-2)0 each have both proper adjacent factors present and do not occur; only the last fails reversal symmetry. An independent full factor-set enumeration for k=5..10 reproduced complete set, count, lengths and one nonpalindrome; unbounded proof depends on accurately indexed primary occurrence/Sturmian results, not finite sampling.

## originality

PASS

Best-of-knowledge noncoverage of the specific new claim: Classifying every minimal absent contiguous factor of a standard finite Fibonacci word, including the exact two linear boundary exceptions and the sole nonpalindromic element, is a natural complete combinatorics-on-words invariant. Prior overlapping premises and historical-priority caveats are explicitly credited and scoped.

## value

PASS

Classifying every minimal absent contiguous factor of a standard finite Fibonacci word, including the exact two linear boundary exceptions and the sole nonpalindromic element, is a natural complete combinatorics-on-words invariant. It distinguishes finite linear from infinite or cyclic factor languages and provides directly usable anti-dictionary data, rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
