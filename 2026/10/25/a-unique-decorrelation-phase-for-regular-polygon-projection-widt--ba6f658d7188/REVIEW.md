# Independent mathematical audit

## correctness

PASS

PASS. For the regular n-gon the width is the support function of its difference body. For even n the difference body is a regular n-gon of circumradius 2R; for odd n it is a regular 2n-gon of circumradius 2R cos(pi/(2n)). On each cosine chamber of half-width a=pi/N, the normalized width is rho cos(theta). Independently integrating the two overlap pieces for angular lag 0<=d<=a reproduces the exact mixed moment [(2a-d)cos d+d cos(2a-d)+sin(2a-d)+sin d]/(4a). Subtracting (sin a/a)^2 gives covariance. Differentiation yields rho^2[d sin(2a-d)-(2a-d)sin d]/(4a), strictly negative because sinc decreases over the positive interval and 0<d<a. The mean-zero period integral of covariance and strict decrease imply the centered half-period endpoint is negative, and the positive zero-lag variance gives one and only one interior sign reversal. The centered chamber expansion converges uniformly to F(x)=1/6-x^2/2 on [-1,1]; its autocorrelation is H(q)=[8-15q^2(2-q)^2]/360. Thus the asymptotic zero fraction is 1-sqrt(1-sqrt(8/15)), and the lag-half-period correlation tends to -7/8. The stated odd/even radius normalizations, n=3 boundary, and n->infinity quantifiers were checked; no finite regression substitutes for the analytic strict decrease.

## originality

PASS

PASS, best of knowledge. Akiyama–Kamae (2022) provides a general edge-projection second-moment kernel and discusses width deviation and regular polygons, a substantial prior ingredient. Its inspected Theorem 1 and regular-polygon conclusions do not state the prescribed angular-lag centered covariance zero, strict one-crossing, or the explicit universal quartic limit. The indexed geometric width results compute chord-width products or marginal width laws and cannot directly imply a joint lag covariance. The geometric reduction uses known tools; the complete all-n sign and asymptotic result is the candidate new contribution, with an explicit risk that the edge-projection kernel could yield an earlier unpublished derivation.

## value

PASS

PASS. Width in two nearby sampled directions is a natural angular-tomography observable. The theorem determines exactly how their centered covariance changes from positive to negative for every regular side count, then shows a nontrivial universal quartic shape, one root and maximal anticorrelation of -7/8. This is a global, motivated classification rather than a zero-lag variance recomputation or an arbitrary finite numerical case. The precise fraction may serve as an analytic benchmark for angular width sampling; no claims outside regular polygons are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
