# Independent mathematical audit

## correctness

PASS

For any strict disagreement label the unique first greedy choice A. Since the marginal comparison is exactly the comparison of the two complete pair scores containing A, the unique global optimum has to be BC. Let a,z,w count ballots A, BC, ABC, let d_B,d_C be the positive approval deficits relative to A, and write 2(P(BC)−P(AB))=1+u, 2(P(BC)−P(AC))=1+v. Pair scores are sums of approval totals minus half their shared approvals. Solving these integer equations gives AB=z+2d_C+1+u, AC=z+2d_B+1+v, B=a+d_B+1+v and C=a+d_C+1+u. Hence n=10+3(a+z+d_B−1+d_C−1)+2(u+v)+w. The remaining marginal difference is (v−u)/2, so strictness costs at least two voters. Equality forces u+v=1 and all other excess terms zero. The two assignments of u,v are exchanged by B↔C and represent distinct count vectors; the three choices of A give six profiles. The given profile's pair scores are (11,23/2,12), and the two second-round marginals are (4,9/2). Adding all-approval ballots preserves all score differences. Thus the argument covers all n, not only the enumeration range.

## originality

PASS

The best-supported distinct claim is the exact tie-free threshold and equality classification for three candidates, not the existence of PAV/seq-PAV differences or the 10-voter committee-monotonicity example. No inspected antecedent covers both unique greedy rounds and the sharp classification in this size regime.

## value

PASS

The smallest candidate/seat setting in which a greedy pair can disagree with the global pair yields a sharp minimal electorate under a substantive uniqueness constraint. The orbit classification supplies a canonical test profile and isolates the two-voter cost of removing the known second-round tie. This is a usable boundary, not merely another disagreement example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
