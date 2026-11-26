# Independent mathematical audit

## correctness

PASS

The three moments follow by choosing nonincident edges, then the unique leaf edge as appropriate; in the mixed moment the vertices must be distinct and only n-2 neighbors are possible. Conditional on the isolate the remaining graph is G(n-1,m), which gives Cov=E[X_0]*(f_(n-1)-f_n) with f the expected leaf count. For positive f_(n-1) and f_n the ratio starts at 1 for m=1; successive ratios are less than 1 since the denominator minus numerator in the consecutive-factor formula equals (n-1)(n-4)/2+m>0. This holds on the positive range 1<=m<=B; for B+2<=m<=A the smaller graph cannot have a leaf but the larger one can. At m=0,1 the leaf count is deterministic; at m>A the isolate count is identically zero. For m=O(n), the consecutive factor is uniformly 1-2/n^2+O(n^-3); taking logs and summing gives n*(R_n(m)-1) tending to -c. The isolate probability tends to exp(-c) by its finite no-incidence product, and the leaf probability tends to c*exp(-c) by choosing its one incident edge and applying the same product estimate. This gives the asserted covariance divided by n. Under independent edges the distinct-vertex joint probability is (n-2)*p*(1-p)^(2n-4) and the one-vertex probabilities give the stated subtraction. At m=n and n>=5, n<=A and p=2/(n-1) lies strictly between 2/n and 1. The packaged artifacts/verify.py was read, not executed; its finite checks are not used in place of proof.

## originality

PASS

The earlier fixed-size histogram covariance spectrum and its proof already determine the exact isolate–leaf covariance in every case. Credit that coverage explicitly, as well as the known independent-edge comparison formula; neither exact mixed-moment counting nor merely extracting the entry is an independent advance. The supported distinct result is the sharp all-density sign and zero-set classification (and resulting finite ensemble reversal). The earlier degree-score covariance is not an entrywise sign bound; its conditional-degree representation reduces the question to an inequality between hypergeometric probabilities, not a direct sign evaluation uniform in m and n. The submitted isolate-conditioning comparison resolves that inequality. The fixed-size sparse constant is consistent with existing conditioning heuristics; priority of that asymptotic alone is not asserted by this review.

## value

PASS

Isolates and leaves are natural degree-profile summaries. Their covariance has an explicit strict sign up to the isolated-vertex support cutoff, with all degenerate cases resolved. Matching the edge count in expectation can give the opposite sign under independent sampling, a concrete constraint on transferring ensemble intuition. The value is the structural sign classification and comparison, not recomputing the known mixed entry or asserting wider negative association.

The dated certificate retains the supplied scientific assessment, sources and limitations.
