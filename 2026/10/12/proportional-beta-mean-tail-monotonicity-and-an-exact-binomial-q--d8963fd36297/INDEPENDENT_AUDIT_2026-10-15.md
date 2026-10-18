# Independent mathematical audit

## correctness

PASS

Reconstructed the exact theorem on p in (0,1), tau>0: the inverse branches of Bernoulli KL divergence give u(s),v(s), r=v/u in ((1-p)/p,1) for p>1/2. Differentiating R_r(w)=r^2(A+Bw-w^2)/(A-Brw-r^2w^2) yields r^2(1+r)J_r/(...)^2; J_r>=J_{(1-p)/p}=B(1-p)(p-w)^2/p>0. The ratio of equal-energy displacements decreases strictly, and the log-odds beta density is an e^{-tau s} tilt of branch weights with decreasing conditional k(s)=r/(1+r). Monotone likelihood-ratio of the energy tilt proves the strict CDF trend. Escape to infinite energy for tau down to 0 and concentration at zero for tau to infinity give limits 1-p and 1/2. Reflecting p handles p<1/2. The beta-binomial identity with parameters ((n-1)t,t), cutoff (n-1)/n, gives the exact discrete strictness and infimum; n=2 is symmetric. Independently checked the symbolic derivative identity using SymPy and several rational binomial sequences using Fraction; finite tests supplement the analytic argument.

## originality

PASS

Best-of-knowledge novelty is the proportional-two-shape beta mean-tail theorem and its exact finite-n binomial quantile conjecture consequence, not monotonicity in one beta coordinate.

## value

PASS

This proves a precise, previously formulated finite-agent matroid-rank quantile threshold and a strict distributional monotonicity theorem across all real positive beta shape scales. The relevance follows directly from a named conjecture; it is neither a numerical-only bound nor a routine one-parameter parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
