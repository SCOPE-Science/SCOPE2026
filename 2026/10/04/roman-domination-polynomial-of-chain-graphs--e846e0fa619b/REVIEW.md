# Independent mathematical audit

## correctness

PASS

The four-way partition by locations of label 2 is exhaustive and disjoint. With no label 2, every vertex must be 1. With label 2 only on A, the latest A class containing a 2 determines exactly which A classes may contain 2 and which B classes are defended and may contain 0; the B-only case is symmetric. When both sides contain a 2, the earliest B class r and latest A class s determine independently, class by class, whether labels 0 and 2 are permitted, while subtracting the no-2 boundary-class factor forces A_s and B_r to contain a 2. These permissions are exactly the stated F_n^{z,t} factors, so the product formula counts each Roman dominating function once. The minimum formula follows by comparing the no-2, one-side-2 and both-sides-2 regimes. A fresh independent brute-force replay on four nontrivial canonical twin profiles matched the closed polynomial coefficientwise; the package verifier exhaustively checks all 255 positive twin-class profiles through total order 9, over 3,023,307 labelings.

## originality

PASS

The complete 2021 Roman-domination-polynomial paper was inspected at the definition and its specific-family section; Theorem 3.4 gives the complete-bipartite polynomial, exactly the p=1 boundary case, but it does not give the arbitrary chain-graph twin-class factorization. The 2020 chain-graph paper is framed as minimum-weight Roman domination optimization, and accessible material does not state an all-weight enumerator; its full text was not available through the inspected route, so incidental overlap remains a residual risk rather than a failure. The Roman Census work enumerates pointwise-minimal functions, a different object from all feasible functions by weight. Targeted Resultary search found the audited chain polynomial and nearby different domination polynomials, but no earlier equivalent full Roman weight enumerator for chain graphs.

## value

PASS

Chain graphs are a canonical nested-neighborhood bipartite class, and the full Roman domination polynomial is the natural all-weight refinement of the already studied minimum problem. The formula gives every coefficient from the canonical twin-class sizes in O(p^2) product terms and strictly extends the published complete-bipartite boundary case, making it a motivated complete classification rather than an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
