# Independent mathematical audit

## correctness

PASS

For a,b>=2, a uniform spanning tree of K_{a,b} and opposite-part marked u,v, distance Delta=2t-1 has probability (a-1)_(t-1)(b-1)_(t-1) C_t/(ab)^t, with C_t=t(a+b-t). Ge--Dong Theorem 1.4 counts tree extensions containing a prescribed connected tree H; applying it to each alternating path, then a fixed path plus j eligible edges at u and ell at v, gives mixed factorial moments E[(D_u-1)_j(D_v-1)_ell | Delta]= (b-t)_j (a-t)_ell/(a^j b^ell) [1+(j(a-t)+ell(b-t)-j ell)/C_t]. Factorial-moment summation yields the complete stated bivariate PGF, including R=b-t=0/L=a-t=0 conventions. Mixed first moments simplify via C_t+(a-t)(b-t)=ab to Cov(D_u,D_v|Delta=2t-1)=-(a-t)(b-t)/C_t^2, strictly negative except at maximum distance. Marginal PGFs factor as Bin(b-t-1,1/a)+Bernoulli(b/C_t) and the swapped counterpart, with boundary a leaf; decreasing trial counts and success probability yields strict stochastic regression and negative Cov(D_u,Delta), Cov(D_v,Delta). Independently checked the covariance identity with exact rational arithmetic across five boundary/interior triples; verified the supplied exhaustive code independently counts trees and tests 574 rational constraints, but full run not repeated.

## originality

PASS

Ge and Dong Theorem 1.4 (2019 preprint, 2020 journal) already supplies a powerful arbitrary-fixed-tree extension count; all joint edge-inclusion moments are in principle deducible from it. That input is credited, not claimed new. The assessed additional result is the explicit complete *distance-conditioned* bivariate endpoint-degree PGF, its simple exact negative covariance, and strict first-order stochastic regression as separation grows, requiring simultaneous path conditioning, factorial-moment inversion and monotone coupling. A relevant published Cayley-tree result handles a different nonbipartite host and one endpoint. The earlier general inclusion theorem might be judged to dominate the covariance via a short corollary: high and material originality risk, not obscured.

## value

PASS

Uniform spanning trees of complete bipartite graphs are canonical exactly countable random trees. The full conditional two-endpoint law and its strict distance regression quantify a natural dependency structure under a global path constraint, including a zero-covariance leaf boundary. The compact covariance is useful without repeating full tree enumeration and the exact PGF permits further degree-tail calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
