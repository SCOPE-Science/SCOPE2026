# Independent mathematical audit

## correctness

PASS

For an omitted cell the number of omitted neighbors equals its two incidence degrees minus two; it has no selected neighbor iff both of its incidence lines are full of omissions. Isolated-edge events in a compatible collection form a matching; there are binom(m,k)binom(n,k)k! choices, k forced present edges and (m−k)(n−k) free edges. Full omitted rows and columns force an an+bm−ab union, and when both exist they rule out all isolated edges since each outside edge belongs to or touches one of the two full stars. Thus subtracting that separate inclusion–exclusion polynomial is exact. An independent literal-definition enumeration and independent expansion agreed on all 70,480 subsets of six boards, with sums 5,33,175,307,2967,52539; the 2×3 vector is [1,0,9,14,9,0,0]. Replay by looping through bitmasks, testing each omitted cell for one member and one nonmember in its row/column neighborhood, and tallying by omitted count against the two finite binomial sums. Frozen verification and checker inspected without execution. In the first window the joint falling factorials of empty selected rows and columns are (N)_a(N)_b(1−p)^(N(a+b)−ab)→e^(−c(a+b)); isolated omitted cells have expectation o(1). The first event is a union of the two zero counts, not their intersection. In the second window the kth isolated-edge factorial moment is (N)_k² q^k(1−q)^(2kN−k²−k)→(e^(−c)/2)^k, while full lines are bounded by Nq^N. Poisson convergence yields the stated zero probabilities; the limit of the moment in each case is finite and uniquely specifies the Poisson law. In the last window, a nonempty successful omission set requires an adjacent omitted pair, whose probability is bounded by c²/N; hence the success asymptotic equals the empty-omission probability e^(−c), also for c=0. Finite enumeration verifies only the enumerated boards, not the asymptotic limits.

## originality

PASS

A general Cartesian-product feasibility criterion and the basic obstruction tests are not standalone novel results. What passed is the exact complete rectangular enumerator for this particular property together with the three limits for the same restrained-domination event, including the distinction between requiring one shore or both shores to avoid isolates. No earlier exact coverage of this combined result was found in the inspected sources. The Poisson tools and general occurrence of sparse-window phenomena are not claimed new.

## value

PASS

The labeled rectangular formula is usable coefficientwise for a standard graph invariant. On squares the three separate scales identify which obstruction dominates and prove a concrete near-complete nonmonotonicity: the success probability at q=0 is one, at q=1/N² tends to e^(−1), and at q=(log N+log log N)/(2N) tends to e^(−1/2). This is more informative than feasibility alone or a single monotone-threshold analogy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
