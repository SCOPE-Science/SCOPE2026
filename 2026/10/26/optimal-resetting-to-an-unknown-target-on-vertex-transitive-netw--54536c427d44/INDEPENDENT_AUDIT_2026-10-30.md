# Independent mathematical audit

## correctness

PASS

Reconstructed strong-Markov first-hit resolvent Q_ij=E_i[z^T_j]Q_jj, with target detection at time zero, and geometric-reset renewal including a unit-duration relocation step. This yields H_j=(c/R_j-1)/gamma with R=rho Q, c=Q_jj and sum_j R_j=1/gamma. Strict harmonic-mean inequality, invertibility of Q and min_j R_j<=1/(n gamma) establish unique uniform law for both objectives; expansion gives exact regret c gamma n sum_j (R_j-mu)^2/R_j. Vertex transitivity ensures constant diagonal, symmetry real eigenvalues, so optimal uniform mean is sum_{k>=2}(1-z lambda_k)^-1 and F is strictly convex since sum lambda_k^2>0. Loopless trace implies Fprime(0)=-1. For cycles direct csc²/csc⁴ identities give Fprime(1)=(n²-1)(n²-19)/180; its sign yields n>=5, C5 radical follows two doubled eigenvalues, and uniform Taylor remainder for z=O(1/n) yields gamma*=1-1/n+O(n^-2) and min mean n-1-1/(2n)+O(n^-2). Independently checked cycle derivative n=3..29 and exact resolvent penalty at n=3,5,7 (not a substitute for proof).

## originality

PASS

The spectral Kemeny formula, strict convexity and optimal-rate derivative test are already in Michelitsch et al. 2024 and González et al. 2021; they are credited as premises. Evans–Majumdar 2011 even optimized reset distributions for *distributed targets* in continuous one-dimensional diffusion; this is a very relevant general analogy, but not a theorem for finite vertex-transitive graphs with the current uniform-prior minimax statement. The asserted additional mathematical claim is the exact all-rho strict heterogeneity penalty and simultaneous mean/worst-target optimality at uniform target weighting, plus cycle n=5 cutoff, C5 radical and large-cycle optimal-rate expansion. Strong analogy leaves notable originality risk; inspected sources do not mathematically imply all those propositions in their stated domains.

## value

PASS

A hidden target with an explicitly uniform prior models an information-limited search, distinct from choosing targets by the unknown reset chain stationary law. The strict exact heterogeneity penalty quantifies the full cost of nonuniform relocation; the simultaneous worst-case fairness result and integer cycle phase boundary with exact C5 optimum give actionable natural classifications, not merely a reproduced spectral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
