# Independent mathematical audit

## correctness

PASS

For nodes (-a,0,a), 0<a<=1, Lebesgue [-1,1] and exact unaugmented Gaussian kernel k=e^{-ε²(x−y)²}, the 3×3 kernel solve yields endpoint u=(B−qC)/(1−q²)²>0 and center v=[C(1+q⁴)−2qB]/(1−q²)². An integral S_a(t)=∫_0^1 e^{-tx²}(cosh(2ta²)−cosh(2tax))dx has the same sign as v. Its positive [0,a] and negative [a,1] portions satisfy a strict ratio monotonicity: H_t(s)=s coth(ts) obeys 0<H′<1, yielding positive pairwise derivative for 0<x<a<y<1. Small-t S_a(t)/t²→2a²(a²−1/3); large-t v>0, proving unique crossing for a<1/√3 and all-positive otherwise, including equality. Polynomial (1−x²/a²)² witnesses negative quadrature when v<0. Independently solved the linear system/integrals for 25 (a,t) cases and recovered ε*(1/2)=1.07860960325714381286869398262.

## originality

PASS

Compared statements and implications against the actual primary-source sections listed below, Resultary semantic retrieval and targeted literature searches. A sampled non-match alone is not proof of novelty; prior general frameworks/derivability are credited with material-specific residual risks.

## value

PASS

The threshold a=1/√3 and unique shape-parameter sign transition give a sharp, naturally motivated positive-weight frontier for the simplest nontrivial unaugmented Gaussian kernel quadrature. Negative weights destroy positivity preservation despite exact kernel integration; this explicit design criterion is valuable beyond an isolated root calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
