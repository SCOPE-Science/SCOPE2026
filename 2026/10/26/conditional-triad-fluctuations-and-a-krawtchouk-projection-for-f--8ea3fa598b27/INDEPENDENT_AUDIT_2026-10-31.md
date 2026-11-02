# Independent mathematical audit

## correctness

PASS

Fix v with outdegree k and reveal its full N=n-1 star. Through-v cyclic triangles count a Binomial(k(N-k),1/2); avoiding-v triangles have marginal cyclicity 1/4 and pairwise-independent indicators even when sharing one edge. Pairwise covariance between through-v and avoiding-v sums is zero because for any shared edge the avoiding-v triangle cyclicity conditional on its direction is always 1/4. This establishes E[C|S_v=k]=binom(N,3)/4+k(N-k)/2 and Var(C|S_v=k)=3binom(N,3)/16+k(N-k)/4. Regression against f(S_v), summing over v, gives Cov(C,sum f(S_v))=-n E[((2X-N)^2-N)f(X)]/8. The K_2 identity and binomial orthogonality isolate degree two; zero k require N square >=4. Independently enumerated all 8,64,1024,32768 tournament orientations at n=3,4,5,6 and verified exact rational conditional means, variances and all frequency covariances. This finite check supports but is not the proof for all n.

## originality

PASS

Deterministic identity expressing cyclic-triad count by scores and classical binomial/Krawtchouk orthogonality are explicitly prior mathematical ingredients. The assessed contribution is the fully conditional finite-n variance and entire additive-score covariance functional (including square-order exact zero cases). Inspected primary random-tournament literature focuses on score laws and asymptotic circular-triad fluctuations; historical Kendall–Babington Smith full text inaccessible and retained as priority risk.

## value

PASS

The exact conditional variance of triad intransitivity given one vertex score and its degree-two projection to arbitrary score statistics are natural finite-sample statistics for fair paired comparisons. The square-order zero-covariance classification and universal sign pattern provide precise additional structure beyond a known mean/score identity; no broad downstream theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
