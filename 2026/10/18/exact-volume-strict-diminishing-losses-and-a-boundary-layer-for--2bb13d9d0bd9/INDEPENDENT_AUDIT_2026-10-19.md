# Independent mathematical audit

## correctness

PASS

The dual anchored Lipschitz ball for n leaves with k hub distances t∈[1/2,1] and mutual leaf distance one has |x_i|≤t for i≤k, ≤1 otherwise, and total coordinate range including 0 ≤1. Partition by the unique negative minimum −s and the all-nonnegative sector; conditional short-spoke width w_t(s)=min(t,s)+min(t,1−s), and each long spoke has width 1. The exact integral t^k + k∫_0^t w_t(s)^(k−1)ds +(n−k)∫_0^1w_t(s)^k ds evaluates to V=1+n(2t−1)+2(n−k)(1−t^(k+1))/(k+1), including t=1/2 and t=1. Its k-increment differences are 2∫_t^1s^k((n−k)(1−s)+s)ds>0 and second differences 2∫_t^1s^k(1−s)((n−k)−(n−k−2)s)ds>0 for t<1. When k/n→θ>0 the integral term has limit 2(1−θ)/θ at t=1/2 and vanishes after normalization at t>1/2, yielding V(1/2+c/n)→2c+2/θ−1. Independent exact Ehrhart differences for n=3,k=2,t=1 and t=1/2 reproduce volume 4 and 19/12. Finite enumeration supplements this direct analytic derivation.

## originality

PASS

Best-of-knowledge priority conclusion, not exhaustive novelty certification. The k=1 formula and k=n formula are explicitly previously known boundary specializations. The 2≤k≤n−1 mixed profile is not a direct substitution in either endpoint; relative volume coordinates and p=real are specified to avoid different volume normalizations. The previously computed endpoint and facet statements do not algebraically imply the positive-k mixed volume, the strict second discrete difference, or the two-parameter limit; independent three-region integration is required.

## value

PASS

Dual Lipschitz-ball volume is a natural invariant of finite pointed metrics. The mixed equal-spoke contraction family interpolates genuinely beyond known one-edge and full-star endpoints and reveals both strict diminishing interaction costs and a dimension-critical 1/n boundary layer, which is a meaningful asymptotic structural finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
