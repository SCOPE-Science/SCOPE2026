# Independent mathematical audit

## correctness

PASS

For n>=2, 0<p<1, mean mu=np, k=floor(mu), U is two-level with A=(n+1-2mu+k)/((k+1)(n+1)) for 0..k and C=(2mu-k)/((n-k)(n+1)) for k+1..n. Direct sums normalize and give E U=mu. Binomial PMF b_j increases on 0..k, decreases on k+1..n, so d_j=U_j-b_j decreases on left and increases on right; zero total and first moment plus nonidentity implies d_0,d_n>0 and a central negative run. The affine-secant argument gives Eφ(U)>=Eφ(B) for all convex φ; strictly convex gives strict, and every stoploss threshold t in (0,n) has strict inequality from positive tails. Mixing weights interpolate affinely and endpoints n=1, p=0,1 are exact identities.

## originality

PASS

Groß introduced the identical two-level distribution and established heavier variance, not all stop-loss inequalities or convex order; classical two-crossing conditions provide the proof mechanism, which is credited. Searches of corresponding Resultary records, prior binomial-vs-uniform and relative log-concave literature did not locate this parameterized strict comparison.

## value

PASS

Full convex order is a substantial distributional strengthening of mere variance ordering for a natural new mean-matched heavy-tail alternative: it simultaneously governs every convex loss and precise stop-loss actuarial comparisons across all mixing weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
