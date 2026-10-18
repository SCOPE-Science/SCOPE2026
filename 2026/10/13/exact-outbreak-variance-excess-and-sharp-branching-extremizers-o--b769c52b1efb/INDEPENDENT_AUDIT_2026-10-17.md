# Independent mathematical audit

## correctness

PASS

For finite rooted tree T seeded at root, iid vertex Q_i with E Q=q∈(0,1), Var Q=v≥0 and conditionally independent forward-edge trials, each root-to-u path uses distinct parents and E I_u=q^{d(u)}. For incomparable u,w with LCA a, their shared-path union contains exactly two outward trials from a and other distinct parents, so P(I_u=I_w=1)=(q²+v)q^{d(u)+d(w)−d(a)−2}; same model independent bonds yield q to the full union length. Comparable pairs have identical joint law. Covariance expansion therefore yields Var(Z_T)−Var(Z_T^BP)=2v∑_{u∥w}q^{d(u)+d(w)−d(LCA)−2}. Each exponent≥0 gives upper bound choose(n−1,2), uniquely central star when branching. Pick a depth-k branching vertex with two children, k≤n−3, to obtain lower q^k≥q^{n−3}, uniquely terminal binary broom; zero iff root is endpoint of a path. For v=0 all variance excesses vanish and shape uniqueness is asserted for B_T only. Continuous-time exponential recovery contact specialization v=q²(1−q)/(1+q) checked. Source exact enumeration of trees through n=7 inspected, universal result from indicator proof.

## originality

PASS

Previously known mean tree agreement with bond percolation and shared-infectious-period outgoing-transmission covariance are properly credited. The exact fixed-tree lowest-common-ancestor variance-excess polynomial and both sharp rooted-shape extremizers are more specific than general epidemic-percolation distribution representations or random-degree outbreak-variance formulas inspected. Implicit derivation from earlier general moment frameworks remains plausible.

## value

PASS

The exact single-seed, finite-tree variance inflation and sharp star/broom extremizers characterize how contact topology magnifies shared recovery variability without altering expected outbreak size. This directly addresses a natural distinction between independent percolation and epidemic dependence, not a marginal or trivial numerical restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
