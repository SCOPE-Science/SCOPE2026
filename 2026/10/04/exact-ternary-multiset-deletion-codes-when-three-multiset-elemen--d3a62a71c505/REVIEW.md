# Independent mathematical audit

## correctness

PASS

The heavy-coordinate argument proves the complete infinite statement. If two codewords both have a coordinate of multiplicity at least three in the same alphabet position, their multiset intersection has size at least three, so their heavy-coordinate sets must be pairwise disjoint. For length at least seven every ternary composition has a heavy coordinate, giving at most three codewords and the three constant words attain the bound. At length six the unique heavy-free composition is \((2,2,2)\); at length five the heavy-free words are the three permutations of \((2,2,1)\), any two of which intersect in four symbols. These facts give the sharp upper bound four at lengths five and six, attained by the displayed witnesses. The package verifier exhaustively confirms the two boundary lengths, and an independent exact set-packing reconstruction also returned maxima four, four, and three at lengths five, six, and seven. The unbounded part rests on the analytic pigeonhole argument, not the finite computations.

## originality

PASS

The closest primary paper studies exactly the same multiset deletion model. Its high-deletion section gives the general certificate bound \(S_q(n,n-3)\le q+\binom q2\), which yields only six for the ternary case, while its exact ternary benchmark concerns a different one-deletion regime. Full primary-text inspection did not locate the piecewise ternary values four, four, then three. Current Resultary and equivalent discrete-simplex/intersection searches likewise returned no stronger theorem implying the audited formula.

## value

PASS

This resolves a natural first small-alphabet instance in the source's high-deletion regime and closes a factor-two gap between a general certificate bound and the true ternary optimum. The proof also identifies the simple structural reason for the collapse to three codewords beyond the two exceptional boundary lengths. That is a complete natural classification, not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
