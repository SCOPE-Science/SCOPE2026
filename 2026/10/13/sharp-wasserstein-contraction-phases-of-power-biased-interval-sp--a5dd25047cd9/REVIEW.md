# Independent mathematical audit

## correctness

PASS

On each compact interior state segment the CDF at each threshold is continuous and piecewise C^1 in the state, with a uniformly bounded derivative. Integrating its absolute derivative gives the global upper bound by the supremal local L1 speed, and dominated convergence gives the reverse bound via infinitesimal pairs. Independently, let q=x^p/(x^p+(1-x)^p). Twice the speed is |xq'-q|+|1-q-(1-x)q'|. For p>1 and x<=1/2, q<=x and xq'/q=p(1-q)/(1-x)>1. When the second signed term is nonnegative the speed doubled is 1-2q-(1-2x)q'<=1; otherwise it is q'-1. With x=(1+tanh u)/2, q=(1+tanh(pu))/2, hence q'=p cosh^2(u)/cosh^2(pu)<=p. Reflection covers the other half. The left-end limit is 1/2 and the center speed is (p-1)/2. For 0<p<1, q'~p x^(p-1), which forces unbounded speed at the left endpoint. For p=0 and p=1 direct substitution gives 1/2 and 0. This proves the exact constants, including p=2 and p=3, with no need for endpoint states or numerical extrapolation. The frozen check_w1.py is a finite regression check, not the proof; it was inspected but not executed.

## originality

PASS

The distinct contribution is the full sharp one-step Euclidean W1 coefficient and its contraction thresholds for the existing kernel. The p=1 case is already immediate from the defining density; neither that case nor the prior stationary-law theorem is credited as new.

## value

PASS

This sharp coefficient is a natural invariant of an existing Markov family and tells when a one-step Euclidean coupling argument can work. It gives both the exact loss of strict contraction at p=3 and a uniformly mixing phase with no finite one-step Wasserstein Lipschitz bound, neither of which the prior mixing theorem supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
