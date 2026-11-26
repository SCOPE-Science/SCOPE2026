# Independent mathematical audit

## correctness

PASS

Uniform fixed-degree maps are uniform multiset words, so the probability of specified distinct fixed positions is their degree product divided by (n)ₖ. Expansion gives the PGF, mean 1 and variance 1−2C(d)/(n(n−1)). For a two-label transfer first choose uniformly the union S of the m=A+B positions occupied by either label, then allocate all outside symbols; neither stage depends on the split. With neither designated position in S no local match is possible. With exactly one, swapping the two designated positions gives the same law for the outside fixed-point count, since neither designated position is an outside label. Averaging the two cases gives match probability 1/2 under either split even conditional on the outside count. When both are in S, local counts 0 and 2 have probability AB/[m(m−1)] each; their common increase after balancing is (A−B−1)/[m(m−1)]. Multiplying the change in the three local probabilities by Pr(both in S)=m(m−1)/[n(n−1)] proves the identity for all tests. Integer majorization decomposes into these transfers: for sorted profiles with unequal entries, transfer from a first excess to a first later deficit, maintaining prefix dominance before re-sorting, and decreasing the sum of squares until the sorted target is reached. The excess and deficit give a difference at least two. Convex second differences are nonnegative and strictly positive for strictly convex functions, including when n=2. In the unconditional model E[F|D]=1 gives orthogonality to all degree statistics; F=n forces all degrees one with positive probability, and that degree event is not certain. The probability of a specified ordered pair of fixed points is n⁻², and under that condition its two degrees have one forced hit plus Bin(n−2,1/n), while all others have that binomial alone. Subtracting n bₙ(r) and using the two-step binomial convolution gives the stated signed second difference with factor (n−1)/n². The signs at zero and one are immediate from b(1)/b(0)=(n−2)/(n−1), at two the bracket divided by b(0) is n(n−3)/(2(n−1)²), and for 3≤r≤n the ratio b(r−1)/b(r−2)=(n−r)/[(r−1)(n−1)] is strictly below 1/2. Inspected source scripts without executing them. The convex checker derives probabilities from the PGF, so it is finite corroboration, not independent evidence for the PGF; the map enumeration checks moments directly in its stated small-size ranges.

## originality

PASS

Credit the exact conditional degree-to-law formula and mean independence to the earlier indexed record, and record mathematically equivalent coverage of the transfer theorem in a separately indexed, later-dated record. This pass does not award priority for the conditional theorem; the distinct finite signed covariance profile for ordered fixed-point pairs versus degree frequencies is not covered by either inspected record. The broader model and elementary-symmetric counting are established antecedents.

## value

PASS

The exact signed mixed moment resolves how a standard cycle statistic and degree frequencies can be dependent when the ordinary fixed-point count is uncorrelated with every degree statistic. It identifies which occupancy classes detect paired loops and shows the finite sign transitions, rather than just observing that nonindependence is possible. The conditional transfer is useful context for the phenomenon but its catalogue overlap is not counted as independent value here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
