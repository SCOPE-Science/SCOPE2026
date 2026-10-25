# Independent mathematical audit

## correctness

PASS

For real unit-spaced finite path, N(f)=sup|f|+max adjacent difference. At nonconstant boundary let a,b>0 sum to 1. Tight adjacency edges partition vertices into runs; each must meet a mark |f_i|=a or translating an unmarked component yields a midpoint decomposition. If none of the runs has marks of both signs, a and b can be varied oppositely to give a midpoint; conversely a mixed-sign run fixes 2a=db for an integer 1<=d<=n-1 and, with every tight run marked, all saturated equalities force each vertex uniquely, proving extremality. Shared lattice f_i=-a+(2/(d+2))h_i and every nontight edge must have zero integer step, yielding the exact height walk with steps -1,0,1 and boundary-hit run conditions. Distinct d are recovered by 2a/b. A DP with height j, current mask of level {0,d} hits, and mixed-run Boolean counts all eligible paths; O(n^3) integer additions across 1<=d<n and O(n) reusable storage. Independent direct enumeration of height words gave V_n=4,10,26,64,162,404,998 for n=2..8, matching predicted series. No finite enumeration substitutes for extremality and DP proof.

## originality

PASS

Best-of-knowledge statement-level comparison identifies no prior theorem implying the final claim at its actual hypotheses; known overlap and residual bibliographic risks are recorded, not erased.

## value

PASS

The additive bounded-Lipschitz unit balls of equally spaced finite paths form a natural exact-polytope family. Complete integer-grid rigidity and canonical vertex walks yield an O(n^3) exact census for every n instead of generic exponentially large active-set/polytope enumeration. The count is a useful exact geometric invariant even without a general fast dual norm optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
