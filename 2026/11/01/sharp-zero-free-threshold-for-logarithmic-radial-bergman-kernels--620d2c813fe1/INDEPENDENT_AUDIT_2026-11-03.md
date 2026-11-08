# Independent mathematical audit

## correctness

PASS

For every real alpha>-1 put p=alpha+1; normalized monomial moments are Gamma(p)/(n+1)^p, so K=F_p(u)/Gamma(p), F_p=Σ(n+1)^p u^n. For 0<p<1 the Bernstein representation of x^p gives (1-u)^2F_p as an integral of (1-a)(1-u)/(1-au) with strictly positive real part for |u|<1. For 1<p<2 write p=1+q: the Bernstein representation gives integrand 1−a((1-u)/(1-au))², with its modulus correction <1 because a max|...|²=4a/(1+a)²<1. Endpoints p=1,2 are rational positive-real expressions. For 2<p<4 Abel continuation at u=-1 gives F_p(-1)=(1-2^{p+1})ζ(-p)<0, hence negative real root. For p>=4 test r=2^{1-p}, decreasing alternating terms n>=2 and exact upper U(p)<=U(4)=-335/4096<0, so again a root. Checked U(4) exactly with rational arithmetic. Numerical root tests only corroborate all-real-parameter analytic proof.

## originality

PASS

Classical integer p>=3 Eulerian/polylog zeros are prior art (Yamamori), and Perälä gives radial kernel zeros for other weights. Full real p>0 dichotomy at 2 plus positive-real certificate for logarithmic weights is mathematically more general than integer cases and differs from two published SCOPE power-deficit and Euclidean-distance radial families; no inspected theorem implies it directly.

## value

PASS

Exact Lu Qi-Keng zero-free transition and a constructive half-plane bound for a natural singular/vanishing one-parameter radial Bergman space, including all noninteger p. A complete classification of a natural analytic family can be useful independently of a downstream application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
