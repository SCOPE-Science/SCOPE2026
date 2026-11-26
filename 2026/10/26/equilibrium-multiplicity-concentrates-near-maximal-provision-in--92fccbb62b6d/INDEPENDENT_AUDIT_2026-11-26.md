# Independent mathematical audit

## correctness

PASS

At 0<c<1, any served buyer can profitably drop out and any unserved nonbuyer can profitably buy. The reverse also holds: with no nominations to buyers and all nonbuyers served, changes of the nominations of a continuing buyer do not raise that buyer's payoff, and neither changing buy to abstain nor the reverse benefits the deviator. Thus fixing q nonbuyers leaves an ordered (by purchaser labels) list of k-subsets covering the nonbuyers. The necessary q≥k and k(n−q)≥q are sufficient by the cyclic assignment, also when only one purchaser fits the model. Inclusion–exclusion over omitted nonbuyers with the factor C(n,q) counts precisely these profiles. Independently, write L=log n and B=kn log n−kn log L−n log(k!). At q0=floor(n/L), the probability of a missed recipient is at most q0 exp(−k(n−q0)/q0)=O(n^(1−k)/L), which tends to zero even at k=1. The logarithm of C(n,q0) is o(n), and log C(q0,k)=k log q0−log(k!)+O(1/q0); together these give log N(q0)=B−kn+o(n). The relaxed upper bound g_n at a n/L for fixed a>0 is B+kn(log a−a)+o(n). Its strictly decreasing derivative, positive at a=1−ε and negative at a=1+ε for large n, places every exterior value below the larger endpoint bound. Relative to q0 the endpoints lose kn(a−1−log a)+o(n), a positive linear loss; summing over at most n counts proves convergence in probability. Equilibrium coverage and the extremal feasible counts give both cost ratios. A covering optimum uses at least ceil(n/(k+1)) buyers and the cyclic construction attains it; dropping coverage cannot improve the welfare optimum when an unserved player can instead buy for c<1.

## originality

PASS

The best-response structure and extremal welfare calculation are antecedents, as is the Stirling/surjection form of the count when k=1. The inclusion–exclusion itself is standard. The supported increment is the specified full labelled PNE census together with concentration at n/log n nonbuyers for general fixed k, not a new price-of-anarchy result or novelty for the classical k=1 combinatorics. The strongest model and asymptotic analogues do not give that distribution.

## value

PASS

Knowing which equilibrium sizes exist or that an inefficient equilibrium exists does not tell whether inefficiency is exceptional under the stated counting measure. The result shows that uniformly counted profiles typically incur almost the worst cost for that n and identifies the sublinear scale of the missing purchases. This supplies a quantitative multiplicity result distinct from extremal inefficiency, without treating the uniform measure as a behavioral prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
