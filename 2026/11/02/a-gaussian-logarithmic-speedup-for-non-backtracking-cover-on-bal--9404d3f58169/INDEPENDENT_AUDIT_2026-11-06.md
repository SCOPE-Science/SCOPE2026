# Independent mathematical audit

## correctness

PASS

Alternating iid parity streams for simple walk on K_{n,n} and separately erasing each stream’s consecutive equal symbols produce exact nonbacktracking marginal chains. Conditional on retained chain, discarded repeats are independent geometric-failure counts; the two stream completion times are iid sum_{k=1}^{n-1} Geom(k/(n-1)). Inclusion-exclusion yields the claimed F_n and H_n products. Poisson factorial moments give max(K_A,K_B)/n-log n=>G+log2, while conditional geometric CLT gives repeats (R_*-log n)/sqrt(log n)=>Z, asymptotically independent of max K. The bound sup P(K_n=j)<=1/(n-1) makes late-winner switching probability negligible and gives o(1) correction to the expected saving, proving 2log n+2gamma+2log2+o(1). Independently verified exact stage-CDF identities by rational Markov dynamic programming on n=3,4 with and without loops. The coupling-specific law is explicitly differentiated from coupling-independent mean difference.

## originality

PASS

Single-stream complete-graph coupon-collector Gumbel laws are classical. The primary nonbacktracking cover-time paper by Matsuo et al. treats random regular and configuration-model network means, rather than paired stream compression for K_{n,n}. The submitted two-scale joint Gaussian-Gumbel independence, conditional repetition counts and constant-order mean correction are not stated in that text; searches of related published findings identified discounted biclique hitting/cover invariants rather than this paired law.

## value

PASS

The exact coupling gives an unusually strong comparison: pathwise monotonicity, an intrinsic logarithmic mean improvement, and a microscopic Gaussian independent of the macroscopic cover-time Gumbel law. This quantifies how removing immediate backtracks changes exploration of a natural dense bipartite network without affecting the leading 2nlog n cover scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
