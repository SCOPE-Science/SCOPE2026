# Independent mathematical audit

## correctness

PASS

Under the uniform-parent growth rule, conditional on all marked arrivals, a new vertex's parent is uniform among earlier members of its own class, and those parent choices factor. The color-path probability depends only on class counts. Hence after relabeling by arrival order the two induced trees are independent recursive trees even given just S=s. There is precisely one crossing edge, from the parent of k, chosen independently among the first k−1 unmarked labels. Interior leaf status agrees with whole-tree status; that crossing edge removes an outside leaf exactly when its tail was an outside leaf. The unmarked tree of size N≥2 has rank-i leaf probability (i−1)/(N−1); averaging over its first k−1 vertices gives (k−2)/[2(N−1)]. At k=2 the only candidate is the outside root, a leaf iff N=1. Together with the singleton leaf convention this proves both regressions, including k=n and n=3. The beta-binomial S−1 law with urn parameters (1,k−1) gives ES=n/k, P(S=1)=(k−1)/(n−1), and the stated variance; substitution in Cov(S,U) verifies the exact formula. For the global covariance, write I for attachment inside and F for attachment to a nonleaf. Then E[IF|T_t]=(S_t−U_t)/t, and the S_t E[F|T_t] and L_t E[I|T_t] terms cancel their S_t L_t/t parts. Subtracting mean products gives C_{t+1}−C_t=−(k−1)/[2t(t−1)] and C_k=0. The monotone-score sign follows by the two-independent-copies covariance identity: nonconstant monotone scores differ at support endpoints, as do the regressions in the asserted strict cases. Corroborated the formulas for 197 parameter pairs by an independent integer-state Markov enumeration on (S,U,L), using the four attachment-class sizes U, S−U, L−U, and t−S−L+U. Replay: python3 /workspace/branches/reproduce_discrete.py.

## originality

PASS

The supported distinct contribution is the exact global whole-tree leaf regression for arbitrary k≥3 and its covariance and monotonicity consequences. The classical urn and internal subtree law, local leaf moment ingredients, and the k=2 specialization are not new claims. The closest inspected prior recursive-tree split is at vertex 2; an earlier regression on singleton root branches conditions on a different variable. No verified existing theorem was found that fixes the k≥3 outside-leaf correction or covers the full joint comparison. Bounded retrieval does not establish priority.

## value

PASS

Conditioning on the size of a fixed branch makes its own leaf count grow in expectation but makes the average global leaf count fall. Computing and explaining the crossing-edge correction resolves this natural distinction, identifies the exceptional label and singleton boundaries, and proves the signs for all monotone scores. This is a useful exact dependence statement, stronger than a lone numerically verified correlation and not just an application of a marginal leaf mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
