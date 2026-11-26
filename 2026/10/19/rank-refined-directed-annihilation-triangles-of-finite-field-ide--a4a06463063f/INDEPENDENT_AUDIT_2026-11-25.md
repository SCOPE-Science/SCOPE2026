# Independent mathematical audit

## correctness

PASS

Fix P with E=im P and K=ker P. Choosing E and a complement gives the first Gaussian factor times q^(r(n−r)). From PQ=0 the only nonzero blocks of Q map E and K into K. Idempotence requires D=Q|_K to be a projection and C=Q|_E to have image in im D; hence rank D=s, so r+s≤n. For rank u of C (equivalently rank QP), choose its image and then a surjection from E, giving [s choose u]_q ∏_(i<u)(q^r−q^i). For R, its image W must lie in B=ker Q, avoid E, and have dimension t. The space E∩B has dimension r−u; choose the quotient image of W in B/(E∩B), then each of its q^(t(r−u)) lifts complements E∩B within its preimage. Once W is chosen, R must be zero on E and the identity on W; it is freely chosen on a complement of E+W with values in W, giving q^(t(n−r−t)). This yields the combined exponent t(n−t−u) and requires t≤n−r−s+u. The summation bounds and all nonnegative exponents follow; in particular n−t−u≥r+s−2u≥0 in a nonzero term. Three pairwise sum inequalities are necessary directly from the three containments and sufficient by taking u=max(0,r+s+t−n). This check includes zero and identity ranks. The proper-rank cycles have distinct vertices, since a repeated vertex would entail its zero square. The pairwise bounds give maximum floor(3n/2), and the balanced listed ranks attain it. For n=2m and ranks m, u=m is forced, D is the identity on K, C is an isomorphism, and R is the unique projection with image ker Q and kernel E. This gives the stated GL_m factor and full rank of every reverse product by cycling the argument.

## originality

PASS

The supported distinction is the all-rank census for three cyclic one-sided constraints, including the extremal multiplicity and reverse ranks. The image/kernel graph, pair counts, and dimension-two existence are prior background. The earlier exact pair distribution does determine the prefix marginal by (r,s,rank QP) but not the conditional third-idempotent count. No inspected comparison supplies that count or the full rank-refined triple law.

## value

PASS

Rank-refined directed triangle counts are a natural exact invariant of this idempotent graph beyond single-edge degrees. The result resolves which ranks can coexist in a cyclically noncommutative configuration, quantifies every such profile, and identifies the saturation phenomenon with maximal reverse ranks. The completion step addresses dependent edge constraints, not simply multiplying known pair statistics or relabeling an existing census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
