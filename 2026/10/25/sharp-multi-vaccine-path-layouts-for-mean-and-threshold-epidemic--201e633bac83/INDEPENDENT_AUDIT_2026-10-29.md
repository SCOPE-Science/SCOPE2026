# Independent mathematical audit

## correctness

PASS

Every vaccination set corresponds uniquely to b=k+1 nonnegative gap lengths summing N. In a gap L, exact expected number of seeds with an outbreak of size >=t is 0 for L<t and p^(t-1)[(t-(t-1)p)L-t(t-1)(1-p)] for L>=t, via weighted counts of maximal edge-open runs. Merging two active gaps into one while setting other t-1 strictly decreases risk by (t-1)p^t; filling inactive gaps toward t-1 decreases by positive slope. Hence zero-risk case N<=b(t-1) has exactly all gaps <=t-1, otherwise threshold optimizer unique multiset (N-(b-1)(t-1), t-1,...). Mean cost H(L)=L+2∑(L-d)p^d has strict second differences 2p^(L+1)>0, giving exactly balanced gaps. Both sets intersect iff N<=b(t-1)+1. Independently exhaustively evaluated rational open-edge cases and compositions with N<=9; all matched. Endpoint p=0,1 excluded.

## originality

PASS

Best-of-knowledge PASS after independent statement/implication comparisons with primary literature and published semantic records. Known starting theorems explicitly credited; absence of matching search results not treated as proof of priority.

## value

PASS

Complete optimal vaccination layouts for two naturally conflicting risk objectives, including exact sharp population/budget threshold when mean-optimal prevention cannot also minimize a clinical capacity exceedance probability. Tail cost affine above threshold while expected cost strictly convex; this is a substantial exact path-percolation optimization classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
