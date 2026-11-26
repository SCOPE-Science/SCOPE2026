# Independent mathematical audit

## correctness

PASS

One confined interval multiplies excess conditional variance by c=e^(-2 kappa tau); the Brownian stochastic integral from the past is finite because its variance is bounded by a geometric sum of cycles of finite mean. Contraction kills initial conditions. In the stationary off phase the excess in time units is A+sum_{j>=1}c^j T_j, with renewal-age density P(T>a)/E T and independent past cycles. In the on phase it is e^(-2 kappa U) sum_{j>=0}c^j T_j, since constant on duration does not size-bias T_0. Both A and T have log-tail rate theta^(-p) at speed w^p. For p<=1 subadditivity bounds the pth power by a geometric sum of T_j^p (or A^p for j=0); the product of moment generating functions is finite below theta^(-p), and the positive-probability off phase with A>w gives the matching lower bound. For p>1, as an independent check of the infinite-series upper bound, put q=p/(p-1). For any 0<r<q, Holder bounds (sum c^j Y_j)^p by (1-c^r)^(-(p-1)) sum c^[p(1-r/q)j]Y_j^p, with Y_0=A or T_0 and remaining Y_j=T_j. The exponentially weighted sum on the right has a finite exponential moment at every parameter below theta^(-p) before the prefactor; the log-product tails converge by summability. Taking r up to q yields the claimed upper rate. Constraining the first N+1 variables to exceed w c^[j/(p-1)]/sum_{i=0}^N c^(iq) in the off phase gives the reverse bound on sending N to infinity. The corresponding finite-history optima are strictly costlier at p>1. Given the variance, centered Gaussian tails at W=z x^[2/(p+1)] have log-rate 1/(4Dz); upper and lower bounds agree by splitting the scaled W into a compact grid plus the two endpoints. Optimizing a_p z^p+1/(4Dz) recovers the spatial constant and Rayleigh specialization; symmetry gives the left tail. This proof treats fixed positive parameters, includes p=1, and neither requires simulated rare tails nor gives a density prefactor.

## originality

PASS

The semi-Markov switching/variance representation and classical Weibull-sum calculus are not original here. The supported distinct result is the exact fixed-positive-confinement model-specific stationary Weibull rate, with the geometric-history factor and shape-one boundary. The closest inspected finite-sum theorem does not cover the infinite variance series; the closest switching theorem treats different tails. No broader priority claim is made for the abstract probability steps.

## value

PASS

The logarithmic coefficient quantifies actual remote spatial risk, which stationary moments and the conditional Gaussian description cannot determine. The threshold shows when finite harmonic recovery enters the leading spatial rate and when it does not, and the full coefficient measures that effect. It is a natural quantitative distinction across the whole shape range, not a fit or selected parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
