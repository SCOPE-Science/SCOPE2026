# Independent mathematical audit

## correctness

PASS

The standard independent insertion timestamps characterize an interval of k ranks as fringe iff its two exterior delimiters precede all k internal timestamps; interior event probability p_k=2/((k+1)(k+2)) and end event probability 1/(k+1). The exact local-dependence neighborhoods have O(r√n) sites and event probabilities O(1/n), so AGG b1=O(n^-1/2), b3=0. For b2, overlapping intervals must be nested; strict nested conditional probability is p_k, endpoint-sharing is 1/(k+1), touching disjoint events impossible, and one-rank-gap joint probability is the integral of h_k(t)h_l(t)=O(n^-3/2). Summing O(n) relevant pairs gives b2=O(n^-1/2), and discarded 2r boundary sites probability O(n^-1/2). This establishes process-level TV to lattice field. Riemann-sum intensity convergence gives *weak*, not TV, convergence to continuous Poisson. Independently checked exact insertion interval marginal identities for n=4,5 permutations; inspected full supplied VERIFY.py for n<=7 and six exact n=9 joint identities, not relying on its claimed exit code. Rate constants depend on fixed r,a,b, no assertion outside the critical band.

## originality

PASS

Direct published same-model full 2010 Dennert–Grübel §4.2 explicitly conjectures joint independence of critical-size counts and states lack of a proof, whereas Proposition 2.1 only gives covariance tending to zero. Their 2010 theorem treats small k Gaussian and macroscopic profile processes, not joint critical-band marked process. Feng–Mahmoud–Panholzer, Fuchs, and Holmgren–Janson give individual critical Poisson or fixed-type asymptotics. Resolving the joint conjecture and producing a uniform marked spatial TV bound is a stronger new theorem on the same natural object. Literature search did not locate an intervening full multitype theorem; later priority remains a risk.

## value

PASS

Resolves explicitly stated open independence question for natural critical fringe-subtree counts, with stronger uniform finite-n spatial marked TV error. The complete multitype result is useful when multiple adjacent sizes have identical scale limits; neither variance decay nor one-size Poisson suffices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
