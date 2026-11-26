# Independent mathematical audit

## correctness

PASS

For the signed lag displacement D=(B-1)y-j on branch j, its positive density at x>0 away from branch breakpoints is (B-1-floor(Bx))/(B-1) on (0,1), by counting admissible j. The negative density is its reflection. Integrating to r gives [2(B-1-m)r+m(m+1)/B]/(B-1), m=floor(Br); substituting Br=m+v gives the asserted fractional-part expression. Stationarity and the 2(N-k) ordered pairs at lag k give the exact finite mean. After benchmark subtraction the scaled summand is exactly 1 for Br<=1. Above the threshold, subtracting F from the scaled summand yields r[u-v(1-v)-u^2]/[u^2(u-r)], bounded in magnitude by 2r/u for r<=1/2. With q=floor(log_b(1/r)), the geometric tail beyond q gives the phase, with total approximation error O_b(r+b^{-(N-q)}); the triangular weight costs q(q+1)/(2N)+O_b((q+1)/N). F is continuous including integers; on (m,m+1) it has derivative 2m(u-m-1)/u^3. This is O(u^-2) and tends to zero from the left at positive integers. The composed summands are globally Lipschitz on [0,1] with summable bounds 2b log(b)b^-j, validating their summed right derivative at phase zero; the endpoint match follows by reindexing and F(1)=1. Consequently the phase is continuous and nonconstant. The supplied checker was inspected, not run; the general identities and remainder were independently derived.

## originality

PASS

The supported distinct result is the exact Euclidean one-orbit mean together with its logarithmic coefficient and nonconstant phase. The strongest actual catalog match treats the same expanding map but has exactly the independent mean in the circular metric and a nontrivial variance, not this mean. Relevant primary results for interval maps and periodized lacunary sequences are first-order and do not determine this endpoint correction.

## value

PASS

The exact iid benchmark separates the interval boundary effect from bulk first-order Poisson behavior. The dominant contribution comes from a logarithmically growing range of deterministic lags, while the next scale retains the phase of the lag threshold. That phase is a nonconstant observable mean correction, not a changed convention for pair ordering or the iid subtraction, and it distinguishes this interval model from its circular counterpart.

The dated certificate retains the supplied scientific assessment, sources and limitations.
