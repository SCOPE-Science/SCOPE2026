# Independent mathematical audit

## correctness

PASS

The theorem compares uncorrected unit-step BE and BDF2 fractional-integral coefficients for integrable nonnegative densities w(1-t)~c t^alpha, alpha>-1. For fixed beta, BDF2 weights equal BE coefficients a_{n-k}(beta) averaged over negative-binomial p_k(beta) of mean beta/2 and geometric tails. The uniform coefficient ratio a_{n-k}/a_n=1+(1-beta)k/n+O((1-beta)(k+k^2)/n^2) for k<=n/4 yields difference a_n*beta(1-beta)/(2n)+smaller remainder. Gamma-ratio and endpoint Laplace integration then establish e_n~c Gamma(alpha+1)/(log n)^(alpha+1), d_n~c Gamma(alpha+2)/(2n(log n)^(alpha+2)) positive eventually. Integrability of d_n and z->1 generating-function difference bounded by (1/2)int w(beta)(1-z)^(1-beta) imply sum d_n=0 by dominated Abel limit. Integral tail gives prefix deficit ~e_n/2. In the uniform-order case independent numerical quadrature at n=50,100,1000 found positive differences and increasing scaled n log(n)^2 d_n approx 0.193,0.221,0.292 (approaching 0.5 very slowly); not substituted for asymptotic proof. Endpoint beta=1 atom excluded by density assumption; d0<0 follows from w positive near 1.

## originality

PASS

Best-of-knowledge PASS with access caveat: earlier distributed-order CQ stability and error theory is foundational but the inspected available statements do not establish this all-power-endpoint coefficientwise difference, cancellation, and half-prefix law. Full relevant recent paper inaccessible; historical priority risk explicitly preserved.

## value

PASS

Distributed-order CQ kernels have long logarithmic tails important for memory truncation. The exact redistribution of coefficient mass when replacing BE by BDF2, zero net difference and universal half-prefix deficit furnish precise quantitative benchmarks; these are not merely error-order statements or unsupported assertions of PDE accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
