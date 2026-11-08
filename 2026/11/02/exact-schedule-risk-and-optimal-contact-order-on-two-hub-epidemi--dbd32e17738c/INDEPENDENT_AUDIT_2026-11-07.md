# Independent mathematical audit

## correctness

PASS

PASS: On a one-shot-contact tree the unique u-to-v path transmits from a uniformly random initial seed iff contact times along that oriented path strictly increase, giving conditional probability q^distance. Every edge contributes two directed length-one routes and every two-edge path one increasing direction irrespective of timing. On D_{a,b}, the only three-edge paths are opposite-side leaf pairs; exactly M=x(b-y)+(a-x)y of their routes are chronological if x left and y right contacts precede the bridge. Thus R=C_{a,b}(q)+(q³/(a+b+2))M, with exact extrema 0,ab from the two nonnegative decompositions and equality cases. Uniform edge permutations yield binomial-select/factorial joint law for (X,Y); for pair indicators straddling bridge, mean 1/3, covariance 1/18 if one shared leaf, 1/45 if none, leading to Var[M]=ab(a+b+2)/18+ab(a-1)(b-1)/45. Independent fresh complete enumeration of edge permutations for five (a,b) cases reproduced distribution, extremal counts, exact mean and variance. Explicitly distinguish variance of conditional mean across calendars from variance of realized infection count; q=0 excluded.

## originality

PASS

PASS (qualified): A one-contact path result contains the a=b=1 P4 boundary but not the all-double-star branching classification. De Silva et al. work on longest increasing edge-ordered paths, not the probability-weighted count of all seed-target increasing paths or the random-calendar variance. Holme–Masuda's temporal network epidemic background and Deligkas–Potapov reachability optimization use different objective/model controls. A classical exact covariance count of centrally straddled pairs might exist, so originality is best of knowledge, but the complete two-parameter epidemic-calendar risk distribution is not shown to be covered by inspected work.

## value

PASS

PASS: Temporal contact-order dependence in epidemic models is a natural practical/mathematical invariant, and this result classifies its full law, exact sharp best/worst schedules, optimal-order multiplicities and calendar-to-calendar conditional-mean variance for every positive pair of hub degrees. The distinction between contact timing uncertainty and infection randomness is substantive. The exact diameter-three tree case is motivated rather than an arbitrary single small graph; no claim for arbitrary temporal networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
