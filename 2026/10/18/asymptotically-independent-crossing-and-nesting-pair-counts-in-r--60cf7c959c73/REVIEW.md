# Independent mathematical audit

## correctness

PASS

Uniformly sorted independent random endpoint pairs produce a uniform perfect matching. Conditional projection on chord endpoints a<b gives gC=2(b-a)(1-b+a), gN=(b-a)^2+2a(1-b). Independently computed exact integrals E gC=E gN=1/3, E gC²=E gN²=2/15, E gCgN=1/9. Thus shared-chord cross covariances vanish and same-pair C*N=0 gives covariance -binom(n,2)/9; within type shared covariances 1/45 yield stated variance. Bounded order-two kernels have degenerate Hoeffding remainders of variance O(n²), so multivariate iid CLT for projection yields independent Gaussian fluctuations. Directly enumerated 3,15,105,945 matchings for n=2..5 and checked covariance. Marginal CLT alone does not prove joint asymptotic independence.

## originality

PASS

Best-of-knowledge novelty concerns the explicitly stated combined theorem, not its classical components; direct comparisons and material-reading limitations are recorded. Full finite distribution prior implies moments computationally, so exact covariance as a stand-alone novelty would be weak. It does NOT logically state the joint limit without additional asymptotic inference; orthogonal one-chord projections and multivariate CLT establish a quantitatively distinct fluctuation theorem.

## value

PASS

The natural joint second-order geometry of two-chord crossing and nesting counts exhibits a nontrivial cancellation: negative O(n²) finite covariance but asymptotically independent O(n^{3/2}) Gaussian fluctuations. The exact covariance plus joint CLT provide a statistical distinction between finite dependence and fluctuation-scale independence, not an arbitrary tiny finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
