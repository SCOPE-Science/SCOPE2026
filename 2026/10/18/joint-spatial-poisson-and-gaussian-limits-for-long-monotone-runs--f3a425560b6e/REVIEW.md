# Independent mathematical audit

## correctness

PASS

In the regime n→∞,r→∞,n/r!→λ in (0,∞), each increasing or decreasing consecutive r-window event has probability 1/r!. Signed overlapping windows at separation d (1≤d<r) of the same orientation have probability 1/(r+d)!; opposite orientations with ≥2 shared positions are impossible and with one shared observation have probability 1/[(2r−1)((r−1)!)²]. Hence the expected total number of overlapping event pairs is O(n/(r!r)+nr/(r!)²)=o(1). Split the i.i.d. rank model into disjoint blocks b=⌊n^(1/3)⌋, with r≪b≪√n: discarded boundary events are o(1), each independent block has asymptotically at most one marked rare event, and its marked categorical Laplace factors yield two independent spatial Poisson processes with intensity λdt. Descent indicators are 1-dependent with variance1/4 and adjacent covariance−1/12, giving Var(D_n)=(n+1)/12. Removing block boundaries costs o_p(√n); bounded block sums satisfy Lindeberg and give N(0,1/12). Within each block the rare-event Laplace factor and normalized descent characteristic factor have covariance ≤4|t| b p_j/√n; summing gives o(1), proving joint Poisson/Gaussian factorization, not merely marginal limits. The exact finite covariance identities are consistent with independence only asymptotically. The proof applies to uniformly random permutations/equivalent ranks of i.i.d. atomless observations, not general dependent data.

## originality

PASS

Best-of-knowledge original contribution assessed at statement/implication level against actual named published results, a relevant Resultary search and primary material; inaccessible plausible full text is recorded as risk rather than proof of novelty.

## value

PASS

A marked two-color Poisson point-process limit together with an asymptotically independent global Gaussian Eulerian statistic captures a natural rare-event/local-global decoupling not represented by classic scalar longest-run or descent-only limits. The factorial rare-window regime gives a motivated threshold and answers a natural joint distribution question, including the no-long-run probability times Gaussian CDF.

The dated certificate retains the supplied scientific assessment, sources and limitations.
