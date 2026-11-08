# Independent mathematical audit

## correctness

PASS

The actual Lobatto IIIC [0/2] stability function is R(z)=(1-z+z^2/2)^(-1). For transient shift, coefficients are q^k sin((k+1)theta)/(A_h sin theta), q=cos theta-sin theta, theta=arctan(1/(1+h)). Absorption probabilities are q^k[cos(k theta)+sin(k theta)]. All signs are nonnegative iff (n-1)theta<=3pi/4; the first k crossing necessarily lies between 3pi/4 and pi, giving a negative entry. Therefore all h>=0 work for n<=4, and for n>=5 precisely h=0 or h>=cot(3pi/[4(n-1)])-1. A bounded exact-rational inverse test corroborated representative matrix coefficients, row sums and signs.

## originality

PASS

Qualified best-of-knowledge originality: Loczi-Ketcheson arXiv:1303.6651 develops radii of absolute monotonicity in general; Higueras-Ketcheson-Kocsis arXiv:1505.04024 studies perturbed Runge-Kutta monotonicity. Published [2/2] Pade birth-chain positivity examples use a different rational function. None of the examined statements yields the particular [0/2] all-n threshold. Risk: Unindexed numerical-analysis or older SSP literature might independently derive the same [0/2] absorbing-chain positivity window.

## value

PASS

Markov positivity of a fixed numerical integrator on a natural absorbing process is a meaningful exact invariant. The n=4 to n=5 transition, sharp angular threshold and large-step recovery reveal a counterintuitive structural phenomenon while not claiming improved accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
