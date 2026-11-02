# Independent mathematical audit

## correctness

PASS

The theorem counts distinct nonempty cyclic palindromic factors of length at most n in oriented binary necklaces with exactly three 1s, not their occurrences. Classify factors by 0, 1, 2 or 3 included ones. Sorting zero gaps r<=s<=t gives four valid cases: all equal P=3r+floor(r/2)+3; r=s<t P=t+3r+floor(t/2)+4; r<s=t P=r+3t+floor(r/2)+4; strictly increasing P=t+2s+2r+4. Rotational gap triples yield one necklace for repetitions and two for distinct gaps. Gap substitutions into geometric series reproduce exactly the three-term rational F(x,y) in RESULT.md. Repeated-gap classes are O(m) against Theta(m^2) total, and normalised gap triples converge to the uniform 2-simplex; P/m converges to 2−max(V1,V2,V3) with the stated piecewise cdf and mean 25/18. Independent brute-force enumeration constructed all binary necklace rotation classes of length 3..15, enumerated all length<=n circular palindromic strings, and confirmed every gap-case count and the complete finite distribution for those lengths. Finite validation does not prove formal-series or limit statements.

## originality

PASS

A full individual three-marker palindrome inventory, composition-refined rational bivariate generating function, and nondegenerate limiting law go beyond the published unrestricted circular-word upper bound and maximum sequence. Simpson (2014) is unusually close and its unavailable full text leaves real priority uncertainty; abstract silence was not treated as conclusive noncoverage.

## value

PASS

Fixed-three-marker circular words are a natural constrained family for palindrome complexity. The exact distribution across all compositions, repeated gaps and oriented rotation classes resolves an infinite enumerative problem; the limiting law gives a quantitative typical-case counterpart to the previously known extremal upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
