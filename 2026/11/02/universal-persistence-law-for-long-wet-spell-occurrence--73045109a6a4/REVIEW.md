# Independent mathematical audit

## correctness

PASS

For symmetric stationary two-state transition with 0<q<1, wet marginal 1/2 and k>=3, the k-state killed Markov run-length matrix is primitive and strictly substochastic; hence S_(n,k)^(1/n)->λ=ρ(Q_k(q)). Its positive Perron recurrence gives λ^m(λ-q)=(1-q)^2 Σ_(j=0)^(m-1)q^j λ^(m-1-j), m=k-1. With r=q/λ in (0,1), t=(1-q)/λ=(1-r)/sqrt(1-r^m), the bijection q=r/(r+t) turns minimization of λ into maximization of h(r)=r+t. Derivative sign is m-2r Σ_(j=0)^(m-1)r^j/(1+sqrt(1-r^m)); the second term is strictly increasing 0->2m, so there is a unique interior maximizer. Large m gives m(1-r_m)<=2 and excludes c_m=-m log r_m->0; every positive subsequential limit solves c=2(1-e^-c)/(1+sqrt(1-e^-c)); its RHS/c decreases uniquely from 2 to 0. Thus m(1-q_k)->c/sqrt(1-e^-c)=0.75430126082451 and m(1-λ_k)->c(1/sqrt(1-e^-c)-1)=0.29755327337930. Independent k=2,3,4,6,10 killed-matrix spectral radii matched numerical scalar optima incl k=3 q=.73953495. Long-window limit precedes k->infinity; not fixed-window optimization.

## originality

PASS

Fu–Wang–Lou 2003 full longest-run Markov-chain study derives exact survival probabilities and spectral large-deviation rates with *fixed transition parameters*. The present claim optimizes over q in the symmetric equal-wet-marginal subfamily, proves uniqueness for every k>=3, and obtains two nontrivial large-k constants. A previously established k=2 optimization is explicitly excluded as original. Other waiting-time/run-statistics work (Koutras, Samarova, Lou, Caskey, Weiss) may contain a comparable parameter optimization; their incomplete full-text accessibility is documented. Current best-of-knowledge original conditional on that residual risk.

## value

PASS

For a Markov wet/dry generator with fixed marginal wet probability, changing persistence alters the hazard of ever seeing a long spell. The unique optimized long-window exponential rate for each k and universal asymptotic scaling solve a clear natural stochastic design/extreme-run question. It separates wet fraction from serial correlation and provides reusable exact benchmarks; not an empirical weather prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
